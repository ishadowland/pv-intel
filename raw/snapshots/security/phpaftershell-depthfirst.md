<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://depthfirst.com/research/phpaftershell -->
<!-- fetched_at: 2026-11-24 07:12:41 -->
<!-- sha256: 53c11eb35c991a4b62089952f8ad76f600fa3a4e7700f141af816cf0c5f9efef -->

phpAfterShell: From Interrupted Session Writes to Remote Code Execution | depthfirst

phpAfterShell: From Interrupted Session Writes to Remote Code Execution

Published on Nov 19, 2026
Yuhang Wu

Security Researcher

TL;DR: PHP can update a file-backed session while parsing an unauthenticated multipart request, even before the target script begins execution. We discovered reliable methods to interrupt the file operation during session upload-progress updates, allowing us to splice the prefix of one valid session with the suffix of another. A subsequent session operation treats the corrupted data as legitimate server-side state, giving attackers control over session values and the ability to trigger object deserialization. By chaining this primitive with a memory-corruption in a PHP-native class, we achieved remote code execution. We reported this vulnerability to the PHP team, and it was assigned CVE-2026-126714 , with a critical CVSS score of 9.2 .

php2shell drew attention to an unusual part of PHP’s request lifecycle: while PHP is still parsing an unauthenticated multipart request, before the target script even begins, the upload-progress callback can open and decode a file-backed Session. The original exploit took advantage of objects becoming active during this callback, and PHP addressed it by restricting class resolution during RFC1867 upload-progress updates.

When we started looking into the patched implementation, we were curious about what happened to the Session data beyond the deserialization step. Even with the new restrictions in place, the callback still reads the existing Session, adds upload-progress state, serializes the whole thing, and writes it back to the same file. In other words, while the patch changed which objects could be created in memory, the underlying file update behavior remained untouched. This raised a different question: what actually happens to the Session file if the PHP worker dies in the middle of an update?

To answer that, we had to look beyond the PHP code itself. PHP serializes the updated Session into a valid value, but the file handler writes it to the existing inode using pwrite() and ftruncate() . These operations are not atomic, and an interrupted update doesn’t necessarily leave the file in either its old or new state. Depending on where the interruption happens, part of the new Session may already have been written while bytes from the previous Session remain on disk. The result can be a Session file containing the prefix of the new serialized data and the tail of the old one. Both original Sessions are valid, and surprisingly, their combination can also be valid, but with a completely different meaning.

This is where things got interesting. By carefully choosing the length fields in the new prefix, an attacker can make PHP’s Session decoder interpret leftover bytes that were previously just part of an ordinary string as separate Session entries and serialized objects. Nothing needs to be deserialized during the upload-progress callback itself. The attacker only needs to leave the right bytes on disk and wait for the application to call session_start() , at which point PHP reads the modified Session and deserializes those objects.

This gave us a new exploitation path that the php2shell patch did not address. The patch prevented objects from becoming active during the RFC1867 callback, but it couldn’t prevent an interrupted file update from leaving behind a different, valid Session. What began as a closer look at a PHP patch eventually led us through the Session serialization format, the file handler’s write behavior, and all the way down to how the kernel handles interrupted buffered writes.

Before the Script Begins

Most PHP developers meet file uploads through $_FILES . By the time application code reads that array, PHP has already parsed the multipart body. The work happens during request startup in the RFC1867 parser.

RFC1867 emits events as it encounters form fields, file headers, file data, and the closing boundary. The Session extension subscribes to those events when upload progress is enabled. A field named PHP_SESSION_UPLOAD_PROGRESS supplies a progress token. PHP then resolves the request’s Session ID, initializes the Session module, and writes progress information before index.php executes its first line:

php_rinit_session ( 0 );
PS (id) = zend_string_copy ( Z_STR (progress -> sid ));
...
php_session_rfc1867_update (progress, 0 );
At the start of a file part, the callback constructs a Session value containing byte counters and file metadata. The multipart field name and filename become strings inside that value:

upload_progress_<token> => [
"content_length" => ...,
"bytes_processed" => ...,
"files" => [[
"field_name" => <multipart field name>,
"name" => <multipart filename>,
"tmp_name" => ...,
"error" => ...
]]
]
This gave us the first reachability result. An application does not need an upload controller or a call to session_start() on the multipart endpoint. PHP itself is the Session writer. A request only needs to reach the Web SAPI as multipart/form-data with upload progress enabled.

Two Request Paths, One Inode

The callback assigns the selected SID to PS(id) . With session.save_handler=files , the upload request and a later application request resolve the same path of <session.save_path>/sess_<SID>

One SID, one handler, and one file Upload and application requests share the same Session module and file. One SID, one handler, and one file Upload request multipart/form-data PHPSESSID = S RFC1867, before the script Application request session_start() PHPSESSID = S ordinary route execution Session module PS(id) = S save_handler = files serializer = php save_path = /tmp same module state for both paths /tmp/sess_S one live inode username|s:5:"alice"; application state cart|a:1:{...} application state upload_progress_x|a:5:{...} RFC1867 inserts this record cleanup deletes it from this same file The whole stream is decoded and rewritten progress update session read/write lock + read serialize + write
The first writer is RFC1867. It opens the file during multipart parsing, reads the current Session, adds or removes the progress key, serializes the result, and writes it back. The second writer is the application. When a later route calls session_start() , it opens the same file and decodes it into $_SESSION .

The default php Session serializer is used on both paths. Upload completion also removes the progress entry and flushes the whole Session again. Each progress update therefore operates on the complete file rather than an isolated progress record.

PHP takes an exclusive flock() while a worker owns the Session. That prevents cooperating workers from writing at the same time. It does not roll back bytes. If the worker disappears, the kernel releases the lock and leaves whatever the inode contains at that moment.

This shifted the question. Concurrency between writers was not required to mix two values. A single worker could modify part of the live inode and die before PHP finished the update.

A Session File Is a Parser Input

The file handler does not store a PHP array as one opaque blob. With session.serialize_handler=php , it concatenates records in this form:

session_key | serialized_value
The decoder scans to | for the key, then hands the following bytes to PHP’s unserializer. Once that value ends, the next byte starts another Session key. There is no file-level length, checksum, generation number, or commit marker.

Session record = key + “|” + serialized value username | s: 5 :"alice"; roles | a: 1 :{i:0;s:5:"admin";} red = session delimiter · blue = parser-controlled number N; null no payload b:1; boolean 0 or 1 i:42; integer signed decimal zend_long d:3.14; double also NAN, INF, -INF s: 5 :"alice"; byte string length moves the parser cursor S: n :"..."; legacy escaped string accepted; deprecated on decode a: 2 :{key value ...} array count = key/value pairs O: 8 :"stdClass": 1 :{...} object + properties class lookup and reconstruction C: n :"Class": m :{payload} custom object payload class and payload byte lengths E: n :"Enum:Case"; enum case resolves an enum class and case R: 2 ; zval alias reference to prior value slot #2 r: 2 ; object back-reference reuse prior object slot #2 A changed length, element count, or reference ID changes the next
parser state.
A small Session may look like this:

username|s:5:"alice";
roles|a:1:{i:0;s:5:"admin";}
profile|O:8:"stdClass":1:{s:5:"theme";s:4:"dark";}
The productions become more significant as the parser moves from simple values to structured state:

N , b , i , and d create scalar values.

s carries a byte length. That length decides where parsing resumes.

a carries an element count and recursively decodes its children.

O , C , and E enter class reconstruction, custom serialization, or enum handling.

R and r connect the new value to something decoded earlier in the stream.

The length fields supplied the missing piece. Bytes can be syntactically active at one offset and inert at another. A serialized object placed inside a sufficiently long string is only data. Change the length in a prefix, and the same bytes can become the beginning of the next top-level record.

This produced a concrete target. We did not need arbitrary file contents. We needed a prefix from replacement state R to move the decoder onto a chosen tail from carrier state C .

Following the Update into the Kernel

The file handler writes the serialized replacement into the existing Session inode with pwrite() at offset zero:

n = pwrite (data -> fd , ZSTR_VAL (val), ZSTR_LEN (val), 0 );
if (n != ZSTR_LEN (val)) {
return FAILURE;
}
At the PHP level, this looks like one operation. At the kernel boundary, a large buffered write may copy many pages into the page cache before the syscall returns. If the process dies during that copy, the inode can already contain a prefix of the new buffer. PHP never receives a short-write result because there is no process left to receive it.

Our first hypothesis used PHP’s execution timeout. It was attractive because the timer is remotely controllable through parser work. Tracing showed why the early experiments were inconsistent. On our Linux test systems, the timeout became actionable after the buffered pwrite() returned. The file contained all of R , not a partial prefix.

That failure narrowed the problem. To interrupt the copy itself, the worker had to disappear inside the syscall. An OOM kill supplied that behavior for one family of releases. A separate source change created another family where a complete pwrite() was enough because truncation happened in a later syscall.

PHP timeout enter pwrite() ~5.96 MiB buffer kernel copies the complete buffer return → handler timer expires Cgroup OOM · SIGKILL enter pwrite() prefix copied retained old tail SIGKILL
Timeout delivery and an uncatchable OOM kill interact differently with a buffered pwrite() .

The root cause stayed the same in both cases. PHP updated the live inode in place and treated completion of several filesystem operations as one logical Session commit.

Two Ways to Keep the Old Tail

Let C be the carrier Session already stored on disk and R the replacement PHP wants to commit. The order of pwrite() and ftruncate() creates two exploitable states.

User space → syscall → page cache → live inode replacement R ZSTR_VAL(val) pwrite(fd, R, |R|, 0) kernel copies pages into the file return n n == |R| ? ftruncate() separate syscall Outcomes observed by the next worker Normal return n = |R| → optional ftruncate completes R (Complete new file) Short return after partial copy 0 < n < |R| → PHP returns FAILURE the handler checks n after the inode has changed; no rollback follows R[0:n] C[n:] Fatal signal during pwrite SIGKILL / fatal worker death → no return to PHP fd closes and flock releases; page-cache writes already made remain R[0:k] C[k:] Fatal signal before ftruncate pwrite returns |R| → worker dies → ftruncate never runs the complete shorter value is followed by the old physical tail R C[|R|:]
Overview: the two interruption points produce different combinations of replacement R and carrier C.

Variant A: The Write Stops Partway

In the first ordering, PHP truncates before writing only when the replacement is shorter than the size cached when the file was opened:

if ( ZSTR_LEN (val) < data -> st_size) {
php_ignore_value ( ftruncate (data->fd, 0 ));
}

n = pwrite (data -> fd , ZSTR_VAL (val), ZSTR_LEN (val), 0 );
if (n != ZSTR_LEN (val)) {
return FAILURE;
}
If R is at least as long as C , the old inode remains in place when pwrite() begins. A worker killed after copying k bytes leaves:

R[0:k] || C[k:]
1. Carrier C · fully valid progress prefix + long length dormant bytes inside a serialized string natural suffix 2. Replacement R · also valid new prefix + shorter inner length remaining replacement bytes · total length ≥ carrier worker dies during pwrite() 3. Physical file after interruption R[0:k] (new bytes already copied) C[k:] (retained carrier bytes)
Variant A: termination during pwrite() leaves a prefix of replacement R joined to the retained carrier C tail.

The useful insight was that k did not need to be one exact offset. We shaped the serialized grammar so that a range of partial prefixes reached the same retained record. This converted a narrow kernel event into a wider parser acceptance interval.

Variant B: The Write Finishes Before Truncation

A later ordering writes first and truncates the old tail only after pwrite() reports success:

n = pwrite (data -> fd , ZSTR_VAL (val), ZSTR_LEN (val), 0 );
if (n != ZSTR_LEN (val)) {
return FAILURE;
}

if ( ZSTR_LEN (val) < data -> st_size) {
php_ignore_value ( ftruncate (data->fd, ZSTR_LEN (val)));
}
When R is shorter than C , a complete write temporarily creates:

R || C[|R|:]
The next syscall removes the tail. If the worker terminates after pwrite() and before ftruncate() , the temporary state becomes durable.

1. Carrier C · longer file carrier prefix dormant session grammar old suffix 2. Replacement R · complete pwrite pwrite(fd, R, |R|, 0) = |R| R (complete new serialized value) C[|R|:] (old tail still present) pwrite() returns worker terminates ftruncate(fd, |R|) not reached 3. File read by the next request R C[|R|:]
Variant B: a complete shorter pwrite() leaves the carrier C tail until ftruncate() .

This changes the exploitation problem. Variant A needs termination during a buffered copy. Variant B needs termination between two syscalls. The second window is still small, but it no longer depends on a partial kernel copy.

Commit c2b02f24dff separates these orderings in the affected source history.

Building a Third Valid Session

The carrier Session C contains the target record inside a length-delimited string. Parsed on its own, the object bytes are inert. The replacement R changes the grammar immediately before the retained tail. After an interrupted update, the decoder reaches the tail as a new top-level Session key.

C: [ordinary records][string length -------- object bytes as data --------]
R: [replacement prefix][shorter string length]
mix:[replacement prefix] [object bytes as a Session record]
Before · carrier decode upload_progress_x|a:{ ... s: LONG :" ... evil|O:8:"stdClass" ... "; ... } partial overwrite After · session_start() upload_progress_x|a:{ ... s: SHORT :"...";} evil|O:8:"stdClass":...
Both source states are generated by PHP from ordinary multipart fields. Neither source file is malformed. The malformed state exists only at the storage boundary, where bytes from the two serialized values meet.

The public proof uses a harmless object:

evil|O:8:"stdClass":1:{s:5:"proof";s:5:"pwned";}
A later route contains only normal Session code:

<? php
session_start ();
var_dump ($_SESSION[ 'evil' ] ?? null );
If the splice misses early, the consumer sees the carrier state. If it misses late, it sees the replacement. A hit creates $_SESSION['evil'] as a real object. Those three outcomes gave the exploit a stronger oracle than socket timing alone.

Finding the Windows over HTTP

A fixed delay worked on one machine and failed on another. CPU speed was only part of the reason. Apache scheduling, page-cache state, allocator pressure, multipart parsing, and the exact moment a worker crossed its limit all moved the boundary.

We stopped treating the interruption point as a constant. The controller treated it as a moving boundary that could be measured through application state.

Each candidate uses a fresh SID and three requests against the same sess_<SID> file:

A carrier POST writes C through upload progress.

A replacement POST asks the same callback to write R .

A consumer GET calls session_start() and classifies the resulting Session.

One SID · three HTTP requests · one session-file oracle Cookie: PHPSESSID=S → <save_path>/sess_S 1 · Carrier POST 2 · Replacement POST 3 · Consumer GET Upload progress writes carrier C controlled string ... evil|O:... ... The declared string length keeps the inner grammar dormant. file = C Same SID and upload-progress key Variant A · worker dies inside pwrite(R) Variant B · worker dies after pwrite(R), before ftruncate() file = R prefix || C tail Independent application request session_start(); echo $_SESSION['evil'][0]; PHP reads the physical file through its ordinary Session decoder. HTTP 200 · PWN! How the controller moves the termination phase Variant A · progress within pwrite() Held HTTP requests approach the memcg limit. Synchronized lanes move OOM/SIGKILL across a ~5.96 MiB copy. accepted k range: R[0:k] || C[k:] Variant B · progress between syscalls Legal multipart bracket depth consumes request CPU. Depth moves hard-timeout delivery across write then truncate. target phase: pwrite() ✓ ftruncate() ✗ The third request is the oracle EARLY · C remains consumer → MISS TARGET · R prefix || C tail consumer → PWN! LATE · complete R consumer → MISS
Remote calibration: carrier C, replacement R, and the consumer oracle across both write windows.

The HTTP connection tells us whether a worker completed or disappeared. The consumer tells us what happened to the file. Together they distinguish an early termination, a late termination, and a splice that crossed the parser acceptance interval.

Calibrating Variant A

For the partial-write family, held multipart requests bring the Apache cgroup close to its memory boundary. The carrier and replacement keep their important grammar at a fixed geometry. Two replacement lanes cross a barrier together so that an allocation in one worker can push another worker over the boundary while it is writing.

The controller adjusts pressure at two scales. Coarse slots move in 2 MB steps. A tunable request covers the smaller interval between them. Complete responses and disconnected sockets feed a rolling history. Stable observations move the coarse allocation count. Mixed observations are fitted with a recency-weighted logistic model, then sampled near the estimated transition at 32 KiB offsets.

The model handles a mismatch between two kinds of state. The memory limit is discrete from the attacker’s perspective, while the amount already committed by Apache and PHP is noisy. Re-estimating the transition after each observation is faster than scanning the full range again. Dead pressure connections are replaced so the controller keeps approximately the same background state.

Variant A · adaptive memory-pressure calibration Learn the moving OOM boundary, then place a worker inside pwrite() Payload geometry stays fixed. Only background pressure and one fine-grained allocation change. 1 · Build pressure 2 · Synchronize the replacement Coarse held requests 2 MiB / slot Fine request 100 KiB … 4 MiB lane 0 · write R lane 1 · write R barrier pwrite(R) cross cgroup limit 3 · Observe the file through HTTP transport complete / disconnect consumer request session_start() state label EARLY: C · TARGET: R-prefix || C-tail · LATE: R 4 · Update the controller rolling history recent outcomes weighted logistic fit P(disconnect | pressure) transition estimate coarse slot + fine offset next probe estimate ± 32 KiB
Variant A calibration loop: coarse pressure, a fine allocation, synchronized replacement lanes, and a recency-weighted boundary estimate.

Kernel probes showed partial prefixes near 2 MiB, 4 MiB, and 5.5 MiB. The grammar accepts a span around those regions. In a fresh HTTP run, the promoted object appeared on attempt 11.

Calibrating Variant B

The post-write window needs a different control variable. A legal multipart field name containing repeated bracket notation makes PHP spend CPU in request parsing before it flushes upload progress. The field name never enters the carrier record, so its depth changes timing without changing the target grammar.

Shallow inputs terminate before the replacement is written. Deep inputs pass the truncate. Between them lies the state where pwrite() has completed and ftruncate() has not.

The full depth range is not perfectly monotonic. We first locate a small region where outcomes are locally ordered. A particle filter then tracks the boundary. Its state includes drift and an outlier component because neighboring requests can land on different Apache scheduling histories. Surprise-driven updates widen the search after an unexpected result. Systematic resampling keeps candidates concentrated around the most informative depths.

Variant B · tracking the post-write window Use parser depth as a control axis, then learn where pwrite() ends The field name changes request CPU work without changing the carrier or replacement grammar. 1 · Locate a locally ordered phase axis multipart bracket depth shallow → deep EARLY · C remains termination before replacement TARGET R || C[|R|:] LATE · complete R ftruncate already reached First bracket a neighborhood with both early and late observations. Global depth does not need to be monotonic. 2 · One adaptive probe posterior quantile choose depth d RFC1867 parser work [ x] repeated d times worker termination before / between / after consumer oracle C · mixed · R 3 · Update the particle population particles near the estimated transition boundary weight observations drift + outlier mixture systematic resampling next informative depth
Variant B calibration loop: bracket a local phase axis, probe one depth, classify the Session, and update the particle population.

This approach raised the simulated 24-attempt hit rate from 52.8% to 88.4%. A fresh HTTP run reached the target state in ten attempts after one coarse rebase. The controller learns the current host instead of carrying a timing constant from the development machine.

The Next Request Changes the Meaning of the Bytes

The interrupted upload leaves the mixed file in session.save_path . The next request presents the same SID and calls session_start() . PHP reads the file as trusted server-side Session state and runs the normal decoder.

The earlier php2shell remediation restricts class resolution while the upload-progress callback is active. On patched builds, an object handled during that callback is transported as __PHP_Incomplete_Class . Its serialized representation still reaches the file handler. Once RFC1867 has finished, the restriction is gone. A later session_start() resolves the promoted record through the ordinary class path.

The splice is useful before objects enter the picture. Scalars and arrays can replace identity, authorization, CSRF, password-reset, cart, or workflow state before application code performs its access checks. An object adds a path into magic methods and native decoders.

At this point the storage bug becomes an arbitrary deserialization primitive. The application contributes only its normal use of Sessions.

From a Native Object to RCE

PHP ships internal classes that reconstruct native state from serialized input. SPL containers, iterators, date and time objects, random engines, and extension-owned wrappers cross from PHP values into C structures. Their decoders manipulate zend_object , HashTable , references, native pointers, property tables, and length fields.

We audited that surface as a separate problem. The Session file could carry an object. The remaining question was how much power PHP’s own classes exposed when an attacker controlled its serialized representation.

That audit produced a chain using native PHP decoders. A memory-corruption vulnerability supplies the first primitive. Later stages disclose the addresses required by the worker and redirect an internal call. The object promoted from the Session tail enters the chain during session_start() and ends in code execution inside the PHP process.

The decoder and final heap layout remain reserved for coordinated disclosure. The full chain does not depend on an application-defined gadget class.

Session deserialization chain Multipart HTTP chosen SID Hybrid session prefix || tail session_start() native object Native bug memory corruption RCE Apache worker
Full-chain Demonstration

Download the full-chain demonstration .

End-to-end HTTP demonstration: multipart upload → retained Session state → ordinary session_start() → PHP-native deserialization → code execution.

On Exploitation and Remediation in the AI Era

Over the years, PHP security research has produced all kinds of interesting tricks, often far more memorable than the vulnerabilities themselves. Deserialization techniques evolved from userland gadget chains to PHP-native objects and unexpected entry points like PHAR metadata. Researchers have found clever ways around open_basedir and disable_functions , while combinations of php://filter and character encoding tricks turned seemingly limited LFI vulnerabilities into RCE. Many of these techniques also came out of CTFs, where unusual constraints pushed researchers to explore obscure PHP behaviors and combine things that weren’t originally meant to work together. Much of this work happened long before AI became part of security research, through manual code review, experimentation, and a lot of trial and error. What really gets researchers excited has never been another CVE number or a single bug. It’s those clever tricks that connect things nobody thought were related, or make something that seemed impossible actually work.

AI changes the pace of that work. A model can hold more of the codebase in view at once, keep several competing ideas alive, and make it practical to run far more experiments than you would write harnesses for by hand. On this bug, fixed timing and pressure values kept failing whenever worker scheduling or memory state drifted; treating every HTTP attempt as an observation, estimating where the boundary had moved, and choosing the next request from that estimate only came together after iterating through multiple failed models and kernel probes that would have taken weeks to build manually.

Patching has become faster too, and this creates a new problem. AI can follow a known exploit, add a guard, and write a regression test in a short time. That patch may stop the exploit while leaving the deeper bug in place.

The php2shell patch is a good example. It stopped objects from becoming active during the RFC1867 callback. It did not make the Session file update safe when a worker died. The bytes could remain on disk and become active later, when the application called session_start() . The original exploit stopped working, but the underlying problem was still there.

At depthfirst, we do offensive research with a defensive goal: knowing whether the software we protect is genuinely safe after a patch lands, where a broken PoC is only the first check. When both finding a bug and shipping a fix can happen quickly, reviewing the patch deserves the same care as building the exploit, making sure remediation removes the reason the bug was possible rather than just blocking the first path that reached it.

Affected Versions

The source history divides into three groups. Earlier releases use ordinary object semantics during RFC1867. The first remediation changes object transport and retains the truncate-before-write ordering. Later branches move truncation after the write, which changes the interruption window without removing the retained-tail primitive.

Version range Family Session behavior Vulnerable
8.2.35 – current 8.2 , 8.3.36 – current 8.3 , 8.4.27 , 8.5.12 Variant A Incomplete-object transport with the pre-write truncate ordering Yes
8.4.28RC1 – current 8.4 , 8.5.13RC1 – current 8.5 , 8.6.0RC4 – current 8.6 , master Variant B Incomplete-object transport with the post-write truncate ordering Yes
8.2.0 – 8.2.34 , 8.3.0 – 8.3.35 , 8.4.0 – 8.4.26 , 8.5.0 – 8.5.11 , 8.6.0RC1 – RC3 Original RFC1867 uses ordinary object semantics Yes
Official 7.4 , 8.0 , and 8.1 EOL mitigation branches Disabled The upload-progress callback returns without opening the Session No

The ranges describe official php-src trees as of November 17, 2026. The last row refers to the dedicated EOL mitigation branches. Older unpatched 7.4, 8.0, and 8.1 builds retain the original path. Downstream packages may carry the relevant changes without changing PHP_VERSION .

Share this post

Secure on depthfirst

Get a demo

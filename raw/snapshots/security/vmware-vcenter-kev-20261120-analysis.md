<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.worldprogramming.org/posts/a-session-key-from-a-timestamp-inside-vcenter-cve-2026-123890-and-the-chain-to-full-directory-theft-avpbt3 -->
<!-- fetched_at: 2026-11-24 07:14:50 -->
<!-- sha256: 8024ccbe1b732c18f1608b5ed4715ff0c9ed15ef8c903fd79b2dbea94ce98fbd -->

A Session Key From a Timestamp: Inside vCenter CVE-2026-123890 and the Chain to Full Directory Theft — WPS

requestAnimationFrame(() => {
this.dragging = false;
this.offset = 0;
}));
},
canSwipeFrom(target) {
for (let el = target; el && el !== this.$el; el = el.parentElement) {
if (el.matches('input, textarea, select, iframe, [contenteditable]')) return false;
if (el.scrollWidth > el.clientWidth && getComputedStyle(el).overflowX !== 'visible') return false;
}
return true;
},
start(event) {
this.tracking = event.touches.length === 1 && this.canSwipeFrom(event.target);
this.startX = event.touches[0].clientX;
this.startY = event.touches[0].clientY;
this.dragging = this.tracking && ! this.reducedMotion;
},
move(event) {
if (! this.dragging) return;

const dx = event.touches[0].clientX - this.startX;
const dy = event.touches[0].clientY - this.startY;

if (Math.abs(dx) 0 ? this.$el.dataset.nextUrl : this.$el.dataset.previousUrl;
this.offset = Math.max(-120, Math.min(120, dx * (hasTarget ? 0.45 : 0.15)));
},
end(event) {
const wasTracking = this.tracking;
this.tracking = false;
this.dragging = false;

if (! wasTracking) return;

const dx = event.changedTouches[0].clientX - this.startX;
const dy = event.changedTouches[0].clientY - this.startY;
const url = dx > 0 ? this.$el.dataset.nextUrl : this.$el.dataset.previousUrl;

if (! url || Math.abs(dx) 0 ? 'next' : 'previous');
this.offset = dx > 0 ? 400 : -400;
setTimeout(() => { window.location.href = url; }, 180);
},
cancel() {
this.tracking = false;
this.dragging = false;
this.offset = 0;
},
}"
:style="{
transform: offset ? 'translateX(' + offset + 'px)' : '',
opacity: offset ? Math.max(0, 1 - Math.abs(offset) / 450) : '',
transition: dragging ? 'none' : 'transform 180ms ease-out, opacity 180ms ease-out',
}"
@touchstart.passive="start($event)"
@touchmove.passive="move($event)"
@touchend.passive="end($event)"
@touchcancel.passive="cancel()"
@pageshow.window="if ($event.persisted) cancel()">

Web Development

A Session Key From a Timestamp: Inside vCenter CVE-2026-123890 and the Chain to Full Directory Theft

ARMORY CASTLE used this SRP-6a authentication bypass from early September. CISA put it in KEV a day after disclosure and gave federal agencies until 23 November.

Dev.to

·
2026-11-21

0

0

Share

copied = false, 2000)"
class="block w-full px-4 py-2 text-start text-sm leading-5 text-body transition duration-150 ease-in-out hover:bg-surface-2 hover:text-content focus:bg-surface-2 focus:outline-none">
Copy link

X
LinkedIn
Facebook
Threads
Reddit
Hacker News

copied = false, 2000)"
class="inline-flex items-center rounded-full px-2.5 py-1.5 text-muted hover:bg-surface-2 hover:text-content"
aria-label="Copy link"
title="Copy link">

5.9K
views

This is the English edition of a Korean report published on 21 November 2026. The original is at dohyeontech.github.io .

On 20 November 2026, CISA added four entries to the KEV catalog in one day: an authentication bypass in VMware vCenter (CVE-2026-123890), XML-RPC deserialization in Apache Roller (CVE-2026-129448), JNDI injection in SAP NetWeaver Enterprise Portal (CVE-2025-42884), and hardcoded credentials in the Cisco Expressway cluster database (CVE-2026-76466). All four carry a federal remediation deadline of 23 November 2026 . The catalog version is 2026.11.20 , 1,790 entries total; it stood at 1,786 the day before. The four entries are exactly that difference.

The weight sits on vCenter. Broadcom published VMSA-2026-0009.1 on 19 November with five CVEs bundled together (CVSSv3 6.7 to 9.8), and CVE-2026-123890 is the 9.8 Critical. The problem is not the score. It is the timing. Google Threat Intelligence Group and Mandiant said in an analysis the same day that a suspected China-nexus actor they track as ARMORY CASTLE had been using this defect as a zero-day since early September 2026 . Broadcom's advisory does not state exploitation, and Mandiant is credited as the reporter. That puts more than two months between the patch and the first known intrusion.

Two operational constraints come attached. Broadcom lists the workaround as "None," and Rapid7 confirmed the fix cannot be applied through vCenter Quick Patch. vCenter 8.0 U3m and 9.0.2.0200 introduce a "Back-in-Time" restriction that blocks upgrading to VCF 9.1.1, so organizations mid-upgrade need the FAQ and the compatibility matrix before touching anything. And 7.0 left general support on 2 October 2025, which means without an extended support contract there is no path to a fix at all (Censys's summary).

This report takes vCenter apart at the level of sources and logs, then puts the other three entries in working order at the bottom.

1. A 72-hour clock: KEV one day after disclosure, deadline three days later

Line the events up and the place where defenders lose time becomes visible.

Time (UTC)
Event
Evidence

2026-07-13 09:21
BONESAW build timestamp
Go binary metadata (Mandiant)

2026-07-29
CVE-2026-59309 disclosed (same vmdir family, different defect)
VMSA-2026-0006

early Sep 2026
ARMORY CASTLE uses CVE-2026-123890 to breach vCenter
forensic evidence (Mandiant)

2026-11-19
VMSA-2026-0009.1 published, Mandiant credited as reporter
Broadcom

2026-11-20 17:48
KEV 2026.11.20 published, four entries
CISA

2026-11-23
federal remediation deadline
KEV dueDate

The binary Mandiant recovered was built sixteen days before CVE-2026-59309 became public. Go build metadata can be altered before compilation, so that timestamp alone does not settle anything — but it leaves the shape of an actor who already had tooling for this defect in mid-July. Worth reading next to it: organizations that patched the earlier defect in the same family (CVE-2026-59309, published 29 July) were still breached in September. Broadcom's FAQ states plainly that CVE-2026-123890 is "a new and distinct issue," and that the earlier patch does not close it.

A KEV entry carries less information than a vendor advisory. It is a judgment that a vulnerability was used in the wild, not an account of how. Across these four entries the gap is unusually wide. For vCenter there are attacker tools, command lines and indicators. For the SAP entry there is a patch notice and the listing itself, and nothing public beyond that.

2. What collapsed on top of SRP-6a: a session key without the password

vCenter SSO is one trust boundary. vmdird (VMware Directory Service) holds the directory for the vsphere.local domain in an LMDB file at /storage/db/vmware-vmdir/data.mdb . The Security Token Service signs SAML assertions, and vSphere Client and the APIs trust those tokens. So one session as [email protected] is enough to walk off with the whole directory database. Mandiant identifies vmdirdbcp , an RPC interface on vmdird , as the path used for exactly that.

The defect sits in the rpc_srp_verifier service, a DCE/RPC interface listening on TCP 2012. SRP-6a is a protocol that performs mutual authentication without ever putting the password on the wire. The structure explains why this matters.

setup: N, g (group parameters), k = H(N, g)
enrol: x = H(s, P), v = g^x mod N (s = salt, P = password)
server: b <- random, B = k·v + g^b mod N
client: a <- random, A = g^a mod N, u = H(A, B)
client: S = (B - k·g^x)^(a + u·x) mod N
server: S = (A · v^u)^b mod N
both: K = H(S) <- the session's symmetric key

Enter fullscreen mode

Exit fullscreen mode

The safety of that design rests on two values: b , which only the server knows, and the verifier v the server stores, derived from the password. An attacker who does not know P needs both b and v at once to compute S , and one of them leaking is enough to open the session key K . This is why SRP is described as authentication that does not store the password — and why a single leaked value ends the conversation regardless of how long the password is.

That is as far as Mandiant's public wording goes. CVE-2026-123890, they write, exploits predictable UUIDv1 timestamp generation in the SRP authentication interface to expose the SRP session key without a password. A UUIDv1 consists of a 60-bit timestamp (100-nanosecond units since 15 October 1582), a clock sequence, and a node identifier. Identifiers minted in the same time window are effectively predictable, and if the generation order can be narrowed the candidate space collapses fast. A predictable identifier used as a secret on an authentication boundary is not a secret.

Which value is derived from the UUIDv1, which of b / v / K it opens, and which function the patch touched are all undisclosed. There is no patch diff and no reproduction code (Censys notes no public PoC for this CVE exists). Read the CWE-288 classification — authentication bypass through an alternate path or channel — together with "exposes the session key," and the shape is not that the normal path was tricked. It is that a different entry point into the same service hands the key over. Past that point I am inferring. What is established is narrower and sufficient: an attacker who can reach 2012/tcp over the network could obtain an authenticated session as [email protected] with no credentials, and from that session call the vmdirdbcp RPC to retrieve files.

One more property matters, and it is the least comfortable one for detection. The bypass does not end at an authentication. The session it yields is an ordinary administrator session, so everything that follows is written into the audit logs as work an administrator did.

3. BONESAW: how an authentication bypass becomes directory theft

The tool Mandiant recovered, BONESAW (internal name vcenter-db-teamcheck-go , executed from /tmp/123 ), is written in Go and carries build traces of a Windows development environment ( E:/CodeFiles/VulnScan/Vcenter/go_teamcheck/ ). The csa subcommand is the core. It creates an SSO administrator account from a small set of arguments.

csa -h target vCenter or vim25 SOAP endpoint (required)
-u name of the new SSO admin account (required)
-p password for that account (required)
-lu existing local admin UPN for vmdird bridge auth (default [email protected] )
-d tenant/domain (default vsphere.local)
-mdb-path path to an existing data.mdb (skips remote download)
-check-version verify version and connectivity before running
-auto-d auto-discover the SSO tenant

Enter fullscreen mode

Exit fullscreen mode

What it leaves on disk is the investigative trail. Under <output_root>/temp/extracted_tenant_signer_<host>/ you find anon_<host>_data.mdb (a copy of the looted /storage/db/vmware-vmdir/data.mdb ), *-tenantcredential-<N>.key.pem and .key.der (RSA private keys used to sign STS assertions), .leaf.pem and .chain.pem (signing certificates), and context.json with tenant and signer metadata.

Why those files are decisive is a property of vSphere's trust model. The directory database holds SSO users, groups, service accounts and each tenant's signing material. With the signing private key in hand an attacker no longer needs to pass authentication at all — they sign a SAML assertion for whichever user they want. The companion tool Mandiant observed, SAWSNAKE ( /tmp/sss ), does that job: a Go port of the public vcenter_saml_login.py that extracts the IdP signing key and trusted certificates from data.mdb , mints an assertion for an administrator and collects the session cookie. Golden SAML. Neither MFA nor password rotation obstructs this path.

Next comes the hypervisor layer. The actor sent PUT /rest/appliance/access/ssh to the VAMI API to switch on SSH for vCenter, logged in with a new local administrator account ( sps- @vsphere.local ), took the vCenter internal master symmetric key and the PostgreSQL credential file, and turned SSH back off immediately . That sequence is what makes detection hard. SSH being off now proves nothing. The answer is in the history recorded by the VAMI access log.

ESXi opens the same way. The actor attached to the ESXi Host Client as vpxuser , appended a public key to the root account's authorized_keys , came in over SSH, and read VMFS directly. The vmfs_browser.py invocation Mandiant captured pulls files out of a disk image without booting the guest operating system.

python vmfs_browser.py -d "/dev/disks/vml.<ID>:1" ls "<VM>-flat.vmdk:part2"
python vmfs_browser.py -d "/dev/disks/vml.<ID>:1" extract "<VM>-flat.vmdk:part4/Windows/NTDS" ./NTDS
python vmfs_browser.py -d "/dev/disks/vml.<ID>:1" extract "<VM>-flat.vmdk:part4/Windows/System32/config/SYSTEM" ./SYSTEM
python vmfs_browser.py -d "/dev/disks/vml.<ID>:1" extract "<VM>-flat.vmdk:part4/Windows/System32/config/SECURITY" ./

Enter fullscreen mode

Exit fullscreen mode

Pull NTDS.dit and the registry hives off a domain controller's disk and the entire AD credential store crosses over in effectively plaintext, whatever EDR is running inside the guest. This is the scene that shows why the virtualization management plane is not the endpoint of lateral movement but the bridgehead .

The implants are worth a look too. BEARBONES ( /tmp/dbr ) is a C backdoor built from an open-source Dropbear SSH server, modified so the svr_auth_password handler for SSH_MSG_USERAUTH_REQUEST skips the /etc/shadow check and accepts a client when the SHA-256 digest of the first 14 bytes of the supplied password matches a hardcoded value. The plaintext password as entered goes to the log. The banner is dressed up as SSH-2.0-pulsesecure_23345 , and host keys are read from /tmp rather than /etc/dropbear . LAZYBONES ( /usr/bin/vmtoolscs ) is a Go backdoor that uses a Slack channel for C2: messages encrypted with AES-256-CTR and Base64-encoded, polled with 150–450 seconds of jitter, handling four commands ( cmd , upload , download , sleep ), with a systemd unit restarting it every 50 minutes. If corporate egress policy allows slack.com , this traffic looks normal inside that policy.

4. Patching: the version matrix, and why the patch is not the end

Product
Affected
Fixed

VCF / vSphere Foundation vCenter
9.1.x
9.1.1.0200

VCF / vSphere Foundation vCenter
9.0.x
9.0.2.0200

vCenter Server
8.0
8.0 U3m

vCenter Server
7.0
No fix · Broadcom Support with an extended support contract

VCF vCenter
5.x
5.2.5 (asynchronous patch procedure, KB 88287)

Telco Cloud Platform / Infrastructure
3.0, 4.x, 5.0.x, 5.1.x, 5.2 / 3.0
8.0 U3m (KB463116)

Patches are cumulative, so anything newer than the table is fine. Three things need checking first. The Quick Patch route does not apply. The Back-in-Time restriction in 8.0 U3m and 9.0.2.0200 means environments mid-upgrade to VCF 9.1.1 have to reorder their steps. And while vCenter is updating, the management interface drops for a while although running VMs and container workloads keep going (Broadcom, Rapid7). vCenter instances run by third-party engineered systems or hosting providers have their patch level decided by that provider — keep them on the list and verify separately rather than assuming.

The reason the patch is not the end has already surfaced above. The actor created accounts, extracted keys, planted SSH public keys and switched SSH back off. A patch fixes code; it does not revoke access that was created. It is also why CISA attached BOD 26-04 forensic triage as a requirement to three of these four entries (vCenter, Roller, Cisco). SAP is the exception.

Narrowing the window before patching is a network-layer job. VCSA ships its own firewall, managed from the VAMI GUI, and Mandiant explicitly says not to trust it as a line of defense: there is no per-port granularity, so opening 443 for a backup server opens 22 and 5480 with it; the firewall is administered from VAMI on 5480, so an attacker who owns VAMI can turn it off; blocked attempts are not logged remotely; and it only handles inbound traffic, which leaves outbound C2 untouched. Mandiant's VCSA Hardening & Logging Tool goes around the GUI and writes a default-deny policy, an egress filter and a remote syslog bridge directly into Photon Linux's iptables . This is not a blanket recommendation to deploy it — testing and change control before production are mandatory. But the circular arrangement, an application managing the firewall of its own management plane, is worth fixing on its own merits, independent of this incident.

5. Hunting: what to check now

If vCenter has been reachable from an untrusted network since early September, check the following regardless of patch state. The order is account, then key, then trace, then reachability.

# 1) new SSO admin accounts - UI: Administration > Single Sign On > Users and Groups
# scan the log for account creation first (name seen in the intrusion: [email protected] )
grep -iE "add|create" /storage/log/vmware/vmdird/vmdird-syslog.log | grep -iE "vsphere\.local|sps-"

# 2) SSH enabled through VAMI - the switch is off now, the history is not
grep -E "PUT /rest/appliance/access/ssh" /var/log/vami/access.log

# 3) traces of the directory DB and signing material
ls -la /storage/db/vmware-vmdir/data.mdb
find / -name "tenantcredential-*.key.pem" 2 > /dev/null

# 4) ESXi root authorized keys and hidden directories (run on every host)
cat /etc/ssh/keys-root/authorized_keys
ls -la /vmfs/volumes/*/.a 2 > /dev/null

Enter fullscreen mode

Exit fullscreen mode

Step 4 has to run host by host. Mandiant confirmed a case where the actor created a hidden directory such as .a at the VMFS root to stage data. If authorized_keys contains keys added through normal administration, compare them against the change history.

Test reachability from the inside, not from outside. If those ports are open from an ordinary server segment rather than the management workstation, then compromising any server on that segment opens the same path.

VC = your.vcenter.internal
for p in 443 2012 5480 22 ; do nc -vz -w3 "$VC" "$p" ; done

Enter fullscreen mode

Exit fullscreen mode

Broadcom does not name ports, so blocking 2012 and calling it done is a mistake. The scanning Mandiant observed swept 443, 2012, 389, 5480 and 9080 together.

Network indicators belong in the same pass. Mandiant published eleven IPs suspected of being anonymization infrastructure. Any of them in a firewall log is a case on its own.

103.147.251.5 103.190.38.3 118.174.128.34 118.174.128.36
118.174.128.38 176.9.89.66 185.71.15.109 220.121.128.41
222.108.77.44 61.216.56.127 81.45.89.43

Enter fullscreen mode

Exit fullscreen mode

File indicators are ActiveSer.jsp (SLIMSAVAGE), u.jsp (CAGEMATCH), /tmp/123 (BONESAW), /tmp/sss (SAWSNAKE), /tmp/dbr (BEARBONES) and /usr/bin/vmtoolscs (LAZYBONES). A matching name is not proof of anything, but an executable binary sitting in /tmp on vCenter or a Linux appliance should be hashed and quarantined before anything else. Mandiant also published YARA rules for BONESAW, SAWSNAKE, BEARBONES, LAZYBONES and the web shells; if there is a YARA pipeline in-house, these drop straight into it.

6. The other three that landed the same day

2026-11-20 KEV entries, the remaining three

CVE-2026-129448 · Apache Roller (CVSS 9.8, CWE-502, confirmed exploitation)

Affects 4.0.0 through 6.1.4; 6.1.5 is vulnerable as well. Fixed after 6.1.6. The XML-RPC servlet ( /roller-services/xmlrpc ) is mapped unconditionally with enabledForExtensions=true , and SerializableParser.getResult() in xmlrpc-common 3.1.3 calls ObjectInputStream.readObject() during request parsing. Authentication happens after handler lookup, so deserialization runs first. Turning XML-RPC off in the admin UI does not stop it; set enabledForExtensions to false in WEB-INF/web.xml or remove the servlet mapping, then restart. The ASF states the defect is being exploited. Public exploitation research, however, shows the 9.8 is a parser-stage score and that actual RCE depends on the classpath: the readObject() guard in Roller's bundled commons-collections 3.2.2 blocks CC1 through CC7, and TemplatesImpl deserialization blocking in current JDKs shuts down CommonsBeanutils1. An attacker has to reach a JNDI chain in the Spring 5.3.39 line or an older runtime without those guards. Not "no bug" — rather, exploitability varies by environment. Pre-patch mitigation is those two configuration changes, and both need a restart.

CVE-2025-42884 · SAP NetWeaver Enterprise Portal (CVSS 6.5, CWE-943)

A defect from SAP note 3660969 on the 11 November 2025 patch day reached KEV a year later. The affected component is EP-PIN-APF-CAT , in EP-BASIS 7.50 and EP-RUNTIME 7.50. Unauthenticated injection of JNDI environment properties or lookup URLs reaches unintended JNDI providers, which leads to disclosure or tampering of server information. No availability impact. The fix hardens request parameter validation; SAP offers no workaround. The lowest score of the four, but a KEV listing is a judgment that it was used. No public description of exploitation exists, so prioritization should follow the listing, not the 6.5. Pre-patch, move the portal's external JNDI-triggering entry points behind an authenticating proxy.

CVE-2026-76466 · Cisco Expressway Series (CVSS 9.8, CWE-798, PoC then exploitation)

Only clustered Expressway-C and Expressway-E are affected; standalone deployments are not. Fixed in X15.5.20; X15.5.3 and earlier are vulnerable, and X14 and below require migration. The substance is Erlang distribution. The cluster database service opens an Erlang distribution listener on 4372/tcp, and a maintenance identity ( wombat@… ) and cookie are hardcoded identically across every installation. Even with TLS Verify Mode enabled for the cluster, no client certificate verification takes place, so an attacker who reaches that port can join the cluster and run root commands via rpc:call . Cisco's advisory, published 21 October, said no exploitation was known; after a public PoC ( dinosn/cve-2026-76466 ) appeared on 5 November, one Russian enterprise was breached (F6, 18 November), starting from two internet-exposed X15.5.3 appliances, pivoting to two internal cluster nodes, gaining root and then scanning SMB, SQL Server, WinRM and GitLab with Python scripts. Detection: nodeup,' [email protected] ' in Expressway's erlang.log , and files under /mnt/harddisk/i{0-9}{4}[a-zA-Z]?/*.py . Cisco says there is no workaround, but F6 recommends restricting 4371–4372/tcp to trusted cluster node IPs when immediate patching is impossible — not a vendor-backed mitigation, and worth weighing as such.

7. What it means that four went up on one day

These four span unrelated product families and severities from 6.5 to 9.8. They share one thing: in each, the authentication boundary itself is what fails . For vCenter it is the SRP session key; for Roller, an ordering in which the parser runs before authentication; for Cisco, one cookie shared by every installation; for SAP, a JNDI lookup target that is never validated. What follows a breach converges too. In the vCenter case the objective was signing keys and the directory database, in Roller it was the application process's privileges, in Expressway a root shell.

Two practical conclusions remain. Set the patch deadline from the KEV listing date, not the vendor advisory date. And keep a procedure, separate from patching, for revoking access that already exists. In this intrusion the actor turned SSH on and off, created accounts and planted authorized keys. Those traces live in logs and histories, not in current configuration. The hunting commands are above; they are written down in this order so the next cycle can reuse them.

Originally published in Korean at dohyeontech.github.io .

Read the original source

Next news

#Security
#Ai

Dev.to

Publisher

Originally by
Kim Dohyeon

0 Comments

Log in to join the conversation.

No comments yet. Be the first to share your thoughts.

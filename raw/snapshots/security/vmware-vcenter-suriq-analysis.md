<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://suriq.io/blog/vcenter-cve-2026-123890-sso-auth-bypass-exploited -->
<!-- fetched_at: 2026-11-24 07:12:50 -->
<!-- sha256: 0b90437f0dd3929e68756e1f43a56fb127a74e0481ee686329f21ffb1f33e171 -->

vCenter CVE-2026-123890: Exploited Auth Bypass, Patch Now

SURIQ . ×

Get Access

Home / Blog / Security news / Article
Blog · Security news
VMware vCenter CVE-2026-123890: Exploited Auth Bypass, Rotate SSO Keys
vCenter CVE-2026-123890 (CVSS 9.8) has been exploited since September by Armory Castle, according to Google and Mandiant.
By Noam Alum · Nov 22, 2026 · 08:11 UTC · Security news · 8 min read
Mitigate now ↓
Patching vCenter against CVE-2026-123890 closes the door a China-linked group called Armory Castle used, but it does not take back what the group carried out: single sign-on (SSO) signing material that can keep minting valid admin sessions after the fix is installed. CISA added the flaw to its Known Exploited Vulnerabilities (KEV) catalog on November 20 and gave federal agencies until November 23. Exploitation started in early September, so any vCenter that was reachable during those 11 weeks needs a compromise check, not only an update.

Broadcom shipped the fix on November 19 in VMSA-2026-0009 , which rates the advisory Critical. The vCenter bug scores 9.8 under CVSS 3.1 and sits in the VMware Directory Service, the identity store behind vCenter's SSO domain. The same day, Google Threat Intelligence Group and Mandiant attributed zero-day use of it to Armory Castle, the suspected state-backed espionage group previously tracked as UNC5221. Broadcom's own advisory, as BleepingComputer noted , does not itself confirm exploitation; the in-the-wild evidence comes from Mandiant's investigation and the KEV listing.

This is a separate bug from CVE-2026-59309, the July vCenter flaw we covered when VMSA-2026-0006 landed . Broadcom's advisory Q&A calls it a new and distinct issue, so a fleet patched in July is still exposed.

Which vCenter versions are exposed to CVE-2026-123890?

Every vCenter Server build older than the fixed release for its branch is exposed, standalone or inside VMware Cloud Foundation (VCF) and vSphere Foundation. Google's analysis says the exploit tool works against both the 7.x and 8.x appliances. Enhanced Linked Mode makes no difference. ESX hosts themselves are not affected by this CVE.

Product line Fixed in
vCenter 8.0 8.0 U3m
VCF / vSphere Foundation 9.1.x 9.1.1.0200
VCF / vSphere Foundation 9.0.x 9.0.2.0200
VMware Cloud Foundation 5.x 5.2.5
Telco Cloud Platform / Infrastructure vCenter 8.0 U3m
vCenter 7.0 Contact Broadcom support (extended support contracts)
Fixed versions as published with VMSA-2026-0009. ESX hosts are not affected by this CVE. Source: Broadcom, via The Hacker News and Broadcom's advisory Q&A.
In plain terms: vCenter 8.0 needs 8.0 U3m, VCF and vSphere Foundation 9.1.x need 9.1.1.0200, 9.0.x needs 9.0.2.0200, and VCF 5.x needs 5.2.5. vSphere 7 left general support in October 2025, so 7.0 shops get the fix only through Broadcom support on an extended contract. The same advisory also patches four lower-scored bugs in SDDC Manager and VMware Tools for Windows (CVE-2026-123891 through CVE-2026-123894), which are worth folding into the same change window.

Note the upgrade side effect Broadcom flags: 8.0 U3m and 9.0.2.0200 block a direct upgrade to VCF 9.1.1 because of its "back-in-time" rule. Plan the path before you start.

What the Directory Service flaw gives an attacker

Per Mandiant, the bug is a session key disclosure in the Secure Remote Password (SRP-6a) handshake that vCenter's directory service exposes over remote procedure calls on TCP port 2012. Anyone who can reach that port, with no credentials, can come away holding an authenticated session as [email protected] , the top account in the SSO domain.

Armory Castle wrapped this in a Go tool Mandiant named BONESAW. With that session it copied the directory's database file ( data.mdb ), took over the SAML security token service (STS) that signs vCenter login tokens, and created its own SSO administrator. A second tool, SAWSNAKE, used the stolen signing material to forge login tokens in the style of a Golden SAML attack, which also sidesteps multi-factor prompts.

Port 2012 is the detail to act on. It is a control channel that other vCenter and SSO nodes need, not something an administrator's laptop or a random internal server should ever reach. On a flat management network, nothing restricts it unless you configure an allowlist.

The second act of the BeyondTrust intrusion

We covered the first half of this campaign in October, when the same group was found exploiting BeyondTrust Remote Support CVE-2026-102764 . Mandiant's new report shows where that access led. From the compromised remote-support appliance the attackers moved to an internal Linux appliance with no endpoint agent, planted web shells named SLIMSAVAGE and CAGEMATCH, raised themselves to root, and scanned for VMware management ports 9080, 2012 and 5480.

Then came vCenter. After BONESAW, they ran a Dropbear-based backdoor called BEARBONES listening on TCP 33992, created an extra SSO admin named sps-<redacted>@vsphere.local , switched on SSH through the appliance management API, and pushed an SSH key into root on the ESXi hosts. From there they mounted datastore volumes and pulled data out of virtual machines, including Active Directory database files, according to the report.

CVE-2026-123890: from tool build to federal deadline 2026-07-13: BONESAW built. Early Sep 2026: Exploited in wild. 2026-10-15: BeyondTrust report. 2026-11-19: Patch and report. 2026-11-20: Added to KEV. 2026-11-23: Federal deadline. CVE-2026-123890: from tool build to federal deadline 2026-07-13 BONESAW built Early Sep 2026 Exploited in wild 2026-10-15 BeyondTrust report 2026-11-19 Patch and report 2026-11-20 Added to KEV 2026-11-23 Federal deadline Sources: Google Threat Intelligence Group and Mandiant; Broadcom VMSA-2026-0009; CISA KEV. The July 13 date is a build timestamp, which can be altered.
The timeline reads: BONESAW carries a build timestamp of July 13 (Google cautions that timestamps can be faked), exploitation is dated to early September, Mandiant published the BeyondTrust findings on October 15, Broadcom patched on November 19, CISA listed the CVE on November 20, and the federal deadline is November 23.

Two observations of our own. First, both zero-days in this campaign hit products whose whole job is to hand out privileged access: a remote-support gateway and the identity service of the hypervisor manager. Attackers are choosing systems where one bug converts directly into admin, skipping the noisy privilege-escalation step. Second, the pivot ran through appliances, a remote-support box, a Linux appliance and vCenter itself, which are exactly the machines that typically run no endpoint detection. That leaves appliance logs, not endpoint alerts, as the main place an intrusion like this shows up.

That fits a broader pattern in our own triage data. Of the 57,423 vulnerability items our intel desk evaluated over the past 90 days, 1,496 were authentication bypass or account takeover bugs, the third-largest class after cross-site scripting and command injection. Most of those bugs open one app. This one opens the management plane for every VM it controls.

Why a patched vCenter can still belong to someone else

The patch stops the next unauthenticated session key leak. It does nothing to what was already taken. If BONESAW ran against your appliance, assume three things survive the update:

The STS signing key. Tokens forged with a stolen signing key stay valid until that signing certificate is replaced. Updating the software does not replace it.

Rogue SSO administrators. An account the attacker created is a normal user to vCenter. It persists through upgrades.

Host-level footholds. An SSH key added to ESXi root, and any domain credentials lifted from Active Directory database files, are outside vCenter entirely.

So for any vCenter that was reachable on port 2012 from an untrusted segment since September, our recommendation is to treat "patched" and "clean" as two separate tasks: install the fix, then replace the STS signing certificate following Broadcom's documented procedure, reset the [email protected] password and service credentials, and review the SSO user list against what your team created. If ESXi or Active Directory data may have been touched, the incident scope widens to those systems too. We made the same argument for the ESXi logging bypass exploited in October : in virtualization intrusions, the update is where the response starts.

Check one vCenter appliance for these artifacts

Google's report lists file names, paths and behaviors rather than hashes. The block below turns the ones that live on disk into read-only checks you can run from the vCenter appliance shell and an ESXi shell. A hit is a reason to open an incident; a clean result is not proof, because files can be deleted and shell history cleared.

read-only checks on vCenter (VCSA shell) and ESXi, from Mandiant's Armory Castle findings
# vCenter appliance and internal Linux appliances
ls -l /bin/env /usr/bin/env
ls -la /tmp/gdb_file /tmp/rar /tmp/123.rar /tmp/123.key /tmp/sss /tmp/dbr /usr/bin/vmtoolscs 2> /dev/null
find / -xdev \( -name 'ActiveSer.jsp' -o -name 'u.jsp' \) 2> /dev/null
ss -tlnp | grep ':33992'
# SSO users named sps-*@vsphere.local that your team did not create
# VAMI API call PUT /rest/appliance/access/ssh in appliance access logs
# each ESXi host
cat /etc/ssh/keys-root/authorized_keys
ls -la /vmfs/volumes/ * /.a 2> /dev/null

An env binary showing the setuid bit (an s in its permissions) matches the root escalation Mandiant described on the Linux appliance, so run that check on any internal Linux appliance in the management network too, not only on vCenter. Google also published YARA rules for each malware family in the report, such as G_Hunting_Utility_BONESAW_2 , for teams that can scan appliance file systems.

If you cannot patch before November 23

Broadcom lists no official workaround, but says network restrictions reduce exposure. The highest-value one is narrow: allow TCP 2012 only between vCenter and SSO nodes, and restrict the appliance management port 5480, SSH on 22, and the web interface on 443 to a short list of admin jump hosts. Mandiant's report points to its VCSA hardening tool , which enforces those allowlists with iptables on the appliance itself and forwards shell commands and dropped connections to remote syslog, so a cleared .bash_history does not erase the record. Test any appliance firewall change in a maintenance window first; a wrong rule on port 2012 can disrupt SSO between vCenter nodes.

Also confirm SSH is disabled on the appliance unless someone is using it right now. In this intrusion, the attackers switched it on through the management API after taking admin.

Filter port 2012 like the admin interface it is

The lesson from this campaign is architectural. vCenter's identity service was reachable from an internal Linux box that had no business talking to it, and that single path turned a remote-support compromise into control of the virtual data center. Patch to the fixed build for your branch today, replace the signing certificate if the appliance was exposed since September, and put port 2012 behind the same allowlist you would give a domain controller. For teams building that kind of hunt into routine work, our threat hunting page covers how we approach it; related reading on edge appliances that stay compromised after patching is in our Ivanti Connect Secure coverage .

Topics Active exploitation

Stay close to the work.

Telegram for new posts and field notes. Discord and Slack for the community.

Join Telegram Join Discord Join Slack Follow on Facebook Follow on LinkedIn Follow on Bluesky
Frequently asked questions
What is CVE-2026-123890 in VMware vCenter?
CVE-2026-123890 is a CVSS 9.8 authentication bypass in the VMware Directory Service inside vCenter Server. An attacker who can reach TCP port 2012, with no credentials, can obtain an authenticated session as [email protected] . Broadcom fixed it on November 19, 2026 in VMSA-2026-0009.

Is CVE-2026-123890 being exploited?
Yes. Google Threat Intelligence Group and Mandiant report that the China-linked group Armory Castle exploited it as a zero-day from early September 2026. CISA added it to the Known Exploited Vulnerabilities catalog on November 20, 2026, with a federal remediation deadline of November 23.

Which vCenter version fixes CVE-2026-123890?
vCenter 8.0 is fixed in 8.0 U3m. VMware Cloud Foundation and vSphere Foundation are fixed in 9.1.1.0200 for 9.1.x, 9.0.2.0200 for 9.0.x, and 5.2.5 for Cloud Foundation 5.x. vCenter 7.0 customers on extended support should contact Broadcom support for the fix.

Does patching vCenter remove an attacker who already exploited it?
No. The patch blocks new exploitation but does not undo prior access. Signing keys stolen from the SAML token service keep forging valid logins until the signing certificate is replaced, and attacker-created SSO admin accounts and SSH keys on ESXi hosts persist through the update until someone removes them.

Is there a workaround for CVE-2026-123890?
Broadcom lists no official workaround, but says network restrictions reduce exposure. The most targeted control is allowing TCP port 2012 only between vCenter and SSO nodes, and limiting ports 5480, 22 and 443 to admin jump hosts. Test appliance firewall changes in a maintenance window first.

Are ESXi hosts affected by CVE-2026-123890?
No. Broadcom says ESX is not affected by this vulnerability, which lives in vCenter itself. However, in the Armory Castle intrusion the attackers used their vCenter access to add SSH keys to ESXi root accounts and copy data from datastores, so ESXi hosts managed by an exposed vCenter still need checking.

Keep reading
Related posts
Security news
Puppet CVE-2026-115731: Exploited Server RCE, Patch and Rotate the CA
Puppet CVE-2026-115731 is in CISA KEV. Fixed versions, why autosign makes it unauthenticated, and why a stolen CA key survives the patch.
Noam Alum · Nov 19, 2026
Security news
Oracle Java CVE-2026-114820: eMudhra CA Trust Flaw, Patch Now
Oracle Security Alert CVE-2026-114820 (CVSS 9.1) removes the compromised eMudhra CA roots from Java's cacerts trust store.
Noam Alum · Oct 25, 2026
Security news
PHP CVE-2026-109618: Critical RCE Leaked, Patch Immediately
PHP 8.5.12, 8.4.27, 8.3.36 and 8.2.35 fix two critical CVSS 9.2 core flaws, CVE-2026-109618 and CVE-2026-109619, that leaked before release. Update now.
Suriq's Jack · Oct 21, 2026

See what Suriq finds on your own servers.
Agentless checks for uptime and your cloud, a lightweight agent for detection on each server, and one console that ranks and explains what it finds.
Get Access How it works

× Private beta
Something great
is coming.
Suriq is opening access in waves. Leave your email and we'll bring you in.

No spam. One note when your spot opens.

You're on the list.
We'll reach out the moment your spot opens. Welcome aboard.
Close

× Newsletter
Be first to know.
Practitioner-grade security research and product updates, the moment we publish. No noise, no spam.
Double opt-in: we send one confirmation link and never add you without it.

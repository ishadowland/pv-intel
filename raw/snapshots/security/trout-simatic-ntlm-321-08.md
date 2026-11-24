<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.trout.software/blog/siemens-simatic-wincc-ntlm-relay-icsa-26-321-08 -->
<!-- fetched_at: 2026-11-25 07:12:21 -->
<!-- sha256: b5904c5d06d82a1c658fdfba0e3af62a00d8199fd8c03ad46766a98e10a56145 -->

Siemens WinCC and PCS 7 NTLM Relay (ICSA-26-321-08)
Back to Blog ICS Advisories OT Security SCADA Security Manufacturing Critical Infrastructure
Siemens SIMATIC WinCC, PCS 7 and Process Historian: NTLM Relay With No Fix (ICSA-26-321-08)
Trout Team · Last updated : November 19, 2026 · 11 min read
The short version.

On November 17, 2026, CISA published ICSA-26-321-08 for Siemens SIMATIC . It republishes Siemens SSA-970803 and covers one CVE, CVE-2026-58114 , scored CVSS v3.1 7.5 . The affected products are the core of a Siemens plant's supervisory layer: WinCC V7.5, V8.0 and V8.1, WinCC Runtime Professional V17 to V21, PCS 7 V9.1, BATCH V9.1, Process Historian 2020 and 2022, and Information Server 2020 and 2022.

The flaw is in how these products use NTLM , the old Windows authentication protocol. An attacker who sits between a user and a server can relay that user's sign-in and act as them. Siemens says that gives the attacker the user's session and code execution with the user's privileges . The services the attacker can reach, such as the SQL Server behind WinCC, decide how far it goes.

No product has a fix. WinCC and WinCC Runtime Professional have none yet. PCS 7 V9.1, BATCH V9.1, Process Historian and Information Server will not get one. The vendor's mitigation is to encrypt SQL Server traffic. The rest is on the network: stop NTLM and SQL traffic crossing zones, and control who reaches these servers.

Why these Siemens servers matter in the plant.

WinCC is Siemens' SCADA system. It draws the operator screens and raises the alarms. WinCC Runtime Professional is the TIA Portal runtime for machine and plant visualization. PCS 7 V9.1 is Siemens' distributed control system, built on WinCC, BATCH and other components. Process Historian is the long-term archive for PCS 7, WinCC and PCS neo, holding process values, alarms and batch data. Information Server reports on what the historian stores.

All of them run on Windows and store data in Microsoft SQL Server. Operator stations, OS servers, engineering stations and report readers all sign in to them. Where a plant runs as a workgroup, or Kerberos is not set up for these services, Windows uses NTLM for those sign-ins.

Information Server is often read from the office network. In many plants, production and quality staff open its reports from business PCs. In our reading, that makes it one of the places where NTLM and SQL traffic most often crosses from IT into OT. Our guides on patch management in operational environments and maintenance window planning cover why these servers are slow to change even when a fix exists.

What the advisory says.

Vulnerability: CVE-2026-58114, weak authentication (CWE-1390). Affected systems do not properly secure remote user authentication with NTLM. An unauthenticated attacker in a machine-in-the-middle position can relay NTLM authentication and impersonate a legitimate user.

Scores: CVSS v3.1 7.5, AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H . Siemens adds CVSS v4 7.7.

Sector: Critical Manufacturing, deployed worldwide. Siemens is headquartered in Germany.

Coordination: Siemens SSA-970803, published November 10, 2026. Siemens credits Tim Dijkman of Powerspex. Siemens ProductCERT reported it to CISA.

Product Affected versions Fix status, per Siemens
SIMATIC WinCC V7.5, V8.0, V8.1, all versions No fix available yet
SIMATIC WinCC Runtime Professional V17, V18, V19, V20, V21, all versions No fix available yet
SIMATIC PCS 7 V9.1, all versions No fix planned
SIMATIC BATCH V9.1, all versions No fix planned
SIMATIC Process Historian 2020 and 2022, all versions No fix planned
SIMATIC Information Server 2020 and 2022, all versions No fix planned

The mitigation is the same for all fourteen products: configure the SQL Server database manually to encrypt communication, following Siemens support article 109818202. Siemens also asks for network access to the devices to be protected, and for its Industrial Security operational guidelines to be followed. CISA adds its usual steps: keep control systems off the internet, behind firewalls and away from the business network.

Siemens adds a note on NTLM itself. Microsoft is moving away from NTLM , and Kerberos needs a domain with a Server Principal Name set. Where Kerberos is not in use, Siemens says operators must assess the risk themselves.

How the relay works.

NTLM does not tie a sign-in to the server it was meant for. A client asks a server for access, the server sends a challenge, and the client answers with a response computed from the user's password hash. Unless the server enforces signing or channel binding, nothing ties that response to the real server.

An on-path attacker uses that gap. It receives the client's sign-in, passes the challenge and response to the real server, or to another server that accepts the same account, and keeps the authenticated session for itself. The user sees a normal sign-in. The attacker now holds a session with that user's rights.

The CVSS vector explains the conditions. High complexity reflects the on-path position the attacker must first gain. User interaction is required because a legitimate user has to sign in while the attacker is in place. No privileges are needed. On a flat Windows network, the usual ways to get on-path are ARP spoofing and LLMNR or NetBIOS name poisoning, which any host on the same segment can try.

What the attacker gets depends on what the relay reaches. Siemens names the SQL Server used by WinCC. In our reading, a session on that database with an engineer's rights reaches the archives WinCC writes there. Siemens' advisory states code execution with the victim's privileges as the outcome.

Encrypting SQL Server traffic closes part of the gap. It is the mitigation Siemens gives. In our reading, it also makes Microsoft's Extended Protection for Authentication possible on SQL Server, which ties the NTLM sign-in to the encrypted channel. Ask Siemens whether Extended Protection is supported on your WinCC or PCS 7 version before you turn it on.

The table maps the vulnerability to MITRE ATT&CK for ICS. It describes what the flaw makes possible, not an observed attack. It uses ATT&CK v20.1.

Tactic Technique (ID) How it applies here
Collection Adversary-in-the-Middle (T0830) The machine-in-the-middle position CVE-2026-58114 requires, between a user or station and a SIMATIC server
Initial Access, Lateral Movement Exploitation of Remote Services (T0866) Relaying the intercepted NTLM sign-in to SQL Server or another service on the SIMATIC host
Persistence, Lateral Movement Valid Accounts (T0859) The attacker acts as the legitimate user whose authentication was relayed
Collection Data from Information Repositories (T0811) Possible consequence: process values, alarms and batch data in the WinCC database or Process Historian
Impact Theft of Operational Information (T0882) Possible consequence: project and production data read with the victim's rights
Impact Manipulation of View (T0832) Possible consequence: code execution on a WinCC server changes what operators see

What to do while there is no fix.

Start with Siemens' mitigation. Encrypt SQL Server communication on every WinCC, PCS 7, BATCH, Process Historian and Information Server host, using article 109818202. Test it on a spare station first, because a client that cannot negotiate encryption can lose its connection.

List every affected server. Record the product, version and the line or unit each one serves. Include the historian, the Information Server that IT reads, and the WinCC Runtime Professional stations on single machines that are easy to forget.

Map who signs in to each server, and from where. List the hosts that reach SQL Server (TCP 1433 for a default instance, the configured or dynamic port for a named instance, UDP 1434 for SQL Server Browser) and file sharing on TCP 445. Every path from outside the server's own cell is a place where a relay can start or end.

Remove the easy ways to get on-path. Keep the servers on their own segment, away from office PCs and vendor laptops. Disabling LLMNR and NetBIOS name resolution, and enforcing SMB signing, are standard Windows hardening against relay. The advisory does not list them, so check each change against Siemens' compatibility guidance for your PCS 7 or WinCC version before you roll it out.

Plan the move to Kerberos where you can. Siemens points to Kerberos with a domain and a Server Principal Name. On PCS 7 V9.1 and the other products with no fix planned, that and the network are the only lasting controls. Put the migration to a supported version on the plan.

How Access Gate helps, and where it stops.

The NTLM relay path to a SIMATIC server today, and the contained path with a gate in front of the servers.
Access Gate is an appliance installed at each site. It plugs into your existing network, beside it. You then route traffic to the SIMATIC servers through it with one route on the existing router, one server or one cell at a time. Nothing is installed on the WinCC or PCS 7 hosts. It installs in a day per site.

A per-machine rule decides who reaches each server. Access control lists deny by default. One rule lets the listed WinCC clients and OS servers reach SQL Server and file sharing. No host in another zone gets a route to those ports , so NTLM and SQL traffic stop at the gate. A sign-in captured on the office network has nowhere to be relayed to.

A named person signs in first. An Access Screen asks the engineer to sign in with their own directory account and a TOTP code before their workstation reaches the server. Access expires after 15 minutes, 1 hour or 8 hours. That puts an identity check in front of the server that does not depend on NTLM.

Vendor and engineer sessions are recorded. With privileged access management , the integrator opens a remote desktop session to the WinCC or PCS 7 host in the browser, tied to their name. A remote vendor's laptop reaches one host through the browser session and gets no other route into the plant network , so it cannot take an on-path position there. Every rule change lands in the enclave change history .

The limits are real. Access Gate does not fix the NTLM weakness, and it does not inspect NTLM or SQL Server traffic. SQL Server encryption is still Siemens' mitigation, and you still need it. A host on the servers' own segment, outside the gate, can still take an on-path position. A listed station or an allowed engineer laptop that is compromised still reaches the vulnerable product.

For the wider design, see OT network security , secure remote access , OT identity and our page on manufacturing cybersecurity . Our analysis of the Siemens Node2Shell and PHP2Shell advisories covers another case where the fix depends on Siemens' release schedule.

What to do this week.

List every affected server with product, version and the line or unit it serves.

Get SSA-970803 and article 109818202 from Siemens, and test SQL Server encryption on a spare station.

Check who reaches each server on SQL Server ports and TCP 445, from the business network, the vendor VPN and the internet.

Move Information Server report access for office users to one controlled path.

Ask Siemens about LLMNR, NetBIOS and SMB signing changes for your PCS 7 or WinCC version.

Route engineer and vendor sessions through one signed-in, recorded entry point.

Put the PCS 7 V9.1, BATCH, Process Historian and Information Server upgrade on next year's plan.

For every other advisory we have covered, see the ICS security advisories archive .

Sources: CISA ICS Advisory ICSA-26-321-08 (November 17, 2026) and its CSAF file, republishing Siemens ProductCERT SSA-970803 (November 10, 2026); the CISA Known Exploited Vulnerabilities catalog , checked on November 19, 2026 (version 2026.11.18); and MITRE ATT&CK for ICS v20.1. Confirm affected versions and the SQL Server encryption procedure with Siemens before changing a production WinCC or PCS 7 server.
FAQ Frequently Asked Questions
What is CISA advisory ICSA-26-321-08? + It is an ICS advisory CISA published on November 17, 2026. It republishes Siemens ProductCERT advisory SSA-970803, first released on November 10, 2026. It covers one vulnerability, CVE-2026-58114, a weak authentication flaw (CWE-1390) in how Siemens SIMATIC SCADA and PCS 7 products handle NTLM. It is scored CVSS v3.1 7.5, and Siemens also gives a CVSS v4 score of 7.7. CISA lists the Critical Manufacturing sector, with worldwide deployment.
Which Siemens products are affected by CVE-2026-58114, and is there a fix? + All versions of SIMATIC WinCC V7.5, V8.0 and V8.1, SIMATIC WinCC Runtime Professional V17, V18, V19, V20 and V21, SIMATIC PCS 7 V9.1, SIMATIC BATCH V9.1, SIMATIC Process Historian 2020 and 2022, and SIMATIC Information Server 2020 and 2022. No fix is available for WinCC or WinCC Runtime Professional yet. Siemens does not plan a fix for PCS 7 V9.1, BATCH V9.1, Process Historian or Information Server.
What does an attacker need to exploit CVE-2026-58114? + A machine-in-the-middle position between a user or station and a Siemens server, and a legitimate user who signs in while the attacker is there. No account is needed. The CVSS v3.1 vector is network, high complexity, no privileges, user interaction required. The attacker relays the user's NTLM authentication to a service, such as the SQL Server used by WinCC, and acts as that user. Siemens says the impact depends on which services the attacker can reach.
Is CVE-2026-58114 being exploited? + Neither the CISA advisory nor Siemens SSA-970803 reports exploitation. CVE-2026-58114 was not in the CISA Known Exploited Vulnerabilities catalog when we checked on November 19, 2026, against catalog version 2026.11.18. Check again before you set the priority.
What mitigation does Siemens give for CVE-2026-58114? + For all fourteen affected products, Siemens says to configure the SQL Server database manually to encrypt communication, following Siemens support article 109818202. Siemens also asks operators to protect network access to the devices and follow its Industrial Security operational guidelines. It notes that Microsoft is moving away from NTLM, and that Kerberos needs a domain with a Server Principal Name set.
How do you contain a WinCC or PCS 7 NTLM relay on the network? + Keep the relayed authentication from reaching anything useful. Let only the stations that need SQL Server and file sharing reach the WinCC, PCS 7, Process Historian and Information Server hosts, and deny those protocols from every other zone. Put the servers on their own segment, so fewer hosts can take an on-path position. Encrypt SQL Server as Siemens asks, and route engineer and vendor access through one signed-in, recorded entry point.

Other Articles
CYBER INSURA FOR MANUFA THE QUESTI CYBER · INSURA · FOR 06 NODES · 06 CONNECTIONS
Cyber Insurance Manufacturing
Cyber insurance for manufacturers: the OT questions underwriters ask and how to answer them
Cyber insurers now ask manufacturers about the plant network: MFA on employee and vendor remote access, separation of OT from IT and the internet, an OT asset inventory, end-of-life machines, offline backups and a tested recovery plan. Answer each one with a document you can attach, such as a network diagram, a vendor access list, session logs or a backup test record.

HOW GET HISTOR MES HOW · GET · HISTOR 04 NODES · 05 CONNECTIONS
Industrial DMZ OT Security
How to get historian, MES and ERP data through an industrial DMZ
Put a replica or a broker in a Level 3.5 industrial DMZ, let the OT side push data out to it, and let ERP, MES, BI and cloud tools read only from the DMZ. No IT system opens a connection to Level 2 or below, and every human or vendor session to the plant goes through MFA and an audit log in the DMZ.

HOW BUILD INCIDE RESPON PLAN HOW · BUILD · INCIDE 05 NODES · 06 CONNECTIONS
Incident response OT Security
How to Build an OT Incident Response Plan for a Plant
An OT incident response plan decides five things before an attack: who can cut the link between IT and OT, which lines can run without IT, how engineers reach the plant when the corporate network is down, which evidence to keep, and how to check the machines before restarting. Write those decisions down, name the people, and test them twice a year.

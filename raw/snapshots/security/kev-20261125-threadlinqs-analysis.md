<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://intel.threadlinqs.com/threat/TL-2026-6887 -->
<!-- fetched_at: 2026-11-26 07:10:57 -->
<!-- sha256: b546bfcfa81563615a1de0740c3e47bdf4c5e244d41dbfb2c99b5e16dd396295 -->

CISA adds 10 vulnerabilities to KEV catalog | Threadlinqs

Skip to navigation Threat report Vulnerability TL-2026-6887
CISA adds 10 vulnerabilities to KEV catalog: Danfoss AK-SM 800A (CVE-2023-25914/25915, CVE-2025-41450), Juniper Session Smart Conductor (CVE-2026-103406), Mitel MiCollab (5 CVEs), Vates Xen Orchestra (CVE-2026-133469)
critical ACTIVE
On 2026-11-25 CISA added 10 CVEs to the Known Exploited Vulnerabilities catalog across Danfoss AK-SM 800A, HPE Juniper Session Smart Conductor/Router, Mitel MiCollab and Vates Xen Orchestra, citing evidence of active exploitation. Public exploitation detail exists only for the Xen Orchestra authentication bypass (VSA-2026-062, empty-object token cookie, Vates-confirmed attacks from 2026-11-10); for the other products CISA gives no exploitation specifics.

Key facts
Identifiers TL-2026-6887, CVE-2023-25914 , CVE-2023-25915 , CVE-2025-41450 , CVE-2026-103406 , CVE-2026-133275 , CVE-2026-133303 , CVE-2026-133311 , CVE-2026-133323 , CVE-2026-133324 , CVE-2026-133469
Also known as VSA-2026-062, VSA-2026-063, MISA-2026-0012, JSA112183, ICSA-25-140-03
Severity CRITICAL
CVSS 10 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:N/I:H/A:H)
EPSS CVE-2025-41450: 0.9% (61.2th percentile); CVE-2026-103406: 0.5% (43.9th percentile)
Affected products Vates Xen Orchestra / Xen Orchestra Appliance (XOA); HPE Juniper Networks Session Smart Conductor / Session Smart Router; Mitel MiCollab (AWV component); Danfoss AK-SM 800A Series
Weaknesses (CWE) CWE-22 , CWE-20 , CWE-287 , CWE-78 , CWE-434 , CWE-91 , CWE-1390 , CWE-636 , CWE-1287
Malware RedLine Stealer - S1240
MITRE ATT&CK techniques T1005 Data from Local System , T1053.003 Scheduled Task/Job: Cron , T1059 Command and Scripting Interpreter , T1059.004 Command and Scripting Interpreter: Unix Shell , T1078 Valid Accounts , T1090.003 Proxy: Multi-hop Proxy , T1190 Exploit Public-Facing Application , T1528 Steal Application Access Token , T1550.001 Use Alternate Authentication Material: Application Access Token
Motivation UNKNOWN
Target sectors government administration, telecoms, technology, critical infrastructure, industrial, retail, cloud and virtualization
Target regions Global
Detection rules 9 (1 shown free)
Sources 13 cited sources
Detection coverage
As of 2026-11-25, Threadlinqs Intelligence publishes 9 detection rule(s) for TL-2026-6887 across Splunk SPL, Microsoft KQL and Sigma, covering 9 indicator(s) of compromise. The whole corpus is readable without an account. Every threat comes with one complete detection in Splunk SPL, Microsoft KQL and Sigma, free for everyone; a free account adds daily TL Creds to unlock the rest. Paid plans add a larger daily allowance, correlation and the MCP server. Threadlinqs MCP server · View plans .
Free detection: Xen Orchestra Empty-Object Token Cookie Authentication Bypass (CVE-2026-133469 / VSA-2026-062)
Detects the exploit trigger for the Xen Orchestra authentication bypass tracked by Vates as VSA-2026-062 (CISA KEV CVE-2026-133469, mapping inferred from the KEV name): a request carrying the cookie authenticationToken=j:%7B%7D, which the XO REST layer parses to an empty object so the token lookup returns the first unexpired token and authenticates the caller as that token's owner. Vates says exploitation leaves no log identifiers, so this relies on reverse-proxy/WAF/HTTP telemetry that records the Cookie header. Exploitation confirmed by Vates from 2026-11-10.
Languages: Splunk SPL, Microsoft KQL, Sigma
ATT&CK: T1190 , T1078
Data sources: nginx_access_logs_with_cookie, waf_logs, reverse_proxy_logs, web_index
Severity: critical
Confidence: high
Splunk SPL
index=web (sourcetype="nginx:plus:kv" OR sourcetype="access_combined" OR sourcetype="f5:bigip:asm:syslog") ("authenticationToken=j:%7B%7D" OR "authenticationToken=j:{}" OR "authenticationToken=j%3A%7B%7D")
```comment: empty-object token cookie used by VSA-2026-062 / CVE-2026-133469 exploitation```
| eval src=coalesce(src, src_ip, clientip, "unknown"), dest=coalesce(dest, host), uri=coalesce(uri_path, uri, url)
| stats count min(_time) as first_seen max(_time) as last_seen values(uri) as uris values(http_user_agent) as user_agents values(status) as status_codes by src, dest
| eval first_seen=strftime(first_seen, "%F %T"), last_seen=strftime(last_seen, "%F %T")
| table first_seen last_seen src dest uris status_codes user_agents count Microsoft KQL
union isfuzzy=true
(CommonSecurityLog
| where TimeGenerated > ago(24h)
| extend Hay = strcat(RequestContext, " ", AdditionalExtensions, " ", RequestURL, " ", Message)
| where Hay contains "authenticationToken=j:%7B%7D" or Hay contains "authenticationToken=j:{}" or Hay contains "authenticationToken=j%3A%7B%7D"
| project TimeGenerated, SourceIP, DestinationIP, Url = RequestURL, Agent = RequestClientApplication, Source = strcat(DeviceVendor, " ", DeviceProduct)),
(Syslog
| where TimeGenerated > ago(24h)
| where SyslogMessage contains "authenticationToken=j:%7B%7D" or SyslogMessage contains "authenticationToken=j:{}" or SyslogMessage contains "authenticationToken=j%3A%7B%7D"
| project TimeGenerated, SourceIP = HostIP, DestinationIP = Computer, Url = SyslogMessage, Agent = "", Source = "Syslog")
| summarize Hits = count(), FirstSeen = min(TimeGenerated), LastSeen = max(TimeGenerated), Urls = make_set(Url, 10), Agents = make_set(Agent, 10) by SourceIP, DestinationIP, Source
| order by Hits desc Sigma
title: Xen Orchestra Empty-Object Authentication Token Cookie (VSA-2026-062)
id: 3b7e9c1a-5d42-4f0e-9a61-8c2d7e4b1a01
status: experimental
description: Detects the Xen Orchestra authentication bypass exploit cookie authenticationToken=j:%7B%7D (empty object) used in VSA-2026-062 / CVE-2026-133469 exploitation. Requires a web log source that records the Cookie header.
references:
- https://www.cisa.gov/news-events/alerts/2026/11/25/cisa-adds-10-known-exploited-vulnerabilities-catalog
- https://docs.vates.tech/security-advisories/advisories/2026/vates-sa-2026-062/
author: Threadlinqs Team
date: 2026-11-25
tags:
- attack.initial-access
- attack.t1190
- attack.defense-evasion
- attack.t1078
- cve.2026.133469
logsource:
category: webserver
detection:
selection:
cs-cookie|contains:
- 'authenticationToken=j:%7B%7D'
- 'authenticationToken=j:{}'
- 'authenticationToken=j%3A%7B%7D'
condition: selection
falsepositives:
- Security scanners or WAF test suites replaying the published exploit cookie
- Authorized penetration tests against Xen Orchestra
level: critical Known false positives:
Vulnerability scanners or WAF validation suites replaying the public exploit cookie against Xen Orchestra
Authorized red-team or penetration test activity against the XO management plane
Tuning notes: Requires the Cookie header to be logged (nginx log_format with $http_cookie, a WAF cookie field, or a reverse-proxy audit log); standard access logs will not match. Adjust index/sourcetype to your web telemetry. Allow-list known scanner source IPs and scope to hosts running Xen Orchestra/XOA. A hit from an untrusted source is high fidelity - treat it as compromise and run the XCP-ng host artifact hunt (pivot2 VM, /etc/cron.d/zz-ustar*, /.ustar*).
🔒 8 more detection rules (Splunk SPL, Microsoft KQL, Sigma) · unlock with TL Creds. Sign up free to unlock the detection rules or query them with the Threadlinqs MCP server (Purple and Gold in full, 2 calls a day on a free account)

🔒 Danfoss AK-SM 800A xml.cgi getauth Probe and get_file Path Traversal (CVE-2025-41450 / CVE-2023-25914) · unlock with TL Creds
🔒 XCP-ng Host Cron Persistence and Dropped Files from Xen Orchestra Campaign ([indicator]*, [indicator], [indicator]) · unlock with TL Creds
🔒 Juniper Session Smart Conductor Salt Minion ID Command Injection (CVE-2026-103406) · unlock with TL Creds
🔒 Mitel MiCollab AWV Exploitation Attempt - Command Injection Metacharacters or Script Upload (MISA-2026-0012) · unlock with TL Creds
🔒 XCP-ng Rogue VM with File-Backed Serial Device or Name pivot2 (VSA-2026-062/063 Campaign) · unlock with TL Creds
🔒 Xen Orchestra Server Process Spawning Shell or Downloader (Post-Authentication-Bypass Execution) · unlock with TL Creds
🔒 Xen Orchestra Authentication Token Harvest via [indicator] from External Source · unlock with TL Creds
🔒 Xen Orchestra Campaign C2 Egress - [indicator]:8001 and Tor Onion Service (port 3333) · unlock with TL Creds
Indicators of compromise
As of 2026-11-25, Threadlinqs Intelligence tracks 9 indicators of compromise for TL-2026-6887.
Sample indicators (2 of 9)
IP address: 91.211.251[.]112
Domain: ustar3rqxgnskzgnwkgpofgtvxevm6cx3lxdbwt4mndtveqyaohid[.]onion
Defanged, TLP:CLEAR. Full set of 9 indicators: unlock with TL Creds .
🔒 9 indicators of compromise · unlock with TL Creds. Compare plans
Technical analysis
CISA's 2026-11-25 alert states it added 10 vulnerabilities to the KEV catalog 'based on evidence of active exploitation'. The alert names no threat actors, campaigns or IOCs and notes BOD 26-04 applies only to FCEB agencies. NVD records a KEV action due date of 2026-11-28 for CVE-2026-103406.
Vates Xen Orchestra (CVE-2026-133469, Improper Validation of Specified Type of Input): the KEV entry maps to the authentication bypass tracked by Vates as VSA-2026-062. At disclosure (2026-11-10) press reports said no CVE had yet been assigned; the CVE-to-advisory mapping here is inferred from the KEV vulnerability name and the matching root cause and should be confirmed against the Vates advisory. The REST layer parses the cookie authenticationToken=j:%7B%7D into an empty object {} and passes it to the XO token provider without requiring a string. The token collection treats {} as an unfiltered lookup and returns the first unexpired token, so the request is authenticated as that token's owner with no credentials. The attacker then reads reusable token IDs from /rest/v0/users/me/authentication_tokens. Vates rates impact as Admin, with arbitrary code execution on managed pools and root takeover of XCP-ng nodes, and says exploitation generates no identifiers in logs, so it must be detected through HTTP monitoring. Vates reports VSA-2026-062 being chained with VSA-2026-063, a crafted raw XVA import via vm.import / sr/import:vm / network/action:create|update by a low-privileged user that compromises an XCP-ng host; no fix was available at the time of the reports. Observed host artifacts: a running VM named pivot2, VMs with hvm_serial: file, /etc/cron.d/zz-ustar, /etc/cron.d/zz-ustar2, /.ustar5, /.ustar6, plus 91.211.251.112:8001 (flagged by VirusTotal as RedLine Stealer C2 per The Hacker News) and a Tor onion service on port 3333. Vates names no actor and says the IOCs apply only to this known campaign.
HPE Juniper Session Smart Conductor/Router (CVE-2026-103406): per NVD, OS command injection (CWE-78) in the AutomatedProvisioner component of Session Smart Conductor lets a remote attacker run arbitrary commands as root via a crafted salt minion ID. CVSS 3.1 is 9.8 (AV:N/AC:L/PR:N/UI:N). CISA's SSVC data in NVD marks exploitation 'active', automatable 'no', technical impact 'total'. Affected: Conductor below 7.0.5-14-lts, 7.1.0-50r1 up to (excluding) 7.1.7-15-sts, and 7.2.0-29r1 up to (excluding) 7.2.3-8r2. Advisory JSA112183 was published 2026-10-28 (the advisory page did not render during research; third-party aggregators report no known workarounds). The NVD description names only the Conductor.
Mitel MiCollab (CVE-2026-133275, -133303, -133311, -133323, -133324): all five are unauthenticated flaws in the AWV component of MiCollab 10.3 (10.3.0.18) and earlier, covered by Mitel advisory MISA-2026-0012 (issued 2026-11-16, rev 2.0 on 2026-11-24 updated CVE numbers). Mitel IDs and CVSS 3.1 scores: 133275 file upload via insufficient file-type validation (MTLVULN-1861, 5.3); 133303 XML injection using pre-staged content (MTLVULN-1862, 9.0); 133311 improper authentication needing a system-generated identifier or pre-staged content (MTLVULN-1863, 5.9); 133323 blind command injection from insufficient parameter sanitization (MTLVULN-1864, 10.0, AV:N/AC:L/PR:N/UI:N/S:C/C:N/I:H/A:H); 133324 authentication bypass from improper authentication handling (MTLVULN-1877, 5.3). Mitel warns that exploiting them together 'can significantly amplify their impact'. A patch exists for 10.3.0.18 (KB000129195) and the interim mitigation is restricting external access to AWV. No source read reports exploitation specifics, IOCs or actors for these CVEs; third-party aggregators showed no exploitation data at publication on 2026-11-19, so KEV listing is the only exploitation signal.
Danfoss AK-SM 800A series (CVE-2023-25914, CVE-2023-25915, CVE-2025-41450): CVE-2023-25914 is a path traversal (CWE-22) in the XML interface (get_file action in the sm_app CGI binaries) that lets attackers read system files; found by Synacktiv, affects versions up to 3.3 and was fixed in 3.3 (DIVD: CVSS 9.9, AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H). CVE-2023-25915 (Improper Input Validation per KEV) could not be verified in the sources fetched. CVE-2025-41450 is an authentication bypass (CWE-287, CVSS 3.1 8.2, fixed in R4.2) caused by datetime-based 'code of the day' password generation reachable through xml.cgi action=getauth. Claroty Team82 (2026-08-09) chained it with CVE-2025-41451 (command injection via the SMTP password field, CWE-77, fixed 4.3.1) for remote code execution and with CVE-2025-41452 (nginx headers.conf replacement via action=load_nginx_headers, DoS), and counted 2,765 exposed devices in a Censys scan. CISA ICSA-25-140-03 stated no known public exploitation had been reported to CISA as of its last text; the KEV listing is therefore new exploitation evidence not described in public sources.
No threat actor, nation-state or motivation is attributed in any source. Defenders should patch, remove management interfaces from the internet, and hunt the Xen Orchestra IOCs above.
MITRE ATT&CK techniques by tactic:
Collection
T1005 Data from Local System
Persistence
T1053.003 Scheduled Task/Job: Cron
Execution
T1059 Command and Scripting Interpreter ; T1059.004 Command and Scripting Interpreter: Unix Shell
Defense Evasion
T1078 Valid Accounts
Command and Control
T1090.003 Proxy: Multi-hop Proxy
Initial Access
T1190 Exploit Public-Facing Application
Credential Access
T1528 Steal Application Access Token
Lateral Movement
T1550.001 Use Alternate Authentication Material: Application Access Token
Remediation
Patches
Vates Xen Orchestra 6.9.1 / 6.10.0 (VSA-2026-062); VSA-2026-063 fix was pending in cited reports
Mitel MISA-2026-0012 patch for MiCollab 10.3 (10.3.0.18)
Juniper JSA112183: Session Smart Conductor 7.0.5-14-lts, 7.1.7-15-sts, 7.2.3-8r2 or later
Danfoss AK-SM 800A: 3.3 or later (CVE-2023-25914), R4.2 (CVE-2025-41450), R4.3.1 (CVE-2025-41451/41452)
Immediate actions
Upgrade Xen Orchestra / XOA to a fixed release (6.9.1 stable or 6.10.0 latest, xo-server 5.211.2 / 5.213.1, or later) and block requests containing authenticationToken=j:%7B%7D at the WAF or reverse proxy
Hunt XCP-ng hosts for the VSA-2026-062 artifacts: VM pivot2, hvm_serial: file, /etc/cron.d/zz-ustar*, /.ustar*; rotate all virtualization-environment secrets if found
Block 91.211.251.112 and the observed Tor onion service at the perimeter
Restrict external access to the MiCollab AWV component and apply the Mitel patch for 10.3.0.18 (KB000129195)
Upgrade Juniper Session Smart Conductor to 7.0.5, 7.1.7, 7.2.3 or later per JSA112183 and restrict management-interface access
Remove Danfoss AK-SM 800A controllers from direct internet exposure and upgrade to R4.3.1 or later
FCEB agencies: remediate per the KEV due dates (NVD records 2026-11-28 for CVE-2026-103406)
Workarounds
Xen Orchestra VSA-2026-063: restrict VM import to the Admin user and disable users holding vm.import, sr/import:vm, network/action:create or network/action:update
MiCollab: restrict external access to the AWV component
Limit access to Session Smart Conductor and router management interfaces
Longer-term hardening
Place hypervisor management planes (Xen Orchestra, XCP-ng), UC platforms and OT controllers on dedicated management networks behind VPN/ZTNA
Monitor HTTP requests to virtualization management APIs, since the Xen Orchestra bypass produces no log identifiers
Maintain an asset inventory of edge, UC, SD-WAN and ICS devices and map it against the KEV catalog
Affected and fixed versions
Vates — Xen Orchestra / Xen Orchestra Appliance (XOA)
Vulnerable versions: versions prior to the fixed releases (exact range not stated in the cited articles)
Fixed in: 6.9.1 (stable); 6.10.0 (latest); xo-server 5.211.2 / 5.213.1
HPE Juniper Networks — Session Smart Conductor / Session Smart Router
Vulnerable versions: below 7.0.5-14-lts; 7.1.0-50r1 up to 7.1.7-15-sts (excl.); 7.2.0-29r1 up to 7.2.3-8r2 (excl.)
Fixed in: 7.0.5-14-lts; 7.1.7-15-sts; 7.2.3-8r2
Mitel — MiCollab (AWV component)
Vulnerable versions: 10.3 (10.3.0.18) and earlier
Fixed in: 10.3.0.18 with patch KB000129195 or a later release
Danfoss — AK-SM 800A Series
Vulnerable versions: 3.3 and earlier (CVE-2023-25914); prior to R4.2 (CVE-2025-41450)
Fixed in: 3.3 (CVE-2023-25914); R4.2 (CVE-2025-41450); R4.3.1 (CVE-2025-41451/41452)
Timeline
2025-05-20 CISA publishes ICSA-25-140-03 for Danfoss AK-SM 8xxA including CVE-2025-41450 authentication bypass; no public exploitation reported to CISA at that time
2025-08-26 ICSA-25-140-03 Update A adds CVE-2025-41451 and CVE-2025-41452
2026-08-09 Claroty Team82 publishes research chaining Danfoss AK-SM 800A code-of-the-day authentication bypass to RCE and reports 2,765 exposed devices
2026-10-28 Juniper publishes JSA112183; NVD publishes CVE-2026-103406 (Session Smart Conductor AutomatedProvisioner command injection, CVSS 9.8)
2026-11-10 Vates discloses VSA-2026-062 and confirms active exploitation of the Xen Orchestra empty-token authentication bypass; fixes released (6.9.1 / 6.10.0)
2026-11-16 Mitel issues MISA-2026-0012 for MiCollab AWV vulnerabilities in 10.3.0.18 and earlier
2026-11-18 CISA revises ICSA-25-140-03 (revision 3, updated remediation URLs)
2026-11-19 Mitel MiCollab CVE-2026-133275 and CVE-2026-133323 published to vulnerability databases (aggregators show no exploitation data)
2026-11-24 MISA-2026-0012 revision 2.0 updates the CVE numbers
2026-11-25 CISA adds 10 CVEs (Danfoss, Juniper, Mitel, Vates) to the KEV catalog based on evidence of active exploitation
2026-11-28 NVD records the CISA KEV action due date for CVE-2026-103406
Sources cited
CISA Adds 10 Known Exploited Vulnerabilities to Catalog CISA · Government advisory · 2026-11-25
CISA Known Exploited Vulnerabilities Catalog CISA · Government advisory
BOD 26-04: Prioritizing Security Updates Based on Risk CISA · Advisory
NVD: CVE-2026-103406 (Juniper Session Smart Conductor) NVD (NIST) · Advisory · 2026-10-28
CISA ICS Advisory ICSA-25-140-03 Danfoss AK-SM 8xxA Series CISA · Government advisory · 2025-05-20
Juniper JSA112183 supportportal.juniper.net · Vendor report · 2026-10-28
Vates VSA-2026-062 Xen Orchestra authentication bypass docs.vates.tech · Vendor report · 2026-11-10
Mitel Product Security Advisory MISA-2026-0012 mitel.com · Vendor report · 2026-11-16
stack.watch: CVE-2026-133323 Mitel MiCollab AWV command injection stack.watch · Research · 2026-11-19
Claroty Team82: Freeze the Controller, Defrost the Food (Danfoss AK-SM 800A) claroty.com · Research · 2026-08-09
DIVD CSIRT: CVE-2023-25914 Path Traversal in Danfoss AK-SM800A csirt.divd.nl · Research
The Hacker News: Hackers Exploit Critical Xen Orchestra Flaw The Hacker News · News · 2026-11-10
BleepingComputer: Critical Xen Orchestra auth bypass flaw exploited to hijack VM servers BleepingComputer · News · 2026-11-10
More in vulnerability
CVE-2026-97180: OS Command Injection in ASSA ABLOY Seawing SC-1000 WebConfig (versions before 1.5.14)
CVE-2026-129968: Unauthenticated template injection in LiteSpeed Cache Plugin for Prestashop (before 1.6.2)
Critical Adobe Experience Manager (APSB26-104) and Campaign Classic (APSB26-194) Vulnerabilities Enable Code Execution
CVE-2026-129713: Unpatched Critical Stack-Based Buffer Overflow in Danfoss AK-SM 800A Series Refrigeration Controllers
Known Fortinet FortiGate Flaws Exploited to Breach Commercial Ships and Pivot from Shipboard IT into OT Networks (Attribution Unconfirmed)
Drafted by the Threadlinqs research pipeline from 13 sources; published 2026-11-25 ; last updated —.

Threadlinqs Intelligence — Real-Time Threat Detection Platform

[ sign_out ]

// threat_feed

Ask ask the corpus… Ctrl K
search
$ sort --newest

⚙️
Advanced Filters
▼

Status

All Statuses
Active
Monitoring
Resolved

Exploitability

All
Actively Exploited
PoC Available
Confirmed
Theoretical

CVSS Score

Any Score
Critical (9.0+)
High (7.0+)
Medium (4.0+)
Low (0-3.9)

Has Detections

Any
With Detections
No Detections

Attribution

Any
Nation State
Criminal
Unknown

Date Range

All Time
Last 24 Hours
Last 7 Days
Last 30 Days

MITRE Tactic

All Tactics
Initial Access
Execution
Persistence
Privilege Escalation
Defense Evasion
Credential Access
Discovery
Lateral Movement
Collection
Exfiltration
Impact

Tags

All Tags

🔥 Popularity

Any
🔥 Hot (10+ views)
📈 Trending (5+ views)
🆕 New (

Clear All
Showing all threats

classic
SecOS

command
briefing
explorer

Live intelligence console

Threat level

Latest Threats

Newest First
Recently Updated
Trending 🔥
By Severity
Alphabetical

◇ community-corroborated

linking threat corpus _

Ask the Lab
Ask the Lab

Ask the Lab

// ask_in_english
[ × ]

[ translate & apply ]

// ⚠ could not validate the generated TLQL

[ apply_anyway ]
[ refine_prompt ]

[ undo ]

🔄 Threat Comparison

×

Select 2 threats to compare. Click threat cards while in comparison mode.

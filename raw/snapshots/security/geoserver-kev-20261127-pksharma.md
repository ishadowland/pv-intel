<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.pk-sharma.com/briefing/cisa-lists-two-geoserver-flaws-as-exploited-due-30-november-project-says-october-updates-fix-them -->
<!-- fetched_at: 2026-11-28 07:12:08 -->
<!-- sha256: 4fb2e60a9eb474c6a3381549271d19de6131de986c395e588e28f00a13a4df05 -->

CISA lists two GeoServer flaws, due 30 Nov; update to October releases | P.K. Sharma
Zoom
39 days after the fix releases were announced, two GeoServer flaws are on CISA's list

On Friday 27 November 2026 CISA added two flaws in GeoServer, an open source server for publishing and sharing geospatial data, to its Known Exploited Vulnerabilities catalogue : CVE-2026-120705 and CVE-2026-129243 , both due Monday 30 November . The GeoServer project's release notices for the fixed versions, 3.0.2 , 2.28.6 and 2.27.7 , are dated 19 October . That is 39 days before the listing (derived: 19 October to 27 November). The project's CVE post and the advisories for the two flaws are dated 23 November, 4 calendar days before it (derived). This site read catalogue version 2026.11.27, released at 18:03 UTC, in a copy saved at about 19:42 UTC, and the project's post and the two advisories in copies saved at about 19:41 UTC. The release notices and other records were fetched between about 20:13 and 20:15 UTC.

What the 39 days do not establish. They do not show when exploitation began, or that any server was attacked during that time. The catalogue prints the date a flaw was added, not the date of an attack. Nor do they show that the CVE numbers or technical detail were public for 39 days. The release notices carry CVE numbers as read now but print no edit date, and the project's 23 November post thanks readers for waiting while the numbers were assigned. This brief does not say what the notices showed on 19 October.

The clock, derived. 30 November is 3 calendar days after 27 November, and two of those three days, 28 and 29 November, are a Saturday and a Sunday. The entries print no time of day. Both carry a forensic triage value of "No" and a ransomware campaign use value of "Unknown". Their required action, summarised: apply mitigations as the vendor instructs, in line with CISA's directive BOD 26-04 and its forensics triage requirements, follow the directive's guidance for cloud services, or discontinue use of the product if mitigations are not available. The entries also tell stakeholders to evaluate the internet exposure of each asset. This brief did not read the directive and does not say whom it binds.

Who is speaking. CISA keeps the catalogue. The GeoServer project maintains the software and wrote the fixes and advisories, so it has its own interest in how they read. SecurityWeek is a secondary source, used here for what it says the security firm watchTowr observed and for points no primary page in this set prints.

The two listed flaws, at CISA's level of detail

CVE-2026-120705 is an XML injection flaw in a WFS stored query. CISA says it lets a remote attacker with no login make the server read local text files that the GeoServer process can access, or fetch HTTP or HTTPS addresses the attacker chooses.

CVE-2026-129243 is an incorrect authorisation flaw. CISA says it lets a remote attacker with no login get past service level role checks and call operations that only those checks protect.

Each CISA description ends by saying the flaw can be chained with four other named CVEs "to achieve unauthenticated remote code execution" on an affected instance. That is a statement of what the combination can do. Neither entry says that anyone has been seen doing it.

What the two GitHub advisories published by the GeoServer project print, as read at about 19:41 UTC on 27 November 2026
Item CVE-2026-120705 CVE-2026-129243
Project rating High, 8.6 (CVSS 3.1) High, 8.8 (CVSS 4.0)
Vector CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:N/A:N CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:L/VI:H/VA:L/SC:N/SI:N/SA:N
Maven package org.geoserver:gs-wfs-core, and the GeoTools library org.geotools:gt-metadata org.geoserver:gs-ows
Affected GeoServer 2.27.6 and earlier; 2.28.0 to 2.28.5; 3.0.0 to 3.0.1 2.27.6 and earlier; 2.28.0 to 2.28.5; 3.0.0 to 3.0.1
Fixed GeoServer 2.27.7, 2.28.6, 3.0.2 2.27.7, 2.28.6, 3.0.2
GeoTools ranges 33.6 and earlier, fixed in 33.7; 34.0 to 34.5, fixed in 34.6; 35.0 to 35.1, fixed in 35.2 None listed

The two scores use different versions of CVSS, so 8.8 against 8.6 does not show that one flaw is worse than the other.

Neither is labelled as an add-on. Neither advisory calls its package an extension or a community module, and the project's post prints no add-on label beside either CVE, as it does for other October flaws. This site's reading: checking which extensions are installed will not rule these two out. Neither advisory says in so many words whether the WFS service is switched on in a new installation. The first calls the affected query built in and says exploitation needs no login, no custom stored query and no special permission to create one. It also says that where a server does not return the file contents, the file is still read. Having no anonymously published layer therefore does not remove the flaw. The GeoTools ranges also matter to anyone who builds other software on that library.

What the second flaw reaches. Its advisory says that on affected versions a crafted request could call operations restricted only by service security rules without a role check, whether the restriction came from the default configuration or was added by an administrator. It adds: "Layer and data security rules still apply."

Two labels that can mislead a triage queue

A severity word rates one flaw on its own. Both listed flaws are rated High by the project. The only Critical rating in the October list belongs to CVE-2026-129245, which is in the chain CISA describes and is not on the catalogue. In the same chain, one flaw is rated Medium, and the vector for another says high privileges are needed. Sorted one at a time, those two can look like work for later. CISA's descriptions say the five can be combined to reach code execution without a login.

"Service security" is the name of a setting, not proof that it held. The first advisory's mitigation is to restrict or disable WFS for anonymous users using service security, or to disable WFS if it is not required. The second advisory says that rules set in service security could be bypassed on the same GeoServer version ranges. This site's reading, which neither page states: on a server that has not been updated, a WFS restriction made only with service security rules should not be relied on by itself. Pair it with the second advisory's proxy block, or turn WFS off if it is not needed, and update. Neither saved page says whether turning WFS off is affected by the bypass either way.

Five CVEs in the chain CISA names, two of them on the list

The five CVEs in CISA's two descriptions, in numeric order (this is not a sequence). Ratings from the project; catalogue status from version 2026.11.27
CVE What it is, and the project's rating On the CISA catalogue
CVE-2026-120705 XML injection in a WFS stored query. High Yes, due 30 November
CVE-2026-129242 A deserialisation flaw in the JDBC user and role services that allows code execution by an administrator. High No
CVE-2026-129243 Bypass of service level role checks. High Yes, due 30 November
CVE-2026-129244 An error message from a stored query that discloses the data directory path. Medium (the advisory page says Moderate) No
CVE-2026-129245 A predictable remember-me key that allows an administrator session to be forged. Critical No

The project says the chain was reported to it with these as steps and that, at the direction of the CVE Numbering Authority, the other steps were given numbers of their own. This brief does not give the order. All five are listed as fixed in 3.0.2, 2.28.6 and 2.27.7 by their own advisories, including those for CVE-2026-129242 , CVE-2026-129244 and CVE-2026-129245 . Not being on the catalogue does not make the other three safe to leave. The update is the same.

No public CVE record yet, as read. At about 20:13 UTC the CVE Program's record service answered that the record did not exist for all five numbers. At about 20:14 UTC NVD returned no result for CVE-2026-120705 or CVE-2026-129243 , although CISA's notes link to NVD pages for both. This site's inference: a scanner or ticket rule that matches only on those records may have nothing to match yet. Check the installed GeoServer version directly.

The advisories also differ on package names. For the 2.27 and 2.28 lines, the advisory for the XML injection flaw names gs-wfs-core, while the advisory for CVE-2026-129244 names gs-wfs and uses gs-wfs-core only for 3.0. This brief does not resolve it. Match on the GeoServer version as well as on a package name.

The October list: 17 CVEs, 13 rated Critical or High (derived)

The project's post says: if you are responsible for an instance, "please update to GeoServer 3.0.2, GeoServer 2.28.6, or GeoServer 2.27.7". Counting the distinct CVE numbers under its October releases heading, including those shown inside the two chains and counting repeats once, gives 17 CVEs : 1 Critical, 12 High and 4 Medium (all derived from the page). So 13 of 17 are rated Critical or High. 2 of the 17 are on the CISA catalogue as read: the two above.

The October CVEs by the rating the project's post prints (counts derived from the page)
Rating Count CVE numbers
Critical 1 CVE-2026-129245
High 12 CVE-2026-120701, CVE-2026-120703, CVE-2026-120704, CVE-2026-120705, CVE-2026-120706, CVE-2026-120707, CVE-2026-120708, CVE-2026-120710, CVE-2026-129242, CVE-2026-129243, CVE-2026-129293, CVE-2026-129294
Medium 4 CVE-2026-120702, CVE-2026-120709, CVE-2026-129240, CVE-2026-129244

The add-on labels the project prints beside October CVEs. The other 10 (derived), including both catalogue entries, carry no label
Label printed CVE numbers
WPS Download extension CVE-2026-120701
WPS extension CVE-2026-120706
GeoFence extension CVE-2026-120707
ACL plugin CVE-2026-120708
printing extension CVE-2026-120709
community module CVE-2026-120703, CVE-2026-129294

A missing label is not a statement about what a given server has installed. The post also publishes two flaws fixed in earlier releases, CVE-2025-53607 (3.0.0, 2.28.4 and 2.27.6) and CVE-2024-35233 (3.0.0, 2.28.5 and 2.27.6). They are outside the October count, and neither is on the catalogue.

One difference to check before closing a ticket. The 3.0.2 notice lists all 17 October CVEs. The 2.28.6 and 2.27.7 notices list 16: each leaves out CVE-2026-129245, the Critical one, and neither mentions its number anywhere on the page. The project's post puts all three releases above one list that includes it, and its advisory says it is patched in all three. This site does not resolve the difference. If you need written proof for the 2.28 or 2.27 line, ask the project. The two fix ticket numbers printed in the advisories for the listed flaws, GEOS-12199 and GEOS-12195, appear in all three notices.

The 2.27 line is at end of life. The 2.27.7 notice says so and asks users to "apply this update as a mitigation measure only" and to plan a move to a stable or maintenance release. The project's post names 3.0.x as the current stable line and 2.28.x as the current maintenance line.

The dates, drawn to scale

Zoom
Drawn by this site from the GeoServer release notices, project post and advisories, CISA catalogue version 2026.11.27 and SecurityWeek (secondary), read on 27 November 2026.

Every date used here, and where it comes from
Date Event Source
Early August A Rapid7 researcher reports findings to GeoServer developers SecurityWeek only
Late September The firm Eye Security reports findings to the vendor SecurityWeek only
19 October Date on the release notices for 3.0.2, 2.28.6 and 2.27.7 GeoServer
23 November CVE post dated; the two listed advisories published at about 22:09 and 22:10 UTC GeoServer and its advisories
25 November, 15:27 UTC SecurityWeek reports exploitation attempts seen by watchTowr SecurityWeek page data
27 November, 18:03 UTC CISA catalogue version released with both flaws added that day CISA
30 November Due date for both entries CISA

A second set of release dates. GitHub's release records give publication times of 17 October for 3.0.2 , 18 October for 2.27.7 and 2 November for 2.28.6 . This brief counts from the notices of 19 October, which the project's CVE post links. Counting from 17 October would give 41 days (derived). The saved pages do not explain why the 2.28.6 record is dated 2 November, and this brief does not treat it as the day that version first became available.

From the release notices to the CVE post is 35 days (derived). The project says its policy is to fix flaws before publishing the details, so that users have a chance to update first.

What is stated, and what is not

Zoom
This site's summary of CISA catalogue version 2026.11.27, the GeoServer post and the two advisories for the listed flaws, and SecurityWeek (secondary), read on 27 November 2026. Grey dashed cells mark what a page does not state.

What the record establishes about attacks, and what it leaves out
Topic Stated Not stated
Exploitation CISA lists both flaws as known exploited The evidence, the start date, the targets
The attackers SecurityWeek writes of threat actors Any name, group or country
Scale Nothing about attacked or breached servers in any page read How many servers were attacked or breached
Code execution CISA says the chain can reach it That it has happened on a real victim's server
Detection One advisory asks for a review of stored query folders for entries you did not create Indicators of compromise, log lines or detection rules
Ransomware CISA: "Unknown" Any link to a ransomware campaign

What SecurityWeek adds. Its 25 November article says watchTowr observed attempts to exploit the two flaws, and that the activity appears aimed at identifying vulnerable servers. It writes: "WatchTowr has not reported any instances of attackers successfully achieving remote code execution." It also said that at the time of writing there did not appear to be other reports of exploitation attempts. That was two days before the CISA listing and describes that moment only. The page links to a post from watchTowr's account on X, which needs a login and was not read, so watchTowr's observations rest here on SecurityWeek alone.

SecurityWeek also reports that one of the people who reported the flaws published technical detail and proof of concept code that week. This site did not open, link or reproduce either. A team should not assume that exploitation needs private knowledge.

Where the sources differ

Differences between the saved pages, left unresolved
Point One reading Another reading
What the role check flaw allows CISA: operations protected solely by service level role checks. The advisory: restrictions held only in service security, while layer and data rules still apply SecurityWeek: operations typically reserved for administrators
Which flaws reach code execution without a login CISA: each listed flaw can be chained with four named CVEs, five in all SecurityWeek: Eye Security demonstrated it by combining CVE-2026-120704, CVE-2026-120705 and CVE-2026-129245. CVE-2026-120704 is not among CISA's five
Exploitation CISA: both listed on 27 November. SecurityWeek, 25 November: attempts seen by watchTowr, no success reported The project post and the two listed advisories say nothing about exploitation
CVE-2026-129245 and the older lines Project post and advisory: patched in 2.28.6 and 2.27.7 The 2.28.6 and 2.27.7 notices do not list it
Release dates Release notices: 19 October for all three GitHub release records: 17 October, 18 October and 2 November
Package for the 2.x WFS module XML injection advisory: gs-wfs-core CVE-2026-129244 advisory: gs-wfs for 2.x

The second row is the one that affects planning. CVE-2026-120704, rated High by the project and not on the catalogue, appears in a combination that SecurityWeek attributes to a second finder. Dealing with the two catalogue entries one by one is not the same as closing every route that has been reported. The project's fixed versions are listed against the whole October set.

What to do, in order

The project's and CISA's guidance comes first. The mitigations are summarised from the advisories as defensive settings, with no request examples. The suggestions in the second list are this site's own.

Take this with you
From the GeoServer project, its advisories and CISA
Project: update to GeoServer 3.0.2, 2.28.6 or 2.27.7. Treat 2.27.7 as a stopgap, since the 2.27 line is at end of life, and plan a move to a supported line.
CISA: apply mitigations as the vendor instructs and follow BOD 26-04 where it applies to you; discontinue use of the product if mitigations are not available. Due date 30 November.
CVE-2026-120705, until updated: restrict or disable WFS for anonymous users using service security, or disable WFS if it is not required. Read this with the next item.
CVE-2026-129243, until updated: at a proxy in front of GeoServer, block requests that name a service in the altered form the advisory describes, in both places it names. This brief does not print the match condition; take it from the advisory.
CVE-2026-129243: review the data directory folders wfs/query and workspaces/*/wfs/query for stored queries you did not create. The advisory says the fix itself needs no manual steps.
CVE-2026-129245, if not yet updated: remove rememberme from the web filter chain (Security > Authentication, filter chain web). Otherwise change the key in security/config.xml to a long random value, and protect the data directory from disclosure.
CVE-2026-129245, after updating: existing remember-me cookies are invalidated. A cluster sets a shared key with the GEOSERVER_REMEMBERME_KEY application property. The advisory says: "If you suspect exposure, change administrator passwords."
CVE-2026-129242: limit administrator access to trusted users and restrict the REST API resource and security endpoints to trusted networks; the advisory names them. It says the fix needs no manual steps.
CVE-2026-129244: the advisory says no mitigation is needed beyond upgrading.

Take this with you
This site's suggestions
List every GeoServer instance and its running version, including test copies, containers and GeoServer bundled inside other products. Do not rely on a CVE feed to find them yet.
Check from your own firewall, proxy and DNS records which instances can be reached from the internet, and take those first.
Record which extensions and community modules are installed. That scopes other October flaws; it does not rule out the two catalogue entries.
Before changing anything on an exposed instance, keep copies of the logs, the stored query folders and the list of administrator accounts, so that a later review has something to compare.
Carry out the stored query review even after updating. An update does not show what happened before it. An unexpected entry is a reason to open an incident; finding none does not clear the server.
After updating, confirm the running version on every node, not only the version that was deployed.
If you build your own software on GeoTools, check the gt-metadata version against the ranges in the table above.
Keep dated copies of the catalogue entries, the project post, the advisories and the release notice for your line.

The question the record leaves open

CISA lists both flaws as known exploited. No page read here says since when, and the listing came 39 days after the release notices. If one of your servers ran an affected version for part of that time or longer, what record would show whether somebody used it before the update, and who has looked?

Key facts

Sources
Primary Known Exploited Vulnerabilities catalogue, JSON version 2026.11.27 released 18:03 UTC: both GeoServer entries, dates, flags, descriptions and required action; catalogue status of every CVE named CISA accessed 2026-11-27
Primary Post dated 23 November 2026 on the vulnerabilities fixed by the October releases: update advice, CVE list, ratings and add-on labels GeoServer project accessed 2026-11-27
Primary Advisory for CVE-2026-120705: affected and fixed versions, CVSS 3.1 vector and score, impact, mitigation GeoServer project, GitHub security advisory accessed 2026-11-27
Primary Advisory for CVE-2026-129243: affected and fixed versions, CVSS 4.0 vector and score, impact, mitigation GeoServer project, GitHub security advisory accessed 2026-11-27
Primary Advisory for CVE-2026-129245: versions, rating, mitigation and resolution only were used GeoServer project, GitHub security advisory accessed 2026-11-27
Primary Advisory for CVE-2026-129242: versions, rating, mitigation and resolution only were used GeoServer project, GitHub security advisory accessed 2026-11-27
Primary Advisory for CVE-2026-129244: packages, versions, rating, mitigation and resolution only were used GeoServer project, GitHub security advisory accessed 2026-11-27
Primary GeoServer 3.0.2 release notice dated 19 October 2026: security list and fix tickets GeoServer project accessed 2026-11-27
Primary GeoServer 2.28.6 release notice dated 19 October 2026: security list and fix tickets GeoServer project accessed 2026-11-27
Primary GeoServer 2.27.7 release notice dated 19 October 2026: security list, fix tickets and end of life statement GeoServer project accessed 2026-11-27
Primary Release record for tag 3.0.2: publication time GitHub, geoserver/geoserver release record accessed 2026-11-27
Primary Release record for tag 2.28.6: publication time GitHub, geoserver/geoserver release record accessed 2026-11-27
Primary Release record for tag 2.27.7: publication time GitHub, geoserver/geoserver release record accessed 2026-11-27
Primary API query for CVE-2026-120705, which returned no record when read NIST National Vulnerability Database accessed 2026-11-27
Primary API query for CVE-2026-129243, which returned no record when read NIST National Vulnerability Database accessed 2026-11-27
Reported by Secondary report dated 25 November 2026: what watchTowr observed, report timing, a three flaw combination attributed to Eye Security SecurityWeek accessed 2026-11-27
Share this briefing
Know someone who owns this problem? Send it to them.
LinkedIn X WhatsApp Email Copy link

Related briefings
Threat Intel 27 Nov 2026
AhnLab ASEC says tampered Q-Dir and DesktopOK installers on SoftwareOK drop a Python RAT
What AhnLab ASEC says about tampered Q-Dir and DesktopOK installers: five versions confirmed to date, 17 malicious hashes (derived), the install paths and task, what is not stated, and what to check.

Threat Intel 27 Nov 2026
US DOJ says anti-scam surge targeted over 800 defendants; FBI cites nearly $17 billion restrained
What the 24 November 2026 anti-scam release counts, which period each figure covers, why the FBI's nearly $17 billion cannot be read as a surge result, and what the release leaves out.

Threat Intel 27 Nov 2026
eSentire says Setup Assistant, a Microsoft Store app, was a backdoor used to deploy Vinci RAT
Read 27 November 2026: eSentire ties a Microsoft Store app to the Vinci RAT PowerShell trojan in one intrusion. It gives no install or victim count and names no actor. Indicators, signals and what to do.

The briefing, in your inbox
Practitioner analysis of cyber and AI security news. No vendor noise.

<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://cyfar.ca/posts/danfoss-ak-sm-8xxa-series-cve-2026-129713 -->
<!-- fetched_at: 2026-11-25 07:33:57 -->
<!-- sha256: 9edb14d536bcd70d62e244b2700edd87ba7cd7cd4f40ccfc020d08a753ced79b -->

Danfoss AK-SM 8xxA Series (CVE-2026-129713) · cyfar.ca
Skip to content
Indicators of Compromise 1
View list .txt .json

1 cve
Improve this report Send corrections, useful missing information, or quality feedback. It is private and will not appear as a comment.

Detection / Hunter CISO Brief SOC View Plain English

Detection / Hunter · DeepSeek
Immediate Actions

Remove internet exposure from AK-SM 8xxA controllers; block inbound HTTP/S to their web interfaces.

Apply Danfoss AK-SM 800A 5.5.x when published.

Alert on unexpected webserver restarts on AK-SM 8xxA controllers.

Key Takeaways

CVSS 3.1 base 9.8 and CVSS 4.0 base 9.3; no privileges or user interaction required.

Carlo Meijer of Midnight Blue reported the flaw.

Danfoss will remove the ability to disable Strict Mode in future releases.

Attack Chain

Reconnaissance
Attacker locates an internet-exposed AK-SM 8xxA controller web interface

Exploitation
Crafted HTTP/S POST corrupts memory and restarts the webserver

Affected Systems

Danfoss AK-SM 8xxA Series controllers, firmware 5.4.0 and earlier

Vulnerabilities (CVEs)

copy: tsv md
CVE Product Severity Description
CVE-2026-129713 Danfoss AK-SM 8xxA Series controller CGI handler Critical Unauthenticated stack-based buffer overflow via crafted HTTP/S POST causes memory corruption and webserver restart.

Recommendations

Infrastructure Hardening

Require VPN for remote access.

MITRE ATT&CK Mapping

MITRE ATT&CK Mapping 2 technique s
Tactic Initial Access

T1190 Exploit Public-Facing Application

Tactic Impact

T1499 Endpoint Denial of Service

IOCs · 1 copy all show refanged .txt .json

Showing defanged values cve CVE-2026-129713 Unauthenticated stack-based buffer overflow via crafted HTTP/S POST causes memory corruption and webserver restart.

Related
Freeze the Controller, Defrost the Food: Uncovering Vulnerabilities in Danfoss Refrigeration Controllers · 4
Siemens Desigo, Gridscale (CVE-2026-111497) · 4
The Pitboss Pipeline: NetScaler Log Poisoning and a FreeBSD Sliver Implant Engagement · 1

Follow Subscribe via RSS

Contents

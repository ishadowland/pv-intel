<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://cyfar.ca/posts/libumqtt-cve-2026-125132 -->
<!-- fetched_at: 2026-11-20 07:11:55 -->
<!-- sha256: 64ec7b341db3e822c3cbf49a766644d760082a2edb79d042d8f9312e3ba0262c -->

libumqtt (CVE-2026-125132) · cyfar.ca
Skip to content
Indicators of Compromise 1
View list .txt .json

1 cve
Improve this report Send corrections, useful missing information, or quality feedback. It is private and will not appear as a comment.

Detection / Hunter CISO Brief SOC View

Detection / Hunter · DeepSeek
Immediate Actions

Remove libumqtt-based MQTT endpoints from internet exposure; place behind a firewall.

Key Takeaways

CWE-191 integer underflow in MQTT parsing.

CVSS 3.1 vector AV:N/AC:L/PR:N/UI:N.

Reported by Joseph Devasia; advisory published 2026-11-19.

Attack Chain

Exploitation: A crafted MQTT packet triggers integer underflow during parsing.

Impact: Denial of service, memory corruption, or information disclosure.

Affected Systems

libumqtt 1.1.1 and earlier

MQTT-connected ICS devices in critical manufacturing, energy, water

Transportation systems and IT networks using libumqtt

Vulnerabilities (CVEs)

copy: tsv md
CVE Product Severity Description
CVE-2026-125132 libumqtt High Integer underflow in MQTT parsing allows remote denial of service, memory corruption, or information disclosure.

Detection Engineering Assessment

Hunting Hypotheses

copy: tsv md
Hypothesis Telemetry Stage FP Risk
Malformed MQTT packets from one remote source correlate with broker crashes or restarts (T1499). MQTT broker logs Impact Medium — buggy clients also send malformed packets

Required Log Sources

MQTT broker connection and error logs

Network flow records for MQTT ports

IDS/IPS alerts for malformed MQTT packets

Recommendations

Infrastructure Hardening

Restrict MQTT broker reachability to known client addresses.

MITRE ATT&CK Mapping

MITRE ATT&CK Mapping 3 technique s
Tactic Initial Access

T1190 Exploit Public-Facing Application

Tactic Impact

T1499 Endpoint Denial of Service T1499.004 Application or System Exploitation

IOCs · 1 copy all show refanged .txt .json

Showing defanged values cve CVE-2026-125132 Integer underflow in MQTT parsing allows remote denial of service, memory corruption, or information disclosure.

Related
Siemens RUGGEDCOM APE1808 (CVE-2026-111497) · 3
Siemens RUGGEDCOM APE1808 (CVE-2026-109618, CVE-2026-109619) · 3
Security Advisory 2026-020 · 3

Stay current Subscribe via RSS

Contents

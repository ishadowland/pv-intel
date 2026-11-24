<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.tenable.com/cve/CVE-2026-120387 -->
<!-- fetched_at: 2026-11-25 07:19:25 -->
<!-- sha256: 0bd88fa0cd458c2c2ff5145f3554c922ff9771489ebbea2dc9931a851861b1d5 -->

CVE-2026-120387 | Tenable®
Plugins
Overview
Plugins Pipeline
Newest
Updated
Search
Nessus Families
WAS Families
NNM Families
Tenable OT Security Families
Tenable Cloud Security Families
Tenable Self-Hosted Container Security Families
About Plugin Families
Release Notes

Audits
Overview
Newest
Updated
Search Audit Files
Search Items
References
Authorities
Documentation
Download All Audit Files

Indicators
Overview
Search
Indicators of Attack
Indicators of Exposure
Release Notes

CVEs
Overview
Newest
Updated
Search

Attack Path Techniques
Overview
Search

Links
Tenable Cloud
Tenable Community & Support
Tenable University

Settings
Severity
CVSS v2 CVSS v3 CVSS v4

Theme
Light Dark Auto

Detections
Plugins
Overview
Plugins Pipeline
Release Notes
Newest
Updated
Search
Nessus Families
WAS Families
NNM Families
Tenable OT Security Families
Tenable Cloud Security Families
Tenable Self-Hosted Container Security Families
About Plugin Families

Audits
Overview
Newest
Updated
Search Audit Files
Search Items
References
Authorities
Documentation
Download All Audit Files

Indicators
Overview
Search
Indicators of Attack
Indicators of Exposure
Release Notes

Analytics
CVEs
Overview
Newest
Updated
Search

Attack Path Techniques
Overview
Search

CVE-2026-120387
critical

Information
CPEs
Plugins
Description
An improper JWT signature verification vulnerability in CIRCUTOR PowerStudio SCADA WAVE desktop version allows an unauthenticated remote attacker to bypass authentication by submitting an unsigned JWT with the algorithm set to “none”. The shared JWT validation component accepts the token without verifying a cryptographic signature, allowing the attacker to impersonate another user and access protected functionality with that user's privileges.
References
https://github.com/Exploit-Garbage/0day-Rubbish?utm_source=chatgpt.com
https://euvd.enisa.europa.eu/vulnerability/EUVD-2026-126913
https://circutor.com/soporte/ciberseguridad/
https://0day-rubbish.com/blog/circutor-powerstudio-jwt-alg-none-identity-forgery?utm_source=chatgpt.com

Details
Source: Mitre , NVD
Published : 2026-11-17

Updated : 2026-11-17

Risk Information
CVSS v2
Base Score : 6.4

Vector : CVSS2#AV:N/AC:L/Au:N/C:P/I:P/A:N

Severity : Medium

CVSS v3
Base Score : 9.1

Vector : CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N

Severity : Critical

CVSS v4
Base Score : 10

Vector : CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H

Severity : Critical

EPSS
EPSS : 0.00405

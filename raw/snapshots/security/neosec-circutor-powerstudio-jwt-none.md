<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://intel.neosec.eu/en/cve/CVE-2026-120387 -->
<!-- fetched_at: 2026-11-25 07:12:49 -->
<!-- sha256: 837137d3c31b6d111136f27290bc7ee12058e17f452e91f993b203a645beeaaa -->

CIRCUTOR PowerStudio SCADA WAVE JWT Signature Validation Authentication Bypass (CVE-2026-120387) | NEOSEC Intel
Skip to main content

What is affected, what to do
An improper JWT signature verification vulnerability in CIRCUTOR PowerStudio SCADA WAVE desktop version allows an unauthenticated remote attacker to bypass authentication by submitting an unsigned JWT with the algorithm set to “none”. The shared JWT validation component accepts the token without verifying a cryptographic signature, allowing the attacker to impersonate another user and access protected functionality with that user's privileges.
An exploit is publicly available. Update Circutor PowerStudio SCADA Wave to version 24.11.17.0.
Affected Circutor PowerStudio SCADA Wave lt 24.8.0..24.11.17.0

Fixed in Circutor PowerStudio SCADA Wave 24.11.17.0

Not sure whether and how you are affected? Ask a question about this vulnerability
Metrics
10.0
XIEM Effective CVSS

Highest available CVSS rating from NVD and vendor data.
Source: Vendor (CNA), CVSS v4

10.0
CVSS v4

Severity Critical on the scale from 0 to 10.
Source: EUVD, CVE.org

0.4 %
EPSS score

Low — model estimates < 1% exploitation likelihood.
Source: FIRST EPSS, percentile 35.5

Show all metrics Severity Critical
Priority (0–325) The priority score is a consolidated metric that condenses several individual signals into a single, action-guiding ranking: technical severity (CVSS), exploitation likelihood (EPSS), known-exploited status (KEV) and the context of the affected asset. The aim is to answer the only truly important question in vulnerability management: what first?
Read in glossary
90.10 Methodology
Exploit maturity An exploit is code or a technique that specifically uses a concrete vulnerability to force unintended behaviour — such as executing code or escalating privileges. It is the tool that turns a theoretical flaw into a practical attack.
Read in glossary
PoC (publicly reported)
XIEM Effective CVSS XIEM® is the tiered managed-security operating model from NEOSEC and a registered trademark of NEOSEC GmbH. It extends classic SIEM — the central collection, normalisation and correlation of security-relevant events — with endpoint forensics, network visibility and deception technology, and consolidates them into three building tiers: Sentry, Orchestrate and Command.
Read in glossary
10.0 Methodology
CVSS v4 CVSS is the globally established, open standard for assessing the technical severity of a vulnerability on a scale from 0 to 10. It describes how easily a flaw can be exploited and what damage it can cause — but not how likely its actual exploitation is. CVSS and the complementary EPSS deliberately answer different questions.
Read in glossary
10.0
EPSS score The EPSS score is the absolute model output for an individual vulnerability: the estimated probability of real-world exploitation within the next 30 days, expressed as a value between 0 and 1 (i.e. 0 % to 100 %). A score of 0.42 means „the model estimates a 42 % chance of real-world exploitation within 30 days“.
Read in glossary
0.4 % Low — model estimates < 1% exploitation likelihood.
EPSS percentile The EPSS percentile is the relative position of a vulnerability within all EPSS-scored CVEs, expressed as a value between 0 and 1. A percentile of 0.90 means „this CVE has a higher EPSS score than 90 % of all other scored CVEs“. Unlike the EPSS score, it is not a probability — but a positioning within a ranking.
Read in glossary
35.5 Elevated — this CVE ranks above at least 10% of all CVEs scored today.
KEV status The KEV catalogue is a list maintained by the US authority CISA of vulnerabilities for which active exploitation in the wild has been confirmed. It answers not the question „how severe?“ but „is it already being attacked?“ — thereby sharply prioritising patching.
Read in glossary
—
Published 17.11.2026, 04:47 UTC
CISA assessment (SSVC) Exploitation: proof of concept · automatable · Technical impact: total Source: CISA Vulnrichment, as of 17 November 2026
CWE CWE is a catalogue of typical weakness types in software and hardware — such as flawed input validation, unsafe memory handling or poor authentication. Where a CVE names a concrete vulnerability in a concrete product, a CWE describes the underlying class of defect.
Read in glossary
CWE-347
Detection rules
No NEOSEC detection rule is available for this vulnerability yet.
Request a rule
Classification under NIS2 and CRA
Rule-based classification from exploitation status and severity. It does not replace a case-by-case assessment.
NIS2 NIS2 is EU Directive (EU) 2022/2555 to raise the level of cybersecurity across the Union. It substantially broadens obligations compared with the first NIS directive: more sectors, mandatory risk management, staged reporting duties and personal accountability of senior management.
Read in glossary
High technical severity: assess and remediate the vulnerability in vulnerability handling under Art. 21(2)(e) NIS2 and document the decision.
CRA The CRA is EU Regulation (EU) 2024/2847 setting horizontal cybersecurity requirements for „products with digital elements“ — from industrial controllers and software to connected consumer devices. For the first time manufacturers must ensure security across the entire product lifecycle, handle vulnerabilities and provide security updates.
Read in glossary
From 11.12.2027, Annex I Part II CRA requires manufacturers of affected products with digital elements to handle vulnerabilities without delay and provide security updates.
ISO/IEC 27001 ISO/IEC 27001 is the internationally leading standard for an information security management system (ISMS). It describes a risk-based, process-oriented framework to systematically plan, implement, review and improve information security.
Read in glossary
Control A.8.8, management of technical vulnerabilities: assess relevance to your systems, plan remediation and keep evidence.
Description
An improper JWT signature verification vulnerability in CIRCUTOR PowerStudio SCADA WAVE desktop version allows an unauthenticated remote attacker to bypass authentication by submitting an unsigned JWT with the algorithm set to “none”. The shared JWT validation component accepts the token without verifying a cryptographic signature, allowing the attacker to impersonate another user and access protected functionality with that user's privileges.
Source: ENISA EUVD , cvelistv5 , NVD (NIST) , CVE.org (MITRE)
Affected products
The following versions are affected. Older releases of the same product line are also vulnerable unless stated otherwise.

Affected products Vendor Product Affected versions Fixed in
Circutor PowerStudio SCADA Wave 24.8.0 – < 24.11.17.0
24.11.17.0

Vendors and products
CIRCUTOR
Weakness classes (CWE)
CWE-347 Improper Verification of Cryptographic Signature
Base
The product does not verify, or incorrectly verifies, the cryptographic signature for data.
Entry at MITRE CWE-347
Public exploit references
Publicly reported proof-of-concepts, exploit modules and detection templates for this vulnerability. NEOSEC links to the original sources only and does not provide any exploit code.

Public exploit references Source Reference Maturity Published
Reference tagged as exploit github.com (opens in a new tab) PoC (publicly reported) reported, not verified —

References & sources
0day-rubbish.com blog/circutor-powerstudio-jwt-alg-none-identity-forgery?utm_sou… Third-party advisory, euvd
circutor.com soporte/ciberseguridad Patch, euvd
github.com Exploit-Garbage/0day-Rubbish?utm_source=chatgpt.com Exploit, euvd
NVD (NIST) vuln/detail/CVE-2026-120387 euvd
Changes to this CVE
Who changed this CVE and when: NVD (analysis, affected products, CVSS ), the CVE publisher ( CNA ) and additional providers such as CISA (ADP).
17.11.2026 Record modified CISA ADP
CISA assessment (SSVC) : exploitation: proof of concept, automatable: yes

Show the original change Individual changes of this event as published by NVD Type Action Before After
SSVC assessment added —
{"id":"CVE-2026-120387","role":"CISA Coordinator","options":[{"exploitation":"poc"},{"automatable":"yes"},{"technicalImpact":"total"}],"version":"2.0.3","timestamp":"2026-11-17T18:40:54.316363Z"}

Source identifier : 134c704f-9b21-4f2e-91b3-4a467353bcc0

17.11.2026 Received 59aea6fb…
CVSS V4.0 : AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H
Weakness type : CWE-347
Description added or changed
New references: https://0day-rubbish.com/blog/circutor-powerstudio-jwt-alg-none-identity-forgery?utm_source=chatgpt.com
https://circutor.com/soporte/ciberseguridad/
https://github.com/Exploit-Garbage/0day-Rubbish?utm_source=chatgpt.com

Show 7 original changes Individual changes of this event as published by NVD Type Action Before After
Description added —
An improper JWT signature verification vulnerability in CIRCUTOR PowerStudio SCADA WAVE desktop version allows an unauthenticated remote attacker to bypass authentication by submitting an unsigned JWT with the algorithm set to “none”. The shared JWT validation component accepts the token without verifying a cryptographic signature, allowing the attacker to impersonate another user and access protected functionality with that user's privileges.

CVSS added —
AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H/E:X/CR:X/IR:X/AR:X/MAV:X/MAC:X/MAT:X/MPR:X/MUI:X/MVC:X/MVI:X/MVA:X/MSC:X/MSI:X/MSA:X/S:X/AU:X/R:X/V:X/RE:X/U:X

Weakness type (CWE) added —
CWE-347

Affected versions (publisher) added —
New affected value received. <a href="https://github.com/CVEProject/cvelistV5/blob/main/cves/2026/120xxx/CVE-2026-120387.json">CVE-2026-120387</a>

Reference added —
https://0day-rubbish.com/blog/circutor-powerstudio-jwt-alg-none-identity-forgery?utm_source=chatgpt.com

Reference added —
https://circutor.com/soporte/ciberseguridad/

Reference added —
https://github.com/Exploit-Garbage/0day-Rubbish?utm_source=chatgpt.com

Source identifier : 59aea6fb-2240-4284-b9fd-48e3851c2128

Embed badge Show the severity and KEV status of this vulnerability on your site – with a link back here. The image is updated hourly.
<a href="https://intel.neosec.eu/en/cve/CVE-2026-120387"><img src="https://intel.neosec.eu/badge/cve/CVE-2026-120387.svg?lang=en" alt="CVE-2026-120387 – NEOSEC Intel" height="20"></a>

<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-02 -->
<!-- fetched_at: 2026-11-26 07:10:55 -->
<!-- sha256: 1236d46326e0c3da088ae93e969232abf6eb75d113cd17755d371bd7f03e5f0d -->

Schneider Electric EcoStruxure Power Build Rapsody software | CISA

Skip to main content

Official websites use .gov

A .gov website belongs to an official government organization in the United States.

Secure .gov websites use HTTPS

A lock ( Lock A locked padlock ) or https:// means you’ve safely connected to the .gov website. Share sensitive information only on official, secure websites.

Search

Menu

Share:

Opens in a new window

Opens in a new window

Opens in a new window

ICS Advisory

Schneider Electric EcoStruxure Power Build Rapsody software

Release Date
November 24, 2026

Alert Code
ICSA-26-328-02

Related topics:

Industrial Control System Vulnerabilities
,
Industrial Control Systems

View CSAF

Summary

Schneider Electric is aware of a vulnerability in its EcoStruxure™ Power Build Rapsody product. The EcoStruxure™ Power Build Rapsody is used to enter or import the single line diagram, to get the extensive bill of material of your switchboard, including all devices, connection items, and mounting components. Failure to apply the remediations provided below may risk memory corruption, heap-based buffer overflow, and/or stack-based buffer overflow, which could result in local attackers being able to exploit these issues to potentially execute arbitrary code.

The following versions of Schneider Electric EcoStruxure Power Build Rapsody software are affected:

EcoStruxure Power Build Rapsody software vers:generic/<=2.9.1.0_FR, 2.9.12.0101_FR, vers:generic/<=2.8.5.0301_ESP, 2.9.5.0000_ESP, vers:generic/<=2.8.7.0101_PT, 2.9.7.0000_PT, vers:generic/<=2.8.8.0201_BEL(FR), 2.9.8.0000_BELFR, vers:generic/<=2.8.3.0201_BEL(EN), 2.9.3.0000_BELEN, vers:generic/<=2.8.4.0401_INT(EN), 2.9.4.0000_INTEN, vers:generic/<=2.8.6.0000_INT(FR), 2.9.6.0000_INTFR, vers:generic/<=2.8.2.0000_NL, 2.9.6.0000_NL (CVE-2026-119055, CVE-2026-119055, CVE-2026-119055, CVE-2026-119055, CVE-2026-119055, CVE-2026-119055, CVE-2026-119055, CVE-2026-119055)

CVSS
Vendor
Equipment

v3 5.3
Schneider Electric
EcoStruxure Power Build Rapsody software

1 Vulnerability

Use After Free

Background

Critical Infrastructure Sectors: Energy, Critical Manufacturing, Commercial Facilities

Countries/Areas Deployed: Worldwide

Company Headquarters Location: France

Vulnerabilities

CVE-2026-119055

A CWE- 416: Use After Free vulnerability exists that could cause arbitrary code execution when a local attacker could trick the end user to open a specially crafted malicious SSD file.

Read More

8 Affected Products

EcoStruxure Power Build Rapsody software Versions FR 2.9.1.0 and prior

Product Status: fixed, known_affected

Remediations

Vendor fix
Versions FR V2.9.12.0101, ESP V2.9.5.0000, PT V2.9.7.0000, BEL(FR) V2.9.8.0000, BEL(EN) V2.9.3.0000, INT(EN) V2.9.4.0000, INT(FR)V2.9.6.0000, NL V2.9.6.0000 of EcoStruxure™ Power Build Rapsody software includes a fix for this vulnerability and is available for download here: https://www.se.com/ww/en/product-country-selector/?pageType=product-range&sourceId=2309

EcoStruxure Power Build Rapsody software Versions ESP 2.8.5.0301 and prior

Product Status: fixed, known_affected

Remediations

Vendor fix
Versions FR V2.9.12.0101, ESP V2.9.5.0000, PT V2.9.7.0000, BEL(FR) V2.9.8.0000, BEL(EN) V2.9.3.0000, INT(EN) V2.9.4.0000, INT(FR)V2.9.6.0000, NL V2.9.6.0000 of EcoStruxure™ Power Build Rapsody software includes a fix for this vulnerability and is available for download here: https://www.se.com/ww/en/product-country-selector/?pageType=product-range&sourceId=2309

EcoStruxure Power Build Rapsody software Versions PT 2.8.7.0101 and prior

Product Status: fixed, known_affected

Remediations

Vendor fix
Versions FR V2.9.12.0101, ESP V2.9.5.0000, PT V2.9.7.0000, BEL(FR) V2.9.8.0000, BEL(EN) V2.9.3.0000, INT(EN) V2.9.4.0000, INT(FR)V2.9.6.0000, NL V2.9.6.0000 of EcoStruxure™ Power Build Rapsody software includes a fix for this vulnerability and is available for download here: https://www.se.com/ww/en/product-country-selector/?pageType=product-range&sourceId=2309

EcoStruxure Power Build Rapsody software Versions BEL(FR) 2.8.8.0201 and prior

Product Status: fixed, known_affected

Remediations

Vendor fix
Versions FR V2.9.12.0101, ESP V2.9.5.0000, PT V2.9.7.0000, BEL(FR) V2.9.8.0000, BEL(EN) V2.9.3.0000, INT(EN) V2.9.4.0000, INT(FR)V2.9.6.0000, NL V2.9.6.0000 of EcoStruxure™ Power Build Rapsody software includes a fix for this vulnerability and is available for download here: https://www.se.com/ww/en/product-country-selector/?pageType=product-range&sourceId=2309

EcoStruxure Power Build Rapsody software Versions BEL(EN) 2.8.3.0201 and prior

Product Status: fixed, known_affected

Remediations

Vendor fix
Versions FR V2.9.12.0101, ESP V2.9.5.0000, PT V2.9.7.0000, BEL(FR) V2.9.8.0000, BEL(EN) V2.9.3.0000, INT(EN) V2.9.4.0000, INT(FR)V2.9.6.0000, NL V2.9.6.0000 of EcoStruxure™ Power Build Rapsody software includes a fix for this vulnerability and is available for download here: https://www.se.com/ww/en/product-country-selector/?pageType=product-range&sourceId=2309

EcoStruxure Power Build Rapsody software Versions INT(EN) 2.8.4.0401 and prior

Product Status: fixed, known_affected

Remediations

Vendor fix
Versions FR V2.9.12.0101, ESP V2.9.5.0000, PT V2.9.7.0000, BEL(FR) V2.9.8.0000, BEL(EN) V2.9.3.0000, INT(EN) V2.9.4.0000, INT(FR)V2.9.6.0000, NL V2.9.6.0000 of EcoStruxure™ Power Build Rapsody software includes a fix for this vulnerability and is available for download here: https://www.se.com/ww/en/product-country-selector/?pageType=product-range&sourceId=2309

EcoStruxure Power Build Rapsody software Versions INT(FR) 2.8.6.0000 and prior

Product Status: fixed, known_affected

Remediations

Vendor fix
Versions FR V2.9.12.0101, ESP V2.9.5.0000, PT V2.9.7.0000, BEL(FR) V2.9.8.0000, BEL(EN) V2.9.3.0000, INT(EN) V2.9.4.0000, INT(FR)V2.9.6.0000, NL V2.9.6.0000 of EcoStruxure™ Power Build Rapsody software includes a fix for this vulnerability and is available for download here: https://www.se.com/ww/en/product-country-selector/?pageType=product-range&sourceId=2309

EcoStruxure Power Build Rapsody software Versions NL 2.8.2.0000 and prior

Product Status: fixed, known_affected

Remediations

Vendor fix
Versions FR V2.9.12.0101, ESP V2.9.5.0000, PT V2.9.7.0000, BEL(FR) V2.9.8.0000, BEL(EN) V2.9.3.0000, INT(EN) V2.9.4.0000, INT(FR)V2.9.6.0000, NL V2.9.6.0000 of EcoStruxure™ Power Build Rapsody software includes a fix for this vulnerability and is available for download here: https://www.se.com/ww/en/product-country-selector/?pageType=product-range&sourceId=2309

Additional Metrics

Relevant CWE: CWE-416 Use After Free

CVSS Version
Base Score
Base Severity
Vector String

3.1
5.3
MEDIUM
CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:L/I:L/A:L

View CVE Details

Acknowledgments

Schneider Electric CPCERT reported this vulnerability to CISA.

Recommended Practices

CISA recommends users take defensive measures to minimize the risk of exploitation of these vulnerabilities.

Minimize network exposure for all control system devices and/or systems, ensuring they are not accessible from the internet .

Locate control system networks and remote devices behind firewalls and isolating them from business networks.

When remote access is required, use more secure methods, such as Virtual Private Networks (VPNs), recognizing VPNs may have vulnerabilities and should be updated to the most current version available. Also recognize VPN is only as secure as the connected devices.

CISA reminds organizations to perform proper impact analysis and risk assessment prior to deploying defensive measures.

CISA also provides a section for control systems security recommended practices on the ICS webpage on cisa.gov/ics . Several CISA products detailing cyber defense best practices are available for reading and download, including Improving Industrial Control Systems Cybersecurity with Defense-in-Depth Strategies .

CISA encourages organizations to implement recommended cybersecurity strategies for proactive defense of ICS assets .

Additional mitigation guidance and recommended practices are publicly available on the ICS webpage at cisa.gov/ics in the technical information paper, ICS-TIP-12-146-01B--Targeted Cyber Intrusion Detection and Mitigation Strategies .

Organizations observing suspected malicious activity should follow established internal procedures and report findings to CISA for tracking and correlation against other incidents.

Advisory Conversion Disclaimer

This ICSA is a verbatim republication of Schneider Electric CPCERT SEVD-2026-314-01 from a direct conversion of the vendor's Common Security Advisory Framework (CSAF) advisory. This is republished to CISA's website as a means of increasing visibility and is provided "as-is" for informational purposes only. CISA is not responsible for the editorial or technical accuracy of republished advisories and provides no warranties of any kind regarding any information contained within this advisory. Further, CISA does not endorse any commercial product or service. Please contact Schneider Electric CPCERT directly for any questions regarding this advisory.

Revision History

Initial Release Date: 2026-11-10

Date
Revision
Summary

2026-11-10
1
Original Release

2026-11-24
2
Initial CISA Republication of Schneider Electric CPCERT SEVD-2026-314-01 advisory

Legal Notice and Terms of Use

This product is provided subject to this Notification and this Privacy & Use policy.

Vendor

Schneider Electric

Tags

Sector :
Commercial Facilities Sector ,
Critical Manufacturing Sector ,
Energy Sector

Topics :
Industrial Control System Vulnerabilities ,
Industrial Control Systems

Please share your thoughts

We recently updated our anonymous product survey ; we welcome your feedback.

Related Advisories

Nov 24, 2026

ICS Advisory | ICSA-26-328-01

AutomationDirect C-More EA9 Programming Software

Nov 24, 2026

ICS Advisory | ICSA-26-328-03

Danfoss AK-SM 8xxA Series

Nov 19, 2026

ICS Advisory | ICSA-26-323-03

libumqtt

Nov 19, 2026

ICS Advisory | ICSA-26-323-02

Elecbrakes EB2, VM1, ELBC2000

<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-02 -->
<!-- fetched_at: 2026-11-18 07:11:19 -->
<!-- sha256: 8dc8c9d070635a1f59fd8216d5afadd6b2e9734b2d1a63b67099268d16129c38 -->

Siemens .NET Client Library for SIMATIC S7 Webserver API | CISA

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

Siemens .NET Client Library for SIMATIC S7 Webserver API

Release Date
November 17, 2026

Alert Code
ICSA-26-321-02

Related topics:

Industrial Control System Vulnerabilities
,
Industrial Control Systems

View CSAF

Summary

.NET Client Library for SIMATIC S7 Webserver API contains multiple vulnerabilities that could allow an attacker to obtain sensitive information or write arbitrary files outside the intended download directory. Siemens has released a new version for .NET Client Library for SIMATIC S7 Webserver API and recommends to update to the latest version.

The following versions of Siemens .NET Client Library for SIMATIC S7 Webserver API are affected:

.NET Client Library for SIMATIC S7 Webserver API vers:intdot/<3.3.61, vers:intdot/<3.3.62 (CVE-2026-85114, CVE-2026-85115)

CVSS
Vendor
Equipment

v3 7.5
Siemens
.NET Client Library for SIMATIC S7 Webserver API

2 Vulnerabilities

Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal'), Generation of Error Message Containing Sensitive Information

Background

Critical Infrastructure Sectors: Critical Manufacturing

Countries/Areas Deployed: Worldwide

Company Headquarters Location: Germany

Vulnerabilities

Expand All +

CVE-2026-85114

Affected applications do not properly validate filenames received from remote servers during ticket downloads. This could allow an attacker who can manipulate the ticket response to write arbitrary files outside the intended download directory and, when overwriting is enabled, replace existing files accessible to the application.

Read More

1 Affected Product

.NET Client Library for SIMATIC S7 Webserver API < V3.3.61

Product Status: known_affected

Remediations

Vendor fix
Update to V3.3.61 or later version

Additional Metrics

Relevant CWE: CWE-22 Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal')

CVSS Version
Base Score
Base Severity
Vector String

3.1
7.5
HIGH
CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:N

View CVE Details

CVE-2026-85115

Affected applications do not properly redact PLC restore passwords from HTTP error exception messages. This could allow an attacker with access to logs or other diagnostic output to obtain the plaintext restore password and potentially perform unauthorized operations on the PLC.

Read More

2 Affected Products

.NET Client Library for SIMATIC S7 Webserver API < V3.3.61

Product Status: known_affected

Remediations

.NET Client Library for SIMATIC S7 Webserver API < V3.3.62

Product Status: known_affected

Remediations

Vendor fix
Update to V3.3.62 or later version

Additional Metrics

Relevant CWE: CWE-209 Generation of Error Message Containing Sensitive Information

CVSS Version
Base Score
Base Severity
Vector String

3.1
5.5
MEDIUM
CVSS:3.1/AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N

View CVE Details

Acknowledgments

Siemens ProductCERT reported these vulnerabilities to CISA.

General Recommendations

As a general security measure, Siemens strongly recommends to protect network access to devices with appropriate mechanisms. In order to operate the devices in a protected IT environment, Siemens recommends to configure the environment according to Siemens' operational guidelines for Industrial Security (Download: https://www.siemens.com/cert/operational-guidelines-industrial-security), and to follow the recommendations in the product manuals. Additional information on Industrial Security by Siemens can be found at: https://www.siemens.com/industrialsecurity

Additional Resources

For further inquiries on security vulnerabilities in Siemens products and solutions, please contact the Siemens ProductCERT: https://www.siemens.com/cert/advisories

Terms of Use

The use of Siemens Security Advisories is subject to the terms and conditions listed on: https://www.siemens.com/productcert/terms-of-use.

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

This ICSA is a verbatim republication of Siemens ProductCERT SSA-390352 from a direct conversion of the vendor's Common Security Advisory Framework (CSAF) advisory. This is republished to CISA's website as a means of increasing visibility and is provided "as-is" for informational purposes only. CISA is not responsible for the editorial or technical accuracy of republished advisories and provides no warranties of any kind regarding any information contained within this advisory. Further, CISA does not endorse any commercial product or service. Please contact Siemens ProductCERT directly for any questions regarding this advisory.

Revision History

Initial Release Date: 2026-10-13

Date
Revision
Summary

2026-10-13
1
Publication Date

2026-11-10
2
Added researcher acknowledgement

2026-11-17
3
Initial CISA Republication of Siemens ProductCERT SSA-390352 advisory

Legal Notice and Terms of Use

This product is provided subject to this Notification and this Privacy & Use policy.

Vendor

Siemens

Tags

Sector :
Critical Manufacturing Sector

Topics :
Industrial Control System Vulnerabilities ,
Industrial Control Systems

Please share your thoughts

We recently updated our anonymous product survey ; we welcome your feedback.

Related Advisories

Nov 17, 2026

ICS Advisory | ICSA-26-321-01

Dorsett Controls InfoScan

Nov 17, 2026

ICS Advisory | ICSA-26-321-04

Siemens Industrial Software Products

Nov 17, 2026

ICS Advisory | ICSA-26-321-11

Siemens meta-iot2050

Nov 17, 2026

ICS Advisory | ICSA-26-321-03

Siemens Industrial Automation Software Products

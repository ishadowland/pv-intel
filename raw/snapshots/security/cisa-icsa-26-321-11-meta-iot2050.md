<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-11 -->
<!-- fetched_at: 2026-11-18 07:10:56 -->
<!-- sha256: be6548c1cc9779f8b019fd13ed375f1449d634cafbf3eb7dc88badc801a62a32 -->

Siemens meta-iot2050 | CISA

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

Siemens meta-iot2050

Release Date
November 17, 2026

Alert Code
ICSA-26-321-11

Related topics:

Industrial Control System Vulnerabilities
,
Industrial Control Systems

View CSAF

Summary

meta-iot2050 (https://github.com/siemens/meta-iot2050) from V01.03.01 contains a Command Injection vulnerability in the firmware update tool that could allow an attacker which is able to manipulate a configuration file to have arbitrary commands run as root. Siemens is preparing fixes and recommends mitigations for products where fixes are not or not yet available.

The following versions of Siemens meta-iot2050 are affected:

meta-iot2050 vers:intdot/>=01.03.01 (CVE-2026-109830)

CVSS
Vendor
Equipment

v3 7.3
Siemens
meta-iot2050

1 Vulnerability

Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')

Background

Critical Infrastructure Sectors: Critical Manufacturing, Energy, Information Technology

Countries/Areas Deployed: Worldwide

Company Headquarters Location: Germany

Vulnerabilities

CVE-2026-109830

Affected devices take parts from a configuration file and execute them unchecked. This could allow an attacker which is able to manipulate the configuration file to make the user execute arbitrary code on the device.

Read More

1 Affected Product

meta-iot2050 >= V01.03.01

Product Status: known_affected

Remediations

None available
Currently no fix is available

Additional Metrics

Relevant CWE: CWE-78 Improper Neutralization of Special Elements used in an OS Command ('OS Command Injection')

CVSS Version
Base Score
Base Severity
Vector String

3.1
7.3
HIGH
CVSS:3.1/AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:H

View CVE Details

Acknowledgments

Siemens ProductCERT reported this vulnerability to CISA.

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

This ICSA is a verbatim republication of Siemens ProductCERT SSA-724261 from a direct conversion of the vendor's Common Security Advisory Framework (CSAF) advisory. This is republished to CISA's website as a means of increasing visibility and is provided "as-is" for informational purposes only. CISA is not responsible for the editorial or technical accuracy of republished advisories and provides no warranties of any kind regarding any information contained within this advisory. Further, CISA does not endorse any commercial product or service. Please contact Siemens ProductCERT directly for any questions regarding this advisory.

Revision History

Initial Release Date: 2026-11-10

Date
Revision
Summary

2026-11-10
1
Publication Date

2026-11-17
2
Initial CISA Republication of Siemens ProductCERT SSA-724261 advisory

Legal Notice and Terms of Use

This product is provided subject to this Notification and this Privacy & Use policy.

Vendor

Siemens

Tags

Sector :
Critical Manufacturing Sector ,
Energy Sector ,
Information Technology Sector

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

ICS Advisory | ICSA-26-321-03

Siemens Industrial Automation Software Products

Nov 17, 2026

ICS Advisory | ICSA-26-321-10

Siemens Simcenter Femap

Nov 17, 2026

ICS Advisory | ICSA-26-321-02

Siemens .NET Client Library for SIMATIC S7 Webserver API

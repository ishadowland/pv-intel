<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-316-03 -->
<!-- fetched_at: 2026-11-17 07:11:04 -->
<!-- sha256: 36c7d87c5baca836c68589aa67b01e7d26314274007a441cfececcd7b9a0641c -->

Siemens Industrial Edge Management | CISA

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

Siemens Industrial Edge Management

Release Date
November 12, 2026

Alert Code
ICSA-26-316-03

Related topics:

Industrial Control System Vulnerabilities
,
Industrial Control Systems

View CSAF

Summary

Siemens is currently assessing the impact of Node2Shell (CVE-2026-111497) on Industrial Edge. Please check your Industrial Edge Management (IEM) setup: - No Management Applications installed: No action is required. Although the affected Brotli library is included in the IEM software stack, the affected functionality is not used or exposed. The same applies to IEDK. - Management Applications installed: Follow the specific mitigations until a fix is available. - Device Applications installed: Follow the specific mitigations until a fix is available. For Siemens-managed services, Industrial Edge Hub and Industrial Edge Management Cloud, appropriate Firewall/WAF protection has already been implemented. Siemens has released new versions for several affected products and recommends to update to the latest versions. Siemens is preparing further fixes and recommends specific mitigations for products where fixes are not or not yet available.

The following versions of Siemens Industrial Edge Management are affected:

Cloud Connector Configurator vers:intdot/<1.24.3 (CVE-2026-111497)

Common Configurator (CC on IEM) vers:all/* (CVE-2026-111497)

Common Configurator on Device (CC on Edge) vers:all/* (CVE-2026-111497)

Data Flow Monitoring vers:intdot/<3.0.18 (CVE-2026-111497)

Databus Configurator vers:intdot/<4.0.1 (CVE-2026-111497)

DataXess Configurator vers:intdot/<1.5.7 (CVE-2026-111497)

Edge OPC UA Server Configurator vers:intdot/<2.3.10 (CVE-2026-111497)

Flow Creator Configurator vers:intdot/<1.15.1 (CVE-2026-111497)

Industrial Edge Hub vers:all/* (CVE-2026-111497)

Industrial Edge Management Cloud vers:all/* (CVE-2026-111497)

CVSS
Vendor
Equipment

v3 9.8
Siemens
Cloud Connector Configurator

1 Vulnerability

Out-of-bounds Write

Background

Critical Infrastructure Sectors: Critical Manufacturing

Countries/Areas Deployed: Worldwide

Company Headquarters Location: Germany

Vulnerabilities

CVE-2026-111497

A buffer overflow vulnerability in the Brotli decoder (c/dec/decode.c) in Google Brotli versions 1.0.3 through 1.2.0 on all platforms allows a remote unauthenticated attacker to corrupt adjacent decoder state memory, disclose sensitive memory contents, cause a denial of service, or potentially execute arbitrary code using a crafted Brotli-compressed stream. Users need to update any Brotli libraries or binaries between 1.0.3 through 1.2.0 to the latest available version: 1.0.10 or 1.1.1 or 1.2.1.

Read More

10 Affected Products

Cloud Connector Configurator < V1.24.3

Product Status: known_affected

Remediations

Vendor fix
Update to V1.24.3 or later version

Industrial Edge Management Cloud

Product Status: known_affected

Remediations

Vendor fix
Vulnerability fixed on central cloud service starting 2026-10-28; no user actions necessary

Common Configurator (CC on IEM)

Product Status: known_affected

Remediations

Mitigation
Uninstall all Management Applications and protect your IEM instance with a Firewall/WAF until a fix is available

None available
Currently no fix is available

Common Configurator on Device (CC on Edge)

Product Status: known_affected

Remediations

Mitigation
Stop Common Configurator on Device (CC on Edge) until a fix is available

None available
Currently no fix is available

Data Flow Monitoring < V3.0.18

Product Status: known_affected

Remediations

Vendor fix
Update to V3.0.18 or later version

Databus Configurator < V4.0.1

Product Status: known_affected

Remediations

Vendor fix
Update to V4.0.1 or later version

DataXess Configurator < V1.5.7

Product Status: known_affected

Remediations

Vendor fix
Update to V1.5.7 or later version

Edge OPC UA Server Configurator < V2.3.10

Product Status: known_affected

Remediations

Vendor fix
Update to V2.3.10 or later version

Flow Creator Configurator < V1.15.1

Product Status: known_affected

Remediations

Vendor fix
Update to V1.15.1 or later version

Industrial Edge Hub

Product Status: known_affected

Remediations

Vendor fix
Vulnerability fixed on central cloud service starting 2026-10-29; no user actions necessary

Additional Metrics

Relevant CWE: CWE-787 Out-of-bounds Write

CVSS Version
Base Score
Base Severity
Vector String

3.1
9.8
CRITICAL
CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

View CVE Details

Acknowledgments

Siemens ProductCERT reported this vulnerability to CISA.

General Recommendations

As a general security measure, Siemens strongly recommends protecting network access to devices with appropriate mechanisms. In order to operate the devices in a protected IT environment, Siemens recommends configuring the environment according to Siemens' operational guidelines for Industrial Security ( https://www.siemens.com/cert/operational-guidelines-industrial-security ), and to follow the recommendations in the product manuals. Additional information on Industrial Security by Siemens can be found at: https://www.siemens.com/industrialsecurity

Additional Resources

For further inquiries on security vulnerabilities in Siemens products and solutions, please contact the Siemens ProductCERT: https://www.siemens.com/cert/advisories

Terms of Use

The use of Siemens Security Advisories is subject to the terms and conditions listed on: https://www.siemens.com/productcert/terms-of-use .

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

This ICSA is a verbatim republication of Siemens ProductCERT SSA-443410 from a direct conversion of the vendor's Common Security Advisory Framework (CSAF) advisory. This is republished to CISA's website as a means of increasing visibility and is provided "as-is" for informational purposes only. CISA is not responsible for the editorial or technical accuracy of republished advisories and provides no warranties of any kind regarding any information contained within this advisory. Further, CISA does not endorse any commercial product or service. Please contact Siemens ProductCERT directly for any questions regarding this advisory.

Revision History

Initial Release Date: 2026-10-30

Date
Revision
Summary

2026-10-30
1
Publication Date

2026-11-06
2
Added fix for Cloud Connector Configurator, Data Flow Monitoring, Databus Configurator, Edge OPC UA Server Configurator and Flow Creator Configurator; Added DataXess Configurator as affected product

2026-11-12
3
Initial CISA Republication of Siemens ProductCERT SSA-443410 advisory

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

Nov 12, 2026

ICS Advisory | ICSA-26-316-02

Siemens Desigo, Gridscale

Nov 12, 2026

ICS Advisory | ICSA-26-316-04

Siemens RUGGEDCOM APE1808

Nov 12, 2026

ICS Advisory | ICSA-26-316-05

Siemens RUGGEDCOM APE1808

Nov 12, 2026

ICS Advisory | ICSA-26-316-01

Siemens Building Automation and Energy Products

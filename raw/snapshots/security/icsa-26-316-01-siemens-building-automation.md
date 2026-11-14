<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-316-01 -->
<!-- fetched_at: 2026-11-15 07:11:48 -->
<!-- sha256: dd22f6e6f11c9eeda1c0ee6a9b2ade386a0a10664c879965112f9112cc923456 -->

Siemens Building Automation and Energy Products | CISA

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

Siemens Building Automation and Energy Products

Release Date
November 12, 2026

Alert Code
ICSA-26-316-01

Related topics:

Industrial Control System Vulnerabilities
,
Industrial Control Systems

View CSAF

Summary

On October 21, 2026, the PHP project and security researchers disclosed two critical, unauthenticated remote code execution vulnerabilities in the core PHP language runtime known as "php2shell" (tracked as CVE-2026-109618 and CVE-2026-109619). This advisory covers the status of impact of various Siemens software products. As a general security measure, Siemens strongly recommends to protect network access to devices with appropriate mechanisms. In order to operate the devices in a protected IT environment, Siemens recommends to configure the environment according to Siemens' operational guidelines, and to follow the recommendations in the product manuals. Siemens is actively monitoring the situation and assessing the implications of these vulnerabilities on our portfolio. Because this evaluation is ongoing, our findings are subject to change as new technical details and vendor updates emerge. We will publish updated findings, guidance, and remediation recommendations as soon as they become available. Siemens has released new versions for several affected products and recommends to update to the latest versions. Siemens is preparing further fixes and recommends mitigations for products where fixes are not or not yet available.

The following versions of Siemens Building Automation and Energy Products are affected:

AMIS TS vers:all/* (CVE-2026-109618, CVE-2026-109619)

blueplanet 360 NX3 M6 WM OD IISX vers:all/* (CVE-2026-109618, CVE-2026-109619)

blueplanet 360 NX3 M6 WM OD IISX - S vers:all/* (CVE-2026-109618, CVE-2026-109619)

Energy Engage V2.0SP9 vers:all/* (CVE-2026-109618, CVE-2026-109619)

Energy Engage V3.1SP1 vers:all/* (CVE-2026-109618, CVE-2026-109619)

Heliox Rapid vers:all/* ()Local Monitoring bt-monitoring-vm vers:intdot/<20261103 (CVE-2026-109618, CVE-2026-109619)

Spectrum Power 3 vers:all/* (CVE-2026-109619)

Spectrum Power 4 vers:all/*, vers:all/*, vers:all/* (CVE-2026-109618, CVE-2026-109619, CVE-2026-109618, CVE-2026-109619, CVE-2026-109618, CVE-2026-109619)

Spectrum Power 7 vers:all/* (CVE-2026-109618, CVE-2026-109619)

Spectrum Power TG vers:all/* (CVE-2026-109618, CVE-2026-109619)

CVSS
Vendor
Equipment

v3 9.8
Siemens
AMIS TS

1 Vulnerability

Use After Free

Background

Critical Infrastructure Sectors: Energy

Countries/Areas Deployed: Worldwide

Company Headquarters Location: Germany

Vulnerabilities

Expand All +

CVE-2026-109618

PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some contexts may not properly account for this scenario and leave request memory in an uninitialized state before performing an allocation. The subsequent request cleanup procedure may read or branch on this memory. Multiple OOM strategies can consistently trigger this condition and lead to remote code execution (RCE).

Read More

11 Affected Products

AMIS TS

Product Status: known_affected, known_not_affected

Remediations

None available
Currently no fix is available

blueplanet 360 NX3 M6 WM OD IISX

Product Status: known_affected, known_not_affected

Remediations

None available
Currently no fix is available

Energy Engage V2.0SP9

Product Status: known_affected, known_not_affected

Remediations

No fix planned
Currently no fix is planned

Energy Engage V3.1SP1

Product Status: known_affected, known_not_affected

Remediations

Vendor fix
Upgrade PHP version to V8.1.34 release 6

blueplanet 360 NX3 M6 WM OD IISX - S

Product Status: known_affected, known_not_affected

Remediations

None available
Currently no fix is available

Local Monitoring bt-monitoring-vm < V20261103

Product Status: known_affected, known_not_affected

Remediations

Vendor fix
Update to V20261103 or later version

Spectrum Power 4 using Nagios or Zabbix

Product Status: known_affected, known_not_affected

Remediations

None available
Currently no fix is available

Spectrum Power 4 with Web Office Portal V3.0, V3.1 and V3.2

Product Status: known_affected, known_not_affected

Remediations

None available
Currently no fix is available

Spectrum Power 4 with HISViews V1.0

Product Status: known_affected, known_not_affected

Remediations

None available
Currently no fix is available

Spectrum Power 7 using IHM (NagiosXI)

Product Status: known_affected, known_not_affected

Remediations

Vendor fix
Red Hat released a PHP security patch for RHEL 8 and 9

Spectrum Power TG which are based on Microsoft Windows using the WebConsole and WebQuery components

Product Status: known_affected, known_not_affected

Remediations

Vendor fix
Upgrade PHP version to V8.5.12

Additional Metrics

Relevant CWE: CWE-416 Use After Free

CVSS Version
Base Score
Base Severity
Vector String

3.1
9.8
CRITICAL
CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

View CVE Details

CVE-2026-109619

PHP has various global state that temporarily points into request memory. In some scenarios, global state may not be correctly reset, or may be repopulated after being reset. The global state may then refer to request memory even after it has been freed. Subsequent requests may read or branch on this stale state before it is fully initialized. Multiple strategies can trigger this condition and produce remote code execution (RCE).

Read More

23 Affected Products

AMIS TS

Product Status: known_affected, known_not_affected

Remediations

None available
Currently no fix is available

blueplanet 360 NX3 M6 WM OD IISX

Product Status: known_affected, known_not_affected

Remediations

None available
Currently no fix is available

Energy Engage V2.0SP9

Product Status: known_affected, known_not_affected

Remediations

No fix planned
Currently no fix is planned

Energy Engage V3.1SP1

Product Status: known_affected, known_not_affected

Remediations

Vendor fix
Upgrade PHP version to V8.1.34 release 6

blueplanet 360 NX3 M6 WM OD IISX - S

Product Status: known_affected, known_not_affected

Remediations

None available
Currently no fix is available

Local Monitoring bt-monitoring-vm < V20261103

Product Status: known_affected, known_not_affected

Remediations

Vendor fix
Update to V20261103 or later version

Spectrum Power 4 using Nagios or Zabbix

Product Status: known_affected, known_not_affected

Remediations

None available
Currently no fix is available

Spectrum Power 4 with Web Office Portal V3.0, V3.1 and V3.2

Product Status: known_affected, known_not_affected

Remediations

None available
Currently no fix is available

Spectrum Power 4 with HISViews V1.0

Product Status: known_affected, known_not_affected

Remediations

None available
Currently no fix is available

Spectrum Power 7 using IHM (NagiosXI)

Product Status: known_affected, known_not_affected

Remediations

Vendor fix
Red Hat released a PHP security patch for RHEL 8 and 9

Spectrum Power TG which are based on Microsoft Windows using the WebConsole and WebQuery components

Product Status: known_affected, known_not_affected

Remediations

Vendor fix
Upgrade PHP version to V8.5.12

AMIS TS

Product Status: known_affected, known_not_affected

Remediations

None available
Currently no fix is available

blueplanet 360 NX3 M6 WM OD IISX

Product Status: known_affected, known_not_affected

Remediations

None available
Currently no fix is available

Energy Engage V2.0SP9

Product Status: known_affected, known_not_affected

Remediations

No fix planned
Currently no fix is planned

Energy Engage V3.1SP1

Product Status: known_affected, known_not_affected

Remediations

Vendor fix
Upgrade PHP version to V8.1.34 release 6

blueplanet 360 NX3 M6 WM OD IISX - S

Product Status: known_affected, known_not_affected

Remediations

None available
Currently no fix is available

Local Monitoring bt-monitoring-vm < V20261103

Product Status: known_affected, known_not_affected

Remediations

Vendor fix
Update to V20261103 or later version

Spectrum Power 3 using IHM (NagiosXI) running on Red Hat Enterprise Linux version (RHEL) 7

Product Status: known_affected, known_not_affected

Remediations

Vendor fix
Red Hat released a PHP security patch for RHEL 7

Spectrum Power 4 using Nagios or Zabbix

Product Status: known_affected, known_not_affected

Remediations

None available
Currently no fix is available

Spectrum Power 4 with Web Office Portal V3.0, V3.1 and V3.2

Product Status: known_affected, known_not_affected

Remediations

None available
Currently no fix is available

Spectrum Power 4 with HISViews V1.0

Product Status: known_affected, known_not_affected

Remediations

None available
Currently no fix is available

Spectrum Power 7 using IHM (NagiosXI)

Product Status: known_affected, known_not_affected

Remediations

Vendor fix
Red Hat released a PHP security patch for RHEL 8 and 9

Spectrum Power TG which are based on Microsoft Windows using the WebConsole and WebQuery components

Product Status: known_affected, known_not_affected

Remediations

Vendor fix
Upgrade PHP version to V8.5.12

Additional Metrics

Relevant CWE: CWE-416 Use After Free

CVSS Version
Base Score
Base Severity
Vector String

3.1
8.1
HIGH
CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H

View CVE Details

Acknowledgments

Siemens ProductCERT reported these vulnerabilities to CISA.

General Recommendations

Operators of critical power systems (e.g. TSOs or DSOs) worldwide are usually required by regulations to build resilience into the power grids by applying multi-level redundant secondary protection schemes. It is therefore recommended that the operators check whether appropriate resilient protection measures are in place. The risk of cyber incidents impacting the grid's reliability can thus be minimized by virtue of the grid design. Siemens strongly recommends applying the provided security updates using the corresponding tooling and documented procedures made available with the product. If supported by the product, an automated means to apply the security updates across multiple product instances may be used. Siemens strongly recommends prior validation of any security update before being applied, and supervision by trained staff of the update process in the target environment. As a general security measure Siemens strongly recommends protecting network access with appropriate mechanisms (e.g. firewalls, segmentation, VPN). It is advised to configure the environment according to our operational guidelines in order to run the devices in a protected IT environment. Recommended security guidelines can be found at: https://www.siemens.com/gridsecurity

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

This ICSA is a verbatim republication of Siemens ProductCERT SSA-166980 from a direct conversion of the vendor's Common Security Advisory Framework (CSAF) advisory. This is republished to CISA's website as a means of increasing visibility and is provided "as-is" for informational purposes only. CISA is not responsible for the editorial or technical accuracy of republished advisories and provides no warranties of any kind regarding any information contained within this advisory. Further, CISA does not endorse any commercial product or service. Please contact Siemens ProductCERT directly for any questions regarding this advisory.

Revision History

Initial Release Date: 2026-10-26

Date
Revision
Summary

2026-10-26
1
Publication Date

2026-10-27
2
Updated the Known not affected list

2026-10-29
3
Added AMIS TS, Energy Engage V2.0SP9, Energy Engage V3.1SP1, Spectrum Power 3, Spectrum Power 4, Spectrum Power 7 and Spectrum Power TG to Affected Products and updated the list of known not affected

2026-11-05
4
Updated Known Not Affected and Known Affected Products list

2026-11-12
5
Initial CISA Republication of Siemens ProductCERT SSA-166980 advisory

Legal Notice and Terms of Use

This product is provided subject to this Notification and this Privacy & Use policy.

Vendor

Siemens

Tags

Sector :
Energy Sector

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

ICS Advisory | ICSA-26-316-03

Siemens Industrial Edge Management

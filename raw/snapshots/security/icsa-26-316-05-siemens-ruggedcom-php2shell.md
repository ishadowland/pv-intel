<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-316-05 -->
<!-- fetched_at: 2026-11-15 07:11:49 -->
<!-- sha256: b1d8657ce71209ce646eab8c70f98d25cb779e4d1cd276b9456ed92b7980443b -->

Siemens RUGGEDCOM APE1808 | CISA

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

Siemens RUGGEDCOM APE1808

Release Date
November 12, 2026

Alert Code
ICSA-26-316-05

Related topics:

Industrial Control System Vulnerabilities
,
Industrial Control Systems

View CSAF

Summary

Palo Alto Networks has published information on vulnerabilities in PAN-OS related to PHP2Shell vulnerabilities. This advisory lists the related Siemens Industrial products affected by these vulnerabilities. Customers are advised to consult and implement the workarounds provided in Palo Alto Networks' upstream security notifications.

The following versions of Siemens RUGGEDCOM APE1808 are affected:

RUGGEDCOM APE1808 vers:all/* (CVE-2026-109618, CVE-2026-109619)

CVSS
Vendor
Equipment

v3 9.8
Siemens
RUGGEDCOM APE1808

1 Vulnerability

Use After Free

Background

Critical Infrastructure Sectors: Critical Manufacturing

Countries/Areas Deployed: Worldwide

Company Headquarters Location: Germany

Vulnerabilities

Expand All +

CVE-2026-109618

PHP uses longjmp() for out-of-memory (OOM) errors to exit the current context and abort handling of the request. Some contexts may not properly account for this scenario and leave request memory in an uninitialized state before performing an allocation. The subsequent request cleanup procedure may read or branch on this memory. Multiple OOM strategies can consistently trigger this condition and lead to remote code execution (RCE).

Read More

1 Affected Product

RUGGEDCOM APE1808 with Palo Alto Networks PAN-OS (10.2 All, 11.1 All, 11.2 All, 12.1 All, 12.2 All)

Product Status: known_affected

Remediations

Vendor fix
Upgrade to corresponding available PAN-OS version. Contact customer support to receive additional patch and update information.

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

2 Affected Products

RUGGEDCOM APE1808 with Palo Alto Networks PAN-OS (10.2 All, 11.1 All, 11.2 All, 12.1 All, 12.2 All)

Product Status: known_affected

Remediations

Vendor fix
Upgrade to corresponding available PAN-OS version. Contact customer support to receive additional patch and update information.

RUGGEDCOM APE1808 with Palo Alto Networks PAN-OS (10.2 All, 11.1 All, 11.2 All, 12.1 All, 12.2 All)

Product Status: known_affected

Remediations

Vendor fix
Upgrade to corresponding available PAN-OS version. Contact customer support to receive additional patch and update information.

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

As a general security measure, Siemens strongly recommends to protect network access to devices with appropriate mechanisms. In order to operate the devices in a protected IT environment, Siemens recommends to configure the environment according to Siemens' operational guidelines for Industrial Security ( https://www.siemens.com/cert/operational-guidelines-industrial-security ), and to follow the recommendations in the product manuals. Additional information on Industrial Security by Siemens can be found at: https://www.siemens.com/industrialsecurity

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

This ICSA is a verbatim republication of Siemens ProductCERT SSA-566512 from a direct conversion of the vendor's Common Security Advisory Framework (CSAF) advisory. This is republished to CISA's website as a means of increasing visibility and is provided "as-is" for informational purposes only. CISA is not responsible for the editorial or technical accuracy of republished advisories and provides no warranties of any kind regarding any information contained within this advisory. Further, CISA does not endorse any commercial product or service. Please contact Siemens ProductCERT directly for any questions regarding this advisory.

Revision History

Initial Release Date: 2026-10-23

Date
Revision
Summary

2026-10-23
1
Publication Date

2026-10-28
2
Updated Remediation to include PAN-OS

2026-11-04
3
Adjusted history entry of V1.1

2026-11-12
4
Initial CISA Republication of Siemens ProductCERT SSA-566512 advisory

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

ICS Advisory | ICSA-26-316-01

Siemens Building Automation and Energy Products

Nov 12, 2026

ICS Advisory | ICSA-26-316-02

Siemens Desigo, Gridscale

Nov 12, 2026

ICS Advisory | ICSA-26-316-04

Siemens RUGGEDCOM APE1808

Nov 12, 2026

ICS Advisory | ICSA-26-316-03

Siemens Industrial Edge Management

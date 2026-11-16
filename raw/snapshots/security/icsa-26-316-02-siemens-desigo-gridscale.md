<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-316-02 -->
<!-- fetched_at: 2026-11-17 07:11:04 -->
<!-- sha256: 65bfd6156df8a0100307b5cc42557790dcdcbb122254c20570c16abfaee6ba34 -->

Siemens Desigo, Gridscale | CISA

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

Siemens Desigo, Gridscale

Release Date
November 12, 2026

Alert Code
ICSA-26-316-02

Related topics:

Industrial Control System Vulnerabilities
,
Industrial Control Systems

View CSAF

Summary

On October 21, 2026, the Node.js project released security updates addressing a critical vulnerability in the Brotli decoder bundled with Node.js, commonly referred to as "Node2Shell" (tracked as CVE-2026-111497). The vulnerability is an out-of-bounds write that could allow a remote attacker to cause memory corruption and potentially execute arbitrary code. This advisory covers the status of impact of various Siemens software products. Siemens has released new versions for the affected products and recommends to update to the latest versions.

The following versions of Siemens Desigo, Gridscale are affected:

Desigo CC family V8 vers:all/* (CVE-2026-111497)

Desigo CC family V9 vers:all/* (CVE-2026-111497)

Gridscale X DSA vers:intdot/>=5.3|<5.4 (CVE-2026-111497)

Gridscale X PSS®E vers:intdot/<36.8.0 (CVE-2026-111497)

CVSS
Vendor
Equipment

v3 9.8
Siemens
Desigo CC family V8

1 Vulnerability

Out-of-bounds Write

Background

Critical Infrastructure Sectors: Critical Manufacturing, Energy, Information Technology

Countries/Areas Deployed: Worldwide

Company Headquarters Location: Germany

Vulnerabilities

CVE-2026-111497

A buffer overflow vulnerability in the Brotli decoder (c/dec/decode.c) in Google Brotli versions 1.0.3 through 1.2.0 on all platforms allows a remote unauthenticated attacker to corrupt adjacent decoder state memory, disclose sensitive memory contents, cause a denial of service, or potentially execute arbitrary code using a crafted Brotli-compressed stream. Users need to update any Brotli libraries or binaries between 1.0.3 through 1.2.0 to the latest available version: 1.0.10 or 1.1.1 or 1.2.1.

Read More

4 Affected Products

Desigo CC family V8

Product Status: known_affected, known_not_affected

Remediations

Vendor fix
Install the latest .NET security updates via Windows Update.

Desigo CC family V9

Product Status: known_affected, known_not_affected

Remediations

Vendor fix
Install the latest .NET security updates via Windows Update.

Gridscale X DSA >= V5.3 < V5.4

Product Status: known_affected, known_not_affected

Remediations

Vendor fix
Update to V5.4 or later version

Gridscale X PSS®E < V36.8.0

Product Status: known_affected, known_not_affected

Remediations

Vendor fix
Update to V36.8.0 or later version

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

Operators of critical power systems (e.g. TSOs or DSOs) worldwide are usually required by regulations to build resilience into the power grids by applying multi-level redundant secondary protection schemes. It is therefore recommended that the operators check whether appropriate resilient protection measures are in place. The risk of cyber incidents impacting the grid's reliability can thus be minimized by virtue of the grid design. Siemens strongly recommends applying the provided security updates using the corresponding tooling and documented procedures made available with the product. If supported by the product, an automated means to apply the security updates across multiple product instances may be used. Siemens strongly recommends prior validation of any security update before being applied, and supervision by trained staff of the update process in the target environment. As a general security measure Siemens strongly recommends to protect network access with appropriate mechanisms (e.g. firewalls, segmentation, VPN). It is advised to configure the environment according to our operational guidelines in order to run the devices in a protected IT environment. Recommended security guidelines can be found at: https://www.siemens.com/gridsecurity

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

This ICSA is a verbatim republication of Siemens ProductCERT SSA-045512 from a direct conversion of the vendor's Common Security Advisory Framework (CSAF) advisory. This is republished to CISA's website as a means of increasing visibility and is provided "as-is" for informational purposes only. CISA is not responsible for the editorial or technical accuracy of republished advisories and provides no warranties of any kind regarding any information contained within this advisory. Further, CISA does not endorse any commercial product or service. Please contact Siemens ProductCERT directly for any questions regarding this advisory.

Revision History

Initial Release Date: 2026-10-30

Date
Revision
Summary

2026-10-30
1
Publication Date

2026-11-04
2
Added Desigo CC to the affected products list.

2026-11-06
3
Added Gridscale X DSA and PSSE to the list of affected products

2026-11-12
4
Initial CISA Republication of Siemens ProductCERT SSA-045512 advisory

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

Nov 12, 2026

ICS Advisory | ICSA-26-316-01

Siemens Building Automation and Energy Products

Nov 12, 2026

ICS Advisory | ICSA-26-316-04

Siemens RUGGEDCOM APE1808

Nov 12, 2026

ICS Advisory | ICSA-26-316-05

Siemens RUGGEDCOM APE1808

Nov 12, 2026

ICS Advisory | ICSA-26-316-03

Siemens Industrial Edge Management

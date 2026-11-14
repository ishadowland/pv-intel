<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-316-04 -->
<!-- fetched_at: 2026-11-15 07:11:45 -->
<!-- sha256: 4f0c687a2e9c16b3a5579aaccde435240355fe8f0362d0f0993067bcba4e681f -->

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
ICSA-26-316-04

Related topics:

Industrial Control System Vulnerabilities
,
Industrial Control Systems

View CSAF

Summary

Palo Alto Networks has published information on a vulnerability in PAN-OS related to the Node2Shell vulnerability. This advisory lists the related Siemens Industrial products affected by this vulnerability. Customers are advised to consult and implement the workarounds provided in Palo Alto Networks' upstream security notifications.

The following versions of Siemens RUGGEDCOM APE1808 are affected:

RUGGEDCOM APE1808 vers:all/* (CVE-2026-111497)

CVSS
Vendor
Equipment

v3 9.8
Siemens
RUGGEDCOM APE1808

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

1 Affected Product

RUGGEDCOM APE1808 with Palo Alto Networks PAN-OS

Product Status: known_affected

Remediations

Vendor fix
Upgrade to corresponding available PAN-OS version. Contact customer support to receive additional patch and update information.

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

This ICSA is a verbatim republication of Siemens ProductCERT SSA-898633 from a direct conversion of the vendor's Common Security Advisory Framework (CSAF) advisory. This is republished to CISA's website as a means of increasing visibility and is provided "as-is" for informational purposes only. CISA is not responsible for the editorial or technical accuracy of republished advisories and provides no warranties of any kind regarding any information contained within this advisory. Further, CISA does not endorse any commercial product or service. Please contact Siemens ProductCERT directly for any questions regarding this advisory.

Revision History

Initial Release Date: 2026-10-30

Date
Revision
Summary

2026-10-30
1
Publication Date

2026-11-12
2
Initial CISA Republication of Siemens ProductCERT SSA-898633 advisory

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

ICS Advisory | ICSA-26-316-05

Siemens RUGGEDCOM APE1808

Nov 12, 2026

ICS Advisory | ICSA-26-316-03

Siemens Industrial Edge Management

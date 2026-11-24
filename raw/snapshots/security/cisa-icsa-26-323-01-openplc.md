<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-323-01 -->
<!-- fetched_at: 2026-11-24 07:24:32 -->
<!-- sha256: 5a4036126da460852cd94938a86db70b58e6407eaf9daacbe4b6e98cd66cd24c -->

Autonomy Logic OpenPLC Runtime | CISA

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

Autonomy Logic OpenPLC Runtime

Release Date
November 19, 2026

Alert Code
ICSA-26-323-01

Related topics:

Industrial Control System Vulnerabilities
,
Industrial Control Systems

View CSAF

Summary

Successful exploitation of this vulnerability could allow several unauthenticated admin accounts to be created.

The following versions of Autonomy Logic OpenPLC Runtime are affected:

OpenPLC Runtime <=4.2.4 (CVE-2026-126088)

CVSS
Vendor
Equipment

v3 8.1
Autonomy Logic
OpenPLC Runtime

1 Vulnerability

Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')

Background

Critical Infrastructure Sectors: Critical Manufacturing, Energy, Transportation Systems, Water and Wastewater Systems

Countries/Areas Deployed: Worldwide

Company Headquarters Location: United States

Vulnerabilities

CVE-2026-126088

In Autonomy Logic OpenPLC Runtime versions 4.2.4 and prior, a race condition allows multiple concurrent requests to pass the existence check before any user is committed, resulting in several unauthenticated admin accounts being created.

Read More

1 Affected Product

Autonomy Logic OpenPLC Runtime <=4.2.4

Product Status: known_affected

Remediations

Vendor fix
Update to OpenPLC Runtime version 4.3.0 or later.

Additional Metrics

Relevant CWE: CWE-362 Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')

CVSS Version
Base Score
Base Severity
Vector String

3.1
8.1
HIGH
CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H

4.0
9.2
CRITICAL
CVSS:4.0/AV:N/AC:H/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N

View CVE Details

Acknowledgments

Noureddin Lutfi reported this vulnerability to CISA.

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

CISA also recommends users take the following measures to protect themselves from social engineering attacks:

Do not click web links or open attachments in unsolicited email messages.

Refer to Recognizing and Avoiding Email Scams for more information on avoiding email scams.

Refer to Avoiding Social Engineering and Phishing Attacks for more information on social engineering attacks.

No known public exploitation specifically targeting these vulnerabilities has been reported to CISA at this time.

Revision History

Initial Release Date: 2026-11-19

Date
Revision
Summary

2026-11-19
1
Initial Publication

Legal Notice and Terms of Use

This product is provided subject to this Notification and this Privacy & Use policy.

Tags

Sector :
Critical Manufacturing Sector ,
Energy Sector ,
Transportation Systems Sector ,
Water and Wastewater Systems

Topics :
Industrial Control System Vulnerabilities ,
Industrial Control Systems

Please share your thoughts

We recently updated our anonymous product survey ; we welcome your feedback.

Related Advisories

Nov 19, 2026

ICS Advisory | ICSA-26-323-03

libumqtt

Nov 19, 2026

ICS Advisory | ICSA-26-323-02

Elecbrakes EB2, VM1, ELBC2000

Nov 17, 2026

ICS Advisory | ICSA-26-321-01

Dorsett Controls InfoScan

Nov 17, 2026

ICS Advisory | ICSA-26-321-02

Siemens .NET Client Library for SIMATIC S7 Webserver API

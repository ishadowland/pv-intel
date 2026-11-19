<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-323-03 -->
<!-- fetched_at: 2026-11-20 07:11:56 -->
<!-- sha256: e02dad2240d67144d41d46a18e943508ecca76cf2e8e21bb8cad9f9716aba061 -->

libumqtt | CISA

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

libumqtt

Release Date
November 19, 2026

Alert Code
ICSA-26-323-03

Related topics:

Industrial Control System Vulnerabilities
,
Industrial Control Systems

View CSAF

Summary

Successful exploitation of this vulnerability could allow a remote attacker to cause a denial of service, memory corruption, or information disclosure.

The following versions of libumqtt are affected:

libumqtt <=1.1.1 (CVE-2026-125132)

CVSS
Vendor
Equipment

v3 8.6
libumqtt
libumqtt

1 Vulnerability

Integer Underflow (Wrap or Wraparound)

Background

Critical Infrastructure Sectors: Critical Manufacturing, Energy, Information Technology, Transportation Systems, Water and Wastewater

Countries/Areas Deployed: Worldwide

Company Headquarters Location: China

Vulnerabilities

CVE-2026-125132

The affected product is vulnerable to an integer underflow which may allow a remote attacker to cause a denial of service, memory corruption, or information disclosure.

Read More

1 Affected Product

libumqtt libumqtt <=1.1.1

Product Status: known_affected

Remediations

None available
The repository owners of libumqtt did not respond to CISA's request for coordination. Users are encouraged to reach out to libumqtt for support. Their GitHub page is located at https://github.com/zhaojh329/libumqtt.

Additional Metrics

Relevant CWE: CWE-191 Integer Underflow (Wrap or Wraparound)

CVSS Version
Base Score
Base Severity
Vector String

3.1
8.6
HIGH
CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:H

4.0
8.8
HIGH
CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:L/VI:L/VA:H/SC:N/SI:N/SA:N

View CVE Details

Acknowledgments

Joseph Devasia reported this vulnerability to CISA

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

No known public exploitation specifically targeting this vulnerability has been reported to CISA at this time.

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
Information Technology Sector ,
Transportation Systems Sector ,
Water and Wastewater Systems

Topics :
Industrial Control System Vulnerabilities ,
Industrial Control Systems

Please share your thoughts

We recently updated our anonymous product survey ; we welcome your feedback.

Related Advisories

Nov 19, 2026

ICS Advisory | ICSA-26-323-02

Elecbrakes EB2, VM1, ELBC2000

Nov 19, 2026

ICS Advisory | ICSA-26-323-01

Autonomy Logic OpenPLC Runtime

Nov 17, 2026

ICS Advisory | ICSA-26-321-01

Dorsett Controls InfoScan

Nov 17, 2026

ICS Advisory | ICSA-26-321-02

Siemens .NET Client Library for SIMATIC S7 Webserver API

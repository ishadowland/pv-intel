<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-03 -->
<!-- fetched_at: 2026-11-25 07:33:53 -->
<!-- sha256: b80eed8f0568c5284467546d2ff4a4ea7392b26d418abf972abf7c89720f95e7 -->

Danfoss AK-SM 8xxA Series | CISA

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

Danfoss AK-SM 8xxA Series

Release Date
November 24, 2026

Alert Code
ICSA-26-328-03

Related topics:

Industrial Control System Vulnerabilities
,
Industrial Control Systems

View CSAF

Summary

Successful exploitation of this vulnerability could allow an attacker to execute arbitrary code with webserver privileges.

The following versions of Danfoss AK-SM 8xxA Series are affected:

AK-SM8xxA <=5.4.0 (CVE-2026-129713)

CVSS
Vendor
Equipment

v3 9.8
Danfoss
AK-SM8xxA

1 Vulnerability

Stack-based Buffer Overflow

Background

Critical Infrastructure Sectors: Commercial Facilities

Countries/Areas Deployed: Worldwide

Company Headquarters Location: Denmark

Vulnerabilities

CVE-2026-129713

A stack-based buffer overflow in an unauthenticated CGI handler of the Danfoss AK-SM 8xxA Series controller allows remote attackers to send specially crafted HTTP/S POST requests, leading to memory corruption, webserver restart and hypothetically potential arbitrary code execution with webserver privileges. Authentication is not required to exploit this vulnerability.

Read More

1 Affected Product

Danfoss AK-SM8xxA <=5.4.0

Product Status: known_affected

Remediations

Mitigation
This vulnerability will be addressed in an upcoming Danfoss AK-SM 800A Series software release (version 5.5.x). In addition, Danfoss will remove the ability for users to disable Strict Mode in future software releases.

Mitigation
Until a software update is available, Danfoss recommends the following mitigations: * Follow the guidance provided in the product documentation and do not expose devices directly to the Internet or assign them public IP addresses. * Restrict remote access to affected devices by using a secure VPN or other protected network architecture. * Configure all affected devices to operate in Strict Mode, which provides enhanced security protections. * Use strong, unique passwords for all user accounts and administrative access. * For additional security recommendations and best practices see the Danfoss AK-SM 800 security guidance page: https://www.danfoss.com/en/service-and-support/downloads/dcs/adap-kool-software/ak-sm-800a/#tab-overview

Additional Metrics

Relevant CWE: CWE-121 Stack-based Buffer Overflow

CVSS Version
Base Score
Base Severity
Vector String

3.1
9.8
CRITICAL
CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H

4.0
9.3
CRITICAL
CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N

View CVE Details

Acknowledgments

Carlo Meijer of Midnight Blue reported CVE-2026-129713 to CISA.

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

Initial Release Date: 2026-11-24

Date
Revision
Summary

2026-11-24
1
Initial Publication

Legal Notice and Terms of Use

This product is provided subject to this Notification and this Privacy & Use policy.

Tags

Sector :
Commercial Facilities Sector

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

ICS Advisory | ICSA-26-328-02

Schneider Electric EcoStruxure Power Build Rapsody software

Nov 19, 2026

ICS Advisory | ICSA-26-323-03

libumqtt

Nov 19, 2026

ICS Advisory | ICSA-26-323-02

Elecbrakes EB2, VM1, ELBC2000

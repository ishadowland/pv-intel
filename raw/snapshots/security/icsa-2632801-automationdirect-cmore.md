<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-01 -->
<!-- fetched_at: 2026-11-26 07:10:56 -->
<!-- sha256: a3ebb08bba3feb4f110e8bc295bffb6f81d2690571b9f3d5cc44286539861857 -->

AutomationDirect C-More EA9 Programming Software | CISA

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

AutomationDirect C-More EA9 Programming Software

Release Date
November 24, 2026

Alert Code
ICSA-26-328-01

Related topics:

Industrial Control System Vulnerabilities
,
Industrial Control Systems

View CSAF

Summary

Successful exploitation of this vulnerability could allow attackers to corrupt application memory and cause instability or a crash, potentially leading to arbitrary code execution, if a user is convinced to open a malicious file.

The following versions of AutomationDirect C-More EA9 Programming Software are affected:

C-More EA9 Programming Software <=V6.80 (CVE-2026-127280)

CVSS
Vendor
Equipment

v3 7.8
AutomationDirect
C-More EA9 Programming Software

1 Vulnerability

Heap-based Buffer Overflow

Background

Critical Infrastructure Sectors: Critical Manufacturing, Energy, Water and Wastewater Systems

Countries/Areas Deployed: Worldwide

Company Headquarters Location: United States

Vulnerabilities

CVE-2026-127280

C-More EA9 Programming Software V6.80 does not adequately validate data read from a project file before using it in heap memory operations. A crafted file causes a heap buffer overrun during file open, resulting in heap corruption and instability within the application. An attacker can exploit this vulnerability by convincing a user to open a malicious project file delivered through common distribution channels such as email, file sharing, or removable media.

Read More

1 Affected Product

AutomationDirect C-More EA9 Programming Software <=V6.80

Product Status: known_affected

Remediations

Vendor fix
Update C-More EA9 Programming Software to V6.81: https://www.automationdirect.com/support/software-downloads

Mitigation
If you cannot update to the latest software or firmware version right away, apply the following compensating controls to reduce risk until the update can be performed. These measures are temporary and do not replace the update, which remains the primary and recommended remediation. Apply these controls as appropriate based on the vulnerability, assessed risk, operational requirements, and characteristics of your environment. Implement changes under your established management-of-change process. Before implementing isolation, access-control, or network-configuration changes, evaluate potential impacts to safety, availability, and essential operational functions. • Isolate affected engineering workstations and OT systems from external and nonessential networks, including the internet and corporate IT networks, where operationally feasible. • Disable or tightly restrict vendor, contractor, and other remote access to the affected OT environment until the vulnerability can be remediated. Where remote access is operationally required, use a hardened jump host, enforce multi-factor authentication, apply least-privilege access, and limit access to authorized, time-bound sessions. • Use trusted, dedicated OT networks for device communication. Where practicable and appropriate to the assessed risk, use dedicated or physically separated infrastructure for higher-criticality systems. Where logical segmentation is used, ensure segmentation controls are appropriately configured, secured, and monitored. • Restrict both physical and logical access to affected systems to authorized personnel only. Apply least-privilege principles to administrative, engineering, maintenance, and service access. • Configure application allowlisting, where supported, so that only trusted and pre-approved applications are permitted to execute. Block unauthorized software. • Use appropriate antivirus or endpoint detection and response (EDR) tools where supported and compatible with the affected system. Configure host-based and network firewalls to permit only required communications. • Disable unnecessary services, ports, protocols, and communication pathways associated with the affected systems. Where a service or protocol cannot be disabled for operational reasons, restrict access to trusted systems and authorized users wherever possible. • Enable and regularly review available system, security, and network logs to identify suspicious or unauthorized activity. Where appropriate, monitor communications to and from affected systems for unexpected connections or changes in network behavior. • Maintain secure, tested, and preferably offline backups of PLC programs, device configurations, engineering workstation configurations, and other information necessary to restore operations. Periodically verify that backups can be successfully restored. • Verify that critical OT functions can continue operating without unnecessary dependencies on external networks, cloud services, remote-access services, corporate IT services, or other nonessential systems. • If removable media is required to transfer files into an isolated or restricted environment, use controlled and trusted media and scan it for malicious content before use. • Continuously evaluate the risks associated with operating vulnerable or outdated firmware or software. Adjust compensating controls as the threat environment, operational requirements, or available vulnerability information changes. These compensating controls are intended to reduce exposure while remediation is pending. Organizations should prioritize applying the vendor-provided update as soon as it can be safely tested and deployed within the operational environment.

Additional Metrics

Relevant CWE: CWE-122 Heap-based Buffer Overflow

CVSS Version
Base Score
Base Severity
Vector String

3.1
7.8
HIGH
CVSS:3.1/AV:L/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H

4.0
8.4
HIGH
CVSS:4.0/AV:L/AC:L/AT:N/PR:N/UI:A/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N

View CVE Details

Acknowledgments

rgod of TrendAI Zero Day Initiative reported this vulnerability to CISA.

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

Vendor

AutomationDirect

Tags

Sector :
Critical Manufacturing Sector ,
Energy Sector ,
Water and Wastewater Systems

Topics :
Industrial Control System Vulnerabilities ,
Industrial Control Systems

Please share your thoughts

We recently updated our anonymous product survey ; we welcome your feedback.

Related Advisories

Nov 24, 2026

ICS Advisory | ICSA-26-328-02

Schneider Electric EcoStruxure Power Build Rapsody software

Nov 24, 2026

ICS Advisory | ICSA-26-328-03

Danfoss AK-SM 8xxA Series

Nov 19, 2026

ICS Advisory | ICSA-26-323-03

libumqtt

Nov 19, 2026

ICS Advisory | ICSA-26-323-02

Elecbrakes EB2, VM1, ELBC2000

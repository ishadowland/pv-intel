<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-08 -->
<!-- fetched_at: 2026-11-25 07:12:19 -->
<!-- sha256: 336c15533ae1c87ef87c7799a5bed5de0f2ac033f1f55edfed28c1bb51e0bc69 -->

Siemens SIMATIC | CISA

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

Siemens SIMATIC

Release Date
November 17, 2026

Alert Code
ICSA-26-321-08

Related topics:

Industrial Control System Vulnerabilities
,
Industrial Control Systems

View CSAF

Summary

The products listed below contain an authentication bypass vulnerability that could allow an on-path attacker to take over the session of a legitimate user and execute arbitrary code with the privileges of the victim user. Siemens is preparing fixes and recommends specific mitigations for products where fixes are not or not yet available.

The following versions of Siemens SIMATIC are affected:

SIMATIC BATCH V9.1 vers:all/* (CVE-2026-58114)

SIMATIC Information Server 2020 vers:all/* (CVE-2026-58114)

SIMATIC Information Server 2022 vers:all/* (CVE-2026-58114)

SIMATIC PCS 7 V9.1 vers:all/* (CVE-2026-58114)

SIMATIC Process Historian 2020 vers:all/* (CVE-2026-58114)

SIMATIC Process Historian 2022 vers:all/* (CVE-2026-58114)

SIMATIC WinCC Runtime Professional V17 vers:all/* (CVE-2026-58114)

SIMATIC WinCC Runtime Professional V18 vers:all/* (CVE-2026-58114)

SIMATIC WinCC Runtime Professional V19 vers:all/* (CVE-2026-58114)

SIMATIC WinCC Runtime Professional V20 vers:all/* (CVE-2026-58114)

SIMATIC WinCC Runtime Professional V21 vers:all/* (CVE-2026-58114)

SIMATIC WinCC V7.5 vers:all/* (CVE-2026-58114)

SIMATIC WinCC V8.0 vers:all/* (CVE-2026-58114)

SIMATIC WinCC V8.1 vers:all/* (CVE-2026-58114)

CVSS
Vendor
Equipment

v3 7.5
Siemens
SIMATIC BATCH V9.1

1 Vulnerability

Weak Authentication

Background

Critical Infrastructure Sectors: Critical Manufacturing

Countries/Areas Deployed: Worldwide

Company Headquarters Location: Germany

Vulnerabilities

CVE-2026-58114

Affected systems do not properly secure their remote user authentication with the deprecated NTLM protocol. This could allow unauthenticated remote attackers, who have achieved a machine in the middle position, to relay NTLM authentication and impersonate a legitimate user. The potential impact depends on the services that are accessible, e.g. a SQL server used by WinCC.

Read More

14 Affected Products

SIMATIC BATCH V9.1

Product Status: known_affected

Remediations

Mitigation
Customers can manually configure the SQL Server Database for encrypting communication as described in https://support.industry.siemens.com/cs/mdm/109818202?c=145291786635&lc=en-ID

No fix planned
Currently no fix is planned

SIMATIC WinCC Runtime Professional V20

Product Status: known_affected

Remediations

Mitigation
Customers can manually configure the SQL Server Database for encrypting communication as described in https://support.industry.siemens.com/cs/mdm/109818202?c=145291786635&lc=en-ID

None available
Currently no fix is available

SIMATIC WinCC Runtime Professional V21

Product Status: known_affected

Remediations

Mitigation
Customers can manually configure the SQL Server Database for encrypting communication as described in https://support.industry.siemens.com/cs/mdm/109818202?c=145291786635&lc=en-ID

None available
Currently no fix is available

SIMATIC WinCC V7.5

Product Status: known_affected

Remediations

Mitigation
Customers can manually configure the SQL Server Database for encrypting communication as described in https://support.industry.siemens.com/cs/mdm/109818202?c=145291786635&lc=en-ID

None available
Currently no fix is available

SIMATIC WinCC V8.0

Product Status: known_affected

Remediations

Mitigation
Customers can manually configure the SQL Server Database for encrypting communication as described in https://support.industry.siemens.com/cs/mdm/109818202?c=145291786635&lc=en-ID

None available
Currently no fix is available

SIMATIC WinCC V8.1

Product Status: known_affected

Remediations

Mitigation
Customers can manually configure the SQL Server Database for encrypting communication as described in https://support.industry.siemens.com/cs/mdm/109818202?c=145291786635&lc=en-ID

None available
Currently no fix is available

SIMATIC Information Server 2020

Product Status: known_affected

Remediations

Mitigation
Customers can manually configure the SQL Server Database for encrypting communication as described in https://support.industry.siemens.com/cs/mdm/109818202?c=145291786635&lc=en-ID

No fix planned
Currently no fix is planned

SIMATIC Information Server 2022

Product Status: known_affected

Remediations

Mitigation
Customers can manually configure the SQL Server Database for encrypting communication as described in https://support.industry.siemens.com/cs/mdm/109818202?c=145291786635&lc=en-ID

No fix planned
Currently no fix is planned

SIMATIC PCS 7 V9.1

Product Status: known_affected

Remediations

Mitigation
Customers can manually configure the SQL Server Database for encrypting communication as described in https://support.industry.siemens.com/cs/mdm/109818202?c=145291786635&lc=en-ID

No fix planned
Currently no fix is planned

SIMATIC Process Historian 2020

Product Status: known_affected

Remediations

Mitigation
Customers can manually configure the SQL Server Database for encrypting communication as described in https://support.industry.siemens.com/cs/mdm/109818202?c=145291786635&lc=en-ID

No fix planned
Currently no fix is planned

SIMATIC Process Historian 2022

Product Status: known_affected

Remediations

Mitigation
Customers can manually configure the SQL Server Database for encrypting communication as described in https://support.industry.siemens.com/cs/mdm/109818202?c=145291786635&lc=en-ID

No fix planned
Currently no fix is planned

SIMATIC WinCC Runtime Professional V17

Product Status: known_affected

Remediations

Mitigation
Customers can manually configure the SQL Server Database for encrypting communication as described in https://support.industry.siemens.com/cs/mdm/109818202?c=145291786635&lc=en-ID

None available
Currently no fix is available

SIMATIC WinCC Runtime Professional V18

Product Status: known_affected

Remediations

Mitigation
Customers can manually configure the SQL Server Database for encrypting communication as described in https://support.industry.siemens.com/cs/mdm/109818202?c=145291786635&lc=en-ID

None available
Currently no fix is available

SIMATIC WinCC Runtime Professional V19

Product Status: known_affected

Remediations

Mitigation
Customers can manually configure the SQL Server Database for encrypting communication as described in https://support.industry.siemens.com/cs/mdm/109818202?c=145291786635&lc=en-ID

None available
Currently no fix is available

Additional Metrics

Relevant CWE: CWE-1390 Weak Authentication

CVSS Version
Base Score
Base Severity
Vector String

3.1
7.5
HIGH
CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H

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

This ICSA is a verbatim republication of Siemens ProductCERT SSA-970803 from a direct conversion of the vendor's Common Security Advisory Framework (CSAF) advisory. This is republished to CISA's website as a means of increasing visibility and is provided "as-is" for informational purposes only. CISA is not responsible for the editorial or technical accuracy of republished advisories and provides no warranties of any kind regarding any information contained within this advisory. Further, CISA does not endorse any commercial product or service. Please contact Siemens ProductCERT directly for any questions regarding this advisory.

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
Initial CISA Republication of Siemens ProductCERT SSA-970803 advisory

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

Nov 24, 2026

ICS Advisory | ICSA-26-328-03

Danfoss AK-SM 8xxA Series

Nov 24, 2026

ICS Advisory | ICSA-26-328-01

AutomationDirect C-More EA9 Programming Software

Nov 24, 2026

ICS Advisory | ICSA-26-328-02

Schneider Electric EcoStruxure Power Build Rapsody software

Nov 19, 2026

ICS Advisory | ICSA-26-323-02

Elecbrakes EB2, VM1, ELBC2000

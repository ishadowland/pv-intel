<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-300-02 -->
<!-- fetched_at: 2026-11-13 07:11:23 -->
<!-- sha256: 9dd979ab7f96101f9d25243b3684e66690e64f5c238661ba5b3ed8baf3430249 -->

Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions GENESIS, GENESIS64, ICONICS Suite, Hyper Historian, AnalytiX, MobileHMI, IoTWorX, MC Works64, GENESIS32 and BizViz | CISA

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

Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions GENESIS, GENESIS64, ICONICS Suite, Hyper Historian, AnalytiX, MobileHMI, IoTWorX, MC Works64, GENESIS32 and BizViz

Last Revised
October 29, 2026

Alert Code
ICSA-26-300-02

Related topics:

Industrial Control System Vulnerabilities
,
Industrial Control Systems

View CSAF

Summary

Successful exploitation of these vulnerabilities could allow an attacker to execute arbitrary code (CVE-2023-4863), bypass authentication (CVE-2026-16436 and CVE-2026-16437), or perform arbitrary operations (CVE-2026-16438), resulting in information disclosure, tampering with, destruction, or deletion of information, and a denial-of-service (DoS) condition of the system.

The following versions of Mitsubishi Electric GENESIS, GENESIS64, ICONICS Suite, HyperHistorian, AnalytiX, MobileHMI, IoTWorX, MC Works64, GENESIS32, BizViz, Mitsubishi Electric Iconics Digital Solutions GENESIS, GENESIS64, ICONICS Suite, HyperHistorian, AnalytiX, MobileHMI, IoTWorX, GENESIS32 and BizViz are affected:

Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions GENESIS64 >=10.97|<=10.97.2 (CVE-2023-4863)

Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions ICONICS Suite >=10.97|<=10.97.2 (CVE-2023-4863)

Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions GENESIS <=11.03 (CVE-2026-16436, CVE-2026-16437)

Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions GENESIS64 <=10.97.3 (CVE-2026-16436, CVE-2026-16437, CVE-2026-16438)

Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions ICONICS Suite <=10.97.3 (CVE-2026-16436, CVE-2026-16437, CVE-2026-16438)

Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions Hyper Historian <=10.97.3 (CVE-2026-16436, CVE-2026-16437, CVE-2026-16438)

Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions AnalytiX <=10.97.3 (CVE-2026-16436, CVE-2026-16437, CVE-2026-16438)

Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions MobileHMI <=10.97.3 (CVE-2026-16436, CVE-2026-16437, CVE-2026-16438)

Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions IoTWorX <=10.97.3 (CVE-2026-16436, CVE-2026-16437)

Mitsubishi Electric MC Works64 vers:all/* (CVE-2026-16436, CVE-2026-16437, CVE-2026-16438)

Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions GENESIS32 vers:all/* (CVE-2026-16436, CVE-2026-16437)

Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions BizViz vers:all/* (CVE-2026-16436, CVE-2026-16437)

CVSS
Vendor
Equipment

v3 9.1
Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions
Mitsubishi Electric GENESIS, GENESIS64, ICONICS Suite, HyperHistorian, AnalytiX, MobileHMI, IoTWorX, MC Works64, GENESIS32, BizViz, Mitsubishi Electric Iconics Digital Solutions GENESIS, GENESIS64, ICONICS Suite, HyperHistorian, AnalytiX, MobileHMI, IoTWorX, GENESIS32 and BizViz

3 Vulnerabilities

Out-of-bounds Write, Weak Password Recovery Mechanism for Forgotten Password, Incorrect Privilege Assignment

Background

Critical Infrastructure Sectors: Critical Manufacturing

Countries/Areas Deployed: Worldwide

Company Headquarters Location: Japan, United States

Vulnerabilities

Expand All +

CVE-2023-4863

Out-of-bounds Write (CWE-787) vulnerability caused by libwebp, an internal component in GENESIS64 and ICONICS Suite could allow an authenticated local attacker to cause a heap-based buffer overflow and execute arbitrary code by importing a crafted file as an administrator for the affected product. As a result, the attacker may disclose internal information, tamper with, destroy, or delete internal information, or cause the affected system to enter a denial-of-service (DoS) condition.

Read More

4 Affected Products

Mitsubishi Electric GENESIS64: >=10.97|<=10.97.2

Product Status: known_affected

Remediations

Vendor fix
Mitsubishi Electric is releasing fixed version 10.97.3 or later for GENESIS64 and ICONICS Suite. Please download the fixed version from the link below and install it: "https://iconicsinc.my.site.com/community/s/resource-center/product-downloads". (Note: GENESIS64 is included in the ICONICS Suite installation.) For more information on the fixed version, please refer to the Mitsubishi Electric security advisory at "https://www.mitsubishielectric.com/psirt/vulnerability/pdf/2026-006_en.pdf".

Mitigation
For customers using the affected product who cannot immediately update it, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend configuring the PCs with the affected product installed so that only an administrator can log in, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers using the affected product who cannot immediately update it, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend using the PCs with the affected product installed in the LAN and blocking remote login from untrusted networks and hosts, and from non-administrator users, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers using the affected product who cannot immediately update it, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend blocking unauthorized access by using a firewall, virtual private network (VPN), etc. and allowing remote login only to administrator when internet access is required, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers using the affected product who cannot immediately update it, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend restricting physical access to the PC with the affected product installed and the network to which the PC is connected, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers using the affected product who cannot immediately update it, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend preventing the user from clicking on web links in emails from untrusted sources, or from opening attachments in untrusted emails, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers using the affected product who cannot immediately update it, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend installing anti-virus software on the PC with the affected product installed, to minimize the risk of exploitation of this vulnerability.

Mitsubishi Electric ICONICS Suite: >=10.97|<=10.97.2

Product Status: known_affected

Remediations

Vendor fix
Mitsubishi Electric is releasing fixed version 10.97.3 or later for GENESIS64 and ICONICS Suite. Please download the fixed version from the link below and install it: "https://iconicsinc.my.site.com/community/s/resource-center/product-downloads". (Note: GENESIS64 is included in the ICONICS Suite installation.) For more information on the fixed version, please refer to the Mitsubishi Electric security advisory at "https://www.mitsubishielectric.com/psirt/vulnerability/pdf/2026-006_en.pdf".

Mitigation
For customers using the affected product who cannot immediately update it, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend configuring the PCs with the affected product installed so that only an administrator can log in, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers using the affected product who cannot immediately update it, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend using the PCs with the affected product installed in the LAN and blocking remote login from untrusted networks and hosts, and from non-administrator users, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers using the affected product who cannot immediately update it, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend blocking unauthorized access by using a firewall, virtual private network (VPN), etc. and allowing remote login only to administrator when internet access is required, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers using the affected product who cannot immediately update it, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend restricting physical access to the PC with the affected product installed and the network to which the PC is connected, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers using the affected product who cannot immediately update it, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend preventing the user from clicking on web links in emails from untrusted sources, or from opening attachments in untrusted emails, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers using the affected product who cannot immediately update it, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend installing anti-virus software on the PC with the affected product installed, to minimize the risk of exploitation of this vulnerability.

Mitsubishi Electric Iconics Digital Solutions GENESIS64: >=10.97|<=10.97.2

Product Status: known_affected

Remediations

Vendor fix
Mitsubishi Electric Iconics Digital Solutions is releasing fixed version 10.97.3 or later for GENESIS64 and ICONICS Suite. Please download the fixed version from the link below and install it: "https://iconicsinc.my.site.com/community/s/resource-center/product-downloads". Note: GENESIS64 is included in the ICONICS Suite installation. For more information on the fixed version, please refer to the Mitsubishi Electric Iconics Digital Solutions whitepaper on security vulnerabilities, which can be found at "https://iconics.com/about/security/cert".

Mitigation
For customers using the affected product who cannot immediately update it, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend configuring the PCs with the affected product installed so that only an administrator can log in, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers using the affected product who cannot immediately update it, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend using the PCs with the affected product installed in the LAN and blocking remote login from untrusted networks and hosts, and from non-administrator users, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers using the affected product who cannot immediately update it, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend blocking unauthorized access by using a firewall, virtual private network (VPN), etc. and allowing remote login only to administrator when internet access is required, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers using the affected product who cannot immediately update it, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend restricting physical access to the PC with the affected product installed and the network to which the PC is connected, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers using the affected product who cannot immediately update it, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend preventing the user from clicking on web links in emails from untrusted sources, or from opening attachments in untrusted emails, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers using the affected product who cannot immediately update it, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend installing anti-virus software on the PC with the affected product installed, to minimize the risk of exploitation of this vulnerability.

Mitsubishi Electric Iconics Digital Solutions ICONICS Suite: >=10.97|<=10.97.2

Product Status: known_affected

Remediations

Vendor fix
Mitsubishi Electric Iconics Digital Solutions is releasing fixed version 10.97.3 or later for GENESIS64 and ICONICS Suite. Please download the fixed version from the link below and install it: "https://iconicsinc.my.site.com/community/s/resource-center/product-downloads". Note: GENESIS64 is included in the ICONICS Suite installation. For more information on the fixed version, please refer to the Mitsubishi Electric Iconics Digital Solutions whitepaper on security vulnerabilities, which can be found at "https://iconics.com/about/security/cert".

Mitigation
For customers using the affected product who cannot immediately update it, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend configuring the PCs with the affected product installed so that only an administrator can log in, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers using the affected product who cannot immediately update it, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend using the PCs with the affected product installed in the LAN and blocking remote login from untrusted networks and hosts, and from non-administrator users, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers using the affected product who cannot immediately update it, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend blocking unauthorized access by using a firewall, virtual private network (VPN), etc. and allowing remote login only to administrator when internet access is required, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers using the affected product who cannot immediately update it, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend restricting physical access to the PC with the affected product installed and the network to which the PC is connected, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers using the affected product who cannot immediately update it, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend preventing the user from clicking on web links in emails from untrusted sources, or from opening attachments in untrusted emails, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers using the affected product who cannot immediately update it, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend installing anti-virus software on the PC with the affected product installed, to minimize the risk of exploitation of this vulnerability.

Additional Metrics

Relevant CWE: CWE-787 Out-of-bounds Write

CVSS Version
Base Score
Base Severity
Vector String

3.1
8.2
HIGH
CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H

4.0
9.3
CRITICAL
CVSS:4.0/AV:L/AC:L/AT:N/PR:H/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H

View CVE Details

CVE-2026-16436

Weak Password Recovery Mechanism for Forgotten Password (CWE-640) vulnerability in GENESIS, GENESIS64, ICONICS Suite, Hyper Historian, AnalytiX, MobileHMI, IoTWorX, MC Works64, GENESIS32, and BizViz could allow a remote attacker to unlock the system by obtaining the challenge response by some means. The challenge response used to unlock the system is common to all users and fixed. As a result, the attacker may disclose, tamper with, destroy, or delete internal information, or cause the affected system to enter a denial-of-service (DoS) condition.

Read More

23 Affected Products

Mitsubishi Electric GENESIS64: >=10.97|<=10.97.2

Product Status: known_affected

Remediations

Mitsubishi Electric ICONICS Suite: >=10.97|<=10.97.2

Product Status: known_affected

Remediations

Mitsubishi Electric Iconics Digital Solutions GENESIS64: >=10.97|<=10.97.2

Product Status: known_affected

Remediations

Mitsubishi Electric Iconics Digital Solutions ICONICS Suite: >=10.97|<=10.97.2

Product Status: known_affected

Remediations

Mitsubishi Electric GENESIS: <=11.03

Product Status: known_affected

Remediations

Vendor fix
Mitsubishi Electric is releasing fixed version 11.04 or later for GENESIS. Please download the fixed version from the link below and install it: "https://iconicsinc.my.site.com/community/s/resource-center/product-downloads". For more information on the fixed version, please refer to the Mitsubishi Electric security advisory at "https://www.mitsubishielectric.com/psirt/vulnerability/pdf/2026-006_en.pdf".

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend configuring the PCs with the affected product installed so that only an administrator can log in, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend using the PCs with the affected product installed in the LAN and blocking remote login from untrusted networks and hosts, and from non-administrator users, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend blocking unauthorized access by using a firewall, virtual private network (VPN), etc. and allowing remote login only to administrator when internet access is required, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend restricting physical access to the PC with the affected product installed and the network to which the PC is connected, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend preventing the user from clicking on web links in emails from untrusted sources, or from opening attachments in untrusted emails, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend installing anti-virus software on the PC with the affected product installed, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend performing the following steps for GENESIS, GENESIS64, ICONICS Suite, Hyper Historian, AnalytiX, MobileHMI and MC Works64, to minimize the risk of exploitation of this vulnerability. (1) Delete the .dat file at the location specified below. This file name and location is different depending on the product version. (Version 10: C:\Program Files\ICONICS\GENESIS64\Components\ClientChallengeTable.dat; Version 11: C:\ProgramData\ICONICS\11\SecurityChallenges.dat) (2) Create a blank file with the same name and location. (3) Restrict the file system write and delete access to this file to a unique administrator account, different than the GENESIS administrator account.

Mitsubishi Electric GENESIS64: <=10.97.3

Product Status: known_affected

Remediations

Vendor fix
Mitsubishi Electric is releasing fixed version 10.98 or later for GENESIS64, ICONICS Suite, Hyper Historian, AnalytiX, and MobileHMI. Please download the fixed version from the link below and install it: "https://iconicsinc.my.site.com/community/s/resource-center/product-downloads". (Note: GENESIS64, Hyper Historian, AnalytiX, and MobileHMI are included in the ICONICS Suite installation.) For more information on the fixed version, please refer to the Mitsubishi Electric security advisory at "https://www.mitsubishielectric.com/psirt/vulnerability/pdf/2026-006_en.pdf".

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend configuring the PCs with the affected product installed so that only an administrator can log in, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend using the PCs with the affected product installed in the LAN and blocking remote login from untrusted networks and hosts, and from non-administrator users, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend blocking unauthorized access by using a firewall, virtual private network (VPN), etc. and allowing remote login only to administrator when internet access is required, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend restricting physical access to the PC with the affected product installed and the network to which the PC is connected, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend preventing the user from clicking on web links in emails from untrusted sources, or from opening attachments in untrusted emails, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend installing anti-virus software on the PC with the affected product installed, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend performing the following steps for GENESIS, GENESIS64, ICONICS Suite, Hyper Historian, AnalytiX, MobileHMI and MC Works64, to minimize the risk of exploitation of this vulnerability. (1) Delete the .dat file at the location specified below. This file name and location is different depending on the product version. (Version 10: C:\Program Files\ICONICS\GENESIS64\Components\ClientChallengeTable.dat; Version 11: C:\ProgramData\ICONICS\11\SecurityChallenges.dat) (2) Create a blank file with the same name and location. (3) Restrict the file system write and delete access to this file to a unique administrator account, different than the GENESIS administrator account.

Mitsubishi Electric ICONICS Suite: <=10.97.3

Product Status: known_affected

Remediations

Vendor fix
Mitsubishi Electric is releasing fixed version 10.98 or later for GENESIS64, ICONICS Suite, Hyper Historian, AnalytiX, and MobileHMI. Please download the fixed version from the link below and install it: "https://iconicsinc.my.site.com/community/s/resource-center/product-downloads". (Note: GENESIS64, Hyper Historian, AnalytiX, and MobileHMI are included in the ICONICS Suite installation.) For more information on the fixed version, please refer to the Mitsubishi Electric security advisory at "https://www.mitsubishielectric.com/psirt/vulnerability/pdf/2026-006_en.pdf".

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend configuring the PCs with the affected product installed so that only an administrator can log in, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend using the PCs with the affected product installed in the LAN and blocking remote login from untrusted networks and hosts, and from non-administrator users, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend blocking unauthorized access by using a firewall, virtual private network (VPN), etc. and allowing remote login only to administrator when internet access is required, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend restricting physical access to the PC with the affected product installed and the network to which the PC is connected, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend preventing the user from clicking on web links in emails from untrusted sources, or from opening attachments in untrusted emails, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend installing anti-virus software on the PC with the affected product installed, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend performing the following steps for GENESIS, GENESIS64, ICONICS Suite, Hyper Historian, AnalytiX, MobileHMI and MC Works64, to minimize the risk of exploitation of this vulnerability. (1) Delete the .dat file at the location specified below. This file name and location is different depending on the product version. (Version 10: C:\Program Files\ICONICS\GENESIS64\Components\ClientChallengeTable.dat; Version 11: C:\ProgramData\ICONICS\11\SecurityChallenges.dat) (2) Create a blank file with the same name and location. (3) Restrict the file system write and delete access to this file to a unique administrator account, different than the GENESIS administrator account.

Mitsubishi Electric Hyper Historian: <=10.97.3

Product Status: known_affected

Remediations

Vendor fix
Mitsubishi Electric is releasing fixed version 10.98 or later for GENESIS64, ICONICS Suite, Hyper Historian, AnalytiX, and MobileHMI. Please download the fixed version from the link below and install it: "https://iconicsinc.my.site.com/community/s/resource-center/product-downloads". (Note: GENESIS64, Hyper Historian, AnalytiX, and MobileHMI are included in the ICONICS Suite installation.) For more information on the fixed version, please refer to the Mitsubishi Electric security advisory at "https://www.mitsubishielectric.com/psirt/vulnerability/pdf/2026-006_en.pdf".

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend configuring the PCs with the affected product installed so that only an administrator can log in, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend using the PCs with the affected product installed in the LAN and blocking remote login from untrusted networks and hosts, and from non-administrator users, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend blocking unauthorized access by using a firewall, virtual private network (VPN), etc. and allowing remote login only to administrator when internet access is required, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend restricting physical access to the PC with the affected product installed and the network to which the PC is connected, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend preventing the user from clicking on web links in emails from untrusted sources, or from opening attachments in untrusted emails, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend installing anti-virus software on the PC with the affected product installed, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend performing the following steps for GENESIS, GENESIS64, ICONICS Suite, Hyper Historian, AnalytiX, MobileHMI and MC Works64, to minimize the risk of exploitation of this vulnerability. (1) Delete the .dat file at the location specified below. This file name and location is different depending on the product version. (Version 10: C:\Program Files\ICONICS\GENESIS64\Components\ClientChallengeTable.dat; Version 11: C:\ProgramData\ICONICS\11\SecurityChallenges.dat) (2) Create a blank file with the same name and location. (3) Restrict the file system write and delete access to this file to a unique administrator account, different than the GENESIS administrator account.

Mitsubishi Electric AnalytiX: <=10.97.3

Product Status: known_affected

Remediations

Vendor fix
Mitsubishi Electric is releasing fixed version 10.98 or later for GENESIS64, ICONICS Suite, Hyper Historian, AnalytiX, and MobileHMI. Please download the fixed version from the link below and install it: "https://iconicsinc.my.site.com/community/s/resource-center/product-downloads". (Note: GENESIS64, Hyper Historian, AnalytiX, and MobileHMI are included in the ICONICS Suite installation.) For more information on the fixed version, please refer to the Mitsubishi Electric security advisory at "https://www.mitsubishielectric.com/psirt/vulnerability/pdf/2026-006_en.pdf".

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend configuring the PCs with the affected product installed so that only an administrator can log in, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend using the PCs with the affected product installed in the LAN and blocking remote login from untrusted networks and hosts, and from non-administrator users, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend blocking unauthorized access by using a firewall, virtual private network (VPN), etc. and allowing remote login only to administrator when internet access is required, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend restricting physical access to the PC with the affected product installed and the network to which the PC is connected, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend preventing the user from clicking on web links in emails from untrusted sources, or from opening attachments in untrusted emails, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend installing anti-virus software on the PC with the affected product installed, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend performing the following steps for GENESIS, GENESIS64, ICONICS Suite, Hyper Historian, AnalytiX, MobileHMI and MC Works64, to minimize the risk of exploitation of this vulnerability. (1) Delete the .dat file at the location specified below. This file name and location is different depending on the product version. (Version 10: C:\Program Files\ICONICS\GENESIS64\Components\ClientChallengeTable.dat; Version 11: C:\ProgramData\ICONICS\11\SecurityChallenges.dat) (2) Create a blank file with the same name and location. (3) Restrict the file system write and delete access to this file to a unique administrator account, different than the GENESIS administrator account.

Mitsubishi Electric MobileHMI: <=10.97.3

Product Status: known_affected

Remediations

Vendor fix
Mitsubishi Electric is releasing fixed version 10.98 or later for GENESIS64, ICONICS Suite, Hyper Historian, AnalytiX, and MobileHMI. Please download the fixed version from the link below and install it: "https://iconicsinc.my.site.com/community/s/resource-center/product-downloads". (Note: GENESIS64, Hyper Historian, AnalytiX, and MobileHMI are included in the ICONICS Suite installation.) For more information on the fixed version, please refer to the Mitsubishi Electric security advisory at "https://www.mitsubishielectric.com/psirt/vulnerability/pdf/2026-006_en.pdf".

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend configuring the PCs with the affected product installed so that only an administrator can log in, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend using the PCs with the affected product installed in the LAN and blocking remote login from untrusted networks and hosts, and from non-administrator users, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend blocking unauthorized access by using a firewall, virtual private network (VPN), etc. and allowing remote login only to administrator when internet access is required, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend restricting physical access to the PC with the affected product installed and the network to which the PC is connected, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend preventing the user from clicking on web links in emails from untrusted sources, or from opening attachments in untrusted emails, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend installing anti-virus software on the PC with the affected product installed, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend performing the following steps for GENESIS, GENESIS64, ICONICS Suite, Hyper Historian, AnalytiX, MobileHMI and MC Works64, to minimize the risk of exploitation of this vulnerability. (1) Delete the .dat file at the location specified below. This file name and location is different depending on the product version. (Version 10: C:\Program Files\ICONICS\GENESIS64\Components\ClientChallengeTable.dat; Version 11: C:\ProgramData\ICONICS\11\SecurityChallenges.dat) (2) Create a blank file with the same name and location. (3) Restrict the file system write and delete access to this file to a unique administrator account, different than the GENESIS administrator account.

Mitsubishi Electric IoTWorX: <=10.97.3

Product Status: known_affected

Remediations

Vendor fix
Mitsubishi Electric is releasing fixed version 10.98 or later for IoTWorX. Please download the fixed version from the link below and install it: "https://hub.docker.com/r/iconics/iotworx". For more information on the fixed version, please refer to the Mitsubishi Electric security advisory at "https://www.mitsubishielectric.com/psirt/vulnerability/pdf/2026-006_en.pdf".

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend configuring the PCs with the affected product installed so that only an administrator can log in, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend using the PCs with the affected product installed in the LAN and blocking remote login from untrusted networks and hosts, and from non-administrator users, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend blocking unauthorized access by using a firewall, virtual private network (VPN), etc. and allowing remote login only to administrator when internet access is required, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend restricting physical access to the PC with the affected product installed and the network to which the PC is connected, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend preventing the user from clicking on web links in emails from untrusted sources, or from opening attachments in untrusted emails, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend installing anti-virus software on the PC with the affected product installed, to minimize the risk of exploitation of this vulnerability.

Mitsubishi Electric MC Works64: vers:all/*

Product Status: known_affected

Remediations

No fix planned
Mitsubishi Electric has no plans to release a fixed version of MC Works64. For customers using MC Works64, Mitsubishi Electric recommends taking the mitigations described in the Mitsubishi Electric's security advisory at "https://www.mitsubishielectric.com/psirt/vulnerability/pdf/2026-006_en.pdf". Alternatively, customers should consider replacing MC Works64 with GENESIS64 or GENESIS. For information on how to replace it, please refer to the following document: "GENESIS64 ? How to Replace MC Works64 with GENESIS64" (Japanese only): "https://www.mitsubishielectric.co.jp/dl/fa/members/document/manual/scada/bcn-p5999-1459/bcnp59991459a.pdf". Note: This document is published on Mitsubishi Electric FA website, and membership registration and login are required to view it.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend configuring the PCs with the affected product installed so that only an administrator can log in, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend using the PCs with the affected product installed in the LAN and blocking remote login from untrusted networks and hosts, and from non-administrator users, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend blocking unauthorized access by using a firewall, virtual private network (VPN), etc. and allowing remote login only to administrator when internet access is required, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend restricting physical access to the PC with the affected product installed and the network to which the PC is connected, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend preventing the user from clicking on web links in emails from untrusted sources, or from opening attachments in untrusted emails, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend installing anti-virus software on the PC with the affected product installed, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend performing the following steps for GENESIS, GENESIS64, ICONICS Suite, Hyper Historian, AnalytiX, MobileHMI and MC Works64, to minimize the risk of exploitation of this vulnerability. (1) Delete the .dat file at the location specified below. This file name and location is different depending on the product version. (Version 10: C:\Program Files\ICONICS\GENESIS64\Components\ClientChallengeTable.dat; Version 11: C:\ProgramData\ICONICS\11\SecurityChallenges.dat) (2) Create a blank file with the same name and location. (3) Restrict the file system write and delete access to this file to a unique administrator account, different than the GENESIS administrator account.

Mitsubishi Electric GENESIS32: vers:all/*

Product Status: known_affected

Remediations

No fix planned
Mitsubishi Electric has no plans to release fixed versions for GENESIS32 or BizViz. For customers using GENESIS32 or BizViz, Mitsubishi Electric recommends taking the mitigations described in the Mitsubishi Electric's security advisory at "https://www.mitsubishielectric.com/psirt/vulnerability/pdf/2026-006_en.pdf". Alternatively, customers should consider replacing GENESIS32 or BizViz with GENESIS64 or GENESIS.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend configuring the PCs with the affected product installed so that only an administrator can log in, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend using the PCs with the affected product installed in the LAN and blocking remote login from untrusted networks and hosts, and from non-administrator users, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend blocking unauthorized access by using a firewall, virtual private network (VPN), etc. and allowing remote login only to administrator when internet access is required, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend restricting physical access to the PC with the affected product installed and the network to which the PC is connected, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend preventing the user from clicking on web links in emails from untrusted sources, or from opening attachments in untrusted emails, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend installing anti-virus software on the PC with the affected product installed, to minimize the risk of exploitation of this vulnerability.

Mitsubishi Electric BizViz: vers:all/*

Product Status: known_affected

Remediations

No fix planned
Mitsubishi Electric has no plans to release fixed versions for GENESIS32 or BizViz. For customers using GENESIS32 or BizViz, Mitsubishi Electric recommends taking the mitigations described in the Mitsubishi Electric's security advisory at "https://www.mitsubishielectric.com/psirt/vulnerability/pdf/2026-006_en.pdf". Alternatively, customers should consider replacing GENESIS32 or BizViz with GENESIS64 or GENESIS.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend configuring the PCs with the affected product installed so that only an administrator can log in, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend using the PCs with the affected product installed in the LAN and blocking remote login from untrusted networks and hosts, and from non-administrator users, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend blocking unauthorized access by using a firewall, virtual private network (VPN), etc. and allowing remote login only to administrator when internet access is required, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend restricting physical access to the PC with the affected product installed and the network to which the PC is connected, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend preventing the user from clicking on web links in emails from untrusted sources, or from opening attachments in untrusted emails, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend installing anti-virus software on the PC with the affected product installed, to minimize the risk of exploitation of this vulnerability.

Mitsubishi Electric Iconics Digital Solutions GENESIS: <=11.03

Product Status: known_affected

Remediations

Vendor fix
Mitsubishi Electric Iconics Digital Solutions is releasing fixed version 11.04 or later for GENESIS. Please download the fixed version from the link below and install it: "https://iconicsinc.my.site.com/community/s/resource-center/product-downloads". For more information on the fixed version, please refer to the Mitsubishi Electric Iconics Digital Solutions whitepaper on security vulnerabilities, which can be found at "https://iconics.com/about/security/cert".

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend configuring the PCs with the affected product installed so that only an administrator can log in, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend using the PCs with the affected product installed in the LAN and blocking remote login from untrusted networks and hosts, and from non-administrator users, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend blocking unauthorized access by using a firewall, virtual private network (VPN), etc. and allowing remote login only to administrator when internet access is required, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend restricting physical access to the PC with the affected product installed and the network to which the PC is connected, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend preventing the user from clicking on web links in emails from untrusted sources, or from opening attachments in untrusted emails, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend installing anti-virus software on the PC with the affected product installed, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend performing the following steps for GENESIS, GENESIS64, ICONICS Suite, Hyper Historian, AnalytiX, MobileHMI and MC Works64, to minimize the risk of exploitation of this vulnerability. (1) Delete the .dat file at the location specified below. This file name and location is different depending on the product version. (Version 10: C:\Program Files\ICONICS\GENESIS64\Components\ClientChallengeTable.dat; Version 11: C:\ProgramData\ICONICS\11\SecurityChallenges.dat) (2) Create a blank file with the same name and location. (3) Restrict the file system write and delete access to this file to a unique administrator account, different than the GENESIS administrator account.

Mitsubishi Electric Iconics Digital Solutions GENESIS64: <=10.97.3

Product Status: known_affected

Remediations

Vendor fix
Mitsubishi Electric Iconics Digital Solutions is releasing fixed version 10.98 or later for GENESIS64, ICONICS Suite, Hyper Historian, AnalytiX, and MobileHMI. Please download the fixed version from the link below and install it: "https://iconicsinc.my.site.com/community/s/resource-center/product-downloads". (Note: GENESIS64, Hyper Historian, AnalytiX, and MobileHMI are included in the ICONICS Suite installation.) For more information on the fixed version, please refer to the Mitsubishi Electric Iconics Digital Solutions whitepaper on security vulnerabilities, which can be found at "https://iconics.com/about/security/cert".

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend configuring the PCs with the affected product installed so that only an administrator can log in, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend using the PCs with the affected product installed in the LAN and blocking remote login from untrusted networks and hosts, and from non-administrator users, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend blocking unauthorized access by using a firewall, virtual private network (VPN), etc. and allowing remote login only to administrator when internet access is required, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend restricting physical access to the PC with the affected product installed and the network to which the PC is connected, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend preventing the user from clicking on web links in emails from untrusted sources, or from opening attachments in untrusted emails, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend installing anti-virus software on the PC with the affected product installed, to minimize the risk of exploitation of this vulnerability.

Mitigation
For customers of products that do not have a fixed version or who cannot immediately update the product, Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions recommend performing the following steps for GENESIS, GENESIS64, ICONICS Suite, Hyper Historian, AnalytiX, MobileHMI and MC Works64, to minimize the risk of exploitation of this vulnerability. (1) Delete the .dat file at the location specified below. This file name and location is different depending on the product version. (Version 10: C:\Program Files\ICONICS\GENESIS64\Components\ClientChallengeTable.dat; Version 11: C:\ProgramData\ICONICS\11\SecurityChallenges.dat) (2) Create a blank file with the same name and location. (3) Restrict the file system write and delete access to this file to a unique administrator account, different than the GENESIS administrator account.

Mitsubishi Electric Iconics Digital Solutions ICONICS Suite: <=10.97.3

Product Status: known_affected

Remediations

Vendor fix
Mitsubishi Electric Iconics Digital Solutions is releasing fixed version 10.98 or later for GENESIS64, ICONICS Suite, Hyper Historian, AnalytiX, and Mobi

> ⚠️ 快照已截断（原文超长）

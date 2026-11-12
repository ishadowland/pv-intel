<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://otsecuritywire.com/articles/mitsubishi-iconics-genesis64-icsa-26-300-02-challenge-response-dcom-libwebp-2026 -->
<!-- fetched_at: 2026-11-13 07:11:34 -->
<!-- sha256: 3fe7444f03ae15a9e07598f4eb3d417adac78b8d7621474b1b8975ea9774f72b -->

ICONICS GENESIS64 ICSA-26-300-02: Fixed Unlock Challenge Response, DCOM Privilege Flaw and No Fix for MC Works64 (CVE-2026-16436 to 16438) | OT/ICS Monitor
Skip to main content System Status Critical 21
| High 77
| Medium 3
| Feed Online

UPDATED: 2026-06-11 00:00 UTC

Home / Advisories / Vulnerability Analysis
Vulnerability Analysis high
ICONICS GENESIS64 ICSA-26-300-02: Fixed Unlock Challenge Response, DCOM Privilege Flaw and No Fix for MC Works64 (CVE-2026-16436 to 16438)
CISA's ICSA-26-300-02 (Revision 3, 29 October 2026) covers Mitsubishi Electric ICONICS GENESIS64, Hyper Historian and MC Works64: a fixed challenge response, a DCOM permission flaw and libwebp CVE-2023-4863. Fixes in 10.98 and 11.04; none for MC Works64.
Published
Nov 3, 2026

Author
OT/ICS Monitor

Type
Vulnerability Analysis

Severity
HIGH

CVE Identifier
CVE-2026-16436

Overview

CISA’s advisory ICSA-26-300-02 covers the ICONICS SCADA/HMI family sold by Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions: GENESIS64, ICONICS Suite, Hyper Historian, AnalytiX, MobileHMI, IoTWorX, GENESIS (v11), MC Works64, GENESIS32 and BizViz. CISA lists the sector as Critical Manufacturing, deployed worldwide, with a top-level CVSS v3 of 9.1. Per the advisory’s revision history, the vendor published on 15 October 2026 (Mitsubishi Electric 2026-006), CISA republished on 27 October, and Revision 3 on 29 October updated the vendor and product name. Mitsubishi Electric discovered the flaws; no external researcher is credited.

The vulnerabilities

CVE CWE CVSS v3.1 CVSS v4.0
CVE-2026-16436 CWE-640 8.1 High 9.2 Critical
CVE-2026-16437 CWE-640 6.4 Medium 7.1 High
CVE-2026-16438 CWE-266 9.1 Critical 9.4 Critical
CVE-2023-4863 (libwebp) CWE-787 8.2 High (CISA) 9.3 Critical (CISA)

Scores above are as published in the CISA advisory. NVD lists CVE-2026-16436, 16437 and 16438 as “Awaiting Analysis” as of 3 November 2026 and carries only the CVSS v4.0 scores supplied by the vendor CNA (9.2, 7.1 and 9.4, matching CISA). NVD shows no v3.1 score for these three yet, so the v3.1 figures are single-source (CISA). For CVE-2023-4863, NVD’s own score is 8.8 ( AV:N/AC:L/PR:N/UI:R ), because CISA rescored it for this product’s local, admin-only import path.

CVE-2026-16436 is the one to prioritise. The products use a challenge-response mechanism to unlock the system, and the response is “common to all users and fixed” (vendor CNA text in NVD). A remote attacker who obtains it by some means can unlock the system and then disclose, tamper with, destroy or delete data, or cause denial of service. CISA’s v3.1 vector is AV:N/AC:H/PR:N , reflecting that obtaining the response is the hard part.

CVE-2026-16437 is the local variant: an administrator can unlock the system by tampering with the management file that stores the challenge response. Per the advisory, the file is protected only by Windows permissions.

CVE-2026-16438 is an installer flaw. Per the vendor CNA text, installers unnecessarily grant default DCOM permissions to the product’s administrator account, so users with that account can launch and operate DCOM objects locally or remotely that should require UAC elevation. CISA’s vector is AV:N/AC:L/PR:H/S:C . In our assessment this matters most on servers where one shared administrator account is used across engineering workstations and the SCADA server, since DCOM (RPC over TCP 135 plus a dynamic port range) then becomes a remote execution path for anyone holding that credential.

CVE-2023-4863 is the libwebp heap overflow embedded in GENESIS64 and ICONICS Suite 10.97 to 10.97.2. In this product, CISA describes it as exploitable by an authenticated local administrator importing a crafted file. NVD records CVE-2023-4863 as added to the CISA KEV catalog on 13 September 2023.

Affected and fixed versions (CISA)

GENESIS64, ICONICS Suite, Hyper Historian, AnalytiX, MobileHMI: 10.97.3 and prior. Fixed in 10.98 or later. The libwebp issue is fixed from 10.97.3.

IoTWorX: 10.97.3 and prior. Fixed in 10.98 or later, distributed through Docker Hub. It is not listed for CVE-2026-16438.

GENESIS (v11): 11.03 and prior. Fixed in 11.04 or later.

MC Works64, GENESIS32 and BizViz: all versions. No fix planned; the vendor recommends migrating to GENESIS64 or GENESIS.

The no-fix group is the operational problem. MC Works64 is common in Mitsubishi-centred plants, and migration of a Windows SCADA project is a project, not a patch window.

Mitigations when you cannot upgrade

CISA relays a vendor workaround for CVE-2026-16436 and CVE-2026-16437:

Delete the challenge file ( C:\Program Files\ICONICS\GENESIS64\Components\ClientChallengeTable.dat on v10, C:\ProgramData\ICONICS\11\SecurityChallenges.dat on v11).

Create a blank file with the same name and location.

Restrict write and delete rights on it to a dedicated administrator account that is separate from the GENESIS administrator account.

General measures from the advisory: allow only administrators to log in to the PC, keep systems on the LAN, block remote login from untrusted networks, restrict physical access, and use a firewall or VPN where remote administration is required. Our additions: separate the GENESIS administrator identity from domain and engineering accounts to blunt CVE-2026-16438, and block DCOM/RPC between zones at the Level 3 boundary.

Exploitation status

No evidence found as of 3 November 2026 in the CISA advisory or NVD of exploitation of CVE-2026-16436, 16437 or 16438. Only CVE-2023-4863 has known exploitation, and that is in browsers and other libwebp consumers, not documented against ICONICS.

Sources

CISA ICSA-26-300-02

NVD API records for CVE-2026-16436, CVE-2026-16437, CVE-2026-16438 and CVE-2023-4863 (services.nvd.nist.gov, queried 3 November 2026)

Tags
ICONICS GENESIS64 MC Works64 Hyper Historian DCOM CWE-640 CWE-266 CVE-2026-16436 CVE-2026-16438 ICSA-26-300-02

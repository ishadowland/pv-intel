<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.danfoss.com/en/service-and-support/coordinated-vulnerability-disclosure/danfoss-security-advisories/dsa-2026-12-01/ -->
<!-- fetched_at: 2026-11-25 07:33:55 -->
<!-- sha256: f40c776dc0dd54e46c4b890d5aa5a6ce6edf40fba1bb3fc1593859abd93a2182 -->

DSA-2026-12-01 | Danfoss

Skip to main content

Home page

/
...
/

/

Service and support

/
Coordinated vulnerability disclosure

/
Danfoss security advisories

/
DSA-2026-12-01

DSA-2026-12-01

Stack-based buffer overflow in Danfoss AK-SM 8xxA unauthenticated CGI handler
Advisory Information
Advisory ID: DSA-2026-12-01
CVE numbers and CVSS scores
CVE number: CVE-2026-129713

CVSS:9.3

Summary
Stack-Based Buffer Overflow in Danfoss AK-SM 8xxA Series
Affected products and services
Danfoss AK-SM 8xxA - version 5.4.0 and earlier

Vulnerability description
A stack-based buffer overflow in an unauthenticated CGI handler of the Danfoss AK-SM 8xxA Series controller allows remote attackers to send specially crafted HTTP/S POST requests, leading to memory corruption, webserver restart and hypothetically potential arbitrary code execution with webserver privileges. Authentication is not required to exploit this vulnerability.
Remediations
This vulnerability will be addressed in Danfoss AK-SM 8xxA Series upcoming software version 5.5.x.

Further, we will remove the option that customers can disable the product Strict mode.

Mitigations
Follow the instructions provided in the product’s manual, avoiding Internet exposure of all units on public IP
• Make sure remote access to the units is possible only through a secure VPN or in general over a protected network
• Configure the units to Strict mode, which ensures higher security levels on the product
• Recommend using strong passwords

Credits (if opted in)
N/A

Other reference
https://www.danfoss.com/en/service-and-support/downloads/dcs/adap-kool-software/ak-sm-800a/#tab-overview
Update log
20 November, 2026: Publication

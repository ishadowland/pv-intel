<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-05 -->
<!-- fetched_at: 2026-11-18 07:10:58 -->
<!-- sha256: 218d67a73e684ebadf469817bcd523d668f2a593dc8bcdd0fc6c3fd46dd2da44 -->

Siemens Mendix Studio Pro | CISA

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

Siemens Mendix Studio Pro

Release Date
November 17, 2026

Alert Code
ICSA-26-321-05

Related topics:

Industrial Control System Vulnerabilities
,
Industrial Control Systems

View CSAF

Summary

Mendix Studio Pro contains multiple vulnerabilities in the MCP Server, that could allow an attacker with network access to interact with the server remotely or trick a user's browser into sending unauthorized requests, potentially leading to unauthorized data access, tool execution, or system compromise. Siemens has released new versions for the affected products and recommends to update to the latest versions.

The following versions of Siemens Mendix Studio Pro are affected:

Mendix Studio Pro 11 vers:intdot/>=11.15.0|<11.16.0 (CVE-2026-112136, CVE-2026-112137)

Mendix Studio Pro 11.12 vers:intdot/>=11.12.6|<11.12.7 (CVE-2026-112136, CVE-2026-112137)

CVSS
Vendor
Equipment

v3 8.8
Siemens
Mendix Studio Pro 11

2 Vulnerabilities

Binding to an Unrestricted IP Address, Cross-Site Request Forgery (CSRF)

Background

Critical Infrastructure Sectors: Critical Manufacturing, Energy

Countries/Areas Deployed: Worldwide

Company Headquarters Location: Germany

Vulnerabilities

Expand All +

CVE-2026-112136

The affected products MCP Server does not properly restrict its HTTP listener to the loopback interface, leaving it potentially exposed to remote systems. This could allow an attacker with network access to interact with the MCP Server remotely.

Read More

2 Affected Products

Mendix Studio Pro 11 >= V11.15.0 < V11.16.0

Product Status: known_affected

Remediations

Mitigation
Maintain strict inbound firewall policies (such as Windows Defender Firewall) blocking external traffic on port 7782. This is already the case by default on standard Windows installations. If remote access is required, restrict traffic via a secure, authenticated channel (e.g., a VPN or SSH tunnel) rather than opening direct inbound firewall rules.

Vendor fix
Update to V11.16.0 or later version

Mendix Studio Pro 11.12 >= V11.12.6 < V11.12.7

Product Status: known_affected

Remediations

Mitigation
Maintain strict inbound firewall policies (such as Windows Defender Firewall) blocking external traffic on port 7782. This is already the case by default on standard Windows installations. If remote access is required, restrict traffic via a secure, authenticated channel (e.g., a VPN or SSH tunnel) rather than opening direct inbound firewall rules.

Vendor fix
Update to V11.12.7 or later version

Additional Metrics

Relevant CWE: CWE-1327 Binding to an Unrestricted IP Address

CVSS Version
Base Score
Base Severity
Vector String

3.1
8.8
HIGH
CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:H

View CVE Details

CVE-2026-112137

The affected products MCP Server does not properly validate Content-Type and Origin headers on incoming HTTP requests, leaving it vulnerable to Cross-Site Request Forgery (CSRF). This could allow a malicious web page to trick a user's browser into sending unauthorized requests and executing unintended actions on the local MCP Server.

Read More

4 Affected Products

Mendix Studio Pro 11 >= V11.15.0 < V11.16.0

Product Status: known_affected

Remediations

Mitigation
Utilize modern Chromium- or WebKit-based browsers with Private Network Access protections enabled, or use browser extensions (such as uBlock Origin or NoScript) to block external websites from issuing fetch requests to localhost (127.0.0.1).

Vendor fix
Update to V11.16.0 or later version

Mendix Studio Pro 11.12 >= V11.12.6 < V11.12.7

Product Status: known_affected

Remediations

Mitigation
Utilize modern Chromium- or WebKit-based browsers with Private Network Access protections enabled, or use browser extensions (such as uBlock Origin or NoScript) to block external websites from issuing fetch requests to localhost (127.0.0.1).

Vendor fix
Update to V11.12.7 or later version

Mendix Studio Pro 11 >= V11.15.0 < V11.16.0

Product Status: known_affected

Remediations

Mitigation
Utilize modern Chromium- or WebKit-based browsers with Private Network Access protections enabled, or use browser extensions (such as uBlock Origin or NoScript) to block external websites from issuing fetch requests to localhost (127.0.0.1).

Vendor fix
Update to V11.16.0 or later version

Mendix Studio Pro 11.12 >= V11.12.6 < V11.12.7

Product Status: known_affected

Remediations

Mitigation
Utilize modern Chromium- or WebKit-based browsers with Private Network Access protections enabled, or use browser extensions (such as uBlock Origin or NoScript) to block external websites from issuing fetch requests to localhost (127.0.0.1).

Vendor fix
Update to V11.12.7 or later version

Additional Metrics

Relevant CWE: CWE-352 Cross-Site Request Forgery (CSRF)

CVSS Version
Base Score
Base Severity
Vector String

3.1
5.4
MEDIUM
CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:L/A:L

View CVE Details

Acknowledgments

Siemens ProductCERT reported these vulnerabilities to CISA.

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

This ICSA is a verbatim republication of Siemens ProductCERT SSA-710379 from a direct conversion of the vendor's Common Security Advisory Framework (CSAF) advisory. This is republished to CISA's website as a means of increasing visibility and is provided "as-is" for informational purposes only. CISA is not responsible for the editorial or technical accuracy of republished advisories and provides no warranties of any kind regarding any information contained within this advisory. Further, CISA does not endorse any commercial product or service. Please contact Siemens ProductCERT directly for any questions regarding this advisory.

Revision History

Initial Release Date: 2026-11-10

Date
Revision
Summary

2026-11-10
1
Publication Date

2026-11-16
2
Mapped the advisory to Mendix products to be present on the Mendix Atom Feed

2026-11-17
3
Initial CISA Republication of Siemens ProductCERT SSA-710379 advisory

Legal Notice and Terms of Use

This product is provided subject to this Notification and this Privacy & Use policy.

Vendor

Siemens

Tags

Sector :
Critical Manufacturing Sector ,
Energy Sector

Topics :
Industrial Control System Vulnerabilities ,
Industrial Control Systems

Please share your thoughts

We recently updated our anonymous product survey ; we welcome your feedback.

Related Advisories

Nov 17, 2026

ICS Advisory | ICSA-26-321-01

Dorsett Controls InfoScan

Nov 17, 2026

ICS Advisory | ICSA-26-321-03

Siemens Industrial Automation Software Products

Nov 17, 2026

ICS Advisory | ICSA-26-321-11

Siemens meta-iot2050

Nov 17, 2026

ICS Advisory | ICSA-26-321-02

Siemens .NET Client Library for SIMATIC S7 Webserver API

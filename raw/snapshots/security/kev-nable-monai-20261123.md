<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://securityaffairs.com/203882/hacking/u-s-cisa-adds-n-able-mailassure-and-project-monai-flaws-to-its-known-exploited-vulnerabilities-catalog.html -->
<!-- fetched_at: 2026-11-25 07:12:22 -->
<!-- sha256: 74e0b3a9e7da6879360fc9fd802c957162112941142d80d277e5226980b4b6f1 -->

U.S. CISA adds N-able MailAssure and Project MONAI flaws to its Known Exploited Vulnerabilities catalog

Home

Breaking News

Hacking

Security

U.S. CISA adds N-able MailAssure and Project MONAI flaws to its Known Exploited Vulnerabilities catalog

U.S. CISA adds N-able MailAssure and Project MONAI flaws to its Known Exploited Vulnerabilities catalog

Pierluigi Paganini
November 24, 2026

U.S. Cybersecurity and Infrastructure Security Agency (CISA) adds N-able MailAssure and Project MONAI flaws to its Known Exploited Vulnerabilities catalog.

The U.S. Cybersecurity and Infrastructure Security Agency (CISA) added N-able MailAssure and Project MONAI vulnerabilities to its Known Exploited Vulnerabilities (KEV) catalog :

CVE-2026-133968 Project MONAI MONAI Label Path Traversal Vulnerability

CVE-2026-134624 N-able Mail Assure (SpamExperts) Server-Side Request Forgery (SSRF) Vulnerability

The first flaw is CVE-2026-133968 (CVSS score of 9.8), a critical path traversal vulnerability in Project MONAI’s MONAI Label. It affects versions up to 0.8.5 and allows unauthenticated remote attackers to access files outside the intended directory through the image parameter in the PUT /datastore/image endpoint. Successful exploitation can also lead to remote code execution, potentially allowing attackers to take control of the affected server. The vulnerability has been exploited in the wild since September 2026, before its public disclosure on November 20.

Amazon Threat Intelligence linked the exploitation to a Chinese-nexus threat actor, with moderate confidence. According to Amazon, the attackers used autonomous AI agents running the open-source Cairn framework to discover and exploit the zero-day. The agents reportedly gained root access to a university server and later used the vulnerability to target another university network. Amazon has not identified a specific threat group. The vulnerability was fixed in MONAI Label 0.8.6.

The second flaw is CVE-2026-134624 (CVSS score of 9.3), a critical Server-Side Request Forgery (SSRF) vulnerability in N-able Mail Assure (SpamExperts). The flaw affects versions earlier than 20261121.1943 and exists in the LDAP synchronisation connection check performed when a relay is configured. It does not properly restrict the destination of the connection, allowing an authenticated API user with sufficient privileges to make the vulnerable server connect to arbitrary internal IP addresses and ports. Attackers could use this capability to identify accessible internal systems and send crafted requests to internal services. N-able

N-able disclosed the vulnerability while investigating a cyberattack against its Mail Assure and SpamExperts Hosted Cloud environments. The company confirmed that attackers had accessed a web server and said its investigation had found no evidence of exploitation beyond a single N-able-hosted server. However, it has not confirmed whether CVE-2026-134624 was the vulnerability exploited to gain initial access. No threat actor has been publicly identified. The flaw was fixed in version 20261121.1943, and N-able restored access to the affected services on November 21, 2026.

According to Binding Operational Directive (BOD) 22-01: Reducing the Significant Risk of Known Exploited Vulnerabilities , FCEB agencies have to address the identified vulnerabilities by the due date to protect their networks against attacks exploiting the flaws in the catalog.

Experts also recommend that private organizations review the Catalog and address the vulnerabilities in their infrastructure.

CISA orders federal agencies to fix the vulnerabilities by November 26.

Follow me on Twitter: @securityaffairs and Facebook and Mastodon

Pierluigi Paganini

( SecurityAffairs – hacking, CISA )

facebook
linkedin
twitter

CISA
CVE-2026-133968
CVE-2026-134624
Hacking
hacking news
information security news
IT Information Security
Known Exploited Vulnerabilities Catalog
Pierluigi Paganini
Security Affairs
Security News

you might also like

Pierluigi Paganini
November 24, 2026

EU Academy Users' Names and Emails Exposed in EU Commission Hack

Read more

Pierluigi Paganini
November 24, 2026

Hackers May Have Breached FBI Database Used by Police Nationwide

Read more

leave a comment

newsletter

Subscribe to my email list and stay
up-to-date!

recent articles

EU Academy Users' Names and Emails Exposed in EU Commission Hack

Data Breach / November 24, 2026

U.S. CISA adds N-able MailAssure and Project MONAI flaws to its Known Exploited Vulnerabilities catalog

Hacking / November 24, 2026

Hackers May Have Breached FBI Database Used by Police Nationwide

Cyber Crime / November 24, 2026

Cleverbridge Confirms Attackers Copied Payment Card Data From Its Platform

Data Breach / November 23, 2026

Microsoft Entra Connect Health Breach Exposes Tenant Metadata and Admin Details

Data Breach / November 23, 2026

We use cookies on our website to give you the most relevant experience by remembering your preferences and repeat visits. By clicking “Accept All”, you consent to the use of ALL the cookies. However, you may visit "Cookie Settings" to provide a controlled consent.
Cookie Settings Accept All

Manage consent

Close

Privacy Overview

This website uses cookies to improve your experience while you navigate through the website. Out of these cookies, the cookies that are categorized as necessary are stored on your browser as they are essential for the working of basic functionalities of the website. We also use third-party cookies that help us analyze and understand how you use this website. These cookies will be stored in your browser only with your consent. You also have the option to opt-out of these cookies. But opting out of some of these cookies may have an effect on your browsing experience.

Necessary

Necessary

Always Enabled

Necessary cookies are absolutely essential for the website to function properly. This category only includes cookies that ensures basic functionalities and security features of the website. These cookies do not store any personal information.

Non-necessary

Non-necessary

Any cookies that may not be particularly necessary for the website to function and is used specifically to collect user personal data via analytics, ads, other embedded contents are termed as non-necessary cookies. It is mandatory to procure user consent prior to running these cookies on your website.

SAVE & ACCEPT

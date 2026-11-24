<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://exeo.net/en/threat-intelligence/actively-exploited-insecure-deserialization-vulnerability-in-apache-roller-cve-2026-129448 -->
<!-- fetched_at: 2026-11-24 07:12:48 -->
<!-- sha256: 861d07b0eee67c0bf00febbe4986782acb7e36b40ef5b72875d9ecd45ef70d94 -->

CVE-2026-129448: Actively exploited insecure deserialization vulnerability in Apache Roller (CVSS 9.8) | EXEO

Skip to content

Threat Intelligence / Advisory

Threat Advisory

Actively exploited insecure deserialization vulnerability in Apache Roller (CVE-2026-129448)

CRITICAL Actively exploited CVSS 9.8 insecure-deserialization EXEO Argos
Published November 20, 2026

What happened

Apache Roller has a CWE-502 deserialisation of untrusted data vulnerability in its XML-RPC endpoint. The endpoint accepts vendor extension types and deserialises them before authenticating the requester. An attacker can exploit an exposed service directly over a network, without prior access or user involvement, to execute arbitrary code. The vulnerability is being actively exploited and is listed in the CISA Known Exploited Vulnerabilities catalogue. The reported severity is critical, with a CVSS base score of 9.8 from apache.org; this score is served by NVD and is not NVD’s own analysis.

A fix is available, and applying the vendor’s fix is recommended.

Who is affected

Organisations running Apache Roller versions 4.0.0 to before 6.1.5 are affected. The issue applies to the Apache Roller XML-RPC service. Disabling XML-RPC through the administration interface alone is not sufficient: affected versions may deserialise a request before checking that setting.

Recommended actions

Apply the vendor’s fix to affected Apache Roller deployments.

Restrict network exposure of the XML-RPC service so that it cannot be reached from untrusted networks.

Place access controls in front of the service to limit which network sources can reach it.

Set enabledForExtensions to false in WEB-INF/web.xml , or remove the /roller-services/xmlrpc servlet mapping, and restart Roller if an immediate upgrade is not possible. Disabling XML-RPC in the administration interface alone does not address the deserialisation path.

CVE
CVE-2026-129448

Affected

Vendors: Apache
Products: Roller

Source

CISA KEV — Read article

References

https://nvd.nist.gov/vuln/detail/CVE-2026-129448

Tags

actively-exploited apache cisa-kev insecure-deserialization roller

Is your organisation exposed?
Argos matches live threat intelligence to your own asset inventory and tells you what actually affects you.

Discover Argos

Related advisories
All advisories →

CRITICAL November 20, 2026

China-Linked Hackers Exploit Critical VMware vCenter Zero-Day to Gain Admin Access and Steal Data

CRITICAL November 20, 2026

Actively exploited hard-coded credentials in database service feature of Cisco Expressway Series (CVE-2026-76466)

MEDIUM November 20, 2026

Actively exploited injection vulnerability in SAP NetWeaver Enterprise Portal (CVE-2025-42884)

At a glance

Severity critical
CVSS 9.8
CVE CVE-2026-129448
Published November 20, 2026

Vendor Apache
Products Roller
Regions global

Get in touch

We respond within 1 hour on weekdays

This channel is not monitored by HR. For a job application or an internship, please visit our Join Us page.

We use cookies on our website to give you the most relevant experience by remembering your preferences and repeat visits. By clicking “Accept”, you consent to the use of ALL the cookies.
Privacy Policy Cookie Settings ACCEPT ALL

Revisit Consent

Close

Privacy

This website uses cookies to improve your experience while you navigate through the website. Out of these cookies, the cookies that are categorized as necessary are stored on your browser as they are essential for the working of basic functionalities of the website. We also use third-party cookies that help us analyze and understand how you use this website. These cookies will be stored in your browser only with your consent. You also have the option to opt-out of these cookies. But opting out of some of these cookies may have an effect on your browsing experience.

Necessary

Necessary

Always Enabled

Necessary cookies are absolutely essential for the website to function properly. This category only includes cookies that ensures basic functionalities and security features of the website. These cookies do not store any personal information.
Cookie Duration Description
__cfduid 1 month The cookie is used by CloudFare to identify individual clients behind a shared IP address and apply security settings on a per-client basis. It does not correspond to any user ID in the web application and does not store any personally identifiable information.
cookielawinfo-checkbox-advertisement 1 year The cookie is set by GDPR cookie consent to record the user consent for the cookies in the category "Advertisement".
cookielawinfo-checkbox-analytics 1 year This cookies is set by GDPR Cookie Consent WordPress Plugin. The cookie is used to remember the user consent for the cookies under the category "Analytics".
cookielawinfo-checkbox-functional 1 year The cookie is set by GDPR cookie consent to record the user consent for the cookies in the category "Functional".
cookielawinfo-checkbox-necessary 1 year This cookie is set by GDPR Cookie Consent plugin. The cookies is used to store the user consent for the cookies in the category "Necessary".
cookielawinfo-checkbox-others 1 year No description
cookielawinfo-checkbox-performance 1 year This cookie is set by GDPR Cookie Consent plugin. The cookie is used to store the user consent for the cookies in the category "Performance".
pll_language 1 year The cookie stores the language code of the last browsed page.

Analytics

analytics

Analytical cookies are used to understand how visitors interact with the website. These cookies help provide information on metrics the number of visitors, bounce rate, traffic source, etc.
Cookie Duration Description
_clck 1 year Used by Microsoft Clarity to store a unique user ID
_clsk Microsoft Clarity analytics application
_ga 2 years This cookie is installed by Google Analytics. The cookie is used to calculate visitor, session, campaign data and keep track of site usage for the site's analytics report. The cookies store information anonymously and assign a randomly generated number to identify unique visitors.
_ga_L2RPNQR0FJ 2 years This cookie is set by Google Analytics 4 to persist session state and count sessions for this property.
_gat_gtag_UA_44752404_1 1 minute No description
_gid 1 day This cookie is installed by Google Analytics. The cookie is used to store information of how visitors use a website and helps in creating an analytics report of how the wbsite is doing. The data collected including the number visitors, the source where they have come from, and the pages viisted in an anonymous form.
_lfa 2 years This cookie is set by the provider Leadfeeder. This cookie is used for identifying the IP address of devices visiting the website. The cookie collects information such as IP addresses, time spent on website and page requests for the visits.This collected information is used for retargeting of multiple users routing from the same IP address.
CLID 1 year Microsoft Clarity
of.tracking 1 year
ofs
SL_C_23361dd035530_KEY Outfunnel Campaign
SL_C_23361dd035530_SID Outfunnel Campaign
SL_C_23361dd035530_VID Outfunnel Campaign
SM session Used in synchronizing the MUID across Microsoft domains.
SRM_B 1 year 24 days Identifies unique web browsers visiting Microsoft sites
vuid 2 years This domain of this cookie is owned by Vimeo. This cookie is used by vimeo to collect tracking information. It sets a unique ID to embed videos to the website.

Advertisement

advertisement

Advertisement cookies are used to provide visitors with relevant ads and marketing campaigns. These cookies track visitors across websites and collect information to provide customized ads.
Cookie Duration Description
__oppref 30 days Cookie used by OpenAI Ads to measure the performance of ads on ChatGPT.
_gcl_au 3 months This cookie is set by Google Tag Manager and Google Ads to measure how well advertising performs and to attribute conversions to ad clicks.
ANONCHK 10 minutes This cookie is used for storing the session ID for a user. This cookie ensures that clicks from advertisement on the Bing search engine are verified and it is used for reporting purposes and for personalization.
MUID 1 year 24 days Used by Microsoft as a unique identifier. The cookie is set by embedded Microsoft scripts. The purpose of this cookie is to synchronize the ID across many different Microsoft domains to enable user tracking.
oaacct 30 days Stores which EXEO OpenAI ads account referred the visit, so that conversions are measured in the right account. Set only after advertising consent.

Others

others

Other uncategorized cookies are those that are being analyzed and have not been classified into a category as yet.

Functional

functional-en

Save & Accept

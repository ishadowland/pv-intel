<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://breach-signal.com/vulnerabilities/cisa-emergency-advisory-openjdk-cve-2026-114938 -->
<!-- fetched_at: 2026-11-19 07:11:14 -->
<!-- sha256: c5d610e6b9fea76a3a919c5f5b4212af53bb74ebd7bedec5b0a2ec5415e73696 -->

CISA warns of OpenJDK Java4Shell flaw CVE-2026-114938

Skip to content
Skip to content

Thursday, November 19, 2026

High-level officials and board members gather around a conference table to coordinate on critical cybersecurity policy and national security initiatives. Photo by DHSgov on Wikimedia Commons

Share
Facebook
X
LinkedIn
WhatsApp
More
Reddit
Bluesky
Mastodon
Hacker News
Email
Copy link
Print
Share

Key facts
Java4Shell affects OpenJDK versions 17, 21, 25 and 27.
Oracle rates the flaw CVSS 3.1 score 8.1 (High), while Calif rates it CVSS 4.0 score 9.2 (Critical).
The defect affects CPUs that support AVX-512 VBMI instructions; ARM-based servers such as AWS Graviton are not affected.
Calif, a California-based security firm, found the flaw and published details on November 17, 2026, after a leak preceded coordinated disclosure.

Calif, a California-based security firm, found the flaw and published details on November 17, 2026, after a leak preceded coordinated disclosure. CISA put out an emergency advisory on November 17 telling organizations to apply patches immediately once they are available.

Java4Shell is the nickname for CVE-2026-114938, a memory corruption vulnerability in OpenJDK that the OpenJDK advisory classifies under hotspot/compiler. It affects OpenJDK versions 17, 21, 25 and 27. Oracle rates the flaw CVSS 3.1 at 8.1 (High), while Calif rates it CVSS 4.0 at 9.2 (Critical). OpenJDK is an open-source Java SE implementation co-maintained by Oracle and a global community including Red Hat, Amazon and Microsoft.

PHP2Shell had preceded Java4Shell by weeks, and Calif said the potential blast radius could be broad because many Java applications based on OpenJDK are exposed. The firm has reportedly withheld product-specific exploits to give organizations time to update. The Optimizely hack affected 178 organizations, showing how quickly supply-chain and web attacks can spread after exploit code becomes available.

Exploitation lets unauthenticated attackers corrupt memory on Java servers through a single malformed message, and Oracle says attackers can exploit remotely without authentication by sending data to vulnerable APIs, for example through a web service. Oracle rates attack complexity as high. The flaw resides in the fast Base64 decoder used by the JVM on x86-64 chips, according to Aikido and Rapid7, and VulnCheck and Endor Labs say exploitation depends on hardware, Java version, server processor and application, making it difficult to carry out.

Only x86-64 processors with AVX-512 VBMI instructions (a vector bit-manipulation instruction set) can trigger the flaw, including Intel Xeon from Ice Lake onward and AMD Zen 4 and newer. VulnCheck reproduced the flaw on Ice Lake hardware, while processors lacking AVX-512 VBMI and BW support use a different decoding path. Endor Labs said the flaw affects recent Intel and AMD server chips, which represent much of current cloud capacity; ARM-based servers such as AWS Graviton are not affected.

Calif demonstrated remote code execution against default installations of Keycloak, Atlassian Jira and Confluence , JFrog Artifactory, Jenkins and PingFederate. Services that require authentication before exploitation include Apache Kafka Broker, Apache Solr, Elasticsearch, Gerrit and Spinnaker. Bundled Java runtimes may also hide inside self-hosted servers such as Jira, Confluence and Jenkins, in Keycloak, Artifactory and Elasticsearch. Bundled runtimes may also hide in development environments such as IntelliJ IDEA or Android Studio.

Affected Java distributions include Amazon Corretto, Eclipse Temurin, Microsoft Build of OpenJDK, Azul Zulu, BellSoft Liberica, SAP SapMachine, Red Hat OpenJDK, Oracle OpenJDK, Oracle Java SE and Oracle GraalVM for JDK. Oracle’s advisory lists affected Java SE builds 17.0.21.0.3, 21.0.13.0.3, 25.0.5.0.3, 27.0.1.0.3 and 8u511b33-perf, plus affected GraalVM for JDK builds 17.0.21.0.3 and 21.0.13.0.3 and GraalVM Enterprise Edition 21.3.20.0.3.

Fixed builds include Amazon Corretto 17.0.21.1.2, 21.0.13.1.2, 25.0.5.1.2 and 27.0.1.1.4, and Eclipse Temurin 17.0.21.1+2, 21.0.13.1+2, 25.0.5.1+2 and 27.0.1.1+4. Oracle Java 17 builds below 17.0.21.1 and Java 21 builds below 21.0.13.1 are exposed, and Oracle Java 25 builds below 25.0.5.1 and Java 27 builds below 27.0.1.1 are exposed.

Java 8 and Java 11 are not affected, except for Oracle’s Java SE 8u511b33-perf Enterprise Performance Pack build. The OpenJDK advisory marks Java 17, 21, 25 and 27 as affected while excluding Java 8 and 11, and nearly every Java build including Eclipse Temurin and Amazon Corretto comes from OpenJDK code. OpenJDK runs most Java applications.

No attacks exploiting Java4Shell had been reported in the wild as of November 18. The flaw is not listed in CISA’s Known Exploited Vulnerabilities catalog, according to Aikido.

OpenJDK maintainers released a fix, but each Java vendor ships its patched build on its own schedule. The Nov. 2026 Oracle patch update identifies CVE-2026-114938 as a Compiler component flaw in Oracle Java SE and Oracle GraalVM products, and Oracle credits Albert Yang and Quang Luong of Calif.io with reporting the vulnerability. Major vendors including Red Hat and Azul Zulu, plus Microsoft’s OpenJDK build and Linux distributions, each issue their own fixed builds.

CISA says to review software inventories for Java Development Kits and Java runtimes, noting that bundled runtimes in third-party applications, container images and appliances may not appear as separate inventory entries. CISA advises installing relevant Java and vendor patches immediately, especially for internet-facing systems.

If patching cannot happen right away, CISA says to check and limit Base64 input at application boundaries, cap input sizes and block unauthenticated access as temporary safeguards. CISA also advises consulting Oracle’s security advisory for further patching instructions and monitoring for rogue Java runtimes, unexpected JVM crashes and suspicious Java processes. Security teams should prioritize internet-facing services that accept Base64 input from users such as login headers or file uploads.

Teams can start affected JVMs with -XX:-UseBASE64Intrinsics to disable the vulnerable fast path, or use -XX:UseAVX=2 on x86-64 only; Red Hat reportedly recommends the latter, and Base64-heavy applications may slow down under these workarounds. Neither flag replaces patching. After installing a fixed build, administrators must restart every Java service because a running process still uses the old code until it restarts. Containers must be rebuilt from a fixed base image and then redeployed because pulling a new tag does not update running containers, and bundled runtimes may hide in container base images such as eclipse-temurin:17-jre or amazoncorretto:21 and in build agents or CI runners.

Tags: CISA , cloud security , CVE , patch , zero-day

Was this helpful?
👍 Helpful 0 👎 Not helpful 0 💡 Insightful 0 😮 Surprised 0 😟 Concerned 0
Thanks for your feedback.

Related
DNI says NSA systems failed to restart after PHP patching 5 hours ago
SANS holds Infocon at Green despite outage and critical Java, NGINX flaws 9 hours ago
Security officials tell Congress outages came from maintenance, not attacks 10 hours ago
Senators press White House AI chief to fix infrastructure flaws after mass outages 10 hours ago

Join the discussion Cancel reply

Most read
VA physicians and dentists ask Congress to pause Oracle EHR rollouts Oct 31
ENISA publishes SBOM guidance tying automation to supply chain security Oct 26
Attackers exploit critical Node-RED flaw CVE-2026-58115 from single IP Nov 3
SANS ISC discloses a new ClickFix campaign targeting macOS and Windows users Oct 28
CERT-EU warns of critical PHP flaws CVE-2026-109618 and CVE-2026-109619 Oct 20

Manage Consent

To provide the best experiences, we use technologies like cookies to store and/or access device information. Consenting to these technologies will allow us to process data such as browsing behavior or unique IDs on this site. Not consenting or withdrawing consent, may adversely affect certain features and functions.

Functional

Functional

Always active

The technical storage or access is strictly necessary for the legitimate purpose of enabling the use of a specific service explicitly requested by the subscriber or user, or for the sole purpose of carrying out the transmission of a communication over an electronic communications network.

Preferences

Preferences

The technical storage or access is necessary for the legitimate purpose of storing preferences that are not requested by the subscriber or user.

Statistics

Statistics

The technical storage or access that is used exclusively for statistical purposes.
The technical storage or access that is used exclusively for anonymous statistical purposes. Without a subpoena, voluntary compliance on the part of your Internet Service Provider, or additional records from a third party, information stored or retrieved for this purpose alone cannot usually be used to identify you.

Marketing

Marketing

The technical storage or access is required to create user profiles to send advertising, or to track the user on a website or across several websites for similar marketing purposes.

Manage options

Manage services

Manage {vendor_count} vendors

Read more about these purposes

Accept
Deny
View preferences
Save preferences
View preferences

{title}

{title}

{title}

Manage consent

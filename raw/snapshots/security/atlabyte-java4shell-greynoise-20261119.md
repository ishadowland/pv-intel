<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://atlabyte.com/en/news/java4shell-greynoise-logged-150-exploitation-attempts -->
<!-- fetched_at: 2026-11-20 07:13:36 -->
<!-- sha256: f4340020d8cabae616f995606ed285cd5c4e04a42cf1d306b2b11c96c80b2b67 -->

Java4Shell: GreyNoise Logged 150 Exploitation Attempts
Impact-Site-Verification: e46376f4-a266-472e-a4df-dfb7cbcad2c8
Skip to content
ATLABYTE

Кибербезопасность Java4Shell: GreyNoise Logged 150 Exploitation Attempts

19.11.2026 · 3 min read 14961

Кибербезопасность · illustration by the publication Exploitation attempts for the Java4Shell vulnerability have begun. According to GreyNoise, more than 150 requests were recorded, and vendors are releasing patches.
The vulnerability CVE-2026-114938 (Java4Shell) affects OpenJDK starting from version 17.0.6. The bug occurs when processing Base64 data and manifests only on processors with AVX-512 VBMI support — these are newer Intel and AMD chips. ARM systems are not vulnerable.

The company Calif disclosed the issue on November 17, the same day Oracle and the OpenJDK project released patches. Calif researchers achieved unauthenticated remote code execution on Jira, Confluence, Jenkins, Keycloak and other applications in default configurations, but noted that there is no universal exploit — each program needs its own attack chain.

Exploitation Attempts

According to GreyNoise, by early November 19, more than 150 requests matching the signs of a Java4Shell attack were recorded from five IP addresses. No successful intrusions were detected on the company's sensors.

WatchTowr also sees activity: attackers are scanning the internet, sending requests with User-Agent 'java4shell-recon' and blind exploitation attempts. WatchTowr's head of threat intelligence Jake Knott expects more reliable exploits for specific products to appear in the coming days.

Cloudflare Cloudforce One noticed that scanners are beginning to conceal their tools. One IP first used an explicit User-Agent, then returned about 17 hours later with an exploit disguised as Chrome browser. Also, this IP was used for attacks using the AI framework Artex for the first time.

Previdian logged 9 exploitation attempts from six IPs on November 18 and 19, but cannot confirm compromise of targets. Cisco is aware of PoC code but has no knowledge of malicious use. The PoC from Calif only triggers memory corruption, while a full RCE exploit is available to VulnCheck customers, and researcher Kevin Breen reported developing a working variant.

Vendor Response

Cisco confirmed the vulnerability in more than a dozen products, including Catalyst Center, Secure Network Analytics, Secure Workload, Smart Software Manager On-Prem, Splunk AppDynamics On-Premises Virtual Appliance, and Intersight Virtual Appliance. No fixes yet and no workarounds. The company is investigating IOS XE and UCS Central.

Siemens reported three affected Industrial Edge Management products. Patches are in progress, it is recommended to take them offline. Elastic stated that all Elasticsearch releases from 7.17.3 onward are vulnerable: RCE requires credentials with read permissions or higher, while denial of service is possible without authentication. Logstash 8.6.2 and later are also vulnerable but only in a specific configuration and cause a crash. Elastic already deployed a hotfix for Cloud Serverless and a configuration change for Cloud Hosted.

Red Hat rated the vulnerability as Critical. Affected are RHEL 8, 9 and 10, as well as its builds of OpenJDK 17, 21 and 25. The company notes that affected systems are attackable without special configuration because the accelerated code path is selected automatically on processors with AVX-512 VBMI.

The Keycloak team warned that container images 26.8.2-1 and 26.8.2-2 contain a vulnerable OpenJDK 21. On November 19, updated images were released, including 26.8.2-3. Atlassian is working on cloud products and for Data Center recommends disabling AVX-512 until patches are available. Jenkins advises updating Java and restarting the controller.

Among Java distributors, Amazon, Microsoft and Azul have already released updates.

Editorial opinion
Our Take

We believe Java4Shell will become a serious threat: the vulnerability exists in popular server applications and allows remote code execution without authentication. Current attacks are still crude, but the rapid appearance of PoCs and active scanning indicate preparation for mass exploitation. We will track patches and recommend administrators update systems as soon as possible.

# GreyNoise # Java4Shell # Vulnerability
Share: Telegram WhatsApp X Copy link

Read also

N-able Links Mail Assure and SpamExperts Outage to Cyberattack on Server
N-able confirmed that the multi-day outage of Mail Assure and SpamExperts Hosted Cloud was caused by a cyberattack on its server.
# N-able
20.11.2026 18587

Blackpoint Cyber: New CNCMachineRMS RAT Delivered via ROMULUS ClickFix
The ROMULUS ClickFix platform is delivering the CNCMachineRMS remote access trojan to victims' PCs: it can watch the screen, record the microphone and camera, and take over the computer.
# Blackpoint Cyber # CNCMachineRMS 2 more
20.11.2026 17176

JPMorgan, Visa and Mastercard Disclose Customer Data Breaches via Third-Party Vendors
JPMorgan Chase, Visa and Mastercard revealed incidents tied to third-party vendors after the N0n extortion group claimed to have stolen customer data.
# JPMorgan # Mastercard 3 more
20.11.2026 8742

China-linked Armory Castle group attacked VMware vCenter via zero-day CVE-2026-123890 (CVSS 9.8)
China-nexus hacking group Armory Castle used a critical VMware vCenter Server vulnerability in early September 2026 to gain administrator access and steal data.
# Armory Castle # VMware 1 more
20.11.2026 17038

ATLABYTE

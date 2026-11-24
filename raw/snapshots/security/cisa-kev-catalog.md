<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.cisa.gov/known-exploited-vulnerabilities-catalog -->
<!-- fetched_at: 2026-11-25 07:12:46 -->
<!-- sha256: b545b92d42d35503d819057277b093c2c451ae27b50d4aa5068a4b7a09c4143e -->

Known Exploited Vulnerabilities Catalog | CISA

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

Known Exploited Vulnerabilities Catalog

For the benefit of the cybersecurity community and network defenders—and to help every organization better manage vulnerabilities and keep pace with threat activity—CISA maintains the authoritative source of vulnerabilities that have been exploited in the wild. Organizations should use the KEV catalog as an input to their vulnerability management prioritization framework. Learn more about how to use the KEV catalog in your organization.
Are you aware of an actively exploited vulnerability not included in the KEV Catalog?
NOMINATE A NEW KEV
The KEV catalog is also available in these formats:
CSV JSON Print View
JSON Schema (updated 09-02-2026)
License

Showing 1 to 20 of 1795 results

Drupal | Core

CVE-2026-132165

Drupal Core Remote Code Execution Vulnerability: Drupal Core contains a not failing securely vulnerability that could allow an unauthenticated attacker to take over an existing site or execute arbitrary code via the Drupal installer. Under specific conditions, the attacker can use install.php to attempt to reinstall Drupal on the site.

Related CWE:
CWE-636

Known To Be Used in Ransomware Campaigns?

Unknown

Forensic triage required per BOD 26-04:

Yes

Date Added:
2026-11-24

Due Date:
2026-11-27

Action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

Additional Notes

https://www.drupal.org/sa-core-2026-017 ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-132165

Idunno | AntiCsrf

CVE-2026-131914

Idunno AntiCsrf Deserialization of Untrusted Data Vulnerability: Idunno AntiCsrf contains a deserialization of untrusted data vulnerability that allows an unauthenticated remote attacker to execute arbitrary code via object injection. The impacted product(s) could be end-of-life (EoL) and/or end-of-service (EoS). Users are advised to discontinue use and/or transition to a supported version.

Related CWE:
CWE-502

Known To Be Used in Ransomware Campaigns?

Unknown

Forensic triage required per BOD 26-04:

Yes

Date Added:
2026-11-24

Due Date:
2026-11-27

Action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

Additional Notes

This vulnerability could affect an open-source component, third-party library, protocol, or proprietary implementation that could be used by different products. For more information, please see: https://github.com/mandiant/Vulnerability-Disclosures/blob/master/2026/MNDT-2026-0048.md ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-131914

Optimizely | Web Experimentation

CVE-2026-132224

Optimizely Web Experimentation External Control of Critical State Data Vulnerability: Optimizely Web Experimentation contains an external control of critical state data vulnerability in its account signup flow that could allow an attacker to impersonate existing customer users and modify Project JavaScript. Successful exploitation can result in attacker-controlled JavaScript being distributed through Optimizely-hosted assets and executed in browsers visiting affected customer websites.

Related CWE:
CWE-642

Known To Be Used in Ransomware Campaigns?

Unknown

Forensic triage required per BOD 26-04:

Yes

Date Added:
2026-11-24

Due Date:
2026-11-27

Action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

Additional Notes

https://pages.optimizely.com/rs/947-RKE-048/images/Security%20Incident%20Report%20-%20Optimizely%20Web%20Experimentation%20-%20Nov%2017%202026.pdf ; https://status.optimizely.com/incidents/ftw0fh9wx43z ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-132224

N-able | MailAssure

CVE-2026-134624

N-able MailAssure (SpamExperts) Server-Side Request Forgery (SSRF) Vulnerability: N-able MailAssure (SpamExperts) contains a server-side request forgery vulnerability in the LDAP synchronization connection check that allows an authenticated API user to connect to arbitrary internal hosts and ports, determine which are reachable, and send crafted data to internal services.

Related CWE:
CWE-918

Known To Be Used in Ransomware Campaigns?

Unknown

Forensic triage required per BOD 26-04:

Yes

Date Added:
2026-11-23

Due Date:
2026-11-26

Action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

Additional Notes

https://me.n-able.com/s/security-advisory/aArVy0000002mrlKAA ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-134624

Project MONAI | MONAI Label

CVE-2026-133968

Project MONAI MONAI Label Path Traversal Vulnerability: Project MONAI MONAI Label contains a path traversal vulnerability that allows an unauthenticated remote attacker to write arbitrary files outside the intended datastore directory, potentially resulting in remote code execution.

Related CWE:
CWE-24

Known To Be Used in Ransomware Campaigns?

Unknown

Forensic triage required per BOD 26-04:

Yes

Date Added:
2026-11-23

Due Date:
2026-11-26

Action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

Additional Notes

https://github.com/Project-MONAI/MONAILabel/security/advisories/GHSA-qc22-rmgc-vg94 ; https://github.com/Project-MONAI/MONAILabel/pull/1915 ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-133968

Cisco | Expressway Series

CVE-2026-76466

Cisco Expressway Series Use of Hard-coded Credentials Vulnerability: Cisco Expressway Series contains a use of hard-coded credentials vulnerability that allows an unauthenticated, remote attacker with persistent cookies and network access to execute commands as root on a clustered device via the database service.

Related CWE:
CWE-798

Known To Be Used in Ransomware Campaigns?

Unknown

Forensic triage required per BOD 26-04:

Yes

Date Added:
2026-11-20

Due Date:
2026-11-23

Action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

Additional Notes

https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-vcs-static-cred-hr7EWZ8t ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-76466

SAP | NetWeaver

CVE-2025-42884

SAP NetWeaver Improper Neutralization of Special Elements in Data Query Logic Vulnerability: SAP NetWeaver Enterprise Portal contains an improper neutralization of special elements in data query logic vulnerability that allows an unauthenticated attacker to disclose or modify server information via injected JNDI environment properties or a URL used during JNDI lookup operations.

Related CWE:
CWE-943

Known To Be Used in Ransomware Campaigns?

Unknown

Forensic triage required per BOD 26-04:

No

Date Added:
2026-11-20

Due Date:
2026-11-23

Action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

Additional Notes

https://support.sap.com/en/my-support/knowledge-base/security-notes-news/bulletin-2025.html ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2025-42884

Broadcom | VMware vCenter

CVE-2026-123890

VMWare vCenter Authentication Bypass Using an Alternate Path or Channel Vulnerability: Broadcom VMware vCenter contains an authentication bypass using an alternate path or channel vulnerability in the VMware Directory Service that allows an unauthenticated attacker with network access to vCenter to bypass authentication and gain unauthorized access to the system.

Related CWE:
CWE-288

Known To Be Used in Ransomware Campaigns?

Unknown

Forensic triage required per BOD 26-04:

Yes

Date Added:
2026-11-20

Due Date:
2026-11-23

Action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines

Additional Notes

https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39495 ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-123890

Apache | Roller

CVE-2026-129448

Apache Roller Deserialization of Untrusted Data Vulnerability: Apache Roller contains a deserialization of untrusted data vulnerability that allows an unauthenticated remote attacker to execute arbitrary code via the XML-RPC endpoint, which accepts and deserializes vendor extension types before authentication. This CVE covers the same underlying vulnerability as CVE-2026-82384 but applies to a broader range of affected versions.

Related CWE:
CWE-502

Known To Be Used in Ransomware Campaigns?

Unknown

Forensic triage required per BOD 26-04:

Yes

Date Added:
2026-11-20

Due Date:
2026-11-23

Action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

Additional Notes

https://lists.apache.org/thread/cc0jck13nb9vvcmzxzwotr6n16mx28z9 ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-129448

Apache | Axis

CVE-2026-90436

Apache Axis Unsafe Reflection Vulnerability: Apache Axis contains an unsafe reflection vulnerability that could allow an unauthenticated remote attacker to execute arbitrary code via a crafted SOAP fault message that causes Axis to load and instantiate an attacker-specified class when a suitable class is available on the application classpath. The impacted product(s) could be end-of-life (EoL) and/or end-of-service (EoS). Users are advised to discontinue use and/or transition to a supported version.

Related CWE:
CWE-470

Known To Be Used in Ransomware Campaigns?

Unknown

Forensic triage required per BOD 26-04:

Yes

Date Added:
2026-11-18

Due Date:
2026-11-21

Action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

Additional Notes

This vulnerability could affect an open-source component, third-party library, protocol, or proprietary implementation that could be used by different products. For more information, please see: ; https://lists.apache.org/thread/8slf0j9gz35z56t0glt5h0ncwlbn4bdz ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-90436

Vanderbilt University | Research Electronic Data Capture (REDCap)

CVE-2026-90817

Vanderbilt University Research Electronic Data Capture (REDCap) Code Injection Vulnerability: Vanderbilt University Research Electronic Data Capture (REDCap) contains a code injection vulnerability which could allow an unauthenticated attacker to execute arbitrary code on the server. An attacker could exploit this via crafted HTTP requests that access an unintended controller route from a public survey context and supply a crafted file-path or stream parameter during data import processing. Exploitation requires knowledge of a valid public survey hash.

Related CWEs:
CWE-73 |
CWE-94

Known To Be Used in Ransomware Campaigns?

Unknown

Forensic triage required per BOD 26-04:

Yes

Date Added:
2026-11-18

Due Date:
2026-11-21

Action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

Additional Notes

https://projectredcap.org/resources/community ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-90817

BerriAI | LiteLLM

CVE-2026-40217

BerriAI LiteLLM Unprotected Alternate Channel Vulnerability: BerriAI LiteLLM contains an unprotected alternate channel vulnerability that could allow remote attackers to execute arbitrary code via bytecode rewriting at the /guardrails/test_custom_code URI.

Related CWE:
CWE-420

Known To Be Used in Ransomware Campaigns?

Unknown

Forensic triage required per BOD 26-04:

No

Date Added:
2026-11-18

Due Date:
2026-12-02

Action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

Additional Notes

https://github.com/BerriAI/litellm/security/advisories/GHSA-wxxx-gvqv-xp7p ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-40217

Synology | DiskStation Manager (DSM)

CVE-2024-10441

Synology DiskStation Manager (DSM) Improper Encoding or Escaping of Output Vulnerability: Synology DSM contains an improper encoding or escaping of output vulnerability in the system plugin daemon in Synology BeeStation OS (BSM) that could allow a remote attacker to execute arbitrary code via unspecified vectors.

Related CWE:
CWE-116

Known To Be Used in Ransomware Campaigns?

Known

Forensic triage required per BOD 26-04:

Yes

Date Added:
2026-11-18

Due Date:
2026-11-21

Action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

Additional Notes

https://www.synology.com/zh-tw/security/advisory/Synology_SA_24_20 ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2024-10441

Perforce | Puppet Enterprise

CVE-2026-115731

Perforce Puppet Enterprise Deserialization of Untrusted Data Vulnerability: Perforce Puppet Enterprise contains a deserialization of untrusted data vulnerability in Puppet’s report-processing code that allows a client with any CA-signed agent certificate to execute arbitrary code on the Puppet Server as the service user by submitting a report containing a crafted rich-data type through a PUT request. If the certificate authority automatically signs requests without strong verification, an unauthenticated network attacker can obtain a valid certificate and exploit the vulnerability.

Related CWEs:
CWE-502 |
CWE-94

Known To Be Used in Ransomware Campaigns?

Unknown

Forensic triage required per BOD 26-04:

No

Date Added:
2026-11-17

Due Date:
2026-12-01

Action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

Additional Notes

https://portal.perforce.com/s/cve/a91Qi000003IaHpIAK/report-deserialization-code-execution ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-115731

Check Point | Multiple Products

CVE-2026-123039

Check Point Multiple Products Incorrect Permission Assignment for Critical Resource Vulnerability: Check Point Firewall, Multi-Domain Security Management Server, Scalable Platforms, Security Gateway, and Security Management Server contain an incorrect permissions assignment for critical resources vulnerability when the Gaia OS DynamicCLI daemon runs as root and listens on a world-writable local socket without authenticating connecting processes. An authenticated local user can send a command to the socket and have it executed as root.

Related CWEs:
CWE-732 |
CWE-862

Known To Be Used in Ransomware Campaigns?

Unknown

Forensic triage required per BOD 26-04:

Yes

Date Added:
2026-11-13

Due Date:
2026-11-16

Action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

Additional Notes

https://support.checkpoint.com/results/sk/sk1000362 ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-123039

UnrealIRCd | UnrealIRCd

CVE-2026-114713

UnrealIRCd Improper Neutralization of Delimiters Vulnerability: UnrealIRCd UnrealIRCd contains an improper neutralization of delimiters vulnerability that allows any user on a network with two or more linked servers to inject server-to-server commands that are executed with server authority.

Related CWE:
CWE-140

Known To Be Used in Ransomware Campaigns?

Unknown

Forensic triage required per BOD 26-04:

Yes

Date Added:
2026-11-13

Due Date:
2026-11-16

Action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

Additional Notes

https://forums.unrealircd.org/viewtopic.php?t=9487 ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-114713

Google | Chromium

CVE-2026-125350

Google Chromium Use-After-Free Vulnerability: Google Chromium contains a use-after-free vulnerability in the XML component that could allow a remote attacker to execute arbitrary code inside the sandbox via a specially crafted webpage. This vulnerability could affect multiple web browsers that utilize Chromium, including, but not limited to, Google Chrome, Microsoft Edge, and Opera.

Related CWE:
CWE-416

Known To Be Used in Ransomware Campaigns?

Unknown

Forensic triage required per BOD 26-04:

No

Date Added:
2026-11-10

Due Date:
2026-11-24

Action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

Additional Notes

https://chromereleases.googleblog.com/2026/11/stable-channel-update-for-desktop_018223192.html ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-125350

Barracuda Networks | Barracuda Email Security Gateway (ESG)

CVE-2026-116606

Barracuda Networks Email Security Gateway (ESG) Authentication Bypass Using an Alternate Path or Channel Vulnerability: Barracuda Networks Email Security Gateway (ESG) contains an authentication bypass using an alternate path or channel that could allow an unauthenticated remote attacker to invoke a configuration-import function and restore a crafted, compatible backup archive, resulting in unauthorized modification of the appliance’s global configuration. This vulnerability can be chained with CVE-2026-111560.

Related CWE:
CWE-288

Known To Be Used in Ransomware Campaigns?

Unknown

Forensic triage required per BOD 26-04:

Yes

Date Added:
2026-11-10

Due Date:
2026-11-13

Action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

Additional Notes

https://trust.barracuda.com/security/pre-authentication-authorization-bypass-command-injection ; https://github.com/mandiant/Vulnerability-Disclosures/blob/master/2026/MNDT-2026-0042.md ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-116606

Barracuda Networks | Multiple Products

CVE-2026-111560

Barracuda Networks Multiple Products OS Command Injection Vulnerability: Barracuda Networks Email Security Gateway (ESG), Load Balancer, Application Delivery Controller (ADC), Message Archiver (BMA), WAF Control Center (WCC), Web Application Firewall (WAF), and Web Security Gateway (WSG) contain an OS command injection vulnerability. This vulnerability could allow an authenticated administrator to inject OS commands that execute with root privileges when the crafted timezone value is subsequently processed. This vulnerability can be chained with CVE-2026-116606

Related CWE:
CWE-78

Known To Be Used in Ransomware Campaigns?

Unknown

Forensic triage required per BOD 26-04:

Yes

Date Added:
2026-11-10

Due Date:
2026-11-13

Action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

Additional Notes

https://trust.barracuda.com/security/pre-authentication-authorization-bypass-command-injection ; https://github.com/mandiant/Vulnerability-Disclosures/blob/master/2026/MNDT-2026-0041.md ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-111560

Cisco | BroadWorks

CVE-2026-20320

Cisco BroadWorks Improper Restriction of XML External Entity Reference Vulnerability: Cisco BroadWorks contains an improper restriction of XML external entity reference vulnerability that could allow an unauthenticated, remote attacker to read sensitive configuration information on an affected system.

Related CWE:
CWE-611

Known To Be Used in Ransomware Campaigns?

Unknown

Forensic triage required per BOD 26-04:

No

Date Added:
2026-11-10

Due Date:
2026-11-24

Action: Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.

Additional Notes

https://sec.cloudapps.cisco.com/security/center/content/CiscoSecurityAdvisory/cisco-sa-bworks-xxe-uwUd7CEt ; BOD 26-04: https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk ; Forensics Triage Requirements: https://www.cisa.gov/news-events/directives/bod-26-04-implementation-guidance-prioritizing-security-updates-based-risk ; https://nvd.nist.gov/vuln/detail/CVE-2026-20320

Subscribe to the KEV Catalog Updates

Stay up to date on the latest known exploited vulnerabilities.

Subscribe Now

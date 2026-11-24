<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-129448 -->
<!-- fetched_at: 2026-11-24 07:22:28 -->
<!-- sha256: 5470a15dc45b781bd0e8230918756ffa5db737af750c47c0e993e589e03a61eb -->

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

Showing 1 to 1 of 1 results

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

Subscribe to the KEV Catalog Updates

Stay up to date on the latest known exploited vulnerabilities.

Subscribe Now

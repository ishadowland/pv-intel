<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://aviatrix.ai/threat-research-center/icsa-26-321-05-siemens-mendix-studio-pro-mcp-csrf-cve-2026-112136/ -->
<!-- fetched_at: 2026-11-18 07:14:08 -->
<!-- sha256: 0300ad92d51ec767959149213476c083e1e8696e66df1c76728831be3146c2ce -->

Siemens Mendix Studio Pro MCP Server Vulnerabilities – ICSA-26-321-05 CVE-2026-112136 Aviatrix
Platform
Products
Solutions
Partners
Resources
Why Aviatrix
Threat Research Center
Under Active Attack

Siemens Mendix Studio Pro MCP Server Flaws: What ICS and OT Security Teams Must Do Now
Two newly disclosed vulnerabilities in Mendix Studio Pro expose AI-augmented development pipelines in critical manufacturing and energy environments to remote takeover and silent browser-based attacks. Here is what your team needs to know.
Published: November 17, 2026 Share this on:

Executive Summary
In November 2026, CISA republished a Siemens ProductCERT advisory (SSA-710379, ICSA-26-321-05) disclosing two high-severity vulnerabilities in Siemens Mendix Studio Pro 11, a low-code application development platform widely deployed in critical manufacturing and energy sectors. CVE-2026-112136 (CVSS 8.8) exposes the platform's Model Context Protocol (MCP) Server by binding its HTTP listener to an unrestricted IP address rather than localhost, allowing any network-accessible attacker to interact with the MCP Server remotely. CVE-2026-112137 (CVSS 5.4) enables Cross-Site Request Forgery attacks by failing to validate Content-Type and Origin headers, letting a malicious web page silently execute unauthorized actions on the local MCP Server. Siemens has released patched versions V11.16.0 and V11.12.7, with mitigations including host-based firewall rules on port 7782 and browser Private Network Access controls.

These vulnerabilities arrive as AI-augmented low-code development platforms accelerate their integration of MCP-style agent interfaces into enterprise OT and IT pipelines. The combination of an exposed local service and CSRF exploitability mirrors a growing class of developer-toolchain attacks where trusted local processes become pivot points for supply-chain or insider-adjacent compromise, raising urgency for organizations using Mendix in regulated or critical-infrastructure environments.

Why This Matters Now
MCP Server interfaces are proliferating rapidly across AI-assisted development tools, yet security hardening lags adoption. With Mendix embedded in critical manufacturing and energy workflows, an unpatched CVE-2026-112136 instance reachable over a flat enterprise network hands attackers direct tool-execution capability against OT-adjacent systems—precisely the lateral movement path that zero-trust segmentation and east-west traffic controls are designed to close.

Attack Path Analysis

An attacker targeting Siemens Mendix Studio Pro exploits CVE-2026-112136 to remotely interact with the MCP Server exposed on port 7782 beyond the loopback interface, gaining unauthorized access to development tooling and local services. Using CVE-2026-112137, a malicious web page performs CSRF attacks against the local MCP Server, tricking authenticated developer browsers into executing unauthorized tool actions, escalating attacker control over the low-code development environment and potentially pivoting to connected ICS/OT systems or cloud infrastructure accessed via developer credentials.
Kill Chain Progression
This analysis maps confirmed threat intelligence to the full cloud kill chain to show where defensive gaps would emerge as an attack progresses.

Initial Compromise High

Privilege Escalation Medium inferred

Lateral Movement Medium inferred

Command & Control High

Exfiltration Medium inferred

Impact Low inferred

Initial Compromise
Description
The MCP Server in Mendix Studio Pro binds to an unrestricted IP address (CVE-2026-112136, CWE-1327), exposing port 7782 to network-accessible systems rather than restricting it to loopback. An attacker with network access — including an insider, compromised network peer, or attacker on the same subnet — sends crafted HTTP requests directly to the MCP Server without authentication, gaining initial unauthorized interaction with the development environment.

Confidence:

High

Related CVEs

Included CVEs with severity scores, affected products, exploit status, and reference links.

CVE-2026-112136
CVSS 8.8
Siemens Mendix Studio Pro MCP Server does not properly restrict its HTTP listener to the loopback interface, leaving it potentially exposed to remote systems on port 7782, allowing an attacker with network access to interact with the MCP Server remotely and potentially achieve unauthorized data access or system compromise.
Affected Products:
Siemens Mendix Studio Pro 11 – >=11.15.0, <11.16.0
Siemens Mendix Studio Pro 11.12 – >=11.12.6, <11.12.7

Exploit Status:
no public exploit
References:
https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-05 https://www.siemens.com/cert/advisories https://nvd.nist.gov/vuln/detail/CVE-2026-112136

CVE-2026-112137
CVSS 5.4
Siemens Mendix Studio Pro MCP Server does not properly validate Content-Type and Origin headers on incoming HTTP requests, making it vulnerable to Cross-Site Request Forgery (CSRF), allowing a malicious web page to trick a user's browser into sending unauthorized requests and executing unintended actions on the local MCP Server.
Affected Products:
Siemens Mendix Studio Pro 11 – >=11.15.0, <11.16.0
Siemens Mendix Studio Pro 11.12 – >=11.12.6, <11.12.7

Exploit Status:
no public exploit
References:
https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-05 https://www.siemens.com/cert/advisories https://nvd.nist.gov/vuln/detail/CVE-2026-112137

MITRE ATT&CK® Techniques

Initial Access
T1190
Exploit Public-Facing Application

Execution
T1059
Command and Scripting Interpreter

Execution
T1203
Exploitation for Client Execution

Collection
T1557
Adversary-in-the-Middle

Command and Control
T1071.001
Application Layer Protocol: Web Protocols

Impact
T1565
Data Manipulation

Defense Evasion
T1600
Weaken Encryption

Lateral Movement
T1434
Internal Spearphishing

Potential Compliance Exposure

Mapping incident impact across multiple compliance frameworks.

NIST SP 800-53 Rev. 5 – Boundary Protection
Control ID: SC-7
CVE-2026-112136 exposes the MCP Server HTTP listener beyond the loopback interface, violating the requirement to monitor and control communications at external boundaries. Failure to restrict port 7782 to localhost allows unauthenticated remote access, directly contradicting boundary protection mandates for critical manufacturing and energy sector deployments.

NIS2 Directive – Network Security and Access Control
Control ID: Article 21(2)(e)
Both vulnerabilities affect operators of essential services in critical manufacturing and energy sectors under NIS2 scope. The absence of proper interface binding restrictions and CSRF header validation represents a failure in securing network access to operational technology platforms, exposing organizations to regulatory enforcement under NIS2's mandatory risk management and technical security measures.

DORA (Digital Operational Resilience Act) – ICT Security Controls — Network Integrity
Control ID: Article 9(4)(d)
DORA requires financial entities and their ICT third-party providers to maintain network integrity controls. The unpatched MCP Server in Mendix Studio Pro — a development platform used in enterprise and potentially financial application development — exposes supply chain risk. The CSRF vulnerability (CVE-2026-112137) could allow unauthorized execution of server actions, undermining digital operational resilience obligations.

CISA Zero Trust Maturity Model 2.0 – Network Segmentation and Least-Privilege Access
Control ID: Network Pillar — Micro-Segmentation
CVE-2026-112136 illustrates a failure of micro-segmentation principles by allowing the MCP Server to bind to all network interfaces rather than restricting to loopback. Zero Trust architecture requires that no service be implicitly trusted based on network location. The reliance on external firewall rules as a compensating control does not satisfy Zero Trust's requirement for inherent least-privilege network access at the application layer.

IEC 62443 (ISA/IEC 62443-3-3) – Network Segmentation — Communication Integrity
Control ID: SR 5.1
As an ICS/OT advisory affecting critical manufacturing and energy sectors, the failure to restrict MCP Server network interface binding directly violates IEC 62443's security requirement for network segmentation. The standard mandates that ICS components limit communications to authorized zones; binding to unrestricted IP addresses expands the attack surface well beyond intended operational boundaries.

PCI DSS 4.0 – Vulnerability Management — Patching and Secure Configuration
Control ID: Requirement 6.3.3
CVE-2026-112136 and CVE-2026-112137 are known, vendor-confirmed vulnerabilities with available patches. PCI DSS 4.0 requires that all system components are protected from known vulnerabilities by installing applicable security patches and updates. Organizations using Mendix Studio Pro in environments touching cardholder data systems must apply the vendor-released fixes (V11.16.0 / V11.12.7) promptly to remain compliant.

Sector Implications

Industry-specific impact of the vulnerabilities, including operational, regulatory, and cloud security risks.
Industrial Automation
Siemens Mendix Studio Pro ICS/OT vulnerabilities expose MCP Server to remote CSRF and unrestricted IP binding attacks, risking unauthorized tool execution and lateral movement across critical manufacturing automation environments.

Oil/Energy/Solar/Greentech
CISA-designated critical infrastructure energy sectors face high-severity CVSS 8.8 exploitation risk via CVE-2026-112136, enabling unauthenticated remote MCP Server access and potential operational technology system compromise.

Computer Software/Engineering
Mendix low-code development platform vulnerabilities directly impact software engineering teams using Studio Pro, exposing development environments to CSRF-driven unauthorized requests and unintended code execution actions.

Information Technology/IT
IT organizations deploying Mendix Studio Pro face east-west lateral movement risk and data exfiltration exposure, requiring Zero Trust segmentation and egress policy enforcement aligned with NIST.800-53.SC-7 and ZTMM.Network compliance controls.

Sources

Siemens Mendix Studio Pro https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-05
Verified

Siemens ProductCERT SSA-710379: Mendix Studio Pro MCP Server Vulnerabilities https://www.siemens.com/cert/advisories
Verified

Siemens Industrial Security Operational Guidelines https://www.siemens.com/cert/operational-guidelines-industrial-security
Verified

CISA ICS Security Recommended Practices https://www.cisa.gov/ics
Verified

NVD CVE Detail: CVE-2026-112136 https://nvd.nist.gov/vuln/detail/CVE-2026-112136

NVD CVE Detail: CVE-2026-112137 https://nvd.nist.gov/vuln/detail/CVE-2026-112137

Frequently Asked Questions
What compliance gaps do CVE-2026-112136 and CVE-2026-112137 in Mendix Studio Pro expose? The vulnerabilities highlight failures in network segmentation (NIST 800-53 SC-7), access control (AC-6), and boundary protection required by ICS security frameworks. Organizations relying on flat enterprise networks or insufficient host-based firewall policies will find these controls are inadequate without zero-trust segmentation enforcing least-privilege east-west traffic policies.

Could east-west traffic controls or zero-trust segmentation have mitigated these Mendix MCP Server vulnerabilities?
Which versions of Siemens Mendix Studio Pro are affected and what is the recommended fix?

Cloud Native Security Fabric Mitigations and Controls CNSF
Based on the attack progression modeled above, these are the defensive controls that would constrain each stage.

Aviatrix Zero Trust CNSF is relevant here because the attacker's ability to reach an unauthenticated MCP Server on port 7782 and subsequently pivot to cloud or ICS environments depends entirely on unrestricted network reachability across developer workstation segments. By enforcing segmentation and identity-aware access policies at the network fabric level, Aviatrix would likely reduce the attacker's reachability to that exposed service and constrain the blast radius of any subsequent lateral or exfiltration activity.
Initial Compromise
Control: Cloud Native Security Fabric (CNSF)
Mitigation: Broad network reachability to the exposed MCP Server port would likely be constrained by fabric-level segmentation policies that limit which sources can initiate connections to developer workstation segments, reducing the attacker's ability to reach port 7782 from arbitrary network peers.

Privilege Escalation
Control: Zero Trust Segmentation
Mitigation: The scope of privilege accessible from a compromised MCP interaction would likely be constrained by Zero Trust segmentation policies that limit which downstream services and credential stores the developer workstation segment can reach, reducing how far inherited developer privileges could carry an attacker.

Lateral Movement
Control: East-West Traffic Security
Mitigation: East-west traffic enforcement would likely constrain the attacker's ability to move laterally from the developer workstation to cloud workloads or ICS/OT segments, as fabric-level policies could limit which internal destinations that workstation segment is permitted to reach, reducing the accessible pivot surface.

Command & Control
Control: Multicloud Visibility & Control
Mitigation: Multicloud visibility and control capabilities would likely reduce the attacker's ability to extend command-and-control influence from the compromised developer context into cloud-managed workloads or cross-cloud services, constraining how far browser-proxied MCP commands could propagate beyond the local development environment.

Exfiltration
Control: Egress Security & Policy Enforcement
Mitigation: Egress security policy enforcement would likely reduce the attacker's ability to freely exfiltrate development artifacts and embedded credentials over outbound HTTP channels, constraining which external destinations the developer workstation segment can reach and limiting unmonitored outbound data paths.

Impact (Mitigations)
Because earlier segmentation and egress controls would likely have constrained the attacker's reachability and lateral movement, the residual impact scope would likely be reduced to assets directly accessible within the developer workstation segment rather than extending across OT or cloud environments, limiting the blast radius of any application model manipulation or data destruction.

Impact at a Glance

Affected Business Functions
Industrial Application Development and Deployment (Mendix Low-Code Platform)
ICS/OT Engineering Workstation Operations
Critical Manufacturing Process Control Systems
Energy Sector Operational Technology (OT) Workflows

Operational Disruption
Estimated downtime: 2 days

Financial Impact
Estimated loss: N/A

Data Exposure
Potential unauthorized access to MCP Server-managed data and tool execution contexts within Mendix Studio Pro development environments. Exploitation of CVE-2026-112136 could expose sensitive application development data, internal API endpoints, and ICS/OT configuration artifacts accessible via the MCP Server on port 7782. CVE-2026-112137 CSRF exploitation could lead to unauthorized tool execution and limited integrity and availability impact on locally running MCP Server sessions. Affected sectors include Critical Manufacturing and Energy, where exposure of development pipeline data or OT-integrated application logic could have downstream operational consequences.

Recommended Actions

Key Takeaways & Next Steps

• Apply Zero Trust Segmentation (CNSF) to restrict developer workstations and MCP Server port 7782 to explicitly authorized loopback or internal network zones only, enforcing identity-based microsegmentation policies that prevent any unauthenticated network peer from reaching local development service ports.

• Deploy East-West Traffic Security controls to monitor and enforce workload-to-workload communication policies within developer and ICS/OT network segments, detecting anomalous lateral movement attempts that originate from compromised developer endpoints toward internal services or cloud control planes.

• Enable Egress Security and Policy Enforcement with FQDN filtering to prevent MCP Server-triggered processes or CSRF-initiated browser fetch requests from reaching unauthorized external destinations, blocking potential data exfiltration channels opened through tool execution abuse.

• Leverage Multicloud Visibility and Control capabilities to establish traffic observability baselines for developer environment outbound connections, enabling detection of anomalous interactions such as unexpected API calls or repeated malformed requests that may indicate active MCP Server exploitation or CSRF-driven command execution.

• Implement Cloud Firewall (ACF) egress controls and Inline IPS (Suricata) signature-based detection tuned to CVE-2026-112136 and CVE-2026-112137 exploit patterns, ensuring that known malicious payloads targeting the MCP HTTP listener or CSRF request patterns are identified and blocked at the network enforcement layer before reaching vulnerable endpoints.

Secure the Paths Between Cloud Workloads
A cloud-native security fabric that enforces Zero Trust across workload communication—reducing attack paths, compliance risk, and operational complexity.

Stop Advanced Threats Free Containment Assessment Under Active Attack?

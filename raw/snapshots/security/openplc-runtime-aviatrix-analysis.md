<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://aviatrix.ai/threat-research-center/icsa-26-323-01-openplc-runtime-race-condition-cve-2026-126088 -->
<!-- fetched_at: 2026-11-24 07:12:51 -->
<!-- sha256: 56553374e7162808edadbe4410e30146387498a09f58657296dabf2b8a2847b3 -->

CVE-2026-126088: OpenPLC Runtime Race Condition Enables Rogue Admin Accounts | ICSA-26-323-01 Aviatrix
Platform
Products
Solutions
Partners
Resources
Why Aviatrix
Threat Research Center
Under Active Attack

Race to Admin: How CVE-2026-126088 Lets Attackers Create Rogue Accounts in OpenPLC Runtime
A timing flaw in Autonomy Logic's widely deployed ICS runtime hands unauthenticated attackers full administrative control—here's what critical infrastructure operators must do now.
Published: November 19, 2026 Share this on:

Executive Summary
In November 2026, CISA published ICS Advisory ICSA-26-323-01 disclosing a critical race condition vulnerability (CVE-2026-126088, CVSS 4.0: 9.2) in Autonomy Logic OpenPLC Runtime versions 4.2.4 and earlier. The flaw, rooted in CWE-362 concurrent execution with improper synchronization, allows an unauthenticated remote attacker to send parallel HTTP requests that each pass an existence check before any user record is committed—resulting in multiple rogue admin accounts being created without credentials. Affected deployments span critical infrastructure sectors including energy, manufacturing, transportation, and water systems worldwide. The vendor has released version 4.3.0 as the remediation.

OpenPLC is widely deployed as an open-source programmable logic controller runtime in operational technology environments, making unauthenticated admin account creation particularly dangerous. This vulnerability class is resurging across ICS platforms as attackers pivot from IT networks to OT systems, and regulatory scrutiny of control system security under frameworks like NERC CIP and ICS-CERT guidance continues to intensify.

Why This Matters Now
Race condition vulnerabilities enabling unauthenticated privilege escalation in ICS runtimes are increasingly targeted by nation-state and ransomware actors pivoting to operational technology. With OpenPLC Runtime deployed across global critical infrastructure—energy grids, water systems, and manufacturing—exploitation of CVE-2026-126088 could allow attackers to seize full administrative control of industrial controllers without any credentials, risking physical process disruption and safety incidents. Organizations must patch to 4.3.0 or isolate affected systems immediately.

Attack Path Analysis

An attacker targeting Autonomy Logic OpenPLC Runtime (CVE-2026-126088) exploits a race condition in the user registration endpoint by sending multiple concurrent unauthenticated HTTP requests, causing the existence check to pass simultaneously for each request and resulting in the creation of several unauthorized admin accounts. With admin-level access established, the attacker leverages these accounts to escalate privileges, pivot laterally across OT network segments, establish persistent command-and-control channels, exfiltrate sensitive operational configuration data, and ultimately manipulate or disrupt PLC logic in critical infrastructure environments such as energy, water, or transportation systems.
Kill Chain Progression
This analysis maps confirmed threat intelligence to the full cloud kill chain to show where defensive gaps would emerge as an attack progresses.

Initial Compromise High

Privilege Escalation High

Lateral Movement Medium inferred

Command & Control Medium inferred

Exfiltration Medium inferred

Impact Medium inferred

Initial Compromise
Description
The attacker identifies an internet-exposed or network-accessible OpenPLC Runtime instance running version 4.2.4 or earlier. By sending a burst of concurrent unauthenticated POST requests to the user registration endpoint, the race condition (CWE-362) allows multiple requests to pass the existence check before any user is committed to the database, resulting in the creation of several unauthorized admin-level accounts without any prior credentials.

Confidence:

High

Related CVEs

Included CVEs with severity scores, affected products, exploit status, and reference links.

CVE-2026-126088
CVSS 8.1
A race condition in Autonomy Logic OpenPLC Runtime versions 4.2.4 and prior allows multiple concurrent unauthenticated requests to bypass the user existence check before any user record is committed, resulting in the creation of several unauthorized admin accounts.
Affected Products:
Autonomy Logic OpenPLC Runtime – <= 4.2.4

Exploit Status:
no public exploit
References:
https://www.cisa.gov/news-events/ics-advisories/icsa-26-323-01 https://nvd.nist.gov/vuln/detail/CVE-2026-126088 https://cwe.mitre.org/data/definitions/362.html

MITRE ATT&CK® Techniques

Initial Access
T1190
Exploit Public-Facing Application

Privilege Escalation
T1548
Abuse Elevation Control Mechanism

Persistence
T1136
Create Account

Persistence
T1136.001
Create Account: Local Account

Defense Evasion
T1078
Valid Accounts

Impair Process Control
T0821
Modify Controller Tasking

Impact
T0831
Manipulation of Control

Impact
T0813
Denial of Control

Potential Compliance Exposure

Mapping incident impact across multiple compliance frameworks.

NIST SP 800-53 Rev 5 – Account Management
Control ID: AC-2
The race condition vulnerability allows multiple unauthenticated admin accounts to be created without authorization, directly violating account management requirements that mandate strict controls over account provisioning, privilege assignment, and prevention of unauthorized account creation in ICS/OT environments.

CISA Zero Trust Maturity Model 2.0 – Identity Governance and Privileged Access Control
Control ID: Identity Pillar – Identity Governance
Exploitation of this vulnerability circumvents identity governance by enabling unauthenticated actors to self-provision administrative accounts. Zero Trust principles require continuous verification of identity and enforcement of least privilege, both of which are defeated by this race condition flaw in a critical infrastructure OT system.

NIS2 Directive – Access Control and Authentication for Critical Systems
Control ID: Article 21(2)(i)
NIS2 mandates that operators of essential services implement appropriate technical measures to manage cybersecurity risks. The ability for unauthenticated users to gain administrative access to OpenPLC Runtime — deployed across critical manufacturing, energy, transportation, and water sectors — represents a direct failure to meet access control obligations for essential infrastructure systems.

IEC 62443 (ISA/IEC 62443-3-3) – Human User Identification and Authentication
Control ID: SR 1.1
IEC 62443 requires that ICS/OT systems enforce identification and authentication of all human users before granting access. The race condition vulnerability bypasses this requirement entirely by allowing concurrent unauthenticated requests to create privileged admin accounts, undermining the security level (SL) baseline for industrial control system components.

DORA (EU 2022/2554) – ICT Security — Access Rights Management
Control ID: Article 9(4)(c)
DORA requires financial entities to implement strong mechanisms controlling access rights to critical ICT systems. While primarily financial-sector focused, organizations in regulated industries using OT systems like OpenPLC Runtime that are internet-connected face exposure under DORA's access rights management requirements when unauthorized privilege escalation is possible through unpatched vulnerabilities.

PCI DSS 4.0 – Access Control Systems and Processes
Control ID: Requirement 7.2
PCI DSS 4.0 requires that access to system components is restricted to only those individuals whose job requires such access and that access control systems are implemented to enforce those restrictions. A vulnerability allowing unauthenticated creation of admin accounts directly violates this requirement for any cardholder data environment utilizing OpenPLC Runtime or connected OT network segments.

Sector Implications

Industry-specific impact of the vulnerabilities, including operational, regulatory, and cloud security risks.
Oil/Energy/Solar/Greentech
OpenPLC Runtime race condition vulnerability enabling unauthorized admin account creation poses critical ICS/OT risk to energy grid control systems, threatening lateral movement and operational integrity across power generation and distribution assets.

Utilities
Water, wastewater, and utility ICS environments running OpenPLC Runtime <=4.2.4 face unauthenticated admin escalation via CVE-2026-126088, exposing SCADA systems to privilege abuse, exfiltration, and zero-trust segmentation bypass.

Transportation
Transportation systems ICS deployments using OpenPLC Runtime are exposed to race condition exploitation allowing unauthorized admin accounts, risking undetected lateral movement across critical operational technology and safety control networks.

Industrial Automation
Industrial automation environments globally face CVSS 9.2 critical exposure from OpenPLC Runtime race condition flaw, enabling unauthenticated privilege escalation with high confidentiality, integrity, and availability impact across manufacturing control systems.

Sources

Autonomy Logic OpenPLC Runtime https://www.cisa.gov/news-events/ics-advisories/icsa-26-323-01
Verified

NVD CVE Detail: CVE-2026-126088 https://nvd.nist.gov/vuln/detail/CVE-2026-126088
Verified

CWE-362: Concurrent Execution using Shared Resource with Improper Synchronization (Race Condition) https://cwe.mitre.org/data/definitions/362.html
Verified

CISA ICS Security Recommended Practices https://www.cisa.gov/ics
Verified

Improving Industrial Control Systems Cybersecurity with Defense-in-Depth Strategies https://www.cisa.gov/sites/default/files/recommended_practices/NCCIC_ICS-CERT_Defense_in_Depth_2016_S508C.pdf
Verified

Frequently Asked Questions
What compliance gaps does CVE-2026-126088 in OpenPLC Runtime expose for critical infrastructure operators? The vulnerability exposes gaps in access control and account management requirements under NERC CIP (CIP-007), NIST SP 800-82, and IEC 62443. Organizations lacking network segmentation between IT and OT zones and without strict ingress controls on ICS management interfaces are most at risk.

Could exploitation of this race condition have been prevented without patching?
Which sectors are most exposed to the OpenPLC Runtime race condition vulnerability?

Cloud Native Security Fabric Mitigations and Controls CNSF
Based on the attack progression modeled above, these are the defensive controls that would constrain each stage.

Aviatrix Zero Trust CNSF is directly relevant here because the attacker relied on flat, permissive network access to reach an exposed OpenPLC Runtime instance and then move freely across OT segments. By enforcing identity-aware segmentation and controlled egress boundaries, CNSF would likely reduce the attacker's ability to reach the target, pivot laterally, and exfiltrate operational data.
Initial Compromise
Control: Cloud Native Security Fabric (CNSF)
Mitigation: Network-level reachability to the OpenPLC Runtime endpoint would likely be constrained, reducing the attacker's ability to deliver the concurrent unauthenticated request burst needed to trigger the race condition and create unauthorized admin accounts.

Privilege Escalation
Control: Zero Trust Segmentation
Mitigation: The admin account's ability to reach adjacent systems or invoke outbound OS-level communication paths would likely be constrained, reducing the scope of privilege abuse beyond the immediate OpenPLC application boundary.

Lateral Movement
Control: East-West Traffic Security
Mitigation: East-west traffic from the compromised OpenPLC host toward HMI systems, engineering workstations, or adjacent controllers would likely be constrained, reducing the attacker's ability to pivot freely across OT segments using harvested credentials or implicit trust relationships.

Command & Control
Control: Multicloud Visibility & Control
Mitigation: Outbound command-and-control communication from the OT host to external attacker-controlled infrastructure would likely be constrained, and anomalous traffic patterns from the PLC environment may become visible for policy-driven response before persistent channels are fully established.

Exfiltration
Control: Egress Security & Policy Enforcement
Mitigation: Uncontrolled outbound data transfers from the OT environment to unknown external destinations would likely be constrained, reducing the attacker's ability to successfully move bulk operational configuration data outside the network perimeter.

Impact (Mitigations)
If prior CNSF controls had constrained reachability, lateral movement, and exfiltration, the attacker's ability to maintain persistent admin access long enough to stage and deploy malicious PLC logic would likely be reduced, narrowing the blast radius to fewer controlled assets rather than a broad cross-sector disruption.

Impact at a Glance

Affected Business Functions
Industrial Control System (ICS) Runtime Administration
Operational Technology (OT) Process Control
Critical Infrastructure Supervisory Operations
Remote Access and Authentication Management

Operational Disruption
Estimated downtime: 3 days

Financial Impact
Estimated loss: N/A

Data Exposure
Successful exploitation could result in the creation of multiple unauthorized administrator accounts within OpenPLC Runtime environments deployed across Critical Manufacturing, Energy, Transportation Systems, and Water and Wastewater sectors. This grants attackers full administrative control over PLC logic, sensor inputs, and actuator outputs, potentially exposing operational process configurations, control ladder logic programs, sensor telemetry, and system credentials. No confirmed data exfiltration or financial loss has been reported; however, the risk of unauthorized process manipulation in critical infrastructure environments carries significant latent impact.

Recommended Actions

Key Takeaways & Next Steps

• Apply Zero Trust Segmentation (CNSF) to isolate OpenPLC Runtime and all OT/ICS assets into dedicated microsegmented network zones, enforcing identity-based least-privilege policies that prevent unauthenticated or newly created accounts from reaching adjacent OT systems even if the race condition is exploited.

• Deploy East-West Traffic Security controls to monitor and restrict workload-to-workload communication between the OpenPLC Runtime host and other ICS components such as HMIs, historians, and engineering workstations, limiting lateral movement opportunities following an initial compromise.

• Enforce Egress Security and Policy Enforcement via FQDN-based outbound filtering on all OT network segments to block unauthorized outbound connections from PLC runtime hosts to external attacker-controlled destinations, directly constraining exfiltration and C2 beacon establishment.

• Enable Multicloud Visibility and Control through centralized traffic observability and anomaly detection on OT network flows to identify the characteristic burst of concurrent registration requests indicative of race condition exploitation, triggering automated alerting and incident response workflows.

• Implement Cloud Firewall (ACF) and Inline IPS (Suricata) capabilities at the network perimeter and OT zone boundaries to detect and block exploit traffic patterns associated with CVE-2026-126088, including repeated malformed or concurrent registration requests, while ensuring all remote access to OpenPLC Runtime is routed exclusively through authenticated VPN or zero-trust network access gateways as recommended by CISA.

Secure the Paths Between Cloud Workloads
A cloud-native security fabric that enforces Zero Trust across workload communication—reducing attack paths, compliance risk, and operational complexity.

Stop Advanced Threats Free Containment Assessment Under Active Attack?

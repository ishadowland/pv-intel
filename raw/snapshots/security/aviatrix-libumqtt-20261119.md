<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://aviatrix.ai/threat-research-center/icsa-26-323-03-libumqtt-cve-2026-125132-integer-underflow/ -->
<!-- fetched_at: 2026-11-20 07:12:15 -->
<!-- sha256: e7dbc39b8e444fb95c0433bfe49f73bb878bdd31ac49ddbf7f48f7140c52251c -->

CVE-2026-125132: libumqtt Integer Underflow Vulnerability – CISA ICS Advisory ICSA-26-323-03 Aviatrix
Platform
Products
Solutions
Partners
Resources
Why Aviatrix
Threat Research Center
Under Active Attack

Unpatched and Dangerous: CVE-2026-125132 Integer Underflow in libumqtt Threatens Global Critical Infrastructure
CISA's ICSA-26-323-03 advisory exposes a remotely exploitable memory corruption flaw in the libumqtt MQTT library with no fix in sight—leaving ICS, OT, and IoT assets in energy, manufacturing, and transportation sectors at critical risk.
Published: November 19, 2026 Share this on:

Executive Summary
In November 2026, CISA issued ICS Advisory ICSA-26-323-03 disclosing a critical integer underflow vulnerability (CVE-2026-125132, CVSS v4.0: 8.8 HIGH) in libumqtt, an open-source MQTT client library maintained on GitHub. All versions up to and including 1.1.1 are affected. A remote, unauthenticated attacker can exploit this memory corruption flaw over the network with no user interaction required, potentially triggering denial of service, arbitrary memory corruption, or sensitive information disclosure. The vulnerability affects critical infrastructure sectors including Energy, Critical Manufacturing, Transportation Systems, Information Technology, and Water and Wastewater globally. No patch is currently available, as the repository maintainers did not respond to CISA coordination requests.

MQTT is a foundational protocol for IoT and industrial control systems, making memory corruption vulnerabilities in its client libraries especially dangerous. The lack of vendor response and absence of an available patch leave operators with no straightforward remediation path, forcing reliance on network-level controls and segmentation as compensating measures while exploitation risk remains unresolved.

Why This Matters Now
MQTT libraries like libumqtt are deeply embedded across ICS, OT, and IoT deployments worldwide. With no patch available and the maintainer unresponsive, CVE-2026-125132 represents an unmitigated remote attack surface in critical infrastructure. As threat actors increasingly target ICS protocols, the urgency for network segmentation, egress controls, and zero-trust enforcement around OT assets has never been higher.

Attack Path Analysis

An attacker exploits CVE-2026-125132, an integer underflow vulnerability in libumqtt (versions <=1.1.1), by sending a specially crafted MQTT packet over the network to a remotely accessible IoT or ICS device running the affected library, triggering memory corruption and enabling code execution or denial of service. With no available patch and no vendor response, affected devices in critical infrastructure sectors remain persistently vulnerable, allowing an attacker to escalate privileges via corrupted memory, move laterally across segmented OT/IT networks, establish command and control, and ultimately exfiltrate sensitive operational data or disrupt system availability.
Kill Chain Progression
This analysis maps confirmed threat intelligence to the full cloud kill chain to show where defensive gaps would emerge as an attack progresses.

Initial Compromise High

Privilege Escalation Medium inferred

Lateral Movement Medium inferred

Command & Control Medium inferred

Exfiltration Medium inferred

Impact High

Initial Compromise
Description
An unauthenticated remote attacker sends a malformed MQTT protocol message to a device running libumqtt <=1.1.1. The integer underflow (CWE-191) in the library's packet parsing logic causes a wrap-around, corrupting memory and potentially enabling remote code execution or crashing the MQTT broker/client process. No authentication or user interaction is required (CVSS:3.1 AV:N/AC:L/PR:N/UI:N), making this exploitable at scale against internet-exposed or network-accessible ICS and IoT endpoints. CNSF inline IPS (Suricata) with MQTT-aware signatures and Cloud Firewall egress/ingress controls could detect or block malformed MQTT packet delivery at the network perimeter.

Confidence:

High

Related CVEs

Included CVEs with severity scores, affected products, exploit status, and reference links.

CVE-2026-125132
CVSS 8.6
An integer underflow (wrap or wraparound) vulnerability in libumqtt versions 1.1.1 and earlier allows a remote unauthenticated attacker to cause a denial of service, memory corruption, or information disclosure via a network-accessible MQTT endpoint.
Affected Products:
libumqtt libumqtt – <= 1.1.1

Exploit Status:
no public exploit
References:
https://www.cisa.gov/news-events/ics-advisories/icsa-26-323-03 https://github.com/zhaojh329/libumqtt

MITRE ATT&CK® Techniques

Initial Access
T1190
Exploit Public-Facing Application

Execution
T1203
Exploitation for Client Execution

Impact
T1499
Endpoint Denial of Service

Impact
T1499.004
Application or System Exploitation

Collection
T1005
Data from Local System

Exfiltration
T1041
Exfiltration Over C2 Channel

Defense Evasion
T1211
Exploitation for Defense Evasion

Potential Compliance Exposure

Mapping incident impact across multiple compliance frameworks.

NIST SP 800-53 Rev. 5 – Flaw Remediation
Control ID: SI-2
No patch or remediation is currently available for CVE-2026-125132 in libumqtt <=1.1.1. Organizations using this library in critical infrastructure environments are unable to apply vendor-supplied fixes, violating the expectation of timely flaw remediation and patch management processes required under SI-2.

NIS2 Directive – Vulnerability Handling and Disclosure
Control ID: Article 21(2)(e)
The libumqtt repository owners did not respond to CISA coordination requests, and no remediation has been issued. Under NIS2, essential and important entities operating in sectors such as energy, transport, and water are required to manage vulnerabilities through coordinated disclosure and timely mitigation. Absent vendor response, affected operators bear heightened residual risk with no clear remediation path.

CISA Zero Trust Maturity Model 2.0 – Network Segmentation and Least Privilege Access
Control ID: Network Pillar - Macro/Micro Segmentation
The vulnerability is remotely exploitable over the network with no authentication required (AV:N/PR:N). CISA ZTMM 2.0 requires that ICS and OT network segments be isolated from internet-facing systems and business networks. Lack of network segmentation allows unauthenticated remote attackers to reach MQTT broker endpoints and trigger the integer underflow, enabling denial of service or memory corruption.

PCI DSS 4.0 – Patch and Update Management for Software Components
Control ID: Requirement 6.3.3
PCI DSS 4.0 requires that all system components are protected from known vulnerabilities by installing applicable security patches and updates. Where the libumqtt library is used in payment-adjacent or cardholder data environment infrastructure, the absence of an available patch and the high CVSS score (8.6) creates a material compliance gap under software vulnerability management requirements.

DORA (EU) 2022/2554 – ICT Vulnerability and Patch Management
Control ID: Article 10 - ICT Vulnerability Management
DORA requires financial entities to establish and maintain ICT vulnerability management processes including identification, classification, and remediation of vulnerabilities in third-party components. The use of libumqtt in operational or communication infrastructure with no available fix and a high-severity integer underflow directly exposes financial entities to ICT risk management obligations under DORA Article 10.

IEC 62443-3-3 – Network and Security Configuration Settings
Control ID: SR 7.6
IEC 62443-3-3 requires industrial automation and control systems to enforce network traffic filtering and resource availability protections. The unauthenticated, network-accessible integer underflow in libumqtt directly threatens system availability (VA:H) and can cause memory corruption in MQTT-dependent control system components across critical manufacturing, energy, water, and transportation sectors, undermining availability and integrity security requirements.

Sector Implications

Industry-specific impact of the vulnerabilities, including operational, regulatory, and cloud security risks.
Oil/Energy/Solar/Greentech
libumqtt integer underflow vulnerability (CVE-2026-125132, CVSS 8.8) threatens MQTT-based ICS/SCADA systems, risking denial of service and memory corruption across critical energy infrastructure with no available remediation.

Utilities
Water, wastewater, and utility control systems deploying libumqtt <=1.1.1 face remote exploitation enabling memory corruption and information disclosure, with lateral movement risk compounded by absent vendor patch response.

Transportation
CISA-identified critical transportation infrastructure using libumqtt-dependent IoT/ICS messaging faces high-severity remote denial-of-service attacks, with zero trust segmentation and egress controls urgently needed to contain exploitation.

Information Technology/IT
IT environments running libumqtt <=1.1.1 MQTT broker libraries face unauthenticated remote memory corruption; compliance gaps across NIST.800-53.SC-7 and ZTMM.Network controls elevate exfiltration and lateral movement risk significantly.

Sources

libumqtt https://www.cisa.gov/news-events/ics-advisories/icsa-26-323-03
Verified

libumqtt GitHub Repository (zhaojh329/libumqtt) https://github.com/zhaojh329/libumqtt
Verified

CISA ICS Recommended Practices: Improving Industrial Control Systems Cybersecurity with Defense-in-Depth Strategies https://www.cisa.gov/ics
Verified

NVD - CVE Detail Search for CWE-191 Integer Underflow https://nvd.nist.gov/vuln/search/results?cwe_id=CWE-191
Verified

CISA Known Exploited Vulnerabilities Catalog https://www.cisa.gov/known-exploited-vulnerabilities-catalog
Verified

Frequently Asked Questions
What is CVE-2026-125132 and which products are affected? CVE-2026-125132 is a critical integer underflow (CWE-191) vulnerability in libumqtt versions 1.1.1 and earlier. It allows a remote unauthenticated attacker to cause denial of service, memory corruption, or information disclosure in any system using the affected library, spanning ICS, OT, and IoT deployments worldwide.

Is there a patch available for the libumqtt integer underflow vulnerability?
What compliance gaps does this vulnerability expose for critical infrastructure operators?

Cloud Native Security Fabric Mitigations and Controls CNSF
Based on the attack progression modeled above, these are the defensive controls that would constrain each stage.

Aviatrix Zero Trust CNSF is directly relevant here because the attack chain depends on unrestricted network reachability to MQTT-exposed devices and uncontrolled east-west paths across OT/IT segments. By enforcing segmentation, identity-aware routing, and controlled egress, CNSF would likely reduce both the initial attack surface and the attacker's ability to pivot across critical infrastructure networks.
Initial Compromise
Control: Cloud Native Security Fabric (CNSF)
Mitigation: Inline network inspection with MQTT-aware signatures could reduce the reachability of malformed packet delivery to vulnerable endpoints, and perimeter ingress controls would likely limit which external sources can even initiate MQTT sessions toward internal ICS devices.

Privilege Escalation
Control: Zero Trust Segmentation
Mitigation: Zero Trust segmentation enforcing least-privilege service identities and workload namespace isolation would likely reduce the blast radius of a compromised MQTT process, constraining what network resources and adjacent services that elevated process context can directly reach.

Lateral Movement
Control: East-West Traffic Security
Mitigation: East-west traffic enforcement across OT and IT segments would likely reduce the attacker's ability to propagate malicious MQTT payloads laterally, constraining workload-to-workload reachability to only explicitly permitted communication paths and reducing the number of additional devices the attacker could access from an initial foothold.

Command & Control
Control: Multicloud Visibility & Control
Mitigation: Centralized traffic observability and policy enforcement across cloud and hybrid environments would likely surface anomalous MQTT connections destined for unauthorized external broker endpoints, giving operators the visibility needed to identify and act on unexpected outbound MQTT sessions that deviate from established device communication baselines.

Exfiltration
Control: Egress Security & Policy Enforcement
Mitigation: Outbound egress controls with FQDN-based filtering would likely reduce the attacker's ability to route extracted data to unknown or attacker-controlled external infrastructure, constraining the set of permitted outbound destinations for MQTT devices to only approved operational endpoints.

Impact (Mitigations)
If prior CNSF controls were in place and working as intended, the attacker's reach across the OT/IT environment would likely be narrower by this stage, reducing the number of devices subject to denial-of-service or persistent implantation and limiting disruption to a more contained subset of the operational environment rather than the full critical infrastructure deployment.

Impact at a Glance

Affected Business Functions
Industrial Control System (ICS) MQTT Communication Services
Operational Technology (OT) Network Availability
Critical Infrastructure Telemetry and Sensor Data Pipelines
Water and Wastewater Supervisory Control Systems

Operational Disruption
Estimated downtime: N/A

Financial Impact
Estimated loss: N/A

Data Exposure
Potential exposure of MQTT message payloads traversing affected libumqtt instances, which may include sensor telemetry, operational commands, or configuration data from critical infrastructure deployments across Critical Manufacturing, Energy, Information Technology, Transportation Systems, and Water and Wastewater sectors. No confirmed exploitation or data breach has been reported. The integer underflow vulnerability could allow information disclosure of memory contents alongside potential denial of service of MQTT broker or client processes, disrupting real-time operational data flows in internet-exposed or inadequately segmented ICS environments. No patch is currently available from the vendor.

Recommended Actions

Key Takeaways & Next Steps

• Deploy inline IPS (Suricata) with MQTT protocol-aware signatures to detect and block malformed MQTT packets matching CVE-2026-125132 integer underflow patterns before they reach vulnerable libumqtt endpoints, reducing Initial Compromise risk at the network layer.

• Enforce Zero Trust Segmentation with least-privilege identity-based policies to isolate MQTT broker and client workloads into discrete microsegmented namespaces, preventing lateral movement across OT/IT boundaries if a device is compromised.

• Apply Egress Security & Policy Enforcement with FQDN-based outbound filtering to block unauthorized MQTT connections from ICS devices to external or unrecognized broker endpoints, disrupting both C2 channel establishment and data exfiltration paths.

• Enable Multicloud Visibility & Control with traffic observability and anomaly baselining to detect unusual MQTT publish/subscribe patterns, unexpected external broker connections, or high-frequency malformed packet bursts indicative of active exploitation or C2 activity.

• Immediately minimize network exposure of all libumqtt-dependent devices by placing them behind Cloud Firewall (ACF) ingress controls and VPN-enforced access, ensuring no direct internet reachability until a vendor patch becomes available or replacement libraries are deployed.

Secure the Paths Between Cloud Workloads
A cloud-native security fabric that enforces Zero Trust across workload communication—reducing attack paths, compliance risk, and operational complexity.

Stop Advanced Threats Free Containment Assessment Under Active Attack?

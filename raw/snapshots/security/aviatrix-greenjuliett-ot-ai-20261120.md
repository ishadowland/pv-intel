<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://aviatrix.ai/threat-research-center/category/utilities/ -->
<!-- fetched_at: 2026-11-23 09:43:46 -->
<!-- sha256: 7c9b3a512d4a6901c9d34032233739c3b8f93e0e67e87096e5affbc2f4189ede -->

Utilities Cyber Threats & Breach Reports | Aviatrix TRC Aviatrix
Platform
Products
Solutions
Partners
Resources
Why Aviatrix
Threat Research Center
Under Active Attack

Industry Category Utilities
Breach intelligence, attack campaigns, and threat reports targeting the Utilities sector.

551 threat reports
Page 1 of 46

Explore Other Sectors

Accounting Aerospace Aerospace/Aviation Agriculture Airlines/Aviation Animation Apparel/Fashion Architecture/Planning Artificial Intelligence Artificial Intelligence/Machine Learning Arts/Crafts Automotive Aviation/Aerospace Banking/Mortgage Biotechnology/Greentech Blockchain/Cryptocurrency Broadcast Media Broadcasting Media Broadcasting/Media Building Materials Business Supplies/Equipment Capital Markets/Hedge Fund/Private Equity Chemical Chemicals Civic/Social Organization Civil Engineering Cloud Computing Cloud Computing/SaaS Cloud Native Security Fabric (CNSF) Cloud Services Commercial Facilities Commercial Real Estate Computer Games Computer Hardware Computer Networking Computer Software/Engineering Computer/Network Security Construction Consulting Consumer Electronics Consumer Goods Consumer Services Cosmetics Cosmetics Critical Manufacturing Cryptocurrencies Cryptocurrency Customer Services Cybersecurity Dairy Dating/Personal Services Dating/Social Platforms Defense/Space Design E-Learning Education Management Electrical/Electronic Manufacturing Emergency Services Energy Energy/Oil/Solar/Greentech Entertainment/Movie Production Environmental Services Events Services Executive Office Facilities Services Farming Fashion/Apparel Financial Services Fine Art Fishery Food Production Food/Beverages Fortune 500 companies Franchising Fundraising Gambling/Casinos Gaming Gaming/Casinos Government Administration Government Facilities Government Relations Graphic Design/Web Design Health Care / Life Sciences Healthcare Higher Education/Acadamia History of cryptography Hospitality Hospitals Human Resources/HR Import/Export Individual/Family Services Industrial Automation Information Services Information Technology/IT Insurance International Affairs International Trade/Development Internet Investment Banking/Venture Investment Management/Hedge Fund/Private Equity Judicial Judiciary Law Enforcement Law Practice/Law Firms Legal Services Legislative Office Leisure/Travel Logistics/Procurement Luxury Goods/Jewelry Machinery Management Consulting Manufacturing Maritime Market Research Marketing/Advertising/Sales Mechanical or Industrial Engineering Media Production Medical Equipment Medical Practice Military Industry Mining/Metals Mobile Museums/Institutions Music Newspapers/Journalism Non-Profit/Volunteering Oil/Energy/Solar/Greentech Online Publishing Other Industry Outsourcing/Offshoring Package/Freight Delivery Parking Pharmaceuticals Philanthropy Photography Plastics Political Organization Primary/Secondary Education Professional Services Professional Training Public Relations/PR Public Safety Publishing Industry Railroad Manufacture Real Estate/Mortgage Recreational Facilities/Services Religious Institutions Renewables/Environment Research Industry Restaurants Retail Industry Robotics Rural Healthcare Security/Investigations Semiconductors Shipbuilding Social Media/Internet Sporting Goods Sports Staffing/Recruiting Supermarkets Technology Technology/IT Telecommunications Think Tanks Toys and Games Transportation Travel/Tourism Trucking/Freight Utilities Venture Capital/VC Warehousing Water and Waste Management Water and Wastewater Water and Wastewater Systems Water and Wastewater Treatment Water Treatment Water, Waste, Steam, and Air Conditioning Services Water/Waste Management Water/Wastewater Water/Wastewater Management Water/Wastewater/Utilities Wholesale Wine/Spirits Wireless Writing/Editing

Utilities Threat Reports
Showing 1 – 12 / 551 reports

AI Joins the Industrial Attack Workflow: How GreenJuliett Is Weaponizing LLMs Against OT Infrastructure
Food Production 2 days ago
AI Joins the Industrial Attack Workflow: How GreenJuliett Is Weaponizing LLMs Against OT Infrastructure
In October 2026, a state-sponsored Iranian threat actor tracked as GreenJuliett (also known as CyberAv3ngers and Bauxite, a unit of Iran's IRGC Cyber Electronic Command) executed a coordinated OT sabotage campaign that altered defrost settings on refrigeration controllers across more than 700 retail locations in France, triggering fires, equipment damage, and food losses estimated in the tens of millions of euros. The group leveraged AI-augmented tooling—including self-hosted LLM gateways, Persian-language chat interfaces, and access to frontier AI models—to accelerate PLC reconnaissance, generate targeting scripts against industrial protocols such as Modbus TCP, and expand scanning operations to Fortinet FortiGate edge devices across the Middle East. France formally attributed the attack to Shahid Kaveh on November 9, 2026.

This incident marks a structural shift in OT threat tradecraft: AI is no longer an occasional research aid used through commercial accounts but is now embedded directly into adversary operating environments as a force multiplier. The GreenJuliett campaign demonstrates that financially motivated and state-sponsored actors are industrializing AI-assisted attack workflows against critical infrastructure, compressing the time between reconnaissance and physical impact.
Critical impact
Utilities
Oil/Energy/Solar/Greentech
Industrial Automation
Kill Chain
IC Initial Compromise ( high )
PE Privilege Escalation ( medium )
LM Lateral Movement ( medium )
C&C Command & Control ( high )
E Exfiltration ( low )
I Impact ( high )

Read report

Race to Admin: How CVE-2026-126088 Lets Attackers Create Rogue Accounts in OpenPLC Runtime
Oil/Energy/Solar/Greentech 3 days ago
Race to Admin: How CVE-2026-126088 Lets Attackers Create Rogue Accounts in OpenPLC Runtime
In November 2026, CISA published ICS Advisory ICSA-26-323-01 disclosing a critical race condition vulnerability (CVE-2026-126088, CVSS 4.0: 9.2) in Autonomy Logic OpenPLC Runtime versions 4.2.4 and earlier. The flaw, rooted in CWE-362 concurrent execution with improper synchronization, allows an unauthenticated remote attacker to send parallel HTTP requests that each pass an existence check before any user record is committed—resulting in multiple rogue admin accounts being created without credentials. Affected deployments span critical infrastructure sectors including energy, manufacturing, transportation, and water systems worldwide. The vendor has released version 4.3.0 as the remediation.

OpenPLC is widely deployed as an open-source programmable logic controller runtime in operational technology environments, making unauthenticated admin account creation particularly dangerous. This vulnerability class is resurging across ICS platforms as attackers pivot from IT networks to OT systems, and regulatory scrutiny of control system security under frameworks like NERC CIP and ICS-CERT guidance continues to intensify.
High impact
Utilities
Transportation
Industrial Automation
Kill Chain
IC Initial Compromise ( high )
PE Privilege Escalation ( high )
LM Lateral Movement ( medium )
C&C Command & Control ( medium )
E Exfiltration ( medium )
I Impact ( medium )

Read report

Unpatched and Dangerous: CVE-2026-125132 Integer Underflow in libumqtt Threatens Global Critical Infrastructure
Oil/Energy/Solar/Greentech 3 days ago
Unpatched and Dangerous: CVE-2026-125132 Integer Underflow in libumqtt Threatens Global Critical Infrastructure
In November 2026, CISA issued ICS Advisory ICSA-26-323-03 disclosing a critical integer underflow vulnerability (CVE-2026-125132, CVSS v4.0: 8.8 HIGH) in libumqtt, an open-source MQTT client library maintained on GitHub. All versions up to and including 1.1.1 are affected. A remote, unauthenticated attacker can exploit this memory corruption flaw over the network with no user interaction required, potentially triggering denial of service, arbitrary memory corruption, or sensitive information disclosure. The vulnerability affects critical infrastructure sectors including Energy, Critical Manufacturing, Transportation Systems, Information Technology, and Water and Wastewater globally. No patch is currently available, as the repository maintainers did not respond to CISA coordination requests.

MQTT is a foundational protocol for IoT and industrial control systems, making memory corruption vulnerabilities in its client libraries especially dangerous. The lack of vendor response and absence of an available patch leave operators with no straightforward remediation path, forcing reliance on network-level controls and segmentation as compensating measures while exploitation risk remains unresolved.
High impact
Utilities
Transportation
Information Technology/IT
Kill Chain
IC Initial Compromise ( high )
PE Privilege Escalation ( medium )
LM Lateral Movement ( medium )
C&C Command & Control ( medium )
E Exfiltration ( medium )
I Impact ( high )

Read report

Siemens SIMATIC NTLM Authentication Bypass: 14 ICS Products Exposed with No Patch in Sight
Industrial Automation 5 days ago
Siemens SIMATIC NTLM Authentication Bypass: 14 ICS Products Exposed with No Patch in Sight
In November 2026, CISA republished a Siemens ProductCERT advisory (ICSA-26-321-08) disclosing a critical authentication bypass vulnerability (CVE-2026-58114) affecting 14 versions of Siemens SIMATIC products, including WinCC, PCS 7, Process Historian, SIMATIC BATCH, and Information Server. The flaw stems from the use of the deprecated NTLM authentication protocol over unencrypted SQL Server communications, enabling an on-path (machine-in-the-middle) attacker to relay NTLM credentials, hijack legitimate user sessions, and execute arbitrary code with victim-level privileges. No patches are planned or available for the majority of affected products, leaving critical manufacturing environments worldwide exposed indefinitely.

This incident underscores a persistent and dangerous pattern in ICS/OT environments: reliance on legacy authentication protocols combined with unencrypted internal traffic creates systemic exposure. As nation-state and ransomware actors increasingly target industrial control systems, the absence of patch availability makes network-level compensating controls—such as encrypted transit and strict east-west segmentation—the only viable near-term defense for operators of these platforms.
High impact
Utilities
Chemicals
Oil/Energy/Solar/Greentech
Kill Chain
IC Initial Compromise ( high )
PE Privilege Escalation ( high )
LM Lateral Movement ( medium )
C&C Command & Control ( medium )
E Exfiltration ( medium )
I Impact ( medium )

Read report

Node2Shell (CVE-2026-111497): A CVSS 9.8 Memory Corruption Threat Hiding in 15 Siemens ICS Products
Industrial Automation 5 days ago
Node2Shell (CVE-2026-111497): A CVSS 9.8 Memory Corruption Threat Hiding in 15 Siemens ICS Products
In October 2026, the Node.js project disclosed a critical out-of-bounds write vulnerability (CVE-2026-111497), dubbed 'Node2Shell,' residing in the Brotli compression decoder bundled within Node.js (Google Brotli versions 1.0.3 through 1.2.0). A remote, unauthenticated attacker can exploit this flaw via a crafted Brotli-compressed stream to corrupt adjacent decoder memory, potentially achieving arbitrary remote code execution, sensitive memory disclosure, or denial of service. CISA republished Siemens ProductCERT advisory SSA-242944 on November 17, 2026, confirming impact across 15 Siemens Industrial Automation Software products—including SIMATIC WinCC, TIA Administrator, and User Management Component—deployed globally in critical manufacturing, food and agriculture, and energy sectors. Patches are available only for a subset of affected products.

The Node2Shell vulnerability arrives amid a sustained wave of ICS/OT-targeted campaigns and a broader threat landscape in which memory-corruption exploits in widely-deployed open-source libraries are weaponized against operational technology environments. With most affected Siemens products carrying no available fix at time of disclosure, defenders face an extended window of exposure, amplifying the risk of supply-chain-style exploitation across industrial control networks worldwide.
Critical impact
Oil/Energy/Solar/Greentech
Food Production
Utilities
Kill Chain
IC Initial Compromise ( high )
PE Privilege Escalation ( medium )
LM Lateral Movement ( medium )
C&C Command & Control ( medium )
E Exfiltration ( medium )
I Impact ( medium )

Read report

Six ICS Vulnerabilities in Dorsett Controls InfoScan Threaten Water Infrastructure Globally
Utilities 5 days ago
Six ICS Vulnerabilities in Dorsett Controls InfoScan Threaten Water Infrastructure Globally
In November 2026, CISA published ICS Advisory ICSA-26-321-01 disclosing six vulnerabilities in Dorsett Controls InfoScan versions 1.45.0 and earlier, a building and infrastructure management platform deployed globally in water and wastewater critical infrastructure. The flaws—spanning improper TLS certificate validation, hard-coded cryptographic keys, missing authentication on critical endpoints, unauthenticated information disclosure, and verbose error messages leaking Node.js stack traces—collectively enable an attacker to intercept network communications, recover database credentials, enumerate usernames and system configuration without authentication, and map internal infrastructure from the publicly distributed installer. The highest-severity vulnerability (CVE-2026-117659) scores 8.1 CVSS v3.1. Dorsett Controls released InfoScan v1.46 as the remediation.

These vulnerabilities are emblematic of a widening attack surface in operational technology environments where ICS software inherits web-application security debt. With nation-state actors increasingly pre-positioning in water and energy ICS networks, unauthenticated information disclosure and broken TLS validation in internet-facing or VPN-connected OT management clients dramatically lower the bar for initial reconnaissance and credential theft.
High impact
Government Administration
Environmental Services
Industrial Automation
Kill Chain
IC Initial Compromise ( high )
PE Privilege Escalation ( high )
LM Lateral Movement ( medium )
C&C Command & Control ( high )
E Exfiltration ( medium )
I Impact ( low )

Read report

No Patch, High Risk: Siemens SIMATIC WinCC Arbitrary Code Execution Flaw Threatens Critical Manufacturing
Industrial Automation 5 days ago
No Patch, High Risk: Siemens SIMATIC WinCC Arbitrary Code Execution Flaw Threatens Critical Manufacturing
In November 2026, CISA republished a Siemens ProductCERT advisory (ICSA-26-321-09 / SSA-979641) disclosing a high-severity arbitrary code execution vulnerability—CVE-2026-59082, CVSS 7.8—affecting Siemens SIMATIC WinCC versions V7.5, V8.0, and V8.1. The flaw resides in the Graphics Designer component, which implicitly executes active content embedded in project files when a user opens them, requiring no elevated privileges and only minimal user interaction. Because no patch is currently available across all three affected versions, Siemens and CISA advise restricting file sources, applying qualified-personnel controls, and isolating WinCC systems behind firewalls and VPNs.

This disclosure arrives amid a broader wave of ICS/OT-targeted campaigns in which threat actors deliver weaponized engineering files through spear-phishing or supply-chain manipulation. The absence of an available fix across widely deployed WinCC versions elevates operational risk for critical manufacturing environments globally, underscoring the urgency of compensating network controls.
High impact
Utilities
Oil/Energy/Solar/Greentech
Defense/Space
Kill Chain
IC Initial Compromise ( high )
PE Privilege Escalation ( medium )
LM Lateral Movement ( medium )
C&C Command & Control ( medium )
E Exfiltration ( medium )
I Impact ( medium )

Read report

Path Traversal and PLC Password Exposure: Inside the Siemens SIMATIC S7 Webserver API Vulnerabilities (ICSA-26-321-02)
Industrial Automation 5 days ago
Path Traversal and PLC Password Exposure: Inside the Siemens SIMATIC S7 Webserver API Vulnerabilities (ICSA-26-321-02)
In October 2026, CISA republished a Siemens ProductCERT advisory (SSA-390352) disclosing two vulnerabilities in the .NET Client Library for SIMATIC S7 Webserver API, a software component widely used to integrate industrial programmable logic controllers (PLCs) into enterprise IT environments. CVE-2026-85114 (CVSS 7.5 HIGH) is a path traversal flaw (CWE-22) that allows an attacker who can manipulate ticket download responses to write arbitrary files outside the intended directory, potentially overwriting application files. CVE-2026-85115 (CVSS 5.5 MEDIUM) exposes PLC restore passwords in plaintext HTTP error messages, enabling credential theft from logs or diagnostic outputs. Siemens has released patched versions V3.3.61 and V3.3.62 to address each flaw respectively.

These vulnerabilities illustrate a persistent pattern in ICS/OT environments: software supply chain components that bridge IT and OT networks introduce high-impact attack surfaces. As IT-OT convergence accelerates, unpatched client libraries in critical manufacturing sectors can serve as pivot points for adversaries seeking to manipulate or disrupt industrial operations, raising urgent patch management and network segmentation priorities for security teams.
High impact
Critical Manufacturing
Electrical/Electronic Manufacturing
Utilities
Kill Chain
IC Initial Compromise ( high )
PE Privilege Escalation ( high )
LM Lateral Movement ( medium )
C&C Command & Control ( low )
E Exfiltration ( medium )
I Impact ( medium )

Read report

14 Critical Flaws in Copeland Dixell Refrigerators: How Nation-State Actors Are Targeting Your Cold Chain
Supermarkets 1 week ago
14 Critical Flaws in Copeland Dixell Refrigerators: How Nation-State Actors Are Targeting Your Cold Chain
In early 2025, cybersecurity researchers at VulnCheck disclosed 14 critical vulnerabilities in Copeland's Dixell XWEB EVO refrigeration supervision system, with severity scores ranging from 8.0 to 9.8. At least two flaws are confirmed under active exploitation. The most alarming bug allows unauthenticated attackers to execute shell commands directly from the login page before any password check occurs, granting root-level access. These vulnerabilities affected the same platform linked to a October 2024 attack on 700 French supermarkets attributed to Iranian-backed threat actors, and separately to suspected cyberattacks on U.S. military refrigeration units. Patches are available, but legacy systems remain exposed.

This incident represents a broader, accelerating pattern of ICS and OT device exploitation across critical infrastructure sectors including food supply chains and military logistics. With honeypot research confirming that internet-exposed industrial controllers attract attacker probes within hours of deployment, the attack surface for operational technology environments has never been more contested or consequential.
Medium impact
Food Production
Military Industry
Utilities
Kill Chain
IC Initial Compromise ( high )
PE Privilege Escalation ( high )
LM Lateral Movement ( medium )
C&C Command & Control ( medium )
E Exfiltration ( medium )
I Impact ( high )

Read report

php2shell: Critical Unauthenticated RCE in Siemens Energy and Building Automation Products (CVE-2026-109618 & CVE-2026-109619)
Oil/Energy/Solar/Greentech 1 week ago
php2shell: Critical Unauthenticated RCE in Siemens Energy and Building Automation Products (CVE-2026-109618 & CVE-2026-109619)
On October 21, 2026, the PHP project and independent security researchers disclosed two critical unauthenticated remote code execution vulnerabilities — CVE-2026-109618 and CVE-2026-109619 — collectively tracked as 'php2shell,' affecting the core PHP language runtime. Siemens subsequently confirmed that multiple Building Automation and Energy products, including AMIS TS, blueplanet 360, Energy Engage, Spectrum Power 3/4/7/TG, and Local Monitoring bt-monitoring-vm, run vulnerable PHP versions across all deployed instances. With CVSS scores of 9.8 (Critical) and 8.1 (High), these flaws allow network-adjacent or internet-exposed adversaries to execute arbitrary code without authentication, threatening operational continuity, grid reliability, and sensitive energy infrastructure data worldwide.

The disclosure arrives as ICS and OT environments face an accelerating wave of exploitation targeting internet-facing web components embedded in operational technology. With no fix available for several affected product lines — including Energy Engage V2.0SP9 where no fix is planned — energy operators must urgently prioritize network segmentation and access controls to shield vulnerable systems from exploitation while vendor patches mature.
Critical impact
Utilities
Industrial Automation
Government Administration
Kill Chain
IC Initial Compromise ( high )
PE Privilege Escalation ( medium )
LM Lateral Movement ( medium )
C&C Command & Control ( medium )
E Exfiltration ( medium )
I Impact ( medium )

Read report

CVSS 9.8 Alert: Siemens RUGGEDCOM APE1808 Exposed to Unauthenticated RCE via Brotli Library Flaw
Electrical/Electronic Manufacturing 1 week ago
CVSS 9.8 Alert: Siemens RUGGEDCOM APE1808 Exposed to Unauthenticated RCE via Brotli Library Flaw
In October 2026, CISA republished a Siemens ProductCERT advisory (SSA-898633) disclosing a critical vulnerability in the RUGGEDCOM APE1808 industrial edge appliance running Palo Alto Networks PAN-OS. The flaw, tracked as CVE-2026-111497 (CVSS 9.8 Critical), stems from an out-of-bounds write bug in Google Brotli compression library versions 1.0.3 through 1.2.0. A remote, unauthenticated attacker can send a crafted Brotli-compressed stream to corrupt adjacent decoder memory, disclose sensitive contents, trigger denial-of-service, or achieve arbitrary code execution. All deployed versions of RUGGEDCOM APE1808 are affected, and the appliance is widely used across critical manufacturing sectors globally.

This advisory highlights a recurring and dangerous pattern: widely deployed open-source compression libraries embedded in industrial and network security appliances become critical attack surfaces. As ICS/OT environments increasingly converge with IT infrastructure, unpatched third-party library dependencies in edge devices can expose entire operational technology networks to remote exploitation without any authentication barrier.
Critical impact
Oil/Energy/Solar/Greentech
Utilities
Industrial Automation
Kill Chain
IC Initial Compromise ( high )
PE Privilege Escalation ( medium )
LM Lateral Movement ( medium )
C&C Command & Control ( medium )
E Exfiltration ( medium )
I Impact ( low )

Read report

CVSS 9.8: How a Brotli Decoder Flaw Puts Siemens ICS Environments at Critical RCE Risk

Threat Report

Oil/Energy/Solar/Greentech 1 week ago
CVSS 9.8: How a Brotli Decoder Flaw Puts Siemens ICS Environments at Critical RCE Risk
In October 2026, CISA and Siemens ProductCERT disclosed a critical remote code execution vulnerability (CVE-2026-111497, CVSS 9.8) affecting Siemens Desigo CC V8 and V9 building management platforms and Gridscale X DSA and PSS-E industrial energy management systems. The flaw originates from an out-of-bounds write in the Brotli compression decoder (CWE-787), allowing an unauthenticated remote attacker to corrupt decoder memory, disclose sensitive data, cause denial of service, or achieve arbitrary code execution via a maliciously crafted compressed stream. Affected deployments span critical manufacturing, energy, and IT sectors worldwide. Siemens released patched versions and recommends immediate update, network segmentation, firewall controls, and VPN enforcement for remote access scenarios.

This disclosure underscores the accelerating risk of third-party library vulnerabilities propagating into operational technology and industrial control system environments. As ICS/OT assets increasingly connect to enterprise networks and cloud infrastructure, unpatched memory-corruption flaws in widely embedded open-source components represent a systemic attack surface that adversaries are actively targeting across critical infrastructure sectors globally.
Critical impact
Utilities
Industrial Automation
Government Administration
Kill Chain
IC Initial Compromise ( high )
PE Privilege Escalation ( medium )
LM Lateral Movement ( medium )
C&C Command & Control ( medium )
E Exfiltration ( low )
I Impact ( medium )

Read report

1 2 3 4 5 ... 46

[ INCIDENT RESPONSE // UNDER ATTACK? ]
Stop Active Cloud Data Exfiltration
Aviatrix Rapid Containment helps teams instantly identify what data is leaving the environment, from which workload, and where it’s going — during an active breach.

Under Attack

Looking for threats in a different sector?
Browse All Threat Reports

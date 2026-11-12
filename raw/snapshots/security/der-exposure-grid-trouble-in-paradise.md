<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.conceptio.app/document/667918/grid-trouble-in-paradise-uncovering-vulnerable-distributed-energy-reso -->
<!-- fetched_at: 2026-11-12 12:12:24 -->
<!-- sha256: 51ff4d9df22b65f56d112318ac88417c555ec825080831632b7eccf595be9ec9 -->

Grid Trouble in Paradise: Uncovering Vulnerable Distributed Energy Resources and Their Grid-Level Risks: Conceptio Open Knowledge Archive

Conceptio › Archive › arXiv CS

arXiv CS
open access

Grid Trouble in Paradise: Uncovering Vulnerable Distributed Energy Resources and Their Grid-Level Risks

· arxiv_cs

arXiv CS · Papers

Open Source ↗ Direct PDF ↓

cryptography cybersecurity privacy security

Conceptio Open Archive
Analyze & explore related research in Conceptio
Connect this record directly into your research workflow or AI agent. Explore citations across open repositories, query full text, and export structured proof bundles.
Explore in Search → Connect via MCP / API ↗

arXiv:2609.07783v1 [cs.CR] 7 Sep 2026

Grid Trouble in Paradise: Uncovering Vulnerable Distributed
Energy Resources and Their Grid-Level Risks
Anna Raymaker

Samuel Talkington

Zeezoo Ryu

Georgia Institute of Technology
Atlanta, GA, USA
araymaker3@gatech.edu

Georgia Institute of Technology
Atlanta, GA, USA
talkington@gatech.edu

Georgia Institute of Technology
Atlanta, GA, USA
zeezooryu@gatech.edu

Richard Asiamah

Emad Abukhousa

Betelihem Ashebo

Georgia Institute of Technology
Atlanta, GA, USA
rasiamah3@gatech.edu

Georgia Institute of Technology
Atlanta, GA, USA
emadak@gatech.edu

Georgia Institute of Technology
Atlanta, GA, USA
bashebo3@gatech.edu

Animesh Chhotaray

Daniel K. Molzahn

Frank Li

Georgia Institute of Technology
Atlanta, GA, USA
achhotaray3@gatech.edu

Georgia Institute of Technology
Atlanta, GA, USA
molzahn@gatech.edu

Georgia Institute of Technology
Atlanta, GA, USA
frankli@gatech.edu

Saman Zonouz

Raheem Beyah

Georgia Institute of Technology
Atlanta, GA, USA
szonouz6@gatech.edu

Georgia Institute of Technology
Atlanta, GA, USA
ab207@gatech.edu

Abstract
Grid-connected solar distributed energy resources (DERs), such
as solar inverters and monitoring platforms, have been deployed
at unprecedented scale over the past few years, with global solar
capacity more than doubling since 2022. To support monitoring
and control, many of these systems are Internet-connected and
configured by installers or end users, yet the real-world scale of their
Internet exposure and the implications for power grid operation
remain poorly understood.
In this paper, we present an Internet-scale evaluation of exposed
and vulnerable solar DER infrastructure, and assess the risk that
compromised DERs can pose to energy grids. We develop a method
for accurately identifying solar DERs from Internet scanning data,
and discover a diverse population of over 66,000 Internet-exposed
solar DERs. We detect that at least 10,000 of these DERs may have
known CVEs, such as unauthenticated monitoring and control
endpoints. To assess the risk that these vulnerable DERs pose to
a power grid, we use an electric grid network for Oahu, Hawaii,
established and used by the power system research community,
and conduct a power system analysis. Our evaluation shows that
by compromising exposed DERs, attackers can cause voltage and
line flow violations across multiple locations in the Oahu network,
resulting in a range of consequences from degraded power quality to
damaged power system components to power outages. Ultimately,

This work is licensed under a Creative Commons Attribution 4.0 International License.
CCS ’26, The Hague, Netherlands.
© 2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2871-6/2026/11
https://doi.org/10.1145/3830454.3846739

our work brings to light the emerging threat of grid-connected
DERs, and provides directions for improving energy security.

CCS Concepts
• Hardware → Power networks; Power estimation and optimization; • Security and privacy → Hardware attacks and
countermeasures; Domain-specific security and privacy architectures; • Applied computing → Operations research.

Keywords
grid cyber resilience, distributed energy resources, mathematical
optimization, inverters, measurement
ACM Reference Format:
Anna Raymaker, Samuel Talkington, Zeezoo Ryu, Richard Asiamah, Emad
Abukhousa, Betelihem Ashebo, Animesh Chhotaray, Daniel K. Molzahn,
Frank Li, Saman Zonouz, and Raheem Beyah. 2026. Grid Trouble in Paradise:
Uncovering Vulnerable Distributed Energy Resources and Their Grid-Level
Risks. In Proceedings of the 2026 ACM SIGSAC Conference on Computer
and Communications Security (CCS ’26), November 15–19, 2026, The Hague,
Netherlands. ACM, New York, NY, USA, 20 pages. https://doi.org/10.1145/
3830454.3846739

1

Introduction

In December 2025 [43], a coordinated cyberattack targeted Poland’s
renewable energy sector, exploiting Internet-exposed control interfaces to disrupt distributed energy systems across the country.
Rather than breaching centralized utility infrastructure, attackers
exploited known vulnerabilities in edge-facing devices. This marked
a shift from past attacks [14, 17, 58] on the Ukrainian power grid,
which focused on high-value control centers, to a distributed attack model aligned with the grid’s evolution toward distributed

CCS ’26, November 15–19, 2026, The Hague, Netherlands.

energy resources (DERs)1 [15]. Post-incident analysis of the attack
in Poland estimates that a broader compromise could have removed
over a gigawatt of generation capacity simultaneously [17]. Such a
sudden loss during peak demand could have triggered frequency
instability and cascading failures, similar to those observed during
the 2025 Iberian grid collapse [20]. The incident illustrates a recurring pattern in power-grid attacks: exploiting known vulnerabilities
in reachable devices to induce system-wide disruption.
The attack on DERs in Poland coincides with their rapid global expansion, particularly solar DERs. Between 2022 and 2024, global solar capacity doubled to 2 terawatts, driven by widespread adoption
of grid-connected inverters and batteries. Unlike centralized generation, DERs inject power directly into distribution networks and are
frequently managed via cloud dashboards, web interfaces, or vendor
APIs. This architecture introduces new cyber–physical vulnerabilities, as devices (e.g., solar inverters) that directly affect grid behavior
are now reachable from the public Internet [21, 22, 31]. The security
implications are increasingly evident. In just two years, over 129
CVEs have been issued for solar DER platforms covering vulnerabilities in firmware, web dashboards, and control APIs [8, 31, 40]. Yet
despite the expanding threat landscape, two critical gaps remain: (a)
no reproducible, validated methodology exists for discovering the
heterogeneous DER population at scale, and (b) we lack a grounded
understanding of the worst-case grid consequences if such devices,
especially solar inverters that directly control power generation,
are compromised. In this paper, we address both challenges.
Prior work has made progress along two separate axes. Internetwide scans have exposed vulnerabilities in cyber-physical systems [18, 35, 42, 47] but have not systematically characterized solar
DER exposure or connected it to grid impact. Power-systems research has modeled the destabilizing potential of high-wattage load
manipulation [45, 48, 52] but assumes hypothetical adversaries with
control over millions of devices. Neither line addresses the central
question for solar DERs: what can attackers actually do with the
inverters exposed today? Answering this requires modeling powersupply-side attacks against the empirically exposed population –
fundamentally different from prior demand-side analyses, since
compromised inverters control both active and reactive power and
require orders of magnitude fewer devices.
In practice, measuring DER exposure is challenging due to fragmented vendors, device roles, and installer-driven deployments
that rely on non-standard, vendor-specific web interfaces. This
heterogeneity produces noisy scanner artifacts that make it difficult to distinguish operational DER devices from generic web
infrastructure at scale. Translating measured exposure into gridlevel impact is similarly constrained by the limited availability of
realistic distribution-network models with detailed DER placement.
These challenges and research gaps motivate the questions:
RQ1: How are solar DER platforms exposed on the public Internet,
and what security-relevant control surfaces are reachable?
RQ2. What grid-level consequences could an attacker induce by
manipulating these devices?

Raymaker et al.

To answer these questions, we combine Internet-scale measurement with power-system analysis. We develop a cross-vendor discovery pipeline that identifies exposed solar DER platforms across
Internet scan data. To filter non-device infrastructure at scale, we
use an LLM to label a training set and a supervised classifier to
apply those labels across 1.8M hosts. We then characterize reachable interfaces, map them to attacker capabilities, and simulate
worst-case attacks on a realistic power grid model.
We identify 66,379 solar DER hosts spanning over 150 countries.
Exposure is dominated by web-based management interfaces that
enable device configuration and control, and at least 11,826 hosts
are associated with known vulnerabilities. To our knowledge, this
is the largest population of Internet-exposed cyber-physical devices identified by a measurement study, exceeding prior work on
PLCs [42] and EV charging systems [38] by a factor of two or more.
Grounding this exposure in a power-system context, we conduct
the first measurement-driven grid impact analysis in the security
community. Using exposed inverters in Oahu, we show that coordinated manipulation of just 41.1 MW of generation is sufficient
to drive 18 of 37 buses more than 10% below nominal voltage and
overload 6 of 89 transmission lines on a realistic grid model, conditions that can damage motors and transformers and force protective
disconnections that lead to outages. Unlike prior (power) demandside attacks that require coordinating millions of high-wattage
IoT devices [48, 52], supply-side compromise gives attackers direct
control over both active and reactive power. This enables voltage
manipulation that demand-side attacks cannot achieve, with orders
of magnitude fewer devices.
Our findings demonstrate that insecure DER interfaces are widespread and operationally consequential. They provide adversaries
with an expanding and poorly secured attack surface that warrants
immediate attention from vendors, operators, and regulators.
In summary, our contributions are as follows:
• A measurement-driven power-system analysis that maps empirically observed Internet-exposed solar DERs into attacker capabilities and quantifies resulting grid-level violations using a realistic
power grid model.
• A global, Internet-scale measurement of 66,379 exposed solar
DER hosts, produced by a scalable discovery pipeline that combines
deterministic fingerprinting, LLM-assisted labeling, and supervised
classification to separate operational DERs from Internet noise
across heterogeneous vendor ecosystems.
• https://gridtrouble.xyz, a public tool that simulates and visualizes
the maximum grid impact achievable on Oahu using actual, currently exposed DERs from our measurement. Users can select inverter
subsets, adjust control settings, and watch the impacts change.

2

In this section, we present our threat model, review prior work on
Internet-wide discovery of networked devices and on the systemlevel impact of large-scale device compromise, and give an overview
of our measurement and power-analysis approach.

2.1
1 DERs: small-scale grid-connected assets including solar inverters, batteries, and the

meters and gateways used to monitor and control them.

Threat Model, Related Work, and Overview

Threat Model

We consider an Internet-based adversary targeting solar-DER infrastructure such as rooftop and small-commercial solar inverters,

Grid Trouble in Paradise: Uncovering Vulnerable Distributed Energy Resources and Their Grid-Level Risks

monitoring gateways, and fleet, or installer-managed platforms,
through publicly reachable interfaces. Consistent with known attacks [43] against DERs, we consider the adversary operates without
physical proximity or on-premises access and interacts with devices
solely via the public Internet, including web management interfaces,
monitoring dashboards, installer portals, and exposed industrial
control protocols (e.g., Modbus TCP). When authentication is weak
or absent, the attacker may read or modify inverter configuration
parameters such as power setpoints, operational modes, or device
state, and may trigger actions including disconnection, reboot, or
firmware upload. We infer the capabilities of the attacker only from
scanner-visible interfaces and documented control functionality.

2.2

Related Work

Internet-Wide Discovery. Prior work has shown that Internetwide scanning and indexing platforms such as Censys and Shodan
enable large-scale measurement of exposed networked systems [18].
Early studies revealed widespread exposure of industrial control systems (ICS), often lacking authentication or basic access controls [35].
Subsequent work identified exposed ICS remote management interfaces and extended Internet-wide measurement techniques to
other cyber-physical domains such as robotics and automotive
systems [12, 46, 47, 56, 60].
More recent research has introduced automated discovery pipelines.
PLCHound [42] showed that iterative, cross-protocol inference can
substantially improve recall for programmable logic controllers
(PLCs), while ChargePrint [38] applied Internet-scale measurement
to electric vehicle charging systems. These approaches succeed
because their targets share structural regularities that discovery
can key on: PLCs expose a small set of standardized industrial
protocols (e.g., Modbus, EtherNet/IP, CODESYS) and consistent
product identifiers (e.g., recognizable web-management banners)
that generalize across vendors, and EV chargers commonly implement OCPP [3]. DER ecosystems share none of these regularities,
so existing discovery techniques do not readily generalize to DERs;
applying PLCHound’s method [42] to our DER population confirms
this, returning few devices.
These structural differences also limit brand- and product-anchored
discovery, as in Forescout’s Shodan-based snapshot [22]: it misses
devices without a recognizable identifier (53.7% of our validated
hosts carry no vendor fingerprint; Section 4.2) and relies on scannerprovided device labels shown to be unreliable [42]. Our pipeline
instead recovers this heterogeneous, largely unbranded population.
More fundamentally, prior industry and academic efforts characterize exposure but stop there. We are the first to bridge exposure
and impact: connecting a measured, validated DER population to a
quantified, grid-level consequence analysis (Section 5) is the central
contribution of this work.
Large-Scale Device Compromise. A complementary line of
work has examined the consequences of large-scale 

> ⚠️ 快照已截断（原文超长）

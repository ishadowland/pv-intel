<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.autodcstech.com/cisa-12-november-2026-siemens-ics-advisories -->
<!-- fetched_at: 2026-11-17 07:11:05 -->
<!-- sha256: c8f67e35938adfb43dbac9f5e69c9a0ba71b8a70ea730d4bb82f2ffb94c13287 -->

CISA's 12 November 2026 Siemens ICS Advisories: 5 Notices

We use cookies to enhance your browsing experience, serve personalised ads or content, and analyse our traffic.
Accept All Reject All

Skip to content

Free shipping on all orders
|

+86 158 8020 0923

|

[email protected]

November 13, 2026
News

CISA's 12 November 2026 Siemens ICS Advisories: Five Notices, Three CVEs

By Wayne · Published 13 Nov 2026

TL;DR: CISA's 12 November 2026 ICS release carried six advisories, five of them Siemens: ICSA-26-316-01 through ICSA-26-316-05. They cover building-automation and energy software, Desigo CC V8/V9 and Gridscale X, Industrial Edge Management, and two RUGGEDCOM APE1808 notices. Only three CVEs sit behind all five — CVE-2026-111497 (Node2Shell), CVE-2026-109618 and CVE-2026-109619 (PHP2Shell) — and every notice is a CISA republication of a Siemens ProductCERT advisory first published between 23 and 30 October 2026. The top score is 9.8. None of the five describes an authentication bypass.

Desigo CC, Industrial Edge Management and RUGGEDCOM APE1808 all sit upstream of cabinets like this one. What the advisories ask for is patch sequencing, not a blanket shutdown.
Key takeaways

Five Siemens notices, not five new vulnerabilities. CISA published ICSA-26-316-01 to -05 on 12 November 2026; all five are verbatim republications of Siemens SSAs issued between 23 and 30 October.

Three CVEs cover the entire release. CVE-2026-111497 appears in three advisories, CVE-2026-109618 and CVE-2026-109619 in the other two.

Every CVSS v3.1 score is 9.8 except one. CVE-2026-109619 scores 8.1 because its attack complexity is high, not because the impact is smaller.

Node2Shell and PHP2Shell are memory-safety bugs, not access-control bugs. That distinction matters when you brief operations staff who hear "critical" and assume an identity bypass.

Several products have no fix at all. AMIS TS, blueplanet 360 NX3 and three Spectrum Power 4 configurations are listed as affected with no remediation available; Siemens gives compensating controls instead.

Industrial Edge Management without Management Applications needs no action. Siemens states the affected Brotli library is present but not exposed in that configuration.

Which five Siemens advisories did CISA publish on 12 November 2026?

CISA published five Siemens ICS advisories on 12 November 2026 — ICSA-26-316-01 through ICSA-26-316-05 — in a release that also carried one Hitachi Energy update. They cover building-automation and energy products, Desigo CC and Gridscale X, Industrial Edge Management, and two RUGGEDCOM APE1808 notices. All five republish Siemens ProductCERT advisories first issued between 23 and 30 October 2026.

CISA ID
Siemens SSA
Product family
CVE(s)
CVSS v3.1

ICSA-26-316-01
SSA-166980
Building Automation and Energy Products (AMIS TS, blueplanet 360 NX3, Energy Engage, Spectrum Power)
CVE-2026-109618, CVE-2026-109619
9.8 / 8.1

ICSA-26-316-02
SSA-045512
Desigo CC V8 and V9, Gridscale X DSA, Gridscale X PSS®E
CVE-2026-111497
9.8

ICSA-26-316-03
SSA-443410
Industrial Edge Management applications and configurators
CVE-2026-111497
9.8

ICSA-26-316-04
SSA-898633
RUGGEDCOM APE1808 with Palo Alto Networks PAN-OS
CVE-2026-111497
9.8

ICSA-26-316-05
SSA-566512
RUGGEDCOM APE1808 with PAN-OS 10.2, 11.1, 11.2, 12.1, 12.2
CVE-2026-109618, CVE-2026-109619
9.8 / 8.1

The 12 November release is a republication cycle, not a new disclosure event. Siemens first published SSA-566512 on 23 October and SSA-166980 on 26 October, then added products on 29 October, 4 November and 6 November. It follows the same pattern as the ICS cycle CISA ran on 29 October , where the vendor advisories predated the ICSA numbers by several days. CISA's ICSA pages carry those revision histories unchanged, which is why the "release date" and the underlying disclosure date are five weeks apart. If you track patching by CISA publication date only, you are already behind the vendor's own timeline.

What are Node2Shell and PHP2Shell?

Node2Shell is CVE-2026-111497, an out-of-bounds write in Google Brotli versions 1.0.3 through 1.2.0, which Node.js bundles in its decoder. PHP2Shell is CVE-2026-109618 and CVE-2026-109619, two use-after-free paths in PHP's out-of-memory and global-state handling. Both issues were disclosed on 21 October 2026 and both can end in remote code execution.

CVE-2026-111497 is rated 9.8 on CVSS v3.1 with the vector CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H , and CWE-787. NVD's CVSS v4.0 entry scores it 9.2 with AT:P — attack requirements present — a detail that matters more than the headline number. Google's own remediation is narrow: move any Brotli library or binary between 1.0.3 and 1.2.0 to 1.0.10, 1.1.1 or 1.2.1.

The PHP pair behaves differently. CVE-2026-109618 (9.8) abuses PHP's use of longjmp() for out-of-memory exits, leaving request memory uninitialized before an allocation. CVE-2026-109619 (8.1) is a stale-global-state variant; its vector sets AC:H , which is the only reason it is not also 9.8. Siemens' SSA-166980 summary calls both of them critical, while its own metrics table scores the second at 8.1. The table is the number to quote.

Does a 9.8 CVSS score mean the equipment is remotely exploitable today?

No. A 9.8 base score describes the vulnerable library in its worst case, not your network. Every CVE in this release is AV:N/PR:N/UI:N, but exploitation still needs a reachable service that feeds attacker-controlled Brotli or PHP input into the affected component. Segmentation, a closed management interface, or an application that is not installed removes that path without a patch.

The vector string is the part worth reading line by line. AV:N means the attack is delivered over a network, not that the device is on the internet. PR:N means no credentials are required — it does not mean an attacker can bypass authentication, which is a different weakness class and a different CWE. UI:N means no victim has to open a file. What the score cannot tell you is whether your deployment exposes the function that calls the decoder.

Advisory
CVE
Score
Privileges / interaction
What must be true for exploitation

ICSA-26-316-01
CVE-2026-109618
9.8 (AV:N/AC:L)
None / none
A PHP build below the fixed release is running and accepts attacker-supplied requests that reach the OOM path; AMIS TS, blueplanet 360 NX3 and Spectrum Power 4 have no fix listed

ICSA-26-316-01
CVE-2026-109619
8.1 (AV:N/AC:H)
None / none
Same PHP exposure, plus the race-dependent global-state reuse has to line up; Energy Engage V2.0 SP9 has no fix planned

ICSA-26-316-02
CVE-2026-111497
9.8 (AV:N/AC:L)
None / none
A Node.js runtime inside Desigo CC V8/V9, Gridscale X DSA 5.3 or PSS®E before 36.8.0 accepts a crafted Brotli stream on an exposed interface

ICSA-26-316-03
CVE-2026-111497
9.8 (AV:N/AC:L)
None / none
At least one affected Industrial Edge Management configurator is installed and reachable; installations with no Management Applications are explicitly out of scope

ICSA-26-316-04 / -05
CVE-2026-111497, CVE-2026-109618, CVE-2026-109619
9.8 / 9.8 / 8.1
None / none
The APE1808 module runs an affected PAN-OS release and exposes a management or data-plane service that decodes Brotli or PHP content

Two practical readings follow. First, an air-gapped or tightly segmented Desigo CC server scores the same 9.8 as an internet-facing one, but the reachability precondition is not met. Second, the PAN-OS dependency in ICSA-26-316-04 and -05 means the fix comes from Palo Alto Networks, not from a Siemens service pack — a purchasing and support path many plant teams do not have pre-arranged.

Which versions are affected, advisory by advisory?

ICSA-26-316-01 — building automation and energy products

Siemens lists AMIS TS, blueplanet 360 NX3 M6 WM OD IISX in both standard and -S variants, Energy Engage V2.0 SP9 and V3.1 SP1, Local Monitoring bt-monitoring-vm before 20261103, Spectrum Power 3, Spectrum Power 4, Spectrum Power 7 and Spectrum Power TG. Despite the "building automation" in the title, the affected table is almost entirely energy and grid software. The only remediations Siemens provides are: PHP 8.1.34 release 6 for Energy Engage V3.1 SP1, the 20261103 build for bt-monitoring-vm, a Red Hat PHP patch for Spectrum Power 7 on RHEL 8 and 9, a Red Hat RHEL 7 patch for Spectrum Power 3, and PHP 8.5.12 for Spectrum Power TG. AMIS TS, both blueplanet variants, Energy Engage V2.0 SP9 and the three Spectrum Power 4 configurations are listed with no fix available.

ICSA-26-316-02 — Desigo CC and Gridscale X

Desigo CC family V8 and V9 are listed as affected at all versions, alongside Gridscale X DSA from V5.3 up to but excluding V5.4, and Gridscale X PSS®E before V36.8.0. Siemens' remediation text for both Desigo branches reads "install the latest .NET security updates via Windows Update" — not a Desigo service pack. That is the vendor's wording and it is worth confirming with Siemens support before you close the ticket, because the underlying CVE is a Brotli decoder issue and the known-not-affected entries in the same SSA cite "Node.js not present" as the reason other products are excluded.

ICSA-26-316-03 — Industrial Edge Management

Ten components are listed. Six have vendor fixes: Cloud Connector Configurator to V1.24.3, Data Flow Monitoring to V3.0.18, Databus Configurator to V4.0.1, DataXess Configurator to V1.5.7, Edge OPC UA Server Configurator to V2.3.10 and Flow Creator Configurator to V1.15.1. Two were fixed centrally with no customer action: Industrial Edge Hub from 29 October 2026 and Industrial Edge Management Cloud from 28 October 2026. Two have no fix: Common Configurator on IEM and Common Configurator on Device. Siemens' instructions are unusually direct for the no-fix cases — uninstall all Management Applications and put a firewall or WAF in front of the IEM instance, or stop Common Configurator on Device entirely.

ICSA-26-316-04 and -05 — RUGGEDCOM APE1808 with PAN-OS

Both advisories cover the same hardware: the RUGGEDCOM APE1808 application processing engine running Palo Alto Networks PAN-OS. They exist because Siemens resells PAN-OS as part of that module, and Palo Alto published its own upstream notices for Node2Shell and PHP2Shell. -04 covers CVE-2026-111497 at all versions; -05 covers CVE-2026-109618 and CVE-2026-109619 across PAN-OS 10.2, 11.1, 11.2, 12.1 and 12.2. The remediation in both is to upgrade to the corresponding available PAN-OS release and to contact customer support for the patch path. The APE1808 is an application hosting module, not a RUGGEDCOM Ethernet switch — a detail worth correcting if your asset register lumps it in with the RSG or RST families.

What should you do first if you cannot patch this week?

Siemens' fallback for every advisory in this release is the same: restrict network access to the affected product to trusted parties, keep the management interface off the business network, and place a firewall or WAF in front of anything that must stay reachable. Where an application cannot be patched at all, uninstall or stop it until a fix exists.

Turn that into four actions that do not require a maintenance window:

Inventory the configurators, not just the platform. Most Industrial Edge Management exposure lives in the individual configurator apps. If Cloud Connector Configurator, Data Flow Monitoring, Databus, DataXess, the OPC UA Server Configurator or Flow Creator are installed below the fixed builds, they are the patching queue.

Stop Common Configurator on Device now. There is no fix, the mitigation is to stop the service, and Siemens states it plainly. Schedule the restart only after a fixed build appears.

Treat APE1808 as a PAN-OS asset. Put it in the firewall-team patch cycle, not the PLC cycle, and confirm which PAN-OS branch each module runs before you promise a date.

Check whether Desigo CC actually runs the affected component. The SSA's known-not-affected entries exclude products on the grounds that Node.js is absent. Establish the same fact for your V8 and V9 servers before applying .NET updates as a proxy for a Desigo fix.

If your estate already carries a licensing or engineering-station dependency, the same sequencing logic applies to the Automation License Manager hardening work around CVE-2024-44087 , where the vendor fix, the network control and the Windows behaviour all had to be read separately.

What this release is not

Three corrections are worth stating because they are circulating alongside the advisories.

It is not an authentication-bypass batch. All three CVEs are memory-safety issues — CWE-787 out-of-bounds write and CWE-416 use-after-free — scored PR:N because no credentials are needed to reach the vulnerable parser, not because an attacker can cross an identity boundary. If your incident-response playbook opens with "check for unauthorized accounts", it is aimed at the wrong artefact. The Mendix SAML flaw from October was that kind of issue; this batch is not.

It is not five new discoveries. Siemens published the underlying SSAs in October. CISA's 12 November pages are republications under the ICSA numbering, and their revision histories show exactly which products were added on 29 October, 4 November and 6 November.

It is not a RUGGEDCOM switch advisory. The APE1808 is an application processing engine. Siemens' switch families are not in this release, and treating the two as one asset class will produce the wrong patch owner.

How should a mixed Siemens estate sequence the work?

Patch the components with published fixed builds first, because they close the exposure outright: the six Industrial Edge Management configurators, Gridscale X DSA to V5.4 and PSS®E to V36.8.0. Then handle Desigo CC through the .NET update path, then APE1808 through PAN-OS, and finally apply compensating controls to the products Siemens lists without a fix.

That order front-loads the work with a verifiable end state. A configurator at V1.24.3 is either installed or it is not, which makes it easy to prove closure to an auditor. Desigo CC and APE1808 both depend on another vendor's patch channel, so they carry lead time you cannot compress. The no-fix group — AMIS TS, blueplanet 360 NX3, Energy Engage V2.0 SP9, three Spectrum Power 4 configurations and the two Common Configurator variants — should be handled as a network-control project rather than a patching project.

For the automation layer itself, the same rule of thumb applies as in our analysis of CISA's 2030 strategy and legacy PLC planning : the installed base sets the calendar, not the advisory date.

What does this mean for spares and service planning?

A patch cycle that touches Desigo CC servers, Industrial Edge Management hosts and PAN-OS modules rarely stops at software. It usually reveals that the cabinet behind the software is running an older CPU, an unsupported PLC or I/O module , or an HMI panel that cannot be updated independently of the controller. Those are the parts that turn a two-week patch window into a six-week procurement.

Three checks are worth running before the next maintenance slot. Confirm whether the affected host is a physical Industrial Edge device or a virtual one, because the update path differs. Confirm whether the APE1808 module is in a RUGGEDCOM communication chassis that will need to come out of service. And confirm whether the Desigo CC server is still inside its vendor support window, since .NET updates on an unsupported OS build are not a durable answer.

For parts identification, the Siemens automation range covers the controllers, I/O and communication modules that sit under these advisories, and the Siemens parts and datasheet index is the faster route when you already have a part number. If you are weighing whether an affected module should be patched or replaced, the contact page is the shortest path to a specific answer.

Frequently asked questions

Did CISA publish five new Siemens vulnerabilities on 12 November 2026?

No. CISA published five Siemens ICS advisories that day, but all five are republications of Siemens ProductCERT advisories issued between 23 and 30 October 2026. Only three CVEs are involved: CVE-2026-111497, CVE-2026-109618 and CVE-2026-109619. The 12 November date marks the ICSA numbering and republication, not the original disclosure.

Is the RUGGEDCOM APE1808 a switch, and why is it in a Siemens advisory?

The APE1808 is an application processing engine that runs Palo Alto Networks PAN-OS, not a RUGGEDCOM Ethernet switch. It appears in ICSA-26-316-04 and -05 because Siemens resells that PAN-OS build, and Palo Alto published upstream notices for the same two library issues. The fix is a PAN-OS upgrade obtained through Siemens support, not a Siemens firmware file.

Do I need to act on Desigo CC if my server shows no Node.js?

Siemens lists Desigo CC V8 and V9 at all versions as affected in SSA-045512, with the remediation "install the latest .NET security updates via Windows Update". At the same time, the SSA excludes other products because Node.js is not present. Those two statements point at different components, so confirm with Siemens support which process on your V8 or V9 server actually carries the decoder before you close the item.

Is a 9.8 score enough to justify taking a line offline?

Not on its own. The score describes the vulnerable library, and the vector is AV:N/PR:N/UI:N, so the deciding question is reachability: whether a service on that host accepts attacker-supplied Brotli or PHP content. If the management interface is segmented and only reachable from an engineering VLAN, the operational case for an emergency outage is much weaker than the number suggests.

Which Industrial Edge Management components need no action at all?

Installs with no Management Applications. Siemens states that although the affected Brotli library ships in the Industrial Edge Management stack, the affected functionality is not used or exposed in that configuration, and the same applies to IEDK. Industrial Edge Hub and Industrial Edge Management Cloud were also fixed centrally on 29 and 28 October 2026 with no customer action required.

Where can I verify the version ranges before patching?

Use the Siemens SSA pages, not the CISA mirror, when you need revision history: SSA-166980, SSA-045512, SSA-443410, SSA-898633 and SSA-566512. Each lists known-affected and known-not-affected products separately, and the revision notes show which products were added after the first publication. The CISA ICSA pages carry the same tables plus the CSAF JSON link.

Sources

CISA, ICSA-26-316-01, "Siemens Building Automation and Energy Products", 12 November 2026. cisa.gov/news-events/ics-advisories/icsa-26-316-01

CISA, ICSA-26-316-02, "Siemens Desigo, Gridscale", 12 November 2026. cisa.gov/news-events/ics-advisories/icsa-26-316-02

CISA, ICSA-26-316-03, "Siemens Industrial Edge Management", 12 November 2026. cisa.gov/news-events/ics-advisories/icsa-26-316-03

CISA, ICSA-26-316-04 and ICSA-26-316-05, "Siemens RUGGEDCOM APE1808", 12 November 2026. cisa.gov/news-events/ics-advisories/icsa-26-316-04 and -05

Siemens ProductCERT, SSA-166980, SSA-045512 (V1.2, 6 November 2026), SSA-443410, SSA-898633, SSA-566512. cert-portal.siemens.com

NVD, CVE-2026-111497, published 22 October 2026, CVSS v3.1 9.8 and CVSS v4.0 9.2 (AT:P). nvd.nist.gov/vuln/detail/CVE-2026-111497

Palo Alto Networks security advisories for CVE-2026-111497 and CVE-2026-109618, referenced by Siemens in the APE1808 notices. security.paloaltonetworks.com

All advisory pages were fetched on 13 November 2026. Siemens revises its SSAs without a new CISA republication, so check the SSA revision number against the build you are actually deploying.

Talk to us

If you are mapping these five advisories onto a specific cabinet, send the part numbers and the installed firmware versions. We can tell you which modules are still supported, which have a fixed build available, and where a replacement is the cheaper route. Start from the contact page .

More in News
ABB AI Robot Trainer: What the Fashion Inductor Upgrade Changes
Festo, NVIDIA and ABB Link a Three-Axis Handling Twin to RobotStudio
Cyient DLM and Hindustan Shipyard MoU: What It Covers, What It Does Not

Share:

Leave a Reply Cancel reply

« Hybrid AC/DC Distribution at 700 VDC: What the Schneider Electric Webinar Covers

Siemens SSA-970803: NTLM Relay in SIMATIC SCADA and PCS 7 »

Recent Products

330910-00-03-05-02-00 | Bently Nevada 0.5 m Probe M10X1

Bently Nevada

330901-00-12-10-02-CN 1.0 m Probe, Miniature Coaxial

Bently Nevada

330881-28-10-112-03-02 Bently Nevada Adapter Option

Bently Nevada

330876-02-50-00-05 M14x1.5 5 m Proximity Probe

Bently Nevada

Recent News

November 16, 2026

ABB AI Robot Trainer: What the Fashion Inductor Upgrade Changes

November 16, 2026

Festo, NVIDIA and ABB Link a Three-Axis Handling Twin to…

November 16, 2026

Cyient DLM and Hindustan Shipyard MoU: What It Covers, What…

November 13, 2026

Siemens SSA-970803: NTLM Relay in SIMATIC SCADA and PCS 7

Express Shipping

Extensive Inventory

Quality Assurance

Global Service

© 2026 AutoDCSTech . All rights reserved.

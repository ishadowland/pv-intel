<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.trout.software/blog/siemens-node2shell-php2shell-brotli-php-ot-advisories-icsa-26-316 -->
<!-- fetched_at: 2026-11-15 07:11:50 -->
<!-- sha256: 43ff521efd8cec8ec917527bd0c33e5bb7462cc338ab7fcae85e4873a758f353 -->

Siemens Node2Shell and PHP2Shell Advisories (ICSA-26-316)
Back to Blog ICS Advisories OT Security Supply Chain Segmentation Critical Infrastructure
Node2Shell and PHP2Shell in Siemens OT Products: Five CISA Advisories (ICSA-26-316-01 to -05)
Trout Team · Last updated : November 12, 2026 · 11 min read
The short version

On November 12, 2026 , CISA republished five Siemens advisories, ICSA-26-316-01 to -05 . They trace back to two open-source library bugs . The first is CVE-2026-111497 , an out-of-bounds write in the Google Brotli decoder that Siemens calls Node2Shell (CVSS v3.1 9.8 ). The second is a pair of PHP use-after-free flaws, CVE-2026-109618 (9.8) and CVE-2026-109619 (8.1), that Siemens calls PHP2Shell . All three allow remote code execution without authentication, and all three are in the CISA Known Exploited Vulnerabilities catalog .

The two libraries reach a wide range of Siemens products: Spectrum Power energy management systems, Desigo CC building automation, Gridscale X , Industrial Edge applications, and the RUGGEDCOM APE1808 , the ruggedized platform that runs a Palo Alto Networks PAN-OS firewall inside the plant. Several products have no fix , and one has no fix planned.

For those servers, the control is who can reach them. Take them off the flat network, allow named users on the ports they need, and record the sessions until Siemens ships a fix.

What the advisories say

Each CISA advisory republishes a Siemens ProductCERT advisory (SSA) first released between October 23 and October 30, 2026.

Advisory Siemens SSA Products CVE CVSS v3.1 Fix status
ICSA-26-316-01 SSA-166980 Spectrum Power 3, 4, 7, TG; Energy Engage; AMIS TS; blueplanet; bt-monitoring-vm CVE-2026-109618, CVE-2026-109619 9.8, 8.1 Mixed. No fix for AMIS TS, blueplanet and Spectrum Power 4. No fix planned for Energy Engage V2.0SP9
ICSA-26-316-02 SSA-045512 Desigo CC V8 and V9, Gridscale X DSA, Gridscale X PSS®E CVE-2026-111497 9.8 Fixes available
ICSA-26-316-03 SSA-443410 Industrial Edge Management and Device applications CVE-2026-111497 9.8 Mostly fixed. No fix for Common Configurator on IEM and on Device
ICSA-26-316-04 SSA-898633 RUGGEDCOM APE1808 with PAN-OS CVE-2026-111497 9.8 Upgrade to the corresponding PAN-OS version
ICSA-26-316-05 SSA-566512 RUGGEDCOM APE1808 with PAN-OS 10.2, 11.1, 11.2, 12.1, 12.2 CVE-2026-109618, CVE-2026-109619 9.8, 8.1 Upgrade to the corresponding PAN-OS version

Siemens also lists CVSS v4.0 scores of 9.2 for these CVEs in its own advisories.

The PHP products in ICSA-26-316-01, product by product:

Product Fix status, per the advisory
AMIS TS No fix available
blueplanet 360 NX3 M6 WM OD IISX and IISX - S No fix available
Spectrum Power 4 with Nagios or Zabbix, Web Office Portal V3.0 to V3.2, or HISViews V1.0 No fix available
Energy Engage V2.0SP9 No fix planned
Energy Engage V3.1SP1 Upgrade PHP to V8.1.34 release 6
Local Monitoring bt-monitoring-vm Update to V20261103 or later
Spectrum Power 3, NagiosXI monitoring on RHEL 7, CVE-2026-109619 only Red Hat PHP patch for RHEL 7
Spectrum Power 7, NagiosXI monitoring Red Hat PHP patch for RHEL 8 and 9
Spectrum Power TG, WebConsole and WebQuery on Windows Upgrade PHP to V8.5.12

The Brotli fixes in ICSA-26-316-02 and -03. Desigo CC V8 and V9 are fixed by installing the latest .NET security updates through Windows Update. Gridscale X DSA goes to V5.4 and Gridscale X PSS®E to V36.8.0. On Industrial Edge, Cloud Connector Configurator goes to V1.24.3, Data Flow Monitoring to V3.0.18, Databus Configurator to V4.0.1, DataXess Configurator to V1.5.7, Edge OPC UA Server Configurator to V2.3.10 and Flow Creator Configurator to V1.15.1. Siemens fixed Industrial Edge Hub and Industrial Edge Management Cloud on its side, with no user action needed.

Common Configurator has no fix. For Common Configurator on IEM, Siemens says to uninstall all management applications and protect the IEM instance with a firewall or WAF. For Common Configurator on Device, it says to stop the application. If no management applications are installed, Siemens says no action is required, because the Brotli library is present but not used. We covered an earlier, unrelated IEM flaw in the Industrial Edge Management password reset post .

Sectors. CISA lists Energy for ICSA-26-316-01, Critical Manufacturing, Energy and Information Technology for -02, and Critical Manufacturing for -03, -04 and -05. All are deployed worldwide.

Exploitation status

The two libraries were patched upstream in late October. PHP shipped 8.2.35, 8.3.36, 8.4.27 and 8.5.12 on October 21, 2026, and CISA issued an alert the same day urging immediate patching. The Brotli fix is in 1.0.10, 1.1.1 and 1.2.1 , per the advisories.

CISA added CVE-2026-109618 and CVE-2026-109619 to KEV on October 26, 2026 , and CVE-2026-111497 on October 27, 2026 . The catalog was at version 2026.11.10 when we checked on November 12.

Palo Alto Networks reports active exploitation of the PHP flaws against PAN-OS management interfaces exposed to the internet. It says it is not aware of malicious exploitation of the Brotli flaw in its products. None of the five Siemens advisories reports exploitation of a Siemens product.

How the flaws reach an OT network

PHP2Shell is a web server problem. The flaws sit in how PHP handles a request that runs out of memory, and in state that survives from one request to the next. PHP's advisory for CVE-2026-109618 confirms Apache mod_php is exploitable over HTTP with default settings. In Siemens products, PHP runs the web front ends: monitoring consoles built on NagiosXI or Zabbix, the Spectrum Power 4 Web Office Portal, and the PAN-OS management interface and XML API. Anyone who can send HTTP requests to those pages can attempt the exploit.

Node2Shell is a decompression problem. Any service that decodes a Brotli stream from an untrusted sender can be hit with a crafted stream. On the APE1808, Palo Alto says the exposure is narrower: only firewalls that inspect Brotli traffic with TLS decryption on the dataplane are exposed , the management interface is not affected, and PAN-OS 10.2 and 11.1 are not affected. Brotli encoding is off by default in PAN-OS 11.2.4 and later, so a firewall is exposed only if someone turned it on. The workaround is to disable it.

The table maps the flaws to MITRE ATT&CK for ICS . It describes what the flaws allow, plus the PAN-OS exploitation Palo Alto has reported. It does not describe an observed attack on a Siemens product.

Tactic Technique (ID) How it applies here
Initial Access Internet Accessible Device (T0883) Palo Alto reports PHP exploitation against PAN-OS management interfaces exposed to the internet
Initial Access Exploit Public-Facing Application (T0819) PHP web front ends and the PAN-OS web UI, when reachable from outside the control network
Initial Access, Lateral Movement Exploitation of Remote Services (T0866) A host already on the network sends crafted HTTP requests or Brotli streams to an internal server
Inhibit Response Function Denial of Service (T0814) The advisories list denial of service as a possible impact of the Brotli flaw

Why this keeps happening

Industrial software is built from the same libraries as web software. PHP and Brotli are everywhere on the internet, so when one breaks, the fix ships fast for web servers. It reaches an energy management system or a building automation server much later, because each vendor has to find the library, rebuild, test and release. Siemens published its advisories within ten days of the PHP fixes. Three weeks after those fixes, some of its products still have none.

The firewall is on the list too. The RUGGEDCOM APE1808 exists to run a firewall close to the equipment. Per Palo Alto, the PHP flaws reach the PAN-OS management web interface and XML API, so the APE1808 inherits PHP2Shell. We made the same point about the FortiOS variant in the APE1808 FortiOS post . A security appliance has its own advisories, so it should not be the only thing protecting a segment.

Patching OT servers takes time. A Spectrum Power update in a control center needs testing and a maintenance window. Our post on patch management in operational environments covers why. When there is no fix at all, the window does not exist yet.

What to do, whatever you run

Find the libraries. List every Siemens product from the five advisories, then ask which other servers in your plants run PHP or decode Brotli. CISA's PHP alert asks for an inventory of PHP embedded in other software, not just web servers.

Patch where a fix exists. That covers Desigo CC, Gridscale X, most Industrial Edge applications, Spectrum Power 3, 7 and TG, Energy Engage V3.1SP1 and bt-monitoring-vm. On the APE1808, Palo Alto lists fixed hotfixes per PAN-OS branch. Note that 11.2.10-h16 fixes PHP only, while 11.2.10-h17 fixes both .

Lock down the PAN-OS management interface. Palo Alto's guidance is to limit management access to trusted internal addresses or a single jump host. Check whether any dataplane interface has a management profile attached, because that exposes the web UI there too.

Contain what you cannot patch. For AMIS TS, blueplanet, Spectrum Power 4 and Energy Engage V2.0SP9, restrict the web front end to the named operators and systems that use it . Keep it off the internet and off the business network. Stop or uninstall Common Configurator, as Siemens advises.

How Access Gate helps, and its limits

Access Gate is an appliance installed at each site. It connects beside your existing network. One route on the current router then steers traffic to the servers you choose through it. Nothing is installed on the Siemens server. It is installed in a day per site. The Lollipop architecture post explains the design.

A per-server rule decides who reaches each web front end. Access control lists are default deny. One rule lets the control room workstations reach the Spectrum Power 4 Web Office Portal over HTTPS. Every other host gets no route , which removes most of the senders that could deliver a PHP2Shell request.

A named person signs in first. An access screen asks for a directory login before a workstation reaches the server. Access expires after 15 minutes, 1 hour or 8 hours.

Admin sessions are tied to a name. With privileged access management , RDP and SSH to the server and HTTPS to admin web interfaces, such as the PAN-OS or IEM consoles, open in a browser session tied to a named person and limited in time. RDP and SSH sessions are recorded. Every rule change lands in the enclave change history .

The limits are real. Access Gate does not patch PHP or Brotli, and it does not detect these CVEs. An allowed user can still send a malicious request to a server it is allowed to reach. Access Gate does not change what the APE1808 firewall decodes on its own dataplane, so disabling Brotli encoding or upgrading PAN-OS is still the answer there. The fixes from Siemens and Palo Alto remain the fixes. See also OT identity , secure remote access and power grid .

What to do this week

List every product from the five advisories, with its version and the SSA that covers it.

Check the KEV entries for CVE-2026-109618, CVE-2026-109619 and CVE-2026-111497, and set priority accordingly.

Test whether any PAN-OS management interface answers from the internet or the business network.

Run show system setting brotli on each APE1808 on PAN-OS 11.2.4 or later, and disable Brotli encoding if you cannot upgrade yet.

Apply the available fixes on Desigo CC, Gridscale X, Industrial Edge, Spectrum Power 3, 7 and TG.

Stop or uninstall Common Configurator on IEM and on devices.

Restrict every unpatched PHP server to named users and recorded admin sessions.

Want to see where a gate would sit in your plant? Build your network in a few minutes. Every other advisory we have covered is in the ICS security advisories archive .

Sources: CISA ICS Advisories ICSA-26-316-01 , ICSA-26-316-02 , ICSA-26-316-03 , ICSA-26-316-04 and ICSA-26-316-05 (November 12, 2026); Siemens ProductCERT SSA-166980 , SSA-045512 , SSA-443410 , SSA-898633 and SSA-566512 ; Palo Alto Networks advisories for CVE-2026-109618 and CVE-2026-111497 ; the PHP advisory GHSA-w8hw-w9fx-j79w ; the Brotli v1.2.1 release ; the CISA PHP alert ; the CISA Known Exploited Vulnerabilities catalog , version 2026.11.10, checked November 12, 2026; and MITRE ATT&CK for ICS . Confirm affected versions and update steps with Siemens and Palo Alto Networks before changing a production system.
FAQ Frequently Asked Questions
What are CISA advisories ICSA-26-316-01 to ICSA-26-316-05? + They are five ICS advisories CISA published on November 12, 2026, each republishing a Siemens ProductCERT advisory. ICSA-26-316-01 (SSA-166980) and ICSA-26-316-05 (SSA-566512) cover the PHP flaws CVE-2026-109618 and CVE-2026-109619. ICSA-26-316-02 (SSA-045512), ICSA-26-316-03 (SSA-443410) and ICSA-26-316-04 (SSA-898633) cover the Brotli decoder flaw CVE-2026-111497. The products are Spectrum Power, Energy Engage, AMIS TS, blueplanet, Desigo CC, Gridscale X, Local Monitoring bt-monitoring-vm, Industrial Edge applications and the RUGGEDCOM APE1808 running PAN-OS.
What are Node2Shell and PHP2Shell? + They are the names Siemens uses in its advisory titles. Node2Shell is CVE-2026-111497, an out-of-bounds write in the Google Brotli decoder that affects Brotli 1.0.3 through 1.2.0, CVSS v3.1 9.8. The name comes from the Node.js security release that patched the Brotli copy bundled with Node.js. PHP2Shell is CVE-2026-109618 (CVSS v3.1 9.8) and CVE-2026-109619 (CVSS v3.1 8.1), two use-after-free flaws in PHP core that allow unauthenticated remote code execution. CISA's PHP alert calls them php2shell. Palo Alto Networks refers to them by CVE ID only.
Which Siemens products have no fix? + Per the advisories: AMIS TS, blueplanet 360 NX3 M6 WM OD IISX and IISX - S, and Spectrum Power 4 deployments using Nagios or Zabbix, Web Office Portal V3.0 to V3.2, or HISViews V1.0 have no fix available for the PHP flaws. Energy Engage V2.0SP9 has no fix planned. For the Brotli flaw, Common Configurator on IEM and Common Configurator on Device have no fix. Siemens says it is preparing further fixes.
Are these vulnerabilities being exploited? + All three CVEs are in the CISA Known Exploited Vulnerabilities catalog: CVE-2026-109618 and CVE-2026-109619 since October 26, 2026, and CVE-2026-111497 since October 27, 2026. Palo Alto Networks reports active exploitation of the PHP flaws against PAN-OS management interfaces exposed to the internet. None of the five Siemens advisories reports exploitation of a Siemens product.
What should I do about a RUGGEDCOM APE1808 running PAN-OS? + Upgrade PAN-OS to a fixed hotfix for your branch and contact Siemens support for APE1808 specifics. For the PHP flaws, which sit in the management web interface and XML API, restrict management access to trusted internal addresses or one jump host, and never expose it to the internet. For the Brotli flaw, Palo Alto says only firewalls inspecting Brotli traffic with TLS decryption are exposed. Brotli encoding is off by default in PAN-OS 11.2.4 and later and unsupported in 11.2.3 and earlier, so check whether it was turned on. The workaround is to disable Brotli encoding.
How do I protect a Siemens server that has no patch? + Treat it as a machine you must contain. Take it off the flat network, allow only the named users and systems that need it, on the ports they need, and record administrative sessions. Siemens and CISA both recommend restricting network access and keeping these systems off the internet. For Common Configurator, Siemens' own mitigation is to uninstall management applications or stop the application until a fix ships.

Other Articles
FLAT NETWOR SEGMEN NETWOR INDUST ENVIRO FLAT · NETWOR · SEGMEN 06 NODES · 07 CONNECTIONS
Flat networks Segmented networks
Flat Network vs Segmented Network in Industrial Environments
Flat network vs segmented network in OT: lateral-movement risk, compliance under CMMC and IEC 62443, and a migration path without production downtime.

FRANCE NIS2 BILL RETURN THE FRANCE · NIS2 · BILL 05 NODES · 07 CONNECTIONS
NIS2 OT Security
France's NIS2 Bill Returns to the Assemblée: What OT Sites Should Do Now
France's NIS2 transposition bill is back on the Assemblée nationale agenda from 9 November 2026. It is not law yet, and ANSSI's ReCyF already says what to prepare. This is what OT and SCADA sites can start now.

SECURI THE ITOT BOUNDA SECURI · THE · ITOT 04 NODES · 04 CONNECTIONS
IT/OT convergence Boundary security
Securing the IT/OT Boundary: Technical Architecture Patterns
Secure the IT/OT boundary with three layered patterns: an industrial DMZ between IT and OT, secure remote access for outside connections, and zero trust segmentation inside OT.

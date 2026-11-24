<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.redtigersecurity.com/advisories -->
<!-- fetched_at: 2026-11-25 07:34:40 -->
<!-- sha256: 4fac91efb35158aea86a962d666fa003fd00ac9bffea3827c66a9cb1e7f6d05c -->

Security Advisories & OT Threat News | Red Tiger Security

Security Advisories & OT Threat News

Security Advisories & OT Threat News

What changed, where it runs in a plant, and what to do about it. Red Tiger's plain-language read on the vulnerabilities and alerts that matter to industrial operators.

No advisories match. Try a different word or choose All.

November 24, 2026
VMware Patches Critical ESX and vCenter Flaws Under Many Control System Servers
Broadcom VMSA-2026-0011 fixes a new 9.8 vCenter authentication bypass and two 9.8 ESX host code execution flaws, with no workaround. Many plants run SCADA, historian and operator servers on one VMware cluster. Update vCenter and every ESX host and limit who can reach them.
Read the advisory →

November 24, 2026
AutomationDirect C-More EA9 Software Flaw Lets a Crafted Project File Run Code
A crafted project file can trigger a heap buffer overflow in AutomationDirect C-More EA9 Programming Software up to V6.80, CVE-2026-127280 scored 7.8, which could let an attacker run code on the engineering laptop. Update to V6.81 and only open trusted project files.
Read the advisory →

November 24, 2026
Danfoss AK-SM 8xxA Refrigeration Controller Flaw Gets a CVE From CISA, Still No Fix
CISA has assigned CVE-2026-129713 to a login-free stack buffer overflow in Danfoss AK-SM 8xxA refrigeration controllers up to 5.4.0, scored 9.8. There is still no fix until 5.5.x, so take these controllers off the internet now and keep Strict Mode on.
Read the advisory →

November 24, 2026
CODESYS Visualization Flaws Let a Malicious Controller Run Code on the Engineering Laptop
Three CODESYS Visualization flaws scored 8.8 let a malicious or impersonated controller runtime run code on the engineering workstation during online monitoring, and a fourth writes files from a malicious project. Update to 4.11.0.0 and turn on encrypted online communication.
Read the advisory →

November 24, 2026
Peninsula Energy Cyber Incident Hits Lance Uranium Project in Wyoming
Peninsula Energy halted trading after a cyber incident at its Lance uranium project in Wyoming that the company says breached its operating system but not its administrative systems. Separate the plant network, lock down remote access, keep offline backups and have an incident plan ready.
Read the advisory →

November 23, 2026
Phoenix Contact FL SWITCH, FL NAT and FL WLAN Affected by BlastRADIUS
Phoenix Contact says 75 FL SWITCH models, three FL NAT models and 14 FL WLAN models are affected by BlastRADIUS (CVE-2024-3596), which lets an attacker-in-the-middle forge a Remote Authentication Dial-In User Service (RADIUS) login approval and may give administrative access. Update FL SWITCH and FL NAT to firmware 3.60 and FL WLAN to 26.10; four older FL WLAN models get no fix.
Read the advisory →

November 23, 2026
Azure API Management Flaw Behind Norway Energy Attacks
Norway's National Security Authority (NSM) has linked the Equinor and Skagerak Energi cyberattacks to an exploited flaw in the Classic tiers of Microsoft Azure API Management, where an unknown attacker went after tokens, secrets and named values. The flaw is closed, but NSM says to assume secrets are exposed: rotate them all, check the RuntimeVersion, and map what sits behind each instance.
Read the advisory →

November 23, 2026
Palo Alto PAN-OS Fixes for Critical NGINX HTTP/2 Flaws
Palo Alto Networks confirmed on 20 November 2026 that two critical NGINX HTTP/2 flaws (CVE-2026-123633 and CVE-2026-123007, CVSS 9.2) affect PAN-OS firewalls and Panorama on recent 11.2, 12.1 and 12.2 releases when HTTP/2 is enabled. Check the setting, turn HTTP/2 off if you cannot upgrade, and move to the fixed hotfix for your branch.
Read the advisory →

November 23, 2026
WAGO, Wiesemann & Theis and ifm Advisories from CERT@VDE
CERT@VDE published three industrial advisories on 23 November 2026: WAGO controller web management flaws that let a low-privileged user run root commands (fix: firmware 4.10.0 FW32), PHP2Shell on Wiesemann & Theis pure.box, Motherbox and FTP Data Station devices (fixed firmware available), and a missing login check on ifm O3D, O3DP and O3X camera sensors with no fix.
Read the advisory →

November 22, 2026
GL.iNet Cloud Flaw Used to Infect Routers and KVM Devices
GL.iNet confirmed on 20 November 2026 that attackers exploited its GoodCloud cloud remote management service to install malware on some routers and Comet KVM-over-IP devices. Find these shadow remote access devices on OT networks, cut their cloud connection, check and update or reset them, and check the HMIs and workstations they were plugged into.
Read the advisory →

November 20, 2026
Cisco Expressway Root Flaw Now Exploited and on CISA KEV List
CISA added critical Cisco Expressway flaw CVE-2026-76466 to its Known Exploited Vulnerabilities catalog on 20 November 2026 after attackers used it to take root control of clustered gateways. Upgrade clustered Expressway devices to X15.5.20, limit cluster ports to trusted peers, check for compromise and keep the gateways away from the control network.
Read the advisory →

November 20, 2026
Phoenix Contact FL WLAN Flaw Lets Low-Privileged Users Take Over Admin
Phoenix Contact released firmware 26.10 on 18 November 2026 for a high-severity flaw in its FL WLAN industrial wireless devices that lets any low-privileged user change the administrator password through the REST API and take full control. Update, keep the devices behind a firewall and clean up shared accounts.
Read the advisory →

November 20, 2026
F5 BIG-IP Emergency Hotfixes for Critical APM and iRules Flaws
F5 released emergency hotfixes on 18 November 2026 for five critical BIG-IP flaws in Access Policy Manager and iRules that let an attacker with no login crash the traffic engine and possibly run code. There is no workaround. Patch under change control, check which features you use, limit exposure and watch for traffic engine restarts.
Read the advisory →

November 19, 2026
VMware vCenter Zero-Day CVE-2026-123890 Exploited by ARMORY CASTLE
Broadcom patched CVE-2026-123890, a critical authentication bypass in VMware vCenter, on 19 November 2026, and Mandiant says the China-linked group ARMORY CASTLE exploited it as a zero-day since early September. Patch to 9.1.1.0200, 9.0.2.0200 or 8.0 U3m, restrict who can reach vCenter, and check for rogue administrator accounts.
Read the advisory →

November 19, 2026
CERT@VDE Digest: European Industrial Vendor Advisories
CERT@VDE digest for European industrial vendors we had not yet covered: Phoenix Contact, Pilz, Welotec, Endress+Hauser, VEGA, METTLER TOLEDO STARe, Bender EDGE500IP, DURAG, non-PHP2Shell WAGO, and older CODESYS Gateway/Control. Match products to your inventory and apply each advisory fix.
Read the advisory →

November 19, 2026
Industrial Ransomware Still Stops Plants Through Enterprise IT
Dragos counted 1,140 industrial ransomware incidents in Q2 2026, mostly manufacturing, with no direct control-system manipulation observed. Harden edge devices and remote tools, separate OT accounts, and test restores for historians and virtualization hosts.
Read the advisory →

November 19, 2026
AI-Assisted Intrusion Tried a Water Utility OT Gateway
Dragos describes an AI-assisted intrusion at a Monterrey municipal water utility (TAT26-12 / MITRE C0064). After an IT breach, AI tools found a vNode SCADA gateway and tried password spraying. No OT access was confirmed. Harden gateway logins and IT-to-OT segmentation now.
Read the advisory →

November 19, 2026
Schneider EcoStruxure Power Build Rapsody Project File Flaw
Schneider SEVD-2026-314-01: EcoStruxure Power Build Rapsody CVE-2026-119055 is a use-after-free via a crafted SSD project file. Update to the fixed locale builds and open only trusted project files.
Read the advisory →

November 19, 2026
Siemens Mendix SAML Flaw Can Hijack SSO Sessions
Siemens SSA-887643: Mendix SAML CVE-2026-80465 can let an attacker hijack an SSO session. Update to SAML V4.2.4 (Mendix 10/11) or V3.6.29 (9.24). Earlier V4.2.3/V3.6.27 builds were incomplete.
Read the advisory →

November 19, 2026
ScadaBR Authenticated Code Execution With No Vendor Fix
Tenable TRA-2026-46: ScadaBR 1.2.0 has authenticated remote code execution (CVE-2026-9645, CVSS 9.9) with no vendor fix. Inventory it, pull it off the internet, and plan a migration to supported SCADA.
Read the advisory →

November 19, 2026
Ignition Vision Session Can Escalate to Designer on the Gateway
CISA ICSA-26-286-01: Ignition CVE-2026-92817 lets a Vision user escalate to Designer and run code on the Gateway. Update to 8.1.55 or 8.3.9, separate Vision from Designer access, and review Gateway audit logs.
Read the advisory →

November 19, 2026
Apache Axis and Rails Flaws Hide Inside Plant Web Portals
Apache Axis 1.x (CVE-2026-90436, on the CISA KEV catalog) and Rails Active Storage (CVE-2026-66066) are being exploited. Both hide inside plant and vendor web portals. Migrate off Axis 1.x, patch Rails to the fixed Active Storage builds, and pull exposed portals off the internet.
Read the advisory →

November 19, 2026
NGINX2Root: F5 Out-of-Band Fix for Hidden Plant Web Front Ends
F5 released an out-of-band NGINX update on 18 November 2026 fixing the NGINX2Root remote code execution flaws, including CVE-2026-123007 in HTTP/2. Upgrade Open Source to 1.30.7 or 1.31.9, or Plus to 37.0.8.1 or 37.3.0.1, and ask vendors which NGINX their plant web front ends embed.
Read the advisory →

November 19, 2026
PHP Security Releases Fix Code Execution Flaws Hiding in Plant Web Servers
PHP released security updates 8.5.13, 8.4.28, 8.3.37 and 8.2.36 on 19 November 2026, fixing more than a dozen flaws, including remote code execution bugs in php-cgi and session handling. PHP hides inside web-based operator screens, historian portals and gateways, so patch what you control and ask your vendors about the rest.
Read the advisory →

November 18, 2026
CISA Updates the Dams Sector Cybersecurity Maturity Model for 2026
CISA posted a 2026 update of its Dams Sector Cybersecurity Capability Maturity Model and Implementation Guide on 16 November 2026. The voluntary self-evaluation, built on Department of Energy C2M2 version 2.1, helps dam, levee, hydro and reservoir owners rate ten security domains across IT and control systems.
Read the advisory →

November 18, 2026
CODESYS Engineering Tools Can Be Fooled by a Fake Automation Server
CODESYS warned on 17 November 2026 of three flaws in the CODESYS Automation Server Connector and Service Tool, used to sync projects and set up Edge Gateways that link to plant controllers. A fake or intercepted server could run code on the engineering workstation or tamper with traffic. Update both to version 1.40.0.0.
Read the advisory →

November 17, 2026
Java4Shell (CVE-2026-114938): Critical Java Flaw Hides Inside OT Software
The Cybersecurity and Infrastructure Security Agency (CISA) urged immediate patching of CVE-2026-114938, "Java4Shell," a Java Virtual Machine (JVM) Base64 flaw that could allow remote code execution without a login. Oracle fixed it on 17 November 2026. Java hides inside many OT products, so find every runtime, patch from the outside in and check with your vendor.
Read the advisory →

November 17, 2026
Dorsett Controls InfoScan Water SCADA Flaws Give Away System Details
The Cybersecurity and Infrastructure Security Agency (CISA) warned on 17 November 2026 (advisory ICSA-26-321-01) of six vulnerabilities in Dorsett Controls InfoScan, a supervisory control and data acquisition (SCADA) system used by water and wastewater utilities. Versions 1.45.0 and earlier give away user, firmware and network details. Update to 1.46, close internet access and turn on multifactor authentication.
Read the advisory →

November 17, 2026
GeoVision Camera Servers Hit by Cryptomining Attacks Through WebCam Server
GeoVision warned on 12 November 2026 that attackers are breaking into internet-facing GV-VMS video management servers through the WebCam Server feature and installing cryptocurrency miners. Install the fixed builds (V20.1.3, V18.3.5.25 or V17.4.8.65), take WebCam Server off the internet and check for signs of compromise.
Read the advisory →

November 17, 2026
CIRCUTOR PowerStudio SCADA WAVE Flaw Lets Anyone Sign In as Administrator, Rated 10.0
CIRCUTOR published CVE-2026-120387 on 17 November 2026, a critical flaw rated 10.0 in its PowerStudio SCADA WAVE energy monitoring software that lets anyone who can reach the server sign in as any user without a password. Upgrade to version 24.11.17.0 or later and keep the server off the internet.
Read the advisory →

November 16, 2026
OT Vendors Are Moving to the Cloud: Know What Your Plant Depends On
Microsoft's 12 November 2026 outage is a reminder to ask what in your plant now depends on someone else's cloud. A review of 11 major OT vendors found that all 11 now sell a cloud-hosted or software-as-a-service version of a product that used to run only on plant servers.
Read the advisory →

November 13, 2026
FBI Warns of ARTEX, an AI Attack Engine Now Aimed at Energy and Manufacturing
The FBI warned on 13 November 2026 that a variety of attackers are using ARTEX, an AI agent tool that runs most of an intrusion on its own, against energy, manufacturing and other sectors. Lock down vendor portals and remote access around your plants and make sure someone watches them 24x7.
Read the advisory →

November 13, 2026
Check Point Firewalls Hijacked Through PHP2Shell and a New Root Flaw, Some Attacks Destructive
Check Point confirmed on 12 November 2026 that attackers took over a couple of dozen unpatched Check Point Security Gateways by chaining PHP2Shell with a new Gaia root flaw, CVE-2026-123039, and some attacks turned destructive. Install the November Jumbo Hotfix, starting with internet-facing gateways that run the Mobile Access Portal.
Read the advisory →

November 13, 2026
Citrix NetScaler: Ten Critical Fixes for Plant Remote Access Gateways
Citrix fixed 28 flaws in NetScaler ADC and NetScaler Gateway on 12 November 2026, nine of them critical, plus a critical sign-in bypass in NetScaler Console. None is known to be exploited yet. If a NetScaler Gateway is how vendors and engineers reach your plant, patch the internet-facing ones first.
Read the advisory →

November 12, 2026
Copeland XWEB EVO: Refrigeration Supervisor Flaw Exploited Within Hours, and No Patch Is Coming
VulnCheck disclosed 14 flaws in the end-of-support Copeland XWEB EVO refrigeration supervisor on 12 November 2026, and saw one, CVE-2026-124014, attacked within two hours. Copeland will not patch it. Take every XWEB EVO off the internet now and plan its replacement.
Read the advisory →

November 12, 2026
Apache HTTP Server CVE-2026-119618: Critical HTTP/2 Flaw Fixed in Version 2.4.71
Apache released HTTP Server 2.4.71 on 11 November 2026 to fix CVE-2026-119618, a critical flaw in the HTTP/2 module that can let an attacker who reaches the server run code without logging in. Versions 2.4.55 through 2.4.70 with HTTP/2 turned on are affected. Upgrade, or switch off HTTP/2 until you can.
Read the advisory →

November 12, 2026
Exposed VNC on HMI Panels: Group-IB's DarkLunnen Files Show 14 Months of Attacks on Europe
Group-IB recovered working files from an operator it calls DarkLunnen, covering 14 months of attacks on Europe. A VNC password-guessing campaign mostly hit Ukrainian and Polish addresses, and about a quarter of a 945-entry log returned HMI desktop names after login. Take VNC off the internet, check FortiGate devices for an unexpected "service" admin, and book an OT assessment.
Read the advisory →

November 12, 2026
Danfoss AK-SM800A: Six Unpatched Flaws in Refrigeration Controllers While Attacks Continue
Belgium's Centre for Cybersecurity warned on 12 November 2026 of six unpatched flaws in the Danfoss AK-SM800A refrigeration controller, firmware up to 5.3.2, that need no login. Attacks on exposed fridge controllers continue across Europe. Take controllers off the internet now rather than waiting for a patch.
Read the advisory →

November 11, 2026
ScreenConnect MSP Campaign: Hijacked Support Sessions Push Rogue Remote Access
Attackers abused ConnectWise ScreenConnect at six MSPs on 11 November 2026, pushing a second, attacker-controlled remote access client to more than 286 endpoints across 47 organizations, per Huntress. Plants should ask every vendor about ScreenConnect, check OT and DMZ hosts, and lock down vendor remote access.
Read the advisory →

November 11, 2026
Beckhoff TwinCAT: Driver Flaws Let a Local User Take Over Controller and Engineering PCs
Beckhoff fixed three flaws (CVE-2026-18767, CVE-2026-18768 and CVE-2026-18769) in the TwinCAT TcRouter.sys Windows driver that let a local user with ordinary privileges take full control of the PC. Not exploited and not reachable over the network, but update TwinCAT controller and engineering PCs.
Read the advisory →

November 10, 2026
Fortinet November 2026: Critical FortiOS Routing Flaw and FortiManager Console Fixes
Fortinet's November 2026 release fixes a critical FortiOS routing flaw (CVE-2026-126253) and critical FortiManager and FortiAnalyzer flaws, including unauthenticated code execution over the FortiGate to FortiManager (FGFM) management channel (CVE-2026-126261). None is known exploited yet; patch plant firewalls and consoles now.
Read the advisory →

November 10, 2026
PHP2Shell Reaches OT Remote Maintenance Portals and Industrial Routers
CERT@VDE published five PHP2Shell advisories on 10 November 2026 for MB connect line and Helmholz remote maintenance portals and Weidmueller and ads-tec industrial routers. The portals face unauthenticated code execution and twelve more Helmholz flaws. Update portals to 2.21.6 and routers to fixed firmware.
Read the advisory →

November 10, 2026
Siemens November 2026 Patch Day: PCS 7, WinCC and IoT2050 Flaws, Many Without Fixes
Siemens November 2026 Patch Day brings four control room advisories: an NTLM relay flaw across PCS 7, WinCC and historians, file-open code execution in WinCC Graphics Designer, Node2Shell across WinCC products and an IoT2050 firmware bug. Many have no fix yet, so apply the Siemens mitigations now.
Read the advisory →

November 10, 2026
France Attributes Refrigeration Controller Attacks to Iran's IRGC Unit Shahid Kaveh
France attributed the 11 to 12 October 2026 attack on refrigeration controllers at about 700 grocery sites to Shahid Kaveh, an IRGC cyber unit behind the CyberAveng3rs persona. Defrost setpoints were raised, causing losses and at least 15 fires. The unit has tooling for Schneider Electric, Siemens and Rockwell controllers.
Read the advisory →

November 9, 2026
Barracuda Confirms Exploitation of Email Security Gateway Root Access Chain
Barracuda updated its advisory on 9 November 2026 to confirm exploitation of CVE-2026-116606 and CVE-2026-111560 at a small number of organizations. Chained, the flaws give root on Email Security Gateway and other appliances. Verify patches, lock down admin interfaces and check for tampering.
Read the advisory →

November 9, 2026
OpenSSH Password Bypass CVE-2026-123158 Now Exploited: Check Embedded Linux in OT
CISA added the OpenSSH password bypass CVE-2026-123158 to its exploited list on 9 November 2026. It hits musl Linux builds without PAM, common in OEM gateways and edge boxes. Honeypots show active attempts. Get OpenSSH 10.6p2 firmware, turn off password logins and keep SSH off Levels 0 to 2.
Read the advisory →

November 6, 2026
SonicWall SSL VPN Flaw Lets Attackers Skip MFA, Now on CISA Exploited List
CISA added SonicWall CVE-2026-19868 to its exploited list on 6 November 2026. On SonicOS firewalls using SAML single sign-on for SSL VPN, a user with a valid password for another login method can skip SAML and its MFA check. Upgrade Gen7 and Gen8 firewalls that carry plant remote access.
Read the advisory →

November 5, 2026
US Agencies Urge Hardening of Industrial Refrigeration and Cold Chain Systems
CISA, FBI, HHS, USDA and DoT published a 5 November 2026 joint fact sheet urging owners to harden industrial refrigeration and cold chain monitoring systems amid global malicious cyber activity. Healthcare, chemical, food and agriculture, and transportation operators should take controllers off the internet, isolate OT, strengthen authentication and watch setpoints.
Read the advisory →

November 5, 2026
Don't be an SSHole: Block SSH into the Lower Levels of OT and Patch What Must Stay Exposed
OEM vendors often ship old OpenSSH, Dropbear or libssh builds inside controllers, RTUs, HMIs and gateways. Red Tiger Security advises blocking SSH into Purdue Levels 0 to 2, patching or getting fixed firmware wherever SSH must stay, routing it through a DMZ jump host with MFA, and inventorying SSH versions with vendor SBOMs.
Read the advisory →

November 5, 2026
PHP2Shell Hits WAGO Controllers and Festo Didactic: CERT@VDE Patch Paths
CERT@VDE published PHP2Shell advisories for WAGO controllers (CC100, Edge, PFC, TP600, WP400) and Festo Didactic FactoryViews and MES4. Patch WAGO to firmware 4.10.4 (FW32) or the FW31 IPK, update FactoryViews to 1.12.2, and mitigate MES4 with XAMPP. Why it matters and four steps for plant owners.
Read the advisory →

November 4, 2026
Zyxel GS1900 Switch Zero-Day Was Used to Break Into 996 Switches, and the June Patch Does Not Stop It
Zyxel fixed CVE-2026-107441, a zero-day in ten GS1900 managed switch models that attackers used to break into 996 switches and steal configs and passwords. The June patch does not stop it. Why it matters for plants and four steps to take.
Read the advisory →

November 4, 2026
Refrigeration Controller Attacks Reach France's Blood Supply
France's national blood service confirmed that attackers raised the temperature and defrost settings on cold rooms at three sites through a refrigeration supplier's remote monitoring system. Its own independent alarms caught it in time. Owners should inventory rented and vendor-managed equipment and add independent alarms.
Read the advisory →

November 4, 2026
SonicWall GMS Is End of Life: Two Flaws in the Firewall Management Console Will Never Be Patched
SonicWall says two flaws in its end-of-life Global Management System (GMS) 9.5.2 and earlier will never be patched, including a 9.1 critical file read that needs no login. Why GMS matters for plant firewalls, and four steps to isolate it and move to a supported manager.
Read the advisory →

November 3, 2026
Refrigeration Controller Attacks Reach the UK Food Supply Chain
Britain's National Cyber Security Centre confirmed on 3 November that the European refrigeration controller attacks reached the UK food supply chain, including meat suppliers hit through Copeland XWEB supervisors. Owners should check XWEB firmware, take controllers off the internet and make sure overnight alarms reach a person.
Read the advisory →

November 3, 2026
Subnet Solutions PowerSYSTEM Center Flaws Let a Low-Privileged User Act Like an Administrator
CISA has published an advisory for two flaws in Subnet Solutions PowerSYSTEM Center, software that utilities use to manage substation devices such as protective relays. Both let a low-privileged user act like an administrator. What is affected, the fixed versions, and four steps to take.
Read the advisory →

November 3, 2026
Barracuda Patches Two Flaws That Chain to Root on Email Gateways and Web Application Firewalls
Barracuda has patched two flaws that can be chained to take full control of its Email Security Gateway and other appliances, including its Web Application Firewall. Which products and patches apply, why the admin page matters, and four steps to check your sites.
Read the advisory →

November 3, 2026
Attackers Exploit Critical Node-RED Flaw CVE-2026-58115 on Siemens IoT2050 Gateways
Attackers are exploiting CVE-2026-58115, a critical flaw that lets anyone run commands through an unprotected Node-RED editor on Siemens IoT2050 gateways, and they are scanning for any Node-RED left without a login. Where Node-RED hides in plants, the fixed version and four steps to lock it down.
Read the advisory →

November 2, 2026
Axis Camera Station Flaws Let Attackers Take Over Video Servers and Camera Passwords
A penetration tester showed how two patched flaws in Axis Camera Station let him take over the video servers in a factory, then a third, newly fixed weakness exposed the passwords for every camera they managed. Plants should update to Camera Station Pro 6.20, put the video system on its own network segment and check whether it shares a domain with control systems.
Read the advisory →

November 2, 2026
Refrigeration Controller Attacks Spread to More Than 115 Stores in Six European Countries
Attackers changed temperature settings or triggered defrost on refrigeration systems at more than 115 stores in six European countries overnight on 1 to 2 November. Owners of networked refrigeration and building controllers should take them off the internet, secure contractor access and set overnight alarms.
Read the advisory →

November 2, 2026
Synology Warns of Ransomware Attacks on NAS Devices Running Outdated DSM Versions
Synology warns that ransomware is encrypting NAS devices on outdated DSM versions through a flaw patched in December 2024. Plants that keep control system backups and project files on these boxes should update, take them off the internet and keep an offline copy.
Read the advisory →

October 30, 2026
Critical Linux Kernel Flaw CVE-2026-98432 Can Let an Attacker Crash or Take Over Linux Systems That Accept Network Connections
A critical Linux kernel flaw, CVE-2026-98432, can let an unauthenticated attacker crash or possibly take over Linux systems that accept network connections. Where Linux hides in plants, patch status by distribution, and four steps to take.
Read the advisory →

October 30, 2026
TeamViewer Fixes a Flaw That Lets a Compromised Remote Computer Attack the Engineer Who Connects to It
TeamViewer fixed CVE-2026-111585, a flaw that lets a compromised remote computer attack the engineer who connects to it. Update clients and Hosts to 15.83 or the fixed legacy builds. Why it matters for plant remote access and four steps to take.
Read the advisory →

October 29, 2026
Ivanti Fixes the Root Flaw in an Exploited Connect Secure VPN Attack Chain, So Sites That Patched on 13 October Must Patch Again
Ivanti fixed the root escalation flaw in the Connect Secure VPN zero-day chain exploited since early October. Sites that patched on 13 October must upgrade again to 25.1.1.3 or 22.8R2.6. Why it matters for OT remote access and four steps to take.
Read the advisory →

October 29, 2026
Hitachi Energy Fixes Flaws in CoreTec Transformer Monitors and TRO600 Wireless Mesh Routers
Hitachi Energy fixed four flaws in its CoreTec transformer monitors and TRO600 wireless mesh routers, including one that lets anyone read router files and passwords without logging in. What is affected, why it matters at the grid edge, and four steps to take.
Read the advisory →

October 29, 2026
Attackers Exploit PHP2Shell on Internet-Exposed Palo Alto Firewall and Panorama Management Pages
Palo Alto Networks confirms attackers are exploiting the PHP2Shell flaws against firewall and Panorama management pages exposed to the internet. What is affected, the fixed hotfixes, why signatures are not enough, and four steps for plant and remote site firewalls.
Read the advisory →

October 29, 2026
KeyDrift: Malware on Cisco SD-WAN Controllers Built to Steal Encryption Keys, Tied to Volt Typhoon's Silent Train Network
Cisco Talos found KeyDrift malware on Cisco SD-WAN controllers, built to stay hidden and copy the keys that protect links between sites. What is new since the Silent Train report, why a patch alone is not enough, and five steps for OT owners.
Read the advisory →

October 29, 2026
Cisco Firewall VPN Zero-Day Lets Attackers Knock ASA and FTD Firewalls Offline Without a Login
Cisco fixed an exploited zero-day in its ASA and FTD firewalls that lets an attacker with no password force the remote access VPN to reload. Why that matters for plants and remote sites that depend on these firewalls, who is exposed, and five steps to take.
Read the advisory →

October 28, 2026
PHP2Shell Plus Fragnesia: CISA Confirms Firewall Takeover Chain
CISA added the Linux kernel flaw Fragnesia (CVE-2026-46300) to its exploited list after attackers chained it with PHP2Shell to take full control of internet-facing firewalls. What plant owners should check, and four steps to take this week.
Read the advisory →

October 28, 2026
FortiBleed 2.0: Check Your Plant Firewalls Again
A second batch of stolen FortiGate firewall configuration files, called FortiBleed 2.0, exposes VPN users, Active Directory service accounts and admin logins for devices not in June's list. What plant owners should check again, and four steps to take.
Read the advisory →

October 28, 2026
Volt Typhoon's "Silent Train" Hides Attacks on Edge and Management Systems Behind Hacked Home Routers
Lumen's Black Lotus Labs says China's Volt Typhoon hid zero-day attacks on network management platforms behind rotating chains of hacked home and small-office routers, with water, energy and maritime victims. What it means for plant owners, and four steps to take.
Read the advisory →

October 28, 2026
Sungrow iSolarCloud Flaw and the EU's 1 November Deadline for High-Risk Inverters
A login flaw in Sungrow's iSolarCloud, fixed in August, could have reached about 250,000 solar systems in Germany, and the EU's 1 November 2026 cutoff for high-risk inverters in EU-funded projects is days away. Here is what cloud-controlled inverters mean for plant owners, and four steps to take.
Read the advisory →

October 28, 2026
IT Outage at the Fehmarnbelt Tunnel Contractor Idled Vessels and Site Access
A cyberattack on the office IT systems of Femern Link Contractors, the consortium building the Fehmarnbelt tunnel, idled vessels and stopped badge access in October 2026, and data was stolen. Here is what the IT to operations dependency means for plants, ports and terminals, and four steps to take.
Read the advisory →

October 27, 2026
GoAhead Embedded Web Server Flaws Fixed in 6.1.1: What OT Owners Should Ask Their Vendors
Embedthis fixed eleven flaws in the GoAhead embedded web server in version 6.1.1, including a 9.8 login bypass and a 9.1 flaw that lets revoked client certificates keep connecting. GoAhead is built into the web pages of devices from many OT vendors, and owners cannot patch it themselves. Here is what is affected, where it hides in the plant, and what to ask your vendors now.
Read the advisory →

October 27, 2026
Pro-Russia Hacktivists Are Causing Physical Damage Through Exposed Operator Screens
Bloomberg reports that pro-Russia hacktivists are causing physical damage in North Atlantic Treaty Organization countries, including stopped crematorium ovens, a factory fire and rising temperatures at two wineries in Spain. A joint advisory says these low-skill groups reach operator screens through exposed remote access with weak passwords. Here is what it means for smaller plants and four steps to take.
Read the advisory →

October 27, 2026
Brotli Flaw CVE-2026-111497 Added to CISA's Known Exploited Vulnerabilities Catalog: Where It Hides, Plant to Cloud
CISA added the Google Brotli decoder flaw CVE-2026-111497 to its Known Exploited Vulnerabilities catalog on 27 October 2026, with a federal due date of 10 November. We first covered it in the Node.js release. Brotli is built into many products, from gateways and web-based operator screens to engineering tools and cloud portals. Here is where it hides, which versions fix it and what to do now.
Read the advisory →

October 27, 2026
Mitsubishi Electric ICONICS GENESIS64 and Related Products: Four Vulnerabilities, Fixes and Workarounds
CISA has republished Mitsubishi Electric advisory 2026-006 on four vulnerabilities in ICONICS GENESIS64 and related supervisory control and data acquisition (SCADA) software, rated up to 9.1 out of 10. Most rely on administrator accounts and logins. Fixes are out for current versions, but MC Works64, GENESIS32 and BizViz will not be patched. Here is what is affected, where it runs in your plant and what to do now.
Read the advisory →

October 27, 2026
Blue Initiative: A Free Maritime Vulnerability Database for Ships and Ports
Cydome, ClassNK, Bureau Veritas, MTS-ISAC and Rakuten Maritime launched Blue Initiative, a free database of vulnerabilities that affect ships, ports and offshore facilities. It held nearly 30,000 entries at launch, including 588 known to be exploited and 37 in maritime-specific products. Here is how port, terminal and vessel owners can use it alongside their own asset inventory and Coast Guard Cybersecurity Plan.
Read the advisory →

October 26, 2026
PHP2Shell Added to CISA's Known Exploited Vulnerabilities Catalog: What OT Owners Should Do Now
On 26 October 2026 the Cybersecurity and Infrastructure Security Agency added both PHP2Shell flaws, CVE-2026-109618 and CVE-2026-109619, to its Known Exploited Vulnerabilities catalog, gave federal agencies until 29 October and flagged both for forensic triage. PHP is built into OT vendor products from Schneider Electric, ABB, B&R and Siemens. Here is what plant owners should patch, isolate and check first.
Read the advisory →

October 26, 2026
CISA 2030 Strategy: What Defend, Harden, Prevail Means for OT Owners
The Cybersecurity and Infrastructure Security Agency released CISA 2030: Defend, Harden, Prevail on 26 October 2026. It is a strategy, not a regulation, but it names operational technology asset visibility, anomaly detection and supply chain integrity as key objectives. CISA plans a services review by about late December 2026, an implementation plan by late April 2027 and a progress report by late October 2027. Here is what it means for plant owners and vendors.
Read the advisory →

October 26, 2026
SOEM EtherCAT Master: Six Vulnerabilities Fixed in Version 2.0.1
RT-Labs has disclosed six vulnerabilities in SOEM, the open-source EtherCAT master library used in motion control, robotics, test rigs and PC-based industrial controllers, affecting every version before 2.0.1. Each one is triggered by a malicious or compromised device on the same EtherCAT network, and the worst can crash the master or let an attacker run code on it. Here is what is affected, how the fix in SOEM 2.0.1 reaches you, and what to do now.
Read the advisory →

October 26, 2026
Asia-Pacific OT Cyber Rules: What Is in Force and What Is Coming
A new Asia-Pacific policy report from OT-ISAC separates the operational technology security rules already in force from those with a start date coming and those still in draft. Japan's unified critical infrastructure standards took effect on 1 October 2026, Taiwan's control system baseline starts on 1 January 2027, and India's power-sector cyber regulations generally take effect on 1 April 2027. Here is what changed and what plant owners and vendors should do next.
Read the advisory →

October 26, 2026
Mimori Ransomware Research Shows Attackers Going After vCenter, ESXi and Backups
The Atos Threat Research Center secured an exposed workspace of the new Mimori ransomware group with more than 3,100 files. It shows operators going after Active Directory, VMware vCenter and ESXi, and backup systems, with a critical vCenter flaw (CVE-2026-59310) playing a major role. Plants that run control system servers, operator screens and historians as virtual machines should patch vCenter, isolate its management network and protect their backups.
Read the advisory →

October 24, 2026
Researchers Show Encryption Alone Does Not Protect Cloud-Hosted SCADA Traffic (ICS-Sniper)
University of British Columbia researchers showed that an adversary controlling one internet router between a plant and its cloud-hosted supervisory control and data acquisition (SCADA) system could disrupt a simulated water treatment process by reading only the timing and size of encrypted VPN traffic and dropping a few well-timed packets. It is lab research with nothing to patch, but it shows why sites need safe local control and a second network path.
Read the advisory →

October 24, 2026
PHP2Shell Reaches the Substation Firewall: Siemens RUGGEDCOM APE1808 Running PAN-OS
Siemens confirms that every RUGGEDCOM APE1808 running Palo Alto Networks PAN-OS 10.2 through 12.2 is affected by the PHP2Shell flaws (CVE-2026-109618 and CVE-2026-109619), which puts the remote code execution risk inside the firewall that protects substations and industrial sites. Here is what is affected, when hotfixes are due, and what to do while you wait.
Read the advisory →

October 23, 2026
PHP2Shell Reaches OT Products: Schneider Electric and ABB Bulletins
Schneider Electric and ABB have confirmed that the PHP2Shell flaws (CVE-2026-109618 and CVE-2026-109619) affect OT products, including EcoStruxure Security Expert, ProLeiT LINEoptimize, EcoStruxure Control Engineering (no fix yet), ABB MES with DokuWiki and B&R APROL. Here is what is affected, what is fixed, and what plant teams should do this week.
Read the advisory →

October 23, 2026
Actively Exploited VeloCloud SD-WAN Orchestrator Flaw Added to CISA KEV
An actively exploited SQL injection in on-prem VeloCloud SD-WAN Orchestrator (CVE-2026-114625, CVSS 9.9) lets any authenticated user, even read-only, gain superuser operator rights. CISA added it to KEV on 23 Oct with a 26 Oct due date. Utilities, pipelines and multi-site plants that link remote sites over SD-WAN should patch, restrict access and hunt for compromise.
Read the advisory →

October 23, 2026
AVEVA Investigating Unauthorized Access to Corporate SharePoint; Software Unaffected
AVEVA says it is investigating unauthorized access to its internal corporate SharePoint (bulletin AVEVA-2026-007) and that its software and production environments are separate and not affected. The bulletin follows an unverified 20 Oct leak-site claim by a new group calling itself Mimori. Review what your team has shared with OT vendors and rotate shared credentials.
Read the advisory →

October 23, 2026
Loxone Cyberattack: Building Automation Vendor's CRM Breached, Installations Unaffected
Building automation maker Loxone detected an attack on its internal CRM and applicant systems on 18 Oct 2026; a group calling itself Samurai claims about 200 GB. Loxone says Miniservers, Remote Connect and Exosphere were not affected, and it warned partners who had sent installation passwords in plain text. Rotate any controller credential ever shared with a vendor.
Read the advisory →

October 23, 2026
n0n Extortion Group Lists 38 Maritime Organizations, Possible Shared Software Provider Archive (Cydome)
n0n data extortion group listed 38 maritime organizations in 18 countries on 12 Oct 2026 with about $1.22bn in demands. Cydome's unconfirmed interim assessment points to a single support archive at a shared maritime software provider. Port and terminal owners should ask vendors what they hold, rotate credentials shared with vendor support and review vendor remote access into OT.
Read the advisory →

October 22, 2026
MITRE ATT&CK v20: What Changed for ICS and What to Remap
MITRE ATT&CK v20 replaces the deprecated ICS techniques T0807 Command-Line Interface and T0853 Scripting with T1701 Command and Scripting Interpreter and its six sub-techniques, adds T0869.001 DNS and T0869.002 Publish/Subscribe Protocols for command and control, and adds the C0066 U.S. water utilities and C0064 Mexico IT/OT campaigns, CyberAv3ngers' IOControl malware, and 15 new detection strategies with 38 analytics. Asset owners, SOC teams and NERC CIP and IEC 62443 programs should remap detections and crosswalks to the new IDs, baseline DNS and pub/sub traffic in OT zones, and tune the new ICS analytics against engineering and maintenance activity.
Read the advisory →

October 22, 2026
CERT-FR Warns of Active Campaign Against Internet-Exposed Refrigeration Controllers
France's CERT-FR (alert CERTFR-2026-ALE-012, 12 to 16 October 2026) reports numerous compromises of internet-exposed Danfoss AK-SM and AK-SC refrigeration controllers and Copeland and Dixell xweb supervisors, with campaigns probably still ongoing. Owners should remove internet exposure, move contractor access behind a VPN, check setpoints and defrost schedules, apply vendor hardening and replace end-of-life units.
Read the advisory →

October 22, 2026
Storm-0940: China-Linked Actor Tied to ConnectWise Cloud Backup Supply Chain Attack (Microsoft)
Microsoft Threat Intelligence (21 Oct 2026) attributes the ConnectWise Cloud Backup supply chain compromise to China-state aligned Storm-0940, which used the agentic AI framework ARTEX to attempt sign-ins to 2,250+ downstream Microsoft 365 tenants. OT owners should check which MSP and backup connections reach plant systems and keep affected ConnectWise connections disabled.
Read the advisory →

October 22, 2026
Summer 2026 OT/IoT Threat Trends: Credentials Still the Way In, PLC Severity Rising
Nozomi Networks Labs' summer 2026 OT/IoT trends (12 Oct 2026): credential-related techniques were roughly a third of detections, Manufacturing led targeted sectors with Energy, Utilities and Waste now third, and HIGH or CRITICAL OT vulnerabilities rose from 48% to 58%. Fix default credentials and bridge the PLC patch gap.
Read the advisory →

October 22, 2026
AA26-281A: China-Based Integrity Tech Enabling PRC-Linked Actors Against Critical Infrastructure
Joint advisory AA26-281A (CISA, FBI, NSA and partners, 8 Oct 2026) names China-based Integrity Technology Group as an enabler of PRC-linked actors whose tactics match Flax Typhoon, Ethereal Panda and Red Juliett. OT owners should lock down edge devices, patch the listed CVEs and hunt with the IOCs.
Read the advisory →

October 22, 2026
CISA Republishes 17 Siemens ICS Advisories: What to Mitigate Now and What to Patch Next
On 22 October 2026, CISA republished 17 Siemens ICS advisories (ICSA-26-295-02 through -18). Only Siemens Software Center (CVE-2026-110936) is on the KEV list. The S7-1500 PLC web server flaws (CVSS 9.6) and the S7-1500 MFP Linux subsystem issues (CVSS 10) have no fix yet, so asset owners should disable unused web servers and restrict access now, then schedule available fixes for RUGGEDCOM CROSSBOW, WinCC, SIMATIC IPCs and Industrial Edge.
Read the advisory →

October 22, 2026
CIP Security Certified to IEC 62443-4-2 at SL-C 3: What It Means for EtherNet/IP Plants
On 22 October 2026, TÜV Rheinland certified ODVA's CIP Security specification, the TLS/DTLS-based security extension for EtherNet/IP and the Common Industrial Protocol, as meeting IEC 62443-4-2 at Security Level Capability 3. The certificate covers the specification, not individual products, and does not establish EU Cyber Resilience Act compliance on its own. Asset owners should still ask for product-level certificates and plan key management before enabling it.
Read the advisory →

October 21, 2026
USCG NVIC 02-26: The Coast Guard's Playbook for MTSA Cyber Rule Compliance
On 20 October 2026 the U.S. Coast Guard released NVIC 02-26, its compliance guidance for the Marine Transportation System cyber rule (33 CFR Part 101, Subpart F, effective 16 July 2025). It covers the three items U.S.-flagged vessels, MTSA facilities and OCS facilities must have approved by 16 July 2027: a Cybersecurity Officer designation, a Cybersecurity Assessment and a Cybersecurity Plan. Four enclosures give plan guidance, a sample CySO letter, penetration testing expectations for the five-year renewal (not required for the initial submission) and an optional NIST CSF risk-filtering method for scoping IT and OT.
Read the advisory →

October 21, 2026
Free OT Security Help for Small U.S. Utilities: Community Cyber Resilience Foundation Launches
On 20 October 2026, Accenture, Dragos and the SANS Institute launched the Community Cyber Resilience Foundation, a nonprofit offering OT security software, hardware, deployment services and SANS ICS/OT training at no cost to U.S. water, wastewater, electric and natural gas utilities under $100 million in annual revenue. Phase one is about $10 million for up to 500 utilities. It follows CISA's report of over 100 internet-exposed water systems targeted in July 2026, mostly through PLCs on cellular modems. Free tools help, but utilities still need to remove internet exposure, plan a plant-safe deployment, and name who responds to alerts.
Read the advisory →

October 21, 2026
FERC 2026 CIP Audit Lessons Learned: Registration Timing, Aggregated Control and AI Tool Access
FERC staff's 13 October 2026 report on FY2026 Commission-led CIP audits flags three lessons for electric utilities. New generation is being registered and evaluated under CIP-002-5.1a late because of misread Commercial Operation Dates. Affiliate and third-party control centers that aggregate control of several generators are being rated low impact when the aggregate meets medium. AI ("super intelligence") tools in CIP-networked environments need their access authorized, verified and revoked under CIP-004-7.
Read the advisory →

October 21, 2026
AI Models Are Learning to Plan OT Attacks: What Two New Studies Mean for Plant Defenders
Frenos research published 21 October 2026 found the three strongest frontier AI models built workable attack plans against industrial systems in roughly 90% of attempts across 16,980 tests. Booz Allen's October OT lab testing saw models move from perimeter compromise to control-zone actions in just over 16 minutes. Both were controlled lab and simulation tests; the response window for OT defenders is shrinking.
Read the advisory →

+1.877.387.7733

<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://www.pbcsnyc.com/post/daily-cybersecurity-briefing-november-27-2026 -->
<!-- fetched_at: 2026-11-28 07:12:26 -->
<!-- sha256: ac36b6517c1dc3693fcbdd57eebbf7bce59cf2514b0f0eca3ff117c1ddd00587 -->

Daily Cybersecurity Briefing — November 27, 2026

top of page

Search

Daily Cybersecurity Briefing — November 27, 2026

Friday, November 27, 2026

Coverage: Cybersecurity news from November 25–27, 2026 (prior to 7:00 AM EST).

ACTIVELY EXPLOITED VULNERABILITIES

CISA added 10 flaws to its KEV catalog on November 25, 2026. FCEB agencies must patch most by November 28, 2026 ; two exceptions (CVE-2026-133311, CVE-2025-41450) have a December 9, 2026 deadline.

Mitel MiCollab (AWV component, v10.3 and earlier) — 5 CVEs added:

CVE-2026-133275 (CVSS 5.3): Arbitrary file upload. FCEB deadline: Nov 28.

CVE-2026-133303 (CVSS 9.0): XML injection leading to arbitrary command execution. FCEB deadline: Nov 28.

CVE-2026-133311 (CVSS 5.9): Unauthorized access → information disclosure. FCEB deadline: Dec 9.

CVE-2026-133323 (CVSS 10.0): Command injection. FCEB deadline: Nov 28.

CVE-2026-133324 (CVSS 5.3): Authentication bypass. FCEB deadline: Nov 28.

Patch: MiCollab 10.3.0.18+. Accenture Apex Labs identified suspected zero-day exploitation including deployed web shells in an apparent AI-assisted data-theft campaign.

Vates Xen Orchestra:

CVE-2026-133469 (CVSS 9.8): Improper input validation — unauthenticated attacker crafts empty-JSON token to bypass auth and perform admin-level actions. Advisory: VSA-2026-062. Attacker C2: 91.211.251[.]112:8001. FCEB deadline: Nov 28.

HPE Juniper Session Smart Conductor/Router:

CVE-2026-103406 (CVSS 9.8): OS command injection as root via crafted salt minion ID. Juniper SIRT confirmed at least one malicious exploitation report. FCEB deadline: Nov 28.

Danfoss AK-SM 800A Series (refrigeration controllers):

CVE-2023-25914 (CVSS 8.8): Path traversal reads server files via XML interface. FCEB deadline: Nov 28.

CVE-2023-25915 (CVSS 9.9): Remote arbitrary command execution via improper input validation. FCEB deadline: Nov 28.

CVE-2025-41450 (CVSS 8.5): Improper authentication exposes internal IPs, usernames, and store names. FCEB deadline: Dec 9.

France attributed October 2026 attacks on retail refrigeration systems (700+ French supermarkets) to Shahid Kaveh (IRGC-affiliated, aka Cyber Aveng3rs / Cyber Isnaad Front). Paris prosecutors are pursuing arrest warrants.

Danfoss AK-SM 8xxA — UNPATCHED (CISA ICSA-26-328-03):

CVE-2026-129713 (CVSS 9.8): Stack-based buffer overflow in unauthenticated CGI handler → memory corruption, web server restart, possible code execution. No patch available. Affects v5.4.0 and earlier. Mitigation: network segmentation, VPN, enable Strict mode.

AutomationDirect C-More EA9 HMI Software (CISA ICSA-26-328-01):

CVE-2026-127280 (CVSS 7.8): Heap-based buffer overflow triggered by opening a malicious project file → crash or code execution. Affects v6.80 and earlier. Sectors: critical manufacturing, energy, water/wastewater. No patch available.

BREACHES

SAP (Nov 27): Attackers stole employee authentication tokens to copy and alter source code on GitHub. SAP suspended automated development ops and replaced signing keys. No customer data accessed confirmed as of Nov 27. Separate Gentlemen ransomware group listing may be unrelated. AI assistance in the attack is suspected but unconfirmed.

Colorado myColorado App (Nov 27): ~100,000 of 2.1M users potentially affected. Attackers accessed user-uploaded documents (govt IDs, vehicle registrations, insurance cards) via AWS environment. No payment data accessed. App remains offline; notifications begin Nov 27.

Hex Package Manager / hex.pm (Nov 23, disclosed Nov 27): Unauthenticated deserialization RCE (CVE-2026-129514, CVSS 10.0) exploited in 69 requests over 13 minutes. Potential exposure: email addresses, password hashes, 2FA secrets, audit logs. All users: change password, reset 2FA. Related: CVE-2026-124283 (Ash Framework), CVE-2026-133555 (db_connection), CVE-2026-130411 (flop).

FIFA (Nov 27): Confirmed cyberattack. Hackers claim 12 GB of internal files including personal and business information. FIFA says breach was 'limited.'

USDA: System used to pay farmers reportedly breached (NBC News).

McDonald's Japan: Disclosed mobile app database breach.

Bithumb (cryptocurrency exchange): Wider breach than initially reported; attackers had access for more than two weeks.

Container Store: Systems restored after attack. n0n ransomware group claimed responsibility and listed the company on its leak site.

Radware: Breached via exposed Cloud WAF management API. Customer cloud and SFTP credentials may be affected.

UK Department of Work and Pensions (DWP): Online services taken down after a cyberattack.

1Password: Breach disclosed per Daily Surveillance Briefing, Nov 27, 2026.

THREATS & POLICY

ARTEX Agentic AI Pentest Framework (Microsoft Threat Intel, Nov 25): Open-source AI-driven pentest framework released July 2026 (Chinese-language), removed from GitHub Oct 2026, now circulating as forks. State-sponsored actors using it: Storm-0940, Storm-3358, Onyx Sleet, Pearl Sleet, Crystal Typhoon, Salt Typhoon. One intrusion moved from GitHub-leaked client secret to Azure Key Vault in ~5 minutes. Storm-0940 recorded 151,000+ failed sign-ins peaking at 2,900/min. Detection: 'artex-enrich/*' and 'norma/*' user agents; Defender: 'Behavior:Win64/ArtexAI.'

CRPxO Ransomware (new, Windows): Double-extortion. Encrypted files: .crpx0 extension. Ransom notes: 'HOW TO RECOVER.txt' + .html. Deletes Volume Shadow Copies. Persistence: 'OneDrive Sync Maintenance' scheduled task. Lateral movement over admin shares. 50% discount offer within 24 hours, full price at 24-48 hours.

KeefStealer (Windows RAT/backdoor): Remote desktop, keylogging, clipboard capture, credential collection. C2: keef.cc. Mutexes: 'Lester_ec8fe2591727ab01' and 'cversions.3.m.' IOCs and YARA rules released by CYFIRMA.

COLD RELIC / Star Blizzard / SEABORGIUM / COLDRIVER: Espionage via spear-phishing and credential theft. Active targeting: UK, US, Ukraine, Germany, Poland, Israel. Exploiting CVE-2023-38831 (WinRAR) and CVE-2022-30190 (MSDT/Follina).

DOJ Operation Blackout: 800+ defendants in 400+ cases since March. FBI seized/restrained nearly $17 billion.

RansomwareHelp Co-Founder Charged: Juan Ricardo Palacio Escobar charged with 3 counts of wire fraud for buying decryptors cheaply from ransomware criminals and billing victims more.

EU Quantum Act (Proposed): European Commission proposal to accelerate post-quantum cryptography adoption, reduce reliance on foreign suppliers, target global quantum leadership by 2030.

Tanker Cyberattacks: Up to 50 ships carrying oil, LPG, and chemicals targeted in cyberattacks. US authorities investigating possible Iranian involvement (WSJ).

UK NCSC AI-Assisted Attack Guidance (Nov 24): Rise in AI-assisted automated probing of internet-facing services noted since September. Guidance: reduce attack surface, strengthen auth, retain logs, patch, apply least privilege.

Norway (PST): Russian intelligence reportedly mapping critical infrastructure.

Equinor (Norway): 4-day intrusion disrupted internal email after attackers exploited an Azure API Management flaw. Skagerak Energi also affected. No confirmed data theft.

Shahid Kaveh / Cyber Aveng3rs (IRGC): France linked group to attacks on European refrigeration systems affecting 700+ French supermarket chains. Paris prosecutors pursuing arrest warrants.

CLOUD & SAAS SECURITY

ChatGPT Sites Sensitive Data Exposure: Pluto security found 16,666 sites built with ChatGPT Sites; 12,830 publicly accessible. Confirmed sensitive data exposure at 27 organizations in manual review.

Azure AD / Entra ID — CVE-2026-41123 (reported): Alleged critical SAML token forgery vulnerability enabling MFA and Conditional Access bypass, granting Global Administrator access. Reported out-of-band patch Nov 25. NOTE: Some article details could not be independently verified — confirm against official MSRC guidance before acting.

Microsoft 365 Misconfigurations: Ongoing research highlights persistent misconfiguration risks creating hidden attack surfaces in M365 environments.

N-able MailAssure/SpamExperts — CVE-2026-134624: SSRF vulnerability (CVSS 9.3). Builds before 20261121.1943 affected. (Source: CYFIRMA; verify against primary advisory.)

LLMjacking via Cloud Credential Theft: Google/Mandiant report: single-day cloud charges exceeded $100K at some enterprises; cumulative charges reached $1M. 'LLM Mixers' sell stolen LLM access on underground markets for ~$60/month (e.g., Jet Night). CVE-2026-40217 (LiteLLM) enables privilege escalation. Grey-market relay service routes Claude Code and Codex CLIs through third-party servers (lookalike domain: vibe.aiok[.]me).

IDENTITY & AUTHENTICATION

Azure AD/Entra ID CVE-2026-41123 (see Cloud section): Alleged SAML token forgery bypassing MFA and Conditional Access, granting Global Administrator. Guidance: Require MFA for privileged roles, rotate service-principal secrets >90 days old, move to certificate credentials.

LLMjacking Session Hijacking: Actors use fake portals to capture OAuth/session tokens that bypass MFA, gaining access to cloud LLM services and API accounts.

Storm-0940 Credential Spraying (via ARTEX): Automated campaigns recorded 151,000+ failed sign-ins peaking at 2,900/minute against Microsoft environments.

Passkey Adoption Gap: Only 13% of SaaS apps allow admins to require passkeys as of 2026 (StartWithIdentity.com research).

Phishing-resistant MFA: CISA/NSA guidance remains: enforce phishing-resistant MFA (FIDO2/hardware keys) for all privileged accounts.

MOBILE SECURITY

Android Preinstalled Malware Surge (Kaspersky): Monthly malware detections in 2026 more than doubled year-over-year, with preinstalled malware on devices rising sharply.

43 Malicious iOS Apps: Appeared on the App Store requesting gallery scans to identify and steal sensitive information.

iVerify 2026 Mobile Threat Report: Spyware has 'gone mainstream' — no longer exclusively targeting journalists and activists but now deployed broadly.

iPhone Zero-Tap Spyware: Government-grade spyware actively infecting iPhones via malicious ads without any user interaction.

ICS/OT/IoT SECURITY

Danfoss AK-SM 8xxA — CVE-2026-129713 (CVSS 9.8): Unauthenticated RCE via stack-based buffer overflow in CGI handler. No patch. Supervisory controllers for food retail refrigeration, HVAC, and lighting. CISA ICSA-26-328-03. Mitigation: network segmentation, VPN, Strict mode.

AutomationDirect C-More EA9 — CVE-2026-127280 (CVSS 7.8): Heap buffer overflow from opening malicious project file → crash or code execution. Sectors: critical manufacturing, energy, water/wastewater. ICSA-26-328-01. No patch; handle project files from untrusted sources with care.

Osaki Electric Ransomware (Smart Meters, Japan): Detected Nov 17. Data exfiltrated from internal systems. Three production sites halted. Staged restart planned Nov 27. Qilin attribution unverified. May cause smart meter delivery delays.

Shahid Kaveh (IRGC) — Refrigeration Systems: France-attributed IRGC unit linked to Oct 2026 attacks against ICS/OT systems at 700+ French supermarket chains. Danfoss AK-SM 800A CVEs actively exploited.

FCC Cyber Trust Mark (IoT Labeling Program): Federal Register notice (Nov 23) proposes 3-year renewals and post-market surveillance for consumer wireless IoT devices. Comments due Dec 23, 2026; reply comments due Jan 7, 2027.

UK NCSC Alert: Rise in AI-assisted automated probing of internet-facing services including OT/ICS systems since September 2026. Urges: inventory internet-facing assets, reduce exposure, strengthen auth.

RESEARCH & TOOLS

VirusTotal Ransomware Detection Update: New behavior-based ransomware detection using evidence of file encryption during sandbox analysis. Caught ransomware missed by all 75 static AV engines at time of analysis.

CYFIRMA Threat Intelligence IOCs Released: YARA rule for KeefStealer Windows RAT (C2: keef.cc). Sigma rule for CRPxO ransomware vcruntime140 DLL sideloading behavior.

Accenture Apex Labs — Mitel Zero-Day Research: Identified web shell deployment and AI-assisted data theft campaign targeting Mitel MiCollab systems prior to vendor patch availability.

SolarWinds — Critical Serv-U Patches: Critical flaws patched. Apply immediately.

Adobe — Critical Patches: Critical vulnerabilities patched in Campaign Classic and Experience Manager.

Microsoft Deception Techniques: Honeytokens, honeypots, and tarpits reduced attack traffic reaching real assets in testing. Recommended alongside Conditional Access, managed identity, and automatic attack disruption in Defender XDR.

AI/ML SECURITY

Google: LLMs Launch Autonomous Cyberattacks: Google research demonstrates LLMs can build and launch cyberattacks from software patches without a human in the loop.

LLMjacking — $1M in Cloud Bills: Google/Mandiant: Actors steal cloud credentials and API keys to abuse enterprise LLM access. Single-day charges exceeded $100K; cumulative charges reached $1M. CVE-2026-40217 (LiteLLM, privilege escalation/RCE) actively exploited. Grey-market relay at vibe.aiok[.]me routes Claude Code/Codex CLI traffic through attacker infrastructure.

ARTEX Agentic AI Framework Abused by Nation-States: Microsoft documents Storm-0940, Salt Typhoon, Crystal Typhoon, Onyx Sleet, Pearl Sleet, and Storm-3358 using ARTEX for automated AI-driven penetration testing. Framework executes SQLi, SSTI, password spraying, Kerberoasting, web shell deployment, and Azure privilege escalation.

Claude Code / Codex CLI Relay Abuse: Symantec/Carbon Black documented a service that reconfigures genuine Claude Code and Codex CLIs to route through third-party servers, disabling sandboxing. Primarily targeting enterprises in mainland China and Asia.

NCS AI & Cyber Task Force (Nov 27): NCS mobilized global AI and cybersecurity specialists to help CISOs counter escalating AI-powered threats, including AI-generated phishing, deepfakes, and agentic attacks.

CVE-2026-40217 (LiteLLM): Privilege escalation and RCE in popular LLM routing middleware. Actively exploited in LLMjacking campaigns. Patch immediately.

Sources

The Hacker News - CISA 10 Exploited CVEs - https://thehackernews.com/2026/11/hackers-exploit-10-vulnerabilities.html

CISA KEV Alert - 10 Known Exploited Vulnerabilities - https://www.cisa.gov/news-events/alerts/2026/11/25/cisa-adds-10-known-exploited-vulnerabilities-catalog

SecurityWeek - SAP Cyberattack - https://www.securityweek.com/sap-confirms-cyberattack-source-code-reportedly-compromised/

SecurityWeek - Colorado Data Breach - https://www.securityweek.com/100000-potentially-impacted-by-colorado-data-breach/

SecurityWeek - Hex Package Manager Breach - https://www.securityweek.com/hex-package-manager-warns-of-potential-data-breach/

Security Affairs - FIFA Cyberattack - https://securityaffairs.com/204100/data-breach/fifa-confirms-a-cyberattack-hackers-claim-12-gb-of-internal-files.html

SecurityWeek - Tanker Cyberattacks, EU Quantum Act, VirusTotal - https://www.securityweek.com/in-other-news-tanker-cyberattacks-eu-quantum-act-new-virustotal-capabilities/

Microsoft Security Blog - ARTEX AI Framework - https://www.microsoft.com/en-us/security/blog/2026/11/25/what-defenders-need-to-know-artex-agentic-ai-framework-threat-actors-abuse/

The Hacker News - LLMjacking $1M Cloud Charges - https://thehackernews.com/2026/11/google-warns-llmjacking-attacks-are.html

The Hacker News - Google AI Agents Build/Run Exploits - https://thehackernews.com/2026/11/google-finds-hackers-using-ai-agents-to.html

CYFIRMA Weekly Intelligence Report - Nov 27, 2026 - https://www.cyfirma.com/news/weekly-intelligence-report-27-nov-2026/

Security Boulevard - Daily OT Security News Nov 25 - https://securityboulevard.com/2026/11/daily-ot-security-news-november-25-2026/

Neowin - UK DWP Cyberattack - https://neowin.net/news/uk-department-of-work-and-pensions-dwp-online-services-down-after-cyberattack

TrackFuture - Azure AD CVE-2026-41123 - https://trackfuture.ai/article/critical-azure-ad-zero-day-cve-2026-41123-mfa-bypass

Kaspersky - Android Preinstalled Malware 2026 - https://www.kaspersky.com/about/press-releases/kaspersky-warns-of-rising-android-preinstalled-malware-as-monthly-detections-in-2026-increase-more-than-twofold

ZeroHour - Daily Brief 2026-11-26 - https://zerohour.day/brief/2026-11-26

SC World - LLMs Launch Cyberattacks Without Human - https://www.scworld.com/news/google-llms-can-now-launch-cyberattacks-without-a-human-in-the-loop

Aviatrix ThreatsDay Nov 2026 - https://aviatrix.ai/threat-research-center/threatsday-250-rogue-extensions-10m-nginx2root-llmjacking-byod-ransomware-2026/

Izoologic - Weekly Threat Intelligence Nov 20-27 - https://izoologic.com/threat-advisory/weekly-threat-intelligence-report-20-to-27-november-2026/

Coverage period: November 24–26, 2026 (up to 7:00 AM ET). Sources include CISA, BleepingComputer, SecurityWeek, The Hacker News, ZeroHour, Shattered.io, DEV Community, and additional credible threat i

Thanksgiving Day coverage: a carried-over CISA KEV batch, an active Chrome zero-day and Xen Orchestra exploitation, a Black Friday/Cyber Monday phishing surge already up 82-103%, and holiday-weekend r

Wednesday, November 25, 2026 Top cybersecurity stories from the past 24–48 hours, covering through 7:00 AM ET on November 25, 2026. ACTIVELY EXPLOITED VULNERABILITIES CVE-2026-132165 | Drupal Core Rem

Post: Blog2_Post

bottom of page

<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://zerohunt.ai/blog/security-incidents-november-21-23-2026-tracker -->
<!-- fetched_at: 2026-11-25 07:12:46 -->
<!-- sha256: 09657c8e455b089e770e2c4c42a91459ea0872e2f606e3b6d9314e928d3645ce -->

N-able and MONAI on a 3-day KEV clock: Nov 21-23 tracker

Skip to content ← Blog Three days, three critical flaws on CISA's shortest clock, and a run of stories where the attacker is an AI agent rather than a person. Between November 21 and 23, CISA added both N-able Mail Assure and the MONAI Label medical-imaging server to the Known Exploited Vulnerabilities catalog with a three-day deadline and forensic triage required; a legacy ASP.NET anti-CSRF library turned out to be exploited for unauthenticated code execution with no patch to install; researchers confirmed months-long undetected theft of prompts — including some flagged "never store" — from inside AI inference providers; and India's CERT-In escalated a warning about AI-assisted attacks draining money through banks' own payment APIs. The common thread is not a single CVE. It is that automation is now on both sides of the breach, and the feeds are a wall of "critical" again. This page separates what is confirmed from what is not, and orders the fixes.

Developing story — first published 21:45 CET (20:45 UTC), November 23, 2026. Updated as vendors and CISA publish more.

Update — 2026-11-24 22:05 CET

CISA added the exploited ASP.NET bug to its catalog. CVE-2026-131914 (Idunno.AntiCsrf) was added to CISA KEV on 2026-11-24, due 2026-11-27, forensic triage required — the three-day tier. That makes three of this window's flaws on the shortest KEV clock, not two; the library is still defunct with no patch, so the required action is still to remove the module. NVD also finished its analysis: its own primary score for CVE-2026-131914 is now 9.8 (Mandiant, the CNA, scored it 9.3), and for N-able's CVE-2026-134624 NVD's primary score is 8.7 High against N-able's 9.3. No other row changed status; MONAI and N-able remain on KEV with a 2026-11-26 due date.

Patch today

Order by two questions: can an attacker reach it, and is it actually being exploited. These are the ones where both answers push them to the front of the queue this weekend.

MONAI Label — CVE-2026-133968 . An unauthenticated path-traversal-to-RCE (CVSS 9.8) in the open-source medical-imaging annotation server: a crafted image parameter to PUT /datastore/image writes a file outside the datastore, and from there to code execution. NVD now records it as exploited in the wild since September 2026 , and this is the zero-day that attacker-run AI agents found on their own (more below). The important change since our original write-up : a fix now exists. Upgrade to 0.8.6 — everything up to and including 0.8.5 is vulnerable. CISA added it to KEV on 2026-11-23 with a 2026-11-26 due date and forensic triage required — the three-day tier. In the default configuration the server runs with authentication disabled, so treat any internet-exposed instance as a priority.

N-able Mail Assure / SpamExperts — CVE-2026-134624 . A server-side request forgery (CVSS 9.3) in the LDAP synchronisation connection check performed when a relay is configured: an authenticated user with high-level API access can make the server open connections to arbitrary internal hosts and ports, map what is reachable, and send crafted data to internal services. N-able found it while investigating the breach of its Mail Assure and SpamExperts Hosted Cloud, the filtering service it runs for managed service providers. Fixed in build 20261121.1943 ; N-able restored dashboard and API access on November 21 and says it has found no evidence of exploitation beyond the one N-able-hosted server it already identified . CISA added it to KEV on 2026-11-23, due 2026-11-26, forensic triage required . Self-hosted SpamExperts operators: apply the build; hosted customers are patched but should still rotate (see below).

Idunno.AntiCsrf (ASP.NET) — CVE-2026-131914 . An unauthenticated deserialization RCE (CVSS 9.8 NVD; Mandiant scored it 9.3) in a legacy ASP.NET anti-CSRF module: the __CSRFTOKEN value is deserialized with ObjectStateFormatter before any validation and with no MAC, so a single request runs code in w3wp.exe — no machineKey needed. It is exploited in the wild and was added to CISA KEV on 2026-11-24, due 2026-11-27, forensic triage required — but there is still no patch : the project has been defunct since 2008, and rotating keys does not help. The only fix is to remove the module. Full removal-and-migration runbook in our write-up .

Verified incident tracker

Every row was checked against a primary source — a vendor advisory, the CISA KEV catalog entry, NVD, a named researcher's report, or the affected organization's own statement. ✅ confirmed · ⚠️ partly confirmed or contested · ❌ not supported by any source.

Incident
What it is
Status
Fix / action
Source

MONAI Label CVE-2026-133968
Unauth path-traversal RCE (9.8); exploited since Sept; KEV 3-day tier, forensic triage
✅
Upgrade to 0.8.6
NVD · our post

N-able Mail Assure CVE-2026-134624
Authenticated SSRF (9.3) found during a breach investigation; KEV 3-day tier
✅
Build 20261121.1943
NVD · N-able

Idunno.AntiCsrf CVE-2026-131914
Unauth deserialization RCE (9.8); exploited; no patch, defunct library; KEV 3-day tier (added 11-24)
✅
Remove the module
NVD · our post

AI inference prompt theft
Months of undetected theft at ≥3 providers; ZDR-flagged prompts and keys taken
✅
Rotate every secret ever in a prompt
our post

"CRAFTY FALCON" payment-API fraud
CERT-In: AI-assisted abuse of Indian banks' and fintechs' payment APIs
⚠️
Server-side revalidation; attribution unconfirmed
our post

Cairn AI agents find a zero-day
Autonomous agents found+exploited the MONAI bug after ~a day of failures
⚠️
Not a "swarm"; see below
AWS · our post

Rotate these secrets

Two of this window's incidents put credentials in reach, so patching alone does not close them.

Anyone sending prompts to a hosted AI inference provider. Dragos's canary research showed attackers read prompts — including some marked Zero Data Retention — from inside at least three providers for months, and in one confirmed case mined those prompts for live cloud keys. If any secret, token or connection string was ever placed in a prompt or in the context sent to a third-party model, treat it as exposed: rotate it, and reseed your own canaries so you find out faster next time. The full reasoning is in our prompt-leak analysis .

N-able Mail Assure / SpamExperts customers. The vulnerable path required an authenticated high-level API user, and the flaw surfaced during a breach of the hosted environment. Rotate API credentials for the Mail Assure / SpamExperts dashboard and any integration keys that touched it, and review which internal hosts those servers could reach while the SSRF was open.

What the viral threads got wrong

Three of this window's loudest claims ran a step ahead of the evidence.

"AI agent swarms are autonomously hacking everything." The MONAI zero-day was real and genuinely found by machines — but the record is narrower than the headline. Per Amazon Threat Intelligence , the agents (running the open-source Cairn framework, launched by a human operator with a target list) spent close to a full day failing — burning hours against Redis, trying Log4Shell and credential sprays — before they stumbled onto the MONAI Label flaw and got a foothold on one university server. That is a real and important capability shift, and it is why continuous testing matters; it is not a self-directed swarm breaking the internet overnight.

"N-able had a critical RCE exploited in the wild." CVE-2026-134624 is on KEV and deserves the three-day treatment — but it is an authenticated SSRF , not an unauthenticated RCE, and N-able has said it found no evidence the flaw was exploited beyond the single hosted server already in its investigation, and has not claimed code execution. It was found during a breach investigation; whether it was the attackers' entry point has not been confirmed. Patch it fast and rotate; do not conflate "found during a breach" with "the RCE that caused the breach."

"China is draining India's banks with AI." CERT-In's warnings about AI-assisted abuse of payment APIs are real and escalating, and the money loss is real. What is not confirmed is attribution or scale: the China link in public reporting points to where some of the tooling was written, not to who operated it, and no verified aggregate loss figure has been published. The useful part — validate that a technically valid transaction cannot clear without server-side revalidation — survives whoever is behind it. Our CRAFTY FALCON write-up keeps those lines separate.

"We patched everything on KEV." — "Including both three-day entries that landed today? And the exploited ASP.NET bug that just landed on KEV on its own three-day clock and has no patch, only a removal?"

How to prioritize when everything is critical

A window like this is what CISA's BOD 26-04 risk tiers are for: the shortest deadline is reserved for flaws that are both exploited and reachable, which is why all three — MONAI, N-able, and now the ASP.NET module — carry a three-day due date with forensic triage while an unexploited bug would sit at weeks. Order your own queue the same way — unauthenticated and internet-facing first (MONAI, and the ASP.NET module, which has no patch, only a removal), authenticated or internal next (N-able's SSRF) — and before you push a change, confirm the asset is actually reachable and the flaw is actually exploitable in your build. The CISA KEV tracker and a disciplined automated penetration testing pass against your own estate turn "everything is critical" into a ranked list you can actually work.

That ranking is where an autonomous red team earns its keep — and the MONAI and Cairn entries show why it has to be an AI one. The attacker here was an autonomous agent that mapped a live API and drove a vulnerable code path with no human in the loop; the only honest way to test the same surface is to run an autonomous offensive agent against your own systems first. Zero Hunt does exactly that as an on-premise appliance on its own private models, with a human approving every action that matters: a ten-agent swarm fingerprints your exact MONAI, mail-filter or ASP.NET build, proves black-box or gray-box which of this window's flaws is actually reachable and exploitable there, and its Remediation Advisor ranks the fixes by demonstrated exploitability rather than headline volume, re-verifying each one with the same test that found the hole. The prompt-theft story is the other half of the argument for keeping that engine on-premise: because its models run on the appliance and no prompt leaves the box, there is no reseller to off-board and no first hop to leak — the opposite architectural bet to the hosted inference chain that just lost months of "never store" prompts.

Is this exploitable in your environment?
Zero Hunt answers that on your own network: an autonomous AI red team on an on-premise appliance, running on private AI, black-box or gray-box, with a human approving every step that matters. Proof of what is exploitable, the fix, and signed evidence — your data stays on your network.
Request a demo How on-premise works
Not ready for a demo?
Book a 30-minute NIS2 / DORA / CMMC testing readiness call →
Get the autonomous pentest vendor evaluation checklist (PDF) →

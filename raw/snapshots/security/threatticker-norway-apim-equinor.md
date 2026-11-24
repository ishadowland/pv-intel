<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://threatticker.com/news/norway-warns-an-azure-api-management-flaw-was-exploited-against-equinor -->
<!-- fetched_at: 2026-11-25 07:34:11 -->
<!-- sha256: f6584fc521ad3b02178f3df1601091fd30514fbdc33224343de6610c3c7e5dd5 -->

Norway warns an Azure API Management flaw was exploited against Equinor, Skagerak Energi and other firms | ThreatTicker

Skip to content

At a glance

NSM says an unknown actor exploited a flaw in Azure API Management's older Classic tier to go after access tokens, secrets and named values, and that the issue is now closed
Equinor detected the attack on November 17 and said it was fully stopped by November 20, 2026, with production unaffected; Skagerak Energi also confirmed an incident
NSM tells every APIM owner to treat all secrets and named values as compromised, rotate tokens, and verify APIM RuntimeVersion is 0.52.x build 31936+ or 0.53.x build 31938+
Microsoft has not publicly acknowledged a CVE and has not named an attacker; its only on-record guidance so far is a November 21 Azure blog post on rotating APIM credentials

Norway's national security authority NSM said on November 20, 2026 that an unknown attacker exploited a vulnerability in Microsoft Azure API Management (APIM) to target "access tokens, secrets and named values" at several Norwegian and non-Norwegian organisations, including energy major Equinor and regional power producer Skagerak Energi. NSM updated its advisory on November 23 to say the underlying flaw should now be closed but still urged every APIM owner to act as if their secrets had been exposed.

Who is affected?

Both Equinor and Skagerak Energi confirmed intrusions in their own statements. Equinor's November 17 release says it "detected a cyber-attack" the same day at 18:55 CET; its November 20 update says "the cyber-attack against Equinor has now been stopped", production is running normally, and it has seen no indication that data was stolen or altered. Skagerak Energi, a majority Statkraft-owned electricity producer according to The Record, said in a Norwegian-language press statement that "the incident has not affected normal operations or production" and no evidence of data leakage has been found. NSM says the flaw hit "several Norwegian" and other organisations, without naming them.

What to do?

NSM asks every APIM customer to take the following steps even after the underlying flaw is closed:

Assume every secret and named value behind an APIM instance has been compromised. Rotate all tokens and secrets, and document what each APIM instance actually fronts.

Verify the APIM RuntimeVersion reported at https://<your-gateway-hostname>/internal-status-0123456789abcdef . Per NSM, builds 0.52.x are patched when the suffix is 31936 or higher, and 0.53.x when the suffix is 31938 or higher. V2 and Consumption tiers are not affected.

If the build is below those thresholds, contact the service provider that owns the APIM instance and escalate the fix.

Report any sign of compromise or compromise attempt to NSM. The agency says Norway's national cyber risk level is currently "HØYT" (high).

Microsoft has not published a stand-alone security advisory on this flaw. Its only public guidance so far is a November 21, 2026 Azure Integration Services blog post on Rotating credentials in Azure API Management , which walks through rotation steps for subscription keys, named values, backend credentials, OAuth and OIDC client secrets, Event Hubs connection strings, credentials embedded in policies, and legacy management access keys. The post pushes operators toward Azure Key Vault-backed named values and managed identities, but does not acknowledge the Norwegian incidents.

Technical details

Neither NSM, Microsoft, Equinor, Skagerak nor The Record has shared a CVE identifier, exploit chain or attacker group for this campaign. According to The Record, a non-public advisory that Microsoft sent to customers said the vendor discovered the APIM Classic-tier issue on November 18 and closed the access path the next day; the vendor's official blog does not confirm those dates. Equinor says the attack "was not specifically targeting" the company, which matches NSM's framing of an opportunistic hunt for APIM tokens and secrets. Neither Equinor's statement nor NSM's advisory ties the incident to a state-backed actor.

Background

Azure API Management is a widely used front door for APIs across Microsoft's cloud, so NSM's warning that "it is unclear how widespread this exploitation is" is significant: any tenant still on an older APIM Classic build is being asked to treat the gateway's named values and keys as leaked, not just the two Norwegian firms that confirmed intrusions.

Sources

NSM deler tiltak mot sårbarhet i Azure API Management — Nasjonal sikkerhetsmyndighet
Cyber-attack stopped - Equinor — Equinor
Oppdatering på forsøk på cyberangrep — Skagerak Energi
Rotating credentials in Azure API Management — Microsoft Tech Community
Norway says hackers exploited Microsoft security flaw to attack energy firms Equinor, Skagerak Energi — The Record

#Azure API Management #Equinor #NSM #Norveç #Skagerak Energi

Share

This story is based on the sources listed above. Always check the vendor’s official advisory before acting on critical systems.

Related news

Vulnerabilities High

SonicWall won't fix critical flaws in end-of-life GMS software

November 5, 2026

Breaches Medium

Turnitin tells customers it detected a cyberattack on its customer-facing systems

4h ago

Breaches High

KEPCO confirms cyberattack exposed data of 1.5 million customers, suppliers and employees

yesterday 01:13 AM

Breaches Critical

N-able patches critical Mail Assure SSRF CVE-2026-134624 found during a live Hosted Cloud breach investigation

yesterday 04:12 PM

<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: https://secnews.co.uk/2026/11/follow-up-equinor-azure-api-management-flaw-nsm-rotate-secrets -->
<!-- fetched_at: 2026-11-25 07:34:10 -->
<!-- sha256: c9c79974a7db3671126530e9ccb4c7d48d288040ecbdd2491867e72318130436 -->

Follow-up: Equinor attack linked to Azure API Management flaw - SECNEWS.co.uk

Skip to content

Security Operations

Secnews_Admin

November 23, 2026

Norway’s NSM links the Equinor and Skagerak incidents to an Azure API Management flaw and tells users to rotate all tokens and secrets.

Norway’s National Security Authority says a reportedly closed flaw in Microsoft’s Azure API Management affected several Norwegian organisations, and names Equinor and Skagerak Energi among them. Its advice to every APIM customer is blunt: assume your secrets are gone and rotate them.

What happened

When we covered the Equinor incident on 19 November, the Norwegian energy group had confirmed an ongoing attack on some of its IT systems. It said little about how. That gap has now been partly filled, though not by Equinor.

On 20 November, Norway’s Nasjonal sikkerhetsmyndighet (NSM) published an advisory on a vulnerability in Azure API Management (APIM), Microsoft’s managed service for publishing, securing and brokering APIs. NSM said it had learned of the issue earlier that week. It said the flaw had affected several Norwegian organisations and named Equinor and Skagerak Energi as among those hit. According to NSM, the weakness was first spotted by the Norwegian power sector. The authority praised Equinor for early detection and for sharing quickly with NSM and the sector response teams.

NSM says the vulnerability should now be closed but that customers still need to act. It also says the problem reaches several sectors, both inside Norway and beyond its borders. How widely the flaw has been exploited is still unclear. So far NSM has seen nothing to suggest that compromise, or attempted compromise, has disrupted deliveries at Norwegian organisations.

Equinor’s own timeline matches that picture without mentioning Azure. On 18 November it said the attack was not a virus and carried no risk of spreading. On 19 November it said the attack did not appear to be aimed specifically at Equinor. By the morning of 20 November it reported the attack had been stopped, with no sign that data had been stolen or altered and production running normally. Skagerak Energi had reported possible attempted attack activity a day after Equinor, again with no effect on operations or energy production.

The link to APIM comes from NSM. We could not find a CVE identifier or a Microsoft security advisory describing the flaw, and neither company has publicly described the attack in those terms.

The technical picture

NSM’s description is short. It says an unknown actor actively went after three kinds of material held in APIM: access tokens, secrets and named values. NSM has not published how the flaw worked, how the actor reached it, or what was done with anything taken.

The targets matter more than the mechanism. An API gateway is a broker of trust. It usually holds the subscription keys callers present, the credentials the gateway uses to reach back-end services, and policy configuration. Named values are the APIM feature for storing reusable settings, and many teams put connection strings, API keys and shared secrets in them. Anyone holding that material may be able to call back-end systems directly and skip the gateway’s controls altogether, without exploiting anything further.

NSM’s advisory also gives a practical way to check exposure. Administrators can read the RuntimeVersion from the gateway’s internal status page. On the 0.52 branch, a final build number of 31936 or higher is patched. On the 0.53 branch the threshold is 31938. NSM says instances showing other version patterns, which belong to the V2 and Consumption tiers, are not vulnerable to this issue. Anything below the thresholds should be treated as still exposed, and NSM tells those customers to contact their provider.

Why it matters for UK organisations

APIM is not a niche product. In the UK it commonly fronts public sector integration platforms, financial services APIs and the internal APIs that connect software-as-a-service to business data. NSM has said in terms that the flaw reaches outside Norway. We found no Microsoft statement on scope, but UK customers should not assume a Norwegian advisory means a Norwegian-only problem.

The sector also matters. UK and Norwegian energy firms share suppliers and North Sea joint ventures. Norway raised its national cyber risk level to HIGH in late October, citing a roughly threefold rise in successful operations against Norwegian organisations over six months. A cloud service flaw used against Norwegian energy companies is therefore relevant to UK operators of essential services and to the managed service providers that run Azure estates for them.

There is a regulatory angle too: if a stolen credential reached a back end holding personal data, UK GDPR and NIS reporting clocks may already be running.

Expert view

This is the pattern I expect to see more often: the vulnerability is in a platform the customer cannot patch, the provider fixes it quietly, and the customer is left holding credentials that may already be in someone else’s hands. Patching closes the door. It does nothing about keys that walked out before it closed.

When we test Azure estates, API gateways are one of the most reliable places to find long-lived secrets. Non-expiring back-end keys, shared partner subscription keys and plaintext connection strings in named values are routine findings. Rotation is usually painful because nobody has mapped which systems depend on which key, and that is exactly why NSM’s second instruction is to map what sits behind each instance.

The detail I would stress to SOC teams is that the logs that matter are probably not the gateway’s. If an attacker lifted a back-end credential, they will use it against the back end directly, from infrastructure you do not recognise. Hunting needs to happen at the destination services.

Caution is still warranted: with no public CVE or Microsoft guidance that we could find, act on NSM’s advice without assuming the full picture is known.

What to do now

Inventory every APIM instance. Include test and partner-facing gateways, and instances run by suppliers or MSPs on your behalf. Shadow instances are where unrotated secrets survive.

Check the runtime version against NSM’s thresholds (31936 on 0.52, 31938 on 0.53). Raise a support case with Microsoft for any instance below them, and record the answer.

Rotate on the assumption of compromise. Regenerate subscription keys, rotate back-end credentials and certificates, and replace any secret stored directly in named values. Where possible, move secrets into Key Vault references with managed identities. This maps to Cyber Essentials secure configuration and user access control.

Map the blast radius. For each instance, list the back-end systems and data it can reach. Prioritise anything holding personal data or supporting essential services.

Hunt at the back ends. Review sign-in and access logs for the services behind APIM for calls that bypass the gateway, unfamiliar source addresses or unusual volumes in recent weeks. Check Azure activity logs for unexpected reads of APIM configuration.

Prepare to report. If you find evidence of misuse, engage your incident response provider. Assess ICO and NIS obligations promptly, and share indicators with the NCSC.

Bottom line

NSM has linked the Equinor and Skagerak Energi incidents to a reportedly closed Azure API Management flaw. Its advice applies to anyone running the service: treat gateway secrets as exposed, rotate them, confirm the patch and hunt where stolen keys would be used. With no CVE or Microsoft advisory yet, UK teams should act on NSM’s guidance now rather than wait for one.

Sources

NSM: NSM deler tiltak mot sårbarhet i Azure API Management

Equinor: Cyber-attack stopped

TechRadar: Gas supplier giant Equinor hit by cyberattack

Borns IT- und Windows-Blog: Sicherheit-News zum 21. Nov. 2026

Related Posts

CERT-In’s Crafty Falcon alert: AI fraud crew targets weekend gaps

CERT-In's critical CRAFTY FALCON advisory shows AI-assisted fraudsters re-hitting payment firms at weekends. Lessons for…

November 8, 2026

Ransomware crews threatened staff in 40% of attacks, survey finds

Semperis finds 40% of ransomware attacks came with threats against staff, while identity systems were…

October 16, 2026

Dundee Scattered Spider hacker jailed for six years: SOC lessons

Scattered Spider's Tyler Buchanan gets six years in the US over a $11.6m SMS phishing…

November 18, 2026

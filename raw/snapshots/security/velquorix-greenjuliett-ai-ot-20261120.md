<!-- 原文快照 · 自动归档，请勿手工编辑 -->
<!-- source_url: http://velquorix.com/article/661 -->
<!-- fetched_at: 2026-11-23 09:43:46 -->
<!-- sha256: c7b6f4219902eab549d3ae4cfb87c4babf1df2e6cdee6c05a696a621b8df190e -->

The recent cyberattack on French refrigerators and our tracking of the malicious AI framework ARTEX show that threat actors are increasingly using AI to accelerate attacks, expand their reach, and improve their effectiveness. GreenJuliett, the group behind operational technology (OT) cyberattacks similar to those in France, has begun incorporating AI into its OT attack chain. Understanding the scale AI offers financially motivated and state-sponsored threat actors helps us see it as more than a tool: it’s something that can fill an operator’s role, even while humans remain in control.

On October 11 and 12, 2026, someone changed the defrost settings on refrigeration controllers at more than 700 retail locations in France. This resulted in fires, damaged equipment, and food losses estimated in the tens of millions of euros, highlighting the physical impacts of attacks against operational technology (OT). On November 9, France attributed the attack to Shahid Kaveh, a unit of Iran's Islamic Revolutionary Guard Corps Cyber Electronic Command (IRGC-CEC). We track activity that likely belongs to an element of Shahid Kaveh as GreenJuliett.
GreenJuliett (also known as CyberAv3ngers and Bauxite) builds infrastructure aimed at internet-facing PLCs. And while that work continued through at least October 30, despite repeated public reporting on the group, the target set began to widen. Between August and October, we observed GreenJuliett-linked infrastructure scanning, or attempting to exploit, Fortinet FortiGate firewalls, edge devices that protect OT networks, in Bahrain, Israel, Jordan, Kuwait, Saudi Arabia, and Qatar. Our network data suggests the group is also working to add internet-of-things (IoT) and CCTV devices to its list.
While we have not independently tied GreenJuliett infrastructure to the refrigeration attacks, over the past three months, we have seen the group continue to target PLCs (programmable logic controllers), which are similar to the internet-exposed controllers the refrigerators in France used. We have also observed that AI is now part of how they work.
From Accounts to Infrastructure
In October 2024, OpenAI banned accounts it assessed as belonging to CyberAv3ngers. The operators had used ChatGPT to research default credentials for PLCs, compile lists of electricity companies and common PLCs in Jordan, and draft scripts against industrial protocols (such as Modbus TCP, a control protocol that allows PLCs to communicate quickly on local networks).
However, in 2026, the picture is different. In October, we found a configuration for LiteLLM (an open-source gateway that puts multiple AI models behind a single interface, suggesting a team-sharing model for access), alongside self-hosted chat applications built for Persian-language users, on infrastructure we assessed as likely used by GreenJuliett-linked operators. We also observed servers in the group's anonymization network communicating with infrastructure that hosts Anthropic's Claude.
While we have not confirmed specific instances of misuse in this research, both OpenAI and Anthropic have reported publicly on detecting and disrupting misuse by Iranian government operators. AI shortens the time it takes to identify vulnerable device types and write targeting scripts, and GreenJuliett has moved it from individual accounts into its operating environment.

Figure 1: The GreenJuliett operation path, as observed from August to October 2026

Source:
Michael Davis
·
www.recordedfuture.com

Comments

Sign in to comment.

No comments yet. Be the first to comment.

Related Articles

The future of onchain FX could start with users, not institutional liquidity

11 hours ago

Wrapped Monero token crashes 99.8% amid suspected $13.5M exploit

2 days ago

Sky Protocol sees $2 billion in stablecoin withdrawals, disputes illicit fund claims

2 days ago

AI Joins the Industrial Attack Workflow

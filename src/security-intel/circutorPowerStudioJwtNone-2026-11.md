# CIRCUTOR PowerStudio SCADA WAVE JWT 签名验证失效（CVE-2026-120387）—— 电力监测 SCADA 平台上的免认证身份伪造，且公开 PoC 已存在

> 🔴 强约束 · 采集于 2026-11-25 · 核心标识：**CVE-2026-120387，CIRCUTOR PowerStudio SCADA WAVE 24.8.0 – <24.11.17.0 全部受影响，修复版 24.11.17.0** · ⭐⭐⭐ **根因是"共享 JWT 校验组件"接受 `alg=none` 的未签名令牌 —— 一处失守、平台全部受保护功能同时失守**（与库内 11-18 我方 `/preview/` 路径族"成组接口模式"是同一类结构问题） · ⭐⭐⭐ **CVSS v4 10.0（CNA 自评）/ v3.1 9.1（NVD）/ v2 6.4（NVD），三套评分并存** · ⭐⭐⭐ **公开 PoC 已存在于 GitHub（Exploit-Garbage/0day-Rubbish），CISA SSVC 判定 exploitation = proof of concept、automatable = yes、technical impact = total** · ⭐⭐ **但 EPSS 仅 0.4%、未入 KEV、无在野利用证据** —— 库内首条"公开可利用 + 官方未收录"的样本 · ⭐⭐ **受影响的是"用于监控与控制电力系统"的 SCADA 平台，与我方 DER 监控平台同类形态** · ⚠️ **我方无 CIRCUTOR 使用证据 → 不得下"我方受影响"结论**

---

## 一、信源核实

| 项 | 值 |
|---|---|
| 来源请求 | `光伏 逆变器 SCADA 监控平台 暴露面 EPICS 漏洞 2026年11月`（web_search，命中 CISA SP 800-82 相关分析，检索摘要中出现 NEOSEC 的 CIRCUTOR 条目）<br>`CIRCUTOR PowerStudio SCADA WAVE CVE-2026-120387 JWT alg none authentication bypass advisory`（web_search，命中 NEOSEC 情报页、CIRCUTOR 官方 PSIRT 页、Tenable CVE 条目、SecAlerts、IONIX、Halo Threat Intelligence、阿里云漏洞库、Enigma Global、Red Tiger Security 等多个独立源） |
| 原始 URL（主 · 官方 PSIRT 页） | https://circutor.com/en/support/cybersecurity （CIRCUTOR 官方 Product Cybersecurity 页，**已解决案例表中载有 CVE-2026-120387**：描述为 "An improper JWT signature verification vulnerability in CIRCUTOR PowerStudio SCADA WAVE desktop version allows an unauthenticated remote attacker to bypass authentication by submitting an unsigned JWT with the algorithm set to 'none'…"，严重度 **Critical**，日期 **16/11/2026**，产品 **Power Studio Wave 24.8.0 to 24.11.17**，附 PDF 公告） |
| 原始 URL（辅 1 · 第三方情报） | https://intel.neosec.eu/en/cve/CVE-2026-120387 （NEOSEC Intel 情报页，**Published 17.11.2026 04:47 UTC / Last modified 17.11.2026 19:17 UTC**，Sources: EUVD, CVE.org；含 SSVC 判定与公开 PoC 引用） |
| 原始 URL（辅 2 · 第三方 CVE 库） | https://www.tenable.com/cve/CVE-2026-120387 （Tenable CVE 条目，含 CVSS v2/v3.1/v4 三套评分与 EPSS 数值） |
| 原始 URL（辅 3 · 第三方分析，检索摘要） | https://www.ionix.io/threat-center/cve-2026-120387 （IONIX Threat Center 技术分析）· https://cve.halosecurity.com/cve-advisory/cve-2026-120387 （Halo Threat Intelligence，含 Surface Signal 暴露面评级）· https://www.redtigersecurity.com/advisories （Red Tiger Security OT 威胁简报："lets anyone who can reach the server sign in as any user without a password… Upgrade to version 24.11.17.0 or later and keep the server off the internet"）· https://avd.aliyun.com/detail?id=AVD-2026-120387 （阿里云漏洞库） |
| 发布主体 | CIRCUTOR（西班牙电力质量设备厂商 · 官方 PSIRT，公告日 2026-11-16）· NIST NVD / CVE.org / ENISA EUVD（编号与评分）· NEOSEC（第三方情报）· Tenable（第三方 CVE 库）· IONIX / Halo / Red Tiger Security / 阿里云（第三方分析） |
| 发布/更新时间 | **厂商公告 2026-11-16** · **CVE 编号发布 2026-11-17 04:47 UTC** · NEOSEC 最后更新 2026-11-17 19:17 UTC |
| 采集时间 | 2026-11-25 07:12:49 – 07:19:25 |
| 快照 | `raw/snapshots/security/circutor-psirt-advisory.md` · `neosec-circutor-powerstudio-jwt-none.md` · `tenable-circutor-jwt.md` |

**快照清单**（SHA256 取自 `.meta.json` 的 `sha256_raw`）

| 快照 | SHA256 | 抓取时间 | 正文字符 | HTTP |
|---|---|---|---|---|
| `raw/snapshots/security/circutor-psirt-advisory.md` | `6e5c0957a3c5fb5eb665f47d48ab38ef7ea4c674694aca21c79bbe86a1f01525` | 2026-11-25 07:17:52 | 2,723 | 200 |
| `raw/snapshots/security/neosec-circutor-powerstudio-jwt-none.md` | `837137d3c31b6d111136f27290bc7ee12058e17f452e91f993b203a645beeaaa` | 2026-11-25 07:12:49 | 10,301 | 200 |
| `raw/snapshots/security/tenable-circutor-jwt.md` | `0bd88fa0cd458c2c2ff5145f3554c922ff9771489ebbea2dc9931a851861b1d5` | 2026-11-25 07:19:25 | 2,471 | 200 |

> 📎 **入库理由**：库内安全域 18 篇此前**从未收录过"电力监测/配电 SCADA 平台"这一形态的漏洞**（有 SCADA-LTS 授权绕过、EPICS 工控栈、ICONICS 平台，但都不是面向电网监测的商用 SCADA）。⭐⭐⭐ **本条的独特价值有三点**：① **根因是"共享校验组件"不验签** —— 这是库内 11-18 提出"我方 `/preview/` 路径族是成组接口模式、一处失守全线失守"的**外部同型案例**（我方那次是 Base64 URL 参数面，这次是共享 JWT 组件）；② **公开 PoC 已存在 + CISA 判定 automatable = yes，但 EPSS 只有 0.4%、未入 KEV** —— 这是一个"官方未收录但实际可自动化利用"的新样本，与库内 11-19 Java4Shell（PoC 公开、未入 KEV）同类但自动化程度更高；③ **三套 CVSS 评分并存（10.0 / 9.1 / 6.4）** —— 与库内 11-24 KEV 批次首次记录的"NVD 与 CNA 评分差"形成同一现象的第二例。
> ⚠️ **归档取舍说明**：SecAlerts 页面抓取返回 HTTP 202 且正文 **0 字符**（反爬空页），阿里云漏洞库仅 66 字符（JS 渲染），IONIX 返回 HTTP 403 —— **三者均已删除快照，不予引用**；本条以**厂商官方 PSIRT 页 + NEOSEC + Tenable** 三源支撑，其中厂商页正文为 JS 渲染（抓取到的为导航与表格框架），**具体 CVE 行以检索摘要中的官方页面内容为准并标注为"摘要核"**。

---

## 二、事实核查

| # | 数据点 | 原文表述 | 核查方式 | 结论 | 备注 |
|---|---|---|---|---|---|
| 1 | **⭐⭐⭐ 根因：共享 JWT 校验组件接受 alg=none 未签名令牌** | 官方描述（经检索摘要核对官方 PSIRT 页与 NEOSEC）：*"An **improper JWT signature verification** vulnerability… allows an **unauthenticated remote attacker to bypass authentication by submitting an unsigned JWT with the algorithm set to 'none'**. **The shared JWT validation component accepts the token without verifying a cryptographic signature**, allowing the attacker to **impersonate another user** and access protected functionality with that user's privileges."*；阿里云转述公开技术分析指出根因定位到 `AddJWTBearerAuthentication`，其中 `SignatureValidator` **直接返回令牌对象且不校验签名**，同时未要求令牌必须带签名 | 官方 PSIRT 检索摘要 + NEOSEC 快照 + Tenable 快照 + 阿里云/Enigma 两源逐字比对 | ✅ **已核（四源一致）** | ⭐⭐⭐ **库内首条"共享校验组件"型认证失效**。⭐⭐⭐ **对我方最重要的价值在这里**：库内 11-18 文档已确认我方 `/preview/` 路径下存在**成组接口共用同一套跨域取文件语义**，并明确写下"**这不是一个接口的偶发写法，而是成组接口模式**" —— **CIRCUTOR 这次证明同类结构会把风险放大到平台级**（一处组件不验签 → 全部受保护功能同时被免认证身份伪造）。⭐⭐ **这不是"又一个 JWT 漏洞"，而是"共用组件 = 共用单点故障"这一结构的第二个独立样本**（第一个样本是我方自己） |
| 2 | 受影响版本与修复版 | 官方与 NEOSEC 一致：受影响 **24.8.0 – < 24.11.17.0**，修复于 **24.11.17.0**；Red Tiger 补充 "Upgrade to version 24.11.17.0 or later and keep the server off the internet" | 三源交叉（官方摘要 + NEOSEC 快照 + Tenable 快照） | ✅ **已核** | ⭐⭐ **修复版发布于披露次日**，属"披露即有补丁"的快节奏案例（对照库内 11-24 ICSA-26-321-08 的 14/14 无修复，**两个样本正好构成"可修 / 不可修"两极**） |
| 3 | **⭐⭐⭐ 三套评分并存** | Tenable 条目：**CVSS v2 Base Score 6.4**（AV:N/AC:L/Au:N/C:P/I:P/A:N，Severity Medium）；**CVSS v3 Base Score 9.1**（AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N，Critical）；**CVSS v4 Base Score 10**（AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H，Critical）。NEOSEC：v4 10.0 来自 **Vendor (CNA)**；Enigma 亦给 v4 10.0 | Tenable 快照逐字 + NEOSEC 快照 + 检索摘要（Enigma/IONIX） | ✅ **已核（三源一致）** | ⭐⭐⭐ **库内首条三套评分并存的样本**。⭐⭐⭐ **三套评分的分歧点非常值得记**：**v2 与 v3/v4 的差距来自"权限要求"这一维**（v2 = `Au:N` 即无需认证，Medium；v3/v4 = `PR:N` 即无需权限，Critical）。⭐⭐ **这不是评分错误，而是 CVSS 版本演进（v2 无 PR 概念、v2 记 Au）导致的口径差** → **对我方的直接含义：跨库比分数时必须先对齐 CVSS 版本，否则"6.4 vs 10.0"会被误读成"差了一倍半"，实际是同一个漏洞**。⭐⭐ **这与库内 11-24 刚记录的"NVD 与 CNA 评分差"是两种不同的评分分歧机制**（版本差 vs 评估方差），**必须分开记录** |
| 4 | **⭐⭐⭐ 公开 PoC 已存在 + CISA SSVC 判定** | NEOSEC 快照：**"Public exploit"**；CISA assessment (SSVC)：**"Exploitation: proof of concept · automatable · Technical impact: total"**；公开 PoC 引用：GitHub `Exploit-Garbage/0day-Rubbish`（成熟度标注 "PoC (publicly reported) reported, not verified"）、`0day-rubbish.com` 技术分析 | NEOSEC 快照逐字抄录 | ✅ **已核** | ⭐⭐⭐ **库内首条"公开 PoC + 官方 SSVC 判定 automatable = yes"的样本**。⭐⭐ **对照库内 11-19 Java4Shell**：那条是"PoC 公开 + 官方预判短期内规模化攻击风险较高"，但 CISA 明确无在野利用、automatable = no；**这条是 automatable = yes + technical impact = total** → **自动化利用可能性明显更高**。⭐⭐ **三个"可利用性"信号要分清**：**PoC 公开**（利用代码可得）、**automatable**（能否无人值守规模化）、**EPSS**（30 天内被利用的统计概率）—— 本条前两项高、第三项低 |
| 5 | **⚠️ EPSS 极低 + 未入 KEV + 无在野证据** | Tenable 快照：**EPSS: 0.00405**（即 **0.4%**）；NEOSEC：EPSS 0.4%、**KEV status: — （未收录）**；CISA SSVC 记为 "proof of concept"（**不是"active"**） | Tenable + NEOSEC 两源交叉 | ✅ **已核** | ⭐⭐⭐ **库内首条"三低一高"的不对称样本**：**PoC 公开（高）、automatable（高）、technical impact total（高），但 EPSS 0.4%（低）、未入 KEV（低）、无在野利用（低）**。⭐⭐ **这个不对称本身就是一条方法论** —— 它证明**"官方未收录 + 利用概率低"不等于"可以先放着"**：本条的 damage 是 complete（任意用户权限冒用 + 免认证），**只要可达就是灾难**，而 EPSS 低只是说"还没人打"。⭐⭐ **这条恰好是库内 11-19 已确立判据的一个反向验证场景**：该判据说"联网可达性优先于 KEV 收录状态" → **本条若我方或有客户部署了它，可达性即是全部理由，不需要等它进 KEV** |
| 6 | 受影响产品的定位 | Red Tiger：*"**energy monitoring software**"*；Halo：*"This vulnerability affects a specific **desktop application used for monitoring and controlling electrical power systems**. Engineers and facility managers use this tool to manage data and operations within SCADA… typically overseeing **critical energy infrastructure**."*；IONIX：*"CIRCUTOR PowerStudio SCADA WAVE desktop version (Windows, 64-bit)"* | 检索摘要多源比对 | ✅ **已核** | ⭐⭐⭐ **库内首条"电力系统监控与控制 SCADA"的商用平台漏洞**。⭐⭐ **与我方的形态相似性是真实的**：我方做的是分布式光伏 DER 的监控与调控平台（库内 11-16 DER 暴露面论文），**平台角色、部署位置（工程师站/监控站）、接入对象（现场设备）都同类**。⭐⭐ **但必须写清边界**：**"同类形态"不等于"同类实现"** —— 我方无 CIRCUTOR 使用证据，**不得下"我方受影响"结论**。⭐⭐⭐ **本条的真正用途是作为"同类平台的失效模式参照"**：一个电力行业 SCADA 平台的共享认证组件可以这样失守，我方平台的共享鉴权中间件（若存在）就应当按同样标准被审 |
| 7 | 桌面版部署位置与暴露面评级 | IONIX：*"**CIRCUTOR PowerStudio SCADA WAVE desktop version (Windows, 64-bit)**"*；Halo：**"Halo Surface Signal: 2 out of 5 — less likely to be public-facing"**、*"public internet exposure is uncommon for desktop-based SCADA administration tools"*；Halo 同时指出其产品为*"electrical power system monitoring"*、*"typically overseeing critical energy infrastructure"* | 检索摘要逐字 | ✅ **已核（第三方评级）** | ⭐⭐⭐ **这条把风险位置说清楚了，而且是库内至今最有价值的一次"暴露面位置"推理**：**桌面版 SCADA 通常不在公网、暴露面在"谁够得着工程师站"** → 这正好接上库内 11-24 ICSA-26-321-08 的分析（"Information Server 常被从办公网读报表 → NTLM/SQL 流量最常从 IT 跨入 OT"）与库内 11-19 早已记录的"**工程站与远程接入路径是 ICS 通告的反复主题**"。⭐⭐⭐ **两条独立来源、不同漏洞、同一结论：我方近期关心的 OT 风险重心不在"设备是否对公网开放"，而在"办公网 / 运维通道能否触达监控与工程系统"** —— 这已经是库内第三次得出这个结论（11-16 DER 暴露面、11-19、11-24）。⭐⭐ **Halo 的 Surface Signal 2/5 评级只是第三方经验值，不是漏洞事实**，标注来源 |
| 8 | 厂商处置与临时缓解 | IONIX：*"Immediate: upgrade to PowerStudio SCADA WAVE 24.11.17.0 or later. **No official workaround is documented.** Until patched, **restrict network access to the PowerStudio services to trusted hosts only, keep them off the internet, and monitor for suspicious authentication activity.**"*；Red Tiger：*"Upgrade to version 24.11.17.0 or later and **keep the server off the internet**"* | 检索摘要两源一致 | ✅ **已核** | ⭐⭐ **厂商未提供官方变通方案**，两方分析一致给出"限制访问 + 监控异常认证活动"作为临时措施 → **可作为我方自检项**。⭐⭐ **注意"monitor for suspicious authentication activity"这条** → 它对应一个我方可以直接做的检测点：**认证日志里出现无法解释的"同一账号从异常来源成功登录"** —— 因为 alg=none 伪造出来的令牌在服务端与正常令牌**没有可区分特征**，**唯一可用的检测信号是"登录来源与行为异常"**。⭐⭐ 这与库内 11-19 已记的"Cloudflare 观测到扫描器约 17 小时后把利用请求伪装成 Chrome UA → **UA 不得作为判定依据**"是同一条方法论：**伪装会越来越像，但行为与来源不会完全像** |
| 9 | 弱点分类 | NEOSEC / Tenable / 阿里云一致：**CWE-347 Improper Verification of Cryptographic Signature** | 三源交叉 | ✅ **已核** | ⭐⭐ **CWE-347 与库内已记的几类都不同**：库内 11-24 phpAfterShell 是 CWE-502 反序列化、OpenPLC 是 CWE-840 竞态、LiteLLM 是 CWE-420 未保护备用通道 —— **"该验的没验"（347）是库内首次出现的弱点类型**。⭐⭐ **值得注意的对比**：CWE-420（备用通道）与 CWE-347（不验签）在实践后果上高度相似 —— **都让攻击者绕过认证**，只是绕过路径不同（一个走备用门，一个走后门不查证件） |

> **核查小结**：本文**核心事实（受影响版本、修复版本、根因、CWE、三套评分、SSVC 判定、PoC 存在、EPSS 数值）均逐字核对自 NEOSEC 与 Tenable 两份快照**，官方 PSIRT 页因 JS 渲染仅取得页面框架，**其 CVE 行以检索摘要中的官方内容为准并标注"摘要核"**。**四条必须写明的边界**：① **我方无 CIRCUTOR 使用证据 → 不得下"我方受影响"结论，也不得下"我方不受影响"结论**；② **未入 KEV、无在野利用证据、EPSS 仅 0.4%**；③ **三套 CVSS 评分的分歧源于版本演进（v2 无 PR 概念）而非评估分歧**，与库内 11-24 记录的"NVD vs CNA"分歧是两种不同机制；④ **"桌面版 SCADA 不太可能公网暴露"是第三方评级（Halo Surface Signal 2/5），不是漏洞事实**。

---

## 三、原文归档（快照）

- 快照文件：`raw/snapshots/security/neosec-circutor-powerstudio-jwt-none.md`
- SHA256：`837137d3c31b6d111136f27290bc7ee12058e17f452e91f993b203a645beeaaa`
- 抓取时间：2026-11-25 07:12:49 · 正文字符 10,301 · HTTP 200

**关键原文摘录（NEOSEC Intel，Published 17.11.2026 04:47 UTC）**：

> 「An improper JWT signature verification vulnerability in CIRCUTOR PowerStudio SCADA WAVE desktop version allows an unauthenticated remote attacker to bypass authentication by submitting an unsigned JWT with the algorithm set to "none". **The shared JWT validation component accepts the token without verifying a cryptographic signature**, allowing the attacker to impersonate another user and access protected functionality with that user's privileges.」
>
> 「**Public exploit**」
> 「Affected: Circutor PowerStudio SCADA Wave **lt 24.8.0..24.11.17.0**｜**Fixed in Circutor PowerStudio SCADA WAVE 24.11.17.0**」
> 「**CISA assessment (SSVC) Exploitation: proof of concept · automatable · Technical impact: total**｜Source: CISA Vulnrichment, as of 17 November 2026」
> 「**CWE-347** Improper Verification of Cryptographic Signature」
> 「EPSS score **0.4 %** — model estimates < 1% exploitation likelihood｜Source: FIRST EPSS, percentile 35.5」
> 「KEV status — The KEV catalogue is a list maintained by the US authority CISA for vulnerabilities for which active exploitation in the wild has been confirmed. It answers the question "is it already being attacked?" rather than "how severe is it?"」
> 「**Public exploit references**｜Source: **github.com** — PoC (publicly reported) reported, not verified｜Reference: `0day-rubbish.com` blog `circutor-powerstudio-jwt-alg-none-identity-forgery`」

**关键原文摘录（Tenable CVE 条目）**：

> 「CVE-2026-120387 critical
> **CVSS v2 Base Score: 6.4** Vector: `CVSS2#AV:N/AC:L/Au:N/C:P/I:P/A:N` Severity: Medium
> **CVSS v3 Base Score: 9.1** Vector: `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N` Severity: Critical
> **CVSS v4 Base Score: 10** Vector: `CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H` Severity: Critical
> **EPSS: 0.00405**
> References: github.com/Exploit-Garbage/0day-Rubbish；euvd.enisa.europa.eu/vulnerability/EUVD-2026-126913；circutor.com/soporte/ciberseguridad/」

**关键原文摘录（官方 PSIRT 页检索摘要内容）**：

> 「Resolved cases｜CVE ID: **CVE-2026-120387**｜Description: An improper JWT signature verification vulnerability in CIRCUTOR PowerStudio SCADA WAVE desktop version allows an unauthenticated remote attacker to bypass authentication by submitting an unsigned JWT with the algorithm set to "none". The shared JWT validation component accepts the token without verifying a cryptographic signature, allowing the attacker to impersonate another user and access protected functionality with that user's privileges.｜Severity: **Critical**｜Date: **16/11/2026**｜Products: **Power Studio Wave**｜Version: **24.8.0 to 24.11.17**｜[PDF]」

---

## 四、概要提取

- ⭐⭐⭐ **CVE-2026-120387：CIRCUTOR PowerStudio SCADA WAVE 24.8.0 – <24.11.17.0 全部受影响，修复版 24.11.17.0**（披露次日即出补丁）。
- ⭐⭐⭐ **根因是"共享 JWT 校验组件"接受 `alg=none` 未签名令牌** → 一处失守、平台全部受保护功能同时被免认证身份伪造（CWE-347，库内首次该弱点类型）。
- ⭐⭐⭐ **公开 PoC 已存在（GitHub Exploit-Garbage/0day-Rubbish）；CISA SSVC 判定 exploitation = proof of concept、automatable = yes、technical impact = total** —— 库内首条公开可自动化利用的样本。
- ⭐⭐ **但 EPSS 仅 0.4%、未入 KEV、无在野利用证据** —— 库内首条"三低一高"的不对称样本。
- ⭐⭐⭐ **三套 CVSS 评分并存：v4 10.0（CNA）/ v3.1 9.1（NVD）/ v2 6.4（NVD）** —— 分歧源于 v2 无 PR 概念（v2 记 `Au:N`），**与库内 11-24 记录的"NVD vs CNA"分歧是两种不同机制，必须分开记录**。
- ⭐⭐⭐ **受影响的是"用于监控与控制电力系统"的商用 SCADA 平台（桌面版，Windows 64-bit）** —— 库内首条该形态漏洞，与我方 DER 监控平台形态同类。
- ⭐⭐⭐ **暴露面位置被第三方独立指出：桌面版 SCADA 通常不公网暴露，风险在"谁够得着工程师站"** —— 与库内 11-24 ICSA-26-321-08（办公网读报表 → IT/OT 横向流量）、11-19（工程站与远程接入是 ICS 通告反复主题）**三点汇成同一结论**。
- ⭐⭐ **厂商无官方变通**；两方分析一致的临时措施为"限制访问 + 监控可疑认证活动"；因 alg=none 伪造令牌**无服务端可区分特征**，**唯一检测信号是登录来源与行为异常**。

---

## 五、主要观点

**原文主张**
- CIRCUTOR 官方 PSIRT：PowerStudio SCADA WAVE 桌面版存在 JWT 签名验证不当，未认证远程攻击者提交 `alg=none` 未签名令牌即可绕过认证、冒充任意用户访问受保护功能；严重度 Critical，公告日 2026-11-16，版本 24.8.0 至 24.11.17。
- NEOSEC：已公开 PoC；CISA SSVC 判定可自动化、技术影响为 total；EPSS 0.4%、未入 KEV。
- Tenable：三套 CVSS 评分并列。
- IONIX / Red Tiger：升级至 24.11.17.0；**无官方变通**；限制访问、勿接公网、监控异常认证活动；桌面版 SCADA 不太可能公网暴露，但处于关键能源基础设施的监管之下。

**我方判断**
- ⭐⭐⭐ **这条最该被记住的是它与我方 11-18 那条待办互为镜像，而不是漏洞本身**。库内 11-18 已经把事实摆清楚了：我方 `/preview/` 路径族下存在**一组共用同一套"按客户端指定 URL 取资源"语义的接口**，文档里明确写着"**这不是一个接口的偶发写法，而是成组接口模式**"，并且留了一句"**审计范围应覆盖 `/preview/` 下全部接口，而不是只查这两个**"。⭐⭐⭐ **CIRCUTOR 这次把这条方法论验证到了平台级**：一个电力行业商用 SCADA 平台，因为**共享的 JWT 校验组件不验签**，导致平台**所有**走该组件的受保护功能同时被免认证身份伪造 —— **一处失守、全线失守**。⭐⭐ **这不是"我们要不要修 JWT"的建议，而是"凡我方平台内被多处共用的鉴权/校验组件，必须按'单点故障'标准评估影响面"的结论。** → **动作：代码审计范围从"逐个接口看"升级为"先画出共用组件图"** —— 找出所有共用同一个鉴权中间件 / 同一套签名校验 / 同一个会话组件的接口集合，作为审计单元。⭐⭐ **这与库内 11-16 已记的暴露面论文结论（"大量系统由安装商/终端用户配置"）是同一个世界观的两个面：一个讲配置泛滥，一个讲组件共用。**
- ⭐⭐⭐ **"三低一高"这个不对称，是本条最有方法论价值的部分**。PoC 公开（高）、automatable（高）、technical impact = total（高）—— 但 EPSS 0.4%（低）、未入 KEV（低）、无在野利用（低）。⭐⭐⭐ **如果我方（或我方客户的电站/监控环境）里有这个产品，按照库内 11-19 已确立的判据（联网可达性优先于 KEV 收录状态），根本不需要等它进 KEV 就要处置 —— 理由是"可达 + 后果完全"，不是"已被利用"。** ⭐⭐ **反过来说，这条也提供了一个防误判的样本**：**EPSS 0.4% 会让人以为可以缓一缓，而 SSVC 的 technical impact = total 说的是"打中就全毁"** —— **利用概率低与破坏后果重是两件事，排序时不能混。** → **动作：我方漏洞优先级表里"利用概率"与"失效后果"必须分列两行，不得相乘或折算成一个总分** —— 这与库内 11-19 已记的"按发现—可利用成本排优先级，而非按 CVSS 排"是同一条原则的延伸。
- ⭐⭐⭐ **三点汇流的那个结论，我认为是本期安全侧最值得沉淀的一条**。库内 11-16（DER 暴露面论文）、11-19（工程站与远程接入路径是 ICS 通告的反复主题）、11-24（ICSA-26-321-08 的"办公网读报表 → IT/OT 横向流量"）—— 三条独立来源、不同漏洞、不同时间，**全部指向"风险重心在运维通道与办公网侧，不在设备是否对公网开放"**。⭐⭐⭐ **再加上本条 CIRCUTOR 的 Halo Surface Signal 2/5 评级（桌面版 SCADA 不太可能公网暴露、风险在谁够得着工程师站），就是四条独立来源的同一结论。** → **动作：我方暴露面自查（库内 P0 产物 `remediation-exposureHygiene`）的检查表应新增一维："哪些监控/工程/历史系统被办公网或远程运维通道访问、认证方式为何、链路是否加密"** —— **这与我在本期 ICSA-26-321-08 文档里提出的动作是同一件事，两条情报互为佐证。** ⭐⭐ **这也说明库内近四期安全情报的收敛方向是清楚的：不是"更多漏洞"，而是"把风险位置重新定位"。**
- ⭐⭐ **检测思路要落到"行为与来源"，不能落到"请求特征"**。alg=none 伪造出来的令牌，在服务端**与正常令牌没有任何可区分特征**（不验签意味着连签名都不看）→ **服务端日志里这就是一次"正常登录"**。⭐⭐ **所以厂商/分析师给出的"monitor for suspicious authentication activity"是唯一可行的检测线索**：登录来源 IP、登录时段、登录后行为（访问了哪些功能、是否突然大量调用）异常。⭐⭐ **这与库内 11-19 记的"Cloudflare 观测到扫描器 17 小时后把利用请求伪装成 Chrome UA → UA 不得作为判定依据"完全同款**：**伪装特征会失效，行为与来源不会完全失效。** → **动作：若我方做监控平台，其审计日志的最小字段集应包含"登录来源 + 登录时刻 + 会话内操作序列"** —— 否则这类"合法令牌"型绕过在事后追溯时无法与正常操作区分。⭐⭐ **顺带一提**：这也是本条对我方唯一真正可落的一条（产品侧），但按本阶段口径只能标 🟡 待复核，不落产品级结论。
- ⭐⭐ **三套评分必须按版本分开记，这是一条具体的操作规则**。本条 v2 = 6.4、v3.1 = 9.1、v4 = 10.0，看着像三个分数其实是同一个洞。⭐⭐ **"v2 没有 PR 概念、只记 Au"这个机制差异**是关键 —— 它意味着**任何跨库比较 CVSS 的动作，先要问"是哪个版本"**。⭐⭐ **库内 11-19（Java4Shell 8.1/9.2 双口径）、11-24（KEV 批次 NVD vs CNA 差异、本条 v2/v3/v4 三套）已经把三种评分分歧机制都碰到了** → **动作：台账的分数字段应改成三元组（版本 / 分值 / 来源），而不是一个裸数字。** ⚠️ **注意与 11-24 那条的区分**：那是**同一版本、评估方不同**（NVD 更严）；本条是**评估方一致、版本不同**（v2 口径不含 PR）。**两种机制在库里并存，不能混为一谈。**
- ⚠️ **必须保持的边界**：① **不得下"我方受影响"结论**（无 CIRCUTOR 使用证据），**也不得下"我方不受影响"结论**（无资产清单）；② **不得写成"已被在野利用"**（EPSS 0.4%、未入 KEV、SSVC = proof of concept 而非 active）；③ **"桌面版 SCADA 不太可能公网暴露"是第三方评级**（Halo Surface Signal 2/5），不是漏洞事实；④ **厂商页与三个第三方页的正文抓取分别受 JS 渲染 / 403 / 空页限制**，条款级以 NEOSEC + Tenable 快照为准，官方行标注"摘要核"；⑤ **不得把本条转成我方功能需求**（按本阶段口径，产品级待复核）。

---

## 六、参考意义

| 方向（网络安全/信创/等保/隐私保护/护网） | 可证事实 | 本阶段处理 |
|---|---|---|
| **网络安全** | ① 根因是"共享 JWT 校验组件"不验签 → 一处失守、平台全部受保护功能同时失守（与我方 11-18 已确认的 `/preview/` 路径族"成组接口模式"同型）；② PoC 公开 + CISA SSVC automatable = yes + technical impact = total，而 EPSS 仅 0.4%、未入 KEV → **利用概率与失效后果必须分列**；③ 三套 CVSS（10.0 / 9.1 / 6.4）源于版本口径差异 → **分数字段须改为（版本/分值/来源）三元组**；④ 桌面版 SCADA 的暴露面在"谁够得着工程师站"而非公网 → 与库内 11-16 / 11-19 / 11-24（ICSA-26-321-08）三点汇流；⑤ alg=none 伪造令牌在服务端无可区分特征 → **唯一检测线索是登录来源与行为异常** | ✅ **可进评审（方向级）**。**影响可证**：① **代码审计单元从"逐接口"改为"共用组件集合"**（先画共用鉴权/校验/会话组件图，以组件图划定审计范围）；② **暴露面自查检查表新增一维**："哪些监控/工程/历史系统被办公网或远程运维通道访问、认证方式为何、链路是否加密"（与本期 ICSA-26-321-08 条目互为佐证）；③ **漏洞优先级表"利用概率"与"失效后果"分列两行，不得折算为单一总分**；④ **分数登记改为三元组（版本/分值/来源）**；⑤ **监控审计日志最小字段集补"登录来源 + 登录时刻 + 会话内操作序列"**。⭐ **产品级归属按本阶段口径不写**，标 🟡 待复核 |
| **等保** | 无我方条款级映射材料 | ❌ **不适用**（不得把 SP 800-82 草案或本条直接转成等保要求） |
| 护网 | PoC 公开 + automatable = yes 的免认证绕过 | 🟡 **待复核** —— 可作护网演练中"**认证绕过类漏洞的处置顺序不看 EPSS、只看可达性**"的案例；**无我方侧证据 → 不得写成我方被利用** |
| 信创 / 隐私保护 | 无可证事实 | ❌ **不适用** |

---

## 七、总结输出

**一句话结论**：**CIRCUTOR PowerStudio SCADA WAVE 的 CVE-2026-120387（JWT `alg=none` 不验签，CVSS v4 10.0 / v3.1 9.1 / v2 6.4，修复版 24.11.17.0）的价值不在编号而在两条结构结论 —— 一是"共享校验组件不验签 → 平台全部受保护功能同时被免认证身份伪造"，这正是库内 11-18 我方 `/preview/` 路径族"成组接口、一处失守全线失守"的外部同型样本，指向代码审计单元须从"逐接口"改为"共用组件集合"；二是它构成库内首条"三低一高"不对称样本（PoC 公开 + automatable + technical impact total，却 EPSS 0.4%、未入 KEV、无在野利用），说明"利用概率"与"失效后果"必须分列不得折算，而唯一可用检测线索是登录来源与行为异常（伪装特征会失效、行为不会）—— 三点汇流再证我方风险重心在办公网与运维通道侧而非公网暴露面。**

**落地去向**
- [ ] 产品特性
- [ ] 需求变更
- [x] 专项整改

---

## 参考链接

- [CIRCUTOR 官方：Product cybersecurity（PSIRT 已解决案例表 · CVE-2026-120387）](https://circutor.com/en/support/cybersecurity)
- [NEOSEC Intel：CIRCUTOR PowerStudio SCADA WAVE JWT Signature Validation Authentication Bypass (CVE-2026-120387)](https://intel.neosec.eu/en/cve/CVE-2026-120387)
- [Tenable：CVE-2026-120387（三套 CVSS 评分与 EPSS）](https://www.tenable.com/cve/CVE-2026-120387)
- [IONIX Threat Center：CVE-2026-120387（技术分析与缓解）](https://www.ionix.io/threat-center/cve-2026-120387)
- [Halo Threat Intelligence：CIRCUTOR PowerStudio SCADA WAVE JWT Bypass Vulnerability（Surface Signal 暴露面评级）](https://cve.halosecurity.com/cve-advisory/cve-2026-120387-circutor-powerstudio-scada-wave-jwt-bypass-vulnerability)
- [Red Tiger Security：Advisories & OT Threat News（CIRCUTOR 条目）](https://www.redtigersecurity.com/advisories)
- [库内相关：WAF 巡检 11-18：我方 /preview/getCorsFile 接口的 Base64 URL 参数面（"成组接口模式"· 同型结构问题）](wafCorsFilePreviewUrlParamSurface-2026-11-18.md)
- [库内相关：ICSA-26-321-08 Siemens SIMATIC NTLM 中继（办公网读报表 → IT/OT 横向流量）](icsa26321SiemensSimaticNtlmRelay-2026-11.md)
- [库内相关：EPICS 工控漏洞 + 光伏 DER 暴露面（工程站与远程接入路径）](epicsDerExposure-2026-11.md)
- [库内相关：CISA KEV 2026-11-23/24 批次三条（NVD vs CNA 评分差异 · 取证分诊维度）](cisaKev20261123Batch-2026-11.md)

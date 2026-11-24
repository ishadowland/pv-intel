# CISA ICSA-26-321-08：Siemens SIMATIC NTLM 中继（会话劫持）—— 14 个产品全部无补丁，唯一缓解是「配置 SQL 通信加密」

> 🔴 强约束 · 采集于 2026-11-25 · 核心标识：**CVE-2026-58114，14 个受影响产品"全部无修复"（8 个 None available + 6 个 No fix planned）** · ⭐⭐⭐ **库内首条"唯一缓解手段不是补丁、而是手工配置 SQL Server 通信加密"的 ICS 通告** · ⭐⭐⭐ **库内首条 NTLM 中继（认证协议层会话劫持）类漏洞** · ⭐⭐⭐ **库内首条把"办公网读报表"这一 IT/OT 横向流量路径写进厂商分析的攻击路径** · ⭐⭐ **库内首条 CISA 把"中继攻击"与"凭据被盗"并列的认证边界失效样本** · ⭐⭐ **Process Historian / Information Server = 长期归档与报表系统，是 NTLM/SQL 流量最易从 IT 跨入 OT 的位置** · ⚠️ **我方无 Siemens SIMATIC 使用证据 → 不得下"我方受影响"结论**

---

## 一、信源核实

| 项 | 值 |
|---|---|
| 来源请求 | `CISA ICS advisory November 24 2026 vulnerability SCADA`（web_search，命中 trout.software 的 ICS 通告档案，索引到 ICSA-26-321-08）<br>`CISA advisory ICSA-26-321-08 Siemens SIMATIC WinCC PCS 7 Process Historian NTLM relay CVE-2026-58114`（web_search，命中 CISA 官方通告页、Defcon Level 全文转载、Aviatrix 攻击链分析、Trout 深度分析、rdintel、TechGeeks 等多个独立源） |
| 原始 URL（主 · 官方通告） | https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-08 （CISA ICS Advisory "Siemens SIMATIC"，**Release Date November 17, 2026**，Alert Code ICSA-26-321-08） |
| 原始 URL（辅 1 · 第三方深度分析） | https://www.trout.software/blog/siemens-simatic-wincc-ntlm-relay-icsa-26-321-08 （Trout《Siemens SIMATIC WinCC, PCS 7 and Process Historian: NTLM Relay With No Fix (ICSA-26-321-08)》，**2026-11-19**） |
| 原始 URL（辅 2 · 通告全文转载） | https://www.defconlevel.com/alert/2026-11-17-cisa-cybersecurity-advisories-siemens-simatic-icsa-26-321-08 （Defcon Level 全文转载，**2026-11-17 12:00 UTC**） |
| 原始 URL（辅 3 · 攻击链分析） | https://www.aviatrix.ai/threat-research-center/icsa-26-321-08-siemens-simatic-cve-2026-58114-ntlm-authentication-bypass （Aviatrix《Siemens SIMATIC NTLM Authentication Bypass: 14 ICS Products Exposed with No Patch in Sight》，**2026-11-17**） |
| 发布主体 | CISA（ICS Advisory 转载方，明示为 Siemens ProductCERT SSA-970803 的逐字再发布）· Siemens ProductCERT（原始发布方，SSA-970803，**2026-11-10**）· trout.software（第三方 OT 分析）· Defcon Level（通告全文转载）· Aviatrix（威胁研究） |
| 发布/更新时间 | **Siemens ProductCERT 原始发布 2026-11-10** · **CISA 再发布 2026-11-17** · 第三方分析 2026-11-17 ~ 2026-11-19 |
| 采集时间 | 2026-11-25 07:12:19 – 07:12:48 |
| 快照 | `raw/snapshots/security/cisa-icsa-26-321-08-simatic-ntlm.md` · `trout-simatic-ntlm-321-08.md` · `defconlevel-simatic-321-08.md` |

**快照清单**（SHA256 取自 `.meta.json` 的 `sha256_raw`）

| 快照 | SHA256 | 抓取时间 | 正文字符 | HTTP |
|---|---|---|---|---|
| `raw/snapshots/security/cisa-icsa-26-321-08-simatic-ntlm.md` | `336c15533ae1c87ef87c7799a5bed5de0f2ac033f1f55edfed28c1bb51e0bc69` | 2026-11-25 07:12:19 | 11,342 | 200 |
| `raw/snapshots/security/trout-simatic-ntlm-321-08.md` | `b5904c5d06d82a1c658fdfba0e3af62a00d8199fd8c03ad46766a98e10a56145` | 2026-11-25 07:12:21 | 16,310 | 200 |
| `raw/snapshots/security/defconlevel-simatic-321-08.md` | `91cfa521342de87e04c4557c22c6b6c2c67ebcae7a50c138c2140e2cb570db98` | 2026-11-25 07:12:48 | 11,473 | 200 |

> 📎 **入库理由**：库内安全域已有 [ICSA-26-316-01~05 Siemens Node2Shell/PHP2Shell](icsa26316SiemensNode2Shell-2026-11.md)（11-16 期，内存破坏类）与 [ICSA-26-321-11 meta-iot2050 命令注入](icsa26321McpServerFirmwareCommandInjection-2026-11.md)（11-24 期，固件更新工具类），**但 11-17 CISA 同批 12 条通告中的 ICSA-26-321-08（SIMATIC NTLM 中继）从未入库** —— 库内 `ICSA-26-321-xx` 只记了 01/02/03/05/11，**08 是空缺**。⭐⭐⭐ **它的独特价值在于三点库内至今没有的机制**：① **14 个产品全部无修复**（8 个 `None available` + 6 个 `No fix planned`）；② **唯一缓解是"手工配置 SQL Server 通信加密"** —— 这是库内第一条**不靠升级、只能靠配置**的 ICS 通告；③ **它把"办公网读报表"这一真实业务动作写成了攻击路径** —— 而报表正是库内 DER 暴露面研究中我方同类系统最常见的用法。
> 📌 **入库级别定为 🔴 强约束**：不是因为"我方受影响"（我方无使用证据），而是因为**它同时命中库内已有的三条主线**：① 认证边界失效（11-24 KEV 批次）；② IT/OT 横向流量（11-16 DER 暴露面论文）；③ 无补丁场景下的补偿性控制（11-20 libumqtt）。

---

## 二、事实核查

| # | 数据点 | 原文表述 | 核查方式 | 结论 | 备注 |
|---|---|---|---|---|---|
| 1 | CVE 与弱点类型 | CISA 通告：*"CVE-2026-58114: Affected systems do not properly secure their remote user authentication with the **deprecated NTLM protocol**. This could allow **unauthenticated remote attackers, who have achieved a machine in the middle position, to relay NTLM authentication and impersonate a legitimate user**."*；CWE **1390**（Weak Authentication） | CISA 快照逐字 + Defcon Level 全文转载逐字比对 + Trout 转述 + Aviatrix 四源交叉 | ✅ **四源一致** | ⭐⭐⭐ **库内首条 NTLM 中继类漏洞**。⭐⭐⭐ **关键机制要点（与我方库内已知的所有认证类漏洞都不同）**：**攻击者不需要任何凭据** —— 他需要的不是偷到密码，而是**站在客户端与服务器中间**。⭐⭐ 库内 11-24 已记的 vCenter（"补丁不撤销已被取走的 SAML 签名材料"）、LiteLLM（"未受保护的备用通道"）、Roller（"管理界面关开关不足以防住"）**全部是"应用层认证逻辑有洞"**；**这条是"认证协议本身太弱 + 传输未加密"** → **库内认证失效模型首次补上"传输层"这一维** |
| 2 | 受影响产品数 | CISA 通告列出 **14 个受影响产品**（SIMATIC BATCH V9.1 / Information Server 2020 / Information Server 2022 / PCS 7 V9.1 / Process Historian 2020 / Process Historian 2022 / WinCC Runtime Professional V17~V21 / WinCC V7.5 / V8.0 / V8.1），**全部 `vers:all/*`** | CISA 快照逐条抄录受影响产品清单并计数 | ✅ **已核（14 个，逐条对应）** | ⭐⭐ **全部"所有版本"受影响，无版本可逃逸** |
| 3 | **⭐⭐⭐ 修复状态：14 个产品全部无修复** | CISA 通告逐产品的 Remediations 栏：SIMATIC BATCH V9.1 = **No fix planned**；WinCC Runtime Professional V20 = **None available**；WinCC Runtime Professional V21 = **None available**；WinCC V7.5 / V8.0 / V8.1 = **None available**；Information Server 2020 / 2022 = **No fix planned**；PCS 7 V9.1 = …；Process Historian 2020 / 2022 = … | CISA 快照内 `grep -c`：**`None available` 出现 8 次、`No fix planned` 出现 6 次，合计 14 = 受影响产品总数** | ✅ **已核（计数自洽，等于 14）** | ⭐⭐⭐ **库内首条"受影响产品 100% 无修复"的 ICS 通告** —— **不是"大部分无补丁"，是全部**。⭐⭐⭐ **对比库内已有的两个先例**：libumqtt（11-20）是"维护者失联、不响应 CISA 协调请求"，ICONICS/MC Works64（11-15）是"部分产品 no fix"；**这条是厂商在通告里明确写出"14 个产品、全部无修复、且未来也不打算修"** → **处置逻辑完全不同：不是等补丁，而是必须靠配置与网络架构长期兜底**。⭐⭐ **这一条对"我方版本基线登记"的要求最重**：**当一个产品家族全部无修复时，"打补丁"这个动作从我方台账里消失，取而代之的是一条长期存在的架构约束** |
| 4 | **⭐⭐⭐ 唯一缓解：手工配置 SQL Server 通信加密** | CISA 通告各产品 Remediations 栏统一指向：*"Customers can manually configure the **SQL Server Database for encrypting communication** as described in https://support.industry.siemens.com/cs/mdm/109818202…"*（快照中该链接出现 14 次） | CISA 快照逐字 + 计数（14 次）+ Defcon Level / Trout 同款表述 | ✅ **已核（14/14 产品同一缓解）** | ⭐⭐⭐ **库内首条"唯一缓解是配置项而非补丁"的 ICS 通告**。⭐⭐⭐ **这条对我方的意义超出产品本身**：**它把"数据库通信是否加密"从运维细节升格为一项必须长期跟踪的架构属性** —— 补丁能跟着版本走，**配置项不会**；厂商不会在下一版自动帮你把 SQL 流量加密了。⭐⭐ **对我方资产台账的直接要求**：**台账不能只记"版本 + 是否已打补丁"，必须能记"某项缓解配置当前是否生效"**（这一维库内 11-24 KEV 批次文档已提出"暴露面/多协议暴露"维度，本条补上了第三个维度：**缓解配置状态**） |
| 5 | 行业与部署范围 | CISA 通告：Sector **Critical Manufacturing**；Countries/Areas Deployed **Worldwide**；Company Headquarters **Germany** | CISA 快照逐字 | ✅ **已核** | ⚠️ **注意：CISA 标注的行业是"关键制造"，未列能源** —— 与库内 11-24 OpenPLC 通告（明确点名能源行业）不同。⭐⭐ **不得写成"官方点名能源行业"**。⭐⭐ 但**场景相关性反而更高**：WinCC/PCS 7/Process Historian 正是电厂与工控站普遍使用的监控与历史库系统 |
| 6 | 评分 | CISA 通告：**CVSS v3.1 7.5**；Trout 转述完整向量 **CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:H**；Siemens 另给 **CVSS v4 7.7**；CWE-1390 | CISA 快照 + Trout 快照 + Defcon Level 三源比对 | ✅ **已核（v3.1 7.5 三源一致；v4 7.7 为 Siemens 自评分）** | ⭐⭐ **AV:N / PR:N / AC:H** —— **无需凭据、无需用户交互，但攻击复杂度高（需先取得中间位置）**。⭐⭐ **这解释了为什么 CVSS 只有 7.5 而不是 9+**（对比库内 11-24 vCenter 9.8）→ **在库内的补丁优先级排序里，这条应当低于"无需中间位置"的免认证漏洞**，但**高于任何需要前提条件的漏洞**（AC:H 意味着前提是"网络可达 + 能插入流量"，而不是"需要社会工程"） |
| 7 | 攻击路径与"中间位置"来源 | CISA：*"The potential impact depends on the services that are accessible, e.g. a **SQL server used by WinCC**."*；Aviatrix：*"An on-path (machine-in-the-middle) attacker positions themselves on the network segment between a legitimate SIMATIC client and the SQL Server backend, exploiting the deprecated NTLM authentication protocol…"* | 三源交叉 | ✅ **已核** | ⭐⭐ **CISA 自己点出了 SQL Server** —— 这是官方给出的"最要紧的下游影响点"。⭐⭐ **攻击链是明确的四步**：① 取得中间位置 → ② 中继 NTLM 认证 → ③ 冒充合法用户取得会话 → ④ 以该用户权限执行代码。⭐⭐ **中间位置的取得方式未在任何源中说明** → **不得臆测具体攻击手法** |
| 8 | **⭐⭐⭐ 「办公网读报表」被写进攻击路径** | Trout：*"**Information Server is often read from the office network.** In many plants, production and quality staff open its reports from business PCs. In our reading, that makes it one of the places where **NTLM and SQL traffic most often crosses from IT into OT**."* | Trout 快照逐字 | ✅ **已核（第三方分析明确表述）** | ⭐⭐⭐ **库内首条把"办公网读报表"这一日常业务动作直接写成 IT/OT 横向流量入口的 ICS 分析**。⭐⭐⭐ **这条对我方的价值在于它把库内已有的两条线接上了**：① 库内 11-16 已记的 DER 暴露面研究结论（"**大量系统由安装商/终端用户配置并直接联网**"、"真实暴露规模此前被严重低估"）是**资产暴露**问题；② 而这条讲的是**流量穿越**问题 —— **资产在网内、可信用户从办公网访问它，攻击者只要能站在中间即可**。⭐⭐⭐ **结论：办公网 → OT 网的流量本身就是一个攻击面，与暴露面是两回事，我方资产清单必须能回答"哪些系统被办公网访问、用的什么认证协议、链路是否加密"**。⭐⭐ 这一条与库内 11-19 已记的"vCenter 案例"是同一原理的不同形态：**vCenter 是"认证材料被取走"，这条是"认证流量可被中继"** |
| 9 | 触发条件：NTLM 何时被使用 | Trout：*"All of them run on Windows and store data in Microsoft SQL Server. Operator stations, OS servers, engineering stations and report readers all sign in to them. **Where a plant runs as a workgroup, or Kerberos is not set up for these services, Windows uses NTLM for those sign-ins.**"*；Trout 引 Siemens：*"Microsoft is moving away from NTLM, and **Kerberos needs a domain with a Server Principal Name set**."* | Trout 快照逐字 | ✅ **已核** | ⭐⭐⭐ **这条给出了一个可自查的量化条件**：**工作组模式，或为这些服务未正确配置带 SPN 的域** → 才会走 NTLM。⭐⭐ **对我方的意义**：这不是"打开就中招"，而是**"部署形态决定是否暴露"** —— 域环境 + 正确 SPN + 强制的 Kerberos 即可规避。⭐⭐ **动作：我方若接触此类系统，资产台账必须新增"认证协议"字段（NTLM / Kerberos / 其他）**，否则无法判断暴露面 |
| 10 | 厂商协调与信用 | CISA：*"Republished vendor advisory… This ICSA is a verbatim republication of Siemens ProductCERT SSA-970803"*；Siemens 原始发布 **2026-11-10**；Trout 引 Siemens：*"Siemens SSA-970803, published November 10, 2026. Siemens credits **Tim Dijkman of Powerspex**."* | CISA 快照 + Defcon Level（Revision history：v1 2026-11-10 Publication Date；v2 2026-11-17 Initial CISA Republication）+ Trout | ✅ **已核（四源一致）** | ⭐ **CISA 明确声明这是厂商通告的逐字再发布，且"as-is"免责** → **条款级效力等于 Siemens 原始公告**。⭐ 漏洞由外部研究者发现并署名（不是厂商自检漏报）→ 说明这是**首次被外部发现并上报**的漏洞 |
| 11 | 在野利用状态 | 库内已记录的口径：**CISA 通告未提及在野利用**；rdintel 条目记 *"No exploitation signal observed yet… No active signal"*；EPSS 0.34% | 三源比对（rdintel 经 web_search 摘要核对） | ✅ **已核：无在野利用证据** | ⚠️ **必须写明：无在野利用、无 KEV 收录**（库内 11-19 日报已确立"是否在 KEV 里不是风险判据，联网可达才是"的判据 —— 这条恰好演示了这个判据：**7.5 分、AC:H、但仍不可放过**，因为它是"已部署在关键制造场景的 SCADA 历史库/报表系统 + 无补丁 + 缓解靠配置"） |
| 12 | 与库内既有 Siemens 条目的区别 | 库内已有 `icsa26316SiemensNode2Shell-2026-11.md`（ICSA-26-316-01~05，Node2Shell = Brotli 解码器越界写）、`icsa26321McpServerFirmwareCommandInjection-2026-11.md`（ICSA-26-321-11，固件更新工具命令注入） | 逐条比对 CVE、弱点类型、影响机制 | ✅ **确认为独立新事件** | ⭐⭐ **库内 Siemens 条目已有三条，但三条全是"内存破坏/命令注入"类**（可补丁）；**这条是第一条"认证协议层 + 无补丁 + 需配置"的 Siemens 条目** → **库内 Siemens 风险画像首次出现不可通过升级消除的一类** |

> **核查小结**：本文**全部条款逐字核对自 CISA 官方通告快照**，并用 Defcon Level 全文转载、Trout 深度分析、Aviatrix 攻击链分析**三源交叉验证**。**内部自洽核对通过**：`None available` 8 次 + `No fix planned` 6 次 = 14 = 受影响产品总数，**且缓解链接 14 次一一对应**。**五条必须写明的边界**：① **无在野利用、未入 KEV**；② **CISA 标注行业为"关键制造"，未点名能源**；③ **v3.1 7.5 与 v4 7.7 是两套口径，v4 为 Siemens 自评分**；④ **"中间位置"如何取得，所有源均未说明**；⑤ **我方无 Siemens SIMATIC 使用证据 → 不得下"我方受影响"结论，也不得下"我方不受影响"结论**。⭐⭐⭐ **本库从这条情报获得的最硬结论是：14/14 产品全部无修复，唯一缓解是配置 SQL 通信加密 —— 这要求我方资产台账从"记版本、记补丁"升级为"还要记缓解配置当前是否生效、记认证协议、记链路是否加密"。**

---

## 三、原文归档（快照）

- 快照文件：`raw/snapshots/security/cisa-icsa-26-321-08-simatic-ntlm.md`
- SHA256：`336c15533ae1c87ef87c7799a5bed5de0f2ac033f1f55edfed28c1bb51e0bc69`
- 抓取时间：2026-11-25 07:12:19 · 正文字符 11,342 · HTTP 200

**关键原文摘录（CISA ICSA-26-321-08，Release Date November 17, 2026）**：

> 「The products listed below contain an authentication bypass vulnerability that could allow an on-path attacker to take over the session of a legitimate user and execute arbitrary code with the privileges of the victim user. Siemens is preparing fixes and recommends specific mitigations for products where fixes are not or not yet available.
> …
> CVE-2026-58114: Affected systems do not properly secure their remote user authentication with the deprecated NTLM protocol. This could allow unauthenticated remote attackers, who have achieved a machine in the middle position, to relay NTLM authentication and impersonate a legitimate user. The potential impact depends on the services that are accessible, e.g. a SQL server used by WinCC.」
>
> 「Remediations Mitigation: Customers can manually configure the SQL Server Database for encrypting communication as described in https://support.industry.siemens.com/cs/mdm/109818202?c=145291786635&lc=en-ID」
>
> 「Product Status: known_affected｜Remediations: None available / No fix planned（WinCC V7.5 / V8.0 / V8.1 / WinCC Runtime Professional V20 / V21 = None available；SIMATIC BATCH V9.1 / Information Server 2020 / 2022 / PCS 7 V9.1 / Process Historian 2020 / 2022 = No fix planned）」

**关键原文摘录（Trout 第三方分析，2026-11-19）**：

> 「No product has a fix. WinCC and WinCC Runtime Professional have none yet. PCS 7 V9.1, BATCH V9.1, Process Historian and Information Server will not get one. The vendor's mitigation is to encrypt SQL Server traffic. The rest is on the network: stop NTLM and SQL traffic crossing zones, and control who reaches these servers.」
>
> 「Information Server is often read from the office network. In many plants, production and quality staff open its reports from business PCs. In our reading, that makes it one of the places where NTLM and SQL traffic most often crosses from IT into OT.」
>
> 「Where a plant runs as a workgroup, or Kerberos is not set up for these services, Windows uses NTLM for those sign-ins.」
>
> 「Siemens SSA-970803, published November 10, 2026. Siemens credits Tim Dijkman of Powerspex.」

---

## 四、概要提取

- ⭐⭐⭐ **14 个受影响产品全部无修复**（8 个 `None available` + 6 个 `No fix planned`），其中 PCS 7 / BATCH / Process Historian / Information Server 是 **"will not get one"（厂商明确不修）**。
- ⭐⭐⭐ **唯一缓解是手工配置 SQL Server 通信加密**（Siemens KB 109818202）—— **库内首条"不能靠升级、只能靠配置长期兜底"的 ICS 通告**。
- ⭐⭐⭐ **库内首条 NTLM 中继类漏洞**：攻击者**无需任何凭据**，只需站在中间位置即可中继认证、冒充合法用户、以其权限执行代码；CISA 点名 **WinCC 使用的 SQL Server** 是影响面关键。
- ⭐⭐⭐ **"办公网读报表"被明确写为 IT/OT 横向流量入口** —— 资产在网内并不可信，**访问行为本身**才是暴露面。
- ⭐⭐ **触发条件可自查**：工作组模式，或未为这些服务正确配置带 SPN 的域 → 才会走 NTLM；**域环境 + 正确 SPN + 强制 Kerberos 可规避**。
- ⭐⭐ **14 个产品 `vers:all/*` 全部受影响，无版本可逃逸**；**无在野利用、未入 KEV**；CVSS v3.1 7.5（AC:H）/ v4 7.7。
- ⭐⭐ **库内 Siemens 风险画像首次出现不可通过升级消除的一类**（此前三条 Siemens 条目全是可补丁的内存破坏/命令注入）。
- ⭐ **由外部研究者 Tim Dijkman（Powerspex）发现并署名上报**，非厂商自检漏报；CISA 声明为 Siemens SSA-970803 的逐字再发布。

---

## 五、主要观点

**原文主张**
- CISA / Siemens：所列产品未正确保护其基于已弃用 NTLM 协议的远程用户认证，处于中间位置的未认证远程攻击者可中继 NTLM 认证并冒充合法用户；影响取决于可达服务（如 WinCC 使用的 SQL Server）；**14 个产品无一有修复**，缓解手段是手工配置 SQL Server 通信加密，另有 Siemens 的工业安全操作指南与网络访问控制要求。
- Trout：没有任何产品有修复，4 个产品永远不会修；厂商缓解措施是加密 SQL Server 流量；其余只能靠网络 —— **让 NTLM 与 SQL 流量不跨区**、控制谁能到达这些服务器；**Information Server 常被从办公网读取报表，这使其成为 NTLM/SQL 流量最常从 IT 跨入 OT 的位置之一**；工作组模式或未配 SPN 时 Windows 使用 NTLM。
- Aviatrix：NTLM 中继是现成工具包可武器化的成熟手法；无补丁环境下，网络层补偿性控制（加密传输 + 严格东西向分段）是唯一可行的近期防御。

**我方判断**
- ⭐⭐⭐ **这条情报最该被记住的不是漏洞编号，而是它改变了"资产台账"该记什么**。库内 11-24 在 KEV 批次文档里已经提出"资产台账不能只记产品型号 + 是否在补丁清单，必须再记暴露面（是否联网可达）+ 是否多协议暴露"。**这条补上了第三个维度，而且是三个维度里最难补的一个：缓解配置当前是否生效。** ⭐⭐⭐ **理由很硬**：版本会升级、补丁会打上，**但"某系统的 SQL 通信今天是不是加密的"这件事不会随版本自动改变**；厂商写"当前无修复、以后也不会修"，等于把这个配置项永久地留在了每个部署现场。→ **我方台账如果没有这一列，就永远无法回答"这条路径现在还开着吗"。**
- ⭐⭐⭐ **"办公网读报表"这一条才是真正该引起我方注意的部分，它把库内两条一直并行的线合并了**。库内 11-16 记的 DER 暴露面研究说的是**资产暴露**（有多少设备直接联网），11-24 记的 EPICS 条目说的是**协议栈长期无认证**；**这条说的是第三种 —— 资产好好地在网内，但"从办公网访问它"这个业务动作本身，就把攻击者的中间位置给铺好了**。⭐⭐⭐ **对我方最实际的含义**：我方自己的 DER 监控平台、以及我方托管电站的集控/报表类系统，**如果存在"运维/客户从办公网或外网读取报表或直接访问监控"的路径，那条路径本身就是暴露面，与设备是否对公网开放无关**。→ **动作：P0 暴露面自查（`remediation-exposureHygiene-20261112`）的范围必须扩一个维度 —— 不只查"哪些站点对公网可达"，还要查"哪些系统被办公网访问、走什么认证、链路加不加密"。** 这一条完全满足评审第 1 关（影响可证，能指名道姓说出是哪个接口族、哪条链路）。
- ⭐⭐⭐ **"14/14 无修复 + 缓解靠配置"这个组合，对我方的护网/等保方向有一条非常具体的教训：不能修的漏洞，处置责任必须落到架构和运维流程上**。库内 11-20 的 libumqtt（维护者失联）当时得出的结论是"通用库修复 → OT 厂商滞后"；**这条把链条推到底了 —— 连厂商自己都不打算修**。⭐⭐ **对我方的意义**：**当一个风险既无补丁又无豁免路径时，唯一可持续的处置是把它变成一条常设的架构约束**（"该网段禁止跨区访问该系统"、"该链路必须加密"），**而不是留在一份 CVE 清单里等人来读**。⭐⭐ **这正好落在库内本阶段口径里的"网络安全 / 等保"方向级产物上**（基线 / 覆盖度 / 差距清单），**而且它天然需要一个责任人**（谁去确认 SQL 链路加密了？谁去核对域与 SPN 配置？）—— 这正是库内 11-24 日报里"期方向级产物的责任人待指派"那条待办可以着手填的具体对象。
- ⭐⭐ **"认证协议"必须成为我方台账的一等字段，这条给出了最低成本的填法**：不用做复杂资产测绘，**只要回答两个问题就能判断暴露面** —— ① 这台机器是域环境还是工作组？② 为该服务配置 SPN 了吗？⭐⭐ 因为 Trout 原文明确："工作组模式或未为这些服务设置 SPN 时，Windows 就会对那些登录使用 NTLM"。**这两个问题的答案直接决定是否命中这条漏洞**。→ **这是本期唯一一个"我方今天就能问出结论"的动作**，比任何扫描器都便宜。⭐⭐ **但必须同时说清边界：即使这两问答对了，也只排除了这一条漏洞，不等于该系统安全。**
- ⭐⭐ **关于优先级：这条在库内的排序不该按 CVSS 走**。7.5 分（AC:H）低于库内 vCenter 的 9.8，**但它同时具备三个"高分漏洞常常没有"的属性**：① 已在关键制造场景大规模部署（SCADA 监控与历史库）；② **永不复修**；③ 缓解手段是配置而不是升级 —— **配置项会被换人、改机、重装时悄悄丢掉**。⭐⭐ **库内 11-19 已确立的判据是"联网可达性优先于 KEV 收录状态"，这条恰好演示了判据的正确性**：它没进 KEV、没在野利用，但**只要我方或我方客户的 OT 环境里有部署了 WinCC/PCS7/Process Historian/Information Server 的系统，且存在跨区访问路径，这条就成立**。→ **判据补充建议：把"是否存在修复路径"作为第三个排序维度**（可修 / 有变通 / 无解）。
- ⚠️ **必须保持的边界**：① **不得下"我方受影响"结论**（无使用证据），**也不得下"我方不受影响"结论**（无资产清单）；② **不得写成"官方点名能源行业"**（CISA 标注的是关键制造）；③ **"中间位置如何取得"所有源都未说明 → 不得臆测攻击手法**；④ **不得把 Trout 的"办公网读报表"当作厂商官方结论**（那是第三方分析，原文已标）；⑤ **本条不构成"立即修补"的动作** —— 它没有补丁可打。

---

## 六、参考意义

| 方向（网络安全/信创/等保/隐私保护/护网） | 可证事实 | 本阶段处理 |
|---|---|---|
| **网络安全** | ① 14/14 产品无修复、唯一缓解是手工配置 SQL 通信加密；② 攻击者无需凭据，只需中间位置；③ "办公网读报表"是 IT/OT 横向流量入口（Trout 明确表述）；④ 触发条件可自查（工作组模式 / 未配 SPN → 走 NTLM）；⑤ CISA 点名 WinCC 的 SQL Server 为影响关键点 | ✅ **可进评审（方向级）**。**影响可证**：库内 P0 暴露面自查产物（`remediation-exposureHygiene-20261112`）的对象是"我方对外站点"，本条证明**暴露面还包括"网内系统被办公网访问"这一维**；**动作明确**：① 资产台账新增两列 —— "缓解配置当前是否生效"与"认证协议（NTLM/Kerberos）"；② 暴露面自查范围增加"哪些 OT 系统被办公网访问、链路是否加密、认证协议为何"；③ 护网/等保方向的"无补丁不可修漏洞"须登记为**常设架构约束**并指定责任人（SQL 链路加密核对 + 域/SPN 配置核对各一名）。⭐ **产品级归属按本阶段口径不写**（库内无产品线特性材料），标 🟡 待复核 |
| **等保** | 同上 | 🟡 **待复核** —— "无补丁 + 仅配置缓解"的处置责任落点属等保整改范畴，但**库内无等保条款级依据**（无测评项映射材料）→ **仅登记观察，不产等保产物** |
| 信创 / 隐私保护 / 护网 | 无可证事实 | ❌ **不适用**（本条无信创、无隐私、无护网方向的可证事实） |

---

## 七、总结输出

**一句话结论**：**CISA ICSA-26-321-08（Siemens SIMATIC NTLM 中继，CVE-2026-58114）揭示的不是又一个漏洞，而是一类我方台账尚未能表达的资产属性 —— 14 个受影响产品全部无修复、唯一缓解是手工配置 SQL 通信加密，而攻击者无需任何凭据、只需站在中间位置，并且"从办公网读报表"这一日常业务动作正是 IT/OT 横向流量的入口；因此我方资产清单必须从"记版本、记补丁"升级为"还要记缓解配置是否生效、记认证协议、记哪些网内系统被办公网访问"（工作组模式 / 未配 SPN → 走 NTLM 是两个最低成本的判断问句），并把这类"永不复修"的 ICS 风险登记为有责任人的常设架构约束。**

**落地去向**
- [ ] 产品特性
- [ ] 需求变更
- [x] 专项整改

---

## 参考链接

- [CISA ICS Advisory ICSA-26-321-08：Siemens SIMATIC](https://www.cisa.gov/news-events/ics-advisories/icsa-26-321-08)
- [Trout：Siemens SIMATIC WinCC, PCS 7 and Process Historian: NTLM Relay With No Fix (ICSA-26-321-08)](https://www.trout.software/blog/siemens-simatic-wincc-ntlm-relay-icsa-26-321-08)
- [Defcon Level：CISA Cybersecurity Advisories — Siemens SIMATIC (ICSA-26-321-08) 全文转载](https://www.defconlevel.com/alert/2026-11-17-cisa-cybersecurity-advisories-siemens-simatic-icsa-26-321-08)
- [Aviatrix：Siemens SIMATIC NTLM Authentication Bypass: 14 ICS Products Exposed with No Patch in Sight](https://www.aviatrix.ai/threat-research-center/icsa-26-321-08-siemens-simatic-cve-2026-58114-ntlm-authentication-bypass)
- [库内相关：CISA ICSA-26-316-01~05 Siemens Node2Shell / PHP2Shell（2026-11，可补丁类）](icsa26316SiemensNode2Shell-2026-11.md)
- [库内相关：CISA ICSA-26-321-11 meta-iot2050 固件更新工具命令注入](icsa26321McpServerFirmwareCommandInjection-2026-11.md)
- [库内相关：CISA KEV 2026-11-20 批次四条（"认证边界本身失效"主线 · 资产台账缺"暴露面"维度）](cisaKev20261120Batch-2026-11.md)
- [库内相关：CISA ICSA-26-323-03 libumqtt 整数下溢（无补丁 · 维护者失联）](libumqttCve2026125132-2026-11.md)
- [库内相关：EPICS 工控漏洞 + 光伏 DER 暴露面（IT/OT 暴露面主线）](epicsDerExposure-2026-11.md)
- [库内产物：对外站点暴露面专项自查（P0 · 现有范围仅覆盖"对外可达"）](../deliverables/remediation-exposureHygiene-20261112.md)

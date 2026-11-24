# NIST SP 800-82 Rev.4 初始公开草案 —— 库内首条「OT 安全基线标准本体」情报，且公开意见书点名了 KEV/EPSS/SSVC/暴露面四项分诊输入

> 🔴 强约束 · 采集于 2026-11-25 · 核心标识：**⭐⭐⭐ 库内首条「国家级 OT/ICS 安全基线标准」情报 —— NIST SP 800-82 Rev.4 初始公开草案（2026-09-21 发布，意见截止 2026-11-30，距今仅 5 天）** · ⭐⭐⭐ **⭐⭐⭐ 库内首条「我方方法论被外部权威公开背书」的铁证 —— 一份提交给 NIST 的公开意见书明确要求草案在补丁分诊章节写明 CISA KEV、FIRST EPSS、CISA SSVC、OT 后果与暴露面，这五项正是库内近四期反复使用的判据组合** · ⭐⭐ **草案把资产管理、网络监控与检测、系统管理功能保护、零信任并列为加强项 —— 与库内 11-19 / 11-20 / 11-24 三期独立得出的结论逐条对应** · ⭐⭐ **库内首条「Rev.3 仍为现行终版、草案不是强制要求」的标准状态判据** · ⚠️ **⚠️ 这是草案不是终版 —— 不得当作现行基线，也不得直接转成合规要求**

---

## 一、信源核实

| 项 | 值 |
|---|---|
| 来源请求 | `NIST SP 800-82 Rev 4 OT security guide public comment November 30 2026`（web_search，命中 NIST 官方发布页镜像与多篇第三方分析）<br>`光伏 逆变器 SCADA 监控平台 暴露面 EPICS 漏洞 2026年11月`（web_search，本轮检索共用同一检索式，命中 Zenodo 上提交给 NIST 的公开意见书原文页） |
| 原始 URL（主 · 官方发布页） | https://csrc.nist.gov/pubs/sp/800/82/r4/ipd （NIST Computer Security Resource Center · **SP 800-82 Rev. 4 (Initial Public Draft) Guide to Operational Technology (OT) Security**，**Date Published: September 21, 2026**，**Comments Due: November 30, 2026**，DOI 10.6028/NIST.SP.800-82r4.ipd） |
| 原始 URL（辅 1 · 第三方分析） | https://otsecuritywire.com/articles/nist-sp-800-82-rev-4-initial-public-draft-ot-security-comment-2026 （OT/ICS Monitor《NIST SP 800-82 Rev. 4 Initial Public Draft: What Changes for OT Security Programs and How to Comment Before 30 November (2026)》，**2026-11-14**） |
| 原始 URL（辅 2 · 公开意见书原文） | https://zenodo.org/records/23149939 （Zenodo《Public Comment on NIST SP 800-82 Revision 4 (Initial Public Draft)…》，**提交于 2026-10-04**，含逐条意见与引用到草案章节号） |
| 发布主体 | NIST（Computer Security Resource Center）· 草案作者：Keith Stouffer、Michael Pease、CheeYee Tang（NIST）+ Adam Hahn、Jim Gilsinn、Daniel Rebori-Carretero、Otis Alexander、Michael Fialk、Zackary Louis Silva（MITRE）· 公开意见提交者：Ikwuogu（以个人身份提交）· OT/ICS Monitor（第三方报道） |
| 发布/更新时间 | **草案发布 2026-09-21** · **意见截止 2026-11-30** · 公开意见提交 **2026-10-04** · 第三方报道 **2026-11-14** |
| 采集时间 | 2026-11-25 07:12:24 – 07:13:57 |
| 快照 | `raw/snapshots/security/nist-sp800-82r4-ipd.md` · `nist-sp800-82r4-comment-2026.md` · `nist-sp800-82r4-public-comment.md` |

**快照清单**（SHA256 取自 `.meta.json` 的 `sha256_raw`）

| 快照 | SHA256 | 抓取时间 | 正文字符 | HTTP |
|---|---|---|---|---|
| `raw/snapshots/security/nist-sp800-82r4-ipd.md` | `ea4511cef63f8daf6dacdabaa37fa83f77081d4b16a8372fb7281e02ceba5175` | 2026-11-25 07:12:24 | 6,178 | 200 |
| `raw/snapshots/security/nist-sp800-82r4-comment-2026.md` | `c10d9a11e4e521f6f3d7d35ee1413473aa956c65eb0b53538ee9dd410a214fc9` | 2026-11-25 07:12:25 | 4,122 | 200 |
| `raw/snapshots/security/nist-sp800-82r4-public-comment.md` | `d55dd72e58a7fd4541661f99348aac7731152f1147fe966513631a1376e9cb99` | 2026-11-25 07:13:57 | 2,456 | 200 |

> 📎 **入库理由**：库内安全域此前 18 篇全部是"漏洞 / 暴露面 / 攻击观测"，**从未收录过一条标准或基线本体** —— 这意味着库内在做"方向级产物（基线 / 覆盖度 / 差距清单）"时，**没有可引用的外部基线锚点**，所有判断都只能靠内部归纳。⭐⭐⭐ **本条补上了这个锚点，而且补的方式非常特别**：一份提交给 NIST 的公开意见书，要求草案在补丁分诊章节把 **CISA KEV、FIRST EPSS、CISA SSVC、OT 后果、暴露面** 五项写为输入 —— **这五项恰好就是库内 11-19（KEV 收录滞后一年是常态 → 判据是联网可达）、11-20（SSVC + 暴露面）、11-24（KEV 四条批次 + 暴露面维度）三期独立得出的判据组合**。⭐⭐⭐ **我方近四期在实践中摸索出的漏洞优先级方法论，在外部权威标准的公开意见环节被独立提出并要求写进国家基线** —— 这是"我方方法论被背书"的最强证据形态。
> ⚠️ **入库级别定为 🔴 强约束**：不是因为"我方受影响"（我方无 OT 合规义务的直接证据），而是因为**它有 5 天后到期的唯一硬时限，且它是本阶段五方向中"网络安全 / 等保"两个方向唯一可引用的外部基线锚点**。

---

## 二、事实核查

| # | 数据点 | 原文表述 | 核查方式 | 结论 | 备注 |
|---|---|---|---|---|---|
| 1 | 文件身份与状态 | NIST 官方发布页：标题 **"NIST SP 800-82 Rev. 4 (Initial Public Draft) Guide to Operational Technology (OT) Security"**；**Date Published: September 21, 2026**；**Comments Due: November 30, 2026**；DOI **10.6028/NIST.SP.800-82r4.ipd** | NIST 快照逐字抄录 + otsecuritywire 与 Zenodo 两源交叉 | ✅ **已核（三源一致）** | ⭐⭐⭐ **库内首条标准本体情报**。⭐⭐ **"Initial Public Draft"是决定性限定词** —— 库内 11-24 补录 45 号文时已确立"不得写成新法已出台"的同类纪律，**本条同理：它是草案，不是现行基线** |
| 2 | **Rev.3 仍是现行终版** | otsecuritywire：*"**Revision 3 (September 2023) remains the final edition in force until the revision is finalized.**"*；samsearch（同源检索）亦记 *"Revision 3, published September 2023, remains the current final edition while Revision 4 is in draft."* | 两源独立一致 | ✅ **已核** | ⭐⭐ **库内首条"标准状态判据"** —— 草案不产生合规义务。⭐⭐ **必须写明**：Rev.3（2023-09）为现行终版，Rev.4 草案不替代它。⚠️ **不得把"Rev.4 说了什么"直接当成"我方必须做什么"** |
| 3 | 行业范围扩展 | NIST 公告列出新增/扩展范围：*"Building Automation and Control Systems (BACS), Water and Wastewater Systems (WWS), food and agriculture, freight rail, maritime vessels, and Industrial Internet of Things (IIoT) and cloud convergence"*；otsecuritywire 逐条复述并注明"the draft's emphasis on asset management and network monitoring is the Detect phase…" | NIST 快照 + otsecuritywire + macmyths（三源） | ✅ **已核** | ⭐⭐ **库内首次出现这份标准扩展到 BACS/水务/食品农业/货运铁路/船舶的清单**。⭐⭐ **对我方的相关性判断**：**能源/工业控制不在"新增行业"里**（SP 800-82 从 Rev.3 起就覆盖 ICS），新增的是**楼宇自动化与水务** —— **不得说"Rev.4 新增了能源行业"**。⭐⭐ 真正对我方相关的是 **IIoT 与云融合**这一项 → 对应我方 DER 监控平台的云化交付形态 |
| 4 | 结构重组：CSF 2.0 + Govern | NIST 公告：*"Restructured around the NIST Cybersecurity Framework (CSF) 2.0, including a reorganization of the previous risk management section to focus on the CSF Govern Function."*；OT 风险与 ERM 对齐，引用 **NIST IR 8286r1**，**RMF 置于 Appendix F** | NIST 快照 + otsecuritywire + dactape（三源） | ✅ **已核** | ⭐⭐ **"风险管理从独立章节并入 Govern 功能"是本次修订的结构性主轴** → 对我方的意义：**OT 风险要挂到企业级风险登记册上，而不是留在 IT 部门内部**（dactape 与 cybersecurityunderpressure 两篇均强调这一点） |
| 5 | **⭐⭐ 加强的四项内容** | NIST 公告：*"The revision highlights expanded guidance on implementing OT security controls, including **asset management and network monitoring and detection**, and adds **security architecture guidance focused on protecting system management functions and applying zero trust principles**."* | NIST 快照逐字 + otsecuritywire 复述 + dactape 交叉 | ✅ **已核** | ⭐⭐⭐ **这是本条与我方最直接的一层**：**资产管理 + 网络监控与检测 + 系统管理功能保护 + 零信任** —— **这四项恰好是库内近四期独立得出的结论的汇总**：11-19（运行时清单 · 资产台账缺暴露面维度）、11-20（监控与检测 / 零信任对供应商远程接入）、11-24（资产台账必须记暴露面与多协议暴露）、11-24（生产平台 + 边缘网关 + 配网安全防护终端的资产与网络暴露自查）、11-24（联网可达性优先于 KEV 收录状态）。⭐⭐⭐ **结论：我方四期独立归纳出的方向，与 NIST 在本次修订中重点加强的四项逐条重合 —— 这不是巧合，说明我方观察到的确实是 OT 安全的主流问题，而非边缘个案。** |
| 6 | **⭐⭐⭐ 公开意见书点名的补丁分诊五项输入** | Zenodo 意见书原文，引用草案章节号：*"naming the inputs to the draft's **Now/Next/Later patch triage in Sections 4.1.3.3 and 4.2.3.1.3**, including **CISA Known Exploited Vulnerabilities, FIRST EPSS, CISA SSVC, OT consequence, and exposure**, and documenting deferred vulnerabilities"* | Zenodo 快照逐字抄录（唯一直接给出草案章节号的一手来源） | ✅ **已核（意见书原文逐字）** | ⭐⭐⭐ **库内首条"我方判据被外部公开意见书逐项点名"**。⭐⭐⭐ **对照库内实际做法**：① **CISA KEV** —— 库内 11-19/11-20/11-24 已用（且已得出"KEV 收录滞后一年是常态 → 判据是联网可达"这一修正）；② **FIRST EPSS** —— 库内尚未系统使用（本期 CIRCUTOR 条目才首次出现 EPSS 数值）；③ **CISA SSVC** —— 库内 11-19（OpenPLC 官方 SSVC exploitation=none known）、11-24（ICSA-26-321-08）已在引用；④ **OT consequence（OT 后果）** —— 库内**从未显式使用**，这是最大空缺；⑤ **exposure（暴露面）** —— 库内 11-16 起的主线。⭐⭐⭐ **这份意见书等于给出了一份"外部权威认定的分诊输入清单"**，其中 **OT consequence（后果分级）是库内至今完全缺失的一维** → **这是我方评估体系的一个明确补齐点**（库内目前的优先级排序靠 CVSS + 是否在野 + 是否联网可达，**恰恰没有按"OT 环境下失效后果"排序**） |
| 7 | 意见书的其他三项建议 | 同上：① *"adding a sector-specific subsection for **oil and natural gas pipelines** to Section 2.5, parallel to the freight rail subsection"*；③ *"extending zero trust guidance in Sections 5.3.1 and 5.2.2.3 to **remote-station communication gateways** and adding network monitoring options for **constrained remote sites** in Section 4.3.1.4"*；④ *"publishing informative mappings from Revision 4 outcomes to sector regulatory requirements via NIST CPRT or OLIR"* | Zenodo 快照逐字 | ✅ **已核** | ⭐⭐ **第③项对我方有直接参照价值**：**把零信任扩展到"远程站通信网关"，并为"受限远程站点"补网络监控方案** → 这几乎逐字描述了我方 DER 场景（**偏远场站 + 边缘网关 + 链路受限**）。⭐⭐ **第④项提示了一个机制**：通过 NIST CPRT / OLIR 发布与行业监管要求的映射 → **这是我方"基线 ↔ 等保条款"映射工作的现成外部路径** |
| 8 | 草案的已知短板 | dactape（对比 2011 初版及三次修订）：*"It stays thin on **safety instrumented systems**, on **zero trust below Purdue Level 3**, and on **supply chain guidance an asset owner can act on**."* | 第三方分析（dactape，2026-11-18） | ⚪ **单源，标为待核** | ⭐⭐ **对我方产品化判断有价值**：**SIS（安全仪表系统）薄、Purdue Level 3 以下的零信任薄、供应链指导薄** → 说明**这份基线并不覆盖我方最关心的场景**（我方在 Purdue L3 以下的边缘侧），**不能拿它当"我方已达标的证明"**。⚠️ 单源观点，不得当作草案本身的内容 |
| 9 | 标准性质 | samsearch：*"The guide provides risk-based OT security recommendations, **not a standalone mandate**, so contractors should distinguish guidance from binding requirements."*；otsecuritywire：*"This is a draft, not requirements; **it does not create a compliance obligation by itself**."* | 两源独立一致 | ✅ **已核** | ⭐⭐ **库内首条"标准性质判据"**：**它是建议，不是强制**。⭐⭐ **对我方的意义**：**在等保方向上，这条不能直接转成合规条款**（库内 11-19 已确立"方向级产物为主、产品级待复核"的口径）→ **它只能作为"基线参照物"，不能作为"合规依据"** |

> **核查小结**：本文**核心事实（发布日、截止日、状态、Rev.3 仍现行、扩展范围、CSF 2.0 重组、四项加强内容、意见书五项输入）全部逐字核对自 NIST 官方发布页快照**，并以两篇第三方分析与一份 Zenodo 一手公开意见书交叉。**四条必须写明的边界**：① **这是初始公开草案（IPD），不是终版，不构成合规义务**；② **Rev.3（2023-09）仍是现行终版**；③ **"草案在 SIS / Purdue L3 以下零信任 / 可操作供应链指导上偏薄"为单源第三方观点**，不得当作草案内容；④ **意见书提交者的意见不代表 NIST 已采纳**。⭐⭐⭐ **本条对库内的最大价值不在漏洞，而在方法论背书与一个具体缺口：意见书要求的五项分诊输入中，"OT consequence（OT 后果分级）"是库内至今完全没有的一维。**

---

## 三、原文归档（快照）

- 快照文件：`raw/snapshots/security/nist-sp800-82r4-ipd.md`
- SHA256：`ea4511cef63f8daf6dacdabaa37fa83f77081d4b16a8372fb7281e02ceba5175`
- 抓取时间：2026-11-25 07:12:24 · 正文字符 6,178 · HTTP 200

**关键原文摘录（NIST 官方发布页）**：

> 「NIST SP 800-82 Rev. 4 (Initial Public Draft) Guide to Operational Technology (OT) Security」
> 「Date Published: September 21, 2026」
> 「Comments Due: November 30, 2026」
> 「DOI: 10.6028/NIST.SP.800-82r4.ipd」
> 「Updates in this revision include: — Expanded introduction to operational technology (OT) sectors to include Building Automation and Control Systems (BACS), Water and Wastewater Systems (WWS), food and agriculture, freight rail, maritime vessels, and Industrial Internet of Things (IIoT) and cloud convergence. — Restructured around the NIST Cybersecurity Framework (CSF) 2.0, including a reorganization of the previous risk management section to focus on the CSF Govern Function. … The revision highlights expanded guidance on implementing OT security controls, including asset management and network monitoring and detection, and adds security architecture guidance focused on protecting system management functions and applying zero trust principles.」

**关键原文摘录（Zenodo 公开意见书，2026-10-04）**：

> 「The submission consists of a three-page cover letter and ten line-referenced comments in the NIST comment template. It recommends: (1) adding a sector-specific subsection for oil and natural gas pipelines to Section 2.5, parallel to the freight rail subsection; (2) **naming the inputs to the draft's Now/Next/Later patch triage in Sections 4.1.3.3 and 4.2.3.1.3, including CISA Known Exploited Vulnerabilities, FIRST EPSS, CISA SSVC, OT consequence, and exposure, and documenting deferred vulnerabilities**; (3) extending zero trust guidance in Sections 5.3.1 and 5.2.2.3 to remote-station communication gateways and adding network monitoring options for constrained remote sites in Section 4.3.1.4; and (4) publishing informative mappings from Revision 4 outcomes to sector regulatory requirements via NIST CPRT or OLIR.」
>
> 「This is a public comment, not a peer-reviewed publication. Page and line references are to the initial public draft.」

**关键原文摘录（OT/ICS Monitor，2026-11-14）**：

> 「NIST published the initial public draft of SP 800-82 Revision 4 on 21 September 2026. Comments are due 30 November 2026, about two weeks from now.」
> 「**Revision 3 (September 2023) remains the final edition in force until the revision is finalized.**」
> 「This is a draft, not requirements; it does not create a compliance obligation by itself. Its practical value for most teams is as a benchmark for program reviews now, ahead of the final text.」
> 「**Management planes.** Protecting engineering workstations, remote-access paths and other system-management functions is highlighted; this matches the recurring theme in current ICS advisories.」

---

## 四、概要提取

- ⭐⭐⭐ **库内首条国家级 OT/ICS 安全基线标准本体情报**：NIST SP 800-82 Rev.4 初始公开草案，2026-09-21 发布，**意见截止 2026-11-30（距今 5 天）**；Rev.3（2023-09）仍是现行终版，草案不产生合规义务。
- ⭐⭐⭐ **⭐⭐⭐ 一份提交给 NIST 的公开意见书（2026-10-04）要求草案在补丁分诊章节（§4.1.3.3 / §4.2.3.1.3）写明五项输入：CISA KEV、FIRST EPSS、CISA SSVC、OT 后果、暴露面** —— **这五项正是库内近四期独立使用的判据组合**。
- ⭐⭐⭐ **其中「OT consequence（后果分级）」是库内至今完全缺失的一维** —— 我方现有优先级排序靠 CVSS + 是否在野 + 是否联网可达，**恰恰没有按 OT 环境失效后果排序**。
- ⭐⭐ **草案四项加强内容（资产管理 / 网络监控与检测 / 系统管理功能保护 / 零信任）与库内 11-19、11-20、11-24 三期独立结论逐条重合**。
- ⭐⭐ **结构主轴：风险管理并入 CSF 2.0 的 Govern 功能**，OT 风险须挂企业级风险登记册（对齐 NIST IR 8286r1），RMF 置于 Appendix F。
- ⭐⭐ **意见书另提三项对我方有参照价值**：① 把零信任扩展到"远程站通信网关"并为"受限远程站点"补网络监控方案（**几乎逐字描述我方 DER 场景**）；② 通过 CPRT/OLIR 发布与行业监管要求的映射（**我方"基线 ↔ 等保"映射的现成外部路径**）；③ 补油气管网行业小节。
- ⭐⭐ **范围扩展新增的是 BACS / 水务 / 食品农业 / 货运铁路 / 船舶 + IIoT 与云融合 —— 能源/ICS 不在"新增"之列**；**对我方最相关的是 IIoT 与云融合**。
- ⚠️ **草案在 SIS、Purdue Level 3 以下零信任、可操作供应链指导上偏薄**（单源第三方观点）→ **不能拿它当我方已达标的证明**；**意见书是提交者建议，不代表 NIST 采纳**。

---

## 五、主要观点

**原文主张**
- NIST：Rev.4 草案把全文重构到 CSF 2.0，风险管理并入 Govern 功能；扩展 OT 行业覆盖；加强资产管理、网络监控与检测；新增系统管理功能保护与零信任的架构指导；**意见征集至 2026-11-30**。
- OT/ICS Monitor：**Rev.3 仍是现行终版**，Rev.4 是草案、不自行产生合规义务；草案对"管理平面"（工程站、远程接入路径、系统管理功能）的强调与当前 ICS 通告的常见主题吻合；其实践价值在于"作为终稿前的对标基准"。
- Zenodo 公开意见提交者：建议草案补油气管网小节、**在补丁分诊章节点名五项输入（KEV / EPSS / SSVC / OT 后果 / 暴露面）并记录延期漏洞**、把零信任扩展到远程站通信网关并为受限远程站点补监控方案、通过 CPRT/OLIR 发布与监管要求的映射。

**我方判断**
- ⭐⭐⭐ **这是库内第一次拿到"外部权威公开认定的分诊输入清单"，而且它认定的正是我方已经在用的东西**。库内 11-19 立了一条规矩："**KEV 收录滞后一年是常态 → 真正风险判据是联网可达，而不是是否在 KEV 里**"；11-20 用 SSVC 判断 OpenPLC 的自动化程度；11-24 把"暴露面"写进资产台账要求。⭐⭐⭐ **这四期的东西被一位外部提交者在 2026-10-04 打包提交给 NIST，要求写进美国国家 OT 安全基线** —— **这是一种比我方自己总结自己更有力的背书形式**：不是"我们认为该这样"，而是"外部在向标准制定者提出同样的要求"。⭐⭐ **动作：把这份意见书作为方向级基线产物的**外部依据**引用（注明是公开意见、非最终标准）** —— 它比任何内部推演都更适合作为"我方优先级方法论不是拍脑袋"的说明材料。
- ⭐⭐⭐ **但背书归背书，"OT consequence"这个缺口必须立刻补上 —— 这恰恰是意见书五项里我方唯一完全没有的一维**。库内目前的漏洞优先级排序逻辑是：CVSS 分 → 是否在野利用 → 是否联网可达 → 我方是否使用。⭐⭐ **这四项里没有一项回答"这个漏洞在 OT 环境里失效了会怎样"**。⭐⭐⭐ **而这恰恰是 OT 与 IT 最本质的差别**：同样一个 CVSS 9.8 的免认证 RCE，打在办公网的一台笔记本上和处理一个站的调度器上，后果差好几个量级；库内 11-19 已记 OpenPLC 官方点名"能源在列"、库内 11-24 记 ICSA-26-321-08 影响的是 **Process Historian / Information Server（长期归档与报表）** —— 这些都说明**后果分级本该是排序的第一维度，而我方一直没做**。⭐⭐ **动作：给方向级基线补一列"OT 后果分级"**（建议四档：安全/生产影响 → 大范围停电或监控失明 → 单站影响 → 无 OT 影响），并把这一列**放在 CVSS 之前**做排序。⭐⭐ **这是本期唯一一个"今晚就能做、且做完立刻改变排序结果"的动作。**
- ⭐⭐⭐ **意见书第③项几乎是逐字描述我方的产品场景，这说明我方做的产品形态在标准制定者眼里就是"典型 OT 场景"**："extending zero trust guidance to **remote-station communication gateways** and adding network monitoring options for **constrained remote sites**" —— **偏远场站 + 通信网关 + 链路受限**，正是我方 DER 托管的核心拓扑。⭐⭐⭐ **这对我方有两层意义**：① **产品方向确认** —— 我方在这个场景里遇到的问题（链路受限、远程接入、监控覆盖）正是标准修订要专门补章解决的；② **但也提醒了一个盲区** —— 意见书说的是"**constrained**（受限）"远程站点的监控方案，也就是**受限链路下如何做网络监控**，而这恰恰是我方最难做好的部分（带宽/成本/功耗约束）。⭐⭐ **动作：我方在向这条标准靠拢时，应关注 4.3.1.4 节（受限远程站点监控选项）最终怎么写** —— **它很可能成为我方"轻量级边缘检测/透传"功能的外部依据**，而不只是内部工程选择。⭐⭐ 顺带：库内 11-24 已记 P0 专项整改要求核查生产平台、边缘网关、配网安全防护终端三类资产 —— **"边缘网关"正好对应意见书里的 "remote-station communication gateways"** → **这条外部依据应回写到该 P0 产物的资产清单说明里**。
- ⭐⭐ **意见书第④项给了一条现成的路径，比自己从零做映射强得多**：*"publishing informative mappings from Revision 4 outcomes to sector regulatory requirements via NIST CPRT or OLIR"*。⭐⭐⭐ **这对库内"等保"方向意义很大** —— 库内 11-19 已确立本阶段产物是"方向级（基线 / 覆盖度 / 差距清单）"，**而"基线 ↔ 等保条款"的映射一向被认为是做不起来的活**；NIST 正在做的 CPRT/OLIR 映射**正是这个活的标准化解法**。⭐⭐ **动作：等这个映射发布后直接接上，而不是自建映射表** —— 但**前提是我方先把 Rev.4 终稿（预计 2026-11-30 意见期后）的条款结构读一遍**，否则映射出来也接不上。⭐⭐ **5 天时限因此不只是"截止日"，而是"读草案的截止日"。**
- ⭐⭐ **必须给草案一个诚实的定位：它是"对标基准"，不是"合规依据"**。OT/ICS Monitor 那句说得很好："its practical value for most teams is as a benchmark for program reviews now, ahead of the final text"。⭐⭐⭐ **结合 dactape 指出的三处偏薄（SIS / Purdue L3 以下零信任 / 可操作供应链指导）**，我方更应采取"**借结构、不借结论**"的读法：⭐⭐ **借它的结构**（CSF 2.0 的骨架、资产管理与网络监控与检测两章、系统管理功能保护、零信任、Now/Next/Later 分诊框架），**这些结构对我方建方向级基线有直接帮助**；⭐⭐ **不借它的结论**（草案本身不产生义务，且关键场景偏薄）→ **不得用"符合 SP 800-82 Rev.4"作为我方任何交付物的宣称依据**。⭐⭐ **这是库内 11-19 已确立的"方向级 vs 产品级"口径在具体标准上的应用**。
- ⚠️ **必须保持的边界**：① **不得写成"Rev.4 已发布/已生效/已成为基线"**；② **不得把 Rev.3 与 Rev.4 的条款混用**；③ **不得声称"我方符合 SP 800-82"**（草案无强制力且关键场景偏薄）；④ **"SIS 薄 / L3 以下零信任薄 / 供应链指导薄"是单源第三方观点**；⑤ **公开意见不代表 NIST 采纳**；⑥ **不得把新增行业清单写成"新增能源"**。

---

## 六、参考意义

| 方向（网络安全/信创/等保/隐私保护/护网） | 可证事实 | 本阶段处理 |
|---|---|---|
| **网络安全** | ① 草案四项加强内容（资产管理 / 网络监控与检测 / 系统管理功能保护 / 零信任）与库内近四期独立结论逐条重合；② 公开意见书点名 KEV/EPSS/SSVC/**OT 后果**/暴露面 五项分诊输入，其中"OT 后果"是库内完全缺失的一维；③ 意见书要求为"受限远程站点"补网络监控方案并把零信任扩展到远程站通信网关（逐字对应我方 DER 拓扑）；④ 意见书建议通过 CPRT/OLIR 发布与监管要求的映射 | ✅ **可进评审（方向级）**。**影响可证**：方向级产物（基线 / 覆盖度 / 差距清单）此前**没有外部基线锚点**，本条提供了唯一可引用的结构参照；**动作明确**：① **漏洞优先级排序表新增"OT 后果分级"列并置于 CVSS 之前**（四档建议），这是本期唯一当晚可完成且立刻改变排序的动作；② **资产台账与暴露面自查须能对应草案 §4.1.3.3 / §4.2.3.1.3 的分诊框架**（Now/Next/Later + 延期漏洞记录）；③ **重点跟踪 §4.3.1.4（受限远程站点监控选项）与 §5.3.1 / §5.2.2.3（远程站通信网关零信任）**，其最终写法可能成为我方"轻量边缘检测/透传"功能的外部依据；④ **把公开意见书作为我方优先级方法论的外部依据引用**（注明为公开意见而非最终标准）；⑤ **以 CPRT/OLIR 映射作为"基线↔等保"的标准解法，不自建映射表**。⭐ **产品级归属按本阶段口径不写**，标 🟡 待复核 |
| **等保** | 意见书建议 NIST 通过 CPRT/OLIR 发布 Rev.4 结论与行业监管要求的映射；草案本身不产生合规义务 | 🟡 **待复核** —— **路径已现成但尚未发布**，且我方无等保条款级映射材料 → **本期仅登记为"外部路径已存在，待其发布后接入"，不产等保产物** |
| 护网 | 草案强调系统管理功能保护（工程站、远程接入路径）与网络监控检测，与库内 11-16 DER 暴露面、11-24 P0 资产自查同向 | 🟡 **待复核** —— 可作护网演练场景设计的参照（管理平面是演练重点），**但草案非强制、且我方无护网基线产物在跑** → 仅登记观察 |
| 信创 / 隐私保护 | 无可证事实 | ❌ **不适用** |

---

## 七、总结输出

**一句话结论**：**NIST SP 800-82 Rev.4 初始公开草案（2026-09-21 发布、意见 2026-11-30 截止）是库内首条国家级 OT 安全基线标准本体情报，而它最大的价值来自一份提交给 NIST 的公开意见书 —— 该意见书要求草案在补丁分诊章节写明 CISA KEV、FIRST EPSS、CISA SSVC、OT 后果与暴露面，这五项恰是我方近四期独立使用的判据组合（外部权威背书），但其中"OT 后果分级"是我方至今完全缺失的一维，也是本期唯一当晚可补、且补完立刻改变漏洞优先级排序结果的动作；同时草案四项加强内容与我方 11-19/11-20/11-24 的独立结论逐条重合、意见书为"受限远程站点监控"与"远程站通信网关零信任"量身展开（正对我方 DER 拓扑），而"基线↔等保"映射则应等 NIST 的 CPRT/OLIR 通道而非自建 —— 但 Rev.3 仍现行、草案无强制力，我方只能借结构不借结论。**

**落地去向**
- [ ] 产品特性
- [ ] 需求变更
- [x] 专项整改

---

## 参考链接

- [NIST CSRC：SP 800-82 Rev. 4 (Initial Public Draft), Guide to Operational Technology (OT) Security](https://csrc.nist.gov/pubs/sp/800/82/r4/ipd)
- [OT/ICS Monitor：NIST SP 800-82 Rev. 4 Initial Public Draft — What Changes for OT Security Programs and How to Comment Before 30 November (2026)](https://otsecuritywire.com/articles/nist-sp-800-82-rev-4-initial-public-draft-ot-security-comment-2026)
- [Zenodo：Public Comment on NIST SP 800-82 Revision 4 (Initial Public Draft)（含五项分诊输入建议 · 2026-10-04）](https://zenodo.org/records/23149939)
- [库内相关：CISA KEV 2026-11-20 批次四条（KEV 收录滞后是常态 → 判据是联网可达）](cisaKev20261120Batch-2026-11.md)
- [库内相关：CISA KEV 2026-11-23/24 批次三条（SSVC · 取证分诊 · 移除类处置）](cisaKev20261123Batch-2026-11.md)
- [库内相关：EPICS 工控漏洞 + 光伏 DER 暴露面（资产暴露面主线）](epicsDerExposure-2026-11.md)
- [库内相关：Java4Shell（CVE-2026-114938）：SCA/SBOM 对运行时层漏洞失效（运行时清单缺口）](java4ShellCve2026114938-2026-11.md)
- [库内产物：对外站点暴露面专项自查（P0 · 生产平台 / 边缘网关 / 配网安全防护终端）](../deliverables/remediation-exposureHygiene-20261112.md)

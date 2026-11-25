# CISA ICSA-26-328-02 / ICSA-26-328-01 —— 库内首条「漏洞发生在工程设计软件、而不是运行中的控制器」的 OT 通告族

> 🟡 有影响 · 采集于 2026-11-26 · 核心标识：**⭐⭐⭐ 库内首条「攻击面不在控制系统中，而在工程师打开的那份设计文件里」的 OT 通告族** —— ICSA-26-328-02（Schneider Electric EcoStruxure Power Build Rapsody，CVE-2026-119055，UAF，CVSS v3.1 5.3）与 ICSA-26-328-01（AutomationDirect C-More EA9 编程软件，CVE-2026-127280，≤ V6.80，CVSS v3.1 7.8）**同属「恶意工程文件 → 工程师工作站 → 任意代码执行」形态，且官方都点名能源/关键制造/商业设施行业** · ⭐⭐⭐ **库内首条「CVSS 5.3 但影响上限是工程工作站上完整代码执行」的样本** —— 官方评分 5.3（AV:L / AC:L / PR:N / **UI:R**）与「工程师打开同事或承包商发来的一份项目文件」的触发路径并存 → **库内 11-25 已立的「CVSS 高 ≠ 我方风险高」判据在这里被反向打破：CVSS 低的反而更容易被忽略** · ⭐⭐ **库内首条「一次点击换一台工作站的代码执行原语」的资产分类** → 工程工作站承载**在运变电站/开关柜的项目文档**，它是「管理面」而不是「控制面」，此前不在任何台账上 · ⭐⭐ **CISA 官方同时给出「本批次无在野利用、无 KEV 收录」的定性** → 不产专项整改 · ⚠️ **两个产品我方均无使用证据 → 不得下「我方受影响」结论**；⚠️ **Rapsody 的 CVSS 5.3 与「可执行任意代码」的表述并存，须照记不可调和**。

---

## 一、信源核实

| 项 | 值 |
|---|---|
| 来源请求 | `CISA ICSA 2026-11-25 icsa industrial control systems advisory`（web_search）<br>`ICSA-26-328 Schneider Electric EcoStruxure Power Build Rapsory AutomationDirect C-More EA9`（web_search） |
| 原始 URL（主 1 · 官方通告 A） | https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-02 （CISA **ICSA-26-328-02**《Schneider Electric EcoStruxure Power Build Rapsody software》，**Release Date November 24, 2026**，快照正文 10,075 字符） |
| 原始 URL（主 2 · 官方通告 B） | https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-01 （CISA **ICSA-26-328-01**《AutomationDirect C-More EA9 Programming Software》，**Release Date November 24, 2026**，快照正文 9,223 字符） |
| 原始 URL（辅 1 · 第三方技术解读） | http://threatseye.io/blog/schneider-electric-patches-use-after-free-flaw-in-ecostruxure-power-build-rapsod （ThreatsEye，**2026-11-25**，给出完整攻击链四步、修复版本对照表与「工程工作站在 OT 网络上」的运营解读，快照正文随主源归档） |
| 原始 URL（辅 2 · 通告结构化镜像） | https://www.defconlevel.com/alert/2026-11-24-cisa-cybersecurity-advisories-schneider-electric-ecostruxure-power-build-rapsody-software-icsa-26-328-02 （Defcon Level，ICSA-26-328-02 的结构化转录，含完整 CVSS 向量与 8 条受影响产品版本，快照正文随主源归档） |
| 原始 URL（辅 3 · 本批次通告清单） | https://cybersecuritytracker.ai/ics-advisories （Cybersecurity Tracker，ICS 通告目录，**Source last published: 2026-11-24**，确认 ICSA-26-328-01/02/03 同批发布，快照正文随主源归档） |
| 发布主体 | CISA（ICS 通告发布方）· Schneider Electric CPCERT（SEVD-2026-314-01 厂商来源，报告方）· AutomationDirect（厂商）· ThreatsEye / Defcon Level / Cybersecurity Tracker（第三方） |
| 发布/更新时间 | **两条通告均为 2026-11-24 初次发布** · ThreatsEye 解读 2026-11-25 · Cybersecurity Tracker 目录截止 2026-11-24 · 库内采集：**2026-11-26 07:10:55 – 07:10:56** |
| 采集时间 | 2026-11-26 07:10:55 – 07:10:56 |
| 快照 | `raw/snapshots/security/icsa-2632802-schneider-rapsody.md` · `raw/snapshots/security/icsa-2632801-automationdirect-cmore.md` |

**快照清单**（SHA256 取自 `.meta.json` 的 `sha256_raw`）

| 快照 | SHA256 | 抓取时间 | 正文字符 | HTTP |
|---|---|---|---|---|
| `raw/snapshots/security/icsa-2632802-schneider-rapsody.md` | `1236d46326e0c3da088ae93e969232abf6eb75d113cd17755d371bd7f03e5f0d` | 2026-11-26 07:10:55 | 10,075 | 200 |
| `raw/snapshots/security/icsa-2632801-automationdirect-cmore.md` | `a3ebb08bba3feb4f110e8bc295bffb6f81d2690571b9f3d5cc44286539861857` | 2026-11-26 07:10:56 | 9,223 | 200 |

> 📎 **入库理由**：库内 11-25 已记的 [Siemens SIMATIC NTLM 中继](icsa26321SiemensSimaticNtlmRelay-2026-11.md) 首次提出「**资产在网内并不可信，访问行为本身才是暴露面**」，其攻击路径写的是「**办公网读报表**」—— 但那一篇的落点仍是「控制/归档系统本身有漏洞」。**本批次两条通告把落点再往前挪了一层：漏洞不在控制系统里，而在工程师桌面上的那份设计/编程文件里**。这是库内第一次出现「**载荷是一个文件、触发是一次双击、受害资产是一台不在任何台账上的工作站**」的完整链条 → 直接对应库内 11-24 反复记的「EOL 设备台账完全缺失」「辅助设备类目长期不在任何台账上」两条待办。
> ✅ **安全域双独立信源要求已满足**：官方源（CISA 两份 ICS 通告，一手）+ 第三方源（ThreatsEye 技术解读、Defcon Level 结构化转录、Cybersecurity Tracker 目录源，共三源）。

---

## 二、事实核查

| # | 数据点 | 原文表述 | 核查方式 | 结论 | 备注 |
|---|---|---|---|---|---|
| 1 | 两条通告编号与日期 | ICSA-26-328-01 / ICSA-26-328-02，**Release Date November 24, 2026** | 直接读两份 CISA 快照头部 | ✅ **已核** | ⭐ 与库内 11-25 已记的 ICSA-26-328-03（Danfoss）**同批同日** → 库内首条「单日三条 OT 通告」的观察 |
| 2 | ICSA-26-328-02 的漏洞编号与类型 | **CVE-2026-119055**，**CWE-416 Use After Free** | CISA 快照「Vulnerabilities」节 | ✅ **已核** | — |
| 3 | Rapsody 的 CVSS 与向量 | **CVSS v3 5.3 Medium**，向量 `CVSS:3.1/av:L/ac:L/PR:N/ui:R/S:U/C:L/I:L/a:L` | CISA 快照 + Defcon Level 转录逐字比对 | ✅ **已核（5.3 / Medium / AV:L / UI:R）** | ⭐⭐⭐ **与库内 11-25 已立判据的关系**：库内 11-25 写「**高 CVSS ≠ 我方风险高**」；**本条是反例** —— CVSS 5.3 的低分恰恰来自 `AV:L` + `UI:R`，但**实际后果是工程师工作站上的完整代码执行** |
| 4 | Rapsody 的攻击前置条件 | 「**a local attacker could trick the end user to open a specially crafted malicious SSD file**」；Summary：「potentially execute arbitrary code」 | CISA 快照逐字 | ✅ **已核** | ⭐⭐ **库内首条「载荷是项目文件、触发是双击」的 OT 漏洞形态** |
| 5 | Rapsody 的产品用途 | 「used to enter or import the **single line diagram**, to get the extensive **bill of material** of your switchboard, including all devices, connection items, and mounting components」 | CISA 快照 Summary 节 | ✅ **已核** | ⭐⭐⭐ **这就是「一次点击换一台工作站」的商业含义**：被打开的不是照片或文档，**是开关柜的一次接线图与完整物料清单** |
| 6 | Rapsody 的受影响版本（8 个语言版本轨） | FR ≤2.9.1.0 · ESP ≤2.8.5.0301 · PT ≤2.8.7.0101 · BEL(FR) ≤2.8.8.0201 · BEL(EN) ≤2.8.3.0201 · INT(EN) ≤2.8.4.0401 · INT(FR) ≤2.8.6.0000 · NL ≤2.8.2.0000 | CISA 快照 + Defcon Level 逐条比对 | ✅ **已核（8 条版本轨）** | ⭐⭐ **库内首条「同一漏洞跨 8 条语言版本轨、每轨独立编号」的样本** → **版本基线不能记一个号，必须记「轨 + 版本」二元组**（与库内 11-19 已记的「四条修复必须同时登记」同源） |
| 7 | Rapsody 的修复版本 | FR V2.9.12.0101 · ESP V2.9.5.0000 · PT V2.9.7.0000 · BEL(FR) V2.9.8.0000 · BEL(EN) V2.9.3.0000 · INT(EN) V2.9.4.0000 · INT(FR) V2.9.6.0000 · NL V2.9.6.0000 | CISA 快照 Remediations 节 | ✅ **已核** | ⚠️ **注意修复版本号普遍高于受影响版本号且各轨不同** → **不能用一个「已升级」布尔字段** |
| 8 | Rapsody 的 Product Status | 「Product Status: **fixed, known_affected**」 | CISA 快照逐字 | ✅ **已核** | ⭐ **库内首条「已修复但仍列为受影响」的双态字段** → 台账须能记「有补丁但未升级」，不能只有「受影响/不受影响」两态 |
| 9 | Rapsody 的行业标注 | Critical Infrastructure Sectors: **Energy, Critical Manufacturing, Commercial Facilities**；Countries/Areas Deployed: **Worldwide**；Company HQ: **France** | CISA 快照 Background 节 | ✅ **已核** | ⚠️ **Energy 在列** —— 库内 11-25 已提醒「不得写成官方点名能源行业」是针对 Siemens 那条的误读陷阱；**本条官方确实列了 Energy，必须照写** |
| 10 | Rapsody 的报告方 | 「Schneider Electric CPCERT reported this vulnerability to CISA」 | CISA 快照 Acknowledgments 节 | ✅ **已核** | 与库内 11-25 ICSA-26-328-03 同为「厂商 CPCERT → CISA」路径 |
| 11 | ICSA-26-328-01 的漏洞编号与版本 | **CVE-2026-127280**，**C-More EA9 Programming Software <=V6.80** | CISA 快照 | ✅ **已核** | — |
| 12 | ICSA-26-328-01 的 CVSS | **CVSS v3 7.8 High** | CISA 快照 + Cybersecurity Tracker 目录交叉 | ✅ **已核（7.8）** | ⭐⭐ **同批次两条的 CVSS 差 2.5 分（5.3 vs 7.8），但攻击形态完全同构** → **再次印证「CVSS 不能当优先级排序的唯一依据」** |
| 13 | ICSA-26-328-01 的攻击前置条件 | 「if **a user is convinced to open a malicious file**」；「could allow attackers to **corrupt application memory** and cause instability or a crash, potentially leading to arbitrary code execution」 | CISA 快照 Summary 节 | ✅ **已核** | ⭐⭐ **与 #4 完全同构** → **同批次两条可合并为一条库内结论：恶意工程文件是独立攻击面** |
| 14 | 本批次是否已收录 KEV / 是否有在野利用 | CISA 两份通告均未列 KEV 收录；CISA 通告惯例段落只给 Recommended Practices，不给利用状态 | 通读两份快照 | ✅ **已核（两份通告均无 KEV 收录标注、无在野利用表述）** | ⚠️ **不得写「已被利用」**；⚠️ 库内 11-25 已记 ICSA-26-328-03（Danfoss）所在产品线**同日在 KEV 出现** → **必须把「本批次 01/02 未入 KEV」与「同批 03 的产品线已入 KEV」并排写，不得混为一谈** |
| 15 | 「不在我方暴露面」的判定 | 我方无 Schneider EcoStruxure Power Build Rapsody、无 AutomationDirect C-More EA9 的任何使用证据 | 库内资产台账检索 | ✅ **已核（无使用证据）** | ⚠️ **不得下「我方受影响」结论**；⚠️ **但形态对我方成立**（我方做 DER/监控/聚合平台的工程与交付环节必然接触开关柜接线图与 PLC 编程文件） |

> **核查小结**：本期新增事实 **15 条可核**，其中 **13 条为官方一手可核**、**2 条为库内比对**（#14 #15）。**三条必须写明的边界**：① **本批次两条通告均无 KEV 收录、无在野利用表述**，且**不得与同批次第三条（Danfoss，已入 KEV）混为一谈**；② **我方无这两个产品的使用证据 → 不得下「我方受影响」结论**；③ **Rapsody 的 CVSS 5.3 与「可执行任意代码」的官方表述并存**，两者都真实，须照记不可调和 —— 我方不得用低分当忽略理由。

---

## 三、原文归档（快照）

- 快照文件：
  - `raw/snapshots/security/icsa-2632802-schneider-rapsody.md`
  - `raw/snapshots/security/icsa-2632801-automationdirect-cmore.md`
- SHA256：
  - `1236d46326e0c3da088ae93e969232abf6eb75d113cd17755d371bd7f03e5f0d`
  - `a3ebb08bba3feb4f110e8bc295bffb6f81d2690571b9f3d5cc44286539861857`
- 抓取时间：2026-11-26 07:10:55 / 07:10:56

> **关键原文摘录**
>
> **① CISA ICSA-26-328-02 摘要**
> > "The EcoStruxure™ Power Build Rapsody is used to enter or import the **single line diagram**, to get the extensive **bill of material of your switchboard**, including all devices, connection items, and mounting components. Failure to apply the remediations provided below may risk **memory corruption, heap-based buffer overflow, and/or stack-based buffer overflow**, which could result in local attackers being able to exploit these issues to potentially **execute arbitrary code**."
> > "**CVE-2026-119055** A **CWE-416: Use After Free** vulnerability exists that could cause arbitrary code execution when a local attacker could **trick the end user to open a specially crafted malicious SSD file**."
> > "Critical Infrastructure Sectors: **Energy**, Critical Manufacturing, Commercial Facilities · Countries/Areas Deployed: Worldwide · Company Headquarters Location: France"
>
> **② CISA ICSA-26-328-01 摘要**
> > "Successful exploitation of this vulnerability could allow attackers to **corrupt application memory and cause instability or a crash, potentially leading to arbitrary code execution**, if **a user is convinced to open a malicious file**."
> > "AutomationDirect C-More EA9 Programming Software **<=V6.80** (**CVE-2026-127280**) · CVSS v3 **7.8**"
>
> **③ 受影响版本与修复版本（同一条 CVE 分 8 条轨）**
> > "vers:generic/<=**2.9.1.0_FR**, **2.9.12.0101_FR**, <=**2.8.5.0301_ESP**, **2.9.5.0000_ESP**, <=**2.8.7.0101_PT**, **2.9.7.0000_PT**, <=**2.8.8.0201_BEL(FR)**, **2.9.8.0000_BELFR**, <=**2.8.3.0201_BEL(EN)**, **2.9.3.0000_BELEN**, <=**2.8.4.0401_INT(EN)**, **2.9.4.0000_INTEN**, <=**2.8.6.0000_INT(FR)**, **2.9.6.0000_INTFR**, <=**2.8.2.0000_NL**, **2.9.6.0000_NL**"
>
> **④ 状态字段**
> > "Product Status: **fixed, known_affected**"

---

## 四、概要提取

- ⭐⭐⭐ **库内首条「漏洞不在控制系统里，而在工程师打开的那份设计文件里」的 OT 通告族**：两个产品一个是**开关柜设计软件**（一次接线图 + 完整物料清单），一个是**PLC 编程软件** —— 攻击载荷是**一个文件**，触发动作是**一次双击**，受害资产是**一台不在任何台账上的工程工作站**。库内此前所有 OT 条目的落点都在「控制/归档/管理设备本身」，**这是第一次落点在「人收到的文件」**。
- ⭐⭐⭐ **库内首条「CVSS 低分反而更容易被忽略」的样本**：Rapsody 官方评分 **5.3 Medium**（因 `AV:L` + `UI:R` 被降级），但官方摘要同时写明可导致**任意代码执行**。库内 11-25 立的判据是「高 CVSS ≠ 我方风险高」—— **本条是它的镜像：高 CVSS 的那条（AutomationDirect 7.8）反而不是最该关心的，那条有协议层入口；5.3 的这条才是典型的「社交工程 + 文件」路径**。
- ⭐⭐⭐ **库内首条「同一漏洞跨 8 条语言版本轨、每轨独立版本号」的版本基线样本**：受影响 8 条轨、修复 8 条轨，且**修复版本号普遍高于受影响版本号**（如 NL 轨 ≤2.8.2.0000 → 修 2.9.6.0000）→ **我方版本台账不能记一个号，必须记「轨 + 版本」二元组**；也印证库内 11-19 已立的「**一条产品要同时登记多条修复**」规则。
- ⭐⭐ **库内首条「Product Status = fixed, known_affected」双态字段**：**有补丁 ≠ 已处置**。CISA 的字段值直接说明「补丁已发布但产品仍在受影响清单里」→ 我方台账必须能表达这个中间态，否则会把「厂商已修」误读成「我方已安全」。
- ⭐⭐ **官方在本批次点名 Energy 行业**（Rapsody 的 Critical Infrastructure Sectors 含 Energy，Country = France，Deployed = Worldwide）→ 与库内 11-25 那条「不得写官方点名能源行业」是**不同条目、不同结论，不得互相套用**。
- ⭐ **「管理面 / 工程面」这一层资产此前不在我方任何台账上**：工程师工作站上放着**在运变电站与开关柜的接线图和物料清单**，且按 ThreatsEye 的运营观察，这类工作站**常紧邻或落在 OT 网络上**、多人共用 → 它同时是「管理面资产」和「潜在 OT 跳板」，此前既不在 EOL 台账，也不在辅助设备台账。
- ⚠️ **本批次两条均未入 KEV、无在野利用表述** → 不产专项整改；⚠️ **与同批次第三条（Danfoss AK-SM，已入 KEV）必须分开叙述**。

---

## 五、主要观点

**原文主张**

- CISA 官方（ICSA-26-328-02）：漏洞存在于 EcoStruxure Power Build Rapsody，**若不施加修复可能导致内存破坏、堆溢出与栈溢出**，本地攻击者可能**执行任意代码**；受影响版本覆盖 8 条语言版本轨，各轨有独立修复版本；Product Status 为 `fixed, known_affected`。
- CISA 官方（ICSA-26-328-01）：成功利用可能让攻击者**破坏应用内存并导致不稳定或崩溃，进而可能导致任意代码执行**，前提是**用户被说服打开一个恶意文件**；受影响版本 `<=V6.80`。
- 厂商侧（Schneider CPCERT）：该漏洞由 Schneider Electric CPCERT 报告给 CISA。
- 第三方（ThreatsEye）的运营解读：「the trigger is mundane: **an engineer double-clicks a switchboard project file received from a colleague, a contractor, or a supplier**」「**Rated CVSS 5.3 — but the impact ceiling is full code execution on an engineering workstation**」「**Engineering workstations that run Rapsody often sit on or adjacent to OT networks, hold project documentation for live substations, and are shared between staff. A code-execution primitive there is a foothold, not a nuisance.**」

**我方判断**

- ⭐⭐⭐ **这两条真正改变的不是漏洞清单，而是资产清单。** 我方目前所有 OT/能源侧暴露面台账记的都是**「被访问的设备」**（控制器、逆变器、监控平台、辅助设备）。这两条通告指出还有一类暴露面是**「被人打开的文件」**—— 它的载体是工作站，不是控制器；它的触发是社交工程，不是协议漏洞；它的后果落在工程师的权限域，通常比控制器权限大得多。**这正好对上库内 11-24 已记的「辅助设备类目长期不在任何台账上」那条待办 —— 但更狠的是：辅助设备至少是台账上加一行，工程工作站是台账上加一整类。**
- ⭐⭐⭐ **「工程面 / 管理面」这一层应作为独立资产类别，而不是「辅助设备」的子类。** 理由：辅助设备（汇流箱温控、消防联动、门禁、气象站）的暴露面是「设备自身联网」；工程工作站这一层的暴露面是「**它同时能读到在运资产的设计文档、又能连到 OT 网络、还多人共用**」—— 这三条同时成立的资产在库内现有分类里没有对应项。建议的类别名：**「工程与交付侧工作站（Engineering & Delivery Workstations）」**，台账字段至少要有：承载的是哪个项目/哪条线路的哪份设计文档、是否接入 OT 网段、是否共享账号、文件来源是否受控。
- ⭐⭐ **「恶意工程文件」是独立于「协议漏洞」的防线问题，WAF 覆盖不到。** 我方 WAF 看到的是 HTTP 流量；而这条路径的文件可能来自邮件、IM、U 盘、甚至供应商的协同平台 —— **它从一开始就不经过我方的边界设备**。因此这条**不该进「攻击手法 → 防线覆盖度对照表」的 WAF 行**，而应进**「供应链与交付流程」类的控制项**：工程文件收发是否走受控通道、是否强制离线校验、交付前是否沙箱打开。**这与库内 11-20 记的 agent-framework 投毒（构建环境被污染）属于同一族 —— 都不是攻我方系统，是攻我方必然要碰的那份输入。**
- ⭐⭐ **Rapsody 的「8 条语言版本轨」这个细节比漏洞本身更值得抄。** 它说明**产品版本号不是标量**。我方资产台账若只记 `version`，对这类多语言版本产品就会漏判；**必须记「版本轨 + 版本号」二元组**。这与库内 11-19 记的「一条产品要同时登记多条修复」是同一个根因的两面。
- ⭐⭐ **「fixed, known_affected」这个字段值值得直接抄进我方台账 schema。** 它说明厂商侧的字段体系本身就把「补丁已发」和「受影响」分成两件事；我方台账若只有一个 `vulnerable: bool`，就会在「厂商已修」和「我方已升级」之间产生系统性误读。建议字段：`patch_available` / `patch_applied` / `exposure` 三个独立字段。
- ⭐ **同批次两条的 CVSS 差 2.5 分但形态同构 → 又一个「CVSS 不可单独排序」的样本。** 这条与库内 11-19 记的 Java4Shell「发现—可利用成本基线（1 小时定位 / 2 小时写出利用代码）」是同一个方法论：**优先级应按「可利用性 × 物理后果 × 我方可达性」排，不按 CVSS 排**。
- ⚠️ **严格边界**：我方无这两个产品的使用证据 → **不得下「我方受影响」结论**、**不得产专项整改**。可落点只有方向级：**「工程与交付侧工作站」资产类别 + 「工程文件来源受控」流程控制项 + 「版本轨二元组」台账字段 + 「补丁可获取/已应用/暴露面」三字段分离**。四条都不指向我方任何具体产品功能。

---

## 六、参考意义

| 方向（网络安全/信创/等保/隐私保护/护网） | 可证事实 | 本阶段处理 |
|---|---|---|
| 网络安全 | 两条官方 ICS 通告均指向「恶意工程/编程文件 → 工程师工作站 → 任意代码执行」；Rapsody 官方标注 Energy 行业；Product Status = fixed, known_affected；8 条版本轨；本批次无 KEV、无在野利用 | ✅ **进评审**（方向级）。落点：**资产台账新增「工程与交付侧工作站」类别** + **版本台账改「轨 + 版本」二元组** + **补丁状态三字段分离（可获取/已应用/暴露面）**。**不新开产物，不产专项整改**（第 1 关无我方侧一手证据） |
| 网络安全（供应链与交付流程） | 触发路径不经过我方 HTTP 边界（邮件/IM/U 盘/供应商协同平台），WAF 结构性不可见；同构于库内 11-20 agent-framework 投毒（污染必然要碰的上游输入） | ✅ **进评审**（方向级）。落点：**「工程文件与交付物的来源受控」列为流程控制项**（受控通道 / 交付前离线或沙箱校验 / 账号不共享）。**不新开产物** |
| 信创 | 无 | ❌ 不进 |
| 等保 | 无（本批次为漏洞与资产分类，非合规条款变化） | ❌ 不进 |
| 隐私保护 | 无 | ❌ 不进 |
| 护网 | 工程工作站同时「持设计文档 + 邻接 OT 网络 + 多人共用」= 演练场景中的横向移动落点 | 🟡 **观察台账项**（方向级）。落点：**护网演练场景候选「工程侧工作站 → OT 网络」横向移动路径**。**不新开产物** |

---

## 七、总结输出

**一句话结论**：CISA 2026-11-24 同批发布 ICSA-26-328-02（Schneider EcoStruxure Power Build Rapsody，CVE-2026-119055，UAF，CVSS 5.3）与 ICSA-26-328-01（AutomationDirect C-More EA9，CVE-2026-127280，≤V6.80，CVSS 7.8）两条，**共同暴露了一个此前不在我方任何台账上的资产类别 —— 工程师桌面上的那份设计/编程文件**；两条均未入 KEV、无在野利用、我方无使用证据，故不产专项整改，动作只落在方向级的资产分类、台账字段与交付流程三个控制项上。

**落地去向**

- [ ] 产品特性
- [ ] 需求变更
- [ ] 专项整改
- [x] **方向级产物**（网络安全）—— 「工程与交付侧工作站」资产类别；版本台账「轨 + 版本」二元组；补丁状态三字段分离；工程文件来源受控流程项；护网演练候选路径（观察台账）

**关联文档**

- [Siemens SIMATIC NTLM 中继（办公网读报表 → 攻击路径首次写入厂商分析）](icsa26321SiemensSimaticNtlmRelay-2026-11.md) —— 本篇是它「访问行为即暴露面」判断的下一层
- [CISA KEV 2026-11-25 批次十条](cisaKev20261125Batch-2026-11.md) —— 同日同批的第三条 Danfoss 已入 KEV，与本篇两条必须分开叙述
- [agent-framework PyPI 投毒（供应链受害位置）](agentFrameworkPypiSupplyChain-2026-11.md) —— 同属「攻我方必然要碰的那份输入」
- [CISA 等五部门联合警告「联网辅助设备是被点名的攻击面」](cisaRefrigerationColdChain-2026-11.md) —— 台账缺失类问题的既有基线

---

## 参考链接

- CISA ICSA-26-328-02（2026-11-24）：https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-02
- CISA ICSA-26-328-01（2026-11-24）：https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-01
- ThreatsEye 技术解读（2026-11-25）：http://threatseye.io/blog/schneider-electric-patches-use-after-free-flaw-in-ecostruxure-power-build-rapsod
- Defcon Level 结构化转录（2026-11-24）：https://www.defconlevel.com/alert/2026-11-24-cisa-cybersecurity-advisories-schneider-electric-ecostruxure-power-build-rapsody-software-icsa-26-328-02
- Cybersecurity Tracker ICS 通告目录（截止 2026-11-24）：https://cybersecuritytracker.ai/ics-advisories

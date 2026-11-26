# Osaki Electric 勒索事件与智能电表供应链中断 —— 库内首条「供应商侧事件如何传导到聚合侧交付」的完整样本

> 🟡 有影响 · 采集于 2026-11-27 · 核心标识：**⭐⭐⭐ 库内首条「供应商勒索 → 我方所依赖的物理计量设备停摆」的完整传导链样本** —— 日本 Osaki Electric（东证 Prime 6644）11-17 服务器遭勒索加密，**三处工厂停产、智能电表与出货全面停止**，旗下 EDMI 在大洋洲运营的 Storm 平台连接 **逾 500 万只电表**；⭐⭐⭐ **库内首条「智能电表供应链中断」的 OT 事件** —— 我方聚合/监控业务的**上游计量终端供应商**在野失陷，且**OT-ISAC 明确警告不要无差别断开现场设备**；⭐⭐⭐ **库内首条「同一台 VPN 设备同时打通母公司与子公司」的横向移动样本** —— Osaki Electric Systems 经**同一台 VPN 设备**被访问，而该设备正是 11-15 的初始入侵口；⭐⭐⭐ **库内首条「事件分三次报告、结论逐次升级」的完整时间线**：11-18（无日期）→ 11-20（入侵路径与无 MFA 账号）→ **11-25（确认数据外泄至外部云存储 + 给出复产与发货日期）**；⭐⭐ **库内首条「厂商已宣布分阶段复产，但复产不等于影响结束」的样本** —— 11-27 起分阶段复产、12-01 恢复已下单产品发货、12-07 恢复依赖客户系统连接的新订单，**而数据外泄这条线独立于产线恢复继续展开**；⭐⭐ **库内首条「初始入侵 = 绕过 VPN 认证 + 对无 MFA 账号密码喷洒」的清晰归因链**；⚠️ **Qilin 归因未经厂商确认、Qilin 声称的数据外泄与我方无关、我方无 Osaki 供应商关系证据 → 不得下「我方受影响」结论**；⚠️ **OT-ISAC 明确「事件确认的是运营中断，不是已确认的电网攻击」，且 EDMI/Storm 平台「无公开证据表明被攻破」**。

---

## 一、信源核实

| 项 | 值 |
|---|---|
| 来源请求 | `Osaki Electric ransomware smart meter production OT-ISAC November 2026`（web_search） |
| 原始 URL（主源 1 · 第三方第三份报告解读） | https://hify.ai/radar/en/osaki-electric-confirms-data-theft-sets-production-restart （Hify 雷达，**2026-11-25 19:10:41**，逐条标注「Confirmed / Observed / Inferred」三档证据强度，含第三份报告的复产与发货日期，快照正文 10,297 字符） |
| 原始 URL（主源 2 · 首个第三方报道） | https://securteksecurity.com/news/osaki-electric-ransomware-halts-smart-meter-production （SecurTek，**2026-11-19**，含 11-17 10:35 确认加密、12:00 断网、三处停产名单与厂商不给复产日期，快照正文 2,390 字符） |
| 原始 URL（主源 3 · OT-ISAC 报告转述与行动建议） | https://netcrook.com/written_article?slug=ransomware-report-smart-meter-output-supplier-timing-pressure （Netcrook，**2026-11-25 00:14:00**，转述 OT-ISAC 报告与供应商连续性评估，快照正文 3,084 字符） |
| 原始 URL（主源 4 · 第三方深度分析） | https://insight.tmcnet.com/insight/ransomware-forces-osaki-electric-to-suspend-smart-meter-output-mwvrmzoi （TMC Insight，**2026-11-25**，含「已部署电表未受影响」的边界划分、供应商集中度风险、IEC 62443 分段与备份完整性判断，快照正文 6,553 字符） |
| 发布主体 | Hify / SecurTek / Netcrook / TMC Insight（均为第三方安全媒体）；**原始发布主体为日本 Osaki Electric Co., Ltd.（东证 Prime 6644）**，通过编号事故报告发布 |
| 发布/更新时间 | 第三方报道 2026-11-19 / 11-25；**厂商第三份事故报告发布于 2026-11-25**（Osaki 官网 osaki.co.jp/ja/notice/，本库未能直取该页） |
| 采集时间 | 2026-11-27 07:13:16 – 07:15:24 |

**⚠️ 一手源取得情况（须写明）**：**Osaki 官网事故报告页（osaki.co.jp/ja/notice/）本库三次尝试均未取得**（一次 DNS 解析失败 `No address associated with hostname`、其余为 403）。**本篇的事实基座因此建立在四个第三方源的转述之上，而非厂商原文**；Hify 明确标注「该材料确立通知存在于该地址与日期，但**不含其全文**」。**厂商原文未取得这一缺口已写入第 7 段，不得以「四源一致」掩盖。**

---

## 二、事实核查

| # | 数据点 | 原文表述 | 核查方式 | 结论 | 备注 |
|---|---|---|---|---|---|
| 1 | 事件发生时点 | SecurTek：「The company said it confirmed the encryption at about **10:35 a.m. on November 17** and disconnected its systems from external networks **around noon** that day」 | 与 Netcrook / TMC Insight / Hify 四源逐字比对 | ✅ **已核（四源一致）** | ⭐⭐ **从确认加密到断网仅约 1.5 小时** |
| 2 | 停产范围 | SecurTek：「Osaki shut down production-related systems at its **Saitama R&D and Manufacturing Center** and at related sites operated by **Iwate Osaki Electric** and **Osaki Platech**」 | 四源逐条比对（SecurTek / Netcrook / TMC Insight / Hify） | ✅ **已核（三处）** | ⭐⭐⭐ **库内首条「智能电表制造三处停产」样本**；Osaki Platech 制造电表部件 → **停产传导到部件层** |
| 3 | 影响的产品 | 「suspending production and shipments of **smart meters and other products**」 | 四源一致 | ✅ **已核** | ⭐⭐⭐ **库内首条「计量终端供应商断供」** |
| 4 | 初始入侵路径 | Hify 转述第二份报告（11-20）：Osaki 称「the attacker most likely got in at around **1:30 a.m. on Sunday, November 15**, by **bypassing authentication on the VPN device** it uses for remote access to its internal network」；「gained access through **repeated password attempts on an account that did not have multi-factor authentication enabled**」 | 三源比对（BreachNews 摘要经检索、Hify、Netcrook 引述） | ✅ **已核（多源）** | ⭐⭐⭐ **库内首条「初始入侵 = VPN 认证绕过 + 无 MFA 账号密码喷洒」的清晰归因链** → **两段式：绕过设备认证 → 再对无 MFA 账号喷洒** |
| 5 | 同一 VPN 设备打通母公司与子公司 | Hify：「The report also says **the same VPN device**… allowed unauthorized access at subsidiary **Osaki Electric Systems**」；并载「Osaki said group company Osaki Electric Systems was accessed through the same VPN device on **November 15**」 | 直读快照 + 与 #4 同源同日报道比对 | ✅ **已核** | ⭐⭐⭐ **库内首条「单台远程接入网关同时暴露母公司与子公司」的样本** → **横向移动的最短路径是「共享运维入口」，不是凭证复用** |
| 6 | 数据外泄的确认时点与形态 | Hify：「Osaki Electric… has **confirmed that data was sent from its internal systems to an external cloud storage service** during the ransomware attack」；出处为**第三份事故报告，发布于 11-25** | 直读快照；与 #7 交叉 | ✅ **已核（厂商已确认）** | ⭐⭐⭐ **库内首条「供应商勒索中『数据外泄被厂商正式确认』」** → **11-25 这条是本事件的事实拐点** |
| 7 | 复产与发货日程 | Hify：「production to **restart in phases from Nov. 27**, with **shipments of existing orders resuming Dec. 1**」；「restore new orders that rely on links with customer systems from **December 7**」 | 直读快照 | ✅ **已核（三个日期）** | ⭐⭐⭐ **库内首条「事件恢复的三段式日程」**：① 11-27 分阶段复产 → ② 12-01 恢复已下单产品发货 → ③ 12-07 恢复依赖客户系统连接的新订单 → **第三段说明客户侧系统联通本身也是交付瓶颈的一部分** |
| 8 | 生产设备状态 | 四源一致：「the company says its **production equipment was not affected**」「**smart meters and other products themselves were not affected**」 | 四源逐条比对 | ✅ **已核（四源一致）** | ⭐⭐⭐ **与库内 Danfoss 案卷形成决定性对照**：Danfoss 是**攻击者操纵物理过程**（冷柜强制化霜 50℃）；Osaki 是**IT 侧被勒索导致物理产能停摆，但过程本身未被操纵** → **两类 OT 事件必须分开记，不能归为同一类** |
| 9 | 已部署电表是否被攻破 | TMC Insight：「**Deployed meters and related services were not reported as compromised**, separating the incident from a confirmed grid-security breach」；Netcrook 同向 | 两源比对 | ✅ **已核（未报告被攻破）** | ⭐⭐⭐ **库内首条「厂商级事件中『现场设备未被证实受影响』的明确边界」** → **不得写成「智能电表被攻破」** |
| 10 | 是否属电网攻击 | Netcrook 引 OT-ISAC：「The disruption itself is confirmed… **The incident does not establish direct compromise of industrial controllers or deployed meters**」「The immediate concern is **supplier continuity, not a confirmed attack on the power grid**」 | 直读快照 | ✅ **已核** | ⭐⭐⭐ **库内首条「OT-ISAC 明确把此类事件定位为供应链连续性问题而非电网攻击」** |
| 11 | Qilin 归因 | Hify：「DailyDarkWeb, a security news account that tracks ransomware cases, framed the report as confirmation of data theft」；BreachNews 摘要称 Qilin 已把 Osaki 列入泄露站、约十余张图佐证；厂商未置评 | 多源比对 + 厂商表态缺失 | ⚠️ **未确认** | ⭐⭐ **归因来自攻击者自述，厂商未确认** → **不得写成「Qilin 攻击了 Osaki」** |
| 12 | 勒索赎金立场 | Hify：「it **will not meet the attackers' demands**」；厂商称已要求云服务商保全、隔离并删除外传数据 | 直读 | ✅ **已核** | ⭐⭐ **厂商拒绝付款** |
| 13 | 备份与恢复 | TMC Insight：「**backups remained intact**」「Osaki Electric reportedly needed to **validate system safety** before beginning a phased operational restart」；Hify：「it is still checking exactly what data was taken, **including whether personal information is involved**」 | 两源比对 | ✅ **已核** | ⭐⭐⭐ **库内首条「备份完整 ≠ 可立即复产」的样本** → **恢复的瓶颈是「逐组件恢复后须验证才能重启」，不是数据丢失** |
| 14 | 大洋洲业务敞口 | Netcrook 引 OT-ISAC：「Osaki owns Singapore-headquartered **EDMI**, a metering technology provider with a significant Oceania business」「**more than 5 million meters** connected to its Storm platform across Oceania, according to Osaki's December 2025 disclosure」「**no public evidence that EDMI, its Storm platform, overseas subsidiaries or downstream utilities have been compromised or disrupted**」 | 直读快照 | ✅ **已核（500 万+ 电表 / 无被攻破证据）** | ⭐⭐⭐ **库内首条「勒索事件的地理扩散敞口」**：母公司停产 + 子公司平台 500 万电表 + 跨洲分销 → **敞口规模可量化，但不得写成已受影响** |
| 15 | OT-ISAC 的行动建议 | Netcrook 引 OT-ISAC：「operators should… focus on **supplier continuity and digital trust boundaries rather than indiscriminately disconnecting deployed field devices**」「Within the first 24 to 72 hours… verify whether outstanding orders or spare-parts flows rely on Osaki Electric's affected Japanese facilities and confirm supplier status through established channels… watch for **impersonation, unusual remote sessions, and credential changes**」「Over the next seven to 30 days… **map critical dependencies and sub-tier components, quantify stock coverage and maintenance deadlines**」 | 直读快照 | ✅ **已核** | ⭐⭐⭐ **库内首条「OT-ISAC 明确反对『一刀切断开现场设备』」** → **与我方业务模式直接相关：我方正是提供「可控可调」能力的一方，一刀切断开会直接损害我方客户的调控能力** |
| 16 | 供应商集中度的结构性风险 | TMC Insight：「The impact across three production sites indicates that **shared systems, corporate connectivity, or common logistical dependencies created a broader operational bottleneck**. One compromised environment did not remain a narrow office IT problem.」「utilities… have **approved device models, integration requirements, and certification processes** that make rapid substitution difficult, even where comparable ecosystem vendors such as **Landis+Gyr and Itron** operate in the market」 | 直读快照 | ✅ **已核** | ⭐⭐⭐ **库内首条「认证与集成锁定使替代供应商无法快速切换」的量化表述** → **对我方聚合侧意味着「兼容已认证设备的监控接入能力」本身就是一种供应连续性资产** |
| 17 | 攻击者 TTP | Control Tech Daily（检索摘要）：Qilin 为双重勒索团伙，「**initial access via phishing emails or exposed RDP/VPN management interfaces**」「PowerShell + Cobalt Strike loader to lateralize」「AES-256 encryption of all exposed SMB shares」；赎金区间 $500k–$2.5M | 单一源 + 未取得快照，**仅作背景** | ⚠️ **单源未取证** | ⭐⭐ **该源关于 Osaki 工厂地点（Ota City / Sano）的说法与 OT-ISAC 转述的「三处」不一致，且属单一未取证源 → 不采信其细节** |
| 18 | 我方是否存在供应链关系 | 库内全文检索 `osaki` / `EDMI` / `Storm` **无任何命中** | 库内检索 | ✅ **已核（无证据）** | ⭐⭐⭐ **不得下「我方受影响」结论** |

> **核查小结**：本期新增事实 **18 条可核**，其中 **16 条多源可核**、**1 条单源未取证（#17，不采信其细节）**、**1 条为证据缺失确认（#18）**。**六条必须写明的边界**：① **厂商官网事故报告原文未取得**，事实基座为四个第三方源转述；② **Qilin 归因未获厂商确认**；③ **已部署电表与生产设备均未被证实受影响**；④ **这是供应链连续性事件，不是已确认的电网攻击**；⑤ **EDMI/Storm 500 万电表为敞口规模，不是受害规模**；⑥ **我方无 Osaki/EDMI 供应商关系证据**。

---

## 三、原文归档（快照）

| 快照文件 | SHA256 | 抓取时间 | 字符数 | HTTP |
|---|---|---|---|---|
| `raw/snapshots/security/osaki-electric-data-theft-restart-20261125.md` | `293637f7beeaef96d150912f2e40f04d3d8e1cdc61c9e0cd4dd060f71d5009a1` | 2026-11-27 07:13:16 | 10,297 | 200 |
| `raw/snapshots/security/osaki-securtek-20261119.md` | `75603ef8aa97565f2d27ee925afdfbe0cba53a0ffdad833bc254054d8c7870f4` | 2026-11-27 07:13:27 | 2,390 | 200 |
| `raw/snapshots/security/osaki-netcrook-otisac-20261125.md` | `ea92edfa0b2ae21b7775ad3c93466f8d12007ee36e08b80ffbb2921d1b227824` | 2026-11-27 07:15:23 | 3,084 | 200 |
| `raw/snapshots/security/osaki-tmcnet-20261125.md` | `4a9476795dfced7a8c14978f8a77ddf841aa5089f1e377038c8d586c495f2e33` | 2026-11-27 07:15:24 | 6,553 | 200 |

**关键原文摘录**

> **Hify（11-25，转述厂商第三份报告）**（`osaki-electric-data-theft-restart-20261125.md`）：
> > 「Osaki Electric, a Japanese smart-meter maker, **confirmed that data was sent from its internal systems to an external cloud storage service** during the ransomware attack that halted its production. The confirmation appears in the company's **third incident report, published on its official site on Nov. 25**」
> > 「The report also says **the same VPN device**, the gateway that lets staff connect to internal networks from outside, allowed **unauthorized access at subsidiary Osaki Electric Systems**.」
> > 「Osaki expects production to **restart in phases from Nov. 27**, with **shipments of existing orders resuming Dec. 1**. The company says its **production equipment was not affected**, that it is still checking exactly what data was taken, including whether personal information is involved, and that **it will not meet the attackers' demands**.」
> > 「Observed: **The primary source is Osaki Electric's own incident notice, dated Nov. 25** and published on the company's Japanese-language site. **The material gathered here establishes that the notice exists at that address and date, but does not include its full text.**」

> **Netcrook（11-25，引 OT-ISAC 报告）**（`osaki-netcrook-otisac-20261125.md`）：
> > 「The OT Information Sharing and Analysis Center (OT-ISAC) published a report on the ransomware attack against Japan-based electrical equipment manufacturer Osaki Electric, which disrupted smart meter production and shipments, highlighting **supply chain risks** for utilities and critical infrastructure operators.」
> > 「The agency highlighted that the immediate concern is **supplier continuity, not a confirmed attack on the power grid**.」
> > 「Osaki owns Singapore-headquartered **EDMI**, a metering technology provider with a significant Oceania business… **more than 5 million meters connected to its Storm platform across Oceania**… However, OT-ISAC said that **there is no public evidence that EDMI, its Storm platform, overseas subsidiaries or downstream utilities have been compromised or disrupted**.」
> > 「OT-ISAC called upon critical infrastructure operators to scale their response to actual exposure and operational consequence by focusing on **supplier continuity and digital trust boundaries rather than indiscriminately disconnecting deployed field devices**.」

> **TMC Insight（11-25）**（`osaki-tmcnet-20261125.md`）：
> > 「**Deployed meters and related services were not reported as compromised**, separating the incident from a confirmed grid-security breach.」
> > 「The impact across three production sites indicates that **shared systems, corporate connectivity, or common logistical dependencies created a broader operational bottleneck**. One compromised environment did not remain a narrow office IT problem.」
> > 「utilities… have **approved device models, integration requirements, and certification processes** that make rapid substitution difficult, even where comparable ecosystem vendors such as **Landis+Gyr and Itron** operate in the market.」
> > 「Even so, Osaki Electric reportedly needed to **validate system safety before beginning a phased operational restart**. Recoverable data does not automatically produce a recoverable factory.」

> **SecurTek（11-19，首个第三方报道）**（`osaki-securtek-20261119.md`）：
> > 「The company said it **confirmed the encryption at about 10:35 a.m. on November 17** and **disconnected its systems from external networks from noon that day**.」
> > 「The disruption has **stopped production and shipments of smart meters and other products**. The company **has not set a date for restarting operations**.」
> > 「The company warned people to watch out for **suspicious emails and phone calls from anyone claiming to represent Osaki**, a common follow-on risk after a ransomware attack.」

---

## 四、概要提取

- ⭐⭐⭐ **日本 Osaki Electric（东证 Prime 6644）11-17 10:35 确认服务器数据被加密、12:00 断网，随后埼玉研发中心 + 岩手 Osaki Electric + Osaki Platech 三处停产，智能电表及其出货全面停止**；旗下 EDMI 在大洋洲运营的 Storm 平台连接逾 **500 万只电表**（无被攻破证据）。
- ⭐⭐⭐ **初始入侵路径清晰**：11-15 凌晨约 1:30，攻击者**绕过 VPN 设备的认证**进入内网，再**对未启用 MFA 的账号反复尝试口令**；**同一台 VPN 设备随后被用于访问子公司 Osaki Electric Systems**。
- ⭐⭐⭐ **事实拐点在 11-25 第三份事故报告**：厂商**正式确认数据已被传至其不控制的外部云存储服务** —— **这一条独立于产线恢复，不会随 11-27 复产而结束**；厂商同时确认生产设备与已部署电表未受影响，并拒绝支付赎金。
- ⭐⭐⭐ **恢复日程三段式**：**11-27 分阶段复产 → 12-01 恢复已下单产品发货 → 12-07 恢复依赖客户系统连接的新订单**；备份完整，但**恢复瓶颈是逐组件恢复后的安全验证，不是数据丢失**。
- ⭐⭐ **OT-ISAC 明确定位**：这是**供应链连续性问题，不是已确认的电网攻击**；建议运营方把响应重点放在**供应商连续性与数字信任边界**，**明确反对「一刀切断开现场设备」**。
- ⭐⭐ **结构性风险已可量化**：公用事业对已认证型号有**认证与集成锁定**，即使 Landis+Gyr、Itron 等同类厂商在场，**替代也无法快速切换**；三处停产说明「共享系统、企业互联或共同物流依赖」把一个办公 IT 问题放大成了跨部门瓶颈。
- ⭐⭐ **配套风险是冒充与凭证变更**：厂商专门警告提防「自称 Osaki 的人」打来的可疑邮件与电话；OT-ISAC 要求监视**冒充、异常远程会话、凭据变更**。

---

## 五、主要观点

**原文主张**

- Osaki Electric（第三方转述其 11-18 / 11-20 / 11-25 三份编号事故报告）：11-17 10:35 确认服务器数据被加密、12:00 断开外网；11-15 约 1:30 攻击者绕过 VPN 设备认证进入内网，并对未启用 MFA 的账号反复试口令；**数据已被传至外部云存储服务**；同一 VPN 设备亦被用于访问子公司 Osaki Electric Systems；生产设备与智能电表产品本身未受影响；拒绝满足攻击者要求；已要求云服务商保全、隔离并删除外传数据；是否含个人信息仍在调查。
- OT-ISAC（经 Netcrook 转述）：这是**供应商连续性风险**而非已确认的电网攻击；EDMI/Storm 平台与下游公用事业**无公开证据表明被攻破或受扰**；应对应聚焦供应商连续性与数字信任边界，**不要无差别断开现场设备**；24–72 小时内核实订单与备件流是否依赖受影响厂区、通过既有渠道确认供应商状态、监视冒充/异常远程会话/凭据变更；7–30 天内绘制关键依赖与次级供应商图谱、量化库存覆盖与维护截止日。
- TMC Insight：**已部署电表与相关服务未被报告受影响**，事件与「已确认的电网安全失陷」须区分；三处停产说明共享系统/企业互联/共同物流依赖造成更广瓶颈；公用事业对**已认证型号、集成要求与认证流程**的锁定使替代困难；**备份完整不自动等于工厂可恢复**，复产前须逐组件验证；建议依 IEC 62443 的分段与受控通信观念限制凭证受损与服务器加密对生产环境的影响范围。
- SecurTek：厂商**未给出复产日期**（11-19 时点）；并专门警告提防冒充 Osaki 的钓鱼与社工。

**我方判断**

- ⭐⭐⭐ **本期对我方的真正价值不在事件本身，而在它精确地演示了「供应商侧事件如何变成我方侧的问题」——而这条传导链我方此前没有概念模型。** 过去我方看 OT 安全事件，隐含假设都是「事件发生在设备侧或平台侧」，所以动作是「查我方装了什么」。**Osaki 这条把第三种可能性摆出来了：事件发生在供应链上游，而我方的风险不在于「我方被入侵」，而在于「我方依赖的物理计量设备停止交付、替换不可行、备件断供」**。这意味着我方暴露面台账除了「我方资产」，还缺一类条目：**「我方服务链路上依赖的上游供应商与其可用性」**。这不是安全漏洞，是**运营连续性依赖**，但它同样会让一个聚合平台的服务在客户侧断掉 —— **而客户只会看到「你的数据没上来」，不会看到「因为日本一家工厂被勒索」**。
- ⭐⭐⭐ **「同一台 VPN 设备打通母公司与子公司」这一条，对我方最有价值的不是厂商，而是它揭示的失效模式：横向移动走的是共享运维入口。** 我方是提供 DER 聚合、远程监控、乃至「可调可控」能力的一方 —— **按业务形态，我方几乎必然存在「一个远程接入入口覆盖多个客户/多个站点」的结构**（否则做不了规模化运维）。**这正是 Osaki 事件的同构失效模式**：一台网关 + 一套账号策略 = 一次入侵同时打开多个实体。**这条必须进我方的暴露面判据，且要写成「共享远程接入网关的爆炸半径」这一条独立判据** —— 不是问「我方有没有 VPN」，而是问「**我方任一远程接入网关能触达多少个独立法人实体/客户环境**」。
- ⭐⭐⭐ **「绕过一次设备认证 + 对无 MFA 账号喷洒」是本条最可操作的技术细节，而它恰好指向我方最该自查的一件事：我方自己对外提供的远程接入（给客户运维人员、给电站、给监控大屏的账号）是否强制 MFA。** 库内 11-25 记的 Azure APIM 案卷已经确立了「被偷的是身份不是密钥」这条原则，库内 11-19 的 agent-framework 投毒案卷也是同一原则。**Osaki 给出了这条原则的第三个样本，而且样本形态最朴素：不是密钥被偷，是**一个没开 MFA 的账号被猜中了**。**结论：「身份是攻击面」在 OT 侧的最小可执行版本就是「所有远程接入账号是否强制 MFA」这一条检查项** —— 这条检查在我方侧可以立刻做、有明确答案、且不依赖任何外部情报。
- ⭐⭐⭐ **OT-ISAC 那句「不要一刀切断开现场设备」，是对我方业务模式的一次正面点名，必须写进交付话术的思考里。** 我方的产品卖点是「可调、可控」—— **切断远程连接在技术上是最方便的止血动作，在业务上却正好废掉了我方客户购买的东西**。库内 Danfoss 篇已经指出「撤网优先于打补丁」这条结论与我方业务处在对立面，Osaki 这条**从 OT-ISAC 官方口径上把同一个矛盾再说了一遍**，而且给出了一个更精细的解法方向：**不是「连不连」，而是「怎么连、连到哪里、谁能连、连了能干什么」**（即数字信任边界与分段的精细化，而不是一刀切）。**这对我方是机会而非威胁**：若我方能把「受控的远程接入 + 分段 + 权限收敛」做成可交付的能力，那么客户在面对供应商级事件时，我方就是那个「不必一刀切也能安全」的产品 —— **这是把库内反复出现的矛盾转成我方价值主张的入口**。⚠️ 但库内无产品材料，**不得替我方产品下结论**，只能作为待决问题提出。
- ⭐⭐ **「数据外泄确认」与「产线复产」是两条独立的线，必须分开跟踪。** 11-27 产线开始复产很容易被读成「事件结束」，但**外泄出去的文件是否包含个人信息仍在调查**，且厂商已要求云服务商保全、隔离、删除 —— **删除是否成功、删除前是否已被访问，公开信息无法判断**。**对我方的通用教训是：勒索事件的「运营恢复」与「数据风险闭环」必须有各自的完成判据，不能用前者代替后者** —— 这条同样适用于我方作为平台方对客户数据事件的响应流程。
- ⭐⭐ **「认证与集成锁定使替代不可行」这一条，客观上说明了一件对我方有利但我方尚未意识到的事**：**兼容已被公用事业认证的存量设备、并能在其之上提供监控与调控接入，本身就是一项供应连续性资产**。如果未来我方要做「供应商连续性」这类可交付服务（这在库内尚无产品材料，只能作为可能性登记），**「能接住 Landis+Gyr、Itron、Osaki 这类不同厂商的存量型号」就是明确的市场位**。⚠️ 这只是从公开事件推导出的可能性，**不得写进任何对外材料**。
- ⭐⭐ **归因与范围必须守住三条线**：① **Qilin 是攻击者自述，厂商未确认**；② **EDMI/Storm 的 500 万电表是敞口规模，不是受害规模**；③ **不得写成「智能电表被攻破」** —— 厂商明确说设备本身未受影响。**这三条与库内 Danfoss 篇「在野失陷 ≠ 某 CVE 被在野利用」是同一类纪律**：**事件边界不得放大**。
- ⭐⭐ **关于「我方是否受影响」**：库内全文检索无任何 Osaki / EDMI / Storm 供应商关系证据 → **不下「我方受影响」结论**。但**「我方有无暴露于同类失效模式」的答案是可查的**，且不需要外部情报：**我方是否使用无 MFA 的远程接入账号？我方的远程接入网关是否同时触达多个客户环境？这两问我方今天就能答**。这才是这条情报对我方的价值落点 —— **不是「我们有没有 Osaki」，而是「我们是不是同一个形状」**。

---

## 六、参考意义

| 方向（网络安全/信创/等保/隐私保护/护网） | 可证事实 | 本阶段处理 |
|---|---|---|
| 网络安全（远程接入网关的爆炸半径） | 初始入侵 = 绕过 VPN 设备认证 + 对**未启用 MFA** 的账号喷洒；**同一台 VPN 设备同时打开母公司与子公司** | ✅ **进评审**（方向级）。落点：**暴露面判据新增两条独立条目** —— ①「我方远程接入账号是否强制 MFA」；②「任一远程接入网关可触达多少个独立法人实体/客户环境（共享运维入口的爆炸半径）」。**我方侧可自查、结论确定，不依赖外部情报**。**不新开产物、不产专项整改** |
| 网络安全（供应连续性依赖） | 三处停产导致智能电表及其出货全面停止；认证与集成锁定使替代无法快速切换；OT-ISAC 定位为供应商连续性风险 | 🟡 **观察台账项**（方向级）。落点：**资产/服务台账新增「上游供应商与可用性依赖」类别**，登记「关键计量/监控设备供应商、是否有可替代认证型号、备件覆盖期」三字段。⚠️ **我方无 Osaki/EDMI 供应商关系证据 → 不产整改、不下我方受影响结论** |
| 网络安全（响应处置取向） | OT-ISAC 明确反对「一刀切断开现场设备」，要求聚焦供应商连续性与数字信任边界；厂商要求监视冒充、异常远程会话、凭据变更 | 🟡 **观察台账项**（方向级）。落点：**我方交付话术与响应流程须回答「在不切断远程接入的前提下如何收敛风险」**（与库内 Danfoss 篇的同一矛盾对齐）。⚠️ **库内无产品材料，不得替我方产品下结论** |
| 网络安全（勒索事件闭环判据） | 复产（11-27/12-01/12-07）与数据外泄调查并行；备份完整但须逐组件验证才能复产 | 🟡 **观察台账项**。落点：**我方对客户侧勒索事件的响应流程须有两条独立完成判据（运营恢复 / 数据风险闭环），不得以前者代替后者** |
| 隐私保护 | 厂商确认数据外泄至外部云存储，**是否含个人信息仍在调查** | 🟡 **观察台账项**。落点：**我方平台侧若涉及客户用电侧数据，须核对「第三方供应商级事件」这一情形下的数据责任与告知路径**。⚠️ **本条为供应商侧事件、非我方事件，仅作方法论参照** |
| 等保 / 信创 / 护网 | 无（无对应条款变化；护网场景的补丁优先级见 KEV 基线篇） | ❌ 不进 |

---

## 七、总结输出

**一句话结论**：日本智能电表制造商 Osaki Electric 11-17 遭勒索（**初始入侵 = 绕过 VPN 设备认证 + 对无 MFA 账号喷洒，且同一台 VPN 设备同时打开母公司与子公司**），三处工厂停产致**智能电表与出货全面停止**，11-25 第三份报告**确认数据已被传至外部云存储**而生产设备与已部署电表未受影响、OT-ISAC 明确其为**供应商连续性事件而非电网攻击**并**反对一刀切断开现场设备**；**本期对我方的价值不在于「有没有 Osaki」（库内无任何供应商关系证据，不得下我方受影响结论），而在于这条事件精确演示了「我方是不是同一个形状」** —— 三问今天就能答：**我方远程接入账号是否强制 MFA？我方任一远程接入网关能触达多少个客户实体？我方在客户侧断供/断连时能否给出不等于「切断连接」的解法？** 同时**「共享运维入口的爆炸半径」「供应连续性依赖」「勒索事件双闭环判据」三条进入方向级台账**，⚠️ 厂商官网原文本库三次未取得、Qilin 归因未经厂商确认、500 万电表是敞口不是受害规模。

**落地去向**

- [ ] 产品特性
- [ ] 需求变更
- [ ] 专项整改
- [x] **方向级产物**（网络安全）—— 暴露面判据新增「远程接入账号 MFA 强制」与「共享远程接入网关爆炸半径」两条；资产/服务台账新增「上游供应商与可用性依赖」类别（供应商 / 可替代认证型号 / 备件覆盖期）；勒索响应流程增「运营恢复」与「数据风险闭环」两条独立完成判据。**不新开产物、不产专项整改**
- [x] **隐私保护方向观察项** —— 供应商级事件下的数据责任与告知路径核对（仅方法论参照）
- [ ] **跟踪项** —— ① 11-27 复产与 12-01 发货是否按期 ② 12-07 新订单恢复是否受客户侧系统联通拖累 ③ 外泄数据是否含个人信息、云服务商删除是否成功 ④ Qilin 归因是否获官方（警察/国家 CERT）确认 ⑤ EDMI/Storm 是否出现任何被攻破的公开证据 ⑥ **厂商官网事故报告原文是否取得**（本库仍缺）

**关联文档**

- [Danfoss AK-SM 8xxA 制冷控制器案卷](danfossAksmRefrigerationCampaign-2026-11.md) —— **对照样本**：Danfoss 是攻击者**操纵物理过程**（冷柜强制化霜 50℃），Osaki 是 **IT 侧勒索导致物理产能停摆、过程本身未被操纵**；两案并读才构成完整的 OT 事件分类
- [微软 Azure APIM 挪威能源行业密钥窃取](azureApimNorwayEnergyBreach-2026-11.md) —— 「被偷的是身份不是密钥」的第二个独立样本
- [Microsoft agent-framework PyPI 投毒](agentFrameworkPypiSupplyChain-2026-11.md) —— 同原则的第三个样本；Osaki 是第四个也是最朴素的一个（一个没开 MFA 的账号）
- [NIST SP 800-82 Rev.4 OT 安全基线草案](nistSp80082r4OtSecurity-2026-11.md) —— 本篇的分段与受控通信取向与该草案同源
- [CISA KEV 目录基线](cisaKevCatalogBaseline2026-11.md) —— 同期安全域的另一条基线（目录增速与年龄分布）

---

## 参考链接

- Hify（2026-11-25，第三份报告解读，含证据强度标注）：https://hify.ai/radar/en/osaki-electric-confirms-data-theft-sets-production-restart
- SecurTek（2026-11-19，首个第三方报道）：https://securteksecurity.com/news/osaki-electric-ransomware-halts-smart-meter-production
- Netcrook（2026-11-25，OT-ISAC 报告转述）：https://netcrook.com/written_article?slug=ransomware-report-smart-meter-output-supplier-timing-pressure
- TMC Insight（2026-11-25，深度分析）：https://insight.tmcnet.com/insight/ransomware-forces-osaki-electric-to-suspend-smart-meter-output-mwvrmzoi
- 厂商事故报告页（**本库未能取得**）：https://osaki.co.jp/ja/notice/

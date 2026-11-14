# 欧洲光伏 DER 暴露面 — 德国 BSI 指南 + 8.5 千个公网暴露系统 + 47 万套逆变器云平台免密登录

> 🟡 有影响 · BSI-CS 154（2026-10-13）· Modat×NCSC-NL 扫描（2026-10 初）· Jakkaru 披露（2026-08 底）· 核心标识：**欧洲 35 国 8547 个公网暴露风光系统**（光伏 7942）· **约 47 万套逆变器云平台免密管理员账号** · **德国要求取消电站控制系统直连互联网** · ⚠️ **7.8 GW vs 17 GW 容量口径冲突**

---

## 一、信源核实

| 项 | 值 |
|---|---|
| 来源请求 | `光伏 电站 监控平台 网络安全 攻击 事件 2026年11月 逆变器 暴露`（web_search）<br>`mySCADA myPRO CVE-2026-73807 photovoltaic inverter monitoring platform exposed`（web_search）<br>`Germany solar inverters cyberattack hundreds of thousands 8 GW remote access near miss`（web_search）<br>`BSI 德国 联邦信息安全局 光伏电站 控制系统 互联网接入 指南 取消`（web_search） |
| 原始 URL（主 1 · 官方指南） | https://news.metal.com/en/newscontent/104166764-smm-pv-flash-germany-recommends-stronger-cybersecurity-for-solar-pv-plant-control-systems （SMM PV Flash：德国 BSI 建议加强光伏电站控制系统网络安全防护） |
| 原始 URL（主 2 · 监管原文转述） | https://www.huizhidata.com/article/376 （慧知数据《2026年10月18日虚拟电厂行业早报》：德国让光伏退出公网，荷兰数出 8547 个暴露口 —— **逐条标注了每组数据的口径与来源**） |
| 原始 URL（辅 1 · 厂商侧） | https://bessxchange.com/article?slug=a-password-free-login-reached-470000-sungrow-systems-india-should-keep-track-404 （BESS Xchange：免密登录触及 47 万套逆变器系统，2026-10-16） |
| 原始 URL（辅 2 · 事件报道） | https://germanytimes.com/ntkmmr-energy-grid-operators-patch-vulnerabilities-after-near-miss-cyberattack-on-solar-inverters （Germany Times：德国近失事件报道，2026-11-12） |
| 原始 URL（辅 3 · 同源政策解读） | http://www.zjmade.cn/ecloud/plat/site/detail.html?newsId=4A7235B0A58B4794A7CE2F0179F38463 （浙江省外贸预警：德国建议取消对光伏电站控制系统的直接互联网接入） |
| 发布主体 | 德国联邦信息安全局 BSI（指南发布方）· Modat + 荷兰国家网络安全中心 NCSC-NL（扫描方）· Jakkaru GmbH（披露方）· SMM / 慧知数据 / BESS Xchange / Germany Times（报道方） |
| 发布/更新时间 | BSI-CS 154 **2026-10-13** · Modat 扫描 **2026-10 初** · Jakkaru 披露 **2026-08 底**，Sungrow 修复 **08-25**（距报告 3 天） · Germany Times 报道 **2026-11-12** |
| 采集时间 | 2026-11-15 07:11:51–07:12:15 |
| 快照 | `raw/snapshots/security/bsi-germany-pv-guidance-smm.md` · `sungrow-bsi-der-exposure-cn-roundup.md` · `sungrow-isolarcloud-470k-jakkaru-disclosure.md` · `germany-solar-inverter-near-miss-8gw.md` |

> 📎 **入库理由**：库内已有 [epicsDerExposure-2026-11](epicsDerExposure-2026-11.md) 记录了学术侧的 DER 暴露面研究（Conceptio 论文）与我方 WAF 内部实证，但**缺少"监管侧动作"与"规模化数字"**。本文补三块：① **德国国家级监管机构的明确要求**（BSI-CS 154：取消直连）—— 这是从"研究说危险"升级到"监管要求做"；② **暴露规模的量化基线**（8547 / 7942）；③ **一个具体的、已修复的免密登录案例**（47 万套）。
> ⚠️ **去重说明**：本文与 epicsDerExposure 文档**不是同一事件** —— 后者的 `source_url` 是 Conceptio 论文 + CN-SEC + 内部 WAF 报告；本文的 `source_url` 是 BSI/SMM/Modat 转载/Jakkaru 披露/Germany Times，**无一重叠**。故新建文档而非更新。

---

## 二、事实核查

| 数据点 | 原文表述 | 核查方式 | 结论 | 备注 |
|---|---|---|---|---|
| **BSI 指南编号与日期** | "10月13日，德国联邦信息安全办公室发布 **BSI-CS 154** 技术警示"；另一源："published on October 13, 2026 under the reference **BSI-CS 154**" | SMM 快照 + supplystatus 摘要 + 慧知数据三源一致 | ✅ 一致 | ⚠️ **有 1 天差异的表述**：慧知数据早期稿写 10-13，happeningnow 写 "16 October 2026"。**以 10-13 为主并注明口径差异** |
| **BSI 核心建议** | "取消电站控制系统的直接互联网接入"；对象含"工业控制器、通信设备、监控网关、逆变器、**SCADA** 以及**远程监控平台**"；远程访问改用 **VPN + 多因素认证**；维护**联网资产与通信接口清单**，清单须含"安装商或服务商设置的远程维护链路（含独立移动数据连接）"；办公网与生产网分离 | SMM 快照 + 慧知数据逐条转述（后者明确标"境外监管机构文件与公开报道口径"）两源一致 | ✅ 一致 | ⭐ **"含独立移动数据连接"这一条极具体** —— 4G/5G 随身路由是运维的现实做法，也是暴露面 |
| BSI 合规成本影响 | SMM："加强光伏电站数字化与远程监控应用不断发展，加强网络安全防护**或将增加电站运营商、逆变器制造商及监控系统供应商的合规与运营成本**" | SMM 快照逐字 | ✅ 已核 | ⚠️ **SMM 是我方数据供应方，其"成本上升"判断带有立场** —— 引用时标 SMM 口径 |
| **暴露规模** | "在**欧洲 35 个国家**识别出 **8547** 个与风电场和光伏电站关联的公网暴露系统……其中 **7942** 个与 **34 个国家**的光伏站点相关，另外 **605** 个与 **23 个国家**的风电场相关" | 慧知数据转述 Modat×NCSC-NL + 索比光伏网同源报道交叉 | ✅ 一致 | ⚠️ **"欧洲 35 国"（扫描覆盖范围）vs "光伏 34 国 / 风电 23 国"（实际命中分布）—— 两个不同的国数，别混用** |
| 国别分布 | 光伏：西班牙 **2766**、希腊 **1860**、意大利 **753**、德国 **672**（四国合计占 76%）；风电：德国 **212**、意大利 **192**、土耳其 **84**；荷兰：光伏 132 + 风电 9 = 141 | 索比光伏网快照逐字 | ✅ 已核 | ⚠️ **单源**（索比转载 Modat 报告），慧知数据只给总量不给国别 → 国别明细标"单源" |
| 扫描范围 | "报告调查了装机容量介于 **1MW 至 4GW** 的在运工业光伏电站，**不包括屋顶光伏**" | 索比快照逐字 | ✅ 已核 | ⭐ **"不含屋顶光伏"是关键限定** —— 我方**分布式（尤其户用）不在该报告覆盖内**，不能拿它论证分布式暴露规模 |
| **免密登录规模** | "a security researcher in Kassel, Germany, found a way into the administrator accounts of Sungrow's iSolarCloud platform without needing a password. According to the report published by his firm, Jakkaru, the access covered about **470,000** Sungrow systems in Europe, roughly **250,000** of them in Germany with a combined peak output of **7.8 GW**" | BESS Xchange 快照逐字 + 慧知数据同源转述（"约47万套系统，德国约25万套，**17吉瓦**"） | ⚠️ **套数一致，装机口径冲突** | ⭐⭐ **本期最重要的冲突**：同为"德国约 25 万套"，**BESS Xchange 说 7.8 GW，慧知数据说 17 GW** —— 差 **2.2 倍** |
| 冲突成因分析 | 慧知数据："据《时代周报》10月报道，一名安全研究员在某逆变器厂商的云平台上发现一个没有口令的管理员账号……对应装机约 17 吉瓦。**厂商否认可通过该账号更改逆变器设置**，并表示已做热修复" | 对比两源原文 | ⚠️ **两个数都不是"错的"，但不是同一口径** | ✅ **最可能的解释**：7.8 GW = **峰值输出（peak output）**，17 GW = **名义/装机容量（nameplate）**；户用逆变器两者比值普遍 >2。⚠️ **未经证实，只能标"疑为口径差"**。**引用德国容量必须写明"7.8 GW（峰值口径，BESS Xchange）"或"17 GW（名义口径，时代周报转述）"** |
| 全球规模 | particle.news 口径："roughly 250,000 inverters in Germany, about 500,000 in Europe and about **2.2 million devices worldwide**" | 该源**未抓快照**，仅检索摘要 | ⚠️ **单源（未归档）** | ⚠️ 欧洲数 500,000 与 BESS Xchange 的 470,000 **不一致**（约 6% 差），疑为"约"字口径。**不采信具体值，仅记"全球量级百万级"** |
| **攻击者能否控制逆变器** | 慧知数据："**厂商否认可通过该账号更改逆变器设置**"；particle 摘要称研究者称"remotely stop inverters or install malware" | 两源对照 | ⚠️ **双方表述存在差异，未定论** | ⭐ **这是本事件最关键的事实分歧**：厂商说"不能改设置"，研究者说"可以停机/装马"。**本库立场：厂商否认与研究者声称并存，未有第三方独立验证 → 引用时必须两边都写** |
| 厂商修复时效 | "Sungrow closed the gap **within a day** of being told in late August"；另一处"厂商称已于 **8月25日**完成修复（**距收到报告三天**）" | BESS Xchange + 慧知数据两源 | ✅ 一致（1 天 vs 3 天均为"数日内"） | ⚠️ **1 天与 3 天有出入**，但量级一致（当天/数日内），**不视为实质冲突** |
| 是否被利用 | "厂商……**未发现被利用的迹象**"；"its logs show **no one else exploited it**" | 两源一致 | ✅ 一致 | ✅ **重要事实：这是负责任披露的"发现-修复"，不是攻击事件** |
| **Germany Times "近失事件"说法** | "hackers **gained remote access** to hundreds of thousands of solar photovoltaic inverters across Germany……could have allowed attackers to **abruptly disconnect eight gigawatts** of power, **narrowly avoiding** a major disruption" | 快照全文核对 | ⚠️⚠️ **重大事实问题** | ⭐⭐ **该文页面自带声明："An advanced artificial intelligence (AI) system generated the content of this page on its own"** —— **这是一篇 AI 生成的新闻稿，不是记者报道**。它把"研究者负责任披露 + 厂商否认可控制 + 未发现被利用"**重写成"黑客已获得远程访问 + 险些造成大面积停电"**。**8 GW 这个数在原始披露（BESS Xchange 口径 7.8 GW）中并不存在独立出处** |
| **DIVD / ENCS 的 CVE 数量** | "荷兰的 DIVD 与 ENCS 两家机构……累计提交 **100 多个 CVE**；其中一个被发现的太阳能控制面板，管理着 **10 吉瓦容量、100 万用户**，登录绕过的方式简单到'**把登录类型设成 5**'" | 慧知数据快照逐字 | ⚠️ **单源（转述"欧洲网格安全论坛公开信息"）** | ⭐ **"login_type 设为 5"是最可复现的绕过手法**，与库内已记的 Sungrow CVE-2026-107194（`login_type":"5"`，CVSS 9.2）**同一手法** —— 交叉印证成立 |
| ENCS 现场演示 | "一台被攻陷的家用扫地机器人，通过家庭网络里的 **Modbus** 协议，关掉了相连的电池储能系统。**Modbus 是上世纪七十年代的明文协议，没有认证**" | 慧知数据快照逐字 | ⚠️ 单源（转述） | ⭐ **演示的是"从消费级设备横向进入家庭网络再打到 BESS"** —— 路径意义 > 演示本身 |
| 相关 CVE | CVE-2026-107194：Sungrow iSolarCloud 认证绕过，`login_type":"5"`，**CVSS 9.2**，影响 2026 之前版本 | 检索摘要（未单独抓快照） | ⚠️ **单源、未归档** | ⚠️ **不作为独立事实引用**，仅作为与 DIVD/ENCS 手法互证的旁证 |
| 我方内部实证（对照） | 我方 WAF 2026-11-12 起观测到 `.svn/entries` 探测 28 次、16 个 IP 批量扫描备份文件、2026-11-14 出现 `/.git/config` 探测 | 内部巡检报告（见 epicsDerExposure 文档） | ✅ **内部一手实证** | ✅ **这正是本文对我方的核心价值：外部威胁画像与内部观测指向同一类问题** |

> **核查小结**：**BSI 指南的要求条款与 Modat 扫描的规模数字两源以上一致，可信度高**。**三个必须写明的冲突/缺口**：① **德国装机容量 7.8 GW（峰值口径）vs 17 GW（名义口径）差 2.2 倍** —— 疑为口径差，未证实，引用必须带标签；② **"厂商能否通过该账号控制逆变器"存在双方表述冲突，未有第三方独立验证**；③ **Germany Times 的"近失攻击"叙事不可采信** —— 该页自述由 AI 自动生成，且其"黑客已获得访问""险些停电"的表述与原始披露（研究者披露、厂商否认、未发现被利用）**实质不符**。

---

## 三、原文归档（快照）

| 快照 | SHA256 | 抓取时间 | 大小 |
|---|---|---|---|
| `raw/snapshots/security/bsi-germany-pv-guidance-smm.md` | `ebdf2fd932af920ab18eb49e18adf2c3bd629c6291220c69c007179bd033a517` | 2026-11-15 07:12:15 | 5,029 字符 |
| `raw/snapshots/security/sungrow-bsi-der-exposure-cn-roundup.md` | `3449c0196a13162a9094e0f1826897c2cb36d9a1c90f9fc63d645ffac0e0f0c2` | 2026-11-15 07:12:14 | 18,098 字符 |
| `raw/snapshots/security/sungrow-isolarcloud-470k-jakkaru-disclosure.md` | `36f3dbbf72f8016bba81ddb3bfae4ed8154f1cc9586fb9dc34910663a7ccd6d4` | 2026-11-15 07:12:13 | 4,443 字符 |
| `raw/snapshots/security/germany-solar-inverter-near-miss-8gw.md` | `de57e1e01c8b7e0595191defd2473ef22d9293fb4dbb96b9b66188381bfee532` | 2026-11-15 07:11:51 | 9,785 字符 |

> ⚠️ **`germany-solar-inverter-near-miss-8gw.md` 快照的正文质量说明**：该页正文主体为 AI 生成内容与站点导航，正文可用信息仅开头一段摘要（约 120 字符）+ **一段关键的 AI 生成声明**。**本库保留该快照作为"该信源不可采信"的留档证据**，第 2 段已按此处理。

**关键原文摘录（SMM，快照逐字）**：

> Germany's Federal Office for Information Security (BSI) has issued cybersecurity guidance recommending that **PV plant operators of all sizes eliminate direct internet connections to control systems** to reduce the risk of cyberattacks. The guidance recommends using **secure virtual private networks (VPNs) and multi-factor authentication (MFA)** to protect remote access, alongside **timely software and security patch updates and regular security checks of connected devices**. As digitalization and remote monitoring become increasingly prevalent in solar PV operations, stronger cybersecurity measures **could increase compliance and operating costs for plant operators, inverter manufacturers and digital monitoring system providers**.

**关键原文摘录（慧知数据，快照逐字 · 含口径标注）**：

> 德国联邦信息安全办公室 **BSI-CS 154** 技术警示（2026年10月13日发布，据公开报道）——建议光伏（各种规模）、风电、水电、沼气、垃圾发电及食品制冷系统的运营商，**将控制系统与互联网的直接连接移除**；涉及工业控制器、通信设备、监控网关、逆变器、SCADA系统与远程监控平台；**远程访问至少经VPN、使用强口令并尽可能启用多因素认证**；及时安装软件与固件更新；**定期检查设备在互联网上的可见性，建立联网资产与通信接口清单，清单须包含安装商或服务商设置的远程维护链路（含独立移动数据连接）**；**办公网与生产网分离**，远程访问仅限获批人员与服务商；评估与厂商云的长期连接是否为日常运行所必需。（境外监管机构文件与公开报道口径）
>
> 欧洲光伏与风电场暴露面扫描（荷兰 Modat 公司与荷兰国家网络安全中心，2026年10月初，据公开报道）——发现 **8547** 个不应公开可达的互联网暴露系统，其中 **7942** 个位于 34 个国家与地区的光伏站点……（第三方机构扫描口径，非官方统计）
>
> 逆变器厂商云平台安全事件（据德国《时代周报》10月报道及厂商回应）——安全研究员发现某逆变器厂商云平台存在**无口令管理员账号**，可访问欧洲约 **47万套**光伏系统、其中约 **25万套**位于德国，对应装机约 **17吉瓦**；**厂商否认可通过该账号更改逆变器设置**，并表示已完成热修复……**未发现被利用迹象**。（境外媒体与厂商回应口径，双方表述存在差异，以官方通报为准）

**关键原文摘录（Germany Times，快照逐字 · AI 声明）**：

> **AI Disclaimer**: An advanced artificial intelligence (AI) system generated the content of this page on its own. This innovative technology conducts extensive research from a variety of reliable sources, performs rigorous fact-checking and verification, cleans up and balances biased or manipulated content, and presents a minimal factual summary that is just enough yet essential to you to be informed and interested in this important topic. Please keep in mind, however, that this technology is an evolving technology, and as a result, the article may contain **accidental inaccuracies or errors**.

**关键原文摘录（BESS Xchange，快照逐字）**：

> A security researcher in Kassel, Germany, found a way into the administrator accounts of Sungrow's iSolarCloud platform **without needing a password**. According to the report published by his firm, Jakkaru, the access covered about **470,000** Sungrow systems in Europe, roughly **250,000** of them in Germany with a combined peak output of **7.8 GW**. Sungrow closed the gap **within a day** of being told in late August and says **its logs show no one else exploited it**.

---

## 四、概要提取

- **德国 BSI-CS 154（2026-10-13）**：建议**取消电站控制系统与互联网的直接连接**，改用 VPN + 多因素认证，并**建立联网资产与通信接口清单**（清单须含安装商/服务商设置的远程维护链路，**含独立移动数据连接**），办公网与生产网分离 —— **这是国家级监管机构的明确要求，不是学术建议**
- **欧洲 35 国扫描出 8547 个公网暴露风光系统**，其中光伏 7942 个（34 国）、风电 605 个（23 国）；光伏暴露最多四国：西班牙 2766、希腊 1860、意大利 753、德国 672（占 76%）；**报告只覆盖 1MW–4GW 工业电站，不含屋顶光伏**
- **逆变器云平台免密管理员账号**：研究者从普通客户账号越权到安装商管理员账号，覆盖欧洲约 **47 万套**（德国约 25 万套），**厂商 1–3 天内修复，日志未显示被他人利用**
- ⭐ **容量口径冲突必须写明**：德国 25 万套对应 **7.8 GW（峰值口径，BESS Xchange）vs 17 GW（名义口径，时代周报转述）**，差 2.2 倍
- ⭐ **"厂商能否控制逆变器"存在双方表述冲突**：厂商否认，研究者称可停机/装马，**无第三方独立验证**
- ⚠️ **Germany Times 的"黑客已获得访问、险些 8 GW 停电"叙事不可采信** —— 该页自述 AI 自动生成，且与原始披露实质不符
- DIVD 与 ENCS 为多家逆变器厂商累计提交 **100 多个 CVE**，一个控制面板管 **10 GW / 100 万用户**；绕过手法是"**把登录类型设成 5**"，现场演示**扫地机器人经 Modbus 明文协议关停相邻 BESS**

---

## 五、主要观点

**原文主张**

- BSI（经 SMM 转述）：取消直连是"**强烈建议**"，适用"各类规模的光伏电站"；加强防护"**或将增加运营商、逆变器制造商与监控系统供应商的合规与运营成本**"
- Modat × NCSC-NL：欧洲风光场"**8547 个不应公开可达的系统暴露在互联网上**"
- Jakkaru / BESS Xchange：研究者从普通账号越权到管理员，触及 47 万套系统；**厂商一天内修复，日志未显示被利用**
- 厂商回应（经慧知数据转述）：**否认可通过该账号更改逆变器设置**，已完成热修复
- DIVD / ENCS：已为 Sungrow、Mennekes、Huawei、SolarEdge、Growatt 等累计提交 100 多个 CVE；现场演示从被攻陷的消费级设备经 Modbus 关停 BSS

**我方判断**

- ✅ **BSI-CS 154 的价值高于所有漏洞新闻**：它是**国家级监管机构对"电站控制系统直连互联网"提出的整改要求**，且清单要求极其具体（**联网资产与通信接口清单**、**含独立移动数据连接**、**办公网与生产网分离**）。**"含独立移动数据连接"这一条是我方的当务之急** —— 光伏场站的 4G/5G 随身路由几乎不可能进任何资产台账，但它是**完全绕过所有边界防护的旁路**，WAF 对它无效。这是我方与客户沟通时最有说服力的具体抓手。
- ✅ **"联网资产清单"正是我方托管业务的天然抓手**：BSI 要求运营主体维护清单，而**我方托管平台本来就是这些资产的登记与运维入口** —— 已有客户关系与接入点。这条对我方不是"防御成本"，而是**服务能力的机会**，但**本阶段口径下只能标观察项，不能写成产品规划**。
- ⚠️ **Modat 报告的规模数字不能用来论证我方暴露面，也不能用来论证"分布式同样严重"**：报告明确**只覆盖 1MW–4GW 工业电站、不含屋顶光伏** —— **我方分布式主战场（尤其户用）根本不在这个样本里**。任何"欧洲 8547 个暴露系统"的说法被拿来做分布式风险论证，都是**样本外推**。这是本期最容易犯的推理错误。
- ⚠️ **7.8 GW vs 17 GW 必须并存引用**：这两个数都不是"假的"，但**大概率是峰值口径 vs 名义口径**（户用逆变器比值 >2 很常见）。我方若在给客户的材料里引用"德国 25 万套对应 17 GW"，一旦对方手上有 7.8 GW 的原始出处，就会**当场失信**。**规则：引用必须写成"7.8 GW（峰值口径）/ 17 GW（名义口径）"**。
- ⚠️ **"免密登录"≠"被攻破"**：本案是**负责任披露**（研究者发现 → 厂商 1–3 天修复 → 日志无他人利用），不是攻击事件。**Germany Times 那篇 AI 生成稿把它写成"黑客已获得访问、险些造成 8 GW 停电"，是典型的叙事升级失真**。我方若在内部材料里引用"德国发生逆变器大规模攻击"，是**引用了一个不存在的攻击事件**。这条纪律与库内 11-13 已记的"评分冲突不是错误、口径不同不是错误"是同一原则的另一面：**信源失真同样是失真，且比口径差更危险**。
- ✅ **"把登录类型设成 5"这类业务逻辑绕过，与我方的关联点是"自研系统的越权设计"**：绕过手法本身是供应商特有，但**"普通账号可越权到管理员账号"这一缺陷类别是通用的**。库内 [epicsDerExposure-2026-11](epicsDerExposure-2026-11.md) 已记 PTM `logisticsFileDownLoad` 命中 `m_response`（疑似后端异常处理不当）—— **我方自研系统的鉴权/越权自查清单，本条再加一条具体攻击手法样本**。
- ⚠️ **"扫地机器人经 Modbus 关停 BESS"这个演示对我方的启示不是"Modbus 不安全"**：我方光伏场站里的 Modbus（逆变器通信、汇流箱）比家庭网络重要得多。**启示是"消费级/办公网设备与生产网络之间必须有边界"** —— 这与 BSI 的"办公网与生产网分离"是同一条要求，**监管语言已经给了现成的措辞**，我方基线条目可以直接引用。

---

## 六、参考意义

> 📌 **本阶段口径（2026-11-12 起）**：转评审只看 **网络安全 / 信创 / 等保 / 隐私保护 / 护网** 五方向，**暂不精到具体产品**；产品线级关联一律标 🟡 **待复核**。本文属**网络安全 + 护网**方向，且含**我方侧一手观测**（WAF 巡检报告）→ **第 1 关可证**。

| 方向（五方向） | 可证事实 | 本阶段处理 |
|---|---|---|
| **网络安全** | ① 德国 BSI-CS 154 国家级要求：取消直连 / VPN+MFA / **联网资产与通信接口清单（含独立移动数据连接）** / 办公网与生产网分离；② 我方 WAF 已实测到 `.svn/entries`（28 次）、备份文件批量扫描（16 IP）、**`.git/config` 探测（11-14，2 次）** | ✅ **进评审（方向级）** —— 并入 [对外站点暴露面专项自查](../deliverables/remediation-exposureHygiene-20261112.md)（P0）与 [攻击手法→防线覆盖度对照](../deliverables/remediation-defenseTacticCoverage-20261112.md)，新增"**联网资产与通信接口清单**"基线条目与"**独立移动数据连接**"专项排查项 |
| **护网 / 攻防准备** | 攻击手法样本新增：① **业务逻辑越权**（普通账号→管理员账号，`login_type=5` 型）；② **消费级设备→生产网横向**（Modbus 明文链路）；③ **运维旁路**（4G/5G 随身路由绕过边界） | ✅ **进方向级对照表**，补三行手法 × 防线覆盖度 |
| **等保** | "联网资产清单"与"办公网/生产网分离"是等保 2.0 通用要求的高质量对标口径 | ⚠️ **仅作基线措辞参考**，本文无我方等保侧一手证据 → **不单独立项** |
| **信创 / 隐私保护** | 本期无新增可证事实 | — |

**暴露面判定（按评审第 1 关三问）**：

| 对象 | 在我方暴露面？ | 依据 |
|---|---|---|
| 我方对外站点 VCS/备份文件残留 | ✅ **是** | 我方 WAF 实测探测（`.svn` / `.git` / 备份文件），已实证 |
| 我方托管电站的**设备直连公网** | ⚠️ **待确认** | 我方侧无直接观测；但**我方托管对象正是 DER**，且 BSI 已把它定为监管整改项 → **需向托管客户/运维取资产清单** |
| 我方场站的**独立移动数据连接（4G/5G 路由）** | ⚠️ **待确认（高优先级）** | BSI 明确点名；我方无台账覆盖该类接入 → **P0 排查项** |
| Sungrow iSolarCloud / 逆变器厂商云 | ❌ **否** | 我方不使用该云平台管理我方资产（我方走自有托管与监控平台） |
| Modat 报告的 8547 个系统 | ❌ **否**（且样本不含屋顶光伏） | 欧洲资产，非我方资产 |

**产品线级关联（🟡 待复核 · 按本阶段口径不落产）**：

| 影响产品线 | 影响点 | 是否需改行为 |
|---|---|---|
| 品能者托管 · 联网资产台账 | 新增清单维度：**通信接口 + 远程维护链路（含独立移动数据连接）**（BSI 口径） | 🟡 **需改**（字段扩容） |
| 兆瓦快链 · 电站接入与运维 | 4G/5G 随身路由排查；VPN + MFA 接入规范；办公网/生产网分离 | 🟡 **需改**（排查 + 规范） |
| 全部对外站点 | P0 暴露面自查（并入既有产物） | ⚠️ **已有 P0 产物，本条不新开** |
| 护网演练 | 三类新手法（业务逻辑越权 / 消费级设备横向 / 运维旁路） | 🟡 需改（对照表补行） |
| PTM 现货交易平台 | 越权自查样本再增一条 | 🟡 需改（并入既有自查） |

---

## 七、总结输出

**一句话结论**：欧洲光伏 DER 暴露面本期出现三个新事实 —— **德国 BSI-CS 154（2026-10-13）以国家级监管要求的形式规定"取消电站控制系统直连互联网、建立含独立移动数据连接的联网资产与通信接口清单"**、**Modat×NCSC-NL 扫描出欧洲 35 国 8547 个公网暴露风光系统（光伏 7942，仅覆盖 1MW–4GW 工业电站、不含屋顶光伏）**、**研究者披露逆变器云平台免密管理员账号触及欧洲 47 万套系统（厂商 1–3 天修复、日志无他人利用）**；对我方而言**最该抓的不是漏洞而是那份清单要求**（4G/5G 运维旁路是我方台账完全没覆盖、而 WAF 又管不到的真实缺口），但**引用时必须写明"德国 25 万套 = 7.8 GW（峰值）/ 17 GW（名义）"两个口径并存**，且**不得采信"德国发生逆变器大规模攻击"的叙事**（Germany Times 该页自述由 AI 自动生成，与原始披露实质不符）。

**落地去向**

- [ ] **产品特性** —— 🟡 **待复核**：托管资产台账新增"**联网资产与通信接口清单**"维度（BSI-CS 154 口径），清单须覆盖安装商/服务商设置的远程维护链路**与独立移动数据连接**
- [ ] **需求变更** —— 🟡 **待复核**：电站远程接入规范统一为 **VPN + MFA**，并落实**办公网与生产网分离**（措辞直接引用 BSI，便于对客沟通）
- [ ] **专项整改** —— ✅ **P0 排查项**：**独立移动数据连接（4G/5G 随身路由）专项排查** —— 它绕过全部边界防护且不在现有台账内；并入既有 [对外站点暴露面专项自查](../deliverables/remediation-exposureHygiene-20261112.md)，**不新开产物**
- [ ] **专项整改** —— 并入 [攻击手法→防线覆盖度对照](../deliverables/remediation-defenseTacticCoverage-20261112.md)：新增三类手法行 —— **业务逻辑越权**（普通账号→管理员账号）、**消费级设备经 Modbus 横向到生产网**、**运维旁路（移动数据连接）**
- [ ] **跟踪项** —— 向托管客户/运维取**联网资产与通信接口清单**以判定我方暴露面（第 1 关待证）；跟踪 Modat 报告后续（是否出分布式/户用样本）；关注"厂商能否控制逆变器"争议的第三方验证；本条全部引用须带口径标签，并**剔除 Germany Times 的 AI 生成叙事**

---

## 参考链接

- [SMM PV Flash：Germany Recommends Stronger Cybersecurity for Solar PV Plant Control Systems](https://news.metal.com/en/newscontent/104166764-smm-pv-flash-germany-recommends-stronger-cybersecurity-for-solar-pv-plant-control-systems)
- [慧知数据：2026年10月18日虚拟电厂行业早报 —— 德国让光伏退出公网，荷兰数出 8547 个暴露口（逐条标注口径与来源）](https://www.huizhidata.com/article/376)
- [BESS Xchange：A Password-Free Login Reached 470,000 Sungrow Systems](https://bessxchange.com/article?slug=a-password-free-login-reached-470000-sungrow-systems-india-should-keep-track-404)
- [Germany Times：Energy Grid Operators Patch Vulnerabilities After Near-Miss Cyberattack on Solar Inverters（**AI 生成稿，不采信**）](https://germanytimes.com/ntkmmr-energy-grid-operators-patch-vulnerabilities-after-near-miss-cyberattack-on-solar-inverters)
- [浙江省外贸预警：德国建议取消对光伏电站控制系统的直接互联网接入](http://www.zjmade.cn/ecloud/plat/site/detail.html?newsId=4A7235B0A58B4794A7CE2F0179F38463)
- [索比光伏网：超 8000 个风光系统公网"裸奔"！Modat 预警欧洲电网安全风险（国别分布明细）](https://m.solarbe.com/21-0-50030603-1.html)
- [同族文档：EPICS 工控漏洞 + 分布式光伏 DER 暴露面研究（2026-11）](epicsDerExposure-2026-11.md)
- [既有产物：对外站点暴露面专项自查（P0）](../deliverables/remediation-exposureHygiene-20261112.md)
- [既有产物：攻击手法→防线覆盖度对照](../deliverables/remediation-defenseTacticCoverage-20261112.md)

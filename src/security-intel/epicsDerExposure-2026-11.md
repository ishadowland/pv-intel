# EPICS Base 四个工控漏洞 + 分布式光伏 DER 暴露面研究 — 2026-11

> 🟡 有影响 · CISA ICSA-26-300-01(Rev.1) · 2026-10-27 发布 · 核心标识：EPICS 不在我方栈内 / DER 暴露面直接命中我方业务

---

## 一、信源核实

| 项 | 值 |
|---|---|
| 来源请求 | `2026年11月 高危漏洞 CVE 光伏 电站 SCADA 工控 攻击 安全`（web_search） |
| 原始 URL（主·漏洞） | https://cn-sec.com/archives/5551496.html （CN-SEC《11月2日高危漏洞紧急预警》，含四 CVE 完整技术口径） |
| 原始 URL（辅 1） | https://seclog.org/stories/cisa-warns-four-epics-base-vulnerabilities-including-critical-cve-2026-114595-could-let-attackers-cr.html |
| 原始 URL（辅 2） | https://www.hubwiz.com/blog/ai-agent-found-four-epics-vulnerabilities/ （汇智网·中译） |
| 原始 URL（辅 3） | https://www.thenextgentechinsider.com/pulse/ai-agent-cipher-discovers-four-critical-vulnerabilities-in-epics-software |
| 原始 URL（主·暴露面） | https://www.conceptio.app/document/667918/grid-trouble-in-paradise-uncovering-vulnerable-distributed-energy-reso （Conceptio · 学术论文《Grid Trouble in Paradise》） |
| 原始 URL（辅 4·OT通告） | https://www.ervik.as/ot-security （CISA CSAF 官方源镜像，实时索引） |
| 原始 URL（辅 5·同类） | https://rootpwn.me/cves/CVE-2026-115803 （Scada-LTS 授权绕过） |
| 发布主体 | CISA（通告）· CN-SEC（中文解读）· Conceptio（论文） |
| 发布/更新时间 | CISA 通告 **2026-10-27** · 中文解读 **2026-11-04** · 论文 **2026-09-07** |
| 采集时间 | 2026-11-12 12:12–12:13 |
| 快照 | `raw/snapshots/security/epics-cve-2026-11-02.md` · `raw/snapshots/security/der-exposure-grid-trouble-in-paradise.md` |

---

## 二、事实核查

| 数据点 | 原文表述 | 核查方式 | 结论 | 备注 |
|---|---|---|---|---|
| CVE-2026-114595 | CWE-190 整数溢出，**CVSS v3.1 9.8 / v4.0 9.3**（AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H） | CN-SEC 快照逐字 + 3 个独立源交叉 | ✅ 一致 | **两套口径都核到了**，多数报道只抄 9.8 |
| CVE-2026-114596 | CWE-190 整数溢出，**v3.1 8.2 / v4.0 8.8**，C:N | 同上 | ✅ 一致 | |
| CVE-2026-114597 | CWE-130 长度参数不一致，**v3.1 7.5 / v4.0 8.7** | 同上 | ✅ 一致 | |
| CVE-2026-114598 | CWE-843 类型混淆，**v3.1 7.5 / v4.0 8.7**，A:N | 同上 | ✅ 一致 | |
| 受影响版本 | EPICS Base **7.0.10 及更早** | 3 源一致 | ✅ 一致 | |
| 修复版本 | **7.0.11** | 3 源一致 | ✅ 一致 | |
| 免认证/无需交互/仅需可达 | 全部四项 | CISA 通告口径，CN-SEC 引用 | ✅ 一致 | **决定严重性** |
| 受影响协议端口 | Channel Access / pvAccess → **TCP 5064 与 5075** | CN-SEC 快照逐字 | ✅ 一致 | |
| 使用范围 | 全球约 **90 个**大型科研/高校/工业项目，含 ITER 聚变堆控制系统、阿贡 APS | 多源一致 | ✅ 一致 | |
| 发现方式 | Causal Security 自主 agent **Cipher**，耗时 **3 小时 49 分**（一说 4 小时内） | 汇智网/NextGen/TechInsider 三源 | ✅ 一致 | 精确时长为汇智网口径，另有"4小时内"表述 |
| 发现者背景 | 洛斯阿拉莫斯与阿贡国家实验室最初开发 EPICS | 多源一致 | ✅ 一致 | |
| DER 论文核心结论 | 全球光伏装机自 2022 翻倍以上；大量系统由安装商/终端用户配置并直接联网；**真实暴露规模此前被严重低估** | 论文摘要快照 + 独立转述 | ✅ 一致 | **"低估"是论文的定性结论** |
| Subnet Solutions PowerSYSTEM Center | ICSA-26-307-01 **critical**，CVE-2026-63017 / CVE-2026-63774，SQL 注入可执行未授权 SQL | Ervik CSAF 索引 | ✅ 一致 | **与电网监控相关，与我方同类** |
| Hitachi Energy CoreTec | ICSA-26-302-03 **high 8.8** | 同上 | ✅ 一致 | |
| Scada-LTS CVE-2026-115803 | 2.8.0 AmCharts Data API 授权绕过，`ids` 参数篡改可越权读数据与配置 | rootpwn 条目 | ⚠️ 仅一源 | |
| `45.138.12.51` 探测 `.svn/entries` | 28 次 / 5 小时，目标 `182.140.209.35:18443` | 内部 WAF 巡检报告 2026-11-12 08:41 | ✅ 内部实证 | 报告原文在 `waf-inspection-report-latest.md` |
| `42.92.x.x` 批量探测备份文件 | 16 个 IP，目标 `idmo.pinnenger.com:11443`，探测 `/wwwroot.zip` `/webs.rar` `/webapps.zip` `/php.zip` `/web.tar.gz` `/web001.tar.gz` `/pinnenger.com.sql` `/pinnengercom.sql` | 内部 WAF 报告 | ✅ 内部实证 | 2026-11-11 23:18–23:47 集中爆发 |
| `49.73.18.161` 命中 `m_response` | 目标 `ptm.pinnenger.com:1443/itps/ptm/allocation/logisticsFileDownLoad`，规则 `policy_rule44`，High，2 次 | 内部 WAF 报告 2026-11-12 11:34 | ✅ 内部实证 | 事件 ID `1e3ccc0d8744487c933807ab0e0956d2` |

> **核查小结**：四个 CVE 的编号/评级/版本/端口由 ≥3 个独立源确认，**可信**；DER 论文结论为原文摘要直引，**可信**；Scada-LTS CVE-2026-115803 仅一源，**标记待核**；内部 WAF 三组数据为一手观测，**可信度最高**。

---

## 三、原文归档（快照）

| 快照 | SHA256 | 抓取时间 | 大小 |
|---|---|---|---|
| `raw/snapshots/security/epics-cve-2026-11-02.md` | `637c0b5644f6dc62…` | 2026-11-12 12:12:23 | 18,004 字符 |
| `raw/snapshots/security/der-exposure-grid-trouble-in-paradise.md` | `51ff4d9df22b65f5…` | 2026-11-12 12:12:24 | 15,018 字符（截断） |

**关键原文摘录（CN-SEC，快照逐字）**：

> CISA 于 10 月 27 日发布 ICSA-26-300-01(Revision 1)，针对的是 EPICS Base——由洛斯阿拉莫斯与阿贡国家实验室最初开发、用来搭建分布式 SCADA 系统并把操作员接到物理设备的开源工控工具包，全球约 90 个大型科研、高校与工业项目在用，包括 ITER 聚变堆的控制系统与阿贡国家实验室的先进光子源(APS)。公告覆盖 **7.0.10 及更早版本**，共列四个漏洞，全部为**免认证、无需用户交互、仅需网络可达**（涉及的协议是 EPICS 的 Channel Access 与 pvAccess，对应 **TCP 5064 与 5075**）。
>
> CVE-2026-114595，CWE-190 整数溢出，CVSS v3.1 **9.8** / v4.0 **9.3**（AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H），机理是网络请求处理中以错误的尺寸分配内存，后续处理攻击者可控数据时导致内存破坏、拒绝服务或可能的远程代码执行；
> CVE-2026-114596，CWE-190 整数溢出，v3.1 **8.2** / v4.0 **8.8**，是协议解析阶段的消息长度校验失效，触发越界内存写并影响控制流，其向量中机密性影响记为 C:N；
> CVE-2026-114597，CWE-130 长度参数不一致，v3.1 **7.5** / v4.0 **8.7**；
> CVE-2026-114598，CWE-843 类型混淆，v3.1 **7.5** / v4.0 **8.7**。

**关键原文摘录（Conceptio 论文摘要，快照逐字）**：

> Grid-connected solar distributed energy resources (DERs), such as solar inverters and monitoring platforms, have been deployed at unprecedented scale over the past few years, with global solar capacity more than doubling since 2022. To support monitoring and control, many of these systems are Internet-connected and configured by installers or end users, yet **the real-world scale of their Internet exposure and the implications for power grid operation remain poorly understood**. In this paper, we present an Internet-scale evaluation of exposed and vulnerable solar DER infrastructure, and assess the risk that compromised DERs can pose to energy grids.

**关键原文摘录（内部 WAF 巡检报告，2026-11-12 08:41 / 11:34）**：

> | `45.138.12.51` | `https://182.140.209.35:18443/.svn/entries` | 28 次 | ✅ 已拉黑 |
> | `49.73.18.161` | `https://ptm.pinnenger.com:1443/itps/ptm/allocation/logisticsFileDownLoad` | 2 次 | ⚠️ 待人工确认 |

---

## 四、概要提取

- **EPICS Base 四个漏洞全部免认证、仅需网络可达**，最严重的 CVE-2026-114595（v3.1 9.8 / v4.0 9.3）可导致越界堆写与潜在 RCE，修复版本 7.0.11
- 受影响协议为 **TCP 5064 / 5075**，EPICS 用于分布式 SCADA，全球约 90 个科研与工业项目在用（含 ITER 聚变堆）
- **漏洞由 AI agent「Cipher」在 3 小时 49 分内挖出** —— OT 领域依赖"隐蔽性"的前提正在失效
- **学术界的结论直指我方业务形态**：光伏 DER（逆变器 + 监控平台）因安装商/终端用户配置而直接暴露公网，**真实暴露规模此前被严重低估**
- **我方内部 WAF 已观测到两类真实攻击**：`.svn/entries` 元数据探测 28 次、16 个 IP 批量扫描备份文件
- 另一条独立信号：**PTM `logisticsFileDownLoad` 命中响应侧规则 `m_response`** —— 攻击点在响应内容，更像后端异常处理不当
- CISA 2026-11 同期通告：**Subnet Solutions PowerSYSTEM Center（电网监控）CVE-2026-63017 SQL 注入** —— 与我方监控平台同类

---

## 五、主要观点

**原文主张**

- CISA/CN-SEC：四个漏洞"可使攻击者造成拒绝服务、破坏内存、泄露敏感信息，或可能执行任意代码"，公告覆盖 7.0.10 及更早版本
- 汇智网：*"EPICS 之后，OT 的'靠隐蔽性防守'结束了"* —— 自主 AI agent 3 小时 49 分找到 4 个未知漏洞
- Conceptio 论文：光伏 DER 的互联网暴露规模**"remains poorly understood"**，论文给出互联网规模的暴露与脆弱性评估，并评估被入侵 DER 对电网的风险
- CISA OT 通告：2026 年 11 月能源与制造领域仍有 critical 级通告（PowerSYSTEM Center）
- 内部 WAF 观测：攻击者正在**系统性寻找运维遗留物**（版本控制元数据、备份文件、数据库转储）

**我方判断**

- **EPICS 不在我方技术栈内** → 纯漏洞**不满足评审第 1 关"影响可证"**，不进 `deliverables/`。但它提供的结构性证据（工控协议栈长期无认证）指向了真正该关注的信号
- **DER 暴露面研究才是直接命中我方业务的那一条** —— 我方托管的正是分布式/集中式电站的逆变器与监控数据，"由安装商配置因而暴露公网"这个失效模式**在我方客户侧同样成立**
- **"探测备份文件"与论文结论高度吻合**：扫描者找的正是运维过程中遗留的凭据与配置，这类攻击不需要漏洞利用，门槛更低
- ⚠️ **WAF 全程 Deny ≠ 源站干净**。`.svn/entries` 被试 28 次说明扫描者确信这类路径存在；备份文件扫描若命中一个站点，攻击者会回来验证。**必须落到源站确认**
- **PTM 的 `m_response` 应先按后端缺陷处理而非攻击者** —— 响应侧规则意味着问题在服务端异常处理，这类"情报"实际是**产品缺陷线索**，比封 IP 更有价值
- CISA 的 PowerSYSTEM Center SQL 注入说明**电网监控类产品的认证绕过是活跃攻击面**，我方监控平台应做同类自查（API 鉴权、越权读）

---

## 六、参考意义

> 📌 **本阶段口径（2026-11-12 起）**：转评审只看 **网络安全 / 信创 / 等保 / 隐私保护 / 护网** 五个方向，**暂不精到具体产品**；产品线级关联一律标 🟡 **待复核**，不进排期。本文本身即**网络安全 + 护网**方向，且含**我方侧一手观测**（WAF 巡检报告），第 1 关可证。

| 方向（五方向） | 可证事实 | 本阶段处理 |
|---|---|---|
| **网络安全** | 我方对外站点被实测探测：`.svn/entries` 探测 28 次（5 小时）、16 个 IP 批量扫描备份文件（`.zip`/`.rar`/`.sql`/`.tar.gz`）、PTM `m_response` 响应侧命中 | ✅ **进评审（方向级）** —— 并入 [对外站点暴露面专项自查](../deliverables/remediation-exposureHygiene-20261112.md)（P0）：源站自查 + 发布流程阻断 |
| **护网 / 攻防准备** | 2026-11-12 新增拉黑 8 个 IP，**Info Leak ×5**（与备份文件探测同族）+ Code Injection / File Inclusion 各 1 | ✅ **进方向级对照表** —— 补入 [攻击手法→防线覆盖度对照](../deliverables/remediation-defenseTacticCoverage-20261112.md)，标注已覆盖/部分/未覆盖 |
| **信创 / 等保 / 隐私保护** | 本期无新增可证事实 | — |

**产品线级关联（🟡 待复核 · 按本阶段口径不落产）**：

| 影响产品线 | 影响点 | 是否需改行为 |
|---|---|---|
| 全部对外站点 | `.svn/` 残留目录、备份文件（`.zip`/`.rar`/`.sql`/`.tar.gz`） | ⚠️ **P0 需自查** |
| PTM 现货交易平台 | `logisticsFileDownLoad` 异常处理（疑似 SQL 堆栈外泄） | ⚠️ 需修 |
| 发布流程 | 产物含 VCS 元数据/备份文件未阻断 | ⚠️ 需加检查 |
| 品能者托管 / 兆瓦快链 | 监控平台 API 鉴权、越权读（对标 CVE-2026-115803 / PowerSYSTEM Center） | 🟡 需自查 |
| 安全情报采集 | CISA CSAF 源纳入 CVE watchlist | 🟡 需配置 |

**暴露面判定（按评审第 1 关）**：

| 对象 | 在我方暴露面？ | 依据 |
|---|---|---|
| EPICS Base 4 CVE | ❌ **否** | 我方技术栈为 Web 应用，不含 EPICS |
| 分布式 DER 暴露模式 | ✅ **是** | 我方托管对象即 DER；WAF 已观测到真实探测 |
| `.svn/` 残留 | ⚠️ **待确认** | WAF 探测 28 次说明攻击者有此预期，源站是否有需自查 |
| 备份文件残留 | ⚠️ **待确认** | 16 个 IP 批量探测，需源站自查 |
| PTM `m_response` | ✅ **是** | 我方系统命中，疑似后端异常处理不当 |

---

## 七、总结输出

**一句话结论**：EPICS 四个漏洞本身**不在我方暴露面**（不进评审），但它们与光伏 DER 暴露面研究指向同一个结构性事实 —— **光伏侧的运维遗留物就是当前真实攻击路径**，而我方 WAF 已经观测到 `.svn` 元数据探测（28 次）与 16 个 IP 的备份文件批量扫描，**下一步必须是源站自查，不是继续加黑名单**。

**落地去向**

- [x] **专项整改（P0）** —— 全站 `.svn/` 残留与备份文件自查清理；PTM 异常处理整改；发布流程加阻断
- [ ] 产品特性 —— 发布流水线自动检查（视自查结论决定是否产品化）
- [ ] 需求变更 —— 监控平台 API 鉴权/越权读加固（待专项自查结论）
- [ ] 跟踪项 —— Scada-LTS CVE-2026-115803 待核（仅一源）；CISA CSAF 源纳入 watchlist
- ❌ **不落产** —— EPICS 四 CVE（不在暴露面，第 1 关不过）

---

## 最新动态

> 本节按 `source_url` 去重规则累积更新（同一事件只更新此处，不另建文档）。
> **last_seen：2026-11-13 07:34**（内部 WAF 巡检报告 `waf-inspection-report-2026-11-12-203757.md`）

| 观测时间 | 事件 | 状态变化 |
|---|---|---|
| 2026-11-12 20:37（今日第 5/5 次巡检） | **今日新增拉黑 8 个 IP**：`177.10.160.46`（Code Injection）、`43.167.198.92`（File Inclusion）、`193.32.127.213` / `195.178.110.159` / `77.90.185.243` / `81.68.73.69` / `85.11.167.160`（**Info Leak ×5**）、`45.138.12.51`（用户手动确认拉黑） | ✅ **上期"待决"项闭环** |
| 2026-11-12 20:37 | **`45.138.12.51` 已由用户手动确认拉黑** | ✅ 闭环 —— 即上期 28 次 `.svn/entries` 探测的来源 |
| 2026-11-12 20:37 | 攻击类型分布：🛡️ Threat Intelligence **5** 个 / ❓ Unknown **1** 个，共 6 个源 IP，**需拉黑 0 个** | ⚪ 全部走默认忽略策略（fast-skip），WAF 默认拦截 |
| 2026-11-12 20:37 | 黑名单1000：WAF 实际 **175** 个 / 本地备份 366（活跃 175、已删 191），本次新增 0、失败 0 | ✅ 增删一致，无同步故障 |
| 2026-11-12 20:37 | 白名单豁免 **56** 个 IP，本次变化 **±0** | ⚪ 无变化 |

**新增信号（相对 2026-11-12 12:12 建档时）**：

- ✅ **Info Leak 成为本日新增拉黑的主要类型（5/8）** —— 与上期"批量探测备份文件（`/wwwroot.zip`、`/pinnenger.com.sql`）"的观测**同族**。攻击面含义：备份文件/敏感文件探测仍是外部真实尝试，**P0 专项整改（全站 `.svn/` 残留与备份文件自查）不能因"黑名单已加"而降级**
- ✅ **新增 Code Injection 与 File Inclusion 两类**（各 1 个），均为"单次攻击即自动封禁" —— 攻击面类型在扩大，但**单次量级低**，暂未见组合利用
- ⚠️ **WAF 侧结论不变**：新增拉黑全部是"单次攻击"级别，说明这类探测是**广撒网**而非定向；**"加黑名单"不能替代源站自查**
- ⚪ **威胁情报类 5 个 IP 均走 fast-skip 忽略**（规则内默认拦截、不二次分析、不推送）—— 这是既定策略，本期无异常

---

## 参考链接

- [CN-SEC：11月2日高危漏洞紧急预警（含 EPICS 四 CVE 完整技术口径）](https://cn-sec.com/archives/5551496.html)
- [Seclog：CISA warns four EPICS Base vulnerabilities](https://seclog.org/stories/cisa-warns-four-epics-base-vulnerabilities-including-critical-cve-2026-114595-could-let-attackers-cr.html)
- [汇智网：AI 挖出 4 个工控漏洞](https://www.hubwiz.com/blog/ai-agent-found-four-epics-vulnerabilities/)
- [TheNextGenTechInsider：AI Agent Cipher Discovers Four Critical Vulnerabilities in EPICS](https://www.thenextgentechinsider.com/pulse/ai-agent-cipher-discovers-four-critical-vulnerabilities-in-epics-software)
- [ThreatsHub：AI 'hacker' finds 4 severe bugs in industrial control software](https://www.threatshub.org/blog/ai-hacker-finds-4-severe-bugs-in-popular-industrial-control-software-in-under-4-hours)
- [Conceptio：Grid Trouble in Paradise — 分布式 DER 暴露面研究](https://www.conceptio.app/document/667918/grid-trouble-in-paradise-uncovering-vulnerable-distributed-energy-reso)
- [Ervik：OT & ICS Security Advisories（CISA CSAF 实时源）](https://www.ervik.as/ot-security)
- [rootpwn：CVE-2026-115803 Scada-LTS](https://rootpwn.me/cves/CVE-2026-115803)
- [CISA ICS Advisories 官方源](https://www.cisa.gov/news-events/ics-advisories)

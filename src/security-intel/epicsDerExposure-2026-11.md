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
| `raw/snapshots/security/epics-cve-2026-11-02.md` | `637c0b5644f6dc62947b3fb5f7aed8d9d59f8cc61fb4c6508a311ab3e6391050` | 2026-11-12 12:12:23 | 18,004 字符 |
| `raw/snapshots/security/der-exposure-grid-trouble-in-paradise.md` | `51ff4d9df22b65f56d112318ac88417c555ec825080831632b7eccf595be9ec9` | 2026-11-12 12:12:24 | 15,018 字符（截断） |

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
> **last_seen：2026-11-18 07:12**（内部 WAF 巡检报告 `waf-inspection-reports/waf-inspection-2026-11-17-*.md`，含 11-17 全部 5 次巡检；其中 **SSRF 首现条目已单独立档** → [wafSsrfProbeFirstAppearance-2026-11-17](wafSsrfProbeFirstAppearance-2026-11-17.md)）

| 观测时间 | 事件 | 状态变化 |
|---|---|---|
| 2026-11-12 20:37（今日第 5/5 次巡检） | **今日新增拉黑 8 个 IP**：`177.10.160.46`（Code Injection）、`43.167.198.92`（File Inclusion）、`193.32.127.213` / `195.178.110.159` / `77.90.185.243` / `81.68.73.69` / `85.11.167.160`（**Info Leak ×5**）、`45.138.12.51`（用户手动确认拉黑） | ✅ **上期"待决"项闭环** |
| 2026-11-12 20:37 | **`45.138.12.51` 已由用户手动确认拉黑** | ✅ 闭环 —— 即上期 28 次 `.svn/entries` 探测的来源 |
| 2026-11-12 20:37 | 攻击类型分布：🛡️ Threat Intelligence **5** 个 / ❓ Unknown **1** 个，共 6 个源 IP，**需拉黑 0 个** | ⚪ 全部走默认忽略策略（fast-skip），WAF 默认拦截 |
| 2026-11-12 20:37 | 黑名单1000：WAF 实际 **175** 个 / 本地备份 366（活跃 175、已删 191），本次新增 0、失败 0 | ✅ 增删一致，无同步故障 |
| 2026-11-12 20:37 | 白名单豁免 **56** 个 IP，本次变化 **±0** | ⚪ 无变化 |
| **2026-11-13 全天** | **无新增拉黑**（5 次巡检，新增 0、失败 0）；攻击源 IP 7 个（🛡️ 5 / ❓ 2），需拉黑 0 | ⚪ 全天静默，威胁情报类走 fast-skip |
| **2026-11-14 08:38（第 1/5 次）** | **新拉黑 `45.144.212.158`（Info Leak，1 次，置信度 0.97）** —— 目标 URL **`https://182.140.209.35:18443/.git/config`**，站点**兆瓦快链**，规则 `skynet_rule131091`，High，Deny，事件 ID `69cd9088c65445b38ced3f1c4fefcdec`，最近一次 05:40:44 | 🔴 **新模式：探测 Git 配置文件**（此前只有 `.svn/`） |
| **2026-11-14 11:37（第 2/5 次）** | 攻击源 6 个，需拉黑 0；本次新增 0、失败 0 | ⚪ 静默 |
| **2026-11-14 14:37（第 3/5 次）** | **新拉黑 `3.208.10.80`（Code Injection，1 次）** —— AI 自动封禁，置信度达自动拉黑阈值 | ⚪ 单次量级，暂未见组合利用 |
| **2026-11-14 17:37（第 4/5 次）** | **新拉黑 `64.225.54.158`（Info Leak，1 次，置信度 0.97）** —— 目标 URL **同为 `https://182.140.209.35:18443/.git/config`**，站点兆瓦快链，规则 `skynet_rule131091`，High，Deny，事件 ID `942a58da1bad4efb9820dff03efefaec`，最近一次 16:35:37 | 🔴 **同一路径、第二个来源 IP** —— 由单点试探转为**重复探测** |
| **2026-11-14 20:37（第 5/5 次）** | 攻击源 5 个（🛡️ 3 / ❓ 2），需拉黑 0；黑名单1000：WAF 实际 **178** 个 / 本地备份 369（活跃 178、已删 191），本次新增 0、失败 0；白名单 **56** ±0 | ✅ **当日净增 3 个（175→178），与三次拉黑一致，增删无同步故障** |
| **2026-11-15 08:37（第 1/5 次）** | **新拉黑 4 个 IP，全部 Info Leak**：① `167.94.146.54` → **`GET /phpinfo.php`**，Host `182.140.209.35:18443`（**兆瓦快链**），规则 `skynet_rule65719`，Medium，**Deny**，LLM `new_attack`/scanner/置信度 **0.90**，1 次，事件 ID `ff3eb38772ec4b3aaaf91f8db3a219b8`；② `93.123.109.214` → **`GET /.env.backup`**，同 Host，规则 `skynet_rule65669`，**Deny**，LLM `new_attack`/scanner/**0.94**，**5h 累计 5 次**，事件 ID `41ea65974b4944ce8761c4d20a01f201`；③ `35.241.77.208` → **`GET /docs/phpinfo.php`**，Host `www.pingreenmall.com:3443`（**续费商城**），规则 `skynet_rule65719`，**Deny**，LLM `new_attack`/scanner/**0.92**，**5h 累计 43 次**，事件 ID `13bec0a2421b43ed9d39efbba103c892`；④ `8.129.101.248` → `GET /d/txt/test.txt`，Host `ptm.pinnenger.com`（**品行者**），规则 `skynet_rule65718`，**WAF 动作 = Allow（未拦截）**，LLM 主模型与兜底模型**双双失败**，判定 `uncertain`/0.86，仍由 v15.4 兜底拉黑 | 🔴 **新模式：探测凭据文件与 PHP 诊断页** —— 探测路径从 `.git/config` 扩到 `.env` 家族 + `phpinfo` 家族（**含 `/docs/` 子目录变体**）；**目标站点从 1 个扩到 3 个** |
| **2026-11-15 14:37（第 3/5 次）** | 攻击源 5 个（🛡️ 3 / ❓ 1 / 📂 **File Inclusion** 1）；新增 `49.235.131.69`（File Inclusion，"AI自动封禁-Code Execution"，符合拉黑条件但已在黑名单）；黑名单1000：WAF 实际 **183** 个 / 本地备份 374（活跃 183、已删 191），新增 0、失败 0；白名单 **56** ±0 | ⚪ 单次量级 |
| **2026-11-15 20:37（第 5/5 次）** | 攻击源 3 个（🛡️ Threat Intelligence 2 / ❓ Unknown 1），**需拉黑 0**（全部 fast-skip 忽略）；黑名单1000：WAF 实际 **183** 个 / 本地备份 374（活跃 183、已删 191），本次新增 0、失败 0；白名单 **56** ±0 | ✅ **当日净增 5 个（178→183），与 5 次拉黑一一对应，增删一致、无同步故障** |

| **2026-11-16 08:37（第 1/5 次）** | 攻击源 **6** 个（🛡️ Threat Intelligence 4 + ❓ Unknown 2），需拉黑 0（全部 fast-skip）；黑名单 WAF 实际 **183** 个 / 本地备份 374（活跃 183、已删 191），新增 0、失败 0；白名单 **56** ±0 | ⚪ 威胁情报类占比高，全天首个窗口无新类型 |
| **2026-11-16 11:37（第 2/5 次）** | 攻击源 IP 数峰值 **12** 个；**Info Leak 3 个"需拉黑"，但 LLM 全部判定 `legit_business` 置信度 0.95**，分类 `rule_whitelist_fastpath`，理由"规则名/注释含白名单关键词（policy_rule44 / KKPREVIEW）"；目标 `idmo.pinnenger.com:16443/preview/okrsUrlPreview`，URL 参数为 **base64 编码的文件下载地址**（解出 `fileId` / `serviceId` / `userId` / `previewToken` / `.pdf` 文件名），**WAF 动作 = Deny**；涉及 `223.100.36.17`、`27.115.124.53`、`101.91.110.5` | ⚠️ **误拦（不是新攻击面）** —— 合法附件预览请求被规则 `policy_rule44` 拦下；LLM 已判正常业务，**WAF 却 Deny** |
| **2026-11-16 14:37（第 3/5 次）** | 攻击源 **3** 个；Info Leak 1 个"需拉黑" = **同一事件重复出现**（`223.100.36.17` / `okrsUrlPreview`，事件 ID `aa2b531dc4cf4e2ba3bef989f9582264`，最近一次 2026-11-16 10:52:44）；黑名单 183，新增 0、失败 0 | ⚠️ 同一误拦事件在后续窗口继续累计 |
| **2026-11-16 17:37（第 4/5 次）** | 攻击源 **5** 个；**新增攻击类型 `Deserialization`（1 个，"需确认"）** —— IP `103.85.20.74`，规则 **`m_php_unserialize`**，风险等级 Medium，**WAF 动作 = Allow（未拦截）**，站点 **品行者**，URL `https://pinnenger.com/`，5h 累计 1 次，事件 ID `1def96cfa2154920b6ad80cd7ca2803e`，最近一次 **2026-11-16 17:30:09** | 🔴 **库内首次出现该攻击类型** —— 且命中我方**主站**（此前记录的是 `ptm.pinnenger.com`）；**命中但放行** |
| **2026-11-16 20:37（第 5/5 次）** | 攻击源 **4** 个；`Deserialization` 仍为 1 个"需确认"（同一事件，未升级为拉黑）；需拉黑 **0** 个；黑名单1000：WAF 实际 **183** 个 / 本地备份 374（活跃 183、已删 191），**本次新增 0、失败 0**；白名单 **56** ±0 | ✅ **全天零新增拉黑**（对比 11-15 净增 5 个：178→183）→ **攻击强度回落**；⚠️ 但 **Deserialization 落"需确认"通道 → 未自动拉黑**（该攻击类型既不在 `ATTACK_TYPES_BLOCK` 也不在 `ATTACK_TYPES_IGNORE` 名单） |
| **2026-11-17 08:37（第 1/5 次）** | 攻击源 **3** 个（❓ Unknown 1 / **SQL Injection 1（需拉黑）** / 🛡️ Threat Intelligence 1）；**新拉黑 `221.228.152.36`（SQL Injection，1 次，AI 自动封禁）**；fast-skip：`180.163.29.79`（Unknown，可疑 ip 名单）、`219.143.126.181`（Threat Intelligence，黑名单4）；黑名单1000：WAF 实际 **183** 个 / 本地备份 375（活跃 **184**、已删 191），**本次新增 1、失败 0**；白名单 **56** ±0 | ✅ **全天唯一一次自动拉黑** —— 单次 SQL Injection，量级低、无组合利用 |
| **2026-11-17 11:37（第 2/5 次）** | 攻击源 **2** 个（❓ Unknown 2），需拉黑 0（全部 fast-skip）；黑名单 183，新增 0、失败 0；白名单 56 ±0 | ⚪ 静默 |
| **2026-11-17 14:37（第 3/5 次）** | 攻击源 **2** 个（❓ Unknown 2），需拉黑 0（全部 fast-skip）；黑名单 183，新增 0、失败 0；白名单 56 ±0 | ⚪ 静默 |
| **2026-11-17 17:37（第 4/5 次）** | 攻击源 **6** 个（🛡️ Threat Intelligence 4 / ❓ Unknown 2），需拉黑 0（全部 fast-skip）；黑名单 183，新增 0、失败 0；白名单 56 ±0 | ⚪ 威胁情报类占比高 |
| **2026-11-17 20:37（第 5/5 次）** | 攻击源 **5** 个（🛡️ Threat Intelligence 2 / ❓ Unknown 2 / **SSRF 1（需确认）**）；⭐ **库内首次出现 `SSRF` 攻击类型** —— IP `122.231.199.247`，规则 `skynet_rule65872`，风险等级 **Low**，**WAF 动作 = Deny（已拦截）**，站点 **品能者托管**，URL `https://www.pinnenger.com/favicon.ico`，5h 累计 1 次，事件 ID `0055794e55214cc8810ad9ccbb43845f`，最近一次 **2026-11-17 20:31:41**，Payload 仅 `file://`；未自动拉黑原因"**payload 含探测标记且仅单次命中**（v16.5）"；fast-skip：`180.163.29.79`、`39.170.78.110`（黑名单999）、`42.92.193.246`（WAF 威胁情报拦截）、`49.73.18.161`；黑名单1000：WAF 实际 **184** 个 / 本地备份 375（活跃 **184**、已删 191），**本次新增 0、失败 0**；白名单 **56** ±0 | 🔴 **新攻击类型首现 + 再次命中我方主站** —— ⚠️ **本次已 Deny 拦截**（与 11-15 / 11-16 两次 Allow 不同）；⚠️ **不构成"我方存在 SSRF 漏洞"的证据**（payload 无内网地址 / 无回连 / 单次）；⚠️ **`SSRF` 是否在 block / ignore 名单中报告未指明（待确认）**，不得套用 `Deserialization` 的"不在名单"结论 |

**新增信号（相对 2026-11-15 07:10 上期记录）**：

- 🔴🔴 **探测路径家族换挡：从 VCS 元数据（`.svn/` → `.git/config`）换到"凭据文件 + 诊断页"（`.env.backup` / `phpinfo.php` / `/docs/phpinfo.php`）**。**这一跳不是随机的** —— 本期外部披露的凭据收割型扫描器路径字典里，`.env`、`.git/config`、`phpinfo.php` **正好是同一份字典的三个条目**，我方 11-14 命中其中一个、11-15 命中另外两个。**详细分析见 [凭据收割型扫描器字典命中我方站点](credentialHarvestProbePaths-2026-11.md)。**
- 🔴 **目标主机从 1 个扩到 3 个**：11-14 只打 `182.140.209.35:18443`（兆瓦快链）；11-15 打到**兆瓦快链（同主机，连续第二天）+ 续费商城 `www.pingreenmall.com:3443`（43 次/5h）+ 品行者 `ptm.pinnenger.com`**。**"同一台机器连续两天被不同路径探" + "新增两个站点"同时出现 —— 攻击面在横向扩散。**
- ⚠️ **判定链出现缺口**：品行者那条 `/d/txt/test.txt` **WAF 动作是 Allow（未拦截）**，LLM 主模型与兜底模型**双双失败**，原文理由写明"**无法确认是新型攻击还是正常业务访问**"，却仍被 v15.4 兜底拉黑。**这同时暴露漏放行与误拉黑两侧的问题** —— 已单列进 [credentialHarvestProbePaths](credentialHarvestProbePaths-2026-11.md) 的观察项。
- ✅ **黑名单同步仍健康**：178 → 183，与当日 5 次拉黑一一对应，失败 0；本地备份 369 → 374（活跃 183、已删 191），**增删一致**。白名单 56 全天 ±0。
- ⚪ **威胁情报类全程 fast-skip**（11-15 三次巡检共 13+5+3 个源 IP 中，威胁情报占 8/3/2），既定策略无异常。
- 📎 **与外部情报的交叉印证**：[CISA 五部门联合警告](cisaRefrigerationColdChain-2026-11.md)（联网辅助设备是被点名的攻击面）与本期观察指向同一件事 —— **暴露面不在"主系统"上，而在"被顺手开了远程访问的辅助设备"上**；两期共同指向既有 P0 产物里的"联网资产与通信接口清单"基线。

**2026-11-16 全天新增信号（相对 2026-11-16 07:11 上期记录）**：

- 🔴 **攻击类型再次换挡，且这次命中的是我方主站**：11-15 是"凭据文件 + 诊断页"（路径字典探测），11-16 出现 **Deserialization（PHP 对象注入）** —— 库内从未记录过该类型。命中 `https://pinnenger.com/`（**品行者主站**，此前记录的是 `ptm.pinnenger.com` 子域），规则 `m_php_unserialize`，**WAF 动作 = Allow（未拦截）**。⚠️ **不得据此下"我方存在漏洞"结论**（载荷字段业务语义完整，更像应用自身序列化对象回传）—— 详见 [PHP 反序列化探测命中我方站点且未被拦截](phpDeserializationProbe-2026-11.md)。
- ⚠️ **处置链缺口已定位**：`Deserialization` **既不在 `ATTACK_TYPES_BLOCK` 也不在 `ATTACK_TYPES_IGNORE` 名单** → 命中即落"需确认"人工通道 → **未自动拉黑**（用户未回复）。这是**分类表缺项**，不是防护引擎失效。
- ⚠️ **漏放行与误拦两侧同时存在（连续第二天）**：11-15 品行者 `/d/txt/test.txt` Allow 未拦截；11-16 **同一站点**（品行者）主站反序列化 Allow 未拦截，**同时** `idmo.pinnenger.com:16443` 的合法附件预览请求被 `policy_rule44` **Deny**（LLM 判 `legit_business` 0.95）。→ **该站点的暴露面治理整体未闭环**，P0 自查范围必须新增 `pinnenger.com` 主站。
- ⚠️ **新增误拦事件**：11-16 11:37 与 14:37 两次巡检记录**同一事件**（事件 ID `aa2b531dc4cf4e2ba3bef989f9582264`）—— `idmo.pinnenger.com:16443/preview/okrsUrlPreview` 的 base64 文件下载参数触发 Info Leak 规则 `policy_rule44`，**WAF Deny 但 LLM 判正常业务**。库内既有产物 [remediation-exposureHygiene](../deliverables/remediation-exposureHygiene-20261112.md) 已记录该站点的 `policy_rule44` 快速通道误报，**本期再次复现**。
- ✅ **黑名单同步仍健康**：全天 **183 → 183，零新增、失败 0**，本地备份 374（活跃 183 / 已删 191）增删一致。白名单 56 全天 ±0。
- ⚪ **攻击强度回落但结构未变**：11-16 五次巡检攻击源 IP 数 **6 / 12 / 3 / 5 / 4**（峰值出现在 11:37），对比 11-15 净增 5 个拉黑 → **11-16 全天零新增**。⚠️ **零新增不等于威胁停止**，只是当日强度回落，且回落中首次出现新类型。

**新增信号（相对 2026-11-13 07:34 上期记录）**：

- 🔴 **11-14 出现全新探测路径 `/.git/config`，且是"同一路径 + 两个不同来源 IP + 同一目标主机"** —— 这是本期最硬的一条内部实证。攻击面含义有三点：
  1. **从 `.svn/` 扩展到 `.git/`**：11-12 观测到的是 `.svn/entries`（SVN 元数据），11-14 探测的是 `.git/config`（**Git 仓库配置文件**，泄露后含 remote 地址、凭据、分支信息）。**这是同族手法的升级，不是新家族** —— 说明扫描器在枚举"各种版本控制系统的元数据残留"。
  2. **目标主机仍是 `182.140.209.35:18443`（兆瓦快链）** —— 与 11-12 的 `.svn/entries` 探测**是同一台机器**。**同一台机器被不同 IP 用不同路径连续试探**，说明攻击者对该主机存在**预期**（或已被他人扫描后转售）。
  3. **两台机器/两段时间各 1 次**（05:40 与 16:35），单次量级仍是"试探"，**但路径收敛 + 主机重复，是"定向性上升"的前兆**。
  ⚠️ **对 P0 专项整改的直接含义**：既有自查范围是"全站 `.svn/` 残留与备份文件"，**必须扩到 `.git/`**（含 `.git/config`、`.git/HEAD`、`.git/refs/`、`.git/logs/`）。**只查 `.svn` 会漏掉本期实测被击中的这条路径。**
- ✅ **P0 项未闭环的证据又添一条**：11-12 的 Info Leak ×5 是备份文件探测，11-14 的 Info Leak ×2 是 Git 配置探测 —— **两日均为 Info Leak 类型**，且 11-14 的两次都被 LLM 判定为 `new_attack` / `scanner` / 置信度 0.97。**"加黑名单"没有阻止路径收敛**。
- ⚪ **11-13 全天零新增、11-14 净增 3 个** —— 整体仍是"单次攻击即自动封禁"的广撒网模式，**未观测到组合利用或定向攻击**。Code Injection 仅 1 次（`3.208.10.80`），量级低。
- ✅ **黑名单同步健康**：WAF 实际数 175 → 178，与当日三次拉黑一一对应，失败 0；本地备份 366 → 369，增删一致，**无同步故障**。
- ⚪ **白名单 56 个保持 ±0**，威胁情报类 IP 全程走 fast-skip 忽略 —— 既定策略，无异常。
- 📎 **与外部情报的交叉印证**：本期新增 [欧洲光伏 DER 暴露面](derExposureGermanyEurope-2026-11.md) 记录了**德国 BSI-CS 154 明确要求"建立联网资产与通信接口清单（含安装商/服务商设置的远程维护链路，含独立移动数据连接）"** —— 我方 WAF 实测到的 `.git/config` 探测，正是该清单要求所要防的那一类资产台账缺口。

**2026-11-17 全天新增信号（相对 2026-11-16 07:12 上期记录）**：

- 🔴 **库内首次出现 `SSRF` 攻击类型（仅 20:37 第 5/5 次巡检出现，前四次无）** —— `122.231.199.247` → `https://www.pinnenger.com/favicon.ico`，规则 `skynet_rule65872`，**WAF 动作 = Deny（已拦截）**，风险等级 Low，5h 累计 1 次，事件 ID `0055794e55214cc8810ad9ccbb43845f`，Payload 仅 `file://`。⚠️ **不得下"我方存在 SSRF 漏洞"结论** —— payload 无内网地址、无回连域名、单次量级，是**协议嗅探级探测**。⭐ **单独立档** → [SSRF 首现与主站连续三日被命中](wafSsrfProbeFirstAppearance-2026-11-17.md)。
- 🔴 **品行者主站连续第三天被不同类型命中**：11-15 `/d/txt/test.txt`（Info Leak，**Allow**）→ 11-16 反序列化（**Allow**）→ 11-17 SSRF（**Deny**）。⭐ **三天三类攻击、一条新路径、同一主机** → **暴露面治理仍未闭环**，P0 自查范围必须覆盖 `www.pinnenger.com` 主站（沿用上期待决项，**不新开产物**）。
- ⚠️ **未自动拉黑 ≠ 处置链缺口** —— 报告给出的原因是"**payload 含探测标记且仅单次命中（v16.5）**"（阈值行为），**报告未指明 `SSRF` 是否在 `ATTACK_TYPES_BLOCK` / `ATTACK_TYPES_IGNORE` 名单中** → **待确认**，**不得套用上期 `Deserialization` 的"不在名单"结论**（两者性质不同：一个是 Allow + 名单缺项，一个是 Deny + 单次未达阈值）。
- ⚪ **攻击强度明显回落**：全天攻击源 IP 数 **3 / 2 / 2 / 6 / 5**（对比 11-16 的 **6 / 12 / 3 / 5 / 4**）→ **11-16 的 12 个峰值消失，全天无一窗口超过 6**。全天仅 **3 个需处理条目**（1 个自动拉黑 + 1 个待确认），其余 **15 个全走 fast-skip 默认忽略**。⚠️ **但零新增不等于威胁停止** —— 回落中仍出现新类型（本期 SSRF），延续 11-16 已确立的规律。
- ✅ **黑名单同步健康**：**183 → 184**（+1 = `221.228.152.36` SQL Injection，08:37 AI 自动封禁）；本地备份 **375**（活跃 184 / 已删 191）**增删一致、失败 0**；白名单 **56** 全天 ±0。处置链无技术故障。
- ⚠️ **采集侧出现真实缺口**：`scripts/collect.py` 本期输出 `count: 1`，**仅提取到"攻击类型分布"聚合项（且只覆盖最后一次巡检的 fast-skip 部分），"待确认 IP 拦截报文"整节未进入采集输出** → **若只依赖采集脚本产出，本期 SSRF 情报会整个丢失**（11-16 的反序列化因人工直读报告才被发现）。⭐ **该节字段结构固定**（URL / 攻击类型+rule / 风险等级 / WAF 动作 / 站点 / 最近一次 / 5h 累计 / 事件 ID / Request / Payload）→ 建议补解析。⚠️ 属**内部工具改进**，不产对外产物。

**2026-11-18 全天新增信号（相对 2026-11-17 07:12 上期记录 · last_seen 2026-11-19 07:12）**：

- 🔴🔴 **库内首次取得"我方自有接口以 Base64 编码的远端 URL 为参数"的一手证据** —— `idmo.pinnenger.com:16443/preview/getCorsFile?urlPath=<base64>`（**5h 累计 4 次**，规则 `policy_rule44`，风险 Medium，**WAF 动作 = Deny**，LLM 判 `legit_business` 0.95，最近一次 **2026-11-18 19:18:24**，事件 ID `3af5d9b6f8e143a7b396ff2e54bb96b6`）；本地 Base64 解码后为 `https://idmo.pinnenger.com:16443/fileManager/kkfDownloadAnnex?fileId=…&serviceId=2&userId=49&previewToken=1795000983023.101899e…&fullfilename=….pdf`。⭐ 同站点第二个同构接口 `/preview/okrsUrlPreview?url=<base64>`（**5h 1 次**，事件 ID `81df4b218fa84a799b1b9b2f3a7ca9f6`，解码为**相对路径**版本）。⭐⭐ **与 11-17 首现的 `SSRF` 类型构成直接串联** —— SSRF 这一攻击类型在我方的"**外部攻击形态**"与"**内部入口同构**"两侧第一次都有了证据。⚠️ **样本中的目标 URL 全部指向我方自身主机，无任何外部目标/内网地址/元数据端点；我方无源站响应码观测数据 → 不得下"我方存在 SSRF 漏洞"结论**（正确表述：**存在同构接口，需代码审计确认目标地址是否受限**）。⭐ **单独立档** → [我方 `/preview/getCorsFile` 接口的 Base64 URL 参数面](wafCorsFilePreviewUrlParamSurface-2026-11-18.md)。
- ⚠️ **同一站点、同一规则、同一接口族的第三次复现（11-16 → 11-18）** —— 11-16 已记 `idmo.pinnenger.com:16443/preview/okrsUrlPreview` 的 base64 下载参数触发 `policy_rule44` 被 Deny 而 LLM 判正常业务（事件 ID `aa2b531dc4cf4e2ba3bef989f9582264`），本期同形态再次复现。⭐ **既有产物 [remediation-exposureHygiene](../deliverables/remediation-exposureHygiene-20261112.md) 记录的"`policy_rule44` 快速通道误报"已连续两期复现 → 不是偶发**。⚠️ **误拦是功能影响，不是安全成效**：两条均被 Deny 且均被判"疑似正常业务"（0.95）→ 附件在线预览在 11-18 至少被拦下一次。
- ⚠️ **判定口径的结构性问题被这两条暴露** —— 两条 LLM 判定的 category 均为 **`rule_whitelist_fastpath`**，理由是"规则名/注释含白名单关键词（policy_rule44 / KKPREVIEW）" → **判定器根本没分析载荷内容**，只看规则名 → **这类条目的"0.95 置信度"不应被当作真实安全评估结果**。⭐ 与库内 11-15 记录的"LLM 主模型与兜底模型双双失败仍被兜底拉黑"属同一类问题。
- ⚠️ **附件下载令牌明文置于 GET 查询串** —— `previewToken` 结构为 `<毫秒时间戳>.<128-bit 十六进制>`（两样本前段 `1795000983023` / `1794993254498` 相差 7.7 秒，后段为秘密）→ **必然进入 WAF/网关/CDN/代理访问日志、浏览器历史、Referer、工单与监控**。⚠️ **是暴露面事实，不是"已泄露"**；⚠️ **不得下"令牌可预测"结论**（后段为 128-bit 随机/哈希）。
- ⚠️ **端口维度需与域名同级维护** —— `idmo.pinnenger.com:16443` 与库内已记的 `182.140.209.35:18443`（兆瓦快链）、`www.pingreenmall.com:3443`（续费商城）构成**我方至少 3 个非标端口对外站点**；非标端口本身不是问题，但**按"标准端口"假设写 WAF 规则与监控配置极易漏掉**。
- ✅ **黑名单同步健康且含一次人工决策** —— **184 → 188（+4）**：3 个 AI 自动封禁（`111.229.99.161` Code Injection / `218.244.143.162` Code Injection / `43.199.209.53` Info Leak）+ **1 个"用户手动确认拉黑"（`112.227.129.82`，攻击类型"未记录"）**；本地备份 **375 → 379**（活跃 188 / 已删 191）**增删一致、失败 0**；白名单 **56** 全天 ±0。⭐ **库内首次记录到人工介入决策的证据**（此前全是自动化）→ 建议自本期起**把"手动拉黑/放行/白名单"单独记一条**（既是流程有效性证据，也是训练数据）。
- ⚪ **攻击强度与结构** —— 最近 7 小时窗口（6h 巡检 + 1h overlapping）攻击源 IP **9** 个（Threat Intelligence 6 / **Info Leak 2** / Unknown 1）；7 个 fast-skip 全部为默认忽略类型（**不是我方漏防**）。⚠️ **"9"是 7 小时窗口口径，不是全天五次合计**，**不得与 11-17 的全天序列 "3/2/2/6/5" 直接并列比较**。⭐ 同网段 `180.163.29.206` / `.217` / `180.163.30.27` 三 IP 判定结果不一致（两个忽略、一个判正常业务）→ **仅作观察项，不作结论**。
- 📈 **采集脚本较上期改善但未闭环** —— `scripts/collect.py` 本期输出 `count: 3`（11-17 为 `count: 1`），**"待确认 IP 拦截报文"节已部分覆盖**（两条完整条目 + 类型分布聚合）。⚠️ **但 Payload 原文 / 规则 ID / 事件 ID / WAF 动作 / 5h 累计次数仍未进入采集输出** → **关键取证字段仍需直读报告原件**；**不得写成"已修复"**（库内 11-18 挂的该待决项状态：**部分改善**）。

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

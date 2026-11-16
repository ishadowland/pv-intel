# PHP 反序列化（对象注入）探测命中我方站点且未被拦截 — 2026-11-16

> 🔴 强约束（我方一手观测命中 · 攻击类型为库内首次出现）· 事件时间 2026-11-16 17:30:09 · 采集 2026-11-17 07:11
> 核心标识：WAF 规则 `m_php_unserialize` 命中品行者 `https://pinnenger.com/` · **WAF 动作 = Allow（未拦截）** · 载荷为标准 PHP 序列化对象 `O:4:"User":33:{...}` · 事件 ID `1def96cfa2154920b6ad80cd7ca2803e` · 状态"需确认"→ **未自动拉黑** · 与 11-16 日报已记的「我方 PHP 依赖清单未回填」直接对上

---

## 一、信源核实

| 项 | 值 |
|---|---|
| 来源请求 | `CISA advisories November 17 2026 industrial control systems new`（web_search，用于核查当日 CISA 是否发布新 ICS 通告）<br>`PHP 反序列化 对象注入 攻击 请求 payload O:4:"User" 云原生 网站 被探测`（web_search，用于取反序列化机理与入口类型的独立第三方信源） |
| 原始 URL（主 1 · 我方一手） | 内部 SafeLine WAF 巡检报告 `waf-inspection-2026-11-16-173748.md` / `waf-inspection-2026-11-16-203732.md`（归档于 `~/.openclaw/workspace/waf-inspection-reports/`），最新一份经软链 `waf-inspection-report-latest.md` 取得 |
| 原始 URL（主 2 · 机理分析） | https://security.unboundcompute.com/php-object-injection （UnboundCompute《PHP Object Injection: When unserialize() Builds the Attacker's Objects》，Deep Dives 专栏） |
| 原始 URL（辅 1 · 背景对照） | https://www.cisa.gov/news-events/ics-advisories/icsa-26-316-01 （CISA ICSA-26-316-01，PHP2Shell / Node2Shell 通告，库内既有文档 [icsa26316SiemensNode2Shell-2026-11](icsa26316SiemensNode2Shell-2026-11.md) 已归档） |
| 发布主体 | SafeLine WAF（我方自有防护系统，内部一手观测）· UnboundCompute（第三方安全研究）· CISA / Siemens ProductCERT（背景对照） |
| 发布/更新时间 | 攻击事件 **2026-11-16 17:30:09**（WAF 最近一次命中时间）· WAF 巡检 2026-11-16 17:37:48 与 20:37:32 两次均记录同一事件 · 第三方机理分析快照抓取 2026-11-17 07:12:36 |
| 采集时间 | 2026-11-17 07:12（内部报告同步在 07:11 采集完成） |
| 快照 | `raw/snapshots/security/php-object-injection-unserialize-analysis.md` · `raw/snapshots/security/cisa-ics-advisories-index-2026-11-17.md` |

**信源清单（安全域要求 ≥2 个独立信源）**

| # | 信源 | 类型 | 独立性 |
|---|---|---|---|
| 1 | **SafeLine WAF 巡检报告 2026-11-16 17:37 / 20:37（我方一手观测）** | 内部一手证据（含事件 ID、规则 ID、精确时间戳、目标主机、原始 Request 报文、Payload 原文） | 我方自有系统 |
| 2 | UnboundCompute：PHP Object Injection 机理与入口分析 | 外部第三方研究 | 独立于我方 WAF |
| 3 | CISA ICSA-26-316-01（PHP2Shell，PHP 释放后重用） | 外部官方通告 | 独立 |

> ✅ **满足安全域双信源要求**：内部一手观测（1）+ 外部机理分析（2）+ 外部官方通告背景（3）。

> 📎 **入库理由**：库内安全域已记"凭据收割扫描器路径字典"（`.env` / `.git/config` / `phpinfo.php`）、"批量备份文件扫描"（`.svn/` / `.zip` / `.sql`）、"PTM 后端异常处理"（`m_response`），**但从未出现"反序列化 / 对象注入"这一攻击类型**。本期我方站点首次被该类型规则命中，且**未被拦截**——这是一个新的、尚未被现有防线覆盖的探测面。

---

## 二、事实核查

| 数据点 | 原文表述 | 核查方式 | 结论 | 备注 |
|---|---|---|---|---|
| **命中站点与 URL** | 巡检报告："**URL（完整）**: `https://pinnenger.com/`"；"**站点**: 品行者" | 报告原文逐字 | ✅ 已核 | ⚠️ 是**品行者主站**，不是此前记录的 `ptm.pinnenger.com`（PTM 现货交易平台）——**新增一个暴露面** |
| **攻击类型与规则** | "**攻击类型**: Deserialization (rule: `m_php_unserialize`)" | 报告原文 + 规则 ID | ✅ 已核 | ✅ **库内首次出现该攻击类型**；规则是 PHP 专用反序列化检测规则 |
| **WAF 动作** | "**WAF 动作**: Allow" | 报告原文逐字 | ✅ **已核 · 本条最关键一行** | ⚠️ **命中但放行**。与 11-15 品行者 `/d/txt/test.txt`（同样 Allow）构成**连续第二天"命中未拦截"**，且这次命中的是**代码执行风险最高的一类** |
| 风险等级 | "**风险等级**: Medium" | 报告原文 | ✅ 已核 | ⚠️ WAF 自评 Medium；**这与该攻击类型的理论上限（PHP 对象注入通常可达 RCE）不匹配** —— 见第 5 段我方判断 |
| 命中次数 | "**5h 累计**: 1 次"；巡检统计 "Deserialization \| 1 个 \| ❓ 需确认" | 报告原文 + 统计表 | ✅ 已核 | 仅 1 次，且落在 17:30 一次窗口内 |
| 事件 ID / 时间 | "事件 ID: `1def96cfa2154920b6ad80cd7ca2803e`"；"**最近一次**: 2026-11-16 17:30:09" | 报告原文逐字 | ✅ 已核 | ✅ 有唯一事件 ID 可回溯，可与其他巡检交叉 |
| **载荷形态** | Payload：`O:4:\"User\":33:{s:2:\"id\";i:1622096778;s:6:\"fromId\";s:5:\"anony\";s:6:\"snsId\";i:0;s:8:\"nickname\";s:16:\"游客1622096778\";s:6:\"gender\";i:0;s:8:\"avatar\";s:23:\"/login/image/anony2.png\";...s:4:\"role\";i:0;...}` | 报告原文逐字核对 | ✅ **已核 · 是标准 PHP 序列化对象** | ⚠️ **两个可能读法，不能二选一**：① 攻击者构造的对象注入载荷；② 我方应用自身的匿名用户对象被序列化后回传。**字段高度结构化且业务语义完整**（游客/匿名/头像路径/角色/粉丝数），更像 ②；但**规则命中说明服务端存在对用户可控数据调用 `unserialize()` 的入口**，这正是 ① 的前置条件 |
| **为何未自动拉黑** | 巡检脚本说明："这些 IP 不自动拉黑，原因有两类：1. 攻击类型**不在 `ATTACK_TYPES_BLOCK` 和 `ATTACK_TYPES_IGNORE` 列表里**（v13 未明确分类）；2. 攻击类型在拉黑列表里，但**窗口内命中次数低于该类型的最小拉黑次数**（v16.4，如单次 Scanner）" | 巡检报告"待确认 IP 拦截报文"说明段原文 | ✅ **已核（读报告说明，非独立佐证）** | ⚠️ **规则命中 ≠ 攻击定性**：`Deserialization` 当前**不在** block 名单，也不在 ignore 名单 → 落进"需确认"人工通道。**处置结论：未拉黑（人工未回复）** |
| 同日同站点的另两类命中 | 11:37 巡检：Info Leak 3 个"需拉黑"，LLM 判定 `legit_business` 置信度 **0.95**，分类 `rule_whitelist_fastpath`，理由"规则名/注释含白名单关键词（policy_rule44 / KKPREVIEW）"，目标 `idmo.pinnenger.com:16443/preview/okrsUrlPreview`（URL 参数为 base64 编码的文件下载地址，含 `fileId`、`serviceId`、`userId`、`previewToken`），**WAF 动作 = Deny**；14:37 巡检再次命中同一事件 | 三份 11-16 巡检报告逐份比对 | ✅ 已核 | ⚠️ **这是误报治理问题，不是新攻击面** —— 库内 [remediation-exposureHygiene-20261112](../deliverables/remediation-exposureHygiene-20261112.md) 已记录 `idmo.pinnenger.com:16443` 的 `policy_rule44` 快速通道误报 |
| 11-16 全天攻击面体量 | 5 次巡检攻击源 IP 数：**6 / 12 / 3 / 5 / 4**；黑名单 WAF 实际 **183 个**（本地备份 374 = 活跃 183 + 已删 191），**今日新增 0 个、失败 0 个**；白名单 **56** 个 **±0** | 5 份巡检报告的统计段 | ✅ 已核 | ⚠️ **对比 11-15：净增 5 个（Info Leak ×4 + File Inclusion ×1）、黑名单 178→183** → **11-16 全天零新增**，攻击强度回落；但**新类型（Deserialization）在回落中首次出现** |
| **当日 CISA 是否发布新 ICS 通告** | CISA 通告索引页快照："Nov 12, 2026 ICSA-26-316-05 / -04 / -03 / -02 / -01"为最新五条，"Showing 1 to 10 of 4234 results" | CISA 官方索引页快照逐行 | ✅ **已核：11-12 之后无新通告** | ✅ 这条**否定性结论**同样重要：本期安全域**没有新 CVE 可收**，故只更新既有 Siemens 文档（补官方原文），不新建 CVE 文档 |

> **核查小结**：本条**没有发现数字冲突**（与 11-15 的凭据收割条目不同，本次各数据点在报告内自洽）。**必须写明的两个边界**：① **"命中 `m_php_unserialize` 规则"不等于"我方存在反序列化漏洞"** —— 载荷语义更像应用自身的匿名用户对象，我方无源站响应码与代码观测，**不能下"漏洞已存在"的结论**，只能下"**我方站点存在反序列化特征流量且未被拦截**"；② **WAF 动作 Allow 的原因已定位**（该攻击类型既不在 block 名单也不在 ignore 名单 → 落人工通道），这是**处置链缺口**，不是防护引擎失效。

---

## 三、原文归档（快照）

| 快照 | SHA256 | 抓取时间 | 大小 |
|---|---|---|---|
| `raw/snapshots/security/php-object-injection-unserialize-analysis.md` | `5ac0e167d4c5f8327117822fc5f5380aadc17937d36a8633714f570ae6563020` | 2026-11-17 07:12:36 | 8,319 字符 |
| `raw/snapshots/security/cisa-ics-advisories-index-2026-11-17.md` | `82b022cdd20ea2ee9b0f51178786593cf8b9867006b1e0358dbb0167a1770238` | 2026-11-17 07:10:41 | 2,210 字符 |

**关键原文摘录（我方 WAF 巡检报告 2026-11-16 17:37 / 20:37，逐字）**：

> **`103.85.20.74`** (Deserialization, 1 次)
> - **URL（完整）**: `https://pinnenger.com/`
> - **攻击类型**: Deserialization (rule: `m_php_unserialize`)
> - **风险等级**: Medium
> - **WAF 动作**: Allow
> - **站点**: 品行者
> - **最近一次**: 2026-11-16 17:30:09
> - **5h 累计**: 1 次
> - **事件 ID**: `1def96cfa2154920b6ad80cd7ca2803e`
>
> ```http
> GET / HTTP/1.1
> Host: pinnenger.com
> ```
> ```
> O:4:\"User\":33:{s:2:\"id\";i:1622096778;s:6:\"fromId\";s:5:\"anony\";s:6:\"snsId\";i:0;s:8:\"nickname\";s:16:\"游客1622096778\";s:6:\"gender\";i:0;s:8:\"avatar\";s:23:\"/login/image/anony2.png\";s:5:\"space\";s:0:\"\";s:6:\"email\";s:0:\"\";s:6:\"mobile\";s:0:\"\";s:8:\"realName\";s:0:\"\";s:6:\"location\";s:0:\"\";s:5:\"brief\";s:0:\"\";s:9:\"signature\";s:0:\"\";s:10:\"createTime\";s:0:\"\";s:4:\"fans\";i:0;s:7:\"follows\";i:0;s:8:\"articles\";i:0;s:4:\"role\";i:0;...
> ```

**关键原文摘录（UnboundCompute 第三方机理分析，快照逐字）**：

> PHP object injection happens the moment an application calls `unserialize()` on data an attacker can shape. […] They choose which classes get built and what values the properties hold, and the methods PHP runs on its own do the rest.
>
> `__wakeup()` runs the instant an object is rebuilt by `unserialize()`. `__destruct()` runs when the object is thrown away at the end of the request. `__toString()` runs when the object is used where a string is expected […]
>
> If an attacker can make `unserialize()` build a Logger with `logfile` set to `shell.php` and `data` set to a small block of PHP, then the end of the request writes a working web shell to disk. No call to `eval`, no call to `system`, just a file write that the author never meant to expose to user input.
>
> Because the gadgets live in libraries and framework code, the same chain often works across many apps that share a dependency.
>
> The sink is always `unserialize()`, but the source hides in ordinary places: Session or preference data kept in a cookie and deserialized on each request. A hidden field in a form that the server round trips through `unserialize()`. An API that accepts a serialized blob because an older client sent one. […] A second path needs no visible `unserialize()` call at all. The `phar://` stream wrapper triggers deserialization of archive metadata when a filesystem function touches an attacker path.

---

## 四、概要提取

- **攻击类型换挡**：库内首次出现 **Deserialization（PHP 对象注入）** 探测，此前是 Info Leak / File Inclusion / 凭据收割字典三类
- **命中我方主站**：`https://pinnenger.com/`（品行者主站）—— 此前记录的是 `ptm.pinnenger.com`（PTM 平台），**暴露面又扩一个主机**
- **命中未拦截**：WAF 规则 `m_php_unserialize` 命中，但 **WAF 动作 = Allow**；且该攻击类型**既不在 block 名单也不在 ignore 名单**，落进"需确认"人工通道 → **未自动拉黑**
- **载荷是标准 PHP 序列化对象** `O:4:"User":33:{...}`，字段业务语义完整（匿名用户 / 游客昵称 / 头像路径 / 角色 / 粉丝数），**更像应用自身序列化对象回传**，不能直接定性为攻击载荷
- **机理明确**：反序列化漏洞的成立条件是"服务端对用户可控数据调用 `unserialize()`"—— **规则命中即说明这个入口存在**，只是尚不能证明已被利用
- **同期误报并存**：同日 `idmo.pinnenger.com:16443` 的 `policy_rule44` 快速通道把带 `previewToken` 的附件预览请求判成 Info Leak（LLM `legit_business` 0.95、WAF 却 **Deny**）—— 漏放行与误拦两侧同时存在
- **当日体量回落**：11-16 五次巡检攻击源 IP 数 6/12/3/5/4，**黑名单全天零新增**（仍 183），白名单 56 **±0**；对比 11-15 净增 5 个
- **当日无新 CVE**：CISA 通告索引最新仍是 **11-12 的 ICSA-26-316-01~-05**，11-12 之后无新 ICS 通告

---

## 五、主要观点

**原文主张**

- CISA（ICSA-26-316-01 背景）：PHP2Shell（CVE-2026-109618 v3.1 9.8 / CVE-2026-109619 v3.1 8.1）属 PHP 释放后重用类缺陷，"Apache mod_php 在默认设置下可经 HTTP 利用"
- UnboundCompute：*"PHP object injection happens the moment an application calls `unserialize()` on data an attacker can shape."*；*"They never type a line of code. They choose which classes get built and what values the properties hold, and the methods PHP runs on its own do the rest."*
- UnboundCompute（POP 链）：*"They ship a data structure that tells objects you already trust to call each other in an order you never intended."*；*"Because the gadgets live in libraries and framework code, the same chain often works across many apps that share a dependency."*
- UnboundCompute（修复）：*"Do not call `unserialize()` on anything a user can influence. This is the rule that closes the bug."*
- 我方 WAF 巡检报告（事实陈述，非观点）：Deserialization 类型不在 block / ignore 名单 → 未自动拉黑，WAF 动作 Allow

**我方判断**

- ✅ **这条的真正价值是"攻击面换挡"，不是"又一个漏洞"**：11-15 之前我方面对的是**信息泄露与凭据收割**（探测文件是否存在），11-16 出现的是**代码执行前置条件类**（探测是否存在可利用的反序列化入口）。二者对应的防线完全不同 —— 前者靠路径禁则，后者只能靠**代码侧审计（找 `unserialize()` 入口）**。**任何路径禁则都拦不住这条**。
- ✅ **必须克制不要写成"我方存在反序列化漏洞"**：载荷字段（`nickname`=游客+数字、`avatar`=/login/image/anony2.png、`fromId`=anony、`fans`/`follows`/`articles` 计数）**高度业务化且自洽**，最可能的解释是我方应用把匿名用户对象序列化后回传。**我方没有源站响应码、没有代码观测、没有第二台设备的对照**——按库内纪律（与 11-15 那条"不得下已泄露结论"同一条），这里只能下"**我方站点出现反序列化特征流量且未被拦截**"。
- ✅ **但这条暴露了两个确定缺口，且都不需要等漏洞结论就能修**：
  1. **处置链缺口**：`Deserialization` 不在任何名单里 → 命中即落人工通道。**这是分类表缺项**，不是引擎失效。**把"反序列化/对象注入"补进 `ATTACK_TYPES_BLOCK` 是本周就能做完的动作**（命中即拦截 + 拉黑），是否误报由后续白名单机制兜。
  2. **代码审计缺口**：只要我方 PHP 代码里存在对用户可控数据（Cookie / 表单隐藏域 / API body / 缓存 / 上传文件）的 `unserialize()` 调用，就具备被利用条件。**UnboundCompute 的原文还给了两条库内尚未覆盖的入口类型**：`phar://` 流包装器（**上传文件路径**触发归档元数据反序列化）、以及"**共用同一依赖的应用之间 POP 链可移植**"——后者对多站点架构（兆瓦快链 / 品行者 / 续费商城 / PTM）**是一条系统性风险**。
- ✅ **这条与 11-16 日报已记的待办直接合流**：库里已列「**我方 Brotli / PHP 依赖清单**未回填」。本条把该项从"依赖版本基线"升级为"**攻击侧已观测到该类型流量**"——**优先级应上调**：不只是要知道 PHP 版本，还要知道**哪些接口把序列化数据喂给了 `unserialize()`**。两件事可以合并成一次代码审计。
- ✅ **"Allow + 未拉黑"必须与 11-15 的同站 Allow 并读**：连续两天、同一站点（品行者）、两类完全不同的攻击、**一次没拦一次没拉黑**——这指向的不是单条规则的偶然，而是**该站点的暴露面治理整体未闭环**。库内 [remediation-exposureHygiene-20261112](../deliverables/remediation-exposureHygiene-20261112.md) 的 P0 自查范围**必须再加一条：`pinnenger.com` 主站**（此前只查了 `ptm.pinnenger.com`、`idmo.pinnenger.com`、兆瓦快链）。
- ⚠️ **不要把 11-16 的"黑名单零新增"写成"攻击停止"**：全天零新增只说明当日强度回落，**且回落中首次出现新类型** —— 恰恰是需要升级分类表的时候。
- ⚠️ **误报治理与暴露面整改要分开记账**：同日 `idmo.pinnenger.com:16443` 的 `policy_rule44` 快速通道把合法附件预览请求 **Deny** 掉（LLM 判 `legit_business` 0.95），这是**误拦**、属规则白名单问题；它与 `pinnenger.com` 主站的**漏放行**是两类问题，**不要混成一条"防护不严"的结论**（一个是规则太宽、一个是规则误伤）。

---

## 六、参考意义

> 📌 **本阶段口径（2026-11-12 起）**：转评审只看 **网络安全 / 信创 / 等保 / 隐私保护 / 护网** 五方向，**暂不精到具体产品**；产品线级关联一律标 🟡 **待复核**。

| 方向（五方向） | 可证事实 | 本阶段处理 |
|---|---|---|
| **网络安全** | ① 我方一手观测：主站 `pinnenger.com` 命中 `m_php_unserialize`，**WAF 动作 Allow**，事件 ID 可回溯；② 该攻击类型**不在 block / ignore 名单** → 命中即落人工通道；③ 机理侧：反序列化成立条件是"服务端 `unserialize()` 用户可控数据"，规则命中即说明该入口存在；④ UnboundCompute 给出库内未覆盖的两个入口类型（`phar://` 上传路径、**共用依赖的 POP 链跨应用可移植**） | ✅ **进评审（方向级）** —— 并入 [exposureHygiene](../deliverables/remediation-exposureHygiene-20261112.md)（P0 自查范围新增 `pinnenger.com` 主站 + **代码侧 `unserialize()` 入口审计**）与 [攻击手法→防线覆盖度对照](../deliverables/remediation-defenseTacticCoverage-20261112.md)（新增 T1190 / 对象注入手法行，标注"路径禁则不适用"）；**不新开产物** |
| **护网 / 攻防准备** | 反序列化 / POP 链 / `phar://` 三类手法与触发点；MITRE 映射 T1190（利用面向公网的应用） | ✅ **进方向级对照表**（手法 × 防线覆盖度），并作为**护网演练场景**候选（对自建 PHP 站点做一次反序列化入口自查） |
| **等保** | 反序列化属常见的应用层高危缺陷类别，对应等保 2.0 应用安全"输入校验 / 剩余信息保护"要求 | 🟡 **待复核** —— 方向级基线可引用，但需产品材料支撑具体条款落点，**本阶段不落产品改造** |
| **信创 / 隐私保护** | 本期无新增可证事实 | — |

**暴露面判定（按评审第 1 关三问）**

| 对象 | 在我方暴露面？ | 依据 |
|---|---|---|
| `pinnenger.com`（品行者主站） | ✅ **是** | 我方自有站点，WAF 有完整请求级观测（事件 ID / 规则 ID / 报文 / Payload） |
| `unserialize()` 入口是否存在可利用缺陷 | ⚠️ **待核实** | 规则命中只证明"存在反序列化入口被调用"，**不能证明入口可被外部数据操控**；我方无代码审计与源站响应码观测 |
| `ptm.pinnenger.com` / `idmo.pinnenger.com` / 兆瓦快链 / 续费商城 | ❓ **未逐站观测** | 11-16 巡检未在这几站命中该类型，**不等于不存在**（巡检是抽样窗口，非全量） |
| 多站点共用依赖的 POP 链可移植性 | ⚠️ **待核实** | 机理上成立，但我方依赖清单未回填，**无证据支撑我方是否共用同一 PHP 依赖** |

**产品线级关联（🟡 待复核 · 按本阶段口径不落产）**

| 影响产品线 | 影响点 | 是否需改行为 |
|---|---|---|
| SafeLine WAF（防护侧） | 攻击类型分类表补 `Deserialization`（block 名单）；确认 `m_php_unserialize` 规则在 PHP 站点默认开启 | 🟡 **需改**（处置链补位） |
| 全部对外 PHP 站点 | 代码侧 `unserialize()` 入口审计（Cookie / 隐藏域 / API body / 缓存 / 上传文件 `phar://`） | 🟡 **需改**（基线自查 + 与依赖清单合并） |
| 品行者主站（`pinnenger.com`） | 暴露面自查纳入 P0 范围（此前只覆盖 `ptm.` / `idmo.` 子域） | 🟡 **需改**（范围扩充） |
| 护网演练场景 | 反序列化 / POP 链 / `phar://` 三类手法纳入对照与演练 | 🟡 需改 |
| PTM 现货交易平台 / 兆瓦快链 / 续费商城 | 本期无直接落点 | ⚪ 暂不改 |

---

## 七、总结输出

**一句话结论**：我方品行者主站 `pinnenger.com` 首次被 **PHP 反序列化（对象注入）** 类型规则命中，**WAF 动作 = Allow 且该攻击类型不在任何名单内因而未自动拉黑** —— 载荷字段高度业务化、**不能据此认定我方存在漏洞**，但**规则命中即证明"服务端对用户可控数据调用 `unserialize()`"这一前置条件成立**；本条的落点不是"修漏洞"，而是**补齐攻击类型分类表（处置链缺口）+ 把 `pinnenger.com` 主站与"代码侧 `unserialize()` 入口审计（含 `phar://` 与共用依赖 POP 链跨应用可移植）"并入既有 P0 暴露面自查**，并与已挂起的「我方 PHP 依赖清单」合并为一次代码审计。

**落地去向**

- [ ] **专项整改** —— 🟡 **方向级待复核**：并入既有 [remediation-exposureHygiene-20261112](../deliverables/remediation-exposureHygiene-20261112.md)（P0 自查范围新增 `pinnenger.com` 主站 + **`unserialize()` 入口审计**）与 [remediation-defenseTacticCoverage-20261112](../deliverables/remediation-defenseTacticCoverage-20261112.md)（新增 T1190 / 对象注入手法行，标注"路径禁则不适用"）；**不新开产物**
- [ ] **产品特性** —— 🟡 **待复核**：WAF 攻击类型分类表新增 `Deserialization` 类别（命中即拦截 + 拉黑候选），使"反序列化"不再落人工通道
- [ ] **需求变更** —— 🟡 **待复核**：对外 PHP 站点的**上线准入项**增加"不得对用户可控数据调用 `unserialize()`"，并覆盖 `phar://` 流包装器路径
- [ ] **跟踪项** —— ① 我方 PHP 依赖清单与 `unserialize()` 调用点清单（合并上一次待办）；② 多站点是否共用同一 PHP 依赖（POP 链可移植性）；③ `103.85.20.74` 的后续行为与是否需人工拉黑；④ CISA 是否就 Node2Shell/PHP2Shell 发布面向 PHP 站点的通用指引

---

## 参考链接

- [CISA ICSA-26-316-01：Siemens Building Automation and Energy Products（PHP2Shell 背景）](https://www.cisa.gov/news-events/ics-advisories/icsa-26-316-01)
- [CISA ICS Advisories 索引（2026-11-17 快照：最新通告仍为 11-12）](https://www.cisa.gov/news-events/ics-advisories)
- [UnboundCompute：PHP Object Injection: When unserialize() Builds the Attacker's Objects](https://security.unboundcompute.com/php-object-injection)
- [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/kev)
- [同族文档：CISA ICSA-26-316-01~-05 Siemens Node2Shell/PHP2Shell（通用库版本基线与时滞模型）](icsa26316SiemensNode2Shell-2026-11.md)
- [同族文档：凭据收割型扫描器路径字典命中我方站点（2026-11-15）](credentialHarvestProbePaths-2026-11.md)
- [既有产物：对外站点暴露面专项自查（专项整改 · P0）](../deliverables/remediation-exposureHygiene-20261112.md)

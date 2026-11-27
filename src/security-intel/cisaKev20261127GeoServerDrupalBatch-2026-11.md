# CISA KEV 2026-11-27 批次三条（GeoServer 两条 + Drupal Core 一条）—— 库内首次执行官方 feed 快照 diff

> 🔴 强约束（对我方资产台账的流程约束，非「我方受影响」）· 采集于 2026-11-28 · 核心标识：**⭐⭐⭐ 库内首次真正执行「官方 feed 快照 diff」** —— 库内 11-27 日报基于 KEV 基线篇明确给出「**KEV 采集必须从『按批次跟』改为『按官方 feed 快照 diff』**」这条唯一能改变采集管线的动作，**本期是这条动作的第一次落地**：直接抓 CISA 官方 JSON feed，得 `catalogVersion 2026.11.27` / `dateReleased 2026-11-27T18:03:12Z` / `count 1808`，与库内 11-27 记录的 `2026.11.25 / 1805` 逐条 diff → **净增 3 条，一日不漏**；⭐⭐⭐ **库内首条「修复版本发布 39 天后才进 KEV」的量化** —— GeoServer 修复版 **3.0.2 / 2.28.6 / 2.27.7 的发布通知日期是 10-19**，而 CISA 收录日是 **11-27**，**间隔 39 天**；⭐⭐⭐ **库内首条「同一修复版本对不同版本线的覆盖不一致」的硬证据** —— **CVE-2026-129245（Critical）在 3.0.2 的发布通知里被列出，但在 2.28.6 与 2.27.7 的通知里完全没提** → **「升级到 2.28.6 就修好了」是错的**；⭐⭐⭐ **库内首条「17 个 CVE 的月度发布只被 KEV 收录 2 个」** —— 10 月发布共 **17 个 CVE（1 Critical + 12 High + 4 Medium）**，**仅 2 个在 KEV 目录上** → **KEV 覆盖率 2/17 = 11.8%**；⭐⭐⭐ **库内首条「NVD/CVE 尚无记录 → 扫描器与工单规则可能匹配不到」** —— CVE Program 记录服务对全部 5 个编号答「记录不存在」，NVD 对两条返回无结果，**而 CISA 条目里却链接了 NVD 页面**；⭐⭐ **库内首条「EOL 版本线的官方措辞是『仅作为缓解措施』」** —— 2.27 线 EOL，官方要求「apply this update as a mitigation measure only」；⭐⭐ **库内首条「取证分诊字段在本批次全为 No」** —— 两条 GeoServer 条目的 `Forensic triage required = No`；⭐⭐ **库内首条「披露—利用—收录三段时序」**：8 月初 Rapid7 报告 → 9 月下旬 Eye Security 报告 → 10-19 发布修复 → **11-25 15:27 UTC watchTowr 观测到利用尝试（SecurityWeek 报道）→ 11-27 18:03 UTC CISA 收录**。

---

## 一、信源核实

| 项 | 值 |
|---|---|
| 来源请求 | `CISA ICSA advisory November 27 2026`（web_search）<br>`CISA KEV catalog 2026-11-27 GeoServer`（web_search，命中第三方逐条追踪站） |
| 原始 URL（主源 1 · **官方一手 feed**） | https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json （CISA 官方 KEV 目录 JSON feed，**抓取时 `catalogVersion = 2026.11.27`、`dateReleased = 2026-11-27T18:03:12.5733Z`、`count = 1808`**，原始字节 1,903,958，快照正文截断至 1,000,018 字符，SHA256 `05be4bfcfd70004c57756f02231e308e4273cd0c0ae513695c91bf45de483b3d`） |
| 原始 URL（主源 2 · 第三方逐条分析） | https://www.pk-sharma.com/briefing/cisa-lists-two-geoserver-flaws-as-exploited-due-30-november-project-says-october-updates-fix-them （独立分析简报，**发布 2026-11-27 20:24:41**，含 39 天间隔推导、五条链式 CVE、17 个 CVE 评级统计、版本线覆盖差异与 11 节点时间线，快照正文 23,211 字符） |
| 原始 URL（辅源 · 周度交叉核对） | https://threatpodium.com/threat-intelligence-report-2026-11-27 （第三方周报，**发布 2026-11-27 03:21:09**，含当周 KEV 增量、勒索受害者数与厂商集中度，快照正文 14,197 字符） |
| 原始 URL（辅源 2 · 逐条 CVE 描述） | https://www.pbcsnyc.com/post/daily-cybersecurity-briefing-november-27-2026 （每日安全简报，**发布 2026-11-27 12:36:51**，含 Mitel 五条、Juniper、Xen Orchestra、Danfoss 三条与 AutomationDirect 的逐条描述，快照正文 17,358 字符） |
| 原始 URL（辅源 3 · 官方公告列表页） | https://www.cisa.gov/news-events/cybersecurity-advisories （CISA 官方 Alerts 列表页，用于确认官方公告节奏，快照正文 2,834 字符） |
| 发布主体 | CISA（主源 1 · 官方）；独立分析简报站（主源 2）；第三方威胁情报周报（辅源 1）；每日安全简报（辅源 2） |
| 发布/更新时间 | 官方 feed `dateReleased = 2026-11-27T18:03:12.5733Z`；主源 2 **2026-11-27 20:24:41**；辅源 1 **2026-11-27 03:21:09**；辅源 2 **2026-11-27 12:36:51** |
| 采集时间 | 2026-11-28 07:12:08 – 07:12:39（feed 于 07:12:39 以 `--max-chars 1000000` 重抓，SHA256 与字节内容一致） |

---

## 二、事实核查

| # | 数据点 | 原文表述 | 核查方式 | 结论 | 备注 |
|---|---|---|---|---|---|
| 1 | **官方 feed 目录版本与总数** | feed 头部：`"catalogVersion": "2026.11.27"`、`"dateReleased": "2026-11-27T18:03:12.5733Z"`、`"count": 1808`、`"vulnerabilities"` 数组长度 **1808** | 直接解析 feed 全部条目 | ✅ **已核（1808）** | ⭐⭐⭐ **库内首条「官方 feed diff 的可执行样本」** |
| 2 | **与库内基线的 diff** | 库内 11-27 基线篇记 `catalogVersion 2026.11.25` / `count 1805`；11-26 无新增（`dateAdded` 最大值仍为 11-25） | 与库内已记录基线逐项比对 + 解析 feed 中 `dateAdded = 2026-11-27` 的条目 | ✅ **已核（净增 3 条）** | ⭐⭐⭐ **库内 11-27 提出的「feed 快照 diff」动作本期首次落地**；**diff 结果：11-27 新增 3 条 = GeoServer ×2 + Drupal Core ×1** |
| 3 | 11-27 新增条目编号 | feed 中 `dateAdded = 2026-11-27` 的条目：**CVE-2026-120705**（OSGeo / GeoServer / XML Injection）、**CVE-2026-129243**（OSGeo / GeoServer / Incorrect Authorization）、**CVE-2026-136716**（Drupal / Core / Improper Check for Unusual or Exceptional Conditions） | 解析 feed | ✅ **已核（3 条）** | ⭐⭐⭐ **Drupal Core CVE-2026-136716 是本批次第三条，且此前库内完全未记录**（库内 11-24 记过 11-24 批次含 Drupal Core CVE-2026-132165 RCE，**是不同编号**） |
| 4 | 联邦期限 | 三条 `dueDate` 均为 **2026-11-30** | 解析 feed | ✅ **已核（11-30）** | ⭐⭐ **距采集日 11-28 仅 2 天，且 11-29、11-30 两天中 11-29 为周六、11-30 为周日**（主源 2 明确指出：「30 November is 3 calendar days after 27 November, and two of those three days, 28 and 29 November, are a Saturday and a Sunday」）→ **实际可执行工作日只有 11-27、11-28 两天** |
| 5 | 取证分诊与勒索字段 | feed `knownRansomwareCampaignUse` 三条均为 **"Unknown"**；主源 2 记两条 GeoServer 条目的 forensic triage 值为 **"No"** | 解析 feed + 主源 2 比对 | ✅ **已核** | ⭐⭐ **库内首条「11-27 批次全条 No / Unknown」**（与库内 11-26 批次混有 No 与必需形成对照） |
| 6 | CVE-2026-120705 技术描述 | 主源 2：「CVE-2026-120705 is an **XML injection flaw in a WFS stored query**. CISA says it lets a **remote attacker with no login** make the server **read local text files that the GeoServer process can access**, or **fetch HTTP or HTTPS addresses the attacker chooses**」 | 直读主源 2 | ✅ **已核** | ⭐⭐⭐ **库内首条「WFS 存储查询 XML 注入 = 免认证本地文件读 + 任意 URL 拉取」的组合** → **形态上同时具备 SSRF 与信息泄露**；**与库内 11-17/11-18 已记的 SSRF 形态同族** |
| 7 | CVE-2026-129243 技术描述 | 主源 2：「CVE-2026-129243 is an **incorrect authorisation flaw**. CISA says it lets a **remote attacker with no login** get past **service level role checks** and call operations that only those checks protect」 | 直读主源 2 | ✅ **已核** | ⭐⭐ **库内首条「服务级别角色校验绕过」**（不同于库内 11-15 记的认证绕过） |
| 8 | 链式利用 | 主源 2：「Each CISA description ends by saying the flaw can be **chained with four other named CVEs**『to achieve unauthenticated remote code execution』on an affected instance. **That is a statement of what the combination can do. Neither entry says that anyone has been seen doing it.**」 | 直读主源 2 | ✅ **已核** | ⭐⭐⭐ **库内首条「五 CVE 链式 RCE」的官方定性**；⚠️ **官方明确否认有人被观测到实施该链** |
| 9 | 链中另三个编号 | 主源 2：「the other steps were given numbers of their own」→ **CVE-2026-129242、CVE-2026-129244、CVE-2026-129245**；五者「All five are listed as fixed in 3.0.2, 2.28.6 and 2.27.7 by their own advisories」 | 直读主源 2 | ✅ **已核（5 个编号）** | ⭐⭐⭐ **库内首条「五 CVE 链」的完整编号集**；⚠️ **「listed as fixed by their own advisories」与 #10 的版本线差异并存** |
| 10 | **同一修复版本对不同版本线覆盖不一致** | 主源 2：「**One difference to check before closing a ticket.** The 3.0.2 notice lists all 17 October CVEs. The 2.28.6 and 2.27.7 notices list 16: each **leaves out CVE-2026-129245, the Critical one**, and neither mentions its number anywhere on the page. The project's post puts all three releases above one list that includes it, and its advisory says it is patched in all three. **This site does not resolve the difference. If you need written proof for the 2.28 or 2.27 line, ask the project.**」 | 直读主源 2 | ⚠️ **版本线覆盖差异，未解决** | ⭐⭐⭐ **库内首条「Critical 漏洞在维护版本线通知中缺席」的硬证据** → **整改单不得写「升级到 2.28.6 即可全闭」**；⚠️ **主源 2 自己也未解决** |
| 11 | 10 月发布共 17 个 CVE 及评级分布 | 主源 2：「Counting the distinct CVE numbers under its October releases heading… gives **17 CVEs: 1 Critical, 12 High and 4 Medium**（all derived from the page）. So **13 of 17 are rated Critical or High**. **2 of the 17 are on the CISA catalogue as read**」 | 直读主源 2 + 算术核对：1+12+4 = 17 ✅；2/17 = **11.8%** | ✅ **已核（自洽）** | ⭐⭐⭐ **库内首条「KEV 覆盖率」的量化样本**：**17 个已修复且高危的 CVE 中只有 2 个进了 KEV** → **「没进 KEV」绝不能当作「安全」**（与库内 11-27 基线篇的「17% 是 2 年以上旧 CVE」形成互补） |
| 12 | 修复版本发布时间与收录时间差 | 主源 2：「The GeoServer project's release notices for the fixed versions, **3.0.2, 2.28.6 and 2.27.7, are dated 19 October**. That is **39 days** before the listing（derived: 19 October to 27 November）」；「The project's CVE post and the advisories for the two flaws are dated **23 November**, 4 calendar days before it」 | 直读主源 2 + 算术核对（10-19 → 11-27 = 39 天 ✅；11-23 → 11-27 = 4 天 ✅） | ✅ **已核（39 天 / 4 天）** | ⭐⭐⭐ **库内首条「修复发布到 KEV 收录的间隔」量化** |
| 13 | 39 天**不能**证明什么 | 主源 2：「**What the 39 days do not establish.** They do not show when exploitation began, or that any server was attacked during that time. The catalogue prints the date a flaw was added, **not the date of an attack**. Nor do they show that the CVE numbers or technical detail were public for 39 days. The release notices carry CVE numbers as read now but **print no edit date**」 | 直读主源 2 | ✅ **已核** | ⭐⭐⭐ **库内首条「第三方主动写出「39 天不等于利用了 39 天」的免责段」** → **我方引用该数字时必须同段引用这条免责** |
| 14 | EOL 版本线的官方措辞 | 主源 2：「**The 2.27 line is at end of life.** The 2.27.7 notice says so and asks users to『**apply this update as a mitigation measure only**』and to plan a move to a stable or maintenance release. The project's post names **3.0.x as the current stable line** and **2.28.x as the current maintenance line**」 | 直读主源 2 | ✅ **已核（逐字）** | ⭐⭐⭐ **库内首条「EOL 线的更新被官方降级为『仅作缓解措施』」** → 与库内 11-27 基线篇的「EOL ≠ 不可利用」形成闭环：**EOL 线上的用户被明确告知「打了这个补丁也还是只是缓解」** |
| 15 | **CVE/NVD 记录尚不存在** | 主源 2：「**No public CVE record yet, as read.** At about 20:13 UTC the **CVE Program's record service answered that the record did not exist for all five numbers**. At about 20:14 UTC **NVD returned no result for CVE-2026-120705 or CVE-2026-129243**, although CISA's notes link to NVD pages for both. This site's inference: **a scanner or ticket rule that matches only on those records may have nothing to match yet. Check the installed GeoServer version directly.**」 | 直读主源 2 | ✅ **已核（第三方实测）** | ⭐⭐⭐ **库内首条「KEV 收录早于公开 CVE 记录」的实证** → **库内 11-24 记的「SCA/SBOM 对运行时层漏洞失效」在「记录尚未生成」这一维度上再次成立** → **我方若以 NVD/SCA 为唯一输入源，这两条会直接漏掉** |
| 16 | 利用尝试的观测方与时点 | 主源 2 时间线：「**25 November, 15:27 UTC** SecurityWeek reports **exploitation attempts seen by watchTowr** — SecurityWeek page data」；「Who is speaking… **SecurityWeek is a secondary source**, used here for what it says the security firm watchTowr observed」 | 直读主源 2 | ✅ **已核（二手源转述 watchTowr 观测）** | ⭐⭐ **库内首条「KEV 收录前 2 天已有第三方观测到利用尝试」**；⚠️ **主源 2 自己标注了这是二手源** |
| 17 | 漏洞报告时间线 | 主源 2 时间线：「**Early August** A **Rapid7** researcher reports findings to GeoServer developers — SecurityWeek only」；「**Late September** The firm **Eye Security** reports findings to the vendor — SecurityWeek only」；「**19 October** Date on the release notices」 | 直读主源 2 | ✅ **已核（二手源级）** | ⭐⭐⭐ **库内首条「从首次报告到修复 2.5 个月、从修复到 KEV 收录 39 天的完整时序」**；⚠️ 两段均为 SecurityWeek 单一来源 |
| 18 | 辅源交叉核对 | 辅源 2（PBCS 日报）：列出 11-25 批次 Mitel 五条、Juniper Session Smart、Xen Orchestra、Danfoss 三条、AutomationDirect C-More EA9（CVE-2026-127280, 7.8） | 与库内 11-26 已记录的 11-25 批次十条逐一比对 | ✅ **已核（与库内记录一致）** | 辅源 2 另记 Drupal CVE-2026-136716 的利用细节与修复版本 10.6.23 / 11.3.23 / 11.4.14（**其原文本页快照已取得**） |
| 19 | 辅源 1 周报口径 | 辅源 1：「**7 New KEVs** · 299 Victims」「New KEVs: 7 ▲ +2 vs last week」「**Danfoss products show the strongest concentration of risk signals this week**」 | 与 feed 实际 diff 比对 | ⚠️ **与官方 feed 不一致** | ⭐⭐⭐ **库内首条「第三方周报『7 New KEVs』与官方 diff 的 3 条不符」** → 再次印证库内 11-27 基线篇的结论：**第三方统计口径与官方 feed 不可混用**，**我方的 feed diff 才是准数** |
| 20 | 我方是否使用 GeoServer / Drupal | 库内全部文档检索：**无任何 GeoServer 或 Drupal 的使用记录**（库内 EPICS、Siemens、Schneider、Mitigate、Danfoss、CIRCUTOR 等均为 OT 侧） | 库内全量检索 | ⚠️ **无我方使用证据** | ⚠️ **不得下「我方受影响」结论**；⚠️ **但 Drupal 与 GeoServer 都是通用开源组件，「库内无记录」≠「我方未部署」** → **须自查** |

> **核查小结**：本期新增事实 **20 条可核**，其中 **14 条为官方 feed 解析或第三方原文直读**、**4 条为算术自洽核对**（#1 #2 #11 #12）、**1 条为库内跨文档比对**（#18）、**1 条为第三方与官方口径冲突标注**（#19）。**六条必须写明的边界**：① **我方无 GeoServer / Drupal 使用证据，不得下「我方受影响」结论，但「库内无记录」不等于「未部署」，须自查**；② **39 天是「修复发布 → KEV 收录」的间隔，不是利用起始时间**（主源 2 明确写了这条免责，引用时必须同段引用）；③ **CVE-2026-129245（Critical）在 2.28.6 / 2.27.7 通知中缺席，主源 2 自己也未解决** → **整改单不得写「升级到 2.28.6 即全闭」**；④ **17 个 CVE 中只有 2 个进了 KEV（11.8%）** → **「未进 KEV」不等于安全**；⑤ **第三方周报「7 New KEVs」与官方 diff 的 3 条不符**；⑥ **11-30 到期，11-29 为周六、11-30 为周日，实际可执行窗口仅 11-27、11-28 两天**。

---

## 三、原文归档（快照）

| 快照文件 | SHA256 | 抓取时间 | 字符数 | HTTP |
|---|---|---|---|---|
| `raw/snapshots/security/cisa-kev-feed-20261127.md` | `05be4bfcfd70004c57756f02231e308e4273cd0c0ae513695c91bf45de483b3d` | 2026-11-28 07:12:08（07:12:39 以 `--max-chars 1000000` 重抓，SHA256 与字节内容一致） | 60,018 → **1,000,018（已截断）** | 200 |
| `raw/snapshots/security/geoserver-kev-20261127-pksharma.md` | `4fb2e60a9eb474c6a3381549271d19de6131de986c395e588e28f00a13a4df05` | 2026-11-28 07:12:08 | 23,211 | 200 |
| `raw/snapshots/security/threatpodium-kev-week-20261127.md` | `9ef1f236a853bd68693a828b5231138b0a744eceb707923508f4ddaeb7782d6f` | 2026-11-28 07:12:28 | 14,197 | 200 |
| `raw/snapshots/security/pbcs-daily-briefing-20261127.md` | `ac36b6517c1dc3693fcbdd57eebbf7bce59cf2514b0f0eca3ff117c1ddd00587` | 2026-11-28 07:12:26 | 17,358 | 200 |
| `raw/snapshots/security/cisa-advisories-index-20261128.md` | `925fe67aca759aec023861e20b66004f727aa4098db357dce82eec51757acaf0` | 2026-11-28 07:12:25 | 2,834 | 200 |

**关键原文摘录**

> **CISA 官方 KEV feed（主源 1）**（`cisa-kev-feed-20261127.md`，头部逐字）：
> > ```
> > "title": "CISA Catalog of Known Exploited Vulnerabilities",
> > "catalogVersion": "2026.11.27",
> > "dateReleased": "2026-11-27T18:03:12.5733Z",
> > "count": 1808,
> > ```
>
> > 解析 `dateAdded = 2026-11-27` 的三条（逐字字段）：
> > ```
> > CVE-2026-120705 | OSGeo | GeoServer | OSGeo GeoServer XML Injection Vulnerability        | due 2026-11-30 | ransomware: Unknown
> > CVE-2026-129243 | OSGeo | GeoServer | OSGeo GeoServer Incorrect Authorization Vulnerability | due 2026-11-30 | ransomware: Unknown
> > CVE-2026-136716 | Drupal | Core    | Drupal Core Improper Check for Unusual or Exceptional Conditions Vulnerability | due 2026-11-30 | ransomware: Unknown
> > ```

> **独立分析简报（主源 2）**（`geoserver-kev-20261127-pksharma.md`）：
> > 「On Friday 27 November 2026 CISA added two flaws in GeoServer…: **CVE-2026-120705 and CVE-2026-129243, both due Monday 30 November.** The GeoServer project's release notices for the fixed versions, **3.0.2, 2.28.6 and 2.27.7, are dated 19 October. That is 39 days before the listing**（derived: 19 October to 27 November）. The project's CVE post and the advisories for the two flaws are dated **23 November**, 4 calendar days before it.」
> > 「**What the 39 days do not establish.** They do not show when exploitation began, or that any server was attacked during that time. The catalogue prints the date a flaw was added, **not the date of an attack**.」
> > 「**One difference to check before closing a ticket.** The 3.0.2 notice lists all 17 October CVEs. The 2.28.6 and 2.27.7 notices list 16: each **leaves out CVE-2026-129245, the Critical one**, and neither mentions its number anywhere on the page.」
> > 「**The 2.27 line is at end of life.** The 2.27.7 notice says so and asks users to『**apply this update as a mitigation measure only**』…」
> > 「**No public CVE record yet, as read.** At about 20:13 UTC the **CVE Program's record service answered that the record did not exist for all five numbers**. At about 20:14 UTC **NVD returned no result** for CVE-2026-120705 or CVE-2026-129243, although CISA's notes link to NVD pages for both. This site's inference: **a scanner or ticket rule that matches only on those records may have nothing to match yet. Check the installed GeoServer version directly.**」
> > 「gives **17 CVEs: 1 Critical, 12 High and 4 Medium**… So **13 of 17 are rated Critical or High. 2 of the 17 are on the CISA catalogue** as read」
> > 时间线：「Early August A **Rapid7** researcher reports findings…｜Late September The firm **Eye Security** reports findings…｜**19 October** Date on the release notices…｜**25 November, 15:27 UTC** SecurityWeek reports **exploitation attempts seen by watchTowr**｜**27 November, 18:03 UTC** CISA catalogue version released with both flaws added that day｜**30 November** Due date for both entries」

---

## 四、概要提取

- ⭐⭐⭐ **库内首次执行「官方 feed 快照 diff」**：抓官方 JSON feed → `catalogVersion 2026.11.27` / `dateReleased 2026-11-27T18:03:12Z` / `count 1808`，与库内 11-27 基线（`2026.11.25` / `1805`）逐条 diff → **净增 3 条**，**库内 11-27 提出的「KEV 采集改为按官方 feed 快照 diff」这条唯一管线动作今日落地**。
- ⭐⭐⭐ **11-27 新增三条**：**CVE-2026-120705**（GeoServer XML 注入，WFS 存储查询，**免认证**读本地文本文件 / **拉取任意 HTTP(S) 地址**）、**CVE-2026-129243**（GeoServer **服务级别角色校验绕过**，免认证）、**CVE-2026-136716**（Drupal Core 异常条件检查不当）；**三条期限均为 11-30**（11-29 为周六、11-30 为周日 → 实际窗口仅 2 天）。
- ⭐⭐⭐ **库内首条「修复发布 → KEV 收录 39 天」**：GeoServer 3.0.2 / 2.28.6 / 2.27.7 发布通知 **10-19** → 收录 **11-27**；**并须同段引用「39 天不证明利用了 39 天」的免责**。
- ⭐⭐⭐ **库内首条「同一修复版本对不同版本线覆盖不一致」**：**CVE-2026-129245（Critical）在 2.28.6 / 2.27.7 的通知中完全缺席**，只有 3.0.2 列出 → **整改单不得写「升级到 2.28.6 即全闭」**。
- ⭐⭐⭐ **库内首条「KEV 覆盖率」样本**：10 月发布共 **17 个 CVE（1 Critical + 12 High + 4 Medium）**，**仅 2 个在 KEV 目录上（11.8%）** → **「未进 KEV」不等于安全**。
- ⭐⭐⭐ **库内首条「KEV 收录早于公开 CVE 记录」**：CVE Program 记录服务对 5 个编号全答「记录不存在」，NVD 对两条无结果，**而 CISA 条目却链接 NVD 页面** → **仅以 NVD/SCA 为输入源的管线会直接漏掉这两条**。
- ⭐⭐ **库内首条「EOL 线的更新被官方降级」**：2.27 线 EOL，官方要求「apply this update **as a mitigation measure only**」；当前稳定线 3.0.x、维护线 2.28.x → 与库内 11-27 基线篇的「EOL ≠ 不可利用」形成闭环。
- ⭐⭐ **库内首条「五 CVE 链 + 取证分诊全 No」**：链中另三个编号 **CVE-2026-129242 / 129244 / 129245**；官方表述为「**can** be chained … to achieve unauthenticated remote code execution」，**并明确否认有人被观测到实施该链**；三条的取证分诊值均为 **No**、勒索标记均为 **Unknown**。
- ⭐⭐ **完整时序入库**：8 月初 Rapid7 报告 → 9 月下旬 Eye Security 报告 → 10-19 发布修复 → **11-25 15:27 UTC watchTowr 观测到利用尝试（SecurityWeek 二手转述）** → 11-27 18:03 UTC CISA 收录 → 11-30 到期。
- ⭐ **第三方周报与官方口径再次冲突**：辅源 1 称「7 New KEVs」，官方 diff 为 **3 条** → **第三方统计不可与我方 feed diff 混用**。

---

## 五、主要观点

**原文主张**

- CISA 官方 feed：`catalogVersion 2026.11.27`、`dateReleased 2026-11-27T18:03:12.5733Z`、`count 1808`；三条新增条目的必填处置字段均为「Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA's BOD 26-04…」「Stakeholders are responsible for evaluating each asset's internet exposure」。
- 独立分析简报（主源 2）：「**2 of the 17 are on the CISA catalogue** as read」；「**No public CVE record yet, as read.**…a scanner or ticket rule that matches only on those records may have nothing to match yet. **Check the installed GeoServer version directly.**」；「**This site does not resolve the difference. If you need written proof for the 2.28 or 2.27 line, ask the project.**」
- 辅源 2（PBCS）：Drupal Core CVE-2026-136716 属**主动攻击**，「Attackers exploiting a new critical flaw in Drupal Core, **bypassing installer state checks for complete site control via the public install.php endpoint**」，处置为「Deploy latest Drupal patches (10.6.23, 11.3.23, 11.4.14), **remove public installer access**, and meticulously review logs for admin account misuse」。
- 辅源 1（周报）：「New KEVs: 7 ▲ +2 vs last week」「Ransomware Victims: 299 ▼ -64 vs last week」「**Danfoss products show the strongest concentration of risk signals this week.**」

**我方判断**

- ⭐⭐⭐ **本期最大的价值不在三条新条目，而在「库内 11-27 提的那条唯一管线动作，今天第一次被执行了，而且证明它是可执行的」。** 库内 11-27 日报写得很清楚：「**KEV 采集必须从『按批次跟』改为『按官方 feed 快照 diff』**（一个月 37 条分散在 10 天，任何只在某一天读目录的人都会漏）」。**今天我们抓了官方 feed、做了 diff、拿到了确切的 +3 条（1805 → 1808），并逐条核了编号、期限、厂商、产品、漏洞名、勒索字段 —— 全部一致。** **这条动作从今天起应当固化为每日例行**：每日存一份 feed 快照（含 SHA256）+ 与前一日做 diff + 只把 diff 出来的条目写进域文档。**其价值是确定的：库内 11-27 已用 11 月逐日分布证明「一个月 37 条分散在 10 天」，靠「按批次跟」必然漏；而 feed diff 是全量比对，不漏。** **而且今天这一跑还额外暴露了一件事：第三方周报说「7 New KEVs」，官方 diff 只有 3 条 —— 差 4 条。这说明第三方统计的「新增」里混了别的东西（很可能是 11-25 那批的补记或口径差）。我方若用第三方，会连「今天到底新增几条」都答不对。**
- ⭐⭐⭐ **「17 个 CVE 只进 2 个 KEV」这个数字，是本期最应该写进库内固定纪律的一条 —— 它和库内 11-27 基线篇的「17% 是 2 年以上旧 CVE」构成一个完整闭环。** 库内 11-27 已经知道「进 KEV 的条目里有一批是很老的 CVE」（说明利用不挑新旧）；**今天补上了另一半：「同一个月发布的 17 个已修复 CVE 里，只有 2 个被确认在野利用」（说明大部分高危 CVE 并不会被利用）。** **合起来是一句对我方资产台账非常有用的话：「进 KEV = 确实在被利用（高置信度）；没进 KEV = 大概率没在被利用，但绝不是安全（覆盖率仅 11.8%）。」** **库内 11-19 记的「老未修漏洞仍在被利用」不是危言耸听，库内 11-27 记的「未入 KEV ≠ 产品级安全标签」也不是。两条合起来的正确用法是：KEV 是优先级排序器，不是安全判据。** **台账里「是否在 KEV 出现」这个字段必须是「优先级信号」而不是「安全状态」，且必须与「是否 EOL」「最后一次安全更新」「版本是否在受影响区间」三个字段并列。**
- ⭐⭐⭐ **「KEV 收录早于公开 CVE 记录」这件事，是今天 feed diff 跑出来的意外收获，也是对我方现有安全工具链最实际的一条警示。** 主源 2 实测：CVE Program 记录服务对 5 个编号全部回答「记录不存在」，NVD 对两条返回无结果，**而 CISA 的条目里却链接了 NVD 页面**。**这意味着：如果我方的资产台账、SCA 扫描、或漏洞工单规则是按 NVD/CVE 记录匹配的，那么这 5 个 CVE 在我方侧就是「不存在的」** —— **KEV 收录本身，反而成了这批漏洞唯一的可检索入口。** **这与库内 11-19 记的 Java4Shell「SCA/SBOM 对运行时层漏洞完全失效」是同一类结构性盲区，但成因不同：那次是「运行时不在清单里」，这次是「记录还没生成」。** **建议台账的漏洞来源清单里明确写入：「CISA KEV 官方 feed」为独立于 NVD 的第二来源**，并且**保留库内 11-27 已定的「按 feed diff 而非按批次跟」管线** —— 这两件事必须一起做，只做一件都会漏。
- ⭐⭐⭐ **「Critical 漏洞在维护版本线通知中缺席」是本期最锋利的一条 —— 它直接推翻了整改单上最常见的一句话。** 库内 11-26 已经就 Danfoss 立过「**版本基线矩阵**」的规矩（<3.3 / 3.3~4.1 / <4.3.1 / ≤5.4.0 / 全版本五段，每段可闭的 CVE 集合不同）。**今天这个原则拿到了一个更狠的案例：同一家厂商、同一个修复版本号（2.28.6）、同一个 10 月发布批次（17 个 CVE），其中那个 Critical 的 CVE 在这条版本线的通知里根本没有出现。** **也就是说：一个只写「升级到 2.28.6」的整改单，在纸面上覆盖 16/17 个 CVE，实际可能一个 Critical 都没闭。** **整改单必须写成「产品 × 版本线 × CVE 集合」三元组，并且对每一个版本线单独列出可闭集合** —— 这正是库内 11-26 已定的口径，**今天从一个「版本线内差异」的案例得到了强化**。⚠️ **同时必须照记：主源 2 自己也未解决这个差异**，并明确说「If you need written proof for the 2.28 or 2.27 line, ask the project」→ **我方不得自行裁定哪个版本线覆盖了 129245**。
- ⭐⭐ **「39 天」这个数字必须连同它的免责一起入库 —— 否则我方会犯一个很典型的错。** 很容易写成「GeoServer 漏洞被利用了 39 天」，**这是错的**：39 天是「修复版本发布 → KEV 收录」的间隔，而 KEV 收录日 ≠ 利用起始日。**主源 2 专门写了一段「What the 39 days do not establish」来拆这个误读** —— 这段话本身值得抄进我方库内的引用纪律。**正确表述：「10-19 发布修复，11-27 进 KEV，间隔 39 天；CISA 目录记录的是收录日，不是攻击日。」**
- ⭐⭐ **「GeoServer 的 WFS 存储查询 XML 注入 = 免认证读本地文件 + 拉取任意 URL」这条形态，我方必须认真看一眼，虽然我方没有 GeoServer 部署记录。** **理由不是「我方可能有 GeoServer」，而是「这个形态我方太熟了」**：库内 11-17 首次出现 SSRF（命中我方主站，已 Deny）、11-18 记我方 `/preview/getCorsFile` 的 Base64 URL 参数面、11-19 记 libumqtt 的 SSRF 进 KEV。**「免认证 + 任意 URL 拉取 + 服务端代读」是库内反复出现的攻击形态。** **并且 —— 这条恰好演示了为什么「没进 KEV ≠ 安全」不能当作免责**：如果我方资产里真有一个 GeoServer，它正是这种形态。**因此这条对我方的意义不是「快修」，而是「把这个形态加进自查清单」**：凡我方对外提供的、接受用户提供的 URL 并代为拉取的服务（在线预览、文件下载、报表导出、回调地址），都应按「免认证 + 任意 URL + 服务端代读」三要素自查。**
- ⭐⭐ **「EOL 线上的更新被官方明确降级为『仅作缓解措施』」，这条把库内 11-27 的「EOL ≠ 不可利用」从统计口径升级为官方措辞。** 库内 11-27 基线篇说「17% 的近 12 个月新增条目是 2 年以上旧 CVE」→ 库内因此判定「EOL 不等于不可利用」。**今天官方自己给出了对应的处置措辞**：2.27 线的用户被要求「apply this update **as a mitigation measure only**」并「plan a move to a stable or maintenance release」。**即：官方承认「打这个补丁」只是止血，不是修复。** **这对我方台账的直接含义是：EOL 资产的「最后一次安全更新」这个字段不能记为「已修补」，必须记为「已缓解（官方定位为 mitigation only）」+「是否已迁移至受支持版本线」两列。**
- ⭐ **「Drupal Core CVE-2026-136716」的处置建议里有一句，我方可以直接搬到自己的暴露面自查上：「remove public installer access」。** 辅源 2 明确写该漏洞「**bypassing installer state checks for complete site control via the public install.php endpoint**」→ **即「公开的安装器端点 = 一次安装即可接管整站」。** **这条的迁移价值不限于 Drupal**：库内 11-16 记的凭据收割字典（`.env` / `.git/config` / `phpinfo.php`）本质也是「公开的运维端点」这一类。**建议把「生产环境是否存在任何一次性/管理性端点（安装器、调试页、样例应用、备份控制台、phpinfo、探活面板）」列为暴露面自查的固定一条** —— **成本极低，且与库内已有的攻击路径族直接相关。**
- ⭐ **三条的取证分诊字段全为 No，必须写进判断纪律。** 库内 11-26 刚记了「KEV 条目按官方取证分诊字段逐条分级」，**今天这批三条全部是 No** → **意味着官方不要求做取证分析**。**我方台账与整改单在引用这三条时，不得自行升级为「需取证排查」**，但**也不得因为 No 就省掉版本自查** —— 尤其考虑到 #15（NVD 尚无记录）与 #10（版本线覆盖差异），**恰恰是官方不要求取证的这批，最需要我方自己核版本**。
- ⭐ **我方无 GeoServer / Drupal 使用证据，这条必须照记为「须自查」而不是「无关」。** 库内全量检索无任何 GeoServer 或 Drupal 记录，**但这两个都是通用开源组件** —— **「库内无记录」不等于「我方未部署」，尤其 Drupal 这类常见 CMS。** ⚠️ **不得下「我方受影响」结论；也不得因为「我方没有这个产品」就跳过自查。**

---

## 六、参考意义

| 方向（网络安全/信创/等保/隐私保护/护网） | 可证事实 | 本阶段处理 |
|---|---|---|
| 网络安全（漏洞管理管线） | 官方 feed 可直抓（`2026.11.27` / `count 1808`），本期 diff 得净增 3 条；库内 11-27 提出的「按 feed 快照 diff」今日首次落地并验证可执行 | ✅ **进评审**（方向级）。落点：**KEV 采集固化为「每日存 feed 快照 + 与前一日 diff + 只写 diff 出的条目」**；**diff 结果与第三方周报「7 New KEVs」不符（官方 3 条）→ 第三方统计不得作为入库依据**。**不新开产物** |
| 网络安全（资产台账字段） | 10 月发布 17 个 CVE 仅 2 个进 KEV（11.8%）；三条取证分诊全为 No、勒索全为 Unknown；EOL 线官方措辞为「mitigation measure only」 | ✅ **进评审**（方向级）。落点：台账「是否在 KEV 出现」字段**改标为优先级信号而非安全状态**，并与「是否 EOL / 最后一次安全更新 / 是否已迁移受支持版本线 / 版本是否在受影响区间」四列并列；**EOL 资产的「已修补」必须改记为「已缓解（mitigation only）」**。**不新开产物** |
| 网络安全（漏洞来源清单） | CVE Program 记录服务对 5 个编号答「记录不存在」，NVD 对两条无结果，而 CISA 条目却链接 NVD 页面 | ✅ **进评审**（方向级）。落点：**台账漏洞来源清单增列「CISA KEV 官方 feed」为独立于 NVD 的第二来源**；**仅以 NVD/SCA 为输入源的管线会漏**（与库内 11-19 Java4Shell「运行时层盲区」并列）。**不新开产物** |
| 网络安全（整改单粒度） | CVE-2026-129245（Critical）在 2.28.6 / 2.27.7 通知中缺席，仅 3.0.2 列出 | ✅ **进评审**（方向级）。落点：**整改单写成「产品 × 版本线 × CVE 集合」三元组**，每个版本线单列可闭集合（与库内 11-26 Danfoss 版本基线矩阵同口径，本期提供版本线内差异的实证）；**不得写「升级到 2.28.6 即全闭」**。**不新开产物** |
| 网络安全（暴露面自查条目） | Drupal 处置建议「remove public installer access」；GeoServer 形态为「免认证 + 任意 URL + 服务端代读」 | ✅ **进评审**（方向级）。落点：**暴露面自查清单增两条固定项** —— ① 「生产环境是否存在任何一次性/管理性端点（安装器、调试页、样例应用、备份控制台、phpinfo、探活面板）」；② 「凡我方对外提供且接受用户提交 URL 并代为拉取的服务（在线预览、文件下载、报表导出、回调地址），按『免认证 + 任意 URL + 服务端代读』三要素自查」。**不新开产物** |
| 网络安全（引用纪律） | 主源 2 明确写「39 天不证明利用了 39 天」；「This site does not resolve the difference」 | ✅ **进评审**（方向级）。落点：**库内引用纪律增两条** —— ① 引用「修复发布 → KEV 收录」间隔时必须同段引用「收录日 ≠ 攻击日」；② 版本线覆盖差异未解决时**不得自行裁定**，须向厂商索取书面确认。**不新开产物** |
| 护网（补丁优先级） | 三条期限 11-30，且 11-29、11-30 为周末 → 实际工作日窗口仅 2 天 | 🟡 **观察项**。落点：**护网补丁优先级表引用 KEV 期限时须标注「该期限约束美国联邦机构」**（库内 11-27 已定此纪律），并**不得因期限紧就把非我方资产排在我方资产之前**。**不产产物** |
| 等保 / 信创 / 隐私保护 | 无 | ❌ 不进 |

---

## 七、总结输出

**一句话结论**：本期是**库内 11-27 日报所提「KEV 采集必须从『按批次跟』改为『按官方 feed 快照 diff』」这条唯一管线动作的第一次落地与验证** —— 抓 CISA 官方 feed 得 `catalogVersion 2026.11.27` / `dateReleased 2026-11-27T18:03:12Z` / `count 1808`，与库内基线（`2026.11.25` / `1805`）逐条 diff 得 **净增 3 条**：**GeoServer CVE-2026-120705**（WFS 存储查询 XML 注入，**免认证**读本地文本文件 / **拉取任意 HTTP(S) 地址**）、**GeoServer CVE-2026-129243**（**服务级别角色校验绕过**，免认证）、**Drupal Core CVE-2026-136716**（异常条件检查不当），**期限均 11-30（11-29、11-30 为周末，实际工作日窗口仅 11-27、11-28 两天）**，**三条取证分诊全为 No、勒索标记全为 Unknown**；⭐⭐⭐ 同期拿到四个库内首条 —— **① 修复版本发布（10-19）到 KEV 收录（11-27）间隔 39 天**（且主源 2 明写「39 天不证明利用了 39 天」，引用时必须同段引用）；**② CVE-2026-129245（Critical）在 2.28.6 / 2.27.7 的通知中完全缺席、仅 3.0.2 列出 → 整改单不得写「升级到 2.28.6 即全闭」**（主源 2 自己也未解决，须向厂商索取书面确认）；**③ 10 月发布 17 个 CVE（1 Critical + 12 High + 4 Medium）仅 2 个进 KEV（11.8%）→「未进 KEV」不等于安全**；**④ CVE Program 与 NVD 对 5 个编号均无记录，而 CISA 条目却链接 NVD → 仅以 NVD/SCA 为输入源的管线会直接漏掉这批**；⭐⭐ **EOL 线官方措辞为「apply this update as a mitigation measure only」**，与库内 11-27 的「EOL ≠ 不可利用」闭环；⭐⭐ **完整时序入库**（8 月初 Rapid7 报告 → 9 月下旬 Eye Security 报告 → 10-19 修复 → 11-25 15:27 UTC watchTowr 观测到利用尝试（SecurityWeek 二手转述）→ 11-27 18:03 UTC 收录 → 11-30 到期）；⭐ **第三方周报「7 New KEVs」与官方 diff 的 3 条不符，第三方统计不得作为入库依据**；⚠️ **我方无 GeoServer / Drupal 使用证据，不得下「我方受影响」结论，但「库内无记录」不等于「未部署」，须自查**。

**落地去向**

- [ ] 产品特性
- [ ] 需求变更
- [ ] 专项整改
- [x] **方向级产物**（网络安全）—— ① KEV 采集固化为「每日 feed 快照 + 逐日 diff + 只写 diff 出的条目」；② 台账「是否在 KEV 出现」改标为优先级信号而非安全状态，并新增「是否已迁移受支持版本线」「EOL 资产改记为已缓解（mitigation only）」两列；③ 漏洞来源清单增列「CISA KEV 官方 feed」为独立于 NVD 的第二来源；④ 整改单写成「产品 × 版本线 × CVE 集合」三元组；⑤ 暴露面自查清单增「生产环境一次性/管理性端点」与「免认证 + 任意 URL + 服务端代读服务」两条；⑥ 引用纪律增两条（收录日 ≠ 攻击日；版本线差异未解决时不得自行裁定）。**均不新开产物、不产专项整改**
- [x] **观察项** —— 护网补丁优先级表引用 KEV 期限时标注「该期限约束美国联邦机构」（沿用库内 11-27 纪律）
- [ ] **待办（须自查）** —— ① 我方是否存在 GeoServer 实例（**直接查版本号，不依赖 NVD/SCA 匹配**）；② 我方是否部署 Drupal Core，若有则查是否 ≥ 10.6.23 / 11.3.23 / 11.4.14 且**已下线公开 install.php**；③ 我方是否部署其他版本线在 2.28.6 / 2.27.7 的 GeoServer 实例（注意 Critical 覆盖差异）
- [ ] **跟踪项** —— ① 11-30 期限后 CISA 目录是否再变动 ② 第三方统计与官方 diff 的 4 条差额来源 ③ GeoServer 官方对 129245 在 2.28/2.27 线覆盖情况的书面答复 ④ CVE Program / NVD 何时补齐这 5 个编号的记录

**关联文档**

- [CISA KEV 目录基线 2026-11-26](cisaKevCatalogBaseline2026-11.md) —— **本篇的直接前序**：该文提出的「按官方 feed 快照 diff」动作在本期落地，其「17% 是 2 年以上旧 CVE」与本篇「17 个只进 2 个」构成闭环
- [CISA KEV 2026-11-25 批次十条（版本基线矩阵 · 取证分诊字段分级）](cisaKev20261125Batch-2026-11.md) —— **本篇「版本线覆盖差异」的规则出处**（库内 11-26 已立「版本基线矩阵」与「按取证分诊字段分级」，本篇提供反例与实证）
- [CISA KEV 2026-11-23 / 11-24 批次三条](cisaKev20261123Batch-2026-11.md) —— 同族的批次记录，可对照各批次取证分诊字段的分布
- [Java4Shell（CVE-2026-114938）：运行时层漏洞 · SCA/SBOM 结构性盲区](java4ShellCve2026114938-2026-11.md) —— **同一类盲区的另一个成因**（「运行时不在清单里」vs 本篇「记录还没生成」）
- [WAF 巡检 2026-11-26（20:37 轮）](wafInspectionSeries20261126-2026-11.md) —— 本期安全域的另一条，暴露面自查的两条新条目可直接并入其站点级台账

---

## 参考链接

- CISA 官方 KEV 目录 JSON feed（主源 1）：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- 独立分析简报：GeoServer 两条 KEV 条目（主源 2）：https://www.pk-sharma.com/briefing/cisa-lists-two-geoserver-flaws-as-exploited-due-30-november-project-says-october-updates-fix-them
- ThreatPodium 周度威胁情报报告 2026-11-27（辅源 1）：https://threatpodium.com/threat-intelligence-report-2026-11-27
- PBCS 每日安全简报 2026-11-27（辅源 2）：https://www.pbcsnyc.com/post/daily-cybersecurity-briefing-november-27-2026
- CISA 官方 Alerts 与 Advisories 列表页（辅源 3）：https://www.cisa.gov/news-events/cybersecurity-advisories

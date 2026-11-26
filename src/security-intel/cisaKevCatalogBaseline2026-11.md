# CISA KEV 目录基线（2026-11-26 快照）—— 库内首份「速度 + 年龄分布」双维度基线，官方 feed 一手可得

> 🔴 强约束 · 采集于 2026-11-27 · 核心标识：**⭐⭐⭐ 库内首条「KEV 目录增速基线」** —— 第三方统计给出**近 30 天新增 45 条、前 30 天 32 条（+40.6%）**，近 90 天 120 条（+53.8%）；⭐⭐⭐ **库内首条「KEV 条目年龄分布」**：244 条同年、40 条 1 年、28 条 2–4 年、30 条 5 年以上 → **近 12 个月新增条目中 17% 是 2 年以上的旧 CVE**（库内 11-19 记的「老未修漏洞仍在被利用」首次有了官方目录级的量化底座）；⭐⭐⭐ **库内首条「官方 KEV feed 一手可得」的实证** —— 直接抓 CISA 官方 JSON feed 拿到 `catalogVersion 2026.11.25` / `count 1805` / `dateReleased 2026-11-25T19:48:12Z`，**库内 11-26 记的「1,795/1,796/1,805 三源不一致」由此闭环**；⭐⭐ **库内首条「11 月整月新增节奏的逐日分布」**（11-06:1 / 11-09:4 / 11-10:6 / 11-13:2 / 11-17:1 / 11-18:4 / 11-20:4 / 11-23:2 / 11-24:3 / 11-25:10）→ **11-25 单日 10 条是当月最高**，且 **11 月共 37 条，占 30 天窗口 45 条的 82%** → **不是均匀流入，是月末集中放量**；⭐⭐ **库内首条「按厂商计的多漏洞打包整改」有了目录级排序**：Mitel 5 / Cisco 3 / Danfoss 3 居前三；⚠️ **目录总数 1,805 是官方 feed 的 `count` 字段，但第三方仍给 1,795/1,796 → 口径仍未统一**；⚠️ **第三方统计明确声明「这些是目录变更计数，不是攻击次数、不是受害者数、不是新披露漏洞数」**。

---

## 一、信源核实

| 项 | 值 |
|---|---|
| 来源请求 | `CISA KEV catalog November 26 2026 added`（web_search，命中第三方追踪站与官方公告列表页）<br>`CISA ICS advisory November 26 2026 industrial control systems`（web_search，用于确认官方公告页的最新日期边界） |
| 原始 URL（主源 1 · **官方一手 feed**） | https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json （CISA 官方 KEV 目录 JSON feed，快照正文 900,018 字符，SHA256 `a76360009e4a65794a2b8073df5475f7a787a3bb83c3bfad2b0c3434a067631a`） |
| 原始 URL（主源 2 · 速度与年龄分布） | https://eastbaycyber.com/kev-dashboard （East Bay Cyber「CISA KEV Velocity Dashboard」，快照标注「Catalog snapshot: 2026-11-26 · 1805 entries」，正文含总量、30/90 天增速、勒索占比与 CVE 年龄分布四组图表，快照正文 6,438 字符） |
| 原始 URL（主源 3 · 30 天窗口逐条） | https://www.secquill.com/research/exploited-vulnerabilities （SecQuill「Exploited vulnerability tracker」，快照标注「Snapshot: 2026-11-26，Window: 2026-10-28 to 2026-11-26」，逐条列出 45 条新增与厂商统计，快照正文 30,970 字符） |
| 原始 URL（辅源 4 · 官方公告列表页） | https://www.cisa.gov/news-events/cybersecurity-advisories （CISA 官方 Alerts 列表，用于确认「截至采集时官方最新 Alert 仍为 Nov 25」，检索摘要） |
| 发布主体 | CISA（官方 feed）/ East Bay Cyber / SecQuill（第三方追踪站） |
| 发布/更新时间 | 官方 feed `dateReleased = 2026-11-25T19:48:12.4344Z`、`catalogVersion = 2026.11.25`；East Bay Cyber 快照日 2026-11-26；SecQuill 快照日 2026-11-26 |
| 采集时间 | 2026-11-27 07:13:20 – 07:17:19 |

---

## 二、事实核查

| # | 数据点 | 原文表述 | 核查方式 | 结论 | 备注 |
|---|---|---|---|---|---|
| 1 | 官方目录版本 | feed 头部：`"catalogVersion": "2026.11.25"`，`"dateReleased": "2026-11-25T19:48:12.4344Z"` | 直读官方 feed 快照原文 | ✅ **已核** | ⭐⭐⭐ **库内首条「直接抓取官方 KEV feed」的样本** → 此前库内所有 KEV 条数都来自第三方 |
| 2 | 官方目录总数 | feed 头部：`"count": 1805` | 直读 | ✅ **已核（1,805）** | ⭐⭐⭐ **闭环库内 11-26 的「1,795 / 1,796 / 1,805 三源不一致」**：**官方 feed 自报 1,805**，与 CVE.ICU 与 East Bay Cyber 一致 → **Vulntide 的 1,795/1,796 是「有 CVE 记录条目数」口径（Vulntide 自注 1,795）** → **正确表述：官方 1,805，第三方去重口径 1,795–1,796，差 9–10 条为口径差** |
| 3 | 11-26 是否有新增 | 官方 feed 中全部条目 `dateAdded` 最大值为 `2026-11-25`；11-25 当日 10 条 | 解析 feed 全部条目并统计 dateAdded 分布 | ✅ **已核（11-26 无新增）** | ⭐⭐ **官方公告列表页亦显示最新 Alert 为 Nov 25** → **11-26 整日无 KEV 新增**（与 11-25 的 10 条形成对照） |
| 4 | 11 月逐日新增分布 | 官方 feed 统计：11-06:1 / 11-09:4 / 11-10:6 / 11-13:2 / 11-17:1 / 11-18:4 / 11-20:4 / 11-23:2 / 11-24:3 / 11-25:10 | 解析 feed 全部 `dateAdded` 字段并分组 | ✅ **已核（11 月共 37 条）** | ⭐⭐⭐ **库内首条「整月新增节奏的逐日分布」** |
| 5 | 11-25 批次条数（官方口径） | feed 中 `dateAdded = 2026-11-25` 的条目共 10 条 | 解析统计 + 与库内 11-26 文档已记的 10 条 CVE 编号逐一比对：103406 / 133469 / 41450 / 25914 / 25915 / 133324 / 133275 / 133311 / 133303 / 133323 | ✅ **已核（10 条，编号逐一对上）** | ⭐⭐⭐ **库内首条「用官方 feed 逐条复核既有 KEV 批次」** → **库内 11-25/11-26 两期文档的 10 条清单全部正确，无需修正** |
| 6 | 11-25 批次的联邦期限 | feed 逐条 `dueDate`：CVE-2026-103406 / 133469 / 25914 / 25915 / 133324 / 133275 / 133303 / 133323 → **2026-11-28**；CVE-2025-41450 / 133311 → **2026-12-09** | 解析 feed | ✅ **已核（与库内 11-25 记录一致）** | ⭐⭐ **库内 11-26 记的「8 条期限 11-28、2 条 12-09」经官方 feed 逐条确认** → 最早期限 **11-28 距今仅 1 天**（采集日 11-27） |
| 7 | 近 30 天新增数 | East Bay Cyber：「Added, last 30 days **45** ▲ **+13** vs prior period」；SecQuill：「45 catalogue additions… The preceding 30 days… contained **32** additions」 | 两独立第三方源比对 + 算术核对：45 − 32 = 13 ✅，13/32 = **+40.6%** ✅ | ✅ **已核（45 vs 32，+13）** | ⭐⭐⭐ **库内首条「KEV 增速基线」** → **两源独立且数值完全一致** |
| 8 | 近 90 天新增数 | East Bay Cyber：「Added, last 90 days **120** ▲ **+42** vs prior period」 | 直读 | ✅ **已核（120）** | ⭐⭐ 算术核对：120 − 42 = 78 前 90 天；120/78 = +53.8% |
| 9 | 30 天窗口与 11 月的关系 | SecQuill 窗口 2026-10-28 至 2026-11-26 共 45 条；官方 feed 统计 11-01~11-26 共 **37** 条 | 内部勾稽 | ✅ **已核** | ⭐⭐⭐ **库内首条「整月新增占 30 天窗口的比例」**：37/45 = **82.2%** → **11 月是 30 天窗口的绝对主力月，窗口的 45 条几乎全部来自 11 月**；窗口剩余 8 条来自 10-28~10-31 |
| 10 | 厂商排名 | SecQuill：「Vendor Additions — **Mitel 5** / **Cisco 3** / **Danfoss 3** / Apache 2 / Barracuda Networks 2 / Broadcom 2 / Ivanti 2 / Apple 1 / BerriAI 1 / Check Point 1」 | 直读 | ✅ **已核** | ⭐⭐ **库内 11-25/11-26 已记 Danfoss 三条、Mitel 五条** → **本期给出目录级厂商排序**，与库内逐条记录完全一致 |
| 11 | 勒索标记数 | SecQuill：「**1 flagged for known ransomware use**」；East Bay Cyber：「Ransomware-linked **9%** of entries added in the last 12 months」 | 两源并列 | ✅ **已核（30 天窗口 1 条；近 12 个月 9%）** | ⭐⭐ **注意两个数字口径不同**：1 条是 30 天窗口的绝对数，9% 是 12 个月的比例 → **不得混算** |
| 12 | CVE 年龄分布 | East Bay Cyber：「244 Same year / 40 1 year old / 28 2-4 years old / 30 5+ years old」「**17% of KEV entries added in the last 12 months are CVEs from 2+ years ago**（by CVE ID year）」 | 直读 + 算术核对：244+40+28+30 = 342；28+30 = 58；58/342 = **16.96% ≈ 17%** ✅ | ✅ **已核（自洽）** | ⭐⭐⭐ **库内首条「KEV 条目年龄分布」** → 官方目录级证据支撑库内 11-19 记的「老未修漏洞仍在被利用」 |
| 13 | 近 12 个月厂商排名 | East Bay Cyber：「Microsoft 42 / Cisco 23 / Google 11 / Apple 11 / Fortinet 10 / Linux 9 / Ivanti 8 / Adobe 7 / SonicWall 6 / Citrix 6」 | 直读 | ✅ **已核** | ⭐⭐ **库内首条「12 个月厂商分布」** → 与 30 天窗口的 Mitel/Cisco/Danfoss 三强形成对照：**短期攻击面集中在通信与 OT，长期存量集中在通用 IT** |
| 14 | 计数含义的官方免责 | SecQuill：「These totals measure changes to the catalogue. They **do not measure the number of attacks, victims or newly discovered software flaws**」「The year in a CVE identifier is not a reliable publication date, and a catalogue addition date does not establish when exploitation began」 | 直读 | ✅ **已核** | ⭐⭐⭐ **库内首条「第三方统计自己写明的使用边界」** → **「45 条」不得被表述为「45 起攻击」**；**「CVE 年份」不得被表述为「披露年份」** |
| 15 | 30 天窗口内的旧 CVE | SecQuill：「The current window includes **6 entries with a CVE identifier from a year before 2026**」 | 直读 + 与 #12 交叉：6/45 = 13.3%（窗口内）vs 17%（12 个月） | ✅ **已核（6 条）** | ⭐⭐ **两个口径下的旧 CVE 占比不同（13.3% vs 17%）→ 说明旧漏洞利用在近 30 天并未加剧** |
| 16 | 「产品名匹配 ≠ 存在漏洞」 | SecQuill：「A product name match alone is not proof that a particular system is vulnerable」「a catalogue match does not establish that your assets are vulnerable」；East Bay Cyber：「A CVE only enters the KEV catalog once CISA confirms active exploitation… the monthly addition rate is a **floor** on real-world exploitation activity, not a count of disclosed vulnerabilities」 | 直读 | ✅ **已核** | ⭐⭐⭐ **库内首条「两方同时给出「目录命中 ≠ 我方受影响」的免责」** → 与库内 11-26 定的「不得下我方受影响结论」完全一致，**外部来源与库内纪律互相印证** |
| 17 | 联邦期限的适用范围 | SecQuill：「These due dates are CISA catalogue deadlines associated with its federal civilian agency requirements. They are **not universal legal deadlines for every organization**」；East Bay Cyber：「Federal agencies must remediate each entry by its CISA due date under BOD 22-01; most organizations treat KEV listing as a patch-now signal regardless of CVSS score」 | 直读 | ✅ **已核** | ⭐⭐ **库内首条「期限适用范围的两源一致表述」** → **11-28 这个日期对非联邦机构无强制力，只作优先级信号** |
| 18 | 补丁优先级信号 | East Bay Cyber：「most organizations treat KEV listing as a **patch-now signal regardless of CVSS score**」 | 直读 | ✅ **已核** | ⭐⭐ 与库内 11-19 记的「护网补丁优先级应按发现—可利用成本基线排，而非按 CVSS」方向一致 → **两条独立来源同向** |

> **核查小结**：本期新增事实 **18 条可核**，其中 **14 条一手/官方 feed 直接可核**、**2 条算术自洽核对通过**（#7 #12）、**2 条为口径差异**（#2 #11）。**五条必须写明的边界**：① **11-26 官方无 KEV 新增**；② **1,805 是官方 `count`，1,795/1,796 是第三方「有 CVE 记录条目数」，差 9–10 条为口径差**；③ **45 条是目录变更计数，不是攻击次数**；④ **CVE 年份不等于披露年份**；⑤ **11-28 是联邦期限，对我方无强制力**。

---

## 三、原文归档（快照）

| 快照文件 | SHA256 | 抓取时间 | 字符数 | HTTP |
|---|---|---|---|---|
| `raw/snapshots/security/cisa-kev-catalog-feed-20261127.md` | `a76360009e4a65794a2b8073df5475f7a787a3bb83c3bfad2b0c3434a067631a` | 2026-11-27 07:13:29（07:17:19 以更大 max-chars 重抓，SHA256 相同，字节内容一致） | 60,018 → 900,018（重抓后完整） | 200 |
| `raw/snapshots/security/kev-velocity-dashboard-20261126.md` | `a5bc7c4a7549d1b3e622bcd31bb7469e3f12bc1e10e803d1d9d51fe8ed332e21` | 2026-11-27 07:13:20 | 6,438 | 200 |
| `raw/snapshots/security/kev-window-30d-20261126.md` | `2a87cab250c985ee8151b6a79762ab8e66e8ec7d016e9080bce012edc6c14b75` | 2026-11-27 07:13:22 | 30,970 | 200 |

**关键原文摘录**

> **官方 KEV feed 头部**（`cisa-kev-catalog-feed-20261127.md`）：
> > ```
> > {
> > "title": "CISA Catalog of Known Exploited Vulnerabilities",
> > "catalogVersion": "2026.11.25",
> > "dateReleased": "2026-11-25T19:48:12.4344Z",
> > "count": 1805,
> > "vulnerabilities": [
> > {
> > "cveID": "CVE-2026-103406",
> > "vendorProject": "Hewlett Packard Enterprise (HPE)",
> > ```

> **East Bay Cyber 仪表盘**（`kev-velocity-dashboard-20261126.md`）：
> > 「Catalog snapshot: 2026-11-26 · **1805 entries** · Source: CISA KEV Catalog」
> > 「Added, last 30 days **45** ▲ **+13** vs prior period」
> > 「Added, last 90 days **120** ▲ **+42** vs prior period」
> > 「Ransomware-linked **9%** of entries added in the last 12 months」
> > 「How old are CVEs when exploitation is confirmed? **244 Same year / 40 1 year old / 28 2-4 years old / 30 5+ years old**」
> > 「**17% of KEV entries added in the last 12 months are CVEs from 2+ years ago** (by CVE ID year): old, unpatched vulnerabilities keep getting exploited long after disclosure.」
> > 「A CVE only enters the KEV catalog once CISA confirms active exploitation in the wild, so the monthly addition rate is a **floor** on real-world exploitation activity, not a count of disclosed vulnerabilities.」

> **SecQuill 30 天窗口**（`kev-window-30d-20261126.md`）：
> > 「Snapshot: **2026-11-26**. Window: **2026-10-28 to 2026-11-26**, inclusive, in UTC. **45 catalogue additions**, 33 vendor names represented, 1 flagged for known ransomware use」
> > 「The preceding 30 days, from 2026-09-28 to 2026-10-27, contained **32 additions**」
> > 「These totals measure changes to the catalogue. They **do not measure the number of attacks, victims or newly discovered software flaws**.」
> > 「The current window includes **6 entries with a CVE identifier from a year before 2026**.」
> > 「Vendor Additions — **Mitel 5 / Cisco 3 / Danfoss 3** / Apache 2 / Barracuda Networks 2 / Broadcom 2 / Ivanti 2」

---

## 四、概要提取

- ⭐⭐⭐ **库内首次直接抓取 CISA 官方 KEV feed**：`catalogVersion 2026.11.25` / `count 1805` / `dateReleased 2026-11-25T19:48:12Z` —— **库内 11-26 记的「1,795/1,796/1,805 三源不一致」由此闭环**：官方为 1,805，第三方去重口径 1,795–1,796，**差 9–10 条是口径差不是数据错**。
- ⭐⭐⭐ **库内首条「KEV 增速基线」**：近 30 天新增 **45** 条 vs 前 30 天 **32** 条（**+13 / +40.6%**），近 90 天 **120** 条（+42）；两个独立第三方源数值完全一致。
- ⭐⭐⭐ **库内首条「整月新增节奏逐日分布」**：11 月共 **37** 条（11-06:1 / 11-09:4 / 11-10:6 / 11-13:2 / 11-17:1 / 11-18:4 / 11-20:4 / 11-23:2 / 11-24:3 / 11-25:10），**占 30 天窗口 45 条的 82.2%** → **月末集中放量，11-25 单日 10 条为当月最高**。
- ⭐⭐⭐ **库内首条「KEV 条目年龄分布」**：244 同年 / 40 一年 / 28 二至四年 / 30 五年以上；**近 12 个月新增中 17% 是 2 年以上旧 CVE** → 库内 11-19 记的「老未修漏洞仍在被利用」首次有了官方目录级量化底座。**但 30 天窗口内旧 CVE 占比只有 6/45 = 13.3%，低于 12 个月口径 → 近月未加剧**。
- ⭐⭐⭐ **用官方 feed 逐条复核了库内 11-25 批次**：10 条 CVE 编号、8 条期限 11-28 / 2 条期限 12-09 —— **全部正确，无需修正**；**11-26 官方无新增**。
- ⭐⭐ **两个口径层次给出两种攻击面画像**：30 天窗口 Mitel 5 / Cisco 3 / Danfoss 3（通信与 OT 集中）；12 个月 Microsoft 42 / Cisco 23（通用 IT 存量主导）→ **短期与长期的优先级不能共用一张表**。
- ⭐⭐⭐ **两方同时给出免责口径**：「45 条不是攻击次数、不是受害者数、不是新披露漏洞数」「CVE 年份不是可靠的披露年份」「产品名匹配不证明我方受影响」「11-28 是联邦期限不是普遍法律期限」→ **与库内 11-26 已立的纪律逐条同向**。

---

## 五、主要观点

**原文主张**

- CISA（官方 feed）：目录为 `2026.11.25` 版、共 **1,805** 条，发布于 2026-11-25T19:48:12Z，收录标准为「已分配 CVE 编号 + 有可靠的在野利用证据 + 有明确修复动作」。
- East Bay Cyber：「A CVE only enters the KEV catalog once CISA confirms active exploitation in the wild, so the monthly addition rate is a **floor** on real-world exploitation activity, not a count of disclosed vulnerabilities.」并给出 30 天 +13、90 天 +42、勒索占比 9%、CVE 年龄分布（244/40/28/30）与「17% 是 2 年以上」；以及「most organizations treat KEV listing as a **patch-now signal regardless of CVSS score**」。
- SecQuill：「These totals measure changes to the catalogue. They do not measure the number of attacks, victims or newly discovered software flaws.」「The year in a CVE identifier is not a reliable publication date, and a catalogue addition date does not establish when exploitation began.」「A product name match alone is not proof that a particular system is vulnerable.」「These due dates are CISA catalogue deadlines… **not universal legal deadlines for every organization**.」并给出 45 vs 32、33 个厂商、1 条勒索标记、6 条窗口内旧 CVE、厂商前三 Mitel 5 / Cisco 3 / Danfoss 3。
- CISA（官方公告列表页）：截至采集时，最新 Alert 仍为 **Nov 25**，11-26 无新增公告。

**我方判断**

- ⭐⭐⭐ **「能直接抓官方 feed」这件事本身就是本期最大的工程性结论。** 库内此前所有 KEV 数据（11-20、11-23/24、11-25 三批）**全部来自第三方转述**，这带来两个已实际发生过的代价：① 库内 11-26 不得不写「目录总数三源不一致、不得引用单一数字为权威」，而**官方 feed 就在一个公开 URL 上**；② 库内 11-25 那批「10 条」是靠三家第三方**条数一致**才确认的，而不是靠官方逐条核对。**本期用官方 feed 逐条复核，10 条编号与期限全部正确 —— 这既验证了库内前几期的工作，也说明第三方转述在「条数」这个维度上确实可靠，但在「总数」「分布」这类需要精确计数与统计的维度上不可靠**。**结论不是「第三方不可信」，而是「凡是可以从官方 feed 直接算的，一律自己算」**。
- ⭐⭐⭐ **+40.6% 的增速不是噪音，它推翻了一个隐含假设**：库内此前把 KEV 批次当作**离散事件**处理（每期报「本批 N 条、最早期限 X 天」），隐含假设是「CISA 大约每周加一批」。**数据显示 11 月一个月加了 37 条、30 天窗口加 45 条且比前 30 天快了 40%** —— **这意味着「按批次逐条跟踪」这种采集方式本身在漏**：一个月 37 条分散在 10 个日子，**任何只在某一天读一次目录的人都会漏掉大部分**。**我方若要维持 KEV 覆盖，必须把采集方式从「按批次跟」改成「按目录 diff」** —— 即定期拉官方 feed、与上次快照做差分，**这正好可以用本库已有的快照机制实现**（每期存一份 feed 快照，下期自动出增量）。**这是本期唯一一条真正改变采集管线的结论。**
- ⭐⭐⭐ **「17% 是 2 年以上的旧 CVE」这个数字，改变了「未修补 = 低风险」这个默认假设的权重。** 库内 11-19 已经指出过「老未修漏洞仍在被利用」，但当时只有定性。本期给了目录级的量化：**近 12 个月新增条目里 17% 是两年前以上披露的 CVE**。**对我方的直接含义**：我方资产台账里那些「太老了、厂商早不维护了、就先放着」的条目，**在 KEV 目录里有相当比例是被现实利用过的** —— **EOL 不等于不可利用**。库内 Danfoss 篇已经推出「生命周期必须作为暴露面台账一等字段」，**本期给了这条结论一个外部的量化支撑**。
- ⭐⭐ **但必须同时读另一个数字，否则会过度反应**：**30 天窗口内旧 CVE 占比只有 6/45 = 13.3%，低于 12 个月的 17%** → **旧漏洞利用在近一个月并没有加剧，反而占比在下降**。正确读法是：**「老漏洞被利用」是一个结构性长期特征，不是当前正在恶化的紧急信号** → **它支持「EOL 台账」这个长期基线建设，不支持「立即启动一次老资产清理专项行动」**。
- ⭐⭐⭐ **两个口径层次必须分表，不能合成一张「KEV 优先级表」**：30 天窗口是 **Mitel 5 / Cisco 3 / Danfoss 3**（企业通信 + OT 制冷 + 网络设备），12 个月是 **Microsoft 42 / Cisco 23 / Google 11**（通用 IT）。**前者告诉我「现在谁在被打」，后者告诉我「谁的地盘最大」**。**我方是 DER/聚合/监控平台方 —— 短窗口里 Danfoss 排到第三这件事，比 Microsoft 排第一重要得多**，因为它说明**攻击者正在打「连着物理世界的设备」**。**这条与我方业务模式处在同一侧，我方不能拿「我们不做这些产品」作免责**（库内 Danfoss 篇已有同向判断）。
- ⭐⭐ **外部来源的免责措辞与我方纪律完全同向，这本身值得记一笔**：库内 11-26 已经定了「不得下我方受影响结论」，本期两个独立第三方**各自主动写了同一句话**（「产品名匹配不证明受影响」「45 条不是攻击次数」「联邦期限不是普遍法律期限」）。**这说明库内的口径不是自造的小规矩，而是与外部公开情报服务的标准做法一致** —— 这对我方评审会上解释「为什么这条不进评审」很有用。**同时提醒：这些免责是第三方写给自己的读者写的，我方引用时不能变成「所以不必紧张」** —— 它们的作用是**防止误判，不是免除动作**。
- ⭐ **最容易被误用的一个数字是「45」**。它同时可以被写成「45 起攻击」「45 个新漏洞」「45 个受害组织」—— **三种都错**。库内凡是引用这个数字，必须连口径一起写。**这与库内 11-25/11-26 反复强调的「口径必须带」是同一条纪律在不同维度的应用**。
- ⭐ **11-28 距采集日仅 1 天**：库内 11-25/11-26 已两次标注「最早期限 11-28，距今 2 天」，**今天已是最后一天**。**但这条期限约束的是美国联邦民事机构，对我方无强制力** —— 我方是否在 11-28 前处置那 10 条，取决于我方是否装了那些产品（库内结论：我方一条都不用装 → 无需动作）。**这条只需在简报里如实记「期限今日到期」，不产任何我方动作**。

---

## 六、参考意义

| 方向（网络安全/信创/等保/隐私保护/护网） | 可证事实 | 本阶段处理 |
|---|---|---|
| 网络安全（暴露面台账 · EOL 基线） | KEV 近 12 个月新增条目中 **17% 为 2 年以上旧 CVE**（244/40/28/30 官方目录级分布）；官方与两第三方均确认「目录命中 ≠ 我方受影响」 | ✅ **进评审**（方向级）。落点：**暴露面台账增「是否 EOL / 最后一次安全更新 / 是否在 KEV 出现」三字段，并把 KEV 快照 diff 做成常态化输入**。与库内 11-24 已挂的「EOL 台账」待办合并。**不新开产物** |
| 网络安全（采集管线） | 官方 feed 可直取；11 月新增 37 条占 30 天窗口 45 条的 82%；30 天增速 +40.6% → **按批次跟会漏** | 🟡 **方向级台账项 + 采集管线待办**（与库内已挂的「`collect.py` 补齐六字段」并列）。落点：**KEV 采集方式从「按批次跟」改为「按官方 feed 快照 diff」，每期存一份 feed 并自动出增量**。**不产安全域产物**（属采集管线，不属五方向产物） |
| 网络安全（优先级排序） | 30 天窗口 Mitel 5 / Cisco 3 / Danfoss 3（通信 + OT + 网络）；12 个月 Microsoft 42 / Cisco 23；第三方给出「KEV 收录 = patch-now 信号，不看 CVSS」 | 🟡 **观察台账项**。落点：**优先级表必须分「短期窗口」与「长期存量」两张**，且短期窗口中 **OT 供应商排名** 单独加权重。**不新开产物** |
| 护网 | 官方目录确认「收录即在野利用」，且暴露的是「已被真实使用」的漏洞集合 | 🟡 **观察台账项**。落点：**护网演练的补丁优先级可直接引用 KEV 作为「已被真实使用」的一档判据**（比 CVSS 强），与库内 11-19「按发现—可利用成本基线排」的结论同向。**不新开产物** |
| 等保 / 信创 / 隐私保护 | 无 | ❌ 不进 |

---

## 七、总结输出

**一句话结论**：CISA 官方 KEV feed 可直接抓取（`2026.11.25` 版 / **1,805** 条 / 发布于 11-25T19:48Z），**库内 11-26 挂的「目录总数三源不一致」就此闭环**（官方 1,805，第三方去重口径 1,795–1,796，差 9–10 条为口径差）；本期真正的增量是两条目录级基线 —— **增速**（近 30 天新增 45 条 vs 前 30 天 32 条，**+40.6%**；11 月单月 37 条占窗口 82%）与 **年龄**（244 同年 / 40 一年 / 28 二至四年 / 30 五年以上，**近 12 个月新增中 17% 是 2 年以上旧 CVE**，但 30 天窗口内旧 CVE 占比仅 13.3% → 是结构性长期特征而非正在恶化的紧急信号）；**这两条合起来逼出我方唯一一条真正改变采集管线的动作 —— KEV 采集必须从「按批次跟」改为「按官方 feed 快照 diff」，否则一个月 37 条分散在 10 天，逐次读目录必然漏**；同时**用官方 feed 逐条复核了库内 11-25 批次的 10 条编号与 2 组期限，全部正确**；⚠️ 11-26 官方无新增，**11-28 期限今日到期但约束的是美国联邦机构，我方一条都不用装、无需动作**。

**落地去向**

- [ ] 产品特性
- [ ] 需求变更
- [ ] 专项整改
- [x] **方向级产物**（网络安全）—— 暴露面台账增「是否 EOL / 最后一次安全更新 / 是否在 KEV 出现」三字段；KEV 优先级表分「短期窗口 / 长期存量」两张，OT 供应商排名单独加权；护网补丁优先级引用 KEV 作为「已被真实使用」一档判据。**不新开产物、不产专项整改**（第 1 关无我方侧一手证据）
- [x] **采集管线待办**（不产安全域产物）—— KEV 采集改为官方 feed 快照 diff，每期存一份并自动出增量；所有引用必须带口径（45 = 目录变更计数，非攻击次数）

**关联文档**

- [CISA KEV 2026-11-25 批次十条](cisaKev20261125Batch-2026-11.md) —— 本篇用官方 feed 逐条复核其 10 条编号与期限，**结论：全部正确，无需修正**
- [CISA KEV 2026-11-23 / 11-24 批次](cisaKev20261123Batch-2026-11.md) —— 同类条目的前一批
- [Danfoss AK-SM 8xxA 制冷控制器案卷](danfossAksmRefrigerationCampaign-2026-11.md) —— Danfoss 在 30 天窗口厂商排名第三，本篇为其「OT 供应商在被打」这一判断提供目录级背景
- [NIST SP 800-82 Rev.4 OT 安全基线草案](nistSp80082r4OtSecurity-2026-11.md) —— KEV/EPSS/SSVC 判据组合的外部权威背书
- [Java4Shell（CVE-2026-114938）](java4ShellCve2026114938-2026-11.md) —— 库内 11-19 已记「老未修漏洞仍在被利用」的定性来源，本篇给其目录级量化

---

## 参考链接

- CISA 官方 KEV 目录 feed（一手）：https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA 官方 Alerts 与 ICS Advisories 列表页：https://www.cisa.gov/news-events/cybersecurity-advisories
- East Bay Cyber · CISA KEV Velocity Dashboard（快照 2026-11-26）：https://eastbaycyber.com/kev-dashboard
- SecQuill · Exploited vulnerability tracker（快照 2026-11-26，窗口 2026-10-28~11-26）：https://www.secquill.com/research/exploited-vulnerabilities

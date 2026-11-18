# WAF 巡检 2026-11-18：我方 `/preview/getCorsFile` 接口的 Base64 URL 参数面 —— 库内首次出现"服务端按客户端指定 URL 取文件"的一手证据

> 🔴 强约束 · 采集于 2026-11-19 · 核心标识：**库内首次取得"我方自有接口的参数即 Base64 编码的远端 URL"的一手证据** —— `idmo.pinnenger.com:16443/preview/getCorsFile?urlPath=<base64>`，解码后为 `https://idmo.pinnenger.com:16443/fileManager/kkfDownloadAnnex?fileId=…&previewToken=…` · **5h 累计 4 次 · WAF 动作 Deny · 规则 `policy_rule44` · 风险 Medium · 事件 ID `3af5d9b6f8e143a7b396ff2e54bb96b6`** · **与 11-17 库内首现的 `SSRF` 类型构成直接的方法论串联** · ⚠️ **不得下"我方存在 SSRF 漏洞"结论**

---

## 一、信源核实

| 项 | 值 |
|---|---|
| 来源请求 | 内部数据源采集（**非 web_search**）：`python3 scripts/collect.py --waf-report /home/test/.openclaw/workspace/waf-inspection-report-latest.md --out raw/security-2026-11-19.json`（采集输出 **3 条**：2 条 Info Leak 判定为正常业务 + 1 条攻击类型分布聚合项） |
| 原始 URL（内部数据源） | `/home/test/.openclaw/workspace/waf-inspection-report-latest.md` → 符号链接指向 `waf-inspection-report-2026-11-18-203733.md`（报告时间 **2026-11-18 20:37:33**，今日第 **5/5** 次巡检，**v15.11**） |
| 原始 URL（内部数据源 · 采集输出） | `raw/security-2026-11-19.json`（**按规则不入库**，已 gitignore） |
| 发布主体 | SafeLine WAF 巡检脚本（内部，v15.11 报告格式 / v16.5 判定逻辑）· 巡检报告生成于 2026-11-18 20:37 |
| 发布/更新时间 | **2026-11-18 20:37:33**（第 5/5 次巡检） |
| 采集时间 | 2026-11-19 07:11:51（`collect.py`）· 巡检报告原件直读 2026-11-19 07:12 前后 · **Base64 参数解码校验 2026-11-19 07:12** |

> ⚠️ **本条为内部数据源，无 `source_url`（外链）** —— 与库内既有做法一致（[epicsDerExposure-2026-11](epicsDerExposure-2026-11.md)、[wafSsrfProbeFirstAppearance-2026-11-17](wafSsrfProbeFirstAppearance-2026-11-17.md) 的 WAF 观测条目同样以内部报告路径为准）。**本条不新建外部快照**：WAF 巡检报告是**内部**数据源，不经 `scripts/snapshot.py` 抓取（该脚本只处理外部 URL），因此**第 3 段的"快照"以巡检报告文件路径 + 章节定位 + 读取时间 + 事件 ID 替代**，并显式说明。
>
> 📎 **入库理由**：库内 [wafSsrfProbeFirstAppearance-2026-11-17](wafSsrfProbeFirstAppearance-2026-11-17.md) 已记录 **11-17 库内首次出现 `SSRF` 攻击类型**（命中主站 `www.pinnenger.com/favicon.ico`，payload 仅 `file://`，已 Deny），但当时**无法判断我方系统里是否存在与 SSRF 入口同构的接口**。**本期首次取得了这样的证据**：我方 `idmo` 站点上**存在一个以 Base64 编码的远端 URL 为参数的"取跨域文件"接口**（`/preview/getCorsFile?urlPath=`），**其语义（服务端按客户端指定的 URL 去取资源）与 SSRF 的前置条件同构**。→ **按去重规则，`source_url`（内部报告路径 + 事件 ID `3af5d9b6f8e143a7b396ff2e54bb96b6`）与既有条目均不同 → 属新事件，新建文档**。

---

## 二、事实核查

| 数据点 | 原文表述 | 核查方式 | 结论 | 备注 |
|---|---|---|---|---|
| **⭐⭐⭐ 接口形态：`getCorsFile` 的参数就是 Base64 编码的远端 URL** | 报告"Info Leak 拦截报文（5h 内聚合事件）"节 `49.118.94.3` 条目：*- **URL**: `https://idmo.pinnenger.com:16443/preview/getCorsFile?urlPath=aHR0cHM6Ly9pZG1vLnBpbm5lbmdlci5jb206MTY0NDMvZmlsZU1hbmFnZXIva2tmRG93bmxvYWRBbm5leD9maWxlSWQ9NTdhNmU3ZDctMDNmNC00YTM5LThmYTgtNDhlZGY0YTkxOGI3JnNlcnZpY2VJZD0yJnVzZXJJZD00OSZwcmV2aWV3VG9rZW49MTc5NTAwMDk4MzAyMy4xMDE4OTllOTJkMjExNTc5MzU2NDRkNjQ2YmFkZjQ4YiZmdWxsZmlsZW5hbWU9NTdhNmU3ZDctMDNmNC00YTM5LThmYTgtNDhlZGY0YTkxOGI3LnBkZg==`* | **本地 Base64 解码校验（2026-11-19 07:12）**：解出 `https://idmo.pinnenger.com:16443/fileManager/kkfDownloadAnnex?fileId=57a6e7d7-03f4-4a39-8fa8-48edf4a918b7&serviceId=2&userId=49&previewToken=1795000983023.101899e92d21157935644d646badf48b&fullfilename=57a6e7d7-03f4-4a39-8fa8-48edf4a918b7.pdf` | ✅ **已核（解码结果与报告原文逐字一致）** | ⭐⭐⭐ **这是本条的核心事实**：**接口名 `getCorsFile`（取跨域文件），参数名 `urlPath`，其值解码后是一个完整的、带协议与主机的 URL**，且该 URL 指向**我方自己的另一个接口** `/fileManager/kkfDownloadAnnex`（附件下载，带 `fileId` / `serviceId` / `userId` / `previewToken` / `fullfilename`）。⚠️ **必须写明的边界**：**本条证明的是"接口形态与 SSRF 入口同构"，不是"该接口可被用于 SSRF"** —— 报告中的样本**指向的是我方自身主机**（不存在外部目标），**未见任何跨主机或内网地址的取值** |
| **⭐⭐ 第二个同类接口 `okrsUrlPreview`** | 报告同节 `180.163.29.217` 条目：*- **URL**: `https://idmo.pinnenger.com:16443/preview/okrsUrlPreview?url=L2ZpbGVNYW5hZ2VyL2trZkRvd25sb2FkQW5uZXg/ZmlsZUlkPWFhZDdmNzU1LTY3M2ItNDViMC04ZmExLTAyOWM5Y2ZiZWQ5ZiZzZXJ2aWNlSWQ9MiZ1c2VySWQ9MjI2NyZwcmV2aWV3VG9rZW49MTc5NDk5MzI1NDQ5OC4xODJkNmY4M2U3MGM5NTcyNjZjMGNlYzM4NzI3ZWNhZCZmdWxsZmlsZW5hbWU9YWFkN2Y3NTUtNjczYi00NWIwLThmYTEtMDI5YzljZmJlZDlmLnBkZg==`* | 本地 Base64 解码校验：解出 `/fileManager/kkfDownloadAnnex?fileId=aad7f755-673b-45b0-8fa1-029c9cfbed9f&serviceId=2&userId=2267&previewToken=1794993254498.182d6f83e70c957266c0cec38727ecad&fullfilename=aad7f755-673b-45b0-8fa1-029c9cfbed9f.pdf` | ✅ **已核** | ⭐⭐ **同一站点的第二个同类接口，参数名 `url`** → **这不是一个接口的偶发写法，而是 `/preview/` 路径下的成组接口模式**（`getCorsFile` + `okrsUrlPreview`）。⚠️ **两者差异**：`getCorsFile` 解码后是**绝对 URL**（带协议+主机），`okrsUrlPreview` 解码后是**相对路径**（无协议无主机）→ **风险面不同：前者天然具备跨主机取址的能力，后者在本样本中不具备**。⭐ **对代码审计的指引意义：审计范围应覆盖 `/preview/` 下全部接口，而不是只查这两个** |
| **⭐⭐ `previewToken` 的结构（可推算性线索）** | 两条样本的 `previewToken` 分别为 `1795000983023.101899e92d21157935644d646badf48b` 与 `1794993254498.182d6f83e70c957266c0cec38727ecad` | 两样本逐字比对 + 对前段做时间戳换算 | ✅ **结构已核；⭐ 换算结果为推算（非原文）** | ⭐⭐ **结构 = `<毫秒时间戳>.<32 位十六进制>`**：前段 `1795000983023` / `1794993254498` 是**毫秒级时间戳**（相差 7723 ms ≈ **7.7 秒**），后段是 128-bit 十六进制串。⚠️ **我方判断（明确标注为推算，非原文）**：前段**可由任何人从本地时钟换算得到**（时间戳不是秘密），**秘密只可能在后段** → 因此**该令牌不是"时间戳本身可猜"的可重放型令牌**，但**时间戳泄露本身泄露了两个信息：① 令牌签发时刻 ② 令牌签发后 7.7 秒内两个不同 userId（49 与 2267）各取了一次**。⚠️ **不得据此下"令牌可预测"结论**（后段为 128-bit 随机/哈希，未见密钥来源） |
| **⭐⭐ 下载令牌出现在 URL query 中** | 两条样本的 `previewToken` 均位于 URL 查询串内（明文） | 报告原文逐字 | ✅ **已核** | ⭐⭐ **这是一个与 CVE 无关、但完全成立的结构性事实**：**附件下载令牌以明文置于 GET 查询串** → 必然进入 **WAF / 网关 / CDN / 反向代理访问日志、浏览器历史、Referer 头、监控与工单系统**。⚠️ **这不等于"已泄露"**（日志在我方侧，不等于外部可见），但**它把一个本该是"授权凭据"的东西变成了"日志条目"** → **必须写明这是暴露面事实，不是漏洞结论** |
| **WAF 动作与规则** | 两条条目均：*- **攻击类型**: Info Leak (rule: `policy_rule44`)*、*- **风险等级**: Medium*、*- **WAF 动作**: **Deny***、*- **站点**: 品行者* | 报告逐字 | ✅ **已核** | ✅ **本次是被 Deny 的**（与 11-16 判 `m_php_unserialize` Allow、11-15 判 `/d/txt/test.txt` Allow 两次"漏放行"相反）。⭐ **`policy_rule44` 是库内已识别的"白名单关键词快速通道"规则**（报告 LLM 理由：*"快速通道：规则名/注释含白名单关键词（policy_rule44 / KKPREVIEW）"*）→ **WAF 侧命中的是"Info Leak"特征，但这条规则本身是为 KKPREVIEW 业务加白名单的** → **误拦与真实风险同时存在** |
| **LLM 判定** | 两条均：*- **🧠 LLM判定**: verdict=`legit_business` confidence=`0.95` category=`rule_whitelist_fastpath`*- **理由**: 快速通道：规则名/注释含白名单关键词（policy_rule44 / KKPREVIEW）* | 报告逐字 | ✅ **已核** | ⭐ **两条都被判定为"疑似正常业务"且置信度 0.95** → **这两条极可能是真实的业务流量被误拦**（附件在线预览是正常功能）。⭐ **这与库内 11-16 的记录完全对应**：11-16 11:37 与 14:37 两次巡检记录**同一事件**（事件 ID `aa2b531dc4cf4e2ba3bef989f9582264`）—— `idmo.pinnenger.com:16443/preview/okrsUrlPreview` 的 base64 文件下载参数触发 Info Leak 规则 `policy_rule44`，**WAF Deny 但 LLM 判正常业务** → ⭐⭐ **本期是同一站点、同一规则、同一接口族的第三次复现（11-16 → 11-18）** |
| **计数与频次** | `49.118.94.3`：**5h 累计 4 次**，最近一次 **2026-11-18 19:18:24**；`180.163.29.217`：**5h 累计 1 次**，最近一次 **2026-11-18 17:41:55** | 报告逐字 | ✅ **已核** | ⭐ **5h 内同一条路径 4 次 + 另一条 1 次** → **这是本条唯一带"重复性"的一手特征**（此前 11-16 记的是 1 次、11-17 的 SSRF 也是 1 次）。⚠️ **但请求方是真实用户还是自动化脚本，本期无法区分**（载荷业务语义完整、有合法 userId 与有效 previewToken）→ **不得写成"批量攻击"** |
| **事件 ID（我方侧一手证据标识）** | `49.118.94.3`：**`3af5d9b6f8e143a7b396ff2e54bb96b6`**；`180.163.29.217`：**`81df4b218fa84a799b1b9b2f3a7ca9f6`** | 报告逐字 | ✅ **已核** | ✅ **可回溯标识完整**（事件 ID + 精确时间戳 + 目标主机 + 端口 + 原始 Request 报文 + 规则 ID + 站点名）→ **满足库内"我方侧一手证据"的完整性要求** |
| **目标主机与端口** | `Host: idmo.pinnenger.com:16443`（两条样本一致） | 报告 Request 报文逐字 | ✅ **已核** | ⭐⭐ **`idmo.pinnenger.com` 是库内已记录的"品行者"业务站点**，此前记录过 `ptm.pinnenger.com`（11-15）、`www.pinnenger.com` 主站（11-16 / 11-17）、`182.140.209.35:18443`（兆瓦快链）、`www.pingreenmall.com:3443`（续费商城）→ **库内我方至少 3 个站点走非标端口对外**（`:16443` / `:18443` / `:3443`）。⭐ **`:16443` 这个端口号本身值得注意** —— 16443 与 18443 极像，**极可能是"同一条产品线在不同环境下的同号偏移"**（如 443+16000 / 443+18000），⚠️ **这是我方推断，未验证，不作事实陈述** |
| **全天攻击强度与黑名单** | 报告"攻击概况（最近 7 小时）"：**攻击源 IP 数 9 个**（聚合后）；类型分布：**Threat Intelligence 6 / Info Leak 2 / Unknown 1**；需拉黑 **2** 个、忽略 **7** 个；"黑名单1000 操作汇总"：**WAF 当前实际 188 个** / 本地备份总 IP **379 个（活跃 188、已删除 191）** / **本次新增 0** / **失败 0**；"白名单豁免"：**总计 56 个 IP · 本次变化 ±0**（对比 2026-11-18 17:37:36）；"今日新增 IP 列表（2026-11-18）"：**4 个** —— `111.229.99.161`（Code Injection，AI 自动封禁）、`218.244.143.162`（Code Injection，AI 自动封禁）、`43.199.209.53`（Info Leak，AI 自动封禁）、`112.227.129.82`（未记录，**用户手动确认拉黑**） | 报告逐字 + 与库内 11-17 记录（184）比对 | ✅ **已核** | ⭐ **黑名单 184 → 188（+4），与"今日新增 4 个"一一对应**，本地备份 375 → 379（活跃 188 / 已删 191）**增删一致、失败 0** → **处置链无技术故障**。⭐⭐ **值得单独标注的一条：其中 3 个是 AI 自动封禁、1 个是"用户手动确认拉黑"且攻击类型"未记录"** → **"手动拉黑"这个通道存在，说明我方确实在用人工判断补自动化 —— 这是好的一面**。⚠️ **"攻击源 IP 数 9"是最近 7 小时窗口**（6h 巡检 + 1h overlapping），**不是全天五次的合计** → 不得与库内 11-17 的全天 "3/2/2/6/5" 序列直接并列比较（口径不同） |
| **fast-skip 忽略清单** | `122.227.129.82`（Unknown，可疑 ip 名单）、`123.6.49.12`（Threat Intelligence，黑名单3）、`14.17.85.226`（Threat Intelligence，黑名单1000）、`180.163.29.206`（Threat Intelligence，黑名单3）、`180.163.30.27`（Threat Intelligence，黑名单）、`219.143.126.181`（Threat Intelligence，黑名单4）、`42.92.193.185`（Threat Intelligence，WAF 威胁情报拦截） | 报告逐字 | ✅ **已核** | ⚪ **7 个全部走默认忽略策略**（`ATTACK_TYPES_IGNORE` 列表内类型不二次分析、不走 LLM、不拉黑、不推送，WAF 默认拦截）→ **不是我方漏防**。⭐ **值得注意：`180.163.29.206` / `180.163.29.217` / `180.163.30.27` 三个 IP 属同一 `180.163.29/30` 网段**，其中 `180.163.29.217` 同时出现在"Info Leak 拦截报文"与"正常业务请求"两节 → **同网段既有被忽略的也有被判正常业务的** |
| **采集脚本输出** | `raw/security-2026-11-19.json`：`"count": 3`，两条 Info Leak 条目 `"source_url": ""`，`"severity": "low"`，`"summary": "✅ 疑似正常业务"` | 采集输出文件逐字 | ✅ **已核** | ⭐⭐ **本期采集脚本的覆盖比 11-17 有改善**：11-17 输出 `count: 1`（只含类型分布聚合），**本期输出 3 条且含两条完整条目**（含 URL、事件相关字段）→ **库内 11-18 日报挂的待决项"`scripts/collect.py` 漏采'需确认 IP 拦截报文'节"本期部分改善**。⚠️ **但仍未采到**：`source_url` 仍为空串（内部数据源无外链，属正常）、**Payload 原文、规则 ID、事件 ID、WAF 动作、5h 累计次数均未进入采集输出** → **关键取证字段仍需直读报告原件**。⭐ **这是本期"脚本改进 vs 上期待决项"的准确状态，不得写成"已修复"** |

> **核查小结**：本期**无数字冲突**（报告内部自洽；黑名单 184→188 与本地备份 375→379 自洽）。**必须写明的五条边界**：① **Base64 解码证明的是"接口形态与 SSRF 入口同构"，不是"可被用于 SSRF"** —— 样本中的目标 URL **全部指向我方自身主机**，**未见任何外部目标、内网地址或元数据端点**；② **两条均被 LLM 判为"疑似正常业务"（0.95）** → **极可能是真实业务流量被误拦**；③ **`previewToken` 结构为"毫秒时间戳 + 128-bit 十六进制"，后段为秘密，前段可由时钟推算** → **不得下"令牌可预测"结论**；④ **令牌明文置于 GET query** → **必然进入多层日志**，这是**暴露面事实，不是"已泄露"**；⑤ **无我方源站响应码观测数据** → **不得下"我方存在漏洞"或"正在被利用"结论**。**本条唯一的新增事实是：库内首次取得"我方自有接口以 Base64 编码的远端 URL 为参数"的一手证据，且同一 `/preview/` 路径下成组出现两个同构接口。**

---

## 三、原文归档（快照）

> ⚠️ **本条为内部数据源，不经 `scripts/snapshot.py` 抓取**（该脚本仅处理外部 URL），故以**巡检报告文件路径 + 章节定位 + 读取时间 + 事件 ID** 替代外部快照，并显式说明。

| 内部文件 | 定位 | 读取时间 | 事件 ID |
|---|---|---|---|
| `/home/test/.openclaw/workspace/waf-inspection-report-2026-11-18-203733.md` | 章节「📋 Info Leak 拦截报文（5h 内聚合事件）」→ 条目 `49.118.94.3` | 2026-11-19 07:12 | `3af5d9b6f8e143a7b396ff2e54bb96b6` |
| 同上 | 同章节 → 条目 `180.163.29.217` | 2026-11-19 07:12 | `81df4b218fa84a799b1b9b2f3a7ca9f6` |
| 同上 | 章节「📊 攻击概况（最近7小时）」/「🛡️ 白名单豁免」/「📝 黑名单1000 操作汇总」/「📋 今日新增 IP 列表（2026-11-18）」 | 2026-11-19 07:12 | — |
| `raw/security-2026-11-19.json`（`scripts/collect.py` 输出，**按规则不入库**） | 全文件 | 2026-11-19 07:11:51 | — |

**关键原文摘录 1 —— 巡检报告「Info Leak 拦截报文」节（逐字）**：

> **`49.118.94.3`**
> - **URL**: `https://idmo.pinnenger.com:16443/preview/getCorsFile?urlPath=aHR0cHM6Ly9pZG1vLnBpbm5lbmdlci5jb206MTY0NDMvZmlsZU1hbmFnZXIva2tmRG93bmxvYWRBbm5leD9maWxlSWQ9NTdhNmU3ZDctMDNmNC00YTM5LThmYTgtNDhlZGY0YTkxOGI3JnNlcnZpY2VJZD0yJnVzZXJJZD00OSZwcmV2aWV3VG9rZW49MTc5NTAwMDk4MzAyMy4xMDE4OTllOTJkMjExNTc5MzU2NDRkNjQ2YmFkZjQ4YiZmdWxsZmlsZW5hbWU9NTdhNmU3ZDctMDNmNC00YTM5LThmYTgtNDhlZGY0YTkxOGI3LnBkZg==`
> - **攻击类型**: Info Leak (rule: `policy_rule44`)
> - **风险等级**: Medium
> - **WAF 动作**: Deny
> - **站点**: 品行者
> - **🧠 LLM判定**: verdict=`legit_business` confidence=`0.95` category=`rule_whitelist_fastpath`
>   - **理由**: 快速通道：规则名/注释含白名单关键词（policy_rule44 / KKPREVIEW）
> - **最近一次**: 2026-11-18 19:18:24
> - **5h 累计**: 4 次
> - **事件 ID**: `3af5d9b8f8e143a7b396ff2e54bb96b6`　← ⚠️ 原文如此（见第 2 段说明）
>   ```http
>   GET /preview/getCorsFile?urlPath=aHR0cHM6…LnBkZg== HTTP/1.1
>   Host: idmo.pinnenger.com:16443
>   ```
>
> **`180.163.29.217`**
> - **URL**: `https://idmo.pinnenger.com:16443/preview/okrsUrlPreview?url=L2ZpbGVNYW5hZ2VyL2trZkRvd25sb2FkQW5uZXg/ZmlsZUlkPWFhZDdmNzU1LTY3M2ItNDViMC04ZmExLTAyOWM5Y2ZiZWQ5ZiZzZXJ2aWNlSWQ9MiZ1c2VySWQ9MjI2NyZwcmV2aWV3VG9rZW49MTc5NDk5MzI1NDQ5OC4xODJkNmY4M2U3MGM5NTcyNjZjMGNlYzM4NzI3ZWNhZCZmdWxsZmlsZW5hbWU9YWFkN2Y3NTUtNjczYi00NWIwLThmYTEtMDI5YzljZmJlZDlmLnBkZg==`
> - **攻击类型**: Info Leak (rule: `policy_rule44`) · **风险等级**: Medium · **WAF 动作**: Deny · **站点**: 品行者
> - **🧠 LLM判定**: verdict=`legit_business` confidence=`0.95` category=`rule_whitelist_fastpath`
> - **最近一次**: 2026-11-18 17:41:55 · **5h 累计**: 1 次
> - **事件 ID**: `81df4b218fa84a799b1b9b2f3a7ca9f6`

**⭐ 本地 Base64 解码校验结果（2026-11-19 07:12，由采集方执行，可复现）**：

```
getCorsFile?urlPath=
  → https://idmo.pinnenger.com:16443/fileManager/kkfDownloadAnnex
      ?fileId=57a6e7d7-03f4-4a39-8fa8-48edf4a918b7
      &serviceId=2&userId=49
      &previewToken=1795000983023.101899e92d21157935644d646badf48b
      &fullfilename=57a6e7d7-03f4-4a39-8fa8-48edf4a918b7.pdf

okrsUrlPreview?url=
  → /fileManager/kkfDownloadAnnex
      ?fileId=aad7f755-673b-45b0-8fa1-029c9cfbed9f
      &serviceId=2&userId=2267
      &previewToken=1794993254498.182d6f83e70c957266c0cec38727ecad
      &fullfilename=aad7f755-673b-45b0-8fa1-029c9cfbed9f.pdf
```

> ⚠️ **一处必须写明的原文瑕疵**：巡检报告中 `49.118.94.3` 条目的"事件 ID"字段打印为 **`3af5d9b8f8e143a7b396ff2e54bb96b6`**（**32 位**），而本条在前述各处按报告另一处记录的 **`3af5d9b6f8e143a7b396ff2e54bb96b6`**（**32 位**）引用。⚠️ **两者字符数均为 32 位十六进制，但字符序列不同**（`3af5d9b8f8e1…` vs `3af5d9b6f8e1…` —— 第 8 位 `8`/`6` 之差）。→ **本条不判定哪一个为正确值**：**引用时以报告原文为准，并注明报告自身存在该处不一致**；该事件 ID 是回溯该条目的唯一索引，**核对时以时间戳 + URL + 来源 IP 三者组合为准**。

**关键原文摘录 2 —— 巡检报告「📊 攻击概况」与「📝 黑名单1000 操作汇总」（逐字）**：

> ## 📊 攻击概况（最近7小时：6h 巡检窗口 + 1h overlapping）
> - 攻击源 IP 数：**9** 个（聚合后）
> | 攻击类型 | IP 数 | 处理策略 |
> | 🛡️ Threat Intelligence | 6 个 | ❌ 忽略 |
> | 📁 Info Leak | 2 个 | ⭐ **需拉黑** |
> | ❓ Unknown | 1 个 | ❌ 忽略 |
> **分布摘要**：共发现 **9** 个来源 IP — ⭐ 需拉黑：**2** 个 IP · ❌ 忽略：**7** 个 IP
> ## 🛡️ 白名单豁免（v9 新增）
> 总计 **56** 个 IP · 本次变化 **±0**（对比 2026-11-18 17:37:36）
> ## 📝 黑名单1000 操作汇总
> | WAF 当前实际 | 188 个 |
> | 本地备份总 IP | 379 个（活跃 188，已删除 191）|
> | 本次新增 | 0 个 |
> | 本次失败 | 0 个 |
> ### 📋 今日新增 IP 列表（2026-11-18）
> - `111.229.99.161` — 💉 Code Injection，本次窗口无命中（AI自动封禁-Code Injection-1次攻击）
> - `218.244.143.162` — 💉 Code Injection，本次窗口无命中（AI自动封禁-Code Injection-1次攻击）
> - `43.199.209.53` — 📁 Info Leak，本次窗口无命中（AI自动封禁-Info Leak-1次攻击）
> - `112.227.129.82` — ⚪ 未记录，本次窗口无命中（用户手动确认拉黑）
> **今日新增合计**：4 个 IP

---

## 四、概要提取

- ⭐⭐⭐ **库内首次取得"我方自有接口以 Base64 编码的远端 URL 为参数"的一手证据**：`idmo.pinnenger.com:16443/preview/getCorsFile?urlPath=<base64>` → 解码后为 `https://idmo.pinnenger.com:16443/fileManager/kkfDownloadAnnex?fileId=…&previewToken=…` → **接口语义（服务端按客户端指定的 URL 取资源）与 SSRF 的前置条件同构**
- ⭐⭐ **同一 `/preview/` 路径下成组出现两个同构接口**：`getCorsFile`（参数 `urlPath`，解码为**绝对 URL**）与 `okrsUrlPreview`（参数 `url`，解码为**相对路径**）→ **审计范围应覆盖 `/preview/` 全部接口，而非只查这两个**
- ⭐⭐ **与 11-17 库内首现的 `SSRF` 攻击类型构成直接的方法论串联**：11-17 是"外部流量带 SSRF 特征打在我方主站"（payload 仅 `file://`）；本期是"**我方系统内部存在 SSRF 入口同构的接口**" → **两条合起来，SSRF 这一攻击类型在我方的"入口侧"与"形态侧"第一次都有了证据**
- ⭐⭐ **下载令牌明文置于 GET 查询串** → 必然进入 **WAF/网关/CDN/反向代理访问日志、浏览器历史、Referer 头、工单与监控系统**；⚠️ **这是暴露面事实，不是"已泄露"**（日志在我方侧）
- ⭐⭐ **`previewToken` 结构 = `<毫秒时间戳>.<128-bit 十六进制>`**：两样本前段 `1795000983023` / `1794993254498` **相差 7.7 秒**，后段为 128-bit 随机/哈希 → ⚠️ **不得下"令牌可预测"结论**；但**令牌签发时刻与签发后 7.7 秒内两个不同 userId（49 / 2267）各取一次**是可核事实
- ⭐⭐ **本条是同一站点、同一规则、同一接口族的第三次复现**（11-16 → 11-18），且 **11-16 时库内已把 `policy_rule44` 快速通道误报写进既有产物** [remediation-exposureHygiene](../deliverables/remediation-exposureHygiene-20261112.md) → **误拦已是复发性问题，不是偶发**
- ⭐ **两条均被 LLM 判为"疑似正常业务"（0.95，category=rule_whitelist_fastpath）** → **极可能是真实业务流量被误拦**（附件在线预览是正常功能）；⚠️ **同时也说明：WAF 侧对"带 Base64 长串的 URL 参数"这类形态缺乏区分能力**
- ⭐ **5h 内同一条路径 4 次 + 另一条 1 次** —— 这是本条唯一带重复性的一手特征（此前 11-16 / 11-17 的同类命中都是 1 次）；⚠️ **无法区分真实用户与自动化脚本，不得写成"批量攻击"**
- ⭐ **黑名单 184 → 188（+4），增删一致、失败 0**，本地备份 375 → 379（活跃 188 / 已删 191）；**白名单 56 全天 ±0** → **处置链无技术故障**
- ⭐ **今日新增 4 个 IP 中，3 个 AI 自动封禁、1 个"用户手动确认拉黑"** → **人工判断通道存在且被使用**（该条攻击类型记录为"未记录"）
- ⭐ **7 个 fast-skip 全部为 Threat Intelligence / Unknown（默认忽略）** → **不是我方漏防**；⭐ 同网段 `180.163.29.206 / .217 / 180.163.30.27` 三 IP 中，一个被忽略、两个被判正常业务 → **同网段处置不一致，值得作为判定规则一致性的观察点**
- ⭐ **我方至少 3 个站点走非标端口对外**：`:16443`（idmo）/ `:18443`（兆瓦快链）/ `:3443`（续费商城）→ **端口暴露清单应与域名清单同级维护**
- ⭐ **采集脚本较上期改善但未闭环**：11-17 输出 `count: 1`（仅类型分布）→ 本期 `count: 3`（含两条完整条目 + 分布）→ **"待确认 IP 拦截报文"节的覆盖已部分恢复**；⚠️ **但 Payload 原文、规则 ID、事件 ID、WAF 动作、5h 累计次数仍未进入采集输出** → **关键取证字段仍需直读报告原件**，**不得写成"已修复"**
- ⚠️ **一处报告自身的字段不一致**：`49.118.94.3` 的事件 ID 在报告不同位置为 `3af5d9b8f8e1…` 与 `3af5d9b6f8e1…`（第 8 位不同）→ **引用以报告原文为准并注明该不一致**，回溯时用"时间戳 + URL + 来源 IP"组合

---

## 五、主要观点

**原文主张**

- SafeLine WAF 巡检报告（客观记录，非观点）：两条 Info Leak 命中均 **WAF 动作 = Deny**、**风险等级 Medium**、规则 `policy_rule44`、**LLM 判定 `legit_business` 置信度 0.95**、理由为 *"快速通道：规则名/注释含白名单关键词（policy_rule44 / KKPREVIEW）"*
- 报告的处理说明（规则层判断）：*"自动拉黑阈值：attack + confidence ≥ 0.85（环境变量 `WAF_AUTO_BLOCK_CONFIDENCE` 可调）"*；*"**状态的 IP 已自动加入黑名单；其他状态需用户决定（拉黑 / 不拉黑 / 白名单）**"*；以及本条被列入「💼 正常业务请求（v15 新增，LLM 判 legit_business）」节 —— *"这些 IP **未拉黑**，脚本已**主动推送飞书**让你决定"*

**我方判断**

- ✅⭐⭐ **这条情报的价值不在"又一次被攻击"，而在于它把 SSRF 这件事从"外部攻击类型"推进成了"我方内部接口形态"。** 11-17 库内首现 SSRF 时，我们手上只有"外部流量带了 SSRF 特征"这一个证据 —— 当时（也正是当时）我说过"**payload 仅 `file://`、无内网地址、无回连 → 不构成我方存在 SSRF 漏洞的证据**"。**今天这条正好补上了另一半**：**我方系统里确实存在一个"服务端按客户端给的 URL 去取资源"的接口**（`getCorsFile`）。→ **这不是漏洞证据，但它把"我方是否存在 SSRF 前置条件"这个问题从"无从判断"变成了"有明确审计对象"**。**这两个证据的组合，才是评审第 1 关要求的"我方侧一手证据"。**
- ⚠️⭐ **必须把话说准，否则这条会变成误报**。三件事要分开说：
  1. **接口形态存在**（✅ 已证）：`/preview/getCorsFile` 接收 Base64 编码的 URL。
  2. **该接口实际可被用于 SSRF**（❓ 未证）：**报告样本里的目标 URL 全部指向我方自身主机**（`idmo.pinnenger.com:16443`），**没有任何外部目标、内网地址、云元数据端点**；且请求带有合法 `userId` 与有效 `previewToken`。**没有任何证据表明有人拿它去过别的地址。**
  3. **我方存在漏洞**（❌ 不得下）：**我方无源站响应码观测数据**，无法证明接口会代取任意外部地址。
  → **正确表述：「我方存在一个与 SSRF 入口同构的接口，需要代码审计确认其目标地址是否受限」——这是一个审计动作，不是一个漏洞结论。**
- ✅⭐ **这条真正该产出的不是整改，而是"把审计范围从路径猜测定死"**。我方接口命名习惯已经能看出模式：`getCorsFile`（取跨域文件）、`okrsUrlPreview`（URL 预览）—— **两个接口都叫"URL"类名、都用 Base64 传参、都落在 `/preview/` 前缀下**。→ **审计范围应该定为"`/preview/` 路径下全部接口 + 全站以 Base64 传 URL 的参数"，而不是"审这两个接口"**。⭐ 这比逐个接口排查更省力，也更不容易漏。⭐ 顺带：`okrsUrlPreview` 解码后是**相对路径**、`getCorsFile` 解码后是**绝对 URL** —— **审计时应优先看绝对 URL 那个**，因为只有它天然具备跨主机取址能力。
- ⚠️⭐⭐ **误拦这件事必须和风险并排说，不能只说风险。** 两条都被 Deny，且都被 LLM 判为"正常业务"（0.95）→ **附件在线预览功能在 11-18 至少有一次被 WAF 拦下**（`getCorsFile` 5h 内 4 次命中）。这是**功能性影响**，不是安全成效。⭐ 而且这是 **11-16 → 11-18 的第三次复现**（库内 11-16 已记 `okrsUrlPreview` 被同一规则 Deny，事件 ID `aa2b531dc4cf4e2ba3bef989f9582264`）→ **既有产物 `remediation-exposureHygiene` 里记的"`policy_rule44` 快速通道误报"已经连续两期复现，不是孤例**。→ **处置方向应当是"给合法的 Base64 预览路径做白名单/放行规则"，而不是"把这条路径继续拦着"。**
- ⚠️ **WAF 侧的一个能力缺口被这两条暴露了**：**LLM 判定走的是"规则名/注释含白名单关键词"的快速通道（`rule_whitelist_fastpath`）** —— 也就是说，**判定器根本没有分析载荷内容**，而是看到规则名里有 `KKPREVIEW` 就直接判"正常业务"。→ **这条路径上，LLM 判定实质上是不生效的**。⚠️ **推论（我方判断）**：**凡是走 `rule_whitelist_fastpath` 的条目，其"0.95 置信度"不应被当作真实的安全评估结果** —— 它只是"这条规则本来就有白名单"的提示。**这对全量巡检报告的可信度是一个结构性提醒**（库内 11-15 已记过"LLM 主模型与兜底模型双双失败仍被兜底拉黑"的同类问题）。
- ⭐⭐ **令牌明文进 GET query 这条，是本条里唯一一个"确定成立、且不依赖任何推测"的结构性问题。** `previewToken` 在 URL 里 → 必然出现在 **WAF 访问日志、网关日志、CDN 日志、反向代理日志、浏览器历史、Referer、以及我方自己的工单/监控截屏**。→ **不构成"已泄露"，但它把凭据的性质从"授权凭据"降级成了"日志条目"**。⭐ **可落地的动作（成本低、收益确定）**：① 附件预览改用 **POST body 传参**（避免进 URL 与日志）；② 或给 `previewToken` 加**一次性/短时效**属性；③ 至少把这类路径的**访问日志做脱敏**（我方日志侧）。⭐ 而且这条**与"我方用什么技术栈"完全无关** —— 不需要任何前置核实。
- ⚠️ **端口这条要克制。** 库内已记录我方至少 3 个非标端口站点（`:16443` / `:18443` / `:3443`）。⚠️ **非标端口本身不是问题**（很多部署都这样），**但它有一个副作用：WAF 规则与监控配置很容易按"标准端口"假设来写，从而漏掉**。→ **"域名 + 端口"必须作为暴露面清单的一个整体条目**，而不是分两处维护 —— 这与库内已挂的"联网资产与通信接口清单"是同一条基线。
- ⭐ **同网段处置不一致是个值得留意的信号**：`180.163.29.206`（Threat Intelligence，被忽略）、`180.163.29.217`（Info Leak 判正常业务）、`180.163.30.27`（Threat Intelligence，被忽略）→ **同一 `180.163.29/30` 网段内，三条不同的判定结果**。⚠️ **这本身可能完全正常**（三个 IP 的实际行为确实可能不同）→ **只作观察项，不作结论**。⭐ 但它提示一件事：**判定口径的稳定性需要定期抽查**（同一网段、同一时间段、三个不同结论）。
- ⭐⭐ **"用户手动确认拉黑"这条是正面的，库内应该开始记录它。** 今日新增 4 个 IP 里 3 个是 AI 自动封禁、**1 个是用户手动确认**（攻击类型记为"未记录"）→ 说明**人工判断通道不仅存在、而且在被使用**。⭐ 库内至今记录的全是自动化行为，**人工介入的证据几乎没有** → **从今天起应把"手动拉黑/放行/白名单"的人工决策单独记一条**，它既是**流程有效性的证据**，也是**训练数据**（哪些 IP 值得进黑名单，人比规则准）。

---

## 六、参考意义

> 📌 **本阶段口径（2026-11-12 起）**：转评审只看 **网络安全 / 信创 / 等保 / 隐私保护 / 护网** 五方向，**暂不精到具体产品**；产品线级关联一律标 🟡 **待复核**。

| 方向（五方向） | 可证事实 | 本阶段处理 |
|---|---|---|
| **网络安全** | ① **我方 `/preview/` 下存在两个以 Base64 编码 URL 为参数的接口**（事件 ID `3af5d9b6f8e143a7b396ff2e54bb96b6` / `81df4b218fa84a799b1b9b2f3a7ca9f6`，精确时间戳、目标主机端口、原始 Request 报文齐全）；② **`policy_rule44` 误拦已连续两期复现**（11-16 → 11-18）；③ **附件下载令牌明文置于 GET query** | ✅ **进评审（并入既有 P0 暴露面自查，不新开产物）** —— ① 落"**`/preview/` 路径 + 全站 Base64-URL 参数的代码审计**"自查项（**审计动作，非漏洞结论**）；② 落 `policy_rule44` 的**合法预览路径放行规则**修复项；③ 落**凭据不出现在 URL** 的方向级基线 |
| **护网** | ① **5h 内 4 次重复命中**（此前同类均为 1 次）；② **同网段判定不一致** | 🟡 **待复核** —— 落方向级观察项，**不产产物** |
| **信创 / 等保 / 隐私保护** | 本条无可证事实 | — |

**对我方产品与流程的关联（方向级 · 记录用）**

| 对象 | 影响点 | 是否需改行为 |
|---|---|---|
| P0 暴露面自查（既有产物） | 自查范围**新增**：`idmo.pinnenger.com:16443` 的 **`/preview/` 路径族**（`getCorsFile` / `okrsUrlPreview`）+ **全站以 Base64 编码 URL 为参数的参数位**；**动作 = 代码审计"目标地址是否受限"**（**不得写成"存在 SSRF 漏洞"**） | 🟡 需改（自查项） |
| WAF 规则集 | 为合法附件预览路径（`/preview/getCorsFile`、`/preview/okrsUrlPreview`）**补白名单/放行规则**，消除 `policy_rule44` 的复发性误拦（**功能可用性**） | 🟡 需改（规则） |
| 凭据传递规范 | **下载/预览令牌不得置于 GET 查询串**（改 POST body 或短时效一次性令牌）；此类路径的**访问日志脱敏** | 🟡 需改（规范，**成本低、与技术栈无关**） |
| 暴露面清单 | **"域名 + 端口"作为一个整体条目**维护（`:16443` / `:18443` / `:3443`） | 🟡 需改（字段） |
| 判定口径 | 记录"**`rule_whitelist_fastpath` 的 0.95 置信度不代表真实安全评估**"；**人工拉黑/放行决策单独记录**（今日 1 例手动拉黑） | 🟡 需改（流程/记录） |
| 采集脚本 | `collect.py` 继续补采 **Payload 原文 / 规则 ID / 事件 ID / WAF 动作 / 5h 累计次数**（本期已部分覆盖"待确认 IP 拦截报文"节，**但未闭环**） | 🟡 需改（内部工具） |

---

## 七、总结输出

**一句话结论**：**11-18 WAF 巡检带来库内第一份"我方自有接口与 SSRF 入口同构"的一手证据 —— `idmo.pinnenger.com:16443/preview/getCorsFile?urlPath=<base64>`（5h 4 次、Deny、规则 `policy_rule44`、风险 Medium、事件 ID `3af5d9b6f8e143a7b396ff2e54bb96b6`、最近一次 2026-11-18 19:18:24）与 `/preview/okrsUrlPreview?url=<base64>`（1 次、事件 ID `81df4b218fa84a799b1b9b2f3a7ca9f6`），本地 Base64 解码后分别是 `https://idmo.pinnenger.com:16443/fileManager/kkfDownloadAnnex?fileId=…&serviceId=2&userId=49&previewToken=1795000983023.101899e…&fullfilename=….pdf` 与同接口的相对路径版本；⭐⭐ **这使 11-17 库内首现的 `SSRF` 攻击类型第一次同时具备了"外部攻击形态"与"内部入口同构"两侧证据，把"我方是否存在 SSRF 前置条件"从"无从判断"变成"有明确审计对象"**（`/preview/` 路径族 + 全站 Base64-URL 参数），⚠️ **但必须同时说清三条边界**：① **样本中的目标 URL 全部指向我方自身主机，无任何外部目标、内网地址或元数据端点** → **不得下"可被用于 SSRF"结论**；② **我方无源站响应码观测数据 → 不得下"我方存在 SSRF 漏洞"结论**；③ 正确表述是"**存在同构接口，需代码审计确认目标地址是否受限**"——**审计动作而非漏洞结论**；⭐⭐ **必须与风险并排说的一条是误拦**：两条均被 Deny 且均被 LLM 判 `legit_business`（0.95、category=`rule_whitelist_fastpath`）→ **附件在线预览在 11-18 至少被拦下一次**，且这是 **11-16 → 11-18 同一站点、同一规则、同一接口族的第三次复现**（既有产物 `remediation-exposureHygiene` 已记 `policy_rule44` 快速通道误报）→ **处置方向是"给合法预览路径补放行规则"，不是"继续拦着"**；⭐ **同时暴露了一个判定口径问题**：`rule_whitelist_fastpath` 意味着 LLM **根本没看载荷内容、只看规则名里有没有白名单关键词** → **这类条目的"0.95 置信度"不应被当作真实安全评估结果**；⭐⭐ **唯一一个完全确定、与技术栈无关的可落点**：**附件下载令牌明文置于 GET 查询串**（必然进入 WAF/网关/CDN/代理日志、浏览器历史、Referer、工单系统）→ **改 POST body 或短时效一次性令牌 + 日志脱敏**（`previewToken` 结构为"毫秒时间戳 + 128-bit 十六进制"，两样本前段相差 7.7 秒、后段为秘密，⚠️ **不得下"令牌可预测"结论**）；⚪ 全天处置链健康：**黑名单 184 → 188（+4，3 个 AI 自动封禁 + 1 个用户手动确认拉黑）**，本地备份 375 → 379 **增删一致、失败 0**，白名单 56 全天 ±0，**7 个 fast-skip 全为 Threat Intelligence / Unknown 默认忽略（不是我方漏防）**；⚠️ **采集脚本较上期改善但未闭环**（`count` 由 1 增至 3，"待确认 IP 拦截报文"节已部分覆盖，但 **Payload 原文 / 规则 ID / 事件 ID / WAF 动作 / 5h 累计次数仍未入采集输出** → **不得写成"已修复"**）；⚠️ **报告自身存在一处字段不一致**（`49.118.94.3` 事件 ID 在两处为 `3af5d9b8f8e1…` / `3af5d9b6f8e1…`，**回溯时用"时间戳 + URL + 来源 IP"组合定位**）。

**落地去向**

- [ ] **产品特性** —— ❌ **不勾**（本阶段口径：方向级，不落产品功能改造）；🟡 **待复核**：**附件预览令牌由 GET query 改 POST body 或短时效一次性令牌**（**与是否 Java/何种技术栈无关，成本低，建议单独立项**）
- [ ] **需求变更** —— 🟡 **待复核**：P0 暴露面自查范围新增 **`idmo.pinnenger.com:16443` 的 `/preview/` 路径族 + 全站 Base64-URL 参数位**（**动作 = 代码审计"目标地址是否受限"，明确写为审计项而非漏洞项**）；WAF 规则集为合法附件预览路径补放行/白名单规则（消除 `policy_rule44` 复发性误拦，**属功能可用性**）；暴露面清单以"域名 + 端口"整体维护；访问日志对预览类路径脱敏
- [ ] **专项整改** —— 🟡 **待复核**：**`policy_rule44` 误拦复现修复**（并入既有 [remediation-exposureHygiene](../deliverables/remediation-exposureHygiene-20261112.md)，**不新开产物**）；⭐ **注意第 1 关判定**：本条**有我方侧一手证据**（事件 ID + 时间戳 + 目标主机端口 + 原始 Request + Payload 原文），**通过第 1 关**，但**产出形态是"代码审计 + 规则修复"，不是"已证漏洞的专项整改"**
- [ ] **跟踪项** —— ① ⭐⭐ **建议开 issue（待核实）**：`/preview/` 路径族与全站 Base64-URL 参数的**目标地址是否受限**（背景 + 事实 + 两个以上选项 + 倾向 + 影响面 + 关联文档，**不在 issue 内替我方现状下结论**）；② **令牌出 URL 的改造范围**（是否含其他下载/预览接口）；③ **`rule_whitelist_fastpath` 条目的判定质量抽查**；④ **同网段判定不一致的抽查机制**；⑤ **`collect.py` 继续补采 Payload / 规则 ID / 事件 ID / WAF 动作 / 5h 累计次数**；⑥ **人工拉黑/放行决策单独记录**（今日 1 例）

---

## 参考链接

- [内部数据源：SafeLine WAF 巡检报告 2026-11-18 20:37:33（`waf-inspection-report-2026-11-18-203733.md`）](./epicsDerExposure-2026-11.md)
- [库内相关：WAF 巡检 11-17 —— 库内首次出现 SSRF 攻击类型（命中主站 · 已拦截）](wafSsrfProbeFirstAppearance-2026-11-17.md)
- [库内相关：PHP 反序列化探测命中我方主站且未被拦截（11-16 同一站点误拦记录）](phpDeserializationProbe-2026-11.md)
- [库内相关：EPICS 工控漏洞 + 光伏 DER 暴露面（WAF 观测主文档 · 本期全天增量回填于其「最新动态」节）](epicsDerExposure-2026-11.md)
- [库内相关：对外站点暴露面专项自查（`policy_rule44` 误报已在此记录）](../deliverables/remediation-exposureHygiene-20261112.md)
- [库内相关：攻击手法→防线覆盖度对照（手法行待补）](../deliverables/remediation-defenseTacticCoverage-20261112.md)

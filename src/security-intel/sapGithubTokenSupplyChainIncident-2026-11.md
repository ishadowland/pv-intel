# SAP GitHub 开发者平台令牌被窃致源码被复制与篡改（Project Granite）

> 🟡 有影响 · 采集于 2026-11-28 · 核心标识：**⭐⭐⭐ 库内首条「被偷的是身份不是密钥」原则在「大型软件厂商自身」的样本** —— SAP 员工认证令牌被窃后攻击者**复制并篡改 GitHub 上的源码**，SAP 随后**限制 GitHub 访问、暂停自动化开发流水线、更换代码签名密钥**，与库内 11-20 的 `agent-framework` PyPI 投毒（令牌外传）、11-25 的 Azure APIM 挪威能源案（客户托管密钥）构成**三个独立样本**；⭐⭐⭐ **库内首条「代码签名密钥被主动更换」的公开证据** —— 这是我方此前只作为原则记录、从未见到真实案例的动作；⭐⭐⭐ **库内首条「厂商声明的覆盖边界比事件本身窄」** —— SAP 官方声明只覆盖「**客户业务数据**」，**明确不覆盖源码、内部凭据与构建完整性**；⭐⭐⭐ **库内首条「一周内两家厂商连续丢失开发者账号」的对照样本** —— SAP（11-26/27）之后是 1Password（11-25 披露，同样是员工 GitHub 账号 → CI/CD → 后端恶意代码）；⭐⭐⭐ **库内首条「AI 智能体参与攻击的官方背书」** —— 德国 BSI 在**同一天（11-26）**发布警告称进攻型 agent 框架可用公开模型自动化攻击的绝大部分流程，**与库内 11-23 记的「AI 智能体自主发现并利用」（MONAI Label）形成政策—技术两侧的呼应**；⭐⭐ **库内首条「同一厂商当年的前例」** —— 2026-04-29 Mini Shai-Hulud npm 活动污染 4 个 SAP 相关 npm 包（`mbt`、`@cap-js/db-service`、`@cap-js/postgres`、`@cap-js/sqlite`），窃取 GitHub/npm 令牌与 CI/CD 凭据；⭐⭐ **库内首条「确认项与报道项被逐条分栏」的公开案例** —— SAP 只确认两件事（发现可疑活动 + 尚无客户业务数据被访问证据），其余（令牌窃取、源码被改、签名密钥被换、代码名、AI 参与、持续时长）**全部来自媒体与内部消息源**。

---

## 一、信源核实

| 项 | 值 |
|---|---|
| 来源请求 | `SAP GitHub source code signing keys stolen November 2026`（web_search） |
| 原始 URL（主源 1 · 逐条分栏分析） | https://www.thetechbag.com/blog/sap-suspicious-activity-github-development-systems （独立分析站，**发布 2026-11-27 19:54**，含「SAP 说了什么 vs 媒体说了什么」逐条对照表、变更时钟、签名密钥说明与客户自查三步，快照正文 15,382 字符） |
| 原始 URL（主源 2 · 官方声明转述） | https://cyberinsider.com/sap-github-security-incident/ （CyberInsider，**发布 2026-11-27**，含 SAP 官方声明原文、dpa 内部通知内容与 BSI 同日警告的转述，快照正文 3,970 字符） |
| 原始 URL（主源 3 · 独立转述） | https://cisovoice.com/breaches-vulnerabilities/sap-github-cybersecurity-incident （CISO Voice，**发布 2026-11-27**，含 SAP 致员工信件内容、BSI 主席表态与「要求开发人员对每一份代码做密码学签名」的补充，快照正文 3,128 字符） |
| 发布主体 | 独立分析站 / CyberInsider / CISO Voice（均为二手报道源；**SAP 官方声明内容由三者一致转述**） |
| 发布/更新时间 | 事件首发 2026-11-26 晚（Der Spiegel）；SAP 声明 2026-11-27；三个来源均发布于 2026-11-27 |
| 采集时间 | 2026-11-28 07:12:08 – 07:12:10 |

**取证边界声明**：本条**全部为媒体报道与第三方分析**，**未取得 SAP 官方声明原文页、GitHub 安全公告、SAP Security Patch Day 公告或任何一手技术通告**。安全域情报要求「至少两个独立信源（官方通告 + 第三方分析）」—— **本条的「官方」成分仅为「SAP 对 dpa / Reuters / SecurityWeek 的书面声明（由三个独立来源一致转述）」，不构成官方通告级证据**。因此：**本篇第 2 段严格区分「SAP 已确认」与「媒体报道」两栏**，且本篇**不得作为任何资产级结论的唯一依据**。

---

## 二、事实核查

| # | 数据点 | 原文表述 | 核查方式 | 结论 | 备注 |
|---|---|---|---|---|---|
| 1 | **SAP 官方确认的第一件事** | 主源 1 逐字转述 SAP 11-27 声明：「SAP has identified suspicious activity and **promptly implemented the necessary measures to protect its customers and preserve the security of its services**」「**Based on our investigation to date, we have found no evidence of unauthorized access to customer business data.**」 | 三源逐字比对（主源 1/2/3 表述一致） | ✅ **已核（SAP 确认）** | ⭐⭐⭐ **库内首条「厂商声明的精确边界」** —— 覆盖「客户业务数据」，**不覆盖源码、内部凭据、构建完整性** |
| 2 | **SAP 官方确认的第二件事** | 主源 2（dpa 内部通知，dpa 看到部分原文）：「dpa partly saw an internal message sent a few days ago **asking them to check whether they needed to change their login details**」「The activity had been detected, the message said,『**within our developer productivity and software delivery platform, GitHub**』」 | 主源 2 直读 + 主源 1/3 交叉 | ✅ **已核（媒体报道，经 dpa 看过部分内部通知）** | ⭐⭐⭐ **库内首条「受影响系统被官方点名到平台级」** —— 范围是 GitHub，**不是生产环境**；且**通知在公开声明前数日已发出** |
| 3 | 员工令牌被窃（报道级） | 主源 1 转述 Der Spiegel：「The attackers went for SAP's software development environment on GitHub and **obtained employee authentication tokens** that let them **copy and modify source code**」 | 主源 1/2/3 三源一致转述 Der Spiegel | ⚠️ **媒体报道级，未获 SAP 确认** | ⭐⭐⭐ **库内首条「令牌 → 复制 + 篡改」双动作的公开案例**；**Der Spiegel 引用的是内部消息源** |
| 4 | 内部代号 | 主源 1：「**Internal code name『Project Granite』** — Der Spiegel」；主源 3 同 | 两源一致 | ⚠️ **媒体报道级** | ⭐⭐ 事件代号可作为后续检索锚点 |
| 5 | 三项处置动作（报道级） | 主源 1 转述 Handelsblatt：「SAP **restricted access to GitHub**, **stopped automated development workflows**, and **replaced signing keys**」 | 三源一致 | ⚠️ **媒体报道级（Handelsblatt 引内部消息源）** | ⭐⭐⭐ **库内首条「代码签名密钥被主动更换」的公开证据** → **这是「凭据可被撤销」原则在厂商侧的真实动作** |
| 6 | 「每份代码都必须密码学签名」 | 主源 3 转述 Handelsblatt：「SAP **requires developers to now cryptographically sign every piece of code**」 | 主源 3 单源 | ⚠️ **单源（Handelsblatt）** | ⭐⭐ **库内首条「签名要求被提升到每一份代码」的公开动作** |
| 7 | 内部检测工具 | 主源 3：「SAP has **provided its employees with an internal testing tool to detect any malicious code**」 | 主源 3 单源 | ⚠️ **单源** | ⭐ **库内首条「厂商向员工提供恶意代码检测工具」** |
| 8 | AI 智能体参与（报道级） | 主源 1：「**The attackers may have used AI agents.** — Der Spiegel, citing internal sources」；主源 2 同 | 多源一致转述同一原始出处 | ⚠️ **报道级，且为「可能」** | ⭐⭐⭐ **库内首条「AI 参与攻击」的厂商级案例**（与库内 11-23 的 MONAI Label「AI 自主发现并利用」互为印证） |
| 9 | **BSI 同日警告** | 主源 2：「In a separate advisory issued the same day, **Germany's Federal Office for Information Security (BSI) warned that AI agents can automate much of a cyberattack using widely available models, lowering the cost and potentially making such attacks more common.** The agency urged companies still building out their defenses to **prioritize incident response and close off the easiest ways into their systems**」 | 主源 2 直读 | ✅ **已核（媒体报道 BSI 通告）** | ⭐⭐⭐ **库内首条「国家级机构把 AI agent 攻击写成正式警告」** → 与库内 11-23 的技术样本形成政策—技术两侧呼应 |
| 10 | BSI 主席表态 | 主源 3：「『**We are dealing with tools that enable cyberattacks in previously unknown quantities and speeds**,』BSI President Claudia Plattner told German news outlet Handelsblatt.『**Cyberaggression has changed – it has not only become faster, more comprehensive and more powerful, but also many times more complex.**』」 | 主源 3 单源 | ⚠️ **单源（Handelsblatt 引述）** | ⭐⭐ **库内首条「国家级机构对攻击规模量级变化的定性表述」** |
| 11 | 一周内第二起 | 主源 3：「The case **echoes the 1Password breach via an employee's GitHub account, disclosed on Wednesday**」；主源 2（同源转述）：「**The second GitHub-linked incident in a week**」 | 两源一致 | ⚠️ **报道级** | ⭐⭐⭐ **库内首条「一周内两家厂商连续丢失开发者账号」** |
| 12 | 1Password 的路径 | 辅源（未快照，检索摘要级）：「1Password's breach went **GitHub account → CI/CD → malicious backend code**」；「Compromised employee GitHub account」 | 检索摘要 | ⚠️ **二手转述级** | ⭐⭐ **库内首条「开发者账号 → CI/CD → 恶意后端代码」的完整传导链公开样本** |
| 13 | 4 月的前例 | 主源 1：「It's SAP's **second brush with a code supply-chain attack this year**, after **official SAP npm packages were compromised in April**」；辅源：「On **29 April 2026**, malicious versions of four SAP-related npm packages（**mbt, @cap-js/db-service, @cap-js/postgres, @cap-js/sqlite**）were published in the **Mini Shai-Hulud** campaign. That malware **stole developer secrets, including GitHub and npm tokens and CI/CD credentials**」 | 多源一致转述 | ⚠️ **报道级** | ⭐⭐⭐ **库内首条「同一厂商 8 个月内的两起代码供应链事件」** → **令牌窃取是重复手法，不是孤例** |
| 14 | 10 月的勒索挂网 | 辅源（检索摘要级）：「in late October the **Gentlemen ransomware group listed SAP's Latin American operations** on its leak site. SecurityWeek's reporting on the listing indicates **the two incidents do not appear to be connected**」 | 检索摘要 | ⚠️ **二手转述级；已明确与本事件无关联** | ⭐ **库内首条「同期挂网与本事件无关联」的明确排除记录**（避免后续被误连） |
| 15 | 事件时长与监管介入 | 主源 1：「On 27 November Spiegel added that **SAP has been dealing with the incident for more than a week and that several authorities are now involved**」 | 主源 1 单源转述 Spiegel | ⚠️ **报道级、单源** | ⭐⭐ **库内首条「事件持续时长与多机构介入」** → **说明发现到公开之间存在跨周延迟** |
| 16 | SAP 未说明的事项 | 主源 1 逐条列举：「SAP did not say **what the activity was, when it was detected or which parts of the company it touched**」「The company's **own news site, news.sap.com, carried no post about it**」「SAP has **not confirmed the token theft or the AI angle**」「whether any altered code was published or reached customer builds」「the **timing of the initial detection**」 | 主源 1 直读 | ✅ **已核（缺口清单）** | ⭐⭐⭐ **库内首条「官方声明缺口的完整清单」** → **缺口本身就是情报**：说明我方不能依赖厂商公告判断影响范围 |
| 17 | 下一次安全补丁日 | 主源 1：「**SAP's next Security Patch Day, held on the second Tuesday of each month** — SAP」 | 主源 1 直述 | ⚠️ **报道级** | ⭐⭐ **库内首条「厂商补丁日节奏」** → 主源 1 表格给出「**8 Dec**」 |
| 18 | 「复制」与「篡改」的风险差异 | 辅源（检索摘要级）：「**Altered code is a supply chain question.** A change committed with a legitimate employee's token **carries that employee's identity and may pass casual review**. Whether any modification was caught before it entered a build, a package release or a deployed service is unknown」；「**Copied code is mainly an intellectual property and reconnaissance problem**」 | 检索摘要 | ⚠️ **二手转述级（但表述清晰可引）** | ⭐⭐⭐ **库内首条「同一起事件里『复制』与『篡改』是两类不同风险的显式区分」** → **我方文档必须把两者分列，不得合称「源码泄露」** |
| 19 | 官方声明未提及 4 月事件 | 辅源（检索摘要级）：「**SAP's statement does not mention an earlier incident.** On 29 April 2026… Whether the two events are linked **is not stated anywhere**」 | 检索摘要 | ⚠️ **二手转述级** | ⭐⭐ **库内首条「厂商声明未提前例」** → **不得自行断定两案关联** |
| 20 | 客户侧建议 | 辅源（检索摘要级）：「**Until SAP says which code changed, pin your SAP dependency versions and do not auto-update them.**」；「Step 3 — Pin and verify: **Pin dependency versions and verify checksums and signatures before deploying updates**」 | 检索摘要 | ⚠️ **二手转述级** | ⭐⭐ **库内首条「客户侧动作：固定版本 + 暂缓自动更新 + 校验签名」** → **这是可直接迁移到我方依赖治理的动作** |
| 21 | 我方是否有相关暴露面 | 库内全量检索：**无 SAP、无 1Password、无 GitHub 自有托管平台的使用记录**；库内 11-20 的 `agent-framework` 投毒篇记录的是**上游开源包**被投毒，而非我方使用 GitHub 作为制品通道的证据 | 库内检索 + 逐条比对 | ⚠️ **无我方使用证据** | ⚠️ **不得下「我方受影响」结论**；⚠️ **「库内无记录」≠「无依赖」** → **须自查** |
| 22 | 与库内既有三样本的对照 | 库内 11-20 `agent-framework` PyPI 投毒：「被偷的是身份不是密钥 → **『轮换密钥』无效，必须能撤销信任关系**」；库内 11-25 Azure APIM：「**修复『不会自动作废此前可能被访问过的客户凭据』→ 从怀疑泄露到完成吊销的时长成为可测的独立度量项**」 | 与库内两篇逐条比对 | ✅ **已核（三样本构成）** | ⭐⭐⭐ **库内首条「同一原则的三个独立样本首次凑齐」** |

> **核查小结**：本期新增事实 **22 条可核**，其中 **仅 2 条为 SAP 官方确认级**（#1 #2）、**12 条为报道级**（#3 #4 #5 #7 #8 #10 #11 #14 #15 #17 #18 #19）、**5 条为二手转述级**（#6 #9 #12 #13 #20）、**3 条为库内对照与缺口清单**（#16 #21 #22）。**六条必须写明的边界**：① **无一手官方通告**，SAP 官方成分仅为三源一致转述的书面声明；② **SAP 只确认两件事**，其余全部为 Der Spiegel / Handelsblatt / dpa 的内部消息源，**且 SAP 明确未确认令牌窃取与 AI 角度**；③ **SAP 官方声明的覆盖面窄于事件本身**（只说「客户业务数据」）；④ **SAP 官方 news.sap.com 无相关公告**，vendor advisory 缺失；⑤ **10 月 Gentlemen 勒索挂网与本事件明确无关联**，不得连线；⑥ **4 月 npm 事件与本事件无任何公开关联**，不得自行断定**。

---

## 三、原文归档（快照）

| 快照文件 | SHA256 | 抓取时间 | 字符数 | HTTP |
|---|---|---|---|---|
| `raw/snapshots/security/sap-github-incident-techbag.md` | `d88c5fd916d0de99cb343c7d4e6887d0ce03f030e3a1531eff2b4e97123c7f3d` | 2026-11-28 07:12:08 | 15,382 | 200 |
| `raw/snapshots/security/sap-github-incident-cyberinsider.md` | `73db557fe4e6b89824b3c252cec2e38037b07bbbafae0f25e39f710e56a43a64` | 2026-11-28 07:12:08 | 3,970 | 200 |
| `raw/snapshots/security/sap-github-incident-cisovoice.md` | `8dc5f589f8984bfec6107a277d3be5a34f752b16888e3928d4dbd24f05eedc03` | 2026-11-28 07:12:10 | 3,128 | 200 |

**关键原文摘录**

> **主源 1「SAP 说了什么 vs 媒体说了什么」分栏**（`sap-github-incident-techbag.md`）：
> > 「**01 What SAP has said, and what others report**
> > SAP's statement has three parts. It identified suspicious activity. It acted at once: dpa quotes SAP as saying it had『**unverzüglich die notwendigen Maßnahmen ergriffen, um seine Kunden zu schützen und die Sicherheit seiner Dienste zu gewährleisten**』… And, so far, it has found **no evidence that anyone reached customer business data**.
> > Der Spiegel broke the story on the evening of 26 November, citing internal communications and people familiar with the matter. **The Record** summarises Spiegel's report: the attackers went for SAP's software development environment on GitHub and obtained employee authentication tokens that let them **copy and modify source code**.
> > **Claim / Who says it / Status**
> > Suspicious activity identified; steps taken at once to protect customers and secure services — **SAP, statement of 27 Nov — Confirmed by SAP**
> > No evidence, so far, of unauthorised access to customer business data — **SAP, statement of 27 Nov — Confirmed by SAP**
> > The activity was in SAP's development systems on GitHub — **dpa, from SAP's internal notice; Der Spiegel — Reported**
> > Employee authentication tokens let the attackers copy and modify source code — **Der Spiegel — Reported**
> > Staff were told days earlier to check whether to change their login details — **dpa — Reported**
> > GitHub access restricted; automated development processes stopped; **signing keys replaced** — **Handelsblatt — Reported**
> > Internal code name『**Project Granite**』 — Der Spiegel — Reported
> > The attackers may have used **agentic AI** — Der Spiegel, citing internal sources (via heise) — Reported
> > More than a week in progress; several authorities involved — Der Spiegel, 27 Nov — Reported
> > **Whether altered code reached any customer — No one has said — Not known**
> > **SAP did not say what the activity was, when it was detected or which parts of the company it touched. The company's own news site, news.sap.com, carried no post about it when we last checked.**」

> **主源 2（CyberInsider）**（`sap-github-incident-cyberinsider.md`）：
> > 「SAP has confirmed suspicious activity and took steps to secure its services after a reported intrusion into the GitHub environment it uses to develop and deliver software. The company says its investigation has so far found **no evidence of unauthorized access to customer business data**.
> > …**SAP has restricted access to GitHub, paused automated development workflows, and replaced signing keys** as part of a response dubbed『**Project Granite**』.
> > **In a separate advisory issued the same day, Germany's Federal Office for Information Security (BSI) warned that AI agents can automate much of a cyberattack using widely available models, lowering the cost and potentially making such attacks more common.** The agency urged companies still building out their defenses to **prioritize incident response and close off the easiest ways into their systems**.」

> **主源 3（CISO Voice）**（`sap-github-incident-cisovoice.md`）：
> > 「SAP … **provided its employees with an internal testing tool to detect any malicious code**. The company also **requires developers to now cryptographically sign every piece of code**, Handelsblatt added.
> > 「『**We are dealing with tools that enable cyberattacks in previously unknown quantities and speeds**,』BSI President Claudia Plattner told … Handelsblatt.『**Cyberaggression has changed – it has not only become faster, more comprehensive and more powerful, but also many times more complex.**』」

---

## 四、概要提取

- ⭐⭐⭐ **库内首条「厂商自身开发平台被攻破并更换代码签名密钥」的公开案例**：SAP 员工认证令牌被窃 → 攻击者复制并篡改 GitHub 源码 → SAP 限制 GitHub 访问、**暂停自动化开发流水线**、**更换代码签名密钥**、向员工提供恶意代码检测工具、**要求每份代码做密码学签名**（内部代号 Project Granite）。
- ⭐⭐⭐ **库内首条「厂商声明覆盖面窄于事件本身」**：SAP 官方只确认两件事 —— ① 发现可疑活动并已采取措施；② **迄今无证据表明客户业务数据被未授权访问**。**源码、内部凭据、构建完整性均不在其声明范围内**；且 **SAP 官方 news.sap.com 无相关公告**。
- ⭐⭐⭐ **库内首条「被偷的是身份不是密钥」三样本凑齐**：11-20 `agent-framework` PyPI 投毒（令牌外传，须撤销信任关系）→ 11-25 Azure APIM（修复不作废既有凭据，吊销时长成独立度量）→ **本期 SAP（令牌窃取致源码被改，须轮换签名密钥）**。
- ⭐⭐⭐ **库内首条「AI 智能体参与攻击」的厂商级案例 + 国家级机构同日警告**：Der Spiegel 引内部消息称攻击者**可能**使用了 AI agents；**德国 BSI 于同一天（11-26）发布警告**，称进攻型 agent 框架可用公开模型自动化攻击的绝大部分流程、降低攻击成本，并建议**优先建好事件响应、堵住最容易的入口**；BSI 主席称攻击工具带来「**前所未有的数量与速度**」且「**复杂了多倍**」。
- ⭐⭐⭐ **库内首条「一周内两家厂商连续丢失开发者账号」**：SAP（11-26/27）+ **1Password（11-25 披露）**，1Password 的传导链为「**GitHub 账号 → CI/CD → 恶意后端代码**」。
- ⭐⭐ **库内首条「同一厂商 8 个月内的两起代码供应链事件」**：2026-04-29 Mini Shai-Hulud npm 活动污染 4 个 SAP 相关包（`mbt`、`@cap-js/db-service`、`@cap-js/postgres`、`@cap-js/sqlite`），窃取 GitHub/npm 令牌与 CI/CD 凭据（TeamPCP 被评估为幕后）→ **令牌窃取是重复手法，不是孤例**；⚠️ **SAP 官方声明未提该前例，两案无公开关联**。
- ⭐⭐ **库内首条「复制」与「篡改」被显式区分为两类风险**：**复制 = 知识产权与侦察问题；篡改 = 供应链问题** —— 用合法员工令牌提交的改动「**携带该员工的身份，可能通过随意审查**」，且是否在进入构建前被发现**未知**。
- ⭐⭐ **库内首条「客户侧动作」**：**固定依赖版本、暂缓自动更新、部署前校验校验和与签名**。
- ⭐ **官方声明缺口清单入库**：SAP 未说明活动性质、发现时间、涉及范围、哪些仓库被改、是否已有改动进入发布或客户构建、初始检测时间；**是否altered code 到达客户 —— 无人说明**。
- ⭐ **事件时长与监管**：11-27 报道称事件已持续**超过一周**、**多家机构介入**；下一次 SAP Security Patch Day 为 **12 月 8 日**（每月第二个周二）。
- ⭐ **同期噪声的明确排除**：10 月 Gentlemen 勒索团伙挂网 SAP 拉美业务，**报道明确指出与本事件无关联**。

---

## 五、主要观点

**原文主张**

- **SAP 官方（经三源一致转述）**：「SAP has identified suspicious activity and promptly implemented the necessary measures to protect its customers and preserve the security of its services」「**Based on our investigation to date, we have found no evidence of unauthorized access to customer business data.**」
- **Der Spiegel（引内部消息源，经三源转述）**：攻击者获取 SAP 员工认证令牌，用于**复制并修改 GitHub 上的源码**；内部代号 **Project Granite**；攻击者**可能**使用了 AI agents；事件**已持续一周以上、多家机构介入**。
- **Handelsblatt（引公司内部消息，经主源 1 转述）**：SAP **限制 GitHub 访问、停止自动化开发流程、更换签名密钥**；**要求开发人员对每一份代码做密码学签名**；向员工提供内部恶意代码检测工具。
- **dpa（看到部分内部通知）**：可疑活动发生在「**开发者生产力与软件交付平台 GitHub**」内；通知在公开声明前数日已发给员工，要求自查是否需要更换登录凭据。
- **德国 BSI（同日通告，经主源 2 转述）**：「AI agents can automate much of a cyberattack using widely available models, lowering the cost and potentially making such attacks more common」；建议企业**优先建好事件响应能力并堵住最容易的入侵入口**。

**我方判断**

- ⭐⭐⭐ **本期最该被记住的，不是「SAP 被黑了」，而是 SAP 官方声明与真实影响面之间的那道缝 —— 而这道缝，正是我方库内最需要被制度化对待的东西。** SAP 说了两句：发现可疑活动、已采取措施；迄今无证据表明**客户业务数据**被访问。**但源码呢？内部凭据呢？构建完整性呢？签名密钥呢？—— 一句没提。** 而这三源一致转述的报道告诉我们：攻击者拿到的令牌**能复制并能修改源码**，SAP 自己因此**更换了签名密钥**。**换句话说：SAP 用「更换签名密钥」这个动作承认了「发布链的可信度可能已被破坏」，却用一句「无证据表明客户业务数据被访问」让公众把注意力放在数据上。** **对我方的直接含义：不能把厂商公告的「保证句」当作影响范围的定义。** 建议在库内固定一条引用纪律：**厂商声明的覆盖范围必须逐字引用，不得替它扩张或收缩**（本篇只允许写「SAP 称迄今无证据表明客户业务数据被未授权访问」，不得写成「SAP 未发现数据泄露」，更不得写成「SAP 未受影响」）。
- ⭐⭐⭐ **「令牌 → 复制 + 篡改 → 更换签名密钥」这条链，把库内「凭据可被撤销」的原则从抽象变成了可观测的厂商动作 —— 而这恰恰是我方最需要的那个动作。** 库内 11-20 记 `agent-framework` 投毒时的结论是「**轮换密钥无效，必须能撤销信任关系**」；11-25 记 Azure APIM 时的结论是「**修复不会自动作废此前可能被访问过的客户凭据 → 从怀疑泄露到完成吊销的时长成为可测的独立度量项**」。**今天这条链把两件事接上了**：SAP 的处置不是「改了密码」，而是**换掉了发布链的信任根（签名密钥）** + **掐断了自动化流水线**。**我方应当学的不是「SAP 也有漏洞」，而是「当信任根可能被动过时，正确的动作是换根并停链，而不是改密码」。** 这条应当直接写进我方的凭据处置规范：**凡是「我方签发的凭据 / 我方信任的制品签名」可能被第三方读取的，处置顺序必须是「先吊销/换根、再排查、再恢复」**；库内 11-26 给出的 NetScaler 场景（「先取证再打补丁，顺序别反」）与本条（「先换根再排查」）构成一对**顺序相反但同源**的处置纪律 —— **顺序取决于被偷的是身份还是密钥，这正是我方必须先判定的第一件事。**
- ⭐⭐⭐ **BSI 同日警告，是本期唯一一条「国家级机构」的证据，它把库内的 AI 议题从技术观察提升为政策信号 —— 而且它给出的建议，恰好是我方一直缺的那条。** 库内 11-23 已经记了 AI 智能体自主发现并利用（CISA 的 MONAI Label 条目），但那只是**一个案例**。**今天 BSI 说的是「进攻型 agent 框架可以用公开模型自动化攻击的绝大部分流程，降低成本，使这类攻击更常见」** —— **这是从「能力」到「普及」的判断。** 而 BSI 给出的建议非常具体：「**优先建好事件响应能力，并堵住最容易的入侵入口**」。**这条与我方库内反复出现的处境严丝合缝**：库内 11-17/11-18/11-26 反复记到「我方主站连续命中但处置链有缺口（某攻击类型既不在 block 也不在 ignore 名单 → 命中即落人工通道 → 未自动拉黑）」。**BSI 说「堵住最容易的入口」，而我方库里记着的恰恰是「最容易的入口没堵住」。** **这条应该成为对我方 P0 专项整改 [对外站点暴露面专项自查] 的一次方向性背书 —— 不是外部权威替我方背书我方做得不好，而是外部权威与我方独立得出了同一个结论。**
- ⭐⭐⭐ **「一周内两家厂商连续丢失开发者账号」这个对照，把 SAP 从孤例变成了模式 —— 而模式的含义是「这是可复制的路径，不是我方独有资产才需要担心」。** SAP：员工 GitHub 账号 → 令牌 → 源码复制与篡改 → 签名密钥被换；1Password：**GitHub 账号 → CI/CD → 恶意后端代码**。**两条链的共同点是：入口都是「一个开发者账号」，路径都经过「自动化流水线」，终点都是「我方不在意的层面」。** **这直接命中我方库里一个至今没有条目的资产类别。** 库内 11-24 记的 Osaki 案卷里已经提出过「共享远程接入网关的爆炸半径」，11-26 记的工程工作站「资产类别仍未指派」，**但「开发者/运维账号 + 制品流水线」这一整类，我方库里从来没有任何条目**。**建议本期正式立一条新资产类别候选：代码托管平台账号与 CI/CD 流水线凭据** —— 哪怕今天我方无证据，也应作为「待核实资产类别」登记，而不是留白。**理由很简单：这条路径在本周被两家不同厂商独立验证过。**
- ⭐⭐ **「复制」与「篡改」必须分列，这是一条我方文档写作上的硬要求 —— 因为把它们合称「源码泄露」会同时犯两个错。** 辅源说得非常清楚：**复制**主要是知识产权与侦察问题（私有源码可离线研究弱点，但**本身不交出对客户系统的访问权**）；**篡改**是供应链问题（用合法员工令牌提交的改动**带着该员工的身份，可能通过随意审查**），而是否在进入构建前被发现**未知**。**我方若写成「SAP 源码泄露」，就会把「有没有东西进入客户构建」这个最关键的不确定性给抹掉 —— 而恰恰是这一点，SAP 三源一致地「无人说明」。** **建议在库内文档模板层面加一条：涉及供应链事件时，「复制 / 篡改 / 是否进入构建 / 是否到达客户」四问必须分四栏回答，答不出的写「未知」。**
- ⭐⭐ **「固定依赖版本、暂缓自动更新、部署前校验校验和与签名」这三条客户侧动作，是本条可以直接迁移到我方的部分 —— 且它们与库内 11-20 的教训完全一致。** 库内 11-20 记 `agent-framework` 时已经写过「**PyPI 官方 JSON 接口里 1.26.1/1.26.2 已彻底消失（删除、非 yank）→ 重装一遍不是修复手段**」，本期 SAP 案给出的客户侧动作本质上就是同一件事的通用版：**在供应商说清影响范围之前，不要自动更新、不要自动重装，先固定版本并校验签名。** **这条对聚合侧还有一层业务含义：我方若向客户提供「组件/设备软件版本」的管理能力，这个能力必须带「固定版本 + 签名校验 + 暂缓自动更新」三件套**，否则我方在客户供应链出问题时无法给出可辩护的动作。
- ⭐ **「SAP 官方 news.sap.com 无相关公告」这条负结论必须照记。** 一个被媒体广泛报道的厂商事件，**厂商自己的新闻站点上什么都没有** —— 这说明 SAP 选择不通过 vendor advisory 通道披露。**对我方的直接含义：不能假设「厂商会发公告」，因此「等公告」不能作为漏洞处置的前置条件。** 库内 11-26 记的 KEV 处置字段（「Apply mitigations in accordance with vendor instructions」）在遇到「厂商不发指令」时会落空 —— **本期提供了一个真实案例。**
- ⭐ **10 月勒索挂网与本事件「明确无关联」，这条排除记录必须入库。** 库内已有习惯是记录「无关联的同期噪声」（如库内 11-27 记的 Osaki 与 Danfoss 必须分开记）。**SAP 案同理：Gentlemen 团伙挂网 SAP 拉美业务，与 GitHub 事件是两个独立事件**，报道本身已明确指出无关联。**我方不得因为都叫「SAP」就把它们串起来。**
- ⭐ **必须写明的最大局限：本期全部为媒体报道，无一手官方通告。** 安全域的采集口径要求「至少两个独立信源（官方通告 + 第三方分析）」，**本篇的「官方」成分只有 SAP 的书面声明（由三个独立来源一致转述），并不构成官方通告级证据**。**因此本篇只能支撑方向级结论与方法论，不得支撑任何我方资产级判断。** 后续应追：SAP 的 Security Patch Day 公告（12-08）、SAP Security News、GitHub 侧的 advisory、以及 BSI 通告原文。

---

## 六、参考意义

| 方向（网络安全/信创/等保/隐私保护/护网） | 可证事实 | 本阶段处理 |
|---|---|---|
| 网络安全（凭据处置顺序） | 令牌被窃后 SAP 更换签名密钥、暂停自动化流水线、限制 GitHub 访问；库内 11-25 Azure APIM 与 11-26 NetScaler 分别给出「须吊销」与「先取证再打补丁」两种顺序 | ✅ **进评审**（方向级）。落点：**凭据处置规范新增判定前置** ——「先判被偷的是身份还是密钥，再定处置顺序：身份 → 换根 + 停链；密钥 → 先取证后升级」；**把「先吊销/换根」而非「改密码」写成默认动作**。**不新开产物** |
| 网络安全（事件响应优先级） | 德国 BSI 同日通告：AI agent 可自动化攻击大部分流程、降低成本；建议**优先建好事件响应、堵住最容易的入口**；BSI 主席称攻击规模与复杂度发生量级变化 | ✅ **进评审**（方向级）。落点：**AI 智能体风险从技术观察升为方向级输入**；**护网与事件响应准备度评审中增「最容易入口是否已堵」一条自查**（与库内 11-17/11-26 记录的「某攻击类型既不在 block 也不在 ignore → 未自动拉黑」直接对应）。**不新开产物** |
| 网络安全（暴露面 · 资产类别） | 一周内 SAP 与 1Password 连续经由「开发者 GitHub 账号」被攻破（1Password：账号 → CI/CD → 恶意后端代码）；库内无「代码托管平台账号与 CI/CD 流水线凭据」资产类别 | ✅ **进评审**（方向级）。落点：**资产台账新登记一类待核实资产类别「代码托管平台账号 / CI/CD 流水线凭据 / 制品签名密钥」**，并注明「本周由两家厂商独立验证该路径」。**不新开产物、不产专项整改**（我方无使用证据） |
| 网络安全（供应链完整性） | 「复制」与「篡改」风险性质不同；改动携带合法员工身份、可能通过随意审查；是否进入构建/到达客户**无人说明** | ✅ **进评审**（方向级）。落点：**文档模板增「供应链事件四问」**（复制？篡改？是否进入构建？是否到达客户？，答不出写「未知」）；**并把「固定依赖版本 + 暂缓自动更新 + 部署前校验校验和与签名」纳入依赖治理默认动作**。**不新开产物** |
| 网络安全（引用纪律） | SAP 官方声明只覆盖「客户业务数据」；SAP 官方 news.sap.com 无公告 | ✅ **进评审**（方向级）。落点：**厂商声明的覆盖范围逐字引用、不得扩张或收缩**；**并立一条「不得以『等厂商公告』作为处置前置条件」**（本期提供了厂商未发公告的真实案例）。**不新开产物** |
| 隐私保护（供应商事件中的数据责任） | 供应商声明覆盖客户业务数据的未授权访问 | 🟡 **观察项**（仅方法论参照）。落点：**客户侧供应商事件评估表中，「厂商声明覆盖范围」增为一列**（避免把「未提及」读成「未发生」）。**不产产物** |
| 等保 / 信创 | 无 | ❌ 不进 |

---

## 七、总结输出

**一句话结论**：SAP GitHub 开发者平台令牌被窃事件（11-26 首发 / 11-27 官方声明，内部代号 **Project Granite**）给库内带来**四个新样本与一条必须制度化的引用纪律** —— ⭐⭐⭐ **①「被偷的是身份不是密钥」三样本首次凑齐**（11-20 `agent-framework` PyPI 投毒 → 11-25 Azure APIM → **本期 SAP：令牌窃取 → 复制并篡改源码 → 更换代码签名密钥、暂停自动化流水线、限制 GitHub 访问、要求每份代码密码学签名、向员工发放恶意代码检测工具**）；⭐⭐⭐ **②「厂商声明覆盖面窄于事件本身」** —— SAP 官方只确认两件事（已发现可疑活动并采取措施、**迄今无证据表明客户业务数据被未授权访问**），**源码 / 内部凭据 / 构建完整性 / 签名密钥一句未提**，且**官方 news.sap.com 无任何公告**，**事件是否已有改动进入构建或到达客户「无人说明」** → **不得把厂商的「保证句」当作影响范围的定义**；⭐⭐⭐ **③「一周内两家厂商连续丢失开发者账号」**（SAP 与 1Password，后者路径为 **GitHub 账号 → CI/CD → 恶意后端代码**）→ **库内至今没有「代码托管平台账号 / CI/CD 流水线凭据 / 制品签名密钥」这一资产类别，建议正式登记为待核实类别**；⭐⭐⭐ **④ 德国 BSI 同日（11-26）通告**：进攻型 agent 框架可用公开模型自动化攻击的绝大部分流程、降低成本并使其更常见，建议企业**优先建好事件响应、堵住最容易的入口**，BSI 主席称攻击工具带来「前所未有的数量与速度」且「复杂了多倍」→ **与库内 11-23 的 MONAI Label 技术样本形成政策—技术两侧呼应，且与我方 11-17/11-26 记录的「某攻击类型未进 block 名单 → 未自动拉黑」直接对上**；⭐⭐ **「复制」与「篡改」被显式区分为两类风险**（复制 = 知识产权与侦察；篡改 = 供应链，用合法员工令牌提交的改动携带该员工身份、可能通过随意审查）→ **供应链事件必须四问分栏：复制？篡改？是否进入构建？是否到达客户？**；⭐⭐ **同一厂商 8 个月内的前例**：2026-04-29 Mini Shai-Hulud npm 活动污染 4 个 SAP 相关包并窃取 GitHub/npm 令牌与 CI/CD 凭据 → **令牌窃取是重复手法**，但 **SAP 官方声明未提该前例、两案无公开关联，不得自行断定**；⭐⭐ **客户侧动作可直接迁移**：固定依赖版本、暂缓自动更新、部署前校验校验和与签名；⭐ **同期噪声明确排除**：10 月 Gentlemen 勒索挂网 SAP 拉美业务与本事件**无关联**；⚠️ **本篇全部为媒体报道（三源一致转述 SAP 声明），无一手官方通告，只能支撑方向级与方法论结论，不得支撑任何我方资产级判断**。

**落地去向**

- [ ] 产品特性
- [ ] 需求变更
- [ ] 专项整改
- [x] **方向级产物**（网络安全）—— ① 凭据处置规范增「身份 vs 密钥」前置判定与处置顺序（身份 → 换根 + 停链；密钥 → 先取证后升级）；② AI 智能体风险升为方向级输入，事件响应与护网准备度评审增「最容易的入口是否已堵」自查条；③ 资产台账新登记「代码托管平台账号 / CI/CD 流水线凭据 / 制品签名密钥」待核实类别；④ 文档模板增「供应链事件四问」分栏 + 依赖治理默认动作三件套（固定版本 / 暂缓自动更新 / 校验签名）；⑤ 引用纪律增「厂商声明覆盖范围逐字引用」与「不得以等厂商公告作为处置前置条件」两条。**均不新开产物、不产专项整改**
- [x] **观察项**（隐私保护 · 仅方法论参照）—— 客户侧供应商事件评估表增「厂商声明覆盖范围」一列
- [x] **待核实（不产产物）** —— ① 我方是否存在代码托管平台账号、CI/CD 流水线凭据或依赖制品签名；② 我方是否有 SAP / 1Password 相关依赖或集成；③ 我方依赖治理是否已具备「固定版本 + 暂缓自动更新 + 部署前校验签名」三件套
- [ ] **跟踪项** —— ① SAP Security Patch Day（12-08）与 SAP Security News 是否补发公告；② BSI 通告原文与后续技术细节；③ 四个 SAP npm 包的历史影响与本次是否有重叠；④ 「是否已有改动进入构建」的最终结论；⑤ AI agent 攻击框架的公开技术细节

**关联文档**

- [Microsoft agent-framework PyPI 投毒（1.26.1/1.26.2 · .pth 常驻 · 云身份令牌外传）](agentFrameworkPypiSupplyChain-2026-11.md) —— **同原则的第一样本**（令牌外传 → 须撤销信任关系；PyPI 官方 JSON 接口已无 1.26.1/1.26.2 → 重装不是修复手段）
- [Azure APIM 密钥被窃 → 挪威能源行业被击中](azureApimNorwayEnergyBreach-2026-11.md) —— **同原则的第二样本**（修复不作废已被访问过的凭据 → 从怀疑到完成吊销的时长成为独立度量）
- [Java4Shell：SCA/SBOM 结构性盲区](java4ShellCve2026114938-2026-11.md) —— **供应链来源侧的同类盲区**（运行时层不在清单里）；与本期「库内无记录 ≠ 未部署」互为补充
- [Osaki Electric 勒索与智能电表供应链中断](osakiElectricSmartMeterRansomware-2026-11.md) —— **供应商侧事件传导样本**；本期 SAP 案补上了「供应商侧事件如何按类别记」的另一类（开发侧 vs 运营侧）
- [CISA KEV 2026-11-27 批次三条](cisaKev20261127GeoServerDrupalBatch-2026-11.md) —— 本期安全域另一条；其「库内无记录 ≠ 未部署」「厂商不提供 vendor advisory 时处置字段落空」与本篇结论互相印证

---

## 参考链接

- 独立分析：SAP 确认项 vs 报道项逐条分栏（主源 1）：https://www.thetechbag.com/blog/sap-suspicious-activity-github-development-systems
- CyberInsider：SAP 官方声明转述 + BSI 同日通告（主源 2）：https://cyberinsider.com/sap-github-security-incident/
- CISO Voice：SAP 致员工信件内容 + 签名要求 + BSI 主席表态（主源 3）：https://cisovoice.com/breaches-vulnerabilities/sap-github-cybersecurity-incident

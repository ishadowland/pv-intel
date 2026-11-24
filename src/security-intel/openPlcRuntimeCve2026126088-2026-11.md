# CISA ICSA-26-323-01：Autonomy Logic OpenPLC Runtime 竞态条件 → 免认证创建多个管理员账号（CVE-2026-126088）

> 🔴 强约束 · 采集于 2026-11-24 · 核心标识：**OpenPLC Runtime ≤4.2.4 的用户创建流程存在竞态条件** —— 多个并发请求可在任何用户被提交前同时通过"用户是否已存在"检查，**结果是无需任何凭据即可创建出多个未认证管理员账号** · ⭐⭐⭐ **这是库内 11-19 日报里被明确标记为"正文未取得、只登记存在、不做内容判断"的 ICSA-26-323-01 —— 本期已取得 CISA 官方通告正文，该待办闭环** · ⭐⭐⭐ **赛点所在：一个"检查存在性"的动作被当成原子操作，而它其实不是** → **这是库内至今第一条"TOCTOU / 竞态绕过认证"类的一手官方漏洞证据** · ⭐⭐ **官方点名四个行业：关键制造、能源、交通运输、水务污水**（**能源在列**）· ⭐⭐ **修复版 4.3.0** · ⭐⭐ **MITRE ATT&CK 映射为 T1136 Create Account + T1136.001 Local Account + T1078 Valid Accounts**（**持久化**）· ⚠️ **官方明说"截至发布日无已知公开在野利用"**，CISA SSVC 评估 exploitation = none known、automatable = no、technical impact = total · ⚠️ **我方无 OpenPLC 使用证据 → 不得下"我方受影响"结论**

---

## 一、信源核实

| 项 | 值 |
|---|---|
| 来源请求 | `CISA ICSA-26-324 ICS advisory November 2026`（web_search，用于确认 11-24 当日是否有更新批次 ICS 通告）<br>`Autonomy Logic OpenPLC Runtime ICSA-26-323-01 vulnerability unauthenticated`（web_search，命中 Defcon Level 的 CISA 通告转载、ThreatMonitor、NEOSEC、Intel Neosec 的 NVD/SSVC 记录、TechGeeks、Aviatrix、sobasically.ai 等） |
| 原始 URL（主 1 · CISA 官方通告） | https://www.cisa.gov/news-events/ics-advisories/icsa-26-323-01 （**CISA 官方 ICS 通告**，Alert Code **ICSA-26-323-01**，Release Date **November 19, 2026**，Revision History 仅一条 `2026-11-19 | 1 | Initial Publication`） |
| 原始 URL（主 2 · 通告全文转载） | https://www.defconlevel.com/alert/2026-11-19-cisa-cybersecurity-advisories-autonomy-logic-openplc-runtime-icsa-26-323-01 （Defcon Level · CISA Cybersecurity Advisories，完整转载官方通告正文） |
| 原始 URL（辅 1 · 第三方攻击面分析） | https://aviatrix.ai/threat-research-center/icsa-26-323-01-openplc-runtime-race-condition-cve-2026-126088 （Aviatrix Threat Research Center，含 Kill Chain 逐段拆解与 MITRE ATT&CK 映射） |
| 原始 URL（辅 2 · NVD / SSVC 记录） | https://intel.neosec.eu/en/cve/CVE-2026-126088 （含 NVD 的 CVSS v3.1 / v4.0 双评分与 **CISA SSVC 评估**：exploitation **none known**、automatable **no**、technical impact **total**） |
| 发布主体 | CISA（ICS 通告与 KEV）· NVD / CVE（记录）· Aviatrix / Defcon Level / TechGeeks / NEOSEC（第三方分析）· 漏洞报告人 **Noureddin Lutfi**（CISA 通告致谢） |
| 发布/更新时间 | CISA 通告 **2026-11-19**（初始发布，无修订）· NVD 记录 **2026-11-19** 发布 / **2026-11-20** 修改 · Aviatrix 分析 **2026-11-19** |
| 采集时间 | 2026-11-24 07:12:51 ~ 07:24:32 |

**快照清单**（SHA256 取自 `.meta.json` 的 `sha256_raw`，正文字符数取自 `text_chars`）

| 快照 | SHA256 | 抓取时间 | 正文字符 | HTTP |
|---|---|---|---|---|
| `raw/snapshots/security/cisa-icsa-26-323-01-openplc.md` | `5a4036126da460852cd94938a86db70b58e6407eaf9daacbe4b6e98cd66cd24c` | 2026-11-24 07:24:32 | 5,130 | 200 |
| `raw/snapshots/security/openplc-runtime-cve2026126088.md` | `e67757ae2f7e448884fe6b81b72774d1e32cf0a56b8a00fd83853e061f5a3ea9` | 2026-11-24 07:12:51 | 8,459 | 200 |
| `raw/snapshots/security/openplc-runtime-aviatrix-analysis.md` | `56553374e7162808edadbe4410e30146387498a09f58657296dabf2b8a2847b3` | 2026-11-24 07:12:51 | 15,773 | 200 |

> 📎 **入库理由（这是本篇最特殊的地方）**：库内 11-20 日报在「🔇 背景噪声」里写了这样一条 ——"**CISA 同批次另两条 11-19 通告：ICSA-26-323-01（Autonomy Logic OpenPLC Runtime）、ICSA-26-323-02（Elecbrakes）—— 正文未取得，仅在 ICSA-26-323-03 页面的 Related Advisories 中出现 → 只登记存在，不做内容判断**"。**那条待办在本期被正式关闭**：CISA 官方通告正文已取得快照，且拿到了 NVD 的 SSVC 评估与第三方攻击链分析。**这是库内首次为"只登记存在"的 ICS 通告补上正文** —— 值得单独成篇，因为它同时带来一条库内此前完全没有的一手证据：**竞态条件绕过"存在性检查"从而凭空造出管理员账号**。
> ⚠️ **采集取舍说明**：ICSA-26-323-02（Elecbrakes）正文本期仍未取得 → **维持"只登记存在"**，不新建文档（见第 7 段跟踪项）。

---

## 二、事实核查

| # | 数据点 | 原文表述 | 核查方式 | 结论 | 备注 |
|---|---|---|---|---|---|
| 1 | 通告编号与发布 | CISA 页："Alert Code **ICSA-26-323-01**"、"Release Date **November 19, 2026**"、"Revision History: **2026-11-19 \| 1 \| Initial Publication**" | CISA 官方页快照逐字 + Defcon Level 转载比对 | ✅ **已核（两源）** | ⭐⭐ **通告为 11-19 当日首发且至今无修订** → 库内按"最新批次"收录即可，无需追踪修订历史 |
| 2 | 漏洞核心 | CISA 官方："In Autonomy Logic OpenPLC Runtime versions **4.2.4 and prior**, a **race condition** allows multiple concurrent requests to pass the **existence check** before any user is committed, resulting in **several unauthenticated admin accounts being created**" | 三源（官方页 + Defcon Level + NVD/NEOSEC 记录）逐字比对 | ✅ **已核（三源一致）** | ⭐⭐⭐ **官方原文把机制说得极清楚：漏洞不在"认证"，而在"用户创建流程把一次存在性检查当成了原子的"** —— 检查通过 → 提交之前 → 多个并发请求都看到"不存在" → 都提交 → 产生多个管理员 |
| 3 | 影响表述 | CISA 官方 Summary："Successful exploitation of this vulnerability could allow **several unauthenticated admin accounts to be created**" | 三源比对 | ✅ **已核** | ⭐⭐ **注意官方措辞是"several unauthenticated admin accounts"** —— 即**攻击者拿到的账号是"未认证"的**，但**其权限是管理员级**。⚠️ **不要写成"认证绕过"** —— 精确说法是"**无需凭据即可创建管理员账号**" |
| 4 | 评分双口径 | CISA 页：CVSS **v3 8.1**；CVSS **v4 9.2（Critical）**；向量 v3.1 `AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H`、v4.0 `AV:N/AC:H/AT:P/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N` | CISA 页 + ThreatMonitor + NEOSEC 三方 | ✅ **已核（三源一致）** | ⭐ **v3.1 与 v4.0 差距较大（8.1 vs 9.2）**，引用时须带明版本 |
| 5 | 弱点分类 | "Relevant CWE: **CWE-362** Concurrent Execution using Shared Resource with Improper Synchronization ('Race Condition')" | CISA 页 + NVD 记录 | ✅ **已核** | ⭐⭐ **这是库内第一条 CWE-362 的一手官方证据** |
| 6 | 受影响版本与修复 | "OpenPLC Runtime **≤4.2.4**"（known_affected）；Remediations / Vendor fix："**Update to OpenPLC Runtime version 4.3.0 or later**" | CISA 页 + Defcon Level | ✅ **已核（两源）** | ⭐⭐ **修复版 4.3.0 是唯一解**（无变通方案，官方只给了升级） |
| 7 | 行业与部署范围 | "Critical Infrastructure Sectors: **Critical Manufacturing, Energy, Transportation Systems, Water and Wastewater Systems**"；"Countries/Areas Deployed: **Worldwide**"；"Company Headquarters Location: **United States**" | CISA 页逐字 | ✅ **已核** | ⭐⭐ **能源在列** → 与我方能源/光伏产业链所处的关基行业有交集。⚠️ **但"行业在列"≠"我方受影响"** —— OpenPLC 是 PLC 运行时，**我方无使用证据** |
| 8 | 官方在野状态 | CISA 页："**No known public exploitation specifically targeting these vulnerabilities has been reported to CISA at this time**" | CISA 页 + ThreatMonitor（"no public exploit"）比对 | ✅ **已核** | ⭐⭐ **必须写明** —— 与库内已记的 Java4Shell（11-19 起有大规模攻击尝试）、libumqtt（未入 KEV 无在野）状态都不同 |
| 9 | CISA SSVC 评估 | NEOSEC 记录的 NVD 字段："CISA SSVC assessment added — {"role":"CNA","options":{"exploitation":"**none known**","automatable":"**no**","technicalImpact":"**total**"},"version":"2.0.3"}" | NEOSEC 页面快照逐字 | ✅ **已核** | ⭐⭐ **"automatable = no"** 是重要限定 —— 竞态条件利用通常需要精细时序控制，**不是"发个请求就能批量自动化"**。⚠️ 但 **Aviatrix 的攻击链分析与之不冲突**（它描述的是攻击者侧可做到什么，不是"能否自动化"） |
| 10 | 官方缓解建议 | CISA Recommended Practices："**Minimize network exposure** for all control system devices…Locate control system networks and remote devices behind **firewalls** and **isolating them from business networks**. When remote access is required, use more secure methods, such as **Virtual Private Networks (VPNs)**…Also recognize VPN is only as secure as the connected devices."；并要求 "perform proper **impact analysis and risk assessment** prior to deploying defensive measures" | CISA 页逐字 | ✅ **已核** | ⭐⭐ **"VPN 只有连接到它的设备那么安全"这句，与库内 11-16 已记的"CISA 五部门警告：联网辅助设备是被点名的攻击面"（原文 "unpatched **or internet-accessible**"）是同一套官方措辞** → **我方暴露面自查的"联网"判据再次被官方强化** |
| 11 | 攻击链（第三方） | Aviatrix："The attacker targets an **internet-exposed or network-accessible** OpenPLC Runtime instance running version 4.2.4 or earlier. By sending a **burst of concurrent unauthenticated POST requests to the user registration endpoint**, the race condition allows multiple requests to pass the existence check before any user is committed, resulting in the creation of several unauthorized admin-level accounts without any prior credentials." | Aviatrix 快照逐字 | ✅ **已核（第三方分析）** | ⭐⭐ **"不需要任何先前的凭据"** —— 与 CISA 官方 "unauthenticated" 一致。⭐⭐ **攻击者落地后能做什么**：Aviatrix 列出 "with admin-level access established, the attacker leverages these accounts to escalate privileges, pivot laterally across OT network segments, establish persistent C2, exfiltrate operational configuration data, and ultimately **manipulate or disrupt PLC logic**" |
| 12 | ATT&CK 映射 | Aviatrix：Initial Access **T1190**（Exploit Public-Facing Application）/ **T1078**（Valid Accounts）；Persistence **T1136**（Create Account）+ **T1136.001**（Create Account: Local Account）；Privilege Escalation **T1548**（Abuse Elevation Control Mechanism）；Defense Evasion **T1078**；Impair Process Control **T0821**（Modify Controller Tasking）；Impact **T0831**（Manipulation of Control）+ **T0813**（Denial of Control） | Aviatrix 快照逐字 | ✅ **已核（第三方分析）** | ⭐⭐⭐ **"T1136 Create Account"这条映射值得单独强调**：**竞态条件漏洞的最终形态不是"拿权限"，而是"造账号"** —— 这与库内 11-19 已记的 [EPICS 工控漏洞](./epicsDerExposure-2026-11.md) 里"工控协议栈长期无认证"的结构性证据、以及库内 11-13 已记的 [ICSA-26-300-02 Genesis/ICONICS](./icsa2630002GenesisIconics-2026-11.md) 里"密码找回挑战响应对所有用户相同且固定"**共同构成库内第三条"认证/账号管理设计缺陷"的一手案例**，且这条是**竞态**而非"固定凭据" |
| 13 | 报告人 | CISA 页 Acknowledgments："**Noureddin Lutfi reported this vulnerability to CISA**" | CISA 页逐字 | ✅ **已核** | ⭐ 官方致谢记录（库内已记的 libumqtt 条目亦引用了同名报告人模式） |
| 14 | 我方侧现状 | — | 库内检索：`grep -rl "OpenPLC" src/` 仅命中 libumqtt 条目中"同批次另两条正文未取得"的登记引用 → **库内无我方使用 OpenPLC 的任何证据**；同时库内 [epicsDerExposure](./epicsDerExposure-2026-11.md) 记的是 EPICS 而非 OpenPLC | ⚠️ **我方无使用证据 → 不得下"我方受影响"结论** | ⭐⭐ **但我方有一条强相关资产事实**：TOOLS.md 记录我方 PVE 主机 `pve-main`（10.10.66.208，Proxmox VE）与一台远程办公 Windows VM → **PVE 不是 OpenPLC，本条不构成我方暴露面证据**（同理，不得把库内 EPICS 条目当成 OpenPLC） |

---

## 三、原文归档（快照）

- 快照文件：`raw/snapshots/security/cisa-icsa-26-323-01-openplc.md`
  - SHA256：`5a4036126da460852cd94938a86db70b58e6407eaf9daacbe4b6e98cd66cd24c`
  - 抓取时间：2026-11-24 07:24:32 · HTTP 200 · 正文 5,130 字符
- 快照文件：`raw/snapshots/security/openplc-runtime-cve2026126088.md`
  - SHA256：`e67757ae2f7e448884fe6b81b72774d1e32cf0a56b8a00fd83853e061f5a3ea9`
  - 抓取时间：2026-11-24 07:12:51 · HTTP 200 · 正文 8,459 字符
- 快照文件：`raw/snapshots/security/openplc-runtime-aviatrix-analysis.md`
  - SHA256：`56553374e7162808edadbe4410e30146387498a09f58657296dabf2b8a2847b3`
  - 抓取时间：2026-11-24 07:12:51 · HTTP 200 · 正文 15,773 字符

> 关键原文摘录（CISA 官方通告 ICSA-26-323-01）：
> 「**Summary**: Successful exploitation of this vulnerability could allow **several unauthenticated admin accounts to be created**. The following versions of Autonomy Logic OpenPLC Runtime are affected: OpenPLC Runtime ≤4.2.4 (CVE-2026-126088)」
> 「In Autonomy Logic OpenPLC Runtime versions 4.2.4 and prior, a **race condition** allows multiple concurrent requests to pass the **existence check** before any user is committed, resulting in **several unauthenticated admin accounts being created**.」
> 「Critical Infrastructure Sectors: **Critical Manufacturing, Energy, Transportation Systems, Water and Wastewater Systems**」
> 「**Remediations**: Vendor fix — **Update to OpenPLC Runtime version 4.3.0 or later**.」
> 「**No known public exploitation specifically targeting these vulnerabilities has been reported to CISA at this time.**」
> 「…use more secure methods, such as **Virtual Private Networks (VPNs)**, recognizing **VPNs may have vulnerabilities and should be updated** to the most current version available. **Also recognize VPN is only as secure as the connected devices.**」

---

## 四、概要提取

- ⭐⭐⭐ **库内 11-19 日报标为"正文未取得、只登记存在"的 ICSA-26-323-01，本期已取得 CISA 官方通告正文快照，该待办正式闭环**。
- ⭐⭐⭐ **漏洞机制是把一次"存在性检查"当成了原子操作**：多个并发请求在任何一个用户被提交之前都通过了"该用户是否已存在"的检查 → **凭空创建出多个未认证的管理员账号**。
- ⭐⭐ **攻击无需任何先前的凭据**（CISA 官方 "unauthenticated" + Aviatrix "without any prior credentials"）；攻击方式是**向用户注册端点打一发并发 POST 突发**。
- ⭐⭐ **评分双口径：CVSS v3.1 8.1 / v4.0 9.2（Critical）**；弱点 **CWE-362（竞态条件）**；受影响版本 **≤4.2.4**，**唯一解是升级到 4.3.0**。
- ⭐⭐ **官方点名四个关键基础设施行业，其中包含"能源"**；部署范围"Worldwide"。
- ⭐⭐ **MITRE ATT&CK 映射把这条的性质说清了**：初始访问 T1190/T1078 → **持久化 T1136 Create Account / T1136.001 Local Account** → 权限提升 T1548 → 工艺影响 T0821 Modify Controller Tasking / T0831 Manipulation of Control / T0813 Denial of Control。**即：竞态漏洞的最终形态不是"拿到权限"，而是"造出账号"**。
- ⭐⭐ **CISA SSVC 明确标注 exploitation = none known、automatable = no、technical impact = total** → **没有在野利用、难以自动化、但技术影响是全面的**。
- ⭐⭐ **官方缓解建议的措辞与库内 11-16 已记的 CISA 五部门警告完全同源**："最小化网络暴露 / 防火墙隔离 / 必须远程访问时用 VPN / **VPN 只有连接的设备那么安全**" → **"联网可达"这个判据第三次被 CISA 官方强化**。
- ⭐ **报告人 Noureddin Lutfi**（CISA 通告致谢）。
- ⚠️ **我方无 OpenPLC 使用证据**；库内 [EPICS 工控漏洞条目](./epicsDerExposure-2026-11.md) 记的是 EPICS 而非 OpenPLC，**两者不可混为一谈**。

---

## 五、主要观点

**原文主张**

- **CISA 官方**：漏洞让"几个未认证的管理员账号"被创建；受影响版本 ≤4.2.4；修复方式是升级到 4.3.0 或更高；"截至发布日，**没有已知的、专门针对这些漏洞的公开利用被报告给 CISA**"；建议"最小化所有控制系统设备的网络暴露"、"把控制系统网络和远程设备置于防火墙之后并与业务网隔离"、"远程访问必须使用更安全的方式如 VPN，但**也要认识到 VPN 只有它所连接的设备那么安全**"。
- **Aviatrix（第三方攻击链分析）**：攻击者"向用户注册端点打一发并发未认证 POST 突发"，从而"在任何用户被提交前让多个请求通过存在性检查"；拿到管理员级访问后，攻击者会"提权、横向到其它 OT 网段、建立持久 C2、外泄运行配置数据，最终**操纵或破坏 PLC 逻辑**"。
- **Moltbook 第三方评论**（检索命中，非权威）："A race condition does not just break a function. **It invalidates the entire authorization model** by making the existence of a user a moving target."；"**如果运行时不能保证一次检查在对应动作完成前始终为真，这个软件在本质上就是未认证的。**"

**我方判断**

- ⭐⭐⭐ **这条对我方的真正价值是它第一次给库内一条"TOCTOU / 竞态绕过认证"的一手官方证据，而这类失效模式我方此前完全没有对应物**。库内 11 期安全分析覆盖过的攻击手法是：反序列化（11-17）、SSRF（11-17）、凭据收割（11-16）、会话劫持型（Java4Shell 的 SSRF/字节码）、供应链投毒（11-20）、扫描器路径字典（11-15）—— **全部是"输入怎么进来"，没有一条是"并发怎么进来"**。而 OpenPLC 这一条讲的是完全不同的失效轴：**不是攻击者构造了什么，而是系统自己的一个读-改-写序列不是原子的**。⭐⭐ **这类缺陷最难被现有防线覆盖** —— WAF 看得见"请求内容"，看不见"两个请求的时序"；资产清单看得见"版本不对"，看不见"版本对但代码有竞态"。
- ⭐⭐⭐ **"凭据可凭空产生"这条，直接改变了库内 11-16 至 11-20 一路建立的"凭据泄露/凭据被盗"威胁模型的完整性**。库内已记的凭据相关线是：① 外部凭据收割扫描器（11-16，攻击者找 `.env`/`.git/config`）② `agent-framework` 投毒（11-20，被偷的是身份不是密钥）③ vCenter 案例（本批次，签名材料被取走后可伪造令牌）。**这三条的共同前提都是"凭据本来就在系统里，被拿走了"**。**OpenPLC 是第四条、也是第一条"凭据原本不存在、是被漏洞造出来的"** —— 这意味着**我方若只做"凭据泄露排查 + 强制轮换"，会系统性地漏掉这一整类**。⚠️ 反过来说，我方现有的"账号清单"视角同样漏掉它 —— **清单上本来就没有这个账号**。
- ⭐⭐⭐ **"未认证的管理员账号"这个措辞，比"认证绕过"更值得警惕，也更容易被我方在转述时走样**。官方精确说的是"**几个未认证的管理员账号被创建**" —— 账号有管理员权限，但**创建过程不需要凭据**。**这不是"绕过了一次认证"，而是"认证这一步被跳过了"**。库内已记的 [ICSA-26-300-02](./icsa2630002GenesisIconics-2026-11.md) 里那条"密码找回挑战响应对所有用户相同且固定"是**同族但不同构**（那是"认证机制太弱"，这条是"认证机制被绕过"）—— **两者应归入同一大类（账号/认证管理设计缺陷），但子类不同**。
- ⭐⭐ **SSVC 的"automatable = no"必须和 Aviatrix 的攻击链描述一起读**。Aviatrix 描述的"并发 POST 突发"听起来很易自动化，但 SSVC 明确判定自动化不可行 → **现实情况是"需要精细时序控制，攻击门槛高于普通 RCE"**。**但这不改变优先级判断**：因为① 攻击门槛高恰恰意味着**能打的人是有组织的（本次报告人即专业研究者）**；② 一旦成功，落点是**持久化账号 + PLC 逻辑操纵**，在能源行业等于物理影响；③ 官方明确说"无在野利用" —— 而库内 11-19 已记的 Java4Shell 案例证明，**"无在野利用"到"大规模攻击尝试"之间只隔了两天**（11-17 官方警告 → 11-19 GreyNoise 就记录了 150+ 条特征请求）。**因此"无在野利用"在我方语境下应当读作"尚未开始"，而不是"不会开始"。**
- ⭐⭐ **这条的处置路径几乎全部落在"暴露面"而非"漏洞"上** —— 官方给的三条（最小化网络暴露 / 防火墙隔离 / VPN 且 VPN 只与其连接的设备同安全）**与库内 11-16 已记的 CISA 五部门联合警告（CISA + FBI + HHS + USDA + DOT）那份 fact sheet 的四条措施几乎完全重合**（撤出互联网 / 改默认口令 / 打补丁 / 识别并退役 EOL 设备）。**两份独立的官方文件在一个月内给出同一套暴露面优先的处置逻辑 → 我方暴露面自查清单的"联网可达"判据已被官方三次强化**（11-16 五部门警告、11-19 冷链警告、本条 ICS 通告）。而库内 11-16 就已记下"**EOL 设备台账基线完全缺失**"且该待决至今 🔴 未回填 —— **这条 ICS 通告正是那个缺口再一次被点名的证据**。
- ⭐⭐ **"ICSA-26-323-02 正文仍未取得"这件事本身该被处理成一个流程问题**。库内 11-19 记 ICSA-26-323-01/02 时写的是"只登记存在、不做内容判断"，这条纪律本身是对的（不靠 Related Advisories 链接猜内容）。**但结果是：这两条在本库内挂了整整五天，且其中一条的机制（竞态绕过账号创建）在今天拿到正文后被证明是库内完全空白的一类失效模式**。⚠️ **这说明"只登记存在"这个做法虽然严谨，但代价是"库内会持续存在一个自己不知道内容的洞"**。正确做法不是"猜内容"，而是**把"待取正文"变成一条有责任人和期限的显式待办** —— **建议在库内新增一个「CISA ICS 通告正文待取清单」**，逐条登记通告号、发布日期、取回状态、取回责任方。
- ⭐ **本条不产专项整改、不进产品改造** —— 我方无 OpenPLC，且它是我方不使用的第三方 PLC 运行时。**它的价值 100% 在"失效模式入库"与"暴露面判据强化"上**。这个判断必须写清楚，否则会误导评审。

---

## 六、参考意义

| 方向（网络安全/信创/等保/隐私保护/护网） | 可证事实 | 本阶段处理 |
|---|---|---|
| **网络安全**（方向级）· 护网 · 等保 | 竞态条件使"存在性检查"非原子 → 无凭据创建多个管理员账号；CVSS v3.1 8.1 / v4.0 9.2；CWE-362；≤4.2.4，修复 4.3.0；官方点名能源等行业；SSVC exploitation none known / automatable no / technical impact total；MITRE T1136 Create Account（持久化）+ T0821/T0831 工艺影响；官方缓解=最小化暴露/防火墙隔离/VPN（VPN 只与其连接设备同安全）；我方无 OpenPLC 使用证据 | **✅ 进评审（方向级，不新开产物）**。① **影响可证（同类失效模式对我方成立）**：**① 库内首次出现"TOCTOU / 竞态绕过账号创建"这一失效轴** —— 库内 11 期全部攻击手法都属"输入构造"类，**没有"并发时序"类**，而后者恰恰是 WAF 与资产清单**结构上看不见**的一类；**② "凭据可凭空产生"补齐了库内凭据威胁模型的缺口** —— 库内已有的三条凭据线（扫描器收割 / 投毒窃身份 / vCenter 窃签名材料）前提都是"凭据本来就在系统里"，**这一条是"凭据原本不存在、被漏洞造出来"** → **我方只做凭据泄露排查 + 强制轮换会系统性漏掉这一整类**；**③ 账号清单视角同样漏掉它**（清单上本来就没有这个账号）→ **需补"运行时可自增账号"的审计维度**；**④ "无在野利用"应读作"尚未开始"**（库内 11-19 Java4Shell 案例：官方警告到大规模攻击尝试只隔两天）。② **动作明确**：**防线覆盖度对照表新增"TOCTOU / 竞态绕过账号创建"手法族**；**暴露面自查清单增"运行时账号可自增"审计项**（含自增账号的发现与告警）；**账号/凭据基线增"凭据凭空产生"这一威胁类别**；**新建「CISA ICS 通告正文待取清单」**（登记通告号、发布日期、取回状态、责任方），把"只登记存在"从纪律升级为**有期限的待办**；**"联网可达"判据在暴露面自查中升格为一级筛选条件**（本条官方措辞与库内 11-16 五部门警告同源，已第三次被强化）。③′ 方向归属明确；④ 可验收：逐条挂"手法族是否已加 / 自增账号审计项是否已加 / 威胁类别是否已补 / 通告待取清单是否已建 / 联网判据是否已升格"的结论。⚠️ **本条不宣称"我方受影响"**（我方无 OpenPLC 使用证据），**不产专项整改** |

---

## 七、总结输出

**一句话结论**：**OpenPLC 这条的技术内容对我方几乎无用（我方不用它），但它第一次把库内缺失的一整类失效模式摆到了台面上 —— 一个"存在性检查"被当成原子操作，于是攻击者无需任何凭据就能凭空造出多个管理员账号；这既补齐了库内凭据威胁模型的最后一角（此前三条线的前提都是"凭据本来就在系统里"），也暴露了我方 WAF 与资产清单结构上看不见"并发时序"这类攻击；而我方真正该记住的是官方的处置逻辑 —— 它和库内 11-16 已记的 CISA 五部门警告一字不差地指向"联网可达"，这是官方第三次强化这条判据，也第三次点到我方那个至今未回填的"EOL 设备台账"缺口。**

**落地去向**
- [ ] 产品特性
- [ ] 需求变更
- [x] **专项整改** —— 🟡 **方向级待复核**：并入既有 [remediation-defenseTacticCoverage-20261112](../deliverables/remediation-defenseTacticCoverage-20261112.md)（新增"TOCTOU / 竞态绕过账号创建"手法族）
- [ ] **跟踪项** —— ① **暴露面自查清单增"运行时账号可自增"审计项**（含自增账号的发现与告警 —— WAF 看不见时序，但"账号凭空多出来"是可观测的）；② **账号/凭据基线增"凭据凭空产生"威胁类别**；③ **新建「CISA ICS 通告正文待取清单」**（通告号 / 发布日期 / 取回状态 / 责任方），**ICSA-26-323-02（Elecbrakes）正文待取即登记在此**（库内 11-19 已登记其存在但未取正文）；④ **"联网可达"判据在暴露面自查中升格为一级筛选条件**；⑤ **"EOL 设备台账"基线缺失项再次被官方点名 —— 库内 11-16 起挂至今 🔴 未回填，建议本期一并回填**

---

## 参考链接

- [CISA ICS 通告 ICSA-26-323-01：Autonomy Logic OpenPLC Runtime（Release Date November 19, 2026）](https://www.cisa.gov/news-events/ics-advisories/icsa-26-323-01)
- [Defcon Level：CISA Cybersecurity Advisories — Autonomy Logic OpenPLC Runtime (ICSA-26-323-01)（官方通告全文转载）](https://www.defconlevel.com/alert/2026-11-19-cisa-cybersecurity-advisories-autonomy-logic-openplc-runtime-icsa-26-323-01)
- [Aviatrix：Race to Admin — How CVE-2026-126088 Lets Attackers Create Rogue Accounts in OpenPLC Runtime（攻击链与 ATT&CK 映射）](https://aviatrix.ai/threat-research-center/icsa-26-323-01-openplc-runtime-race-condition-cve-2026-126088)
- [NEOSEC / NVD：CVE-2026-126088（含 CVSS 双评分与 CISA SSVC 评估）](https://intel.neosec.eu/en/cve/CVE-2026-126088)
- [CISA Known Exploited Vulnerabilities Catalog（该 CVE 未收录）](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [库内相关：CISA ICSA-26-323-03 libumqtt 整数下溢（同批次 · 该条记录了 ICSA-26-323-01/02 正文未取得的待办）](./libumqttCve2026125132-2026-11.md)
- [库内相关：EPICS 工控漏洞 + 光伏 DER 暴露面（2026-11 双信号）](./epicsDerExposure-2026-11.md)
- [库内相关：CISA ICSA-26-300-02 三菱/ICONICS 平台四漏洞（认证设计缺陷同族）](./icsa2630002GenesisIconics-2026-11.md)
- [库内相关：CISA 五部门联合警告：联网辅助设备攻击面（2026-11-05 · "联网"判据首现）](./cisaRefrigerationColdChain-2026-11.md)
- [既有产物：攻击手法→防线覆盖度对照（专项整改 · P1 · 方向级）](../deliverables/remediation-defenseTacticCoverage-20261112.md)

# Danfoss AK-SM 8xxA 制冷控制器（CVE-2026-129713）—— 库内首条「已进入在野攻击阶段的 OT 设备」，且法国已把攻击归因到伊朗 IRGC 部队

> 🔴 强约束 · 采集于 2026-11-25 · **最新动态 last_seen 2026-11-26 07:11** · 核心标识：**⭐⭐⭐ 库内首条「从 CISA 联合警告升级为真实在野攻击并被国家级归因」的 OT 设备线 —— CISA 2026-11-24 发布 ICSA-26-328-03，为 Danfoss AK-SM 8xxA 免认证 CGI 处理器栈溢出（CVE-2026-129713，CVSS v3.1 9.8 / v4.0 9.3）分配 CVE** · ⭐⭐⭐ **库内首条「国家级归因」：法国外交部 2026-11-09 将 10 月 11-12 日那波法国零售门店制冷系统攻击归因于伊朗 IRGC 革命卫队「Shahid Kaveh」单位，且明确「仅该次战役」** · ⭐⭐⭐ **库内首条「攻击产生了物理后果」的样本 —— 攻击者把门店冷柜强制进入 50℃ 连续化霜状态（正常为 24 小时内 2 小时化霜）** → 温控被当成攻击武器 · ⭐⭐⭐ **库内首条「CISA 官方明确记录 CVE 仍在无补丁状态」：修复版 5.5.x 尚未发布，Danfoss 同时宣布将取消「关闭 Strict Mode」的选项** · ⭐⭐ **更狠的是 CVE-2026-127057（CVSS 9.9）：Danfoss AK-SC 355 与 AK-SM 800 全系默认凭据「写在产品手册里」→ 查手册即得口令，且官方称「所有版本受影响、无修复」** · ⭐⭐⭐ **库内首条「把暴露面关掉比打补丁更重要」的官方判据 —— CCB 明确指出 Strict Mode 也不解决问题（会话控制另有缺陷），CERT-FR 明确「仅恢复出厂设置是不够的」** · ⭐⭐ **可量化的暴露面实测：Censys 扫描法国 StoreView 控制面板 1,825 → 537 台（10-11 → 10-14，−71%），库内首次取得「联网 OT 面板的实测下线率」** · ⚠️ **我方无 Danfoss 使用证据 → 不得下「我方受影响」结论**；⚠️ **CISA 等五部门明确「公开信息不能证明这些事件共享同一攻击方法，也不能确认对上述 Danfoss CVE 的利用」**；⚠️ **与库内 11-16 已记的 CISA 制冷冷链联合警告属同一产品线但不同事件 → 本篇是它的「案卷升级」**

---

## 一、信源核实

| 项 | 值 |
|---|---|
| 来源请求 | `CISA ICSA Danfoss AK-SM 8xxA refrigeration controller CVE-2026-129713`（web_search）<br>`Azure API Management flaw Equinor Skagerak Energi Norway NSM secrets compromised November 2026`（web_search，安全域横向检索时命中含 Danfoss 战役复盘的 CTI Daily Brief） |
| 原始 URL（主 1 · 官方 ICS 通告） | https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-03 （CISA **ICSA-26-328-03**，**Release Date November 24, 2026**，快照正文 5,913 字符） |
| 原始 URL（主 2 · 厂商官方通告） | https://www.danfoss.com/en/service-and-support/coordinated-vulnerability-disclosure/danfoss-security-advisories/dsa-2026-12-01/ （Danfoss **DSA-2026-12-01**，**2026-11-20**，快照正文 1,687 字符） |
| 原始 URL（辅 1 · 第三方技术分析） | https://cyfar.ca/posts/danfoss-ak-sm-8xxa-series-cve-2026-129713 （Cyfar，**2026-11-24 17:11**，含 ATT&CK 映射与检测建议） |
| 原始 URL（辅 2 · 战役级复盘 · 多国多源汇编） | https://ctipilot.ch/daily/2026-10-13 （CTI Pilot《CTI Daily Brief · 2026-10-13》，**2026-10-13**，逐条标注 CERT-FR / NCSC CH / 法国外交部 / Midnight Blue / Censys / BSI 等原始出处，快照正文 60,018 字符，已截断） |
| 原始 URL（辅 3 · OT 运维视角通告聚合） | https://www.redtigersecurity.com/advisories （Red Tiger Security《Security Advisories & OT Threat News》，**11-24 当日条目含本条与 CERT@VDE 摘要**，快照正文 45,740 字符） |
| 原始 URL（辅 4 · 同产品族另一 CVE） | https://ctiwatch.com/vulnerabilities/CVE-2026-127057 （CTIWatch，**2026-11-20**，快照正文 3,540 字符） |
| 发布主体 | CISA（ICS 通告与 CVE 分配方）· Danfoss（丹麦，厂商与 CVD 发布方）· Midnight Blue（研究方，Carlo Meijer 上报）· CERT-FR / NCSC 瑞士 / 法国外交部 / BSI / Censys / CERT@VDE（战役级官方与测量来源） |
| 发布/更新时间 | **CISA 通告：2026-11-24**（Initial Publication）· **Danfoss 通告：2026-11-20** · CVE 公开：2026-11-20 · **法国归因：2026-11-09** · 法国战役本体：2026-10-11 ~ 10-12 · Midnight Blue 报告六漏洞：2026-11-11 · 库内采集：**2026-11-25 07:33:53 – 07:34:41** |
| 采集时间 | 2026-11-25 07:33:53 – 07:34:41 |
| 快照 | `raw/snapshots/security/cisa-icsa-26-328-03-danfoss-ak-sm.md` · `danfoss-dsa-2026-12-01.md` · `cyfar-danfoss-ak-sm-129713.md` · `ctipilot-danfoss-france-oct2026.md` · `redtiger-advisories-20261124.md` · `ctiwatch-danfoss-127057.md` |

**快照清单**（SHA256 取自 `.meta.json` 的 `sha256_raw`）

| 快照 | SHA256 | 抓取时间 | 正文字符 | HTTP |
|---|---|---|---|---|
| `raw/snapshots/security/cisa-icsa-26-328-03-danfoss-ak-sm.md` | `b80eed8f0568c5284467546d2ff4a4ea7392b26d418abf972abf7c89720f95e7` | 2026-11-25 07:33:53 | 5,913 | 200 |
| `raw/snapshots/security/danfoss-dsa-2026-12-01.md` | `f40c776dc0dd54e46c4b890d5aa5a6ce6edf40fba1bb3fc1593859abd93a2182` | 2026-11-25 07:33:55 | 1,687 | 200 |
| `raw/snapshots/security/cyfar-danfoss-ak-sm-129713.md` | `9edb14d536bcd70d62e244b2700edd87ba7cd7cd4f40ccfc020d08a753ced79b` | 2026-11-25 07:33:57 | 2,074 | 200 |
| `raw/snapshots/security/ctipilot-danfoss-france-oct2026.md` | `c8931b2f29374b96b992e8970f41a0ac5d307890fe02eb62e5ce269bb1a2bb2b` | 2026-11-25 07:34:39 | 60,018 | 200 |
| `raw/snapshots/security/redtiger-advisories-20261124.md` | `4fac91efb35158aea86a962d666fa003fd00ac9bffea3827c66a9cb1e7f6d05c` | 2026-11-25 07:34:40 | 45,740 | 200 |
| `raw/snapshots/security/ctiwatch-danfoss-127057.md` | `b6b00c3ed0525bbcafa88aac455203ffb940b3e50bf4a3d4667af2cbe68bfdd8` | 2026-11-25 07:34:41 | 3,540 | 200 |

> 📎 **入库理由**：库内 11-16 已记 [CISA 等五部门联合警告「联网辅助设备是被点名的攻击面」](cisaRefrigerationColdChain-2026-11.md)，那篇是**警告**（fact sheet + 缓解措施），且当时明确"还没有可归因的具体战役"。**本篇是那篇的案卷升级**：① **同一产品族已出现真实在野攻击**（法国、至少六个其他欧洲国家、瑞士，含法国血液服务三处站点）；② **攻击已被一个国家正式归因到 IRGC 部队**（库内首条国家级 OT 攻击归因）；③ **攻击产生了物理后果**（强制化霜 50℃）—— **库内所有 OT 条目至今都是"信息泄露 / 拒绝服务 / 权限提升"，没有一条是"物理过程被操纵"**；④ **官方明确给出"先把设备从公网撤下来"的优先级**，并证明「恢复出厂设置不够」「Strict Mode 也不够」—— **这直接补上库内 11-19 与 11-24 反复出现的"配置类缓解会不会悄悄失效"这一担忧的实证**。
> ✅ **双信源要求已满足**：官方源（CISA ICS 通告 + Danfoss 厂商通告，两份独立一手）+ 第三方源（Cyfar 技术分析、CTI Pilot 战役级多国汇编、Red Tiger OT 运维视角、CTIWatch 评分分析）。

---

## 二、事实核查

| 数据点 | 原文表述 | 核查方式 | 结论 | 备注 |
|---|---|---|---|---|
| 1 | **⭐⭐⭐ CVE 与受影响范围** | CISA ICSA-26-328-03 快照逐字：*"**Danfoss AK-SM8xxA <=5.4.0 (CVE-2026-129713)**"*；Danfoss DSA-2026-12-01 快照逐字：*"**Danfoss AK-SM 8xxA - version 5.4.0 and earlier**"*；漏洞描述逐字：*"A **stack-based buffer overflow in an unauthenticated CGI handler** of the Danfoss AK-SM 8xxA Series controller allows remote attackers to send specially crafted HTTP/S POST requests, leading to memory corruption, webserver restart and hypothetically potential arbitrary code execution with webserver privileges. **Authentication is not required to exploit this vulnerability.**"* | 三源（CISA + Danfoss + Cyfar）逐字比对 | ✅ **已核** | ⭐⭐⭐ **根因极其干净：免认证的 CGI 处理器里一个栈溢出** → **不需要任何凭据、不需要任何交互、只需要一条构造过的 HTTP/S POST** → 这是可被完全自动化批量扫描利用的形态（Cyfar 的 ATT&CK 映射：T1190 Exploit Public-Facing Application → T1499 Endpoint Denial of Service）。⭐⭐ **"hypothetically potential" 这个措辞必须保留** —— 官方自己把代码执行写成"假想的" |
| 2 | **⭐⭐⭐ 评分三套并存** | CISA 快照逐字：**CVSS v3.1 = 9.8**（`CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`）、**CVSS v4.0 = 9.3**（`CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/vi:H/va:H/SC:N/si:N/sa:N`）；Danfoss 厂商通告自评 **CVSS 9.3**；CWE-121 | CISA + Danfoss 双源比对 | ✅ **已核** | ⭐⭐ **注意 Danfoss 通告只印了一个 9.3（那是 v4.0 口径），而 CISA 同时给了 v3.1 的 9.8** → **库内 11-24 已记 LiteLLM / phpAfterShell 的"多套评分并存"问题，此处是同一现象**，**引用时必须写明口径（v3.1 9.8 / v4.0 9.3），不得只写一个 9.8**。⚠️ ctiwatch 快照把 9.3 标为"CVSS v3.1"、securitydaily 则标 9.8 为 v3.1 —— **第三方口径有错标，以 CISA 官方为准** |
| 3 | **⭐⭐⭐ 修复状态：无补丁** | CISA 快照逐字：*"**Product Status: known_affected**"*；*"This vulnerability will be addressed in an upcoming Danfoss AK-SM 800A Series software release (**version 5.5.x**). **In addition, Danfoss will remove the ability for users to disable Strict Mode in future software releases.**"*；Danfoss 通告逐字同 | CISA + Danfoss 双源一致 | ✅ **已核** | ⭐⭐⭐ **"known_affected" 是 CISA 对「已确认受影响、尚未修复」的正式状态标注** → 与库内 libumqtt（*"None available —— 维护者未响应协调请求"*）不同，本条是**厂商承认、承诺未来版本修** → **比 libumqtt 乐观，但当下同样无补丁可用**。⭐⭐ **"取消关闭 Strict Mode 的选项"是一条被我方低估的官方动作** → 厂商在**收紧**配置面，说明此前"用户可关掉严格模式"本身被视为风险来源 → **迁移到我方：可被用户关闭的安全开关是一个需要被记录的基线事实** |
| 4 | **⭐⭐⭐ 库内首条国家级归因** | CTI Pilot 快照逐字：*"on **2026-11-09 France's foreign ministry attributed the 11 to 12 October campaign, and only that campaign, to the Iranian unit Shahid Kaveh**"*；同页列出受影响方：*"Coopérative U, Intermarché and E. Leclerc confirmed to AFP on 2026-10-12 a cyberattack on their refrigeration systems"* | CTI Pilot 快照（逐条标注法国外交部为出处）+ Red Tiger 快照独立记载 CERT-FR 战役 | ✅ **已核（CTI Pilot 逐条标注出处 + Red Tiger 独立交叉）** | ⭐⭐⭐ **库内首条国家级 OT 攻击归因**。⭐⭐⭐ **但必须把限定词一起写：「仅该次战役」** —— **法国明确只归因 10 月 11-12 日那一波，不是后续的跨国扩散**。⚠️ **归因对象是「伊朗 IRGC 的 Shahid Kaveh 部队」这一个单位，不得写成"伊朗"整体，更不得外推到其它战役** |
| 5 | **⭐⭐⭐ 攻击产生物理后果** | CTI Pilot 快照逐字（AFP via Khaleej Times，2026-10-12）：*"the hackers would have hijacked this function by imposing a **forced and continuous defrost, with a temperature setpoint fixed at 50 degrees**"*；同页 BFMTV 逐字：*"installations can be programmed for **two hours of defrost per 24 hours**, whereas the reported attack is a **continuous forced defrost at a 50-degree setpoint***" | CTI Pilot 快照内两条独立原始出处（AFP / BFMTV）互证 | ✅ **已核（双原始出处）** | ⭐⭐⭐ **库内首条「攻击直接操纵物理过程」的证据**：正常化霜 24 小时内 2 小时，被改为**持续化霜且目标温度 50℃** → **温控参数本身成为攻击载荷**。⭐⭐ **这条改变了我方对 OT 风险的理解层级**：库内此前所有 OT 条目的后果都停留在信息层（泄露、拒绝服务、提权），**本条的后果是"设备按攻击者设定的物理量持续运行"** → **这是"可观测、可测、可调、可控"四个字里"可调"被恶意使用** |
| 6 | **⭐⭐⭐ 受害范围（跨七国）** | CTI Pilot 快照逐字：*"**more than 115 stores in at least six more countries** and the first German shops on 2026-11-02, **altered cold-room settings at three sites of the French blood service through a supplier**, and, per SRF on 2026-11-05, a Köniz butcher and three Volg stores in Switzerland"*；CERT-FR 逐字：*"numerous compromises of the remote refrigeration-installation controllers **Danfoss AK-SM and AK-SC series as well as Copeland xweb and Dixell xweb**"*；NCSC 瑞士逐字：*"**Actively Exploited**"*（advisory 13054，2026-10-13） | CTI Pilot 快照逐条（含 CERT-FR / NCSC CH / SRF / AFP / Cooling Post / Blick 等原始出处） | ✅ **已核** | ⭐⭐⭐ **受害面已经不只是 Danfoss 一家**：**Copeland xweb 与 Dixell xweb 同样被批量攻陷** → **"制冷控制器"是一个产品类别暴露面，不是一个产品暴露面**。⭐⭐⭐ **法国血液服务三处站点被经由供应商篡改冷库设定 —— 这一条对我方最有分量**：**它说明攻击已经打到「医疗冷链」这种后果极严重的场景，而路径是"通过供应商"** → **直接对应库内 11-25 已记的「供应商/MSP 代运维实例是影子密钥存活地」以及库内 11-16 已记的「第三方远程访问 OT」** |
| 7 | **⭐⭐⭐ CVE-2026-127057：默认凭据写在手册里** | CTI Watch 快照逐字：*"**Danfoss legacy AK-SC 355 and AK-SM 800 Series shipped with default credentials that are written in the product manual**, so anyone who knows or looks up those passwords can log in without authorization."*；官方描述逐字：*"These products were **manufactured with default credentials documented in the product manual. All versions are affected.**"*；CTI Pilot 快照亦记载 Danfoss **DSA-2026-12-02**（2026-11-20）同批发布 | CTI Watch + CTI Pilot 双源 | ✅ **已核** | ⭐⭐⭐ **这是库内首条「默认凭据被官方文档公开写明」的样本 —— 攻击者不需要任何漏洞，只需要下载产品手册** → **等价于"把密钥写在了公开文档里"**，与库内 11-20 agent-framework 的「窃取的是身份」是同一类问题的极端形态：**身份本身是公开的**。⭐⭐ **CVSS 9.9（CTI Watch 快照）**、**全部版本受影响、官方无修复** → 官方建议是**替换设备**（NCSC 瑞士逐字：*"no fixes exist for the two older models and that Danfoss urges replacing them"*）。⚠️ **CTI Watch 同时给出：未入 KEV、无公开利用、EPSS 无分数** |
| 8 | **⭐⭐⭐「关掉暴露面比打补丁更重要」是官方结论** | CTI Pilot 快照逐字（CCB，2026-11-12）：*"the research also finds **a flaw in session control, so Strict mode does not remove the risk**"*；同页逐字（CCB）：*"**updating, new passwords and Strict mode are insufficient, so removing internet exposure comes first**"*；CERT-FR（2026-10-13 修订）逐字：*"**an unpatched end-of-life unit kept on the internet is very likely to be compromised, so a factory reset alone is insufficient**"*；CERT-FR（10-16 版）逐字：*"For every unit it asks to **remove the internet exposure** of the affected units and of any unit on a public IP address"*，并把源地址过滤降级为 *"an emergency measure and not a lasting one"* | CTI Pilot 快照内三条独立原始出处（CCB / CERT-FR 两版） | ✅ **已核** | ⭐⭐⭐ **这是本篇最可落地的一条**：**法国国家级 CERT 与比利时 CCB 都独立得出「先撤出公网」这个结论，且明确「恢复出厂设置不够」「Strict Mode 不够」「改密码不够」**。⭐⭐⭐ **它实证了库内 11-19 与 11-24 的核心担忧**：**配置类缓解措施确实会失效**，而且**这里连厂商的自家开关都不够** → **唯一稳定有效的处置是拓扑级的（不上公网）+ 生命周期级的（替换 EOL 设备）**。⚠️ **CERT-FR 明确说源地址过滤只是应急手段、不是长久之计** → **不得把 IP 白名单写成正式缓解方案** |
| 9 | **⭐⭐⭐ 暴露面实测：Censys 扫描数据** | CTI Pilot 快照逐字（Censys，2026-10-14）：*"Its scan counted **1,825 exposed StoreView panels in France on 2026-10-11 and 537 on 2026-10-14, a fall of 71 percent**, with builds below 4.2, build 4.2.4 and builds from 4.3.1 leaving at about the same rate, which it reads as **operators taking controllers off the internet rather than patching them**. Outside France the count fell from **1,166 to 966**, and in ten of the twelve countries with the most exposed hosts **more than 60 percent of the hosts run a build below 4.3.1**, led by **Poland at 81 percent and Romania at 80 percent**"* | CTI Pilot 快照逐字 | ✅ **已核（单源，但含完整可复算数据）** | ⭐⭐⭐ **库内首条「联网 OT 控制面板的实测下线率」** —— 这是**可证伪的公开测量**，比任何定性描述都硬。⭐⭐⭐ **最关键的结论是 Censys 的判读：版本分布没有变化而数量下降 71% → 运营者是在「把设备从公网撤下来」而不是「打补丁」** → **独立印证了第 8 条的官方结论**。⭐⭐ **法国 −71%、境外仅 1,166 → 966（−17%）** → **暴露面收敛速度高度不均**。⭐⭐ **波兰 81%、罗马尼亚 80% 的主机版本低于 4.3.1** → **"未修补且暴露"是绝大多数，而非少数**。⚠️ **该数据是 2026-10 的，不可直接当作当前状态**；⚠️ **Censys 扫描的是 StoreView 控制面板，不等于全部控制器** |
| 10 | **漏洞利用与在野证据的边界** | CISA 快照逐字：*"**No known public exploitation specifically targeting these vulnerabilities has been reported to CISA at this time.**"*；**但** CTI Pilot 快照逐字（CISA 五部门）：*"The public information reviewed **does not establish a common attack method across these incidents or confirm exploitation of the specific Danfoss CVEs listed above.**"*；Cyfar 快照：*"no public exploitation has been reported to CISA"* | CISA + CTI Pilot 内的 CISA 五部门声明，两源一致 | ✅ **已核（边界必须写明）** | ⭐⭐⭐ **这里有一个必须精确表述的分离：① 设备在野被大规模攻陷是确认的（CERT-FR / NCSC 瑞士 Actively Exploited）；② 但「攻击用的就是 CVE-2026-129713 / 127057 这两条具体漏洞」并未被公开信息证实** —— CISA 五部门自己明说了。⭐⭐ **正确写法：「Danfoss AK-SM/AK-SC 控制器已被在野批量攻陷（NCSC 瑞士标记为 Actively Exploited），但公开信息不能确认攻击者使用的正是 CVE-2026-129713 这条未授权 CGI 栈溢出」**。⚠️ **不得把"设备被攻陷"直接写成"该 CVE 被在野利用"** |
| 11 | **披露与归因的时序** | CTI Pilot 快照逐字：*"On **2026-11-11 Midnight Blue reported six pre-authentication remote-code-execution flaws in all Danfoss AK-SM 800A firmware up to 5.3.2**, and on **2026-11-20 Danfoss published CVE-2026-129713** … and CVE-2026-127057"*；同页逐字：*"Danfoss assigned CVE-2026-129713 … **without saying if it is one of the six**"* | CTI Pilot 快照逐字 | ✅ **已核** | ⭐⭐ **「CVE-2026-129713 是否就是那六条中的一条，Danfoss 没有说明」** → 这是一条必须写明的**待核项**：**官方编号的 CVE 与研究者报告的六条漏洞之间的对应关系未公开**。⭐⭐ **另外「BACS 2026-11-10 声称更新已修复已知漏洞」的说法早于 Midnight Blue 报告、且不覆盖那六条** → **厂商的"已修复"表述与研究者的"六个未修"存在时间与范围错位** → 库内 11-24 已记 phpAfterShell「补丁不修它」，这是同一类现象的又一实例 |
| 12 | **EOL 设备的处置结论** | CTI Pilot 快照逐字（Danfoss 对 Cooling Post）：*"the **AK-SM800 was declared end of life in 2021**, that the **AK-SC355 was phased out in 2016**"*；NCSC 瑞士逐字：*"lists the Danfoss AK-SM 800 (**end of life, no longer patched**), the AK-SC 355 (**phased out, no longer patched**) … says **no fixes exist for the two older models and that Danfoss urges replacing them**"* | CTI Pilot 快照内两条原始出处 | ✅ **已核** | ⭐⭐⭐ **这条给出了库内至今最硬的一条生命周期判据**：**一款制冷控制器可以在 2016 年停产、2021 年 EOL、2026 年被国家级 CERT 判定为无补丁且建议替换** → **"在用设备是否还在厂商支持期"必须成为暴露面台账的一等字段**。⭐⭐ **库内 11-16 已记 CISA 五部门警告里提到「联网温控器 / 商用制冷控制器」这个攻击面，但没有"生命周期"这一维** → 本条把它补上。⭐⭐⭐ **它同时和库内 11-24 已记的「EOL 设备台账完全缺失」那条待办精确对上** —— **现在有了具体的产品与具体的时间线作为范例** |
| 13 | 其他受影响厂商 | CTI Pilot 快照逐字（BSI，2026-11-17）：*"**BSI reports exploitation attempts against two Copeland XWEB EVO flaws**"*；CERT-FR 逐字：compromised 名单含 *"**Copeland xweb and Dixell xweb**"* | CTI Pilot 快照 | ✅ **已核（单源，标注 BSI / CERT-FR 为原始出处）** | ⭐⭐ **Copeland XWEB EVO 已有「利用尝试」（不是确认攻陷）** → **同一类控制器（商用制冷压缩机控制器）在多家厂商身上同时暴露** → **库内该做的是"按类别而非按品牌"做暴露面自查** |
| 14 | **官方缓解建议（CISA）** | CISA 快照逐字：*"**Minimize network exposure** for all control system devices and/or systems, ensuring they are not accessible via the internet. Locate control system networks and remote devices behind firewalls and isolating them from business networks. When remote access is required, use more secure methods, such as **Virtual Private Networks (VPNs)**, recognizing VPNs may have vulnerabilities and should be updated to the most current version available."* | CISA 快照逐字 | ✅ **已核** | ⭐⭐ **注意 CISA 自己加了一句「VPN 本身可能有漏洞、须保持更新」** → 与库内 11-19 已记的「CISA 官方口径『unpatched **or internet-accessible**』」同向：**联网可达性优先于是否已打补丁**。⭐⭐ **这条与 Danfoss 厂商自己的建议（不暴露公网、只走 VPN、启用 Strict Mode、强口令）完全一致** → **厂商与 CISA 口径一致，可信度高** |
| 15 | 我方侧现状 | — | 库内检索：`grep -rn "Danfoss\|AK-SM\|AK-SC\|IRGC\|Shahid" src/` → **库内 11-16 已记的 [CISA 制冷冷链联合警告](cisaRefrigerationColdChain-2026-11.md) 是唯一相关条目，且那篇只记了"联网辅助设备是被点名的攻击面"这层警告，未记 Danfoss、无战役、无归因** | ⚠️ **库内无我方使用 Danfoss/Copeland/Dixell 设备的一手证据 → 不得下"我方受影响"结论** | ⭐⭐⭐ **但这条本身是一次有价值的库内升级**：库内 11-16 那篇的主题（"联网辅助设备"）**在本篇之后从"警告"变成"有案卷"** → **库内 11-16 那篇的「最新动态」节应当指向本篇** |

**核查小结**：**本条无来源级数字冲突**（CISA 通告、Danfoss 通告、Cyfar、CTI Pilot、Red Tiger、CTI Watch 六源在受影响版本、根因、评分、修复状态、缓解措施上完全一致），**但存在 1 处评分口径错标**（第三方把 9.3 标为 v3.1，官方为 v3.1 9.8 / v4.0 9.3，以官方为准）、**1 处待核的编号对应关系**（CVE-2026-129713 是否属那六个未修漏洞之一，官方未说明）、**1 处必须写明的证据边界**（设备在野被攻陷 ≠ 该 CVE 被在野利用，CISA 五部门明文如此）。**另有 4 项硬边界**：无公开利用证据、无 EPSS、未入 KEV、攻击手法未获公开证实。

---

## 三、原文归档（快照）

- 快照文件：`raw/snapshots/security/cisa-icsa-26-328-03-danfoss-ak-sm.md`（官方）、`danfoss-dsa-2026-12-01.md`（厂商）、`cyfar-danfoss-ak-sm-129713.md`、`ctipilot-danfoss-france-oct2026.md`、`redtiger-advisories-20261124.md`、`ctiwatch-danfoss-127057.md`
- SHA256：`b80eed8f0568c5284467546d2ff4a4ea7392b26d418abf972abf7c89720f95e7`（CISA）/ `f40c776dc0dd54e46c4b890d5aa5a6ce6edf40fba1bb3fc1593859abd93a2182`（Danfoss）/ `9edb14d536bcd70d62e244b2700edd87ba7cd7cd4f40ccfc020d08a753ced79b`（Cyfar）/ `c8931b2f29374b96b992e8970f41a0ac5d307890fe02eb62e5ce269bb1a2bb2b`（CTI Pilot）/ `4fac91efb35158aea86a962d666fa003fd00ac9bffea3827c66a9cb1e7f6d05c`（Red Tiger）/ `b6b00c3ed0525bbcafa88aac455203ffb940b3e50bf4a3d4667af2cbe68bfdd8`（CTIWatch）
- 抓取时间：2026-11-25 07:33:53 – 07:34:41 · HTTP 200 · 正文 5,913 / 1,687 / 2,074 / 60,018 / 45,740 / 3,540 字符

**关键原文摘录（CISA ICSA-26-328-03 官方通告，逐字）**：

> *"**Release Date November 24, 2026** · **Alert Code ICSA-26-328-03**"*
> *"**Danfoss AK-SM8xxA <=5.4.0 (CVE-2026-129713)**"*
> *"**A stack-based buffer overflow in an unauthenticated CGI handler of the Danfoss AK-SM 8xxA Series controller allows remote attackers to send specially crafted HTTP/S POST requests, leading to memory corruption, webserver restart and hypothetically potential arbitrary code execution with webserver privileges. Authentication is not required to exploit this vulnerability.**"*
> *"**Product Status: known_affected**"*
> *"This vulnerability will be addressed in an upcoming Danfoss AK-SM 800A Series software release (**version 5.5.x**). **In addition, Danfoss will remove the ability for users to disable Strict Mode in future software releases.**"*
> *"**CWE-121 Stack-based Buffer Overflow**"* · *"**CVSS Version 3.1 Base Score 9.8 Critical** · CVSS Version 4.0 Base Score 9.3 Critical"*
> *"**Carlo Meijer of Midnight Blue reported CVE-2026-129713 to CISA.**"*
> *"**Critical Infrastructure Sectors: Commercial Facilities** · Countries/Areas Deployed: Worldwide · Company Headquarters Location: Denmark"*
> *"**No known public exploitation specifically targeting these vulnerabilities has been reported to CISA at this time.**"*

**关键原文摘录（Danfoss 官方通告 DSA-2026-12-01，逐字）**：

> *"**Advisory ID: DSA-2026-12-01** · CVE number: **CVE-2026-129713** · **CVSS: 9.3**"*
> *"**Remediations: This vulnerability will be addressed in Danfoss AK-SM 8xxA Series upcoming software version 5.5.x. Further, we will remove the option that customers can disable the product Strict mode.**"*
> *"**Mitigations:** Follow the instructions provided in the product's manual, **avoiding Internet exposure of all units on public IP** · Make sure remote access to the units is possible only through **a secure VPN** or in general over a protected network · **Configure the units to Strict mode** · Recommend using strong passwords"*

**关键原文摘录（CTI Pilot 战役级复盘，逐条标注原始出处）**：

> *"on **2026-11-09 France's foreign ministry attributed the 11 to 12 October campaign, and only that campaign, to the Iranian unit Shahid Kaveh**"*（法国外交部，2026-11-09）
> *"the hackers would have hijacked this function by imposing a **forced and continuous defrost, with a temperature setpoint fixed at 50 degrees**"*（AFP via Khaleej Times，2026-10-12）
> *"installations can be programmed for **two hours of defrost per 24 hours**, whereas the reported attack is a **continuous forced defrost at a 50-degree setpoint**"*（BFMTV，2026-10-12）
> *"**altered cold-room settings at three sites of the French blood service through a supplier**"*（CTI Pilot 汇总）
> *"**the research also finds a flaw in session control, so Strict mode does not remove the risk** … **updating, new passwords and Strict mode are insufficient, so removing internet exposure comes first**"*（CCB，2026-11-12）
> *"**an unpatched end-of-life unit kept on the internet is very likely to be compromised, so a factory reset alone is insufficient**"*（CERT-FR 修订版，2026-10-13）
> *"Its scan counted **1,825 exposed StoreView panels in France on 2026-10-11 and 537 on 2026-10-14, a fall of 71 percent** … which it reads as **operators taking controllers off the internet rather than patching them** … led by **Poland at 81 percent and Romania at 80 percent**"*（Censys，2026-10-14）
> *"the **AK-SM800 was declared end of life in 2021**, that the **AK-SC355 was phased out in 2016**"*（Danfoss 对 Cooling Post）
> *"The public information reviewed **does not establish a common attack method across these incidents or confirm exploitation of the specific Danfoss CVEs listed above.**"*（CISA / FBI / HHS / USDA / DOT 联合声明）

---

## 四、概要提取

- ⭐⭐⭐ **库内首条「OT 设备在野被批量攻陷并被国家级归因」的案卷**：法国零售门店（Coopérative U / Intermarché / E. Leclerc）10 月 11-12 日遭攻击，**法国外交部 11-09 将该次战役（且仅该次）归因于伊朗 IRGC「Shahid Kaveh」部队**；扩散至**至少六个其他国家的 115 家以上门店**与瑞士（NCSC 瑞士标记 **Actively Exploited**）。
- ⭐⭐⭐ **库内首条「攻击直接操纵物理过程」的证据**：攻击者把门店冷柜改为**持续化霜、目标温度锁定 50℃**（正常为 24 小时内化霜 2 小时）→ **温控设定值本身成为攻击载荷**。
- ⭐⭐⭐ **库内首条「攻击通过供应商打到医疗冷链」的证据**：**法国血液服务三处站点**的冷库设定经由供应商被篡改 → **第三方远程维护路径是真实可达的攻击路径**。
- ⭐⭐⭐ **CISA 11-24 发布 ICSA-26-328-03**：Danfoss AK-SM 8xxA ≤5.4.0 免认证 CGI 处理器栈溢出（CVE-2026-129713，v3.1 9.8 / v4.0 9.3，CWE-121），**Product Status = known_affected（当前无补丁）**，修复版 5.5.x 尚未发布，**Danfoss 同时宣布取消「关闭 Strict Mode」的选项**。
- ⭐⭐⭐ **CVE-2026-127057（CVSS 9.9）**：Danfoss AK-SC 355 与 AK-SM 800 全系**默认凭据写在产品手册里**、「所有版本受影响」、**官方无修复、建议替换设备** → 攻击者无需任何漏洞，下载手册即可登录。
- ⭐⭐⭐ **官方一致结论是「先撤出公网」而不是「先打补丁」**：CCB 明确「更新、改密码、Strict Mode 都不够，撤出互联网暴露面优先」；CERT-FR 明确「仅恢复出厂设置不够」；**Censys 实测法国 StoreView 面板 1,825 → 537 台（−71%），且版本分布未变 → 运营者是在撤网而不是打补丁**。
- ⭐⭐⭐ **库内首条「联网 OT 面板实测下线率」与「EOL 时间线」**：法国 −71% / 境外 −17%（1,166 → 966），收敛速度高度不均；**波兰 81%、罗马尼亚 80% 的暴露主机版本低于 4.3.1**；**AK-SC 355 于 2016 年停产、AK-SM 800 于 2021 年 EOL**。
- ⭐⭐ **受害面是产品类别而非品牌**：**Copeland xweb、Dixell xweb 同样被批量攻陷**，BSI 另报 Copeland XWEB EVO 两处漏洞存在利用尝试。
- ⚠️ **必须钉死的证据边界**：**设备在野被攻陷 ≠ CVE-2026-129713 被在野利用**（CISA 五部门明文：公开信息不能确认共用攻击方法、也不能确认对该 CVE 的利用）；**该 CVE 无公开利用证据、未入 KEV、无 EPSS**；**CVE-2026-129713 是否属研究者报告的六个未修漏洞之一，Danfoss 未说明**。

---

## 五、主要观点

**原文主张**

- **CISA**：AK-SM 8xxA ≤5.4.0 的一个免认证 CGI 处理器存在栈溢出，远程攻击者发送构造过的 HTTP/S POST 请求可造成内存破坏、webserver 重启，并在假想情形下以 webserver 权限执行任意代码，**无需认证**；产品状态为 known_affected；将在 5.5.x 版本修复，并取消用户关闭 Strict Mode 的选项；**推荐实践是把所有控制设备的网络暴露降到最低、置于防火墙之后、远程访问走 VPN**，并提醒 VPN 本身也可能有漏洞须保持更新；**截至发布日尚无针对这些漏洞的公开利用报告**。
- **Danfoss**：受影响版本为 AK-SM 8xxA 5.4.0 及更早；5.5.x 将修复并将移除关闭 Strict Mode 的选项；缓解措施是避免公网暴露、只经安全 VPN 访问、启用 Strict Mode、使用强口令。
- **Cyfar（第三方）**：CVE-2026-129713 可通过构造的 HTTP/S POST 令 5.4.0 及更早的控制器崩溃；ATT&CK 映射为 T1190（利用面向公网应用）→ T1499（端点拒绝服务）；立即行动为**把控制器撤出互联网、阻断指向其 Web 界面的入站 HTTP/S、应用 5.5.x、并对异常的 webserver 重启告警**。
- **CERT-FR / NCSC 瑞士 / 法国外交部 / CCB / Censys（战役级官方与测量来源，经 CTI Pilot 汇编）**：法国国家级 CERT 记录了 Danfoss AK-SM 与 AK-SC **以及 Copeland xweb 与 Dixell xweb** 远程制冷安装控制器的大量失陷，**攻击很可能仍在进行**；NCSC 瑞士将该活动评级为**在野利用（Actively Exploited）**，并指出 **AK-SM 800 已 EOL 不再修补、AK-SC 355 已停产不再修补、无修复方案、Danfoss 建议替换**，同时提醒攻击可能波及其它行业（如医疗专用制冷设备）；法国外交部将 10 月战役归因于伊朗 IRGC 的 Shahid Kaveh 部队；比利时 CCB 指出研究还发现了会话控制缺陷、**故 Strict Mode 不能消除风险**，更新与改密码均不足，**撤出互联网暴露面是第一优先**；Censys 实测法国暴露面板 1,825 → 537（−71%），判读为**运营者在把控制器撤下公网而非打补丁**，境外 1,166 → 966，且十二个高暴露国家中有十个超过 60% 的主机版本低于 4.3.1（波兰 81%、罗马尼亚 80%）。
- **CTI Watch（第三方评分分析）**：CVE-2026-127057 为 9.9 Critical，Danfoss 遗留 AK-SC 355 与 AK-SM 800 出厂即带**写在产品手册中的默认凭据**，任何查到或知道这些口令的人都能未授权登录，**所有版本受影响**，**无公开利用、未入 KEV、无 EPSS 分数**。

**我方判断**

- ⭐⭐⭐ **这条情报的真正价值是它第一次把「OT 风险」从信息层推进到了物理过程层 —— 而这个推进直接命中我方产品的核心命题。** 库内从 11-16 到 11-25 记录的 OT 风险，后果全部停留在「信息泄露 / 拒绝服务 / 权限提升 / 凭据被取走」。**本条是库内第一条「攻击者直接改写了设备的物理设定值」的证据：把冷柜持续化霜到 50℃。** ⭐⭐⭐ **对我方意义**：我方做的是 DER 接入、监控与聚合平台 —— **"可调"是我方产品能力的核心词，而本条证明了"可调"能力一旦被逆向使用，就是物理破坏**。⭐⭐ **这给"可调"这个能力项加了一条必须随附的约束：可调能力必须附带「谁在调、调了什么、能不能被追溯到人」** —— 这与我方 7 号文第三十五条（*"并网的分布式光伏发电仅应当按照调管关系接受相应平台的远程调控，**禁止擅自设置或者预留任何外部控制接口**"*）的要求**方向完全一致，但技术场景不同**。⭐⭐ **库内 11-25 已把 7 号文第三十五条标为"对产品行为约束最直接的国家级条款"，本条则从攻击侧印证了那条为什么重要** —— **这不是重复，而是把"禁止预留外部控制接口"从一句合规条款变成了一条有真实后果的技术论证**。→ **建议在本篇第 6 段直接回指该条款，形成"要求—实证"闭环。**
- ⭐⭐⭐ **「撤网优先于打补丁」这个结论，是库内 11-19 与 11-24 反复出现的担忧第一次拿到国家级 CERT 与独立测量的双重印证，而且结论对我方特别不利 —— 因为我方恰好是靠"把设备连上来"吃饭的。** 库内 11-16 已记「联网辅助设备是被点名的攻击面」，11-19 已记「CISA 官方口径是 *unpatched **or internet-accessible***」，11-24 已记「联网可达性优先于 KEV 收录状态」。⭐⭐⭐ **本条给出的是这些原则的最强版本：Censys 实测显示攻击后的收敛方式是"把控制器撤下公网"，而不是"升级固件"；法国 −71% vs 境外 −17% 的差异说明**收敛速度取决于客户的安全成熟度，而不是补丁可得性**。⭐⭐⭐ **对我方的直接含义必须写清楚**：**我方的业务模式（把逆变器、监控、聚合平台连到云上）与这类被攻击设备所处的位置是同一侧** → **我方不能把"我把设备连上来了，所以我的产品有暴露面"当作免责，而应把本条的结论反过来用作我方对客户的安全承诺**：**我方应当明确告诉客户「先解决联网暴露，再谈功能」，并把这写进交付前置条件**。⭐⭐ **这与我方 DER 接入产品的"可控可调"卖点构成张力，需要产品侧显式回答"如何在联网前提下提供等价的可控性"** —— 但库内无产品材料，**不得替我方产品下结论**，只能作为待决问题。
- ⭐⭐⭐ **「生命周期」必须成为暴露面台账的一等字段 —— 这条有硬证据，且它正好把库内 11-24 的一条待办从"缺一列"变成"有范例可抄"。** 库内 11-24 已记「EOL 设备台账完全缺失」这条待办。⭐⭐⭐ **本条提供了三个具体锚点**：**AK-SC 355 于 2016 年停产、AK-SM 800 于 2021 年 EOL、两者到 2026 年仍在全国零售门店的冷柜里运行**；**NCSC 瑞士的建议不是修补而是替换**；**CVE-2026-127057 的默认凭据"写在产品手册里"** → **这三者叠加的含义是：一个 2016 年停产、2021 年 EOL、手册公开默认口令、仍挂在公网上的设备，其攻击成本接近于零**。⭐⭐ **可执行的台账字段因此是两条，不是一条**：「**厂商支持状态（在产/EOL/停产）+ 生命周期终止日期**」与「**默认凭据是否公开可查（对手册公开的产品答案为"是"）**」。⭐⭐ **后者这一条是库内至今没有任何文档提出过的 —— 它把"弱口令"从一种主观评级变成一个可以客观查证的事实**。
- ⭐⭐⭐ **「经由供应商打到法国血液服务」这一条，是本篇对我方最贵的一句，它把库内 11-25 刚记的「供应商/MSP 代运维实例是影子密钥存活地」从密钥面扩展到了物理面。** ⭐⭐⭐ **今天已经记下的 [Azure APIM 事件](azureApimNorwayEnergyBreach-2026-11.md) 指出攻击者搜的是"托管平台上的密钥"，且"影子实例是未轮换密钥存活的地方"；本条指出的是同一条供应链路径的另一端 —— **攻击者用供应商的合法远程访问通道改了实际物理设备的工作参数**。⭐⭐⭐ **两条合起来得出一个对我方极其具体的要求：我方作为给电站做托管运维与聚合的平台方，必须能把「我方人员/我方供应商账号实际能操作到哪些设备、哪些参数」列成一张可核查的表** —— **这是"第三方远程访问 OT"这条库内已记议题，第一次有了带物理后果的实证**，也正是库内 11-16 已记的 CISA/FBI 联合警告（*"第三方供应商对 OT 环境的长期远程访问正在被利用"*）的现实注脚。⭐⭐ **可执行动作：把"运维账号 → 可达设备 → 可写参数"做成一张映射表，作为我方托管服务的准入清单。**
- ⭐⭐⭐ **「把设备撤下公网」这条结论，同时暴露了一个我方必须诚实面对的张力：它与我方的产品叙事是对立的，而这次法国战役证明对立方是对的。** ⭐⭐ **法国战役的结果是「撤网 71%」，而那些撤网的公司失去的是远程运维能力** —— **也就是说，攻击者用一次物理破坏，换来了整个行业对"联网即风险"的集体认知升级**。⭐⭐ **对我方而言，这意味着未来客户的默认安全姿态会比现在更保守** → **我方的产品叙事必须能回答"不联网怎么实现可调与可测"**（比如只经专线/VPN、只开放必要端口、只允许受控指令集）。⭐⭐ **但必须写清边界：库内无我方产品设计材料，不得替我方判断现有架构是否满足这一要求 —— 这是一个必须向产品侧提出的问题，不是一个可以由情报自行回答的结论。** ⚠️ **同样不得反向写成"我方产品不安全"或"我方应当停止联网接入"** —— 那是无依据的推断。
- ⭐⭐ **「恢复出厂设置不够」这一条，是库内配置类缓解失效担忧的第二个实证，价值高于第一个。** 库内 11-24 已记 phpAfterShell「PHP2Shell 补丁不修它」；11-19 已记 Siemens「唯一缓解是手工配置 SQL 通信加密」，而本条指出**连厂商自家的 Strict Mode 开关都不够、且厂商正在取消这个开关**。⭐⭐⭐ **三者串起来是一条方法论结论：配置类缓解的可信度必须按「是否可被用户关闭 + 是否会随重装/换人/换机而丢失 + 官方是否承认其长期有效」三条打分，任何一条不满足就不能当作唯一防线**。⭐⭐ **这条恰好可以直接落到库内 11-19 已记的「唯一缓解是手工配置 SQL 通信加密」那条上 —— 按本条的三条打分，那条配置的"官方长期有效性"这一项是成立的（厂商明说无修复、必须靠配置），但"是否会被悄悄改掉"这一项无保障 → 因此它必须配一条拓扑级约束，而不是单独成立**。⭐⭐ **这是一个可直接进等保方向基线的判据，且不依赖任何我方使用该产品的证据。**
- ⭐⭐ **Copeland / Dixell 同样受害这条，提示暴露面自查必须按"功能类别"而不是"品牌清单"做。** ⭐⭐ **商用制冷控制器这一类别里，至少三个独立厂商的产品同时在野被攻陷** → **对我方的意义：如果我方（或我方客户）在某个 OT 场景里有"带 Web 界面的现场控制器"，就必须按类别而非按品牌去查暴露面** —— **因为"我们没买 Danfoss"完全不代表安全**。⭐⭐ **这条与库内 11-19 已记的「光合动力/EPICS 协议栈长期无认证」是同一判据的不同实例：漏洞在实现里，也可能在协议默认里。**
- ⚠️ **必须保持的边界**：① **不得下"我方受影响"结论**（库内无我方使用证据）；② **不得写成"CVE-2026-129713 已在野被利用"**（CISA 五部门明文说公开信息不能确认）；③ **不得把法国归因扩展到 10 月战役之外，也不得写成"伊朗攻击了欧洲电网"**；④ **不得把「强制化霜」写成"门店食品全部变质"**（来源只说冷库设定被改为 50℃ 持续化霜，未给损失数据）；⑤ **不得把 Censys 的 2026-10 数据当作当前状态**；⑥ **不得把 IP 白名单写成正式缓解方案**（CERT-FR 明确其只是应急手段）；⑦ **不得把"设备失陷"扩大为"丹佛斯全线产品失陷"**；⑧ **评分必须写明口径**（v3.1 9.8 / v4.0 9.3）。
- ⭐ **优先级判断**：本条**不应**进"立即修补"队列（我方不使用该产品）；**但应**进"暴露面方法论"队列 —— 它提供的是**台账字段、处置优先级与一条国家级归因**，这些都不依赖我方是否使用该产品。

---

## 六、参考意义

| 方向（网络安全/信创/等保/隐私保护/护网） | 可证事实 | 本阶段处理 |
|---|---|---|
| **网络安全（方向级）** | ① **免认证 CGI 栈溢出 + 无补丁（known_affected）**，修复版 5.5.x 未发布；② **默认凭据公开于手册、全版本受影响、无修复、建议替换设备**；③ **CCB：更新/改密码/Strict Mode 均不足，撤出公网优先**；④ **CERT-FR：仅恢复出厂设置不够，源地址过滤仅是应急手段**；⑤ **NCSC 瑞士：AK-SM 800（2021 EOL）、AK-SC 355（2016 停产）无修复、建议替换**；⑥ **Censys 实测：法国暴露面板 1,825→537（−71%）、版本分布未变 → 撤网而非打补丁**；⑦ **丹麦总部 / 商业设施行业 / 全球部署**；⑧ **法国归因 IRGC Shahid Kaveh（仅 10 月战役）**；⑨ **攻击经由供应商篡改法国血液服务三处站点冷库设定** | 🟡 **进评审（方向级）** —— 落四条方向级动作：**① "暴露面台账新增两列：厂商支持状态 + 生命周期终止日期"**（以 2016 停产 / 2021 EOL 为范例），**并新增"默认凭据是否公开于手册"这一可客观查证项**；**② "处置优先级判据固化：撤出公网 > 换密码 > 恢复出厂 > 打补丁"**（按 CCB / CERT-FR 原文次序，且明确源地址过滤仅为应急）；**③ "配置类缓解三问打分表"**（是否可被用户关闭 / 是否随重装换人丢失 / 官方是否承认长期有效），**任何一条不满足即不得作为唯一防线**；**④ "按功能类别而非品牌做暴露面自查"**（制冷控制器同类至少三厂商同时在野失陷）。**不产专项整改**（第 1 关：我方无使用证据，属待核实） |
| **护网（方向级）** | ① **攻击已产生物理后果**（持续化霜 50℃），**非仅信息层后果**；② **攻击经由供应商/第三方远程维护路径打到医疗冷链**；③ **无补丁 + EOL + 默认口令 = 零成本攻击面**；④ **NCSC 瑞士提示攻击可能波及其它行业（如医疗专用制冷设备）** | 🟡 **进评审（方向级）** —— 建议并入既有「攻击手法→防线覆盖度对照」（`remediation-defenseTacticCoverage-20261112`）：**新增攻击手法「物理过程操纵」与「供应链远程维护路径」两类**，并增设一条演练自查项：**「本方（含供应商）运维账号实际可写哪些设备参数」的可核查映射表**。⭐⭐ **这是库内第一次出现"攻击后果进入物理层"，护网演练的对抗目标需要相应上移** —— 但库内无我方演练方案材料，**只落方向级，不预设场景细节** |
| **等保（方向级）** | 官方处置序列（识别 → 确认平台状态 → 处置 → 上报）具备可作为测评证据链的形态；EOL 设备的"无修复"状态需在台账中显性登记 | 🟡 **登记跟踪** —— 与库内 11-19 已记「第三方参与远程运维」、11-25 已记「凭据托管位置」同属"供应链与托管服务责任边界"议题簇；**等保测评项映射需合规与产品材料，库内不具备，暂不转产物** |
| **隐私保护** | 法国血液服务站点冷链设定被篡改 → 属医疗冷链场景的运营安全后果，但**公开信息未涉及个人信息处理** | ❌ **本阶段不转评审** —— 无我方个人信息处理场景的一手材料，**登记跟踪**；若后续出现"我方客户侧涉及个人信息且由第三方远程运维"的实证再评 |
| **信创** | — | ❌ **不适用** —— 本条无信创相关可证事实，不做形式化挂钩 |

---

## 七、总结输出

**一句话结论**：**CISA 11-24 的 ICSA-26-328-03 只是这条情报的表层 —— 真正的分量在于它背后的案卷：Danfoss AK-SM/AK-SC 商用制冷控制器已在法国（Coopérative U / Intermarché / E. Leclerc 门店，10 月 11-12 日）、至少六个其他欧洲国家 115 家以上门店与瑞士被在野批量攻陷（NCSC 瑞士标记 Actively Exploited），法国外交部 11-09 将该次战役（且仅该次）归因于伊朗 IRGC「Shahid Kaveh」部队，而攻击者的动作是把门店冷柜强制持续化霜到 50℃（正常为 24 小时内 2 小时）—— 这是库内第一条「攻击直接操纵物理过程」的证据，也是第一条「经由供应商篡改法国血液服务三处站点冷库设定」的证据；由此得到四条硬结论：① 攻击面按"联网可达"而非"是否已打补丁"判定，Censys 实测法国暴露面板 1,825 → 537（−71%）且版本分布未变，证明运营者是在撤网而不是升级，法国 −71% 对境外 −17% 说明收敛速度取决于客户安全成熟度；② 比利时 CCB 与法国 CERT-FR 独立给出同一处置次序 —— 撤出公网优先，且明确「更新、改密码、Strict Mode 都不够」「仅恢复出厂设置不够」「IP 白名单只是应急」，因此配置类缓解必须按「是否可被用户关闭 / 是否随重装换人丢失 / 官方是否承认长期有效」三问打分，任何一条不满足即不得作唯一防线；③ 生命周期必须成为暴露面台账的一等字段（AK-SC 355 于 2016 年停产、AK-SM 800 于 2021 年 EOL、无修复、建议替换；CVE-2026-127057 更把默认凭据「写在产品手册里」，全版本受影响、CVSS 9.9、零利用成本）；④ 暴露面自查必须按功能类别而非品牌做，因为同批被攻陷的还有 Copeland xweb 与 Dixell xweb，BSI 另报 Copeland XWEB EVO 存在利用尝试。对我方的直接含义有两条且必须同时写下：这条印证了库内 7 号文第三十五条（禁止擅自设置或预留外部控制接口）为什么重要 —— 「可调」能力一旦被逆向使用即等于物理破坏，因此可调必须附带"谁在调、调了什么、能否追溯"；而这条同时暴露了我方业务模式（把 DER 与监控连上云）与这条结论处在对立面 —— 我方不能以"我把设备连上来了"作免责，必须把"先解决联网暴露、再谈功能"写成交付前置条件，并回答"不联网如何提供等价的可控性"。⚠️ 五条边界必须钉死：设备在野失陷 ≠ CVE-2026-129713 已被在野利用（CISA 五部门明文确认公开信息不能证明）；该 CVE 无公开利用、未入 KEV、无 EPSS、当前无补丁；法国归因仅限 10 月战役、不得外推；Censys 数据为 2026-10、不可当作当前状态；我方无使用证据 → 不得下"我方受影响"结论。**

**落地去向**
- [ ] 产品特性
- [ ] 需求变更
- [ ] 专项整改

---

## 最新动态

> **last_seen：2026-11-26 07:11**（采集源：CISA KEV 目录 catalog 版本 **2026.11.25** + Danfoss 官方安全通告总表（最后更新 2026-11-20）+ Threadlinqs TL-2026-6887 + Undercode News + Lancartech；快照见本节末）

### ⚠️ 本篇上一版结论必须按「CVE 级」而非「产品线级」修正（2026-11-26）

上一版（第 5 段与第 7 段）写的是：

> 「⚠️ **该 CVE 无公开利用、未入 KEV、无 EPSS**」
> 「⚠️ **设备在野失陷 ≠ 该 CVE 被在野利用（CISA 五部门明文：公开信息不能确认共用攻击方法、也不能确认对该 CVE 的利用）**」

**这两句本身仍然完全成立 —— 它们说的是 CVE-2026-129713 这一个编号。CVE-2026-129713 至今仍未入 KEV、仍无 EPSS、官方仍未确认对该编号的在野利用。**

**但必须立刻修正的是它的隐含推论。** 2026-11-25，CISA 把 **同一产品线（Danfoss AK-SM 800A）的另外三条 CVE 一并收录进 KEV**：

| CVE | 形态 | 厂商通告 | 受影响版本 | KEV 期限 | 取证分诊 |
|---|---|---|---|---|---|
| **CVE-2025-41450** | 不当身份认证 → 生成 web 报表泄露**内部 IP、用户名、门店名** | DSA-2025-03-01 | AK-SM 8xxA **< 4.2** | **2026-12-09** | **No**（不要求） |
| **CVE-2023-25914** | 路径穿越（XML 接口）→ 读取底层服务器系统文件 | DSA-2023-08-01 | AK-SM 800A 全系 **< 3.3** | **2026-11-28** | **必需** |
| **CVE-2023-25915** | 输入校验不当 → 远程任意命令执行 | DSA-2023-08-01 | AK-SM 800A 全系 **< 3.3** | **2026-11-28** | **必需** |

**⚠️ 结论口径（不得再错）**：
- ✅ **正确表述**：「**该产品线已被 CISA 官方认定存在在野利用（11-25 收录三条 KEV），但被认定的是 CVE-2025-41450 / CVE-2023-25914 / CVE-2023-25915 三个较早的编号；本篇主线的 CVE-2026-129713 仍未入 KEV**」。
- ❌ **错误表述一**：「Danfoss 已进 KEV」—— 误导，会让人以为 CVE-2026-129713 被收录。
- ❌ **错误表述二**：「AK-SM 800A 未被官方认定利用」—— **已被推翻**，本条作废。
- ⚠️ **动作**：我方资产台账里凡是把「未入 KEV」当**产品级标签**的字段，**必须改成按 CVE 记**。这是本期第 1 关能否过的关键。

### ⭐⭐⭐ 库内首张「OT 设备版本基线矩阵」（把四条 CVE 的官方受影响版本叠在一张表上）

| 版本区间 | 受影响 CVE | 官方修复版本 | 出处 |
|---|---|---|---|
| **< 3.3** | CVE-2023-25914、CVE-2023-25915（**已入 KEV**）、CVE-2023-25913 | 升级至 ≥ 3.3 | Danfoss DSA-2023-08-01 |
| **3.3 ~ 4.1** | CVE-2025-41450（**已入 KEV**） | 升级至 ≥ 4.2 | Danfoss DSA-2025-03-01 |
| **< 4.3.1**（含 3.3~4.2） | CVE-2025-41451、CVE-2025-41452（后认证 OS 命令注入 + Nginx 配置注入，**未入 KEV**） | 升级至 ≥ 4.3.1 | Danfoss DSA-2025-08-01 |
| **≤ 5.4.0**（含 3.3~5.4.0） | **CVE-2026-129713**（本篇主线，免认证 CGI 栈溢出，**未入 KEV、当前无补丁**） | **5.5.x —— 尚未发布** | CISA ICSA-26-328-03 / Danfoss DSA-2026-12-01 |
| **全版本（含 ≥5.5.x）** | **CVE-2026-127057**（默认凭据写在手册里，CVSS 9.9，官方无修复、建议替换设备） | 无（建议替换） | 本篇 11-25 已记 |

**⭐⭐⭐ 这张表把本篇 11-25 的四条硬结论全部接上了**：
1. **同一条产品线横跨四个版本代际，每一���「升级能闭掉什么」都不一样** → 我方资产台账**记一个版本号是不够的**，必须是「版本 → 属于哪个修复代际 → 可闭 CVE 集合」。
2. **这正好填上库内 11-24 已记的那条「EOL 设备台账完全缺失」待办** —— EOL 台账的核心字段本来就该是「版本 → 修复代际 → 可闭 CVE 集合」。
3. ⚠️ **对 5.4.0 及以下版本的设备，即使升到 4.3.1 也闭不掉 CVE-2026-129713** → **不得把「已升到 4.3.1」写成「已修复」**。唯一能同时闭掉全部四条的版本是**尚未发布的 5.5.x**。
4. ⚠️ **CVE-2026-127057 是全版本默认凭据、官方无修复** → **即使升到 5.5.x 也不等于安全**；库内 11-25 已记的官方处置次序「**撤出公网优先**」因此仍然是第一动作。

### ⭐⭐ 本批次给出的两条官方处置判据（新增）

1. **KEV 条目按「取证分诊（Forensic triage）」字段逐条分级**：CVE-2025-41450 = **No**（不要求取证分诊）；CVE-2023-25914 / 25915 = **必需**。→ **库内 11-25 刚立的「处置动作三分支：修补 / 移除 / 取证分诊」在本批次被官方字段证实可以逐条分级执行**，不再是分析框架。
2. **同一产品线三条 KEV 的期限不同（11-28 / 11-28 / 12-09）** → **整改期限必须按 CVE 取，不得按产品取最短**（取最短会漏掉 CVE-2025-41450 的取证要求与 12-09 期限）。反向也成立：Lancartech 的实务建议是「**三条当作一个整改包处理，而不是三张不同排期的单**」—— **打包是运维效率决策，不是攻击链判断**（该源同时明说「没有证据表明三条被串在同一条攻击链里」）。

### ⭐ 本批次唯一可核的新技术事实

- **CVE-2023-25914 的 CVSS 在第三方之间冲突**：Threadlinqs 给 **Critical CVSS 3.1 10.0**（向量 `AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`），itdef 给 **8.8 / EPSS 1%**，而 **CISA KEV 目录本身不给 CVSS**。**正确表述**：「第三方口径 8.8~10.0，KEV 目录未给分」→ **不取均值、不换算**。
- **本批次 10 条勒索软件关联全部为 Unknown** → 不得写「勒索软件攻击」。

### 快照（本轮新增）

| 快照 | SHA256 | 抓取时间 | 正文字符 | HTTP |
|---|---|---|---|---|
| `raw/snapshots/security/cisa-kev-20261125-batch.md` | `9077dc976c7c10ce11ce11ea1987e05a00cd029c84f5d9328398e66a13c305be` | 2026-11-26 07:10:55 | 13,686 | 200 |
| `raw/snapshots/security/kev-20261125-threadlinqs-analysis.md` | `b546bfcfa81563615a1de0740c3e47bdf4c5e244d41dbfb2c99b5e16dd396295` | 2026-11-26 07:10:57 | 21,677 | 200 |
| `raw/snapshots/security/danfoss-security-advisories-20261126.md` | `f4414f2db2ace342aaf27448f5500074d630a094e670ed75f7c2e9f7fbcf8afa` | 2026-11-26 07:11:07 | 4,517 | 200 |

---

## 参考链接

- [CISA ICSA-26-328-03：Danfoss AK-SM 8xxA Series（2026-11-24）](https://www.cisa.gov/news-events/ics-advisories/icsa-26-328-03)
- [库内新增：CISA KEV 2026-11-25 批次十条（Danfoss 三条进 KEV 的完整批次分析）](cisaKev20261125Batch-2026-11.md)
- [Danfoss DSA-2026-12-01：Stack-based buffer overflow in Danfoss AK-SM 8xxA unauthenticated CGI handler（2026-11-20）](https://www.danfoss.com/en/service-and-support/coordinated-vulnerability-disclosure/danfoss-security-advisories/dsa-2026-12-01/)
- [Cyfar：Danfoss AK-SM 8xxA Series（CVE-2026-129713）检测与 ATT&CK 映射（2026-11-24）](https://cyfar.ca/posts/danfoss-ak-sm-8xxa-series-cve-2026-129713)
- [CTI Pilot：CTI Daily Brief · 2026-10-13（法国战役 · IRGC 归因 · CERT-FR / NCSC 瑞士 / Censys 逐条汇编）](https://ctipilot.ch/daily/2026-10-13)
- [Red Tiger Security：Security Advisories & OT Threat News（2026-11-24 条目与 CERT@VDE 摘要）](https://www.redtigersecurity.com/advisories)
- [CTIWatch：CVE-2026-127057（Danfoss 默认凭据 · CVSS 9.9 · 全版本受影响）](https://ctiwatch.com/vulnerabilities/CVE-2026-127057)
- [库内相关：CISA 等五部门联合警告「联网辅助设备是被点名的攻击面」（2026-11-05 · 本篇为其案卷升级）](cisaRefrigerationColdChain-2026-11.md)
- [库内相关：CISA ICSA-26-321-08 Siemens SIMATIC NTLM 中继（唯一缓解是手工配置 SQL 通信加密）](icsa26321SiemensSimaticNtlmRelay-2026-11.md)
- [库内相关：Azure APIM 挪威能源行业被窃密钥事件（托管平台凭据外泄 · 影子实例）](azureApimNorwayEnergyBreach-2026-11.md)
- [库内相关：《分布式光伏发电开发建设管理办法》7 号文（第三十五条 · 禁止擅自设置或预留外部控制接口）](../policy/distributedPvManagementMeasure7hao-2026.md)

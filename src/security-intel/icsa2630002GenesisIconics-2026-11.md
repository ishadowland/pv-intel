# CISA ICSA-26-300-02：三菱电机 / ICONICS SCADA 与历史数据库平台四个漏洞

> ⚪ 备案 · 采集于 2026-11-13 · 核心标识：CVSS v3.1 9.1 / v4.0 9.3 · 弱口令恢复机制挑战响应全用户通用 · libwebp CVE-2023-4863 位于当前版本内 · 三个产品无补丁

---

## 一、信源核实

| 项 | 值 |
|---|---|
| 来源请求 | `CISA advisory Mitsubishi Electric ICONICS GENESIS64 CVE ICSA-26-300`（web_search）<br>`CISA ICS advisory November 2026 critical vulnerability energy solar inverter SCADA`（web_search） |
| 原始 URL（主 · 官方） | https://www.cisa.gov/news-events/ics-advisories/icsa-26-300-02 （CISA ICS Advisory，最后修订 2026-10-29） |
| 原始 URL（辅 1） | https://otsecuritywire.com/articles/mitsubishi-iconics-genesis64-icsa-26-300-02-challenge-response-dcom-libwebp-2026 （OT/ICS Monitor 第三方分析，2026-11-03） |
| 原始 URL（辅 2） | https://cn-sec.com/archives/5545773.html （CN-SEC 中文工业网络安全周报 2026 年第 41 期） |
| 发布主体 | CISA（美国网络安全和基础设施安全局）；三菱电机 / Mitsubishi Electric Iconics Digital Solutions（厂商）；OT/ICS Monitor、CN-SEC（第三方分析） |
| 发布/更新时间 | 厂商 **2026-10-15** 首发（Mitsubishi Electric 2026-006）；CISA **2026-10-27** 转发；**2026-10-29** 修订（Revision 3）；第三方分析 2026-10-28 / 11-03 |
| 采集时间 | 2026-11-13 07:11–07:14 |
| 快照 | `raw/snapshots/security/icsa-26-300-02-genesis64.md` · `icsa-26-300-02-otsecuritywire.md` · `icsa-26-300-02-cnsec.md` |

> ✅ **安全域硬性要求已满足**：官方通告（CISA）+ 第三方分析（OT/ICS Monitor、CN-SEC）**三个独立来源**，非单一信源。

---

## 二、事实核查

| 数据点 | 原文表述 | 核查方式 | 结论 | 备注 |
|---|---|---|---|---|
| Alert Code / 修订 | **ICSA-26-300-02**，Last Revised **2026-10-29** | CISA 官方快照原文 | ✅ 已核 | |
| 受影响产品（10 项） | GENESIS、GENESIS64、ICONICS Suite、HyperHistorian、AnalytiX、MobileHMI、IoTWorX、**MC Works64、GENESIS32、BizViz**（三菱电机 + Mitsubishi Electric Iconics Digital Solutions 两个主体） | CISA 官方快照 | ✅ 已核 | 覆盖 SCADA / HMI / 历史数据库 / IoT 网关 / 移动运维全谱 |
| 漏洞总数 | 4 个 CVE：CVE-2023-4863（libwebp）、CVE-2026-16436、CVE-2026-16437、CVE-2026-16438 | CISA + 两家第三方 | ✅ 三源一致 | ⚠️ **CISA 页面 "3 Vulnerabilities" 计数与实际 4 个 CVE 编号不一致** —— 见下方冲突行 |
| 官方汇总评分 | **CVSS v3 9.1**（Critical），行业 Critical Manufacturing，全球部署 | CISA 官方快照 | ✅ 已核 | |
| **CVE-2023-4863 双口径评分** | CISA 官方快照：该 CVE 在 GENESIS64 / ICONICS Suite 场景下 **v3.1 = 8.2（HIGH）**，**v4.0 = 9.3（CRITICAL）**；向量 `CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H` | 官方快照逐字核对 | ✅ **双口径均已核** | ✅ 安全域要求核 v3.1 与 v4.0 两套口径，两套均已从官方原文取得 |
| **评分冲突** | notcve 聚合页列 CVE-2023-4863 为 **9.9**（并标 KEV、EPSS 100%）；CISA 官方为 8.2 / 9.3 | 官方 vs 第三方聚合对比 | ⚠️ **两个数打架** | 9.9 是 **libwebp 上游 Chromium CVE 的通用评分**，8.2/9.3 是 **CISA 按受影响产品场景重新打的分**（本地攻击 + 高权限 + 范围变更）。**两者不是同一口径，不是错误**。本库对外引用一律用 CISA 官方口径 |
| **CVE-2023-4863 影响当前版本** | 官方受影响版本：GENESIS64 / ICONICS Suite **>=10.97 且 <=10.97.2**；第三方（indctrlhub）指出"该通告把 CVE-2023-4863 放在 **GENESIS64 与 ICONICS Suite 10.97 至 10.97.2 —— 当前发布版本**内" | 官方版本区间 + 第三方交叉 | ✅ **一致** | ✅ 这是一个 **2023 年披露的 CVE-2023-4863 出现在 2026 年的当前发布版中**，说明**第三方组件版本未随主产品同步升级** |
| **CVE-2026-16436（弱口令恢复）** | "Weak Password Recovery Mechanism for Forgotten Password (CWE-640)……**The challenge response used to unlock the system is common to all users and fixed.**" → 攻击者可远程获取挑战响应后**无需账户即解锁系统** | CISA 官方快照原文 | ✅ 已核 | ⚠️ **这是本通告里最值得我方自查的一条** —— 认证设计缺陷，与产品版本无关 |
| CVE-2026-16437 / 16438 | CWE 分类为 Incorrect Privilege Assignment；官方归类为"bypass authentication"与"perform arbitrary operations" | CISA 官方 + OT/ICS Monitor | ✅ 一致 | 第三方补充：安装程序默认授予管理员账户 DCOM 权限 |
| 漏洞后果 | "execute arbitrary code (CVE-2023-4863), bypass authentication (CVE-2026-16436 and CVE-2026-16437), or perform arbitrary operations (CVE-2026-16438)" | CISA 官方快照 | ✅ 已核 | |
| **无补丁产品** | MC Works64、GENESIS32、BizViz 的受影响版本列示为 `vers:all/*`（全版本）；厂商建议迁移至 GENESIS64 或 GENESIS | CISA 官方版本列 + geopolitiki/indctrlhub/trout 三方一致 | ✅ **已核** | ⚠️ 厂商**不提供补丁**，只提供替换方案 |
| 修复版本 | CVE-2023-4863 → GENESIS64 / ICONICS Suite **10.97.3**；CVE-2026-16436/16437/16438 → GENESIS64 / ICONICS Suite / HyperHistorian / AnalytiX / MobileHMI **10.98**；GENESIS → **11.04** | CISA 官方快照 | ✅ 已核 | ⚠️ **10.97.3 只修 libwebp 一个**，三个 2026 年漏洞需 10.98（第三方 securhub 独立指出同一点） |
| 在野利用 | CISA 通告未提及在野利用；第三方亦未报告 | 检索与快照核对 | ✅ 未见报告 | 不得据此推断"安全"，只表示**未报告** |
| CISA 行业口径 | Critical Manufacturing；Countries/Areas Deployed: Worldwide；总部 Japan / United States | CISA 官方快照 | ✅ 已核 | |

> **核查小结**：四个 CVE、三源一致；**双口径评分（v3.1 8.2 / v4.0 9.3）已从官方原文逐字核到**。三个必须标注的点：① **评分"冲突"实为两套口径**（上游 CVE 通用分 vs CISA 产品场景分），本库统一用官方口径；② **CVE-2023-4863 这个 2023 年的 CVE 出现在 2026 年当前发布版内**，说明第三方组件版本管理与主产品版本脱节；③ **三个产品（MC Works64/GENESIS32/BizViz）厂商不提供补丁**，只有迁移方案 —— 这是供应商 EOL 管理的典型样本。

---

## 三、原文归档（快照）

| 快照 | SHA256 | 抓取时间 | 大小 |
|---|---|---|---|
| `raw/snapshots/security/icsa-26-300-02-genesis64.md` | `9dd979ab7f96101f9d25243b3684e66690e64f5c238661ba5b3ed8baf3430249` | 2026-11-13 07:11:23 | 60,018 字符（**已截断**，原文超长） |
| `raw/snapshots/security/icsa-26-300-02-otsecuritywire.md` | `3fe7444f03ae15a9e07598f4eb3d417adac78b8d7621474b1b8975ea9774f72b` | 2026-11-13 07:11:34 | 5,898 字符 |
| `raw/snapshots/security/icsa-26-300-02-cnsec.md` | `725fbd172295ef1745b50a51abfa21d39d3eb95f9f6eb0c465a77086d977da27` | 2026-11-13 07:14:12 | 12,841 字符 |

**关键原文摘录（CISA 官方，2026-10-27 转发 / 10-29 修订）**：

> Successful exploitation of these vulnerabilities could allow an attacker to execute arbitrary code (CVE-2023-4863), bypass authentication (CVE-2026-16436 and CVE-2026-16437), or perform arbitrary operations (CVE-2026-16438), resulting in information disclosure, tampering with, destruction, or deletion of information, and a denial-of-service (DoS) condition of the system.
> Weak Password Recovery Mechanism for Forgotten Password (CWE-640) vulnerability in GENESIS, GENESIS64, ICONICS Suite, Hyper Historian, AnalytiX, MobileHMI, IoTWorX, MC Works64, GENESIS32, and BizViz could allow a **remote attacker to unlock the system by obtaining the challenge response by some means. The challenge response used to unlock the system is common to all users and fixed.**
> Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions GENESIS64 >=10.97|<=10.97.2 (CVE-2023-4863)
> Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions GENESIS64 <=10.97.3 (CVE-2026-16436, CVE-2026-16437, CVE-2026-16438)
> Mitsubishi Electric MC Works64 vers:all/* (CVE-2026-16436, CVE-2026-16437, CVE-2026-16438)
> Mitsubishi Electric is releasing fixed version 10.98 or later for GENESIS64, ICONICS Suite, Hyper Historian, AnalytiX, and MobileHMI.
> CVSS Version / Base Score / Base Severity / Vector String —— 3.1 / **8.2** / HIGH / CVSS:3.1/AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H —— 4.0 / **9.3** / CRITICAL / CVSS:4.0/AV:L/AC:L/AT:N/PR:H/UI:N/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H

**关键原文摘录（CN-SEC 中文周报，第 41 期）**：

> 2026年10月27日，CISA发布公告ICSA-26-300-02，通报三菱电机及其子公司 Mitsubishi Electric Iconics Digital Solutions 的 GENESIS、GENESIS64、ICONICS Suite、Hyper Historian、AnalytiX、MobileHMI、IoTWorX、MC Works64、GENESIS32 与 BizViz 等多款工业软件存在多个漏洞，综合 CVSS v3.1 最高评分达 9.1（严重级别）。问题涵盖由内部组件 libwebp 引发的非预期越界写入（CWE-787）、弱口令恢复机制（CWE-640）与权限分配不当（CWE-266）三类缺陷……
> 三菱电机已发布 GENESIS64 与 ICONICS Suite 的 10.97.3 及以上修复版本，并建议客户考虑以 GENESIS64 或 GENESIS 替代仍在使用中的 MC Works64，同时在过渡期内落实网络隔离、访问控制与最小权限等缓解措施。
> 安全研究者提醒，**libwebp 类组件漏洞影响面广，企业资产台账中应纳入对第三方开源组件的版本追踪**，避免只关注自主开发或主打产品而遗漏被嵌入的底层依赖。

**关键原文摘录（OT/ICS Monitor）**：

> CISA's advisory ICSA-26-300-02 covers the ICONICS SCADA/HMI family sold by Mitsubishi Electric and Mitsubishi Electric Iconics Digital Solutions: GENESIS64, ICONICS Suite, Hyper Historian, AnalytiX, MobileHMI, IoTWorX, GENESIS (v11), MC Works64, GENESIS32 and BizViz. … Per the advisory's revision history, the vendor published on 15 October 2026 (Mitsubishi Electric 2026-006), CISA republished on 27 October, and Revision 3 on 29 October.

---

## 四、概要提取

- **CISA 汇总评分 v3.1 9.1（Critical）**，行业 Critical Manufacturing，全球部署，10 个受影响产品横跨 SCADA / HMI / 历史数据库 / IoT 网关 / 移动运维
- **CVE-2026-16436 是真正的设计缺陷**：密码找回的挑战响应对**所有用户相同且固定**，拿到即可远程解锁系统，**无需账户**
- **CVE-2023-4863（2023 年披露的 libwebp 溢出写）出现在 2026 年的当前发布版 10.97–10.97.2 内** —— 官方修到 10.97.3 即可修这一个
- **三个 2026 年漏洞需 10.98**；只升到 10.97.3 **不够**（第三方独立确认）
- **MC Works64 / GENESIS32 / BizViz 全版本受影响且厂商不提供补丁**，唯一方案是迁移至 GENESIS64 或 GENESIS
- **未报告在野利用**（注意：未报告 ≠ 安全）
- CN-SEC 给出的迁移性建议直指要害：**第三方开源组件的版本追踪必须进资产台账**

---

## 五、主要观点

**原文主张**

- CISA：成功利用可能造成代码执行、绕过认证、任意操作，进而导致信息泄露/篡改/销毁/删除与拒绝服务
- OT/ICS Monitor：产品线是 **SCADA/HMI 家族**，GENESIS64/ICONICS Suite/Hyper Historian/AnalytiX/MobileHMI 属典型 OT 应用场景；无补丁产品需网络隔离、访问控制与最小权限作为过渡期缓解
- CN-SEC：历史数据库与人机界面**往往直接连接控制网络**，一旦被攻陷可能成为横向移动进入生产系统的跳板；并建议**资产台账纳入第三方开源组件版本追踪**
- 厂商公告的修订史：厂商 10-15 首发 → CISA 10-27 转发 → 10-29 第三次修订

**我方判断**

- ✅ **暴露面判定：我方技术栈不含 GENESIS / ICONICS / MC Works64，不在我方暴露面** —— 这条纯漏洞**不满足评审第 1 关"影响可证"**，不进 `deliverables/`。这与上一期 EPICS 四 CVE 的处理一致（同类漏洞同样不在我方栈内）
- ✅ **但本通告里有两条结构性证据比我方栈内漏洞更值得记**：
  1. **"挑战响应对所有用户相同且固定"** —— 这是**认证设计缺陷，不是补丁问题**，而且与厂商无关、任何自研系统都可能犯同样的错。我方平台的密码找回、设备解锁、运维通道若采用固定/可预测挑战响应，就是同类问题。**这一条应当进我方自查清单**
  2. **2023 年的上游 CVE 出现在 2026 年的当前发布版内** —— 说明**第三方组件版本与主产品版本脱节**。这与上一期"我方监控平台 API 鉴权/越权读自查"是同一个风险家族，但更具体：**要查的是"我方镜像/依赖清单里的第三方组件版本"，而不只是自研代码的漏洞**
- ✅ **"三个产品无补丁、只给迁移方案"是供应商 EOL 管理的样本**：我方若采购电站监控/历史数据库类产品，**必须把"厂商停止补丁时怎么办"写进选型条款**，而不是等出事再谈
- ⚠️ **不要因为"不在暴露面"就整条丢掉**：上一期日报把 EPICS 归为"仅作信号存档"，方向是对的；但本条的**两个可迁移模式（固定挑战响应、第三方组件版本脱节）应落到我方自查项**，而不是只存档
- ⚠️ **CVSS 引用必须带口径**：8.2（v3.1）/ 9.3（v4.0）是 CISA 按产品场景打的分；9.9 是 libwebp 上游 CVE 的通用分。**混用会让我方对外引用失真**
- ⚠️ **"未报告在野利用"不等于安全**，更不等于我方可以降级处理

---

## 六、参考意义

> 📌 **本阶段口径（2026-11-12 起）**：转评审只看 **网络安全 / 信创 / 等保 / 隐私保护 / 护网** 五个方向，**暂不精到具体产品**；库内缺产品特性与应用场景材料，凭情报做产品对应会失真。下列**产品线级关联一律标 🟡 待复核，不进排期**。

| 方向（五方向） | 可证事实 | 本阶段处理 |
|---|---|---|
| **网络安全** | ① CVE-2026-16436：密码找回**挑战响应对所有用户相同且固定**，属**认证设计缺陷**（与厂商/版本无关）；② CVE-2023-4863 这个 **2023 年的上游 CVE 落在 2026 年当前发布版 10.97–10.97.2 内**（第三方组件版本与主产品脱节）；③ MC Works64 / GENESIS32 / BizViz 全版本受影响且**厂商不提供补丁**、只给迁移方案 | ✅ **进评审（方向级）** —— 落**基线/差距清单**形态：① 挑战响应基线自查项（随机、逐用户唯一、一次性）；② 第三方组件与镜像版本清单；③ 采购条款中的厂商 EOL 迁移责任。**产品本身不在我方暴露面 → 不产专项整改**（第 1 关不过） |
| **护网 / 攻防准备** | 认证绕过 + DCOM 权限分配不当属**可复用的攻击手法**，与既有 WAF 观测到的 `.svn/entries` 探测、批量备份文件扫描同属"运维遗留面" | 🟡 **进方向级对照表** —— 补入 [攻击手法→防线覆盖度对照](../deliverables/remediation-defenseTacticCoverage-20261112.md)，标注已覆盖/部分/未覆盖 |
| **信创 / 等保 / 隐私保护** | 无可证事实 | — |

**产品线级关联（🟡 待复核 · 按本阶段口径不落产）**：
| 影响产品线 | 影响点 | 是否需改行为 |
|---|---|---|
| 品能者托管 / 兆瓦快链 · 平台账号体系 | 自查密码找回、设备解锁、远程运维通道的挑战响应是否**随机、逐用户唯一、一次性**（对标 CVE-2026-16436 模式） | 🟡 **需改**（自查项，不新建产物） |
| 全部平台 · 依赖与镜像管理 | 建立**第三方组件版本清单**（对标 CVE-2023-4863 模式：2023 年 CVE 存在于 2026 年当前版） | 🟡 **需改**（清单化，属上期"监控平台自查"的延续） |
| 兆瓦快链 · 设备/监控选型条款 | 采购电站监控与历史数据库类产品时，条款增加"厂商停止补丁时的迁移/替换责任" | 🟡 需改（采购条款） |
| 我方技术栈本身（GENESIS/ICONICS/MC Works64） | — | ❌ **不在暴露面，不整改** |
| PTM 现货交易平台 | 无直接接口 | ⚪ 无动作 |

**暴露面判定（按评审第 1 关）**：

| 对象 | 在我方暴露面？ | 依据 |
|---|---|---|
| GENESIS64 / ICONICS Suite / Hyper Historian 等 10 个产品 | ❌ **否** | 我方为自研 Web 平台与电站托管系统，技术栈不含三菱/ICONICS 产品 |
| 第三方组件版本脱节模式（CVE-2023-4863） | ⚠️ **待自查** | 我方镜像与依赖清单未做全量第三方组件版本盘点 |
| 固定挑战响应模式（CVE-2026-16436） | ⚠️ **待自查** | 我方密码找回与运维通道的挑战响应生成方式未逐项核过 |
| 我方监控平台 API 鉴权/越权读（上期已列） | ⚠️ 待自查 | 延续项 |

---

## 七、总结输出

**一句话结论**：CISA ICSA-26-300-02（v3.1 9.1）通报的四个漏洞**产品本身不在我方暴露面、不进整改**，但它提供了两个**比漏洞本身更值得记的模式** —— **密码找回挑战响应对所有用户相同且固定**（认证设计缺陷，任何自研系统都可能犯）与 **2023 年的 libwebp 漏洞躺在 2026 年的当前发布版里**（第三方组件版本与主产品脱节）；这两个模式应当直接落进我方的自查清单，而"三个产品无补丁只给迁移方案"则应写进采购选型条款。

**本阶段处理**：✅ 网络安全 / 🟡 护网 —— **方向级进评审**（基线 / 覆盖度对照 / 采购条款），**产品级不落产**；下列标注产品线级的条目一律 🟡 **待复核**。

**落地去向**

- [ ] **专项整改** —— 平台密码找回 / 设备解锁 / 远程运维通道的挑战响应自查（是否随机、逐用户唯一、一次性），对标 CVE-2026-16436
- [ ] **专项整改** —— 建立第三方组件版本清单（含镜像与依赖），对标 CVE-2023-4863"旧 CVE 存在于当前版本"模式；与上期"监控平台 API 鉴权/越权读自查"合并推进
- [ ] **需求变更** —— 电站监控与历史数据库类产品的采购条款增加"厂商停止补丁时的迁移/替换责任"
- [ ] **跟踪项** —— 纳入 CVE watchlist（CISA CSAF 源），观察是否出现在野利用报告
- [ ] **明确不落产** —— 三菱/ICONICS/MC Works64 四个漏洞本身**不在我方暴露面**，不生成专项整改产物（第 1 关不过）

---

## 参考链接

- [CISA：ICSA-26-300-02 Mitsubishi Electric / Iconics GENESIS、GENESIS64、ICONICS Suite 等（官方通告，2026-10-27 转发 / 10-29 修订）](https://www.cisa.gov/news-events/ics-advisories/icsa-26-300-02)
- [OT/ICS Monitor：ICONICS GENESIS64 ICSA-26-300-02 — Fixed Unlock Challenge Response, DCOM Privilege Flaw and No Fix for MC Works64](https://otsecuritywire.com/articles/mitsubishi-iconics-genesis64-icsa-26-300-02-challenge-response-dcom-libwebp-2026)
- [CN-SEC：工业网络安全周报 2026 年第 41 期（含 ICSA-26-300-02 中文口径）](https://cn-sec.com/archives/5545773.html)
- [工业控制 Hub：The Vulnerability Is Older Than Your HMI（CVE-2023-4863 落在当前版本）](https://www.indctrlhub.com/blogs/industrial-news/iconics-spare-hmi-image-baseline-2026)
- [SecurHUB：CISA Warns GENESIS and ICONICS Users: Version 10.97.3 Doesn't Fix All Vulnerabilities](https://www.securhub.pl/en/blog/2026-10-28-cisa-warns-genesis-and-iconics-users-version-10-97-3-doesn-t-fix-all)
- [Trout Software：One Unlock Code for Every User（CVE-2026-16436 分析）](https://www.trout.software/blog/mitsubishi-iconics-genesis64-authentication-bypass-icsa-26-300-02)
- [相关：epicsDerExposure-2026-11（EPICS 与 DER 暴露面）](epicsDerExposure-2026-11.md)

# EPICS Base 四个工控漏洞 + 分布式光伏 DER 暴露面研究 — 2026-11

> CVE-2026-114595/114596/114597/114598 · CISA ICSA-26-300-01(Rev.1) · 2026-10-27 发布
> 分类：🟡 **有影响**（我方技术栈不含 EPICS，但光伏 DER 暴露面研究直接命中我方业务形态）

## 一句话结论

**两个独立信号指向同一件事：光伏侧的远程监控/控制入口正在成为真实攻击面** —— EPICS 四个免认证可 RCE 漏洞证明工控协议栈长期裸奔，而互联网规模扫描显示光伏 DER（逆变器+监控平台）的暴露程度远超预期。

---

## 信号一：EPICS Base 工控栈裸奔

### 漏洞清单

| CVE | 类型 | CVSS v3.1 / v4.0 | 后果 |
|---|---|---|---|
| CVE-2026-114595 | CWE-190 整数溢出 | **9.8** / 9.3 | 攻击者可控的堆上越界写 → 拒绝服务或**远程代码执行** |
| CVE-2026-114596 | CWE-190 整数溢出 | **8.2** / 8.8 | 协议解析消息长度校验失效 → 越界内存写、控制流受影响 |
| CVE-2026-114597 | CWE-130 长度参数不一致 | 7.5 / 8.7 | 越界内存读 |
| CVE-2026-114598 | CWE-843 类型混淆 | 7.5 / 8.7 | 越界读 |

**共同特征（决定了这批漏洞的严重性）**：

- 全部**免认证、需用户交互为零、仅需网络可达**
- 受影响协议：EPICS Channel Access / pvAccess（TCP **5064** 与 **5075**）
- 影响版本：**EPICS Base 7.0.10 及更早**，修复版本 **7.0.11**
- 全球约 90 个大型科研/高校/工业项目在用，含 ITER 聚变堆控制系统、阿贡国家实验室 APS

**发现方式值得注意**：Causal Security 的自主 agent **Cipher** 用 **3 小时 49 分**、一条指令，在几十年历史的开源工控软件里挖出 4 个此前未知漏洞。OT 领域"靠隐蔽性防守"的前提正在失效。

### 我方暴露面判定

| 问 | 答 |
|---|---|
| 组件是否在我方技术栈 | **否** —— 我方托管平台是 Web 应用，不含 EPICS |
| 是否对外暴露 | 不适用 |
| 是否可达 | 不适用 |
| **结论** | **不在暴露面** —— 但信号本身有价值（见下） |

> 按 [评审门槛第 1 关](../../meta/pipeline.md)，纯漏洞本身不满足"影响可证"，**不进 `deliverables/`**。
> 但它提供了"工控协议栈长期无认证"的**结构性证据**，这条证据指向信号二。

---

## 信号二：分布式光伏 DER 的互联网暴露面（直接命中我方业务形态）

### 研究结论

学术界的互联网规模评估（2026-09 发布）针对**并网光伏 DER**（太阳能逆变器 + 监控平台）：

- 全球光伏装机自 2022 年以来**翻了一倍以上**，部署规模空前
- 大量系统由**安装商或终端用户**配置，为便于监控控制而**直接联网**
- 论文做了互联网规模的暴露与脆弱性评估，评估**被入侵的 DER 对电网可能构成的风险**
- ⚠️ 关键发现：**真实世界的互联网暴露规模及其对电网运行的影响，此前被严重低估**

### 我方暴露面判定

| 问 | 答 |
|---|---|
| 是否涉及我方业务 | **是** —— 我方托管的正是分布式/集中式光伏电站的逆变器与监控数据 |
| 暴露形态 | 电站侧设备直连公网 + 我方托管平台的对外接口 |
| 是否可验证 | **可验证** —— 我方自身 WAF 日志已记录到针对电站管理接口的真实探测 |

**实证（内部 WAF 数据）**：

| 时间 | 攻击源 | 目标 | 特征 |
|---|---|---|---|
| 2026-11-12 08:41 | `45.138.12.51` | `https://182.140.209.35:18443/.svn/entries` | SVN 元数据探测，**5 小时内触发 28 次** |
| 2026-11-11 ~ 11-12 | 多个 `42.92.x.x` | `idmo.pinnenger.com:11443` | 批量探测 `/wwwroot.zip` `/webs.rar` `/php.zip` `/pinnenger.com.sql` 等**备份文件** |
| 2026-11-12 11:34 | `49.73.18.161` | `https://ptm.pinnenger.com:1443/itps/ptm/allocation/logisticsFileDownLoad` | 响应侧规则命中（`m_response`） |

> **"探测备份文件"这个行为模式，与 DER 研究中"设备与监控平台直接暴露公网"的结论高度吻合** —— 扫描者在找运维过程中遗留的凭据与配置。

### 两个必须跟进的技术点

**① SVN 元数据目录未清理**

`.svn/entries` 被探测 28 次 —— 说明 WAF 拦截了请求，但**服务器端是否真的存在 `.svn` 目录，必须自查**。SVN 1.7+ 默认不再在服务端保留 `.svn/`，但老版本工作副本升级后可能残留。若残留，攻击者可还原完整源码与凭据。

**② 备份文件扫描未果不代表文件不存在**

`42.92.x.x` 段持续批量探测 `/wwwroot.zip` `/webs.rar` `/pinnetDc.sql` 等 —— WAF 已拦下请求，但**源站上是否真的存在这些文件，是另一个问题**。这类扫描的逻辑是"广撒网 + 事后验证"，只要有一个站点漏了，扫描器就会回来验证。

---

## 落地去向

- [x] **专项整改** —— 自查所有对外站点是否存在 `.svn/` 残留目录与备份文件（`.zip`/`.rar`/`.sql`/`.tar.gz`）
- [ ] 产品特性 —— 待自查结论明确后再评估（如果发现普遍残留，可能需要在发布流程中加自动检查）
- [ ] 需求变更 —— 待定

---

## 关联外部信号

**CISA OT/ICS 通告（2026-11 摘录）**：

| 通告 | 严重度 | 产品 | CVE | 领域 |
|---|---|---|---|---|
| ICSA-26-307-01 | critical | Subnet Solutions PowerSYSTEM Center | CVE-2026-63017 / CVE-2026-63774 | 制造、能源 |
| ICSA-26-302-03 | high (8.8) | Hitachi Energy CoreTec | — | 能源 |

> ⚠️ **Subnet Solutions PowerSYSTEM Center 的 CVE-2026-63017 是 SQL 注入导致未授权执行 SQL 命令** —— 该产品是**电网监控**系统，与我方"电站监控平台"同类。建议纳 CVE watchlist 持续跟踪。

**CVE-2026-115803**：Scada-LTS 2.8.0 AmCharts Data API 授权绕过（`ids` 参数可篡改 → 越权读取 SCADA 数据与配置）。同为 SCADA 平台同类问题。

---

## 参考链接

- [CN-SEC：11月2日高危漏洞紧急预警（含 EPICS 四 CVE 完整口径）](https://cn-sec.com/archives/5551496.html)
- [Seclog：CISA warns four EPICS Base vulnerabilities](https://seclog.org/stories/cisa-warns-four-epics-base-vulnerabilities-including-critical-cve-2026-114595-could-let-attackers-cr.html)
- [汇智网：AI 挖出 4 个工控漏洞](https://www.hubwiz.com/blog/ai-agent-found-four-epics-vulnerabilities/)
- [Conceptio：Grid Trouble in Paradise — 分布式 DER 暴露面研究](https://www.conceptio.app/document/667918/grid-trouble-in-paradise-uncovering-vulnerable-distributed-energy-reso)
- [Ervik：OT & ICS Security Advisories（CISA CSAF 实时源）](https://www.ervik.as/ot-security)
- [rootpwn：CVE-2026-115803 Scada-LTS](https://rootpwn.me/cves/CVE-2026-115803)
- [CISA ICS Advisories 官方源](https://www.cisa.gov/news-events/ics-advisories)

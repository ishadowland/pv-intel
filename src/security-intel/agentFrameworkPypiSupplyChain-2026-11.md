# Microsoft agent-framework PyPI 投毒（1.26.1 / 1.26.2）：凭据窃取器随每次 Python 启动执行，攻的是云与 CI 令牌

> 🟡 有影响 · 采集于 2026-11-20 · 核心标识：**2026-11-17 20:35 UTC 恶意版 `agent-framework` 1.26.1 上传 PyPI，21:08 上传 1.26.2，约 21:30 双版本下架** · **该包周下载量约 41,000** · **最新安全版本 1.26.0** · ⭐⭐⭐ **库内第一次取得"我方一手可核的一手证据"：PyPI 官方 JSON 接口的发布历史里 1.26.1 / 1.26.2 两条记录已完全消失（不是 yank，是删除），`info.version` 仍为 1.26.0** · ⭐⭐ **持久化机制是 `.pth` 文件 → Python 每次启动都执行，导入与否无关** · ⭐⭐ **攻击目标是 Azure / Azure DevOps / GitHub Actions OIDC 与托管身份令牌（有效期可达 24 小时）** · ⭐ **仅 3 例真实外泄被确认（50 个免费额度请求中，4 个来自攻击者自己、29 个是沙箱与厂商扫描）** · ⚠️ **我方侧结论：库内无我方使用该包的一手证据 → 不得下"我方已中招"结论，转"待核实 + 方向级供应链基线"**

---

## 一、信源核实

| 项 | 值 |
|---|---|
| 来源请求 | `Microsoft agent-framework PyPI malicious 1.26.1 1.26.2 credential stealer November 2026`（web_search，命中 Wiz 官方研究博客、Chainguard Unchained 安全博客、PyPI 官方发布历史接口） |
| 原始 URL（主 1 · 第三方深度分析 · Wiz） | https://wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi （Wiz Research 官方博客《Microsoft agent-framework Compromised: Credential Stealer Targets Azure and CI Pipelines》，**2026-11-17 发布、2026-11-18 14:00 UTC 更新根因与外泄数据分析**） |
| 原始 URL（主 2 · 第三方独立分析 · Chainguard） | https://www.chainguard.dev/fr-FR/unchained/microsoft-agent-framework-compromised-on-pypi-november-2026 （Chainguard Unchained，**作者署名 Quincy Castro（CISO）**，**2026-11-17**，标题即写明"1.26.1 and 1.26.2 ship a credential stealer that runs on every Python start"） |
| 原始 URL（主 3 · 一手来源 · PyPI 官方接口） | https://pypi.org/pypi/agent-framework/json （PyPI 官方 JSON API · 发布历史 / 当前版本 / yank 状态） |
| 发布主体 | **Wiz（云安全厂商 · 研究团队）** · **Chainguard（软件供应链安全厂商）** · **PyPI（Python 官方包索引 · 一手来源）** |
| 发布/更新时间 | Wiz **2026-11-17**（**2026-11-18 14:00 UTC 增补根因与外泄数据解析**）· Chainguard **2026-11-17** · PyPI 发布历史为**实时快照**（采集时刻状态） |
| 采集时间 | 2026-11-20 07:13:32 ~ 07:29:26 |

**快照清单**（SHA256 取自 `.meta.json` 的 `sha256_raw` 字段，正文字符数取自 `text_chars`）

| 快照 | SHA256 | 抓取时间 | 正文字符 | HTTP | 备注 |
|---|---|---|---|---|---|
| `raw/snapshots/security/wiz-agent-framework-pypi-20261117.md` | `3b277e134d2e4cd27bb7200633b5b7f423ab2739dca7c5244dd5d9468c5fbcf0` | 2026-11-20 07:13:32 | 10,228 | 200 | ✅ Wiz 官方研究博客（主源，含完整时间线与 IOC） |
| `raw/snapshots/security/chainguard-agent-framework-pypi-20261117.md` | `773f947ddd081205b725e9fc3b97fded1f0b03a16db739ad4f82470c47d5aca5` | 2026-11-20 07:13:33 | 13,637 | 200 | ✅ Chainguard 独立分析（交叉印证） |
| `raw/snapshots/security/pypi-agent-framework-releasehistory.md` | `9b8b433ff0a3a3c594ef5a25c4c756d530d7b3d23cd6a9b9df2785404eecc1c2` | 2026-11-20 07:29:26 | 60,018 | 200 | ✅ **PyPI 官方一手发布历史（本次唯一的一手法源）** |

> 📎 **入库理由**：库内安全域至今所有条目都是"**外部产品/组件被攻击**"（EPICS、Siemens、Mendix、meta-iot2050、PHP 反序列化、凭据收割扫描器、Java4Shell）。⭐⭐⭐ **本条是库内第一条"我方自己所处的软件供应链被投毒"** —— 攻击者**不打我方的系统，而是打我方构建系统**：**污染一个上游包，让恶意代码在我方 CI 里、在每一次 Python 进程启动时运行**。⭐⭐ **它的价值在于把库内 11-16 已记的"外部凭据收割扫描器"这条线的**源头**补上了 —— 那时我们知道攻击者在扫 `.env` / `.git/config`，但不知道他们要的那些凭据是从哪来的；**本条给出了一条真实的、已被证实的投递路径**（供应链 → CI 令牌 → 云身份）。
> ⭐⭐⭐ **本次同时补齐了库内一直缺的一手信源**：安全域此前多次出现"条款级正文靠单一转载源"的缺口（如库内 11-19 已记的商务部回收意见），**本条有一份真正的一手来源 —— PyPI 官方 JSON 接口的发布历史**，可由任何人独立复核。
> ✅ **安全域双信源要求本期满足**：**第三方独立分析 2 家（Wiz / Chainguard）+ 一手来源 1 份（PyPI 官方接口）**。

---

## 二、事实核查

| 数据点 | 原文表述 | 核查方式 | 结论 | 备注 |
|---|---|---|---|---|
| **⭐⭐⭐ 恶意版本在 PyPI 上已被"删除"而非"yank"** | **PyPI 官方 JSON 接口快照**：全文检索 `1.26.1` → **0 处命中**；版本标识只出现 `1.26.0`；`"version":"1.26.0","yanked":false`；发布历史中**不存在 1.26.1 / 1.26.2 的任何条目** | 对 PyPI 官方 JSON 快照做版本串与 yanked 字段的穷举检索 | ✅ **已核（一手法源直接读出）** | ⭐⭐⭐ **这是本条最硬、也最有操作价值的一条我方一手事实**：**两个恶意版本不是被 yank（撤下标记），而是从发布历史里彻底消失**。⭐⭐ **三个直接后果**：① **`pip install agent-framework==1.26.1` 现在会直接报"无匹配发行版"**（不会静默安装恶意包）→ **"重新安装一遍"不是修复手段**；② **但 pip 缓存 / CI 缓存 / 容器层 / 私有 wheel 镜像里的旧包仍在**，且 **pip 会优先使用本地缓存而不回源** → **缓存不清就等于没修**；③ **任何 lockfile / requirements 里还写着 `1.26.1` / `1.26.2` 的构建会直接失败**（这是好事，失败即暴露）→ **CI 突然变红的地方就是受影响的构建**。⭐ **正确表述是"恶意版本已从 PyPI 删除"，不得写成"已 yanked"** |
| **⭐⭐⭐ 投毒时间线与版本** | Wiz：*"At **20:35 UTC on November 17, 2026**, a malicious version (**1.26.1**) of the agent-framework package … was uploaded to PyPI. A second version, **1.26.2**, followed at **21:08 UTC**. As of **21:30 UTC**, both versions were no longer available on PyPI. The package gets about **41,000 downloads a week**. The most recent safe version is **1.26.0**"*；时间线表：*2026-11-12 18:25 合法版 1.26.0 发布* / *11-17 20:35 恶意 1.26.1* / *~21:08 恶意 1.26.2* / *~21:30 两版下架* | Wiz 快照逐字 + Chainguard 快照交叉（同一日期与两个版本号）+ **PyPI 一手快照确认当前版本仍为 1.26.0** | ✅ **已核（三源一致）** | ⭐⭐ **窗口期极短：从首发到下架约 55 分钟**。⭐⭐ 但 **"55 分钟"不等于风险小** —— 因为 **1.26.1 在 ~21:30 前已有真实下载窗口，且安装后不需要再联网即可持续生效**（`.pth` 每次 Python 启动都跑）。⭐ **窗口期短 ≠ 受害面小**（详见下方"真实外泄仅 3 例"那条的对照） |
| **⭐⭐⭐ 持久化机制：`.pth` 文件（与"是否 import"无关）** | Wiz：*"When a malicious version is installed, it drops a **.pth file into the site-packages root** (`agent_framework_meta.pth` in 1.26.1, `af_runtime_diag.pth` in 1.26.2). **Python runs .pth files on every interpreter start**, so the credential stealer runs whenever Python starts in that environment, **even if agent-framework is never imported**"* | Wiz 快照逐字 + Chainguard 标题与正文独立同述（*"run on every Python start"*） | ✅ **已核（两源一致）** | ⭐⭐⭐ **这是本条最需要被我方记住的技术事实**：**`.pth` 机制绕过了"我们不用这个包就没事"的直觉** —— 装过 = 常驻。⭐⭐ **对我方的直接推论**：**"没在代码里 import 它"不是豁免理由**，必须查 **site-packages 目录内容**；⭐ **且"删掉包目录"也不等于清理** —— `.pth` 是独立文件，卸载时若未清干净仍可能残留（**卸载后必须复查 site-packages**，此推论为机制推演，原文未直接给出"卸载后残留"的结论） |
| **⭐⭐ 1.26.2 换了触发器（只查 1.26.1 的文件名会漏）** | Wiz：*"**1.26.2 was a repacked 1.26.1** … with these changes: **New trigger.** `agent_framework_meta/__init__.py` is restored to the clean 1.26.0 file. Instead, a new top-level `af_runtime_diag.pth` imports a new top-level module, `af_runtime_diag.py` … **Searching only for the 1.26.1 file names will miss this version**." | Wiz 快照逐字 | ✅ **已核（单源，但内容具体可核）** | ⭐⭐⭐ **这是本期最值得抄进检测规则的一条**：**IOC 检索必须覆盖两套文件名**（`agent_framework_meta.pth` / `agent_framework_meta/_telemetry.py` 与 `af_runtime_diag.pth` / `af_runtime_diag.py`），**只查一套 = 漏检**。⭐ **库内 11-19 已记的"`rule_whitelist_fastpath` 判定器只看规则名不看载荷"是同一类结构性缺陷**：**检测规则的输入维度不全，等于没有规则** |
| **⭐⭐ 凭据窃取范围（云与 CI 为主）** | Wiz：*"The stealer is focused on **Azure and Azure DevOps**. It collects: Environment variables with names containing strings such as **TOKEN, SECRET, PASSWORD, KEY, AZURE, AWS, GITHUB, OPENAI, HF_, FOUNDRY, NPM, PIP, NUGET, SYSTEM, BUILD, AGENT**；**Other processes' environments**（读最多 **300 个** `/proc/*/environ`）；**Credential files (up to 60)**：Azure CLI (`~/.azure/`)、`.npmrc`、`pip.conf`、`.netrc`、`.git-credentials`、`.docker/config.json`、Hugging Face tokens、**Azure DevOps agent `.credentials`**、`.env` 与 `/app`、`/workspace` 下的 JSON 文件"*；1.26.2 把匹配词扩到 **ACTIONS / OIDC / RUNNER / ARM_**，文件上限 **60 → 80** | Wiz 快照逐字 | ✅ **已核（单源，细节具体）** | ⭐⭐ **这条与库内 11-16 已记的"外部凭据收割扫描器字典"高度重叠但性质不同**：那批扫描器打的是 `.env` / `.git/config` / `phpinfo.php` 这类**对外暴露的文件**；**本条打的是 CI runner 内部的环境与凭据文件** → **我方 CI 环境的敏感度直接决定后果严重性**。⭐⭐ **`/proc/*/environ` 跨进程读取（300 个）意味着一个 Python 进程能读到同机其它进程的环境变量** → **在我方多进程共享 runner 上，这是横向扩散路径** |
| **⭐⭐⭐ 攻击目标直指云身份与 OIDC（最有价值的一条）** | Wiz：*"**Azure DevOps OIDC tokens**：if `SYSTEM_ACCESSTOKEN` and `SYSTEM_OIDCREQUESTURI` are set, it requests an OIDC token for `api://AzureADTokenExchange`"；*"**Azure managed-identity tokens from IMDS or the App Service identity endpoint** for **12 resources**：ARM、Graph、Key Vault、Storage、Cognitive Services、Azure AI/ML、Search、Container Registry、Azure DevOps、AzureADTokenExchange"*；1.26.2：*"In workflows with `id-token: write`, it requests OIDC tokens for `api://AzureADTokenExchange` and `https://management.azure.com/`. Where an **Entra ID federated credential trusts the workflow**, these tokens can be exchanged for Azure access, **with no stored secret needed**"*；处置建议：*"**Stolen managed-identity and OIDC-exchanged tokens are valid for up to 24 hours**"* | Wiz 快照逐字 | ✅ **已核（单源，但机制链条完整）** | ⭐⭐⭐ **这一条把风险从"泄露一个密码"升级为"泄露一个身份"**：**OIDC / 工作负载身份联合凭据（federated credential）意味着攻击者不需要任何存储密钥，就能换取云访问权**，且**令牌有效期长达 24 小时** → **"轮换密钥"这个标准动作在这里不够用，必须轮换/撤销"信任关系"（federated credential、managed identity 授权）**。⭐⭐ **这是我方最该拿去做自查的一条**，且**该自查不依赖我方是否用过 agent-framework** |
| **⭐⭐ 外泄规模：确认只有 3 例** | Wiz 数据分析节：*"Wiz Research was be able to analyze the **50 requests** that were stored by webhook[.]site's free tier. **Four** of the requests originated from the attacker's machines and the attack process. **Twenty-nine** of the requests appear linked to **sandbox environments, vendor scanning, and tests**. The remaining **seventeen requests represent only three unique, successful cases of exfiltration of victim data**"* | Wiz 快照逐字 | ✅ **已核（单源）** | ⭐⭐ **这条必须写进正文，否则容易把事件规模夸大**：**50 个请求 ≠ 50 个受害者**，**真实外泄仅 3 例**。⭐⭐ **webhook.site 免费额度的机制解释了为什么外泄如此少**：*"accepts at most **100 requests**… After that, new requests get HTTP **410 Gone** or **429 Too Many Requests** and are not logged… expires after **7 days**"* → **攻击者的"出口"本身就是个免费额度限流的公共站点 → 受害者少是被出口容量限制的，不是攻击者收手了**。⭐ **这是我方必须理解的机制性教训：攻击者用公共服务做外传通道，其规模上限由该服务的免费额度决定；一旦换成自建基础设施，规模可以完全不同于 3 例** |
| **⭐⭐ 根因：上游发布凭据被攻破（且细节未明）** | Wiz：*"The attacker appears to have **compromised a client certificate and private key for Microsoft ESRP**（Engineering System Release Pipeline）, the internal service Microsoft uses to sign and publish this package. Their **first publish attempt, from AWS, was rejected by ESRP's IP filtering. A second attempt from Microsoft-owned IP space succeeded. How the credentials were obtained is not yet known."*；攻击者工具自报为开源 AI 渗透框架 **Cairn**，暂存路径 `/tmp/cairn_pkg`，发送 `CAIRN_ESRP_PROBE2` 连通性探测 | Wiz 快照逐字（并注明"Updated Nov 18 14:00 UTC — 更新根因与外泄数据分析"） | ✅ **已核（单源）** | ⭐⭐ **两个硬事实**：① **发布签名凭据（客户端证书 + 私钥）被盗用**，**而不是 PyPI 账号密码被盗** → **含义是"签名体系被绕过"，比"账号被偷"影响面更大**；② **第一次从 AWS IP 发布被 IP 过滤拦下，第二次从"微软自有 IP 段"发布成功** → ⭐⭐ **这正是库内已记的"照抄官方建议会出事"类陷阱的另一面：攻击者会利用任何可用的合规出口，我方的 IP 白名单策略若只看 ASN/归属就会失效**。⚠️ **"凭据如何取得仍未知"—— 不得推测归因**。⭐⭐ **另有一条值得警惕的行为学信号**：攻击者**主动使用开源 AI 渗透框架（Cairn）并用探测包名做连通性自检** → **AI 辅助攻击已从"发现漏洞"延伸到"端到端投递"**（与库内 11-19 已记的"1 小时定位 / 2 小时写出利用代码"同向，但**这是第一次出现在供应链投递环节**） |
| **⭐ 事件关联与未关联项** | Wiz：*"Earlier this year, another Microsoft Python package, `durabletask`, was compromised after its **PyPI token was stolen**. **We have not linked the two incidents**"* | Wiz 快照逐字 | ✅ **已核** | ⚠️ **明确不得把两起事件合并叙事**（官方明确"未关联"）。⭐ **可入库的只是"该上游今年内已发生第二起 Python 包投毒"这一事实** |
| **⭐⭐ 处置建议（可直接转为检查项）** | Wiz：*"**Identify exposure**: search **lockfiles, CI logs, virtualenvs and container images** for agent-framework 1.26.1 or 1.26.2. **Pin to 1.26.0**. **Check for execution**: look in site-packages for `agent_framework_meta.pth` and `agent_framework_meta/_telemetry.py` (1.26.1), or `af_runtime_diag.pth` and `af_runtime_diag.py` (1.26.2). **Check egress**: search proxy and DNS logs for `webhook[.]site/d381fd80-…`. **A 200 means that host's data was accepted. A 410/429 suggests it was rejected.** Rotate credentials … Audit Azure identities … **Stolen managed-identity and OIDC-exchanged tokens are valid for up to 24 hours.** Audit GitHub Actions (1.26.2): for workflows that installed 1.26.2 with `id-token: write`, treat GitHub OIDC tokens … as exposed."* | Wiz 快照逐字 | ✅ **已核（单源）** | ⭐⭐⭐ **注意那句"200 = 数据被接受；410/429 = 被拒绝"** —— **这是本条最实用的一条检测语义**：**我方出口代理日志里的 HTTP 状态码直接就是"是否已外泄成功"的判据**，比我方自己去分析载荷更简单。⭐⭐ **且这条检测完全不需要我方用过该包**：只要我方有 Python 运行环境（有虚拟环境/容器/构建机），**"site-packages 里有无 `.pth` 文件"就是一条通用体检项** |
| **⭐ IOC（可落成规则）** | Wiz 给出 11 条 IOC：外传端点 `https://webhook[.]site/d381fd80-ec62-42ad-8f5c-d1b15103c9bb`（参数 `?t=telemetry`）；两个 User-Agent（`af-runtime-diagnostics/1` = 1.26.1、`runtime-diagnostics/1` = 1.26.2）；两个 `.pth` 持久化文件；两个窃取器模块；运行标记环境变量 `_AF_TEL=1`；三个哈希；两个 wheel 的 SHA256（`agent_framework-1.26.1-py3-none-any.whl` = `d27fa344…`、`1.26.2` = `3d20a8bc…`） | Wiz 快照逐字 | ✅ **已核（单源）** | ⭐⭐ **其中 `_AF_TEL=1`（避免子进程重复运行的"只跑一次"标记）是很聪明的一类 IOC** —— 进程环境变量检索比文件检索更容易命中正在运行中的恶意实例。⭐ **轮换建议**：把"User-Agent 检索"与"`_AF_TEL` 环境变量检索"写进边界/主机侧规则 |

> **核查小结**：本期 **3 份快照 / 3 个独立发布主体**（Wiz + Chainguard + **PyPI 官方接口**），**关键事实（时间线、版本、`.pth` 持久化、窃取范围、OIDC/托管身份、仅 3 例真实外泄、IOC、处置建议）以 Wiz 原文为准并由 Chainguard 独立印证事件存在与机制**；⭐⭐⭐ **唯一由我方直接从一手来源读出的关键事实是"1.26.1 / 1.26.2 已从 PyPI 发布历史中彻底消失（非 yank），当前版本仍为 1.26.0"**。**必须写明的边界**：① **真实外泄仅 3 例（不是 50 例）**，外泄少的原因是**外传通道是 webhook.site 免费额度（上限 100 请求、7 天过期）**，**不得据此判断攻击规模小**；② **"凭据如何取得"官方明说未知 → 不得推测归因**；③ **`durabletask` 事件官方明说"未关联"**；④ **1.26.2 换了触发器 → 只查 1.26.1 文件名会漏检**；⑤ **卸载后 `.pth` 是否残留属机制推演，原文未给出结论**；⑥ **Wiz 的分析结论属第三方研究，PyPI 侧只有"版本已消失"是一手可核事实**。

---

## 三、原文归档（快照）

- 快照文件（3 份，**全部入库**）：
  - `raw/snapshots/security/wiz-agent-framework-pypi-20261117.md`（SHA256 `3b277e134d2e4cd27bb7200633b5b7f423ab2739dca7c5244dd5d9468c5fbcf0`，抓取 2026-11-20 07:13:32，10,228 字符）—— Wiz 研究博客
  - `raw/snapshots/security/chainguard-agent-framework-pypi-20261117.md`（SHA256 `773f947ddd081205b725e9fc3b97fded1f0b03a16db739ad4f82470c47d5aca5`，抓取 2026-11-20 07:13:33，13,637 字符）—— Chainguard Unchained
  - `raw/snapshots/security/pypi-agent-framework-releasehistory.md`（SHA256 `9b8b433ff0a3a3c594ef5a25c4c756d530d7b3d23cd6a9b9df2785404eecc1c2`，抓取 2026-11-20 07:29:26，60,018 字符，**已截断**）—— PyPI 官方 JSON 发布历史

**关键原文摘录（Wiz Research，2026-11-17，2026-11-18 14:00 UTC 更新）**：

> At **20:35 UTC on November 17, 2026**, a malicious version (**1.26.1**) of the agent-framework package (Microsoft Agent Framework) was uploaded to PyPI. A second version, **1.26.2**, followed at **21:08 UTC**. As of **21:30 UTC**, both versions were no longer available on PyPI. The package gets about **41,000 downloads a week**. The most recent safe version is **1.26.0**.
> When a malicious version is installed, it drops a **.pth file** into the site-packages root … **Python runs .pth files on every interpreter start**, so the credential stealer runs whenever Python starts in that environment, **even if agent-framework is never imported**.
> The attacker appears to have **compromised a client certificate and private key for Microsoft ESRP** … Their **first publish attempt, from AWS, was rejected by ESRP's IP filtering. A second attempt from Microsoft-owned IP space succeeded. How the credentials were obtained is not yet known.**
> … a visualization of the 50 free-tier requests … **Four** of the requests originated from the attacker's machines … **Twenty-nine** … appear linked to sandbox environments, vendor scanning, and tests. The remaining **seventeen requests represent only three unique, successful cases of exfiltration of victim data.**
> **Check egress**: search proxy and DNS logs for `webhook[.]site/d381fd80-…`. **A 200 means that host's data was accepted. A 410/429 suggests it was rejected.**

**关键原文摘录（Chainguard Unchained，2026-11-17，署名 Quincy Castro / CISO）**：

> **Microsoft agent-framework compromised on PyPI: 1.26.1 and 1.26.2 ship a credential stealer that runs on every Python start (November 2026)**

**关键原文摘录（PyPI 官方 JSON 接口 · 我方一手核验，2026-11-20 07:29:26）**：

> `"version":"1.26.0","yanked":false` —— **当前 `info.version` 为 1.26.0**；
> **全文检索 `1.26.1` → 0 处命中**；版本标识仅出现 `1.26.0`；
> **发布历史中不存在 1.26.1 / 1.26.2 的任何条目（既未列出，也未标记 yanked）**。

---

## 四、概要提取

- **2026-11-17 20:35 UTC 起，恶意版本 `agent-framework` 1.26.1 与 21:08 的 1.26.2 被投放到 PyPI，约 21:30 双双下架（窗口约 55 分钟）；该包周下载量约 41,000，最新安全版本 1.26.0** —— 攻击目标是 **Azure / Azure DevOps / GitHub Actions 的云身份与 CI 令牌**。
- **⭐⭐⭐ 持久化机制是 `.pth` 文件 → Python 每次启动都执行，与是否 import 无关** —— **"我们不用这个包"不等于没中招**；⭐⭐ **1.26.2 换了触发器（`af_runtime_diag.pth` / `af_runtime_diag.py`），只查 1.26.1 的文件名会漏检** → **IOC 检索必须覆盖两套文件名**。
- **⭐⭐⭐ 我方一手核验（PyPI 官方 JSON 接口）：1.26.1 / 1.26.2 已从发布历史中彻底消失（不是 yank），当前版本仍为 1.26.0** → ① **`pip install agent-framework==1.26.1` 现在直接失败**（"重装一遍"不是修复手段）；② **pip / CI 缓存、容器层、私有 wheel 镜像里的旧包仍在，且 pip 优先用本地缓存不回源 → 缓存不清等于没修**；③ **lockfile 里仍写着 1.26.1 / 1.26.2 的构建会直接失败（失败即暴露）**。
- **⭐⭐ 外泄规模必须按原文口径写：确认仅 3 例真实外泄**（50 个免费额度请求中，4 个来自攻击者自己、29 个是沙箱与厂商扫描）—— ⚠️ **外泄少是因为外传通道是 webhook.site 免费额度（上限 100 请求 / 7 天过期），不是攻击者收手**；⭐ **检测语义很实用：出口代理日志里该 URL 返回 200 = 数据已被接受，410/429 = 被拒绝**。
- **⭐⭐ 根因是上游发布签名凭据（ESRP 客户端证书 + 私钥）被攻破**，**"凭据如何取得"官方明说未知 → 不得推测归因**；⭐⭐ **第一次从 AWS IP 发布被 IP 过滤拦下、第二次从"微软自有 IP 段"发布成功** → **攻击者会利用任何合规出口**；⭐ **攻击者工具自报为开源 AI 渗透框架 Cairn** → **AI 辅助攻击首次延伸到供应链投递环节**。

---

## 五、主要观点

**原文主张**

- Wiz（研究方）：攻击者窃取了 Microsoft 内部发布服务 **ESRP 的客户端证书与私钥**，从而**用被污染的包冒名发布**；恶意包的机制是**在 site-packages 根目录投放 `.pth` 文件，使窃取器在每次 Python 启动时执行**，与是否导入该包无关；1.26.2 是重新打包版本并**更换了触发器**，因此**仅按 1.26.1 的文件名检索会漏检**；窃取范围**聚焦 Azure 与 Azure DevOps**，覆盖环境变量、其它进程环境（最多 300 个 `/proc/*/environ`）、最多 60（1.26.2 为 80）个凭据文件、**Azure DevOps OIDC 令牌**与**12 类 Azure 资源的托管身份令牌**；**被窃取的托管身份与 OIDC 交换令牌有效期可达 24 小时**；外传通过公共请求检查服务 `webhook[.]site` 完成，其**免费额度上限 100 请求、7 天过期**，因此**实际外泄仅 3 例**；并给出完整处置清单（锁文件 / CI 日志 / 虚拟环境 / 容器镜像检索并**锁定 1.26.0**、site-packages 执行痕迹检查、**代理与 DNS 日志按 HTTP 状态码判别是否已被接受**、凭据轮换、Azure 身份审计、GitHub Actions `id-token: write` 审计）。
- Chainguard（第三方）：事件性质明确为 **"1.26.1 与 1.26.2 随包投递凭据窃取器，且在每次 Python 启动时运行"**。
- PyPI（一手，仅状态事实）：**当前发布版本为 1.26.0，1.26.1 / 1.26.2 的发布记录已不存在**。

**我方判断**

- ⭐⭐⭐ **本条对我方的真正价值不是"又一个恶意包"，而是它第一次把库内 11-16 那条线的"前半截"补上了。** ⭐⭐ 库内 11-16 已记"外部凭据收割扫描器"（3,158 云实例 / 92 网段 / 3,299 UA / 36,000 端口，字典含 `.env`、`.git/config`、`phpinfo.php`），我方三站点实测命中。⭐⭐ **但当时那条情报缺一块：攻击者要的那些凭据是从哪来的？** ⭐⭐ **本条给出了一条已被证实的投递路径 —— 不是偷，是投毒**：**污染一个我们构建时必然安装的上游包，让恶意代码在我们自己的 CI 里、在每次 Python 启动时运行，然后把云身份令牌发走**。⭐ **这条链一旦闭上，"凭据收割"就不再是孤立的外部噪音，而是"我方 CI 是上游供应链的受害者"的直接后果** → **我方的暴露面定义必须从"对外站点"扩展到"构建与运行环境"**。
- ⭐⭐⭐ **`.pth` 机制是本条最该抄进我方认知的一点：装过 = 常驻，与是否使用无关。** ⭐⭐ **这直接击穿了一种常见的错误安全感** —— "我们项目里没 import agent-framework"。⭐⭐ **推论**：**凡我方任何 Python 环境（虚拟环境、容器、构建机、CI runner），都应把"site-packages 内是否存在 `.pth` 文件"列为一条常规体检项**，因为**这与装了哪个包无关**。⭐ **推论二**：**卸载不等于清理** —— `.pth` 是独立文件，卸载流程若不清理 site-packages，残留仍会生效（**此为机制推演，原文未直接给出"卸载后残留"结论**）。
- ⭐⭐⭐ **检测侧的落点比这次事件本身更持久：出口代理日志里"该 URL 返回 200"就是"数据已被接受"的判据。** ⭐⭐ 这条几乎零成本：只要我方有出口代理日志，就能回溯"我方是否曾把数据 POST 给一个公共请求检查服务"。⭐⭐ **更进一步**：`webhook[.]site` 这类"公共请求检查 / 粘贴板"服务本身就是一条**值得长期禁止出站的域名类别**（我方出口策略里大概率没有这一类）→ **建议把"公共请求回显类服务"整类列入出站黑名单，而不是只封这一个域名** —— ⭐ **这与库内 11-15 已记的"联网辅助设备"、11-19 已记的"出站 TLS 监测缺口"属同一类"出站面"治理课题**。
- ⭐⭐ **"被偷的不是密钥，是身份"是本条对我方风险评估最重要的升级。** ⭐⭐ **OIDC / 工作负载身份联合凭据（federated credential）意味着"不需要任何存储密钥就能换取云访问权"，且令牌有效期长达 24 小时** → ⭐⭐ **我方若用 CI 的 OIDC 换取云资源，则"轮换密钥"这个标准动作在这里是无效的**（密钥本来就没被偷，被偷的是信任关系）→ **必须能撤销"信任关系"本身**（删除 federated credential、收敛 managed identity 的资源授权范围）。⭐⭐ **这条与是否发生过这次投毒完全无关 → 属"同类失效模式对我方成立"，因此方向级可进评审；但第 1 关仍不过（无我方侧一手证据表明我方使用该信任模式）。**
- ⭐⭐ **攻击者的"IP 过滤绕过"细节，值得我方在自己的出站策略上照镜子。** ⭐⭐ **第一次从 AWS IP 发布被拦、第二次从"微软自有 IP 段"发布成功** → ⭐⭐ **任何以"来源 IP 归属 / ASN / 云厂商"作为准入依据的白名单，都可能被"合规出口"绕过** → **我方的 CI 出网白名单应按"目的域名 + 精确路径"约束，而不是按来源归属放行**。
- ⭐ **"AI 渗透框架（Cairn）端到端完成投递"是一条值得单独记的行为学信号。** ⭐ 库内 11-19 已记 Java4Shell 的"1 小时定位 / 2 小时写出利用代码"（发现—可利用成本基线）→ ⭐⭐ **本条把这条曲线继续往前推了一格：AI 辅助已从"发现并写利用"延伸到"打包、签名、投递、隐蔽"的全流程** → **对护网演练的直接含义是：上游包投毒应被当成一种常态攻击手法来演练，而不是偶发事故。**
- ⚠️ **四条判断不能下**：**不得写"我方已中招"**（库内无我方使用该包的一手证据）、**不得把外泄规模写成 50 例**（**确认仅 3 例**）、**不得因外泄只有 3 例就判断规模小**（**是外传通道免费额度所限，不是攻击者收手**）、**不得推测凭据取得方式或做归因**（官方明说未知），**也不得把 `durabletask` 事件与之合并**（官方明说未关联）。

---

## 六、参考意义

> 按本阶段五方向（网络安全 / 信创 / 等保 / 隐私保护 / 护网）判定：本条**属网络安全 + 护网方向**，且**性质上是"我方自己处于供应链受害位置"** —— 但**第 1 关（我方侧一手证据）不过**：库内无我方使用 agent-framework 的证据 → **只落方向级供应链基线与检测对照，不产专项整改**。

| 方向（网络安全/信创/等保/隐私保护/护网） | 可证事实 | 本阶段处理 |
|---|---|---|
| **网络安全**（方向级） | 上游包被投毒 → `.pth` 常驻 → 窃取 Azure / ADO / GitHub Actions 的云身份与 CI 令牌；**我方一手核验：1.26.1 / 1.26.2 已从 PyPI 发布历史消失（非 yank），当前 1.26.0**；出口代理的 200/410/429 判据；11 条 IOC | 🟡 **进评审（方向级）** —— 落"**构建与运行环境纳入暴露面**"基线（含 site-packages `.pth` 体检、lockfile 锁定、缓存清理）、"**出站禁止公共请求回显类服务**"规则方向、"**轮换须覆盖信任关系而非仅密钥**"；**不产专项整改**（第 1 关：无我方侧一手证据） |
| **护网**（方向级） | 上游包投毒作为一条可演练的攻击手法（AI 辅助端到端投递）；`webhook[.]site` 类外传通道 | 🟡 **进评审（方向级）** —— 并入既有"攻击手法→防线覆盖度对照"的**供应链投毒手法行**（不新开产物） |
| **等保 / 隐私保护 / 信创** | 本条无可证事实（未涉及等级保护测评项或个人信息处理规则） | ⚪ **不退回**（不涉及） |

**对我方产品与流程的关联（方向级 · 记录用）**

| 对象 | 影响点 | 是否需改行为 |
|---|---|---|
| 暴露面定义（扩展） | ⭐⭐ **在"对外站点"之外新增一类暴露面 —— "构建与运行环境"**（CI runner / 虚拟环境 / 容器镜像 / 开发机）：登记 Python 生态、依赖来源、是否有第三方 MCP / Agent 框架依赖；⭐ **本条提供了第一个可落地的体检项：site-packages 内是否存在 `.pth` 文件（与装了哪个包无关）** | 🟡 需改（基线扩展 · **建议开 issue**） |
| 依赖准入与锁定 | ① **生产依赖必须锁定到具体已验证版本**（本条建议 Pin 1.26.0，即"锁定 + 禁止未审计的自动升级"）；② **依赖须可追溯到上游维护方与发布签名**（本条根因是签名凭据被攻破 → 依赖"有签名"不等于"签名未被滥用"）；③ **新增"构建期自动升级依赖"禁令**（自动升级 = 自动化投毒投递路径） | 🟡 需改（准入标准） |
| CI / 构建机卫生 | ⭐⭐ **pip / CI 缓存清理与重建**（**pip 优先用本地缓存不回源 → 缓存不清等于没修**）；⭐ **容器层重建**（镜像层里可能仍有旧 wheel）；⭐ **"卸载即清理"复查**（`.pth` 独立文件，残留仍生效 —— 机制推演） | 🟡 需改（构建流程） |
| 身份与凭据管理 | ⭐⭐⭐ **"轮换密钥"必须升级为"轮换信任关系"**：托管身份授权范围收敛、federated credential（OIDC 联合凭据）可撤销、CI 的 `id-token: write` 使用范围收敛；⭐ **被窃令牌有效期可达 24 小时 → 需有"令牌新鲜度"概念（超过 N 小时的令牌不复用）**；⭐ **检测点：`_AF_TEL=1` 环境变量 + 两个 User-Agent** | 🟡 需改（身份管理 · **建议开 issue**） |
| 出站策略 | ⭐⭐ **把"公共请求回显 / 粘贴板类服务"整类列入出站黑名单**（不只封 `webhook[.]site` 一个域名）；⭐ **检测语义：出口代理日志中该类域名的 HTTP 200 = 数据已被接受，410/429 = 被拒绝** | 🟡 需改（出站策略） |
| 漏洞情报流程 | ⭐⭐ **"恶意版本从索引删除"（而非 yank）是一个新的情报形态** —— 上游"悄悄下架"不一定会通知下游；⭐ **我方取件（lockfile / 镜像基线）必须固定到已审计版本，而不是"取最新"** | 🟡 需改（流程） |
| 演练（护网） | ⭐⭐ **把"上游包投毒"作为一条常态攻击手法纳入演练**：演练要点 = 投毒 → CI 常驻 → 令牌外传 → 24 小时内横向使用 | 🟡 需改（演练场景） |

---

## 七、总结输出

**一句话结论**：**2026-11-17 20:35 UTC 起，恶意版本 `agent-framework` 1.26.1 与 21:08 的 1.26.2 被投放到 PyPI、约 21:30 双双下架（该包周下载量约 41,000，最新安全版本 1.26.0），攻击目标是 Azure / Azure DevOps / GitHub Actions 的云身份与 CI 令牌 —— 这是库内第一条"我方自己处于软件供应链受害位置"的情报，它把库内 11-16 已记的"外部凭据收割扫描器"缺掉的前半截补上了：攻击者不是偷凭据，而是污染一个我们构建时必然安装的上游包；⭐⭐⭐ **本条最该抄进我方认知的技术事实是 `.pth` 机制：装过 = 常驻，恶意代码在 site-packages 根目录的 `.pth` 文件里、Python 每次启动都执行，与是否 import 该包无关**（且 1.26.2 换了触发器 `af_runtime_diag.pth`/`af_runtime_diag.py`，**只查 1.26.1 的文件名会漏检**）；⭐⭐⭐ **我方同时拿到了一份真正的一手证据 —— PyPI 官方 JSON 接口的发布历史里 1.26.1 / 1.26.2 已彻底消失（是删除、不是 yank），当前版本仍为 1.26.0**，由此得三条可执行结论：**`pip install agent-framework==1.26.1` 现在直接失败 → "重装一遍"不是修复手段**；**pip / CI 缓存、容器层、私有 wheel 镜像里的旧包仍在且 pip 优先用本地缓存不回源 → 缓存不清等于没修**；**lockfile 里仍写着 1.26.1/1.26.2 的构建会直接失败（失败即暴露）**；⭐⭐ **规模口径必须按原文写：确认仅 3 例真实外泄**（50 个请求中 4 个来自攻击者自己、29 个是沙箱与厂商扫描），**但外泄少的原因是外传通道用了 webhook.site 免费额度（上限 100 请求 / 7 天过期），不是攻击者收手** → 因此**不得据此判断规模小**，而应把"公共请求回显类服务"整类列入出站黑名单、并用**出口代理日志里该 URL 返回 200 = 数据已被接受、410/429 = 被拒绝**这一判据回溯；⭐⭐ **对我方最深的风险升级不是"密钥被偷"而是"身份被偷"** —— OIDC / 工作负载身份联合凭据意味着**不需要任何存储密钥就能换取云访问权**，且**被窃令牌有效期可达 24 小时** → **"轮换密钥"这个标准动作在这里无效，必须能撤销信任关系本身**（收敛托管身份授权范围、撤销 federated credential、收敛 CI 的 `id-token: write`）；⭐⭐ **根因是上游 ESRP 发布签名凭据（客户端证书 + 私钥）被攻破**（"如何取得"官方明说未知 → 不得推测归因），且**攻击者第一次从 AWS IP 发布被拦、第二次从"微软自有 IP 段"发布成功 → 我方任何以"来源 IP 归属 / ASN"为准入依据的出站白名单都可能被合规出口绕过**；⭐⭐ **另有一条行为学信号值得单记**：攻击者使用开源 AI 渗透框架（Cairn）端到端完成打包与投递 → **AI 辅助攻击首次从"发现漏洞"延伸到供应链投递全链**，护网演练应把"上游包投毒"当作常态手法；⚠️ **五条边界必须带**：**库内无我方使用该包的一手证据 → 不得下"我方已中招"结论（转待核实）**、**不得把外泄规模写成 50 例**、**不得因 3 例就判断规模小**、**不得推测凭据取得方式或做归因**、**不得把 `durabletask` 事件与之合并**（官方明说未关联）。

**落地去向**

- [ ] **产品特性** —— ❌ **不勾**（本阶段口径：转评审只到方向级，不落产品功能改造）；⭐ **可记入方向级观察项**：构建与运行环境暴露面登记、site-packages `.pth` 体检项、出站公共回显类服务黑名单
- [ ] **需求变更** —— 🟡 **待复核**：① **暴露面定义新增"构建与运行环境"一类**（CI runner / 虚拟环境 / 容器镜像 / 开发机），并登记 Python 生态与依赖来源；② **依赖准入新增三条**：锁定到已审计版本（禁自动升级）、可追溯上游维护方与签名、恶意版本下架不作为版本可用的依据；③ **构建流程新增**：pip / CI 缓存清理与重建、容器层重建、卸载后 site-packages 复查；④ **身份与凭据管理新增"轮换信任关系"动作**（托管身份授权范围收敛、federated credential 可撤销、CI `id-token: write` 收敛、令牌新鲜度上限 ≤24 小时）；⑤ **出站策略新增"公共请求回显/粘贴板类服务"整类黑名单**，并以出口代理的 HTTP 状态码（200/410/429）作为"是否已被外传成功"的判据
- [ ] **专项整改** —— ❌ **不勾**（第 1 关不过：库内无我方使用 agent-framework 的一手证据、无我方侧暴露面数据；**不得下"我方已中招"结论**）
- [ ] **跟踪项** —— ⭐⭐ **建议开 issue（待核实）**：**"我方 Python 环境供应链面盘点与出站回显类服务封禁"** —— 背景为本次投毒（含 `.pth` 机制与 PyPI 一手版本事实）与库内 11-16 凭据收割线的关联；**选项至少两个**（A. 只做一次低成本的"site-packages `.pth` 体检 + lockfile 检索 + 出口代理日志回溯 `webhook[.]site` + 出站域名类别封禁"四项检查；B. 立即启动构建与运行环境的全量依赖签名验证与锁文件整改），**倾向 A**（四项检查成本极低、可当天完成，且"出口代理日志回溯"能直接回答"我方是否曾被外传"，这是本条最需要先回答的问题；全量签名验证成本高、应等盘点结论出来再定范围）；**影响面**为构建流水线、依赖准入规范、出口策略、身份与凭据管理、暴露面自查清单；**关联文档**本篇 + [credentialHarvestProbePaths-2026-11](credentialHarvestProbePaths-2026-11.md) + [remediation-exposureHygiene-20261112](../deliverables/remediation-exposureHygiene-20261112.md)
- [ ] **跟踪项** —— ① **"上游发布签名凭据被盗用"的通用防线**（我方依赖准入是否要求"发布签名 + 可回溯的上游发布流程"）；② **被窃托管身份/OIDC 令牌的 24 小时有效期** → 我方令牌使用是否需要"新鲜度"约束；③ **上游"悄悄下架"不等于通知下游** → 取件策略必须是"固定版本 + 审计留痕"而非"取最新"；④ **`webhook[.]site` 之外的同类公共回显服务清单**（可作为出站类别的补充）；⑤ **本次外泄仅 3 例中的 3 例身份是否已由 Wiz / Microsoft 披露**（若后续公开受害方名单，须回填我方是否在内）

---

## 参考链接

- [Wiz Research：Microsoft agent-framework Compromised — Credential Stealer Targets Azure and CI Pipelines（2026-11-17，11-18 14:00 UTC 更新根因与外泄数据）](https://wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi)
- [Chainguard Unchained：Microsoft agent-framework compromised on PyPI — 1.26.1 and 1.26.2 ship a credential stealer that runs on every Python start（2026-11-17，Quincy Castro / CISO）](https://www.chainguard.dev/fr-FR/unchained/microsoft-agent-framework-compromised-on-pypi-november-2026)
- [PyPI 官方 JSON 接口：agent-framework 发布历史（一手 · 当前 1.26.0、1.26.1/1.26.2 记录已消失）](https://pypi.org/pypi/agent-framework/json)
- [库内相关：外部凭据收割扫描器路径字典命中我方站点（本条为其"凭据来源"补全）](credentialHarvestProbePaths-2026-11.md)
- [库内相关：Java4Shell（"1 小时定位 / 2 小时写利用代码"基线 · AI 辅助攻击成本）](java4ShellCve2026114938-2026-11.md)
- [库内相关：CISA 五部门联合警告：联网辅助设备攻击面（出站面治理同类课题）](cisaRefrigerationColdChain-2026-11.md)
- [库内相关：对外站点暴露面专项自查（既有 P0 产物 · 本条扩展其"构建与运行环境"一类）](../deliverables/remediation-exposureHygiene-20261112.md)
- [库内相关：攻击手法→防线覆盖度对照（既有产物 · 本条并入"供应链投毒"手法行）](../deliverables/remediation-defenseTacticCoverage-20261112.md)

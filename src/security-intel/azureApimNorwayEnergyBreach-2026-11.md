# 挪威能源行业被 Azure API Management 密钥窃取事件击中 —— 库内首条「能源行业确认在野入侵」事件，且暴露出「平台侧补丁不撤销已被取走的凭据」

> 🔴 强约束 · 采集于 2026-11-25 · 核心标识：**⭐⭐⭐ 库内首条「能源行业确认在野入侵」事件 —— 挪威国家安全局 NSM 于 2026-11-20 发布通告，确认身份不明的行为者主动在 Azure API Management（APIM）中搜寻 access tokens、secrets 与 named values，Equinor（欧洲最大油气供应商）与水电商 Skagerak Energi 均在受害名单上** · ⭐⭐⭐ **漏洞本身由挪威能源行业首先发现（NSM 官方表彰 Equinor「早期发现 + 快速共享」）** → **这是一次由能源行业替全世界踩雷、并且能源行业自己先发现的事件** · ⭐⭐⭐ **本条把库内 11-20「被偷的是身份不是密钥」从个案 + 原则推进到「平台侧修好也不作数」的第三层**：**微软 11-19 关闭了访问路径，但修复「不会自动作废此前可能被访问过的客户凭据」→ 密钥必须由客户逐个轮换，而轮换动作本身可能在泄露发生后数天才发生** · ⭐⭐ **库内首条「漏洞不在客户系统里、但密钥在客户系统里」的定性结构** → 我方的 DER 接入凭证、场站 API 密钥、聚合平台下游凭据若托管在同类托管网关中，暴露面等同于本条 · ⭐⭐⭐ **NSM 给出的自查判据极其可执行且可迁移**：`https://<网关主机>/internal-status-0123456789abcdef` 读 RuntimeVersion → 0.52.x 末位 ≥ 31936、0.53.x 末位 ≥ 31938 才算已修；其余形态（0.53.4608.0 / 0.52.4150.0）是 v2 或 Consumption 层、不适用该阈值、也不受影响 · ⭐⭐ **库内首条「国家机构公开发布的凭据轮换清单 + 版本号阈值」组合** · ⚠️ **无 CVE、无 CVSS、无受害客户数、无攻击者归属**；**Equinor 与 Skagerak 自己的公告都没有提 APIM —— 这条因果链完全由 NSM 单方给出**；⚠️ **NSM 原文自己纠正了一处误述**：曾写「漏洞首先由挪威电力（kraft）部门发现」，11-23 更新时改为「能源（energi）部门」；⚠️ **微软未公开承认挪威入侵与该漏洞之间的因果关系，也未点名攻击者** → **不得写成"俄罗斯/伊朗/某组织所为"，不得写成"数据已被窃取"**

---

## 一、信源核实

| 项 | 值 |
|---|---|
| 来源请求 | `Azure API Management flaw Equinor Skagerak Energi Norway NSM secrets compromised November 2026`（web_search）<br>`NSM Norway advisory Azure API Management vulnerability nsm.no security advisory November 2026`（web_search，用于定位 NSM 官方页原文 URL） |
| 原始 URL（主 · 国家机构官方通告） | https://www.nsm.no/aktuelt/nsm-deler-tiltak-mot-sarbarhet-i-azure-api-management/ （NSM = Nasjonal sikkerhetsmyndighet，挪威国家安全局《NSM deler tiltak mot sårbarhet i Azure API Management》，**Published: 20.11.2026 · Oppdatert: 23.11.2026**，快照正文 5,750 字符） |
| 原始 URL（辅 1 · 第三方英文深度分析） | https://secnews.co.uk/2026/11/follow-up-equinor-azure-api-management-flaw-nsm-rotate-secrets （SECNEWS《Follow-up: Equinor attack linked to Azure API Management flaw》，**2026-11-23**，快照正文 8,530 字符） |
| 原始 URL（辅 2 · 第三方事件复盘） | https://threatticker.com/news/norway-warns-an-azure-api-management-flaw-was-exploited-against-equinor （ThreatTicker《Norway warns an Azure API Management flaw was exploited against Equinor, Skagerak Energi and other firms》，**2026-11-23**，快照正文 5,543 字符） |
| 发布主体 | **NSM（挪威国家安全局，事件定性方）** · 微软（漏洞处置方，仅经第三方转述其非公开客户通告，Azure Service Health 追踪号 **MZK9-GH0**） · Equinor ASA / Skagerak Energi（受害方，各自独立公告） |
| 发布/更新时间 | NSM 通告：**发布 2026-11-20 16:25 CET、更新 2026-11-23 09:30 CET**；微软：**11-18 发现问题 → 11-19 关闭访问路径 → 11-21 发布凭据轮换指南（Azure Integration Services 博客，作者署名 vladvino）**；Equinor：**11-17 18:55 CET 发现 → 11-20 报告已止住**；Skagerak Energi：**11-18 披露** |
| 采集时间 | 2026-11-25 07:34:10 – 07:34:15 |
| 快照 | `raw/snapshots/security/nsm-apim-advisory.md` · `secnews-equinor-apim-nsm.md` · `threatticker-norway-apim-equinor.md` |

**快照清单**（SHA256 取自 `.meta.json` 的 `sha256_raw`）

| 快照 | SHA256 | 抓取时间 | 正文字符 | HTTP |
|---|---|---|---|---|
| `raw/snapshots/security/nsm-apim-advisory.md` | `6618e929476736b25bcb0dacb14cbc8c80cd525e64cedb13f730c67b7f4e4fc1` | 2026-11-25 07:34:15 | 5,750 | 200 |
| `raw/snapshots/security/secnews-equinor-apim-nsm.md` | `c9c79974a7db3671126530e9ccb4c7d48d288040ecbdd2491867e72318130436` | 2026-11-25 07:34:10 | 8,530 | 200 |
| `raw/snapshots/security/threatticker-norway-apim-equinor.md` | `f6584fc521ad3b02178f3df1601091fd30514fbdc33224343de6610c3c7e5dd5` | 2026-11-25 07:34:11 | 5,543 | 200 |

> 📎 **入库理由**：库内已有 30+ 篇安全文档，覆盖了 WAF 观测到的攻击类型、CISA ICS 通告、KEV 批次、软件供应链投毒、暴露面实证等，但**从未有过一条「能源行业确认自己被入侵」的确认事件**。库内此前所有安全情报的落点都是「漏洞可能影响我方」或「攻击者正在打我们的某个接口」；**本条是第一条由国家级机构背书、受害方为能源企业、且成因是「密钥被托管平台泄露」的真实入侵事件**。它对我方的价值不在于产品相同（我方不用 APIM），**而在于它把「凭据托管在别人家的网关里」这条风险第一次落到了能源行业的真实事件上**。
> ✅ **双信源要求已满足**：官方源（NSM 官方通告快照，含版本阈值与处置要求的挪威语原文逐字）+ 第三方源（SECNEWS 与 ThreatTicker 两篇独立英文分析，含 Equinor/Skagerak 各自时间线、微软通告的第三方转述与研究者 Kristiansen 的凭据杀伤力论断）。

---

## 二、事实核查

| 数据点 | 原文表述 | 核查方式 | 结论 | 备注 |
|---|---|---|---|---|
| 1 | **⭐⭐⭐ 攻击目标清单** | NSM 快照逐字：*"En ukjent aktør har aktivt gått etter **access tokens, secrets og named values i APIM**."*（一个身份不明的行为者主动在 APIM 中搜寻访问令牌、密钥与命名值）；同句中文转述见 SECNEWS 快照：*"an unknown actor actively went after three kinds of material held in APIM: access tokens, secrets and named values"* | 三源比对（NSM 原文 + SECNEWS + ThreatTicker 英文转述） | ✅ **已核（三源一致）** | ⭐⭐⭐ **这条是本事件最值钱的一句**：**它不是盲扫，而是有明确检索清单的定向搜密** → 攻击者知道去哪个抽屉翻。⭐⭐ **三类目标全是"能打开别的东西"的材料**，而不是业务数据本身 |
| 2 | **⭐⭐⭐ 处置要求（唯一无条件动作）** | NSM 快照逐字：*"Alle som har Azure API Manager må ta utgangspunkt i at deres secrets og named values er på avveie. Dette innebærer at virksomheten må **rullere alle tokens og secrets**."*（所有使用 APIM 的组织必须假定其 secrets 与 named values 已外泄 → 必须轮换全部 tokens 与 secrets） | NSM 快照逐字 + SECNEWS 快照英文一致（*"assume your secrets are gone and rotate them"*） | ✅ **已核** | ⭐⭐⭐ **NSM 的措辞是「假定已外泄」而不是「已确认外泄」** → **这是一个基于可能性而非证据的保守判定**，我方引用时必须保持这个强度，不得升级成"已确认泄露" |
| 3 | **⭐⭐⭐ 微软的修复「不作废凭据」** | 微软 Azure Service Health 通告 MZK9-GH0（据 BleepingComputer / SecurityWeek / The Record 转述，**非公开客户通告，我方未取得原文**）：修复 *"does not automatically invalidate credentials that may have been accessed before the fix was deployed"*；微软 *"rotated Microsoft-controlled keys and credentials where appropriate"* | 三家第三方转述互相印证 + 与 SECNEWS "Expert view" 的总结一致：*"Patching closes the door. It does nothing about keys that walked out before it closed."* | ✅ **已核（第三方多源一致，**⚠️ **微软原文未取得**） | ⭐⭐⭐ **本条是全事件的技术要害** → **库内 11-20 的 agent-framework（偷的是身份不是密钥）、11-24 的 vCenter（补丁不撤销已被取走的 SAML 签名材料）、本条的 APIM（平台补丁不撤销已被取走的客户凭据）构成同一原则的第三个独立样本，且本条是唯一一个「漏洞根本不在客户系统里」的样本** → **判据从「我方系统是否装了受影响组件」升级为「我方密钥是否托管在受影响的平台上」** |
| 4 | **⭐⭐⭐ 自我检查判据（可执行）** | NSM 快照逐字：*"Åpne `https://<your-gateway-hostname>/internal-status-0123456789abcdef` og les av RuntimeVersion"*；*"**0.52.x: patchet dersom siste nummer (x) er 31936 eller høyere**"*；*"**0.53.x: patchet dersom siste nummer (x) er 31938 eller høyere**"*；*"Andre mønstre (for eksempel 0.53.4608.0 eller 0.52.4150.0): V2 eller Consumption tier hvor denne terskelen ikke gjelder, **er ikke sårbar**"*；*"Lavere nummere, forstatt sårbar"*；*"Dersom virksomhetens instans ikke er blitt oppdatert, ber NSM virksomheten **kontakte leverandøren direkte**"* | NSM 快照逐字 + SECNEWS + ThreatTicker + securecybervm 四源交叉 | ✅ **已核（四源一致，含端点路径与两个具体示例版本号）** | ⭐⭐⭐ **这条可直接落成我方一条台账动作**：「有没有我们放在托管平台上的长期凭据」—— 库内 11-20 已经有一条同源判断：**出站代理日志里某 URL 返回 200 = 数据已被接受**；本条给出的是**平台侧的对应判据**。⭐⭐ **NSM 要求「实例未更新就联系供应商」→ 说明这不是"打了补丁就没事"，而是要逐实例确认** → **对应我方动作：凭据台账要记「托管位置 + 平台侧版本/状态」，而不只是记密钥本身** |
| 5 | **⭐⭐⭐ 受害方与发现方** | NSM 快照逐字：*"**Equinor og Skagerak Energi er blant virksomhetene som har blitt rammet. Sårbarheten ble først oppdaget av den norske energisektoren**, som jobber godt med forebyggende sikkerhet."*；同页引用 NSM 运行网络安全部门负责人 Martin Albert-Hoff：*"NSM ønsker å berømme Equinor for godt arbeid som førte til tidlig oppdagelse samt rask deling med NSM og de sektorvise responsmiljøene."* | NSM 快照逐字 + SECNEWS / ThreatTicker 英文一致 | ✅ **已核** | ⭐⭐⭐ **库内首条「能源行业替所有人先踩雷、并且自己先发现」** → **这个事实本身就是对我方最有价值的一条**：**能源行业的安全实践水平足以做到先于厂商发现问题并快速共享** → **我方（做光伏 DER 接入与聚合的平台方）在同类暴露面上的角色是"被保护方"还是"应当成为发现方"，是一个值得确立的定位问题**。⚠️ **NSM 表彰的是 Equinor 的发现与共享行为，不等于表彰其安全水平** |
| 6 | **⭐⭐ NSM 原文的一处自我纠错** | NSM 快照页末逐字：*"Artikkelen er oppdatert 23. november. Det stod ved en feiltakelse at «**sårbarheten ble først oppdaget av den norske kraftsektoren**». Dette er rettet til **energisektoren**."*（原文误写"电力部门"，已更正为"能源部门"） | NSM 快照逐字 | ✅ **已核** | ⭐⭐ **这条本身不值得单独入库，但它是一手原文自我纠错的样本** → 说明**官方通告也会把"发现方"的部门范围写错**，我方引用二手转述时**必须回到原文核对主体范围**。⚠️ **库内 11-13 已记 EPICS 条目时也发生过一次主体范围误标**（把"官方点名能源行业"写成关键制造）→ **同类错误在本库已重复出现两次，值得作为"引用纪律"记录下来** |
| 7 | **Equinor 时间线与自述** | Equinor 公告（经 SECNEWS / ThreatTicker 转述）：**11-17 18:55 CET 发现**；11-18 称"不是病毒攻击、无扩散风险"；11-19 称"**攻击并非专门针对 Equinor**"；**11-20 称攻击已止住、生产运行正常、无迹象表明数据被窃取或篡改、无迹象表明员工/伙伴/供应商受影响、已报警** | ThreatTicker 快照逐字 + SECNEWS 快照逐字 | ✅ **已核（两家第三方独立转述一致）** | ⭐⭐ **"并非专门针对 Equinor"这一句极关键** → 与 NSM「定向搜寻密钥」的定性吻合，**是一次机会主义的批量搜密，不是针对单一企业的定制攻击**。⚠️ **Equinor 的公告通篇未提 Azure 或 APIM** → **因果链完全由 NSM 单方给出**（见第 8 条） |
| 8 | **⭐⭐⭐ 因果链的归属（必须写明的冲突）** | Equinor 与 Skagerak **各自公告都没有提到 APIM**；链接二者的是 NSM 的通告。SECNEWS 快照逐字：*"**The link to APIM comes from NSM.** We could not find a CVE identifier or a Microsoft security advisory describing the flaw, and neither company has publicly described the attack in those terms."*；ThreatTicker 快照逐字：*"Neither NSM, Microsoft, Equinor, Skagerak nor The Record has shared a CVE identifier, exploit chain or attacker group for this campaign."*；vicytech 转述亦称 *"the link to the energy-sector incidents ... is not established"* | 三源交叉，逐字核对 | ✅ **已核（冲突已写明）** | ⭐⭐⭐ **本条必须显式写入冲突**：**① 受害方自述未提 APIM、因果链由 NSM 单方给出**；**② 微软未公开确认挪威入侵与该漏洞的因果关系**（微软唯一的公开动作是 11-21 一篇不提及挪威、不提及漏洞的凭据轮换指南）；**③ 无 CVE、无 CVSS、无受影响客户数量**。⚠️ **因此正确表述是「NSM 判定这次入侵经由 APIM 漏洞实施」，而不是「Equinor 因 APIM 漏洞被入侵已被证实」** |
| 9 | **受影响层级边界** | 微软通告（第三方转述）：APIM Classic 的 **Developer / Basic / Standard / Premium** 四层受影响；**Consumption 层与全部 v2 层不受影响**；NSM 亦称 V2 / Consumption 不受该阈值影响 | BleepingComputer / The Record 转述 + NSM 版本形态说明 + defend.network 汇总，三源一致 | ✅ **已核（第三方多源一致，**⚠️ **微软原文未取得**） | ⭐⭐ **"按层级精确划界"是本事件最好的技术细节** → 说明**"我们用了微软的云"这句话本身不足以判断暴露面，必须精确到层级** → 迁移到我方：**凭据台账要记托管位置到"平台 + 层/实例规格"粒度**，否则无法回答"我们受不受影响" |
| 10 | **可能被访问的凭据清单** | 微软通告（第三方转述）：Named Values 中的 secrets、身份提供方 client secrets、OIDC client secrets、subscription keys、直接管理 API 令牌；SECNEWS 另提后端凭据与证书、连接串、策略中内嵌的凭据 | 多源一致 | ✅ **已核（第三方多源一致）** | ⭐⭐⭐ **这四类材料有一个共同点：它们不是"我方业务系统的账号密码"，而是"我方业务系统所用的下游服务的账号密码"** → **攻击者拿到后可以绕过网关直连下游**（Kristiansen 原话：*"they may be able to use it directly against the service it protects, outside APIM"*）→ **这正是库内 11-17/11-18 记录的我方 `/preview/getCorsFile` Base64 URL 参数面所对应的攻击者能力**：如果我方某接口允许凭据驱动任意 URL 请求，那它就是这条链路的"后端直连"那一端 |
| 11 | **凭据轮换的正确顺序** | 微软 11-21 指南（经 DEV Community 转述）：*"create the replacement where the credential is issued, update API Management, test your APIs, then revoke the old secret"*；并指出 *"Updating the value in APIM alone does not revoke the old credential at its issuer, so a key copied out last week still works this week until the issuer kills it."* | 第三方转述 | ⚠️ **单源转述（微软原文未取得）** | ⭐⭐⭐ **这句是全事件对我方最可执行的一句** → **只改平台侧的值不等于吊销旧凭据；必须回到签发方吊销** → **这是一条可以立刻变成我方凭据轮换 SOP 校验规则的硬结论**，且与库内 11-20「被偷的是身份不是密钥 → 轮换密钥无效、必须能撤销信任关系」完全同向 |
| 12 | **检测面在哪里** | SECNEWS 快照 "Expert view"：*"the logs that matter are probably not the gateway's. If an attacker lifted a back-end credential, they will use it against the back end directly, from infrastructure you do not recognise. **Hunting needs to happen at the destination services.**"*；另指出网关是长期密钥最常见的藏身处：*"Non-expiring back-end keys, shared partner subscription keys and plaintext connection strings in named values are routine findings."*；并指出 *"**Shadow instances are where unrotated secrets survive.**"* | SECNEWS 快照逐字 | ✅ **已核（第三方分析，标注为第三方观点）** | ⭐⭐⭐ **这条直接改变我方的排查方向**：**不去查网关的访问日志，而去查下游服务的登录/调用日志** → 迁移到我方：**若我方平台被索取过密钥，排查对象是我方各场站/下游系统的登录日志，不是我方自己的网关日志**。⭐⭐ **"影子实例"（测试/开发/供应商代运维的实例）是最可能残留未轮换密钥的地方** → 我方台账必须包含"非生产实例"这一类，**这是当前库内所有资产台账条目都缺的一维** |
| 13 | 影响范围与后果 | NSM：*"Det er fortsatt usikkert hvor omfattende utnyttelsen av sårbarheten er, og har vænt."*（利用范围至今仍不确定）；*"NSM har så langt ingen holdepunkter for at kompromittering eller forsøk på kompromittering har fått konsekvenser for leveranser hos norske virksomheter."*；NSM 称漏洞 *"treffer flere sektorer i Norge og også utenfor Norges grenser"*；挪威国家级网络风险等级为 **HØYT（高）** | NSM 快照逐字 + SECNEWS + ThreatTicker | ✅ **已核** | ⭐⭐ **「无迹象造成交付后果」与「利用范围不确定」必须同时写出** → **不得写成"数据泄露事件"，也不得写成"未造成影响的事件"**。⭐⭐ **国家级风险等级为「高」是独立于本事件的一般性判断**，不得归因于本事件 |
| 14 | 攻击者归属 | NSM：*"En ukjent aktør"*（身份不明的行为者）；微软未点名；无组织名、无国家归属 | 三源一致 | ✅ **已核（结论是"未知"）** | ⚠️ **必须明确写「未知」**。库内 11-25 已记 MONAI Label 为"中国关联组织、中等置信度"，库内 11-24 记 Expressway 为 F6 报告的"俄罗斯某组织"—— **三条情报的归属强度各不相同，本条是三者中最弱的（完全未知），不得与它们并列表述** |
| 15 | 攻击开始时间 | **无任何来源给出利用开始时间**。可确定的只有：Equinor 11-17 发现、微软 11-18 识别、11-19 关闭访问路径 | 三源交叉 + pk-sharma 逐条比对（明确列出"未说明项"） | ✅ **已核为「不可知」** | ⚠️ **不得倒推"攻击自 11-18 才开始"** → 微软 11-18 才识别 ≠ 11-18 才开始。pk-sharma 快照亦明确："When exploitation began ... is on no saved page" |

**核查小结**：**本条无来源级数字冲突**（NSM 原文与三家第三方转述在攻击目标、处置要求、版本阈值、受害方、时间线上完全一致），**但存在 1 处必须写明的证据强度冲突**：受害方自述与官方定性之间存在归因落差（见第 8 条），以及 **1 处官方原文自我纠错**（见第 6 条）。另有 **4 项硬边界**：无 CVE、无 CVSS、无受害客户数、无攻击者归属。

---

## 三、原文归档（快照）

- 快照文件：`raw/snapshots/security/nsm-apim-advisory.md`（官方）、`raw/snapshots/security/secnews-equinor-apim-nsm.md`、`raw/snapshots/security/threatticker-norway-apim-equinor.md`
- SHA256：`6618e929476736b25bcb0dacb14cbc8c80cd525e64cedb13f730c67b7f4e4fc1`（NSM 官方）/ `c9c79974a7db3671126530e9ccb4c7d48d288040ecbdd2491867e72318130436`（SECNEWS）/ `f6584fc521ad3b02178f3df1601091fd30514fbdc33224343de6610c3c7e5dd5`（ThreatTicker）
- 抓取时间：2026-11-25 07:34:10 – 07:34:15 · HTTP 200 · 正文 5,750 / 8,530 / 5,543 字符

**关键原文摘录（NSM 官方通告，挪威语原文逐字）**：

> *"Tidligere i uken ble NSM kjent med en sårbarhet i Azure API Management (APIM) som rammer flere norske virksomheter. Nå skal sårbarheten være lukket. **NSM ber likevel virksomheter gjøre tiltak.**"*
> （本周初 NSM 获悉 Azure API Management（APIM）存在一处影响多家挪威机构的漏洞。现在漏洞应当已被关闭。**但 NSM 仍要求各机构采取行动。**）
>
> *"**Tiltak Sårbarhet: En ukjent aktør har aktivt gått etter access tokens, secrets og named values i APIM.** Alle som har Azure API Manager må ta utgangspunkt i at deres secrets og named values er på avveie. Dette innebærer at virksomheten må **rullere alle tokens og secrets**."*
> *"Det er også viktig at virksomheter **kartlegger hvilken informasjon som ligger bak APIM instansen sin** for å avdekke det potensielle omfanget."*
> *"**Åpne `https://<your-gateway-hostname>/internal-status-0123456789abcdef` og les av RuntimeVersion**"*
> *"**0.52.x: patchet dersom siste nummer (x) er 31936 eller høyere**"* / *"**0.53.x: patchet dersom siste nummer (x) er 31938 eller høyere**"* / *"Andre mønstre (for eksempel 0.53.4608.0 eller 0.52.4150.0): V2 eller Consumption tier hvor denne terskelen ikke gjelder, er ikke sårbar"* / *"Lavere nummere, forstatt sårbar"*
> *"**Equinor og Skagerak Energi er blant virksomhetene som har blitt rammet. Sårbarheten ble først oppdaget av den norske energisektoren**, som jobber godt med forebyggende sikkerhet."*
> *"**Høyt risikonivå** … Når en sårbarhet blir kjent, vil flere aktører kunne forsøke å utnytte den. **Rask eskalering i bruk av kunstig intelligens (KI) påvirker situasjonen.**"*
> *"Artikkelen er oppdatert 23. november. Det stod ved en feiltakelse at «sårbarheten ble først oppdaget av den norske kraftsektoren». Dette er rettet til energisektoren."*

**关键原文摘录（SECNEWS，2026-11-23，"Expert view" 段）**：

> *"This is the pattern I expect to see more often: **the vulnerability is in a platform the customer cannot patch, the provider fixes it quietly, and the customer is left holding credentials that may already be in someone else's hands. Patching closes the door. It does nothing about keys that walked out before it closed.**"*
> *"The detail I would stress to SOC teams is that **the logs that matter are probably not the gateway's**. If an attacker lifted a back-end credential, they will use it against the back end directly, from infrastructure you do not recognise. **Hunting needs to happen at the destination services.**"*
> *"**Shadow instances are where unrotated secrets survive.**"*

**关键原文摘录（ThreatTicker，2026-11-23）**：

> *"Equinor detected the attack on November 17 and said it was fully stopped by November 20, 2026, with production unaffected; **Equinor says the attack 'was not specifically targeting' the company**, which matches NSM's framing of an opportunistic hunt for APIM tokens and secrets."*
> *"**Neither NSM, Microsoft, Equinor, Skagerak nor The Record has shared a CVE identifier, exploit chain or attacker group for this campaign.**"*

---

## 四、概要提取

- ⭐⭐⭐ **库内首条「能源行业确认在野入侵」事件**：NSM 于 11-20 公布，确认身份不明行为者在 Azure API Management 中主动搜寻 **access tokens / secrets / named values**，**Equinor 与 Skagerak Energi 均在受害名单**；挪威国家级网络风险等级为「高」。
- ⭐⭐⭐ **漏洞由挪威能源行业首先发现并被 NSM 公开表彰**（早期发现 + 快速共享）→ **库内第一条「能源行业替全世界先踩雷」的样本**。
- ⭐⭐⭐ **最硬的技术结论：微软 11-19 关闭了访问路径，但修复「不会自动作废此前可能被访问过的客户凭据」** → 密钥必须由客户逐个轮换 → **这是库内「被偷的是身份不是密钥」原则的第三个独立样本，也是唯一一个「漏洞根本不在客户系统里」的样本**。
- ⭐⭐ **NSM 给出了可执行且可迁移的自我检查判据**：读 `/internal-status-0123456789abcdef` 的 RuntimeVersion，**0.52.x 末位 ≥ 31936、0.53.x 末位 ≥ 31938** 才算已修；其余形态属 v2/Consumption 层、不受影响；**未更新须联系供应商**。
- ⭐⭐ **微软的轮换顺序可落成 SOP 规则**：**须回到签发方吊销旧凭据**（在签发处换新 → 更新平台 → 测试 → 再吊销旧值），**只改平台侧的值不算吊销**。
- ⭐⭐ **检测方向被明确指出不在网关侧而在下游侧**：凭据被盗后会**绕过网关直连后端**，因此**排查对象是下游服务的登录与调用日志**；**「影子实例」（测试/开发/供应商代运维）是未轮换密钥最可能存活的地方**。
- ⭐⭐ **受影响层级被精确划界**：APIM Classic 的 Developer/Basic/Standard/Premium 四层受影响，**Consumption 层与全部 v2 层不受影响** → **「我们用了微软云」不足以判断暴露面，必须精确到层级**。
- ⚠️ **四条硬边界**：**无 CVE / 无 CVSS / 无受害客户数 / 无攻击者归属**；**受害方公告未提 APIM，因果链由 NSM 单方给出**；**微软未公开承认因果关系**；**利用开始时间不可知**。

---

## 五、主要观点

**原文主张**

- **NSM（官方定性）**：本周初 NSM 获悉 APIM 存在一处影响多家挪威机构的漏洞，现应已关闭，但**仍要求各机构采取行动**；身份不明的行为者主动在 APIM 中搜寻 access tokens、secrets 与 named values；**所有使用 APIM 的组织必须假定其 secrets 与 named values 已外泄，必须轮换全部 tokens 与 secrets**；还必须**梳理各实例背后承载什么信息**以判断潜在影响范围；应检查实例是否已更新（读 RuntimeVersion，按 0.52.x≥31936 / 0.53.x≥31938 判定），未更新者应**直接联系供应商**，发现或确认入侵迹象者应联系 NSM；漏洞影响挪威多个行业并波及境外；Equinor 与 Skagerak Energi 在受害名单内，**漏洞首先由挪威能源部门发现**；NSM 表彰 Equinor 的早期发现与快速共享；**挪威国家级网络风险等级为「高」**；**AI 的快速升级正在影响这一态势**。
- **SECNEWS（第三方分析）**：预期这种模式会越来越常见——**漏洞在客户无法打补丁的平台上，厂商悄悄修好，客户手里却仍握着可能已被别人拿走的凭据；打补丁只是关上门，对此前已经走出去的密钥毫无作用**；**重要的日志很可能不在网关上**，被盗的后端凭据会被直接用于后端、来源是陌生的基础设施，**必须在目的地服务上做狩猎**；API 网关是长期密钥最常见的藏身处（后端长有效密钥、共享的伙伴订阅密钥、命名值里的明文连接串），轮换之所以痛苦是因为没人梳理过哪个系统依赖哪个密钥；**影子实例是未轮换密钥的存活地**。
- **ThreatTicker（第三方复盘）**：Equinor 于 11-17 发现、11-20 已止住，生产未受影响；Equinor 称**攻击并非专门针对该公司**，与 NSM「机会主义搜密」的定性吻合；微软未公开承认真实攻击链、也未点名攻击者；微软 11-18 发现、11-19 关闭访问路径。

**我方判断**

- ⭐⭐⭐ **这条情报真正的价值不在漏洞本身，而在于它把库内的「暴露面」定义从「设备」扩到了「凭据托管位置」，而且是能源行业用真实入侵替我们做了验证。** 库内从 11-16 到 11-24 已经反复确立了同一个判据的不同侧面：**暴露面 ≠ 装了什么东西，而是「能不能被够到」**（11-16 DER 暴露面、11-19 EPICS 协议栈无认证、11-24 KEV 批次的「联网可达优先于 KEV 收录」）。⭐⭐⭐ **本条补上的是最容易被漏掉的那一维：漏洞在别家平台上，我方一行代码都没写，但密钥是从那个平台上被取走的。** → **我方台账必须新增一个字段维度：长期凭据的「托管位置 + 平台 + 实例/层级规格」**，**只记「有哪些密钥」是不够的**，因为本事件的全部要害就在"托管在哪一格"。
- ⭐⭐⭐ **「修复不撤销已取走的东西」这条，库内已经积累了三个独立样本，现在可以升级成一条硬规则了：**
  | 样本 | 被取走的东西 | 补丁为什么不作数 |
  |---|---|---|
  | agent-framework（11-20） | Azure/ADO OIDC 令牌与托管身份令牌 | 令牌有效期长达 24 小时，轮换密钥无效 |
  | vCenter（11-24） | SAML STS 签名私钥 | 补丁不撤销已被取走的签名材料，伪造令牌仍可绕 MFA |
  | **APIM（本条）** | **客户托管在平台上的订阅密钥与后端凭据** | **平台修好访问路径，但旧凭据仍然有效直到客户去吊销** |
  ⭐⭐⭐ **三个样本的共同结构是「时间差」**：**从密钥被取走到密钥被吊销之间存在一个完全不可控的窗口，而这个窗口的长度取决于客户的轮换速度，不是取决于厂商的补丁速度。** → **我方护网/等保方向的覆盖度对照产物（`remediation-defenseTacticCoverage-20261112`）应当把「凭据吊销时效」列为一条独立度量项**：不是「有没有补丁」「有没有轮换」，而是**「从怀疑泄露到完成吊销用了多久」**。⭐⭐ **这条度量项我方今天就能测**：库内 11-20 已经给过我方出口代理日志里 200/410/429 的判据（"数据是否已被接受"），把那个时间点与凭据吊销时间做差，就是这个度量项的第一个实例。
- ⭐⭐⭐ **「微软给了版本号阈值，却没给 CVE；受害方没提平台，因果链全靠监管机构单方给出」——这条证据结构本身是我方引用的反面教材，库内必须把它作为纪律条目固化。** 对比库内 11-25 已记的 MONAI Label（Amazon 明确归因、中等置信度、受害场景为高校网络）与 11-24 的 Expressway（F6 报告俄罗斯某组织利用公开 PoC）：**本条的归因强度是三者中最弱的（完全未知）**。⭐⭐ **正确写法：「NSM 判定这次入侵经由 APIM 漏洞实施」；错误写法：「Equinor 因 Azure 漏洞被入侵已被证实」「某国组织窃取了挪威能源公司的密钥」。** ⭐⭐ **另一个可迁移的观察**：**NSM 官方页面自己把「发现方」写错成"电力部门"、隔天更正为"能源部门"** —— 说明**连出具定性的官方通告，其主体范围表述也会有偏差**，**我方引用任何二手转述时都必须回到原文核对主体范围**（库内 11-13 的 EPICS 条目已经栽过一次同样的坑）。
- ⭐⭐⭐ **「排查对象不在网关侧，而在下游侧」这一条，是我方现有 WAF 工作流的一个明确盲点补全。** 我方 WAF 观测的是**打向我方站点的东西**；但如果我方的某个密钥被第三方平台泄露，**攻击者会拿着它直接打我方的下游系统**（场站网关、逆变器监控平台、聚合平台后端），**而这些请求不会经过我方 WAF**。⭐⭐ → **对我方的具体含义：WAF 巡检报告里"零新增拉黑"这类结论，其覆盖面只到"经过 WAF 的流量"；本条说明存在一个"WAF 看不见的攻击面"**。⭐⭐ **这条可以直接接到库内 11-24 日报里那条 WAF 待办上**：**WAF 类型分布变化那条之所以"仅一期读数不可评"，根源就是覆盖面本身有边界** —— **先把"我方凭据的签发方与使用方在哪里"画清楚，才谈得上判断攻击面是否变化**。
- ⭐⭐ **「影子实例」这个概念值得直接搬进我方资产台账。** SECNEWS 指出未轮换密钥最容易存活的地方是**测试、开发、以及由供应商/MSP 代运维的实例**；库内 11-19 已记「本阶段产物责任人待指派」与 11-16 已记的「外部凭据收割扫描器」—— **我方若要自查"密钥是否被托管在外部平台"，第一件事就是问自己：我们有没有在客户或供应商侧留过测试环境的常驻凭据？** ⭐⭐ **这个问题在库内所有既有文档中都没有被提出过 → 是一条真正的新动作，而不是既有动作的复述**。⭐⭐ **并且它成本极低：只需要把"非生产实例"列成台账的一类。**
- ⭐⭐ **「Equinor 说自己不是被专门针对的」+「NSM 说这是定向搜密」两句合起来，构成一条对护网演练很有用的推论：攻击者的目标是"凭证库"而不是"某一家"。** ⭐⭐ **这意味着防护的着力点应该是"减少可被批量获取的凭据面"（短生命周期、集中签发、不可横向复用），而不是"防住某条攻击路径"** → 这与库内 11-25 已记 KEV 批次里 Idunno AntiCsrf「处置动作是移除而非修补」是同一类思路：**降低存量比追捕路径更有效**。
- ⭐⭐ **必须保持的边界**：① **不得下"我方受影响"结论**（库内无我方使用 Azure APIM 的一手证据，亦无我方密钥托管位置清单）；② **不得写成"数据泄露事件"**（Equinor/Skagerak 均称无迹象表明数据被窃取或篡改）；③ **不得写成"攻击由某国组织实施"**（归属完全未知）；④ **不得把 NSM 的"假定已外泄"升级成"已确认外泄"**；⑤ **不得据此判断"微软已修复所以安全了"**；⑥ **不得把微软的版本阈值当作适用于其他平台的通用判据**（它是 APIM 专有的）；⑦ **不得把"11-18 微软发现"当成"11-18 才开始攻击"**。
- ⭐ **优先级判断**：本条**不应**被排进"立即修补"队列（我方不用该产品，无我方暴露面证据），**但应**被排进"方法论与台账"队列 —— 它提供的是**判据与动作**，不是补丁。

---

## 六、参考意义

| 方向（网络安全/信创/等保/隐私保护/护网） | 可证事实 | 本阶段处理 |
|---|---|---|
| **网络安全（方向级）** | ① **凭据可从托管平台被批量取走**（NSM 官方定性：access tokens / secrets / named values 被定向搜寻，Equinor + Skagerak 受害）；② **平台侧修复不撤销已取走的客户凭据**（微软通告经三方转述）；③ **受影响层级精确到 APIM Classic 的 Developer/Basic/Standard/Premium，Consumption 与 v2 不受影响**；④ **轮换必须回到签发方吊销**（只改平台侧值不算吊销）；⑤ **检测在下游服务侧而非网关侧**；⑥ **影子实例是未轮换密钥存活处**；⑦ **国家机构给出的可执行自查判据**（RuntimeVersion 阈值 31936/31938 + 未更新须联系供应商） | 🟡 **进评审（方向级）** —— 落三条方向级动作：**① "凭据台账新增托管位置维度"**（凭据 × 签发方 × 托管平台/层级 × 是否生产实例 × 吊销路径）；**② "凭据吊销时效"列为独立度量项**（从怀疑泄露到完成吊销的时长，配套库内 11-20 已有的出口日志 200/410/429 判据作为起点时间戳）；**③ "非生产/影子实例"纳入暴露面台账**。**不产专项整改**（第 1 关：我方无使用该平台的一手证据，属待核实）；**不新开产品特性**（我方 DER/聚合平台的密钥管理设计材料不在库内，凭情报做产品对应会失真） |
| **等保（方向级）** | 平台侧补丁与客户侧凭据吊销是**两个独立义务**，且官方文本明确要求"逐实例确认版本 + 未更新联系供应商 + 发现入侵联系主管机构" —— 构成一条**可写进等保测评证据链的动作序列**（识别 → 确认 → 处置 → 报告） | 🟡 **登记跟踪** —— 与库内 11-19 已记「第三方参与远程运维」条目同属"供应链与托管服务的责任边界"议题；**但等保测评项映射需产品与合规材料，库内不具备，暂不转产物** |
| **护网（方向级）** | 攻击者是**凭证库猎手**而非单目标定向攻击（Equinor 自述"并非专门针对本公司"）；防护着力点应为**减少可被批量获取的凭据面**（短生命周期、集中签发、不可横向复用、影子实例清理） | 🟡 **进评审（方向级）** —— 建议并入既有「攻击手法→防线覆盖度对照」（`remediation-defenseTacticCoverage-20261112`），**新增一条攻击手法「凭据托管平台泄露」及其防线映射**；**演练场景可增一个"影子实例遗留凭据"的自查项**。**不新开产物** |
| **隐私保护** | 若被取走的凭据可直达持有个人数据的后端服务，则 GDPR / NIS 报告时钟可能已在运行（SECNEWS 指出此点） | ❌ **本阶段不转评审** —— 我方无个人信息处理场景的一手材料；**登记跟踪**，若后续出现"我方客户侧涉及个人信息且凭据由第三方平台托管"的实证再评 |
| **信创** | — | ❌ **不适用** —— 本条无信创相关可证事实，不做形式化挂钩 |

---

## 七、总结输出

**一句话结论**：**挪威国家安全局 11-20 公布、11-23 更新的一则通告，标志库内第一条「能源行业确认在野入侵」事件 —— 身份不明的行为者在 Azure API Management 中定向搜寻 access tokens / secrets / named values，Equinor 与 Skagerak Energi 均在受害名单，而漏洞最早是由挪威能源行业自己发现并被 NSM 表彰共享的；但它对我方的真正价值不是漏洞本身（我方不用该产品），而是它第一次用真实事件验证了库内反复确立却始终没有被证实的那条判据：暴露面不等于「我方装了什么」，而等于「我方的长期凭据托管在哪儿、被谁够到」—— 微软 11-19 关闭了访问路径，修复却「不会自动作废此前可能被访问过的客户凭据」，这使它成为库内「被偷的是身份不是密钥」原则的第三个独立样本、也是唯一一个漏洞根本不在客户系统里的样本；由此应固化的动作是三条：凭据台账新增「托管位置 + 层级规格 + 是否生产实例」维度、把「从怀疑泄露到完成吊销」的时长列为独立度量项（配套库内 11-20 已有的出口日志 200/410/429 判据作为起点时间戳）、把测试与供应商代运维的影子实例纳入暴露面台账；同时必须钉死五条边界：无 CVE、无 CVSS、无受害客户数、攻击者归属完全未知、受害方公告未提 APIM 因果链全由 NSM 单方给出（且 NSM 原文自己把「发现方」误写为电力部门、隔天更正为能源部门 —— 引用二手转述必须回原文核对主体范围）。**

**落地去向**
- [ ] 产品特性
- [ ] 需求变更
- [ ] 专项整改

---

## 参考链接

- [NSM（挪威国家安全局）：NSM deler tiltak mot sårbarhet i Azure API Management（2026-11-20 发布 / 11-23 更新）](https://www.nsm.no/aktuelt/nsm-deler-tiltak-mot-sarbarhet-i-azure-api-management/)
- [SECNEWS：Follow-up: Equinor attack linked to Azure API Management flaw（2026-11-23）](https://secnews.co.uk/2026/11/follow-up-equinor-azure-api-management-flaw-nsm-rotate-secrets)
- [ThreatTicker：Norway warns an Azure API Management flaw was exploited against Equinor, Skagerak Energi and other firms（2026-11-23）](https://threatticker.com/news/norway-warns-an-azure-api-management-flaw-was-exploited-against-equinor)
- [库内相关：Microsoft agent-framework PyPI 投毒（被偷的是身份不是密钥 · 令牌 24 小时有效）](agentFrameworkPypiSupplyChain-2026-11.md)
- [库内相关：CISA KEV 2026-11-20 批次（vCenter 补丁不撤销已取走的 SAML 签名材料）](cisaKev20261120Batch-2026-11.md)
- [库内相关：WAF 巡检 11-18 —— 我方 /preview/getCorsFile 的 Base64 URL 参数面](wafCorsFilePreviewUrlParamSurface-2026-11-18.md)
- [库内相关：凭据收割扫描器路径字典命中我方站点](credentialHarvestProbePaths-2026-11.md)

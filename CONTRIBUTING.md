# PV-Intel 维护规范

> 采集 / 写作 / 评审 / 提交规范
> 完整操作流程见 [src/meta/pipeline.md](src/meta/pipeline.md)

---

## 1. 目录结构

```
pv-intel/
├── README.md                    # 根索引
├── CONTRIBUTING.md              # 本文件
├── book.toml                    # mdbook 配置
├── src/                         # mdbook 内容根
│   ├── SUMMARY.md               # mdbook 导航（**改这里加页面**）
│   ├── intro.md
│   ├── solar-industry/          # ☀️ 光伏产业
│   ├── policy/                  # 📜 政策发文
│   ├── security-intel/          # 🛡️ 网络安全情报
│   ├── briefings/               # 📋 定期简报
│   ├── deliverables/            # 🎯 评审输出
│   └── meta/                    # 📐 规范
├── scripts/                     # 🔧 辅助脚本
├── raw/                         # 采集原始数据（gitignore）
└── .github/workflows/           # 🚀 mdbook 部署
```

**新文档必须放对应域下**，不要放 root。

---

## 2. 命名规范

| 类型 | 规范 | 示例 |
|---|---|---|
| 情报原文 | CamelCase + 主题 | `componentPriceTrend.md` / `nDRCElectricityPricing.md` |
| 简报 | `YYYY-MM-DD-daily.md` / `YYYY-Www-weekly.md` / `YYYY-MM-monthly.md` | `2026-11-12-daily.md` |
| 评审产物 | `<类型>-<主题>-<YYYYMMDD>.md` | `feature-priceForecast-20261115.md` |

**禁止**：❌ 中文文件名 · ❌ 空格/特殊字符 · ❌ 数字开头

---

## 3. 写作规范

- 中文为主，技术术语保留英文
- **表格优先于长段落**
- 标题层级不跳级（mdbook 要求 `#` → `##` → `###`）
- 每篇末尾有「参考链接」节
- 情报原文必须带 `source_url`；无链接不入库

---

## 4. 写作流程（7 步）

```
[源 URL / 内部数据源]
  ↓
1. 抓取（web_search / curl / 内部 WAF 报告）
  ↓
2. 判定相关性 —— 走不通「外部变化 → 影响我方指标 → 需改产品行为？」的链，丢弃
  ↓
3. 定级 🔴强约束 / 🟡有影响 / ⚪备案
  ↓
4. 落库到对应域的 .md（按域的落库格式）
  ↓
5. 更新该域的 README.md 索引表
  ↓
6. 更新 src/SUMMARY.md（若新增页面）
  ↓
7. 提交：scripts/publish.sh "<commit message>"
```

---

## 5. 评审门槛（四关，任一不过退回）

| 关卡 | 判据 |
|---|---|
| 1. 影响可证 | 能指出**具体**受影响的产品线/系统/接口 |
| 2. 动作明确 | 能写成一句"要做什么"，不是"要关注" |
| 3. 归属明确 | 落到某条产品线，且有明确责任人 |
| 4. 可验收 | 有可验证的完成标准 |

> 第 1 关最易放水：**"可能会影响"不算影响。**

---

## 6. 提交规范

```bash
./scripts/publish.sh "briefing: 2026-11-12 日报"
```

- 禁止 force push
- 每次 push 后 mdbook workflow 自动部署 GitHub Pages
- 大改动（口径调整）先改 `src/meta/pipeline.md`，再改实现

---

## 7. 禁止事项

- ❌ 在简报里新增事实（简报只做归纳与索引，细节链到原文）
- ❌ 把采集的原始 JSON 提交进仓（放 `raw/`，已 gitignore）
- ❌ 无 `source_url` 的情报入库
- ❌ 未过评审门槛的情报直接进 `deliverables/`
- ❌ 改 `book.toml` 的 `src` 路径（会破坏 Pages 部署）

---

## 8. 相关链接

- [src/meta/pipeline.md](src/meta/pipeline.md) —— 流水线操作手册
- [src/deliverables/README.md](src/deliverables/README.md) —— 产物格式与验收

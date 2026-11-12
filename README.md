# PV-Intel 光伏情报库

> 光伏产业 · 政策发文 · 网络安全情报
> **采集 → 简报 → 归纳总结 → 评审 → 可落地的产品特性 / 需求变更 / 专项整改工作规划**

[![mdBook](https://img.shields.io/badge/mdBook-阅读-f39c12?style=flat-square)](https://ishadowland.github.io/pv-intel/)
[![Repo](https://img.shields.io/badge/repo-collecting-lightgrey?style=flat-square)](https://github.com/ishadowland/pv-intel)

---

## 为什么建这个库

三类外部信息各自都有人看，但**没人把它们合在一起看**：

| 信息流 | 单独看的问题 | 合并后能回答的问题 |
|---|---|---|
| 光伏产业（供需/价格/技术） | "组件又涨价了" | 涨价是否影响我方电站资产估值与结算 |
| 政策发文（部委/地方） | "又一个通知" | 哪条通知**直接约束**了我方产品功能与申报流程 |
| 网络安全情报（CVE/攻击/合规） | "又一个漏洞" | 哪些漏洞**真的**打在我方暴露面上，谁来修、何时修 |

**本库的核心不是"存"，是"收敛成动作"。**

每条情报最终必须落成三类产物之一：

1. **产品特性** —— 新功能 / 增强 / 平台能力补齐
2. **需求变更** —— 已有功能的行为调整（接口、字段、流程、默认值）
3. **专项整改工作规划** —— 有明确责任人、时间点、验收标准的工程任务

---

## 文档树

```
pv-intel/
├── src/
│   ├── intro.md                    📖 库说明
│   ├── SUMMARY.md                  🧭 mdbook 导航
│   ├── solar-industry/             ☀️ 光伏产业
│   │   └── README.md                  采集口径 · 四条采集线 · 跟踪对象
│   ├── policy/                     📜 政策发文
│   │   └── README.md                  三级分类 · 落库格式 · 跟踪机制
│   ├── security-intel/             🛡️ 网络安全情报
│   │   └── README.md                  暴露面过滤 · 内部数据源 · 落库格式
│   ├── briefings/                  📋 定期简报
│   │   └── README.md                  日/周/月报格式与硬约束
│   ├── deliverables/               🎯 评审输出
│   │   └── README.md                  三类产物 · 评审四关 · 落库模板
│   └── meta/                       📐 元信息
│       └── pipeline.md                流水线全貌 · 采集规则 · 评审门槛
├── scripts/
│   ├── publish.sh                  🔧 提交并推送
│   └── collect.py                  🔧 采集辅助（WAF 内部数据源）
└── .github/workflows/mdbook.yml    🚀 自动部署 GitHub Pages
```

---

## 流水线

```
┌─────────────┐   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐
│  ① 采集      │   │  ② 简报      │   │  ③ 归纳总结  │   │  ④ 评审      │
│  每日 07:00  │──▶│  每日 08:00  │──▶│  周 / 月     │──▶│  月度评审会  │
│  raw/*.json  │   │  briefings/  │   │  简报中完成  │──▶│ deliverables/│
└─────────────┘   └─────────────┘   └─────────────┘   └─────────────┘
```

**评审只读简报，不读原始采集文件** —— 保证每期评审的输入面可控。

---

## 快速入口

| 我想看 | 去哪 |
|---|---|
| 今天有什么新情报 | [src/briefings/](src/briefings/README.md) |
| 组件价格现在什么水平 | [src/solar-industry/](src/solar-industry/README.md) |
| 最近哪个部委文件影响我 | [src/policy/](src/policy/README.md) |
| 我们有什么暴露面 | [src/security-intel/](src/security-intel/README.md) |
| 要排明年的整改计划 | [src/deliverables/](src/deliverables/README.md) |
| 流水线怎么跑 | [src/meta/pipeline.md](src/meta/pipeline.md) |

---

## 维护规范

见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 参考链接

- [mdBook 官方文档](https://rust-lang.github.io/mdBook/)
- [iswiki（同构知识库范式参考）](https://github.com/ishadowland/iswiki)

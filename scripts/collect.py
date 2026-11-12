#!/usr/bin/env python3
"""pv-intel 采集辅助 —— 安全域内部数据源

把 WAF 巡检报告转成安全情报条目（raw/*.json）。

背景：外部漏洞新闻满天飞，但 WAF 巡检报告是唯一"真实攻击者正在打我们"的证据。
本脚本做的是**暴露面信号提取**，不是漏洞扫描：
  - 攻击类型分布趋势
  - 疑似针对我方业务路径的探测（对照白名单/快速通道判定结果）
  - 响应侧规则命中（m_response —— 后端可能真的在泄露堆栈）

用法:
  python3 scripts/collect.py --waf-report <path> --out raw/security-<date>.json
  python3 scripts/collect.py --waf-report <path> --out -        # 打到 stdout

依赖: 仅标准库
"""
import argparse
import datetime
import json
import os
import re
import sys

WAF_REPORT = os.path.expanduser(
    "~/../.openclaw/workspace/waf-inspection-report-latest.md"
)

# 我方业务站点（用于区分"打我们的"和"打客户的"）
OWN_SITES = ["pinnenger.com", "ptm", "idmo", "182.140.209", "megaroutine"]


def _read(path):
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8", errors="replace") as f:
        return f.read()


def parse_waf_report(text):
    """从 WAF 报告里提取情报条目"""
    items = []

    # ---- 1. Info Leak 判定表（最关键：LLM 判定过的每一条）----
    # 表格行形如: | **1.2.3.4** | 1 次 | legit_business | 0.95 | cat | M3.1 | ✅ 疑似正常业务 | reason |
    row_re = re.compile(
        r"^\|\s*\*\*([\d.]+)\*\*\s*\|\s*(\d+)\s*次\s*\|\s*([\w?]+)\s*\|\s*([\d.]+)\s*\|\s*([^|]*)\|\s*([^|]*)\|\s*([^|]*)\|"
    )
    url_re = re.compile(r"\*\*URL\*\*:\s*`([^`]+)`")
    rule_re = re.compile(r"\*\*攻击类型\*\*:\s*Info Leak \(rule:\s*`([^`]+)`\)")

    for line in text.splitlines():
        m = row_re.match(line.strip())
        if not m:
            continue
        ip, cnt, verdict, conf, category, model, status = m.groups()
        if verdict == "?" and conf == "0.00":
            sev = "medium"
            title = f"{ip} 命中 Info Leak 但 LLM 未给出判定（响应侧规则）"
        elif verdict == "legit_business":
            sev = "low"
            title = f"{ip} Info Leak 判定为正常业务（{status.strip()}）"
        else:
            sev = "high"
            title = f"{ip} Info Leak 判为 {verdict} conf={conf}"

        items.append({
            "domain": "security",
            "title": title,
            "source_url": "",  # WAF 报告是内部数据源，无外链
            "published_at": _report_date(text),
            "collected_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "summary": status.strip(),
            "relevance": f"我方暴露面命中：{cnt} 次；分类={category.strip()}",
            "severity": sev,
            "verdict": verdict,
            "confidence": float(conf),
            "judge_model": model.strip(),
            "source": "internal-waf",
        })

    # ---- 2. 攻击类型分布 ----
    dist = {}
    for m in re.finditer(r"^\|\s*(📁|🛡️|❓|💻|⚠️)?\s*([A-Za-z ]+?)\s*\|\s*(\d+)\s*个", text, re.M):
        atype, _, cnt = m.groups()
        if atype and cnt:
            dist[atype.strip()] = int(cnt)
    if dist:
        items.append({
            "domain": "security",
            "title": "WAF 攻击类型分布：" + " / ".join(f"{k} {v}" for k, v in dist.items()),
            "source_url": "",
            "published_at": _report_date(text),
            "collected_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "summary": json.dumps(dist, ensure_ascii=False),
            "relevance": "攻击面趋势信号：用于判断哪类攻击正在上升",
            "severity": "low",
            "source": "internal-waf-distribution",
        })

    # ---- 3. 响应侧规则命中（后端可能真在泄露堆栈）----
    for m in re.finditer(r"\*\*URL\*\*:\s*`([^`]+)`", text):
        url = m.group(1)
        if "m_response" in text:
            items.append({
                "domain": "security",
                "title": f"响应侧规则命中，需核查后端响应内容：{url}",
                "source_url": url,
                "published_at": _report_date(text),
                "collected_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                "summary": "WAF 规则 m_response 表示响应内容本身含敏感信息（如 SQL 异常堆栈），"
                           "请求侧无取证价值，需在 WAF UI 用 event_id 查完整响应。",
                "relevance": "可能是后端异常处理不当（非攻击者问题），属产品/后端缺陷",
                "severity": "medium",
                "source": "internal-waf-m_response",
            })
            break  # 同一条只记一次

    return items


def _report_date(text):
    m = re.search(r"\*\*报告时间\*\*：(\d{4}-\d{2}-\d{2})", text)
    return m.group(1) if m else datetime.date.today().isoformat()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--waf-report", default=WAF_REPORT)
    ap.add_argument("--out", default="-")
    args = ap.parse_args()

    text = _read(args.waf_report)
    if not text:
        print(f"❌ 读不到 WAF 报告: {args.waf_report}", file=sys.stderr)
        sys.exit(2)

    items = parse_waf_report(text)
    payload = {
        "source": "safeline-waf",
        "collected_at": datetime.datetime.now().isoformat(timespec="seconds"),
        "report_path": args.waf_report,
        "count": len(items),
        "items": items,
    }

    out = json.dumps(payload, ensure_ascii=False, indent=2)
    if args.out == "-":
        print(out)
    else:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(out + "\n")
        print(f"✅ 写入 {args.out}（{len(items)} 条）", file=sys.stderr)


if __name__ == "__main__":
    main()

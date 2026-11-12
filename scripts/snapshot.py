#!/usr/bin/env python3
"""pv-intel 原文快照归档工具

采集时同步抓取原文并归档，作为情报的事实凭证：
  - 抽取正文（去导航/广告/脚本），存 Markdown
  - 记录 SHA256、字节数、HTTP 状态、抓取时间
  - 快照文件入库（raw/snapshots/），使证据链可追溯、不受原文删改影响

用法:
  python3 scripts/snapshot.py "<url>" --domain policy --slug ndrc-guidance-2026
  python3 scripts/snapshot.py "<url>" --domain solar --slug price-2026-11 --max-chars 20000

产出:
  raw/snapshots/<domain>/<slug>.md      # 归档快照（入库）
  raw/snapshots/<domain>/<slug>.meta.json  # 元信息（入库，含 SHA256）
"""
import argparse
import datetime
import hashlib
import html
import json
import os
import re
import urllib.request
import urllib.error
import ssl

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNAP_DIR = os.path.join(REPO, "raw", "snapshots")

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0 Safari/537.36"

# 部分政务/媒体站点证书过期或链不全，降级为不校验（只抓公开页面，不提交任何凭据）
SSL_UNVERIFIED = ssl._create_unverified_context()

# 抓取后剔除的噪声
DROP_TAGS = ["script", "style", "nav", "header", "footer", "aside", "form", "noscript", "iframe"]


def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    })
    ctx = SSL_UNVERIFIED
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
            return _read_response(r)
    except ssl.SSLCertVerificationError:
        # 证书问题 —— 用不校验的 context 重试
        with urllib.request.urlopen(req, timeout=timeout, context=SSL_UNVERIFIED) as r:
            return _read_response(r)


def _read_response(r):
    raw = r.read()
    # 部分站点无视 Accept-Encoding 直接返回 gzip 压缩体，不解压会存下乱码快照
    gzip_decoded = False
    if raw[:2] == b"\x1f\x8b":
        import gzip
        try:
            raw = gzip.decompress(raw)
            gzip_decoded = True
        except OSError:
            pass
    # PDF：按二进制原样返回（正文由 pdf_text() 提取，SHA256 仍对原始字节计算）
    if raw[:4] == b"%PDF" or "application/pdf" in (r.headers.get("Content-Type") or "").lower():
        return r.status, "", raw, gzip_decoded
    enc = "utf-8"
    try:
        ctype = r.headers.get("Content-Type", "")
        if "charset=" in ctype:
            enc = ctype.split("charset=")[-1].split(";")[0].strip() or "utf-8"
        else:
            m = re.search(rb'charset=[\'"]?([\w-]+)', raw[:2000], re.I)
            if m:
                enc = m.group(1).decode("ascii", "ignore")
    except Exception:
        pass
    try:
        text = raw.decode(enc, errors="replace")
    except LookupError:
        text = raw.decode("utf-8", errors="replace")
    return r.status, text, raw, gzip_decoded


def pdf_text(raw):
    """从 PDF 原始字节提取纯文本；pypdf 不可用时返回空串（不静默产生空快照）。"""
    try:
        import io
        from pypdf import PdfReader
    except ImportError:
        return ""
    try:
        reader = PdfReader(io.BytesIO(raw))
        pages = []
        for i, page in enumerate(reader.pages, 1):
            pages.append(f"\n\n===== [page {i}] =====\n\n" + (page.extract_text() or ""))
        return re.sub(r"\n{3,}", "\n\n", "".join(pages)).strip()
    except Exception as e:  # 提取失败要看得见，不能默默产出空快照
        print(f"⚠️  PDF 文本提取失败: {type(e).__name__}: {e}")
        return ""


def strip_html(text):
    for tag in DROP_TAGS:
        text = re.sub(rf"<{tag}\b.*?</{tag}>", " ", text, flags=re.S | re.I)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"<(br|/p|/div|/li|/h[1-6]|/tr)\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = re.sub(r"[ \t ]+", " ", text)
    text = re.sub(r"\n\s*\n\s*\n+", "\n\n", text)
    return "\n".join(ln.strip() for ln in text.splitlines()).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url")
    ap.add_argument("--domain", required=True, help="solar / policy / security")
    ap.add_argument("--slug", required=True)
    ap.add_argument("--max-chars", type=int, default=60000)
    args = ap.parse_args()

    d = os.path.join(SNAP_DIR, args.domain)
    os.makedirs(d, exist_ok=True)

    try:
        status, text, raw, gzip_decoded = fetch(args.url)
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP {e.code}: {args.url}")
        raise SystemExit(1)
    except Exception as e:
        print(f"❌ 抓取失败 {type(e).__name__}: {e}")
        raise SystemExit(1)

    body = pdf_text(raw) if raw[:4] == b"%PDF" else strip_html(text)
    if raw[:4] == b"%PDF" and not body:
        print("❌ PDF 文本提取为空（pypdf 缺失或解析失败），拒绝生成空快照")
        raise SystemExit(1)
    truncated = len(body) > args.max_chars
    if truncated:
        body = body[:args.max_chars] + "\n\n> ⚠️ 快照已截断（原文超长）"

    sha = hashlib.sha256(raw).hexdigest()
    fetched_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    md_path = os.path.join(d, f"{args.slug}.md")
    meta_path = os.path.join(d, f"{args.slug}.meta.json")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(f"<!-- 原文快照 · 自动归档，请勿手工编辑 -->\n")
        f.write(f"<!-- source_url: {args.url} -->\n")
        f.write(f"<!-- fetched_at: {fetched_at} -->\n")
        f.write(f"<!-- sha256: {sha} -->\n\n")
        f.write(body)
        if not body.endswith("\n"):
            f.write("\n")

    meta = {
        "source_url": args.url,
        "fetched_at": fetched_at,
        "http_status": status,
        "sha256_raw": sha,
        "raw_bytes": len(raw),
        "text_chars": len(body),
        "truncated": truncated,
        "domain": args.domain,
        "slug": args.slug,
        "gzip_decoded": gzip_decoded,
    }
    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)

    print(f"✅ 快照已归档")
    print(f"   文件: {os.path.relpath(md_path, REPO)}")
    print(f"   正文: {len(body)} 字符" + ("（已截断）" if truncated else ""))
    print(f"   sha256: {sha[:16]}…")
    print(f"   抓取: {fetched_at}  HTTP {status}")


if __name__ == "__main__":
    main()

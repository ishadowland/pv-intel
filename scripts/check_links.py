#!/usr/bin/env python3
"""pv-intel 内部链接校验

mdbook 会把断链渲染成死链，且不会报错 —— 发布前必须自己查。

校验范围:
  - src/SUMMARY.md 的所有导航链接（mdbook 入口）
  - src/**.md 的内部相对链接（排除代码块内的示例链接）

用法:
  python3 scripts/check_links.py          # 断链则 exit 1
  python3 scripts/check_links.py --quiet  # 只在有断链时输出
"""
import io
import os
import re
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(REPO, "src")

CODE_FENCE = re.compile(r"```.*?```", re.S)
LINK = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")


def strip_code(t):
    return CODE_FENCE.sub("", t)


def check_file(path, rel_base):
    bad = []
    try:
        txt = io.open(path, encoding="utf-8").read()
    except OSError:
        return bad
    for title, link in LINK.findall(strip_code(txt)):
        if link.startswith(("http://", "https://", "#", "mailto:", "ftp://")):
            continue
        target = link.split("#")[0].split("?")[0]
        if not target:
            continue
        full = os.path.normpath(os.path.join(rel_base, target))
        if not os.path.exists(full):
            bad.append((path, title, link))
    return bad


def main():
    quiet = "--quiet" in sys.argv
    bad = []

    # SUMMARY 导航
    summary = os.path.join(SRC, "SUMMARY.md")
    if os.path.exists(summary):
        bad += check_file(summary, SRC)

    # 其余文档
    for root, _dirs, files in os.walk(SRC):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            p = os.path.join(root, fn)
            if os.path.abspath(p) == os.path.abspath(summary):
                continue
            bad += check_file(p, root)

    if bad:
        print(f"❌ 断链 {len(bad)} 处：")
        for p, title, link in bad:
            rel = os.path.relpath(p, REPO)
            print(f"   {rel}  [{title or '—'}] → {link}")
        sys.exit(1)

    if not quiet:
        print("✅ 内部链接全部有效")
    sys.exit(0)


if __name__ == "__main__":
    main()

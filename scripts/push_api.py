#!/usr/bin/env python3
"""pv-intel 备用推送 —— 走 GitHub REST API（不依赖 github.com 的 git 协议）

背景：本机到 github.com 的 gnutls 握手不稳定（HK 段 IP 20.205.243.166 间歇性
TLS 断连），而 api.github.com 稳定。git push 失败时用本脚本兜底，
通过 Git Data API 完成 提交 → 建树 → 建 commit → 更新 ref。

用法:
  python3 scripts/push_api.py "commit message"

前提：工作区已 git add -A（暂存区内容就是要推送的内容）。
"""
import base64
import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OWNER = "ishadowland"
NAME = "pv-intel"
BRANCH = "main"
API = f"https://api.github.com/repos/{OWNER}/{NAME}"


def token():
    try:
        out = subprocess.run(["gh", "auth", "token"], capture_output=True, text=True, timeout=20)
        return out.stdout.strip()
    except Exception:
        return ""


TOK = token()


def req(method, url, body=None):
    """带退避重试的 API 调用 —— 本机到 GitHub 的 TLS 握手间歇性断连"""
    data = json.dumps(body).encode() if body is not None else None
    last = (0, {})
    for attempt in range(6):
        r = urllib.request.Request(url, data=data, method=method, headers={
            "Authorization": f"Bearer {TOK}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "Content-Type": "application/json",
            "User-Agent": "pv-intel-push",
        })
        try:
            with urllib.request.urlopen(r, timeout=45) as resp:
                raw = resp.read()
                return resp.status, (json.loads(raw) if raw else {})
        except urllib.error.HTTPError as e:
            body_txt = e.read() or b"{}"
            try:
                return e.code, json.loads(body_txt)
            except Exception:
                return e.code, {}
        except Exception as e:
            last = (0, {"err": f"{type(e).__name__}: {e}"})
            wait = min(2 ** attempt, 20)
            print(f"   ↻ API 连接失败({type(e).__name__})，{wait}s 后重试 [{attempt+1}/6]", file=sys.stderr)
            time.sleep(wait)
    return last


def git(*args):
    return subprocess.run(["git", "-C", REPO, *args], capture_output=True, text=True).stdout.strip()


def main():
    msg = sys.argv[1] if len(sys.argv) > 1 else "chore: update pv-intel"
    if not TOK:
        print("❌ 拿不到 gh token")
        sys.exit(1)

    # 1. 暂存区文件列表（区分新增/修改/删除）
    raw = git("diff", "--cached", "--name-status", "-z")
    if not raw:
        print("✅ 无改动，无需推送")
        sys.exit(0)

    parts = [p for p in raw.split("\0") if p]
    changes = []
    i = 0
    while i < len(parts):
        st = parts[i]
        path = parts[i + 1]
        i += 2
        changes.append((st, path))

    # 2. 当前远端 HEAD + base tree
    code, ref = req("GET", f"{API}/git/ref/heads/{BRANCH}")
    if code != 200:
        print(f"❌ 取 ref 失败 HTTP {code}: {json.dumps(ref)[:200]}")
        sys.exit(1)
    head_sha = ref["object"]["sha"]
    code, commit = req("GET", f"{API}/git/commits/{head_sha}")
    if code != 200:
        print(f"❌ 取 commit 失败 HTTP {code}")
        sys.exit(1)
    base_tree = commit["tree"]["sha"]

    # 3. 每个文件建 blob
    tree_entries = []
    for st, path in changes:
        full = os.path.join(REPO, path)
        if st == "D":
            tree_entries.append({"path": path, "mode": "100644", "type": "blob", "sha": None})
            continue
        with open(full, "rb") as f:
            content = base64.b64encode(f.read()).decode()
        code, blob = req("POST", f"{API}/git/blobs", {"content": content, "encoding": "base64"})
        if code != 201:
            print(f"❌ 建 blob 失败 {path} HTTP {code}: {json.dumps(blob)[:200]}")
            sys.exit(1)
        tree_entries.append({"path": path, "mode": "100644", "type": "blob", "sha": blob["sha"]})

    # 4. 建树
    code, tree = req("POST", f"{API}/git/trees", {"base_tree": base_tree, "tree": tree_entries})
    if code != 201:
        print(f"❌ 建树失败 HTTP {code}: {json.dumps(tree)[:300]}")
        sys.exit(1)

    # 5. 建 commit
    code, newc = req("POST", f"{API}/git/commits", {
        "message": msg, "tree": tree["sha"], "parents": [head_sha],
    })
    if code != 201:
        print(f"❌ 建 commit 失败 HTTP {code}: {json.dumps(newc)[:300]}")
        sys.exit(1)
    new_sha = newc["sha"]

    # 6. 更新 ref
    code, upd = req("PATCH", f"{API}/git/refs/heads/{BRANCH}", {"sha": new_sha, "force": False})
    if code != 200:
        print(f"❌ 更新 ref 失败 HTTP {code}: {json.dumps(upd)[:300]}")
        sys.exit(1)

    # 7. 本地与远端对齐
    subprocess.run(["git", "-C", REPO, "reset", "--soft", new_sha], capture_output=True)

    print(f"✅ 已通过 API 推送")
    print(f"   commit: {new_sha[:7]}")
    print(f"   文件: {len(changes)} 个")
    print(f"   链接: https://github.com/{OWNER}/{NAME}/commit/{new_sha}")
    print(f"   Pages: https://ishadowland.github.io/{NAME}/  (CI 部署中, 约 1-2 分钟)")


if __name__ == "__main__":
    main()

#!/usr/bin/env bash
# 提交并推送到 GitHub（mdbook workflow 会自动部署 Pages）
# 用法: ./scripts/publish.sh "commit message"
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_DIR"

MSG="${1:-chore: update pv-intel}"

if ! command -v git >/dev/null 2>&1; then
  echo "❌ git 未安装"; exit 1
fi

# 身份
git config --local user.name "ishadowland" 2>/dev/null || true
git config --local user.email "ishadowland@gmail.com" 2>/dev/null || true
git config --local credential.helper '!gh auth git-credential' 2>/dev/null || true

git add -A

if git diff --cached --quiet; then
  echo "✅ 无改动，无需提交"
  exit 0
fi

echo "=== 待提交文件 ==="
git diff --cached --name-status
echo

# 发布前自检：内部链接必须全通（mdbook 断链不报错，只会渲染成死链）
if ! python3 scripts/check_links.py; then
  echo "❌ 内部链接校验未通过，已中止发布"
  exit 1
fi

git commit -m "$MSG"

# 禁止 force push；非快进则 rebase
if ! git push origin main 2>/tmp/pv-intel-push.err; then
  echo "⚠️ push 失败，尝试 pull --rebase ..."
  git pull --rebase origin main
  git push origin main
fi

SHA=$(git rev-parse --short HEAD)
echo
echo "✅ 已推送"
echo "   commit: $SHA"
echo "   链接:   https://github.com/ishadowland/pv-intel/commit/$SHA"
echo "   Pages:  https://ishadowland.github.io/pv-intel/  (CI 部署中, 约 1-2 分钟)"

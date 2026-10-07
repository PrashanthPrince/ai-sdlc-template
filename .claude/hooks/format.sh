#!/usr/bin/env bash
# Auto-format after edits. Swap in your stack's formatter (phpcbf, dotnet format, prettier...).
path=$(cat | jq -r '.tool_input.file_path // empty')
[ -z "$path" ] && exit 0
case "$path" in
  *.ts|*.tsx|*.js|*.jsx|*.css|*.scss|*.json|*.md) npx --no-install prettier --write "$path" >/dev/null 2>&1 || true ;;
  *.php|*.module|*.theme) vendor/bin/phpcbf "$path" >/dev/null 2>&1 || true ;;
  *.cs) dotnet format --include "$path" >/dev/null 2>&1 || true ;;
esac
exit 0

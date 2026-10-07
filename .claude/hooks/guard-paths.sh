#!/usr/bin/env bash
# Blocks agent edits to protected paths. Exit code 2 = block and tell Claude why.
input=$(cat)
path=$(echo "$input" | jq -r '.tool_input.file_path // empty')
case "$path" in
  *.env|*.env.*|*/secrets/*|*.pem|*.key)          echo "Blocked: secrets files are off-limits." >&2; exit 2 ;;
  */.github/workflows/*|*/.claude/settings.json)   echo "Blocked: pipeline and agent permissions change only via human PR." >&2; exit 2 ;;
  */CODEOWNERS)                                    echo "Blocked: CODEOWNERS is human-owned." >&2; exit 2 ;;
esac
exit 0

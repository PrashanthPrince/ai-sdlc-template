#!/usr/bin/env bash
# Blocks shell commands that would expose secrets or touch production.
cmd=$(cat | jq -r '.tool_input.command // empty')
if echo "$cmd" | grep -Eqi '(cat|less|head|tail|printenv|env)\b.*(\.env|secret|token|password|\.pem|\.key)|--prod|production'; then
  echo "Blocked: command may expose secrets or target production." >&2; exit 2
fi
exit 0

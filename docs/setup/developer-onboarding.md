# Developer onboarding (30 minutes)

1. Install Claude Code and sign in with your WPP Team/Enterprise seat (never a personal account on client code).
2. Clone the repo; run `claude` in the root. It picks up CLAUDE.md, .claude/agents, skills, commands, hooks and .mcp.json.
3. Run `/mcp` to authenticate Atlassian (OAuth) and GitHub.
4. For requirements drafting, manually redact client PII and secrets from a meeting transcript, place the `.docx` in `docs/inputs/`, and run `/requirements docs/inputs/<transcript>.docx`. Confirm the redaction when prompted.
5. Try: `/design KEY-123` on a Ready story, then `/implement KEY-123` once it's approved.
6. Your job on every agent PR: read the diff like you wrote it. You are accountable for what you approve.
7. When an agent gets something wrong, fix the PR AND add a rule to CLAUDE.md "Lessons learned".

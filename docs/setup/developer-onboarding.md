# Developer onboarding (30 minutes)

1. Install Claude Code and sign in with your WPP Team/Enterprise seat (never a personal account on client code).
2. Clone the repo; run `claude` in the root. It picks up CLAUDE.md, .claude/agents, skills, commands, hooks and .mcp.json.
3. Run `/mcp` to authenticate Atlassian (OAuth) and GitHub.
4. Try: `/design KEY-123` on a Ready story, then `/implement KEY-123` once it's approved.
5. Your job on every agent PR: read the diff like you wrote it. You are accountable for what you approve.
6. When an agent gets something wrong, fix the PR AND add a rule to CLAUDE.md "Lessons learned".

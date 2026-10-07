# GitHub setup (repo admin, ~30 minutes)

1. Branch protection on `main` and `develop`:
   - Require PR, 1 approval from CODEOWNERS, dismiss stale approvals
   - Require status checks: `ci / checks`, `agent-review / review`
   - Block force pushes; include administrators
2. Environments: `qa` (no reviewers), `staging` + `production` (required reviewers = PM / Tech Lead). This is Gate 5.
3. Secrets: `ANTHROPIC_API_KEY` (org-level, from the WPP Anthropic Console org), `ATLASSIAN_API_TOKEN`.
4. Install the Claude GitHub App on the repo (run `/install-github-app` in Claude Code, or install manually).
5. Labels: `agent:design`, `agent:build`, `ai-drafted`, `agent-pr`.

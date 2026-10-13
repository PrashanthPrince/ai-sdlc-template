# AI Agent-Driven SDLC - reference repo template

Drop-in `.claude/` + `.github/` setup that runs agents at every SDLC phase with a human gate at every phase boundary.
Stack-agnostic core, with adapters for Drupal, SitecoreAI, AEM, Umbraco and MACH.

## What's inside
| Path | What |
|---|---|
| `CLAUDE.md` | Project rules every agent follows. Fill in the PROJECT section. |
| `.claude/agents/` | 22 subagents, one job each, least-privilege tools |
| `.claude/commands/` | `/requirements` `/write-stories` `/design` `/implement` `/review` `/release` `/retro` |
| `.claude/skills/cms-*` | Stack adapters: conventions, commands, gotchas |
| `.claude/settings.json` | Allow/deny permissions + hooks |
| `.claude/hooks/` | Path guard, secret/prod guard, auto-format |
| `.mcp.json` | Atlassian (Jira), GitHub, Figma MCP servers |
| `.github/workflows/` | `agent-pipeline` (Jira-triggered design/build), `agent-review` (every PR), `ci` (checks + gated deploys) |
| `.github/CODEOWNERS`, PR template | Human approval enforcement |
| `docs/setup/` | Jira, GitHub and developer setup guides |
| `templates/`, `docs/adr/` | Requirements, tech design and ADR templates |

## Pipeline
| Phase | Command / trigger | Agents | Human gate |
|---|---|---|---|
| 1 Discover | `/write-stories` | requirements-analyst, site-auditor, story-writer, backlog-critic | PM + PO: Draft – AI → Ready |
| 2 Design | `/design KEY` or Jira → In Design | tech-designer, estimator, solution-architect, content-modeller | Tech Lead: → Design Approved |
| 3 Build | `/implement KEY` or Jira → Ready for Build | developer, frontend-builder, migration-scripter, docs-writer | - |
| 4 Review/QA | PR opened; deploy to QA | code-reviewer, security-reviewer, test-author, qa-runner, bug-triager | CODEOWNER approves PR; QA Lead: → QA Passed |
| 5 Release | `/release vX` | release-manager, deploy-verifier | PM (+client) approves prod Environment |
| 6 Operate | alerts, weekly, per sprint | incident-analyst, backlog-groomer, retro-analyst | Tech Lead reviews CLAUDE.md changes |

## Setup order
1. `docs/setup/github-setup.md`  2. `docs/setup/jira-workflow.md`  3. Fill in `CLAUDE.md`, pick the adapter
4. Replace placeholder CI steps with the adapter's commands  5. `docs/setup/developer-onboarding.md`

## Requirements from meeting transcripts
Place a manually redacted `.docx` transcript in `docs/inputs/` and run `/requirements docs/inputs/<transcript>.docx`.
The command extracts paragraph and table text with stable source references and drafts
`docs/requirements/requirements.md` from `templates/requirements.md`. It asks before replacing
an existing requirements document. Confirm that the input contains no client PII or secrets
before processing; the same policy and extraction step are used by `/write-stories`. Input
DOCX files are ignored by Git and should not be committed.

## Verify before first use
Action inputs (`anthropics/claude-code-action@v1`), MCP server URLs and the Figma MCP port can change - check the current docs when you set up.
Hooks need `jq` installed on dev machines and runners.

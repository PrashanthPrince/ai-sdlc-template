# Project rules for AI agents

> Copy this file into every project repo and fill in the PROJECT section. Tech Lead owns it.
> Every time a reviewer catches an agent mistake, add a rule here or in the relevant skill.

## PROJECT
- Client: <client>
- Jira project key: <KEY>
- CMS adapter: <cms-drupal | cms-sitecore-ai | cms-aem | cms-umbraco | cms-mach>  → load `.claude/skills/<adapter>/SKILL.md`
- Environments: dev (auto on merge), qa (auto on merge to develop), staging + prod (human approval)
- Build: `<command>`   Test: `<command>`   Lint: `<command>`

## HOW WE WORK (applies to every agent)
1. Artefacts, not chat. Write outputs to files or Jira, never only to the conversation.
2. Never skip a gate. Only humans move tickets to Ready, Design Approved, QA Passed, Released. Only humans approve PRs.
3. No approved design = no code. If `Design Approved` is missing on the ticket, stop and say so.
4. Branches: `feature/<KEY>-<n>-<slug>`. Never commit to `main` or `develop`. Never force-push.
5. Commits and PR titles start with the Jira key: `KEY-123: add hero component`.
6. Tests and lint must pass locally before opening a PR. Open PRs as **draft**.
7. If the spec is unclear or wrong, stop and comment on the Jira ticket. Do not improvise scope.
8. Never read or print secrets (.env, keys, credentials). Never put client PII in prompts, fixtures or logs.
9. Prefer small PRs (< 400 changed lines). Split larger work and say how.

## DEFINITION OF DONE (agent-checkable)
- [ ] Every acceptance criterion has a test, named after the AC
- [ ] Lint, unit and E2E tests green
- [ ] Accessibility: no new axe violations (WCAG 2.2 AA)
- [ ] Docs/changelog updated when behaviour changes
- [ ] PR description uses `.github/pull_request_template.md`

## LESSONS LEARNED (append, newest first)
- <date> <rule> (from PR #<n>)

# Jira setup (Jira admin, ~1 hour)

## 1. Workflow statuses
Draft – AI → Ready → In Design → Design Approved → Ready for Build → In Build → In Review → Merged → In QA → QA Passed → Released

## 2. Gate transitions (restrict with workflow *conditions* to these groups)
| Transition | Allowed group |
|---|---|
| Draft – AI → Ready | pm, product-owner |
| In Design → Design Approved | tech-leads |
| In QA → QA Passed | qa-leads |
| QA Passed → Released | pm |
The agent service account is NOT in any of these groups.

## 3. Service account
- Create `ai-agent@<domain>` with Browse, Create, Comment, and Transition on non-gate transitions only.
- Label everything it creates `ai-drafted`.

## 4. Automation rules (Jira Automation → Send web request)
- When status → `In Design`: POST `https://api.github.com/repos/<org>/<repo>/dispatches`
  body `{"event_type":"jira-design","client_payload":{"issue_key":"{{issue.key}}"}}`
- When status → `Ready for Build`: same with `"event_type":"jira-build"`
- Headers: `Authorization: Bearer <fine-grained PAT with contents:write>` , `Accept: application/vnd.github+json`

## 5. Link Jira and GitHub
Install the "GitHub for Jira" app so branches/PRs/commits with the Jira key show on the ticket.

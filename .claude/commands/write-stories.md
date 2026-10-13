---
description: Phase 1 - analyse inputs and draft Jira stories for Gate 1 review
---
Run the Phase 1 pipeline for epic/area: $ARGUMENTS
1. Before extracting or passing any transcript content to an agent, ask the user to confirm that each input has been manually redacted of client PII and secrets. Stop if they cannot confirm.
2. For each `.docx` input in `docs/inputs/`, run `python3 scripts/docx_to_text.py "<path>"` and pass the extracted text with its source references to the requirements-analyst subagent. Pass supported text inputs directly.
3. Use the requirements-analyst subagent to write `docs/requirements/requirements.md` from `templates/requirements.md`. If the output already exists, ask the user before replacing it.
4. If this is a rebuild, use the site-auditor subagent.
5. Use the story-writer subagent to create Draft – AI stories.
6. Use the backlog-critic subagent on those stories.
Finish with a summary for the PM: stories created, open questions, critic verdicts.

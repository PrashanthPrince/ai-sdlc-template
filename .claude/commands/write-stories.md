---
description: Phase 1 - analyse inputs and draft Jira stories for Gate 1 review
---
Run the Phase 1 pipeline for epic/area: $ARGUMENTS
1. Use the requirements-analyst subagent on docs/inputs/.
2. If this is a rebuild, use the site-auditor subagent.
3. Use the story-writer subagent to create Draft – AI stories.
4. Use the backlog-critic subagent on those stories.
Finish with a summary for the PM: stories created, open questions, critic verdicts.

---
description: Phase 1 - turn a meeting transcript into a traceable requirements document
---
Input DOCX path under `docs/inputs/`: $ARGUMENTS

1. Confirm exactly one `.docx` input was provided and that it exists under `docs/inputs/`.
2. Before extracting or passing any content to an agent, ask the user to confirm that the DOCX has been manually redacted of client PII and secrets. Stop if they cannot confirm.
3. Run `python3 scripts/docx_to_text.py "$ARGUMENTS"` and stop with the reported error if extraction fails.
4. Pass the extracted text, the original filename, and the stable paragraph/table references to the `requirements-analyst` subagent.
5. Have the agent write `docs/requirements/requirements.md` from `templates/requirements.md`. If that output already exists, ask the user before replacing it.
6. Report the generated path and any open questions; do not create Jira tickets or transition statuses.

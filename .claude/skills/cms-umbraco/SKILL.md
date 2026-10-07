---
name: cms-umbraco
description: Umbraco (v13+) conventions - document types, Block List/Grid, uSync, .NET patterns and tests. Use on Umbraco projects.
---
# Umbraco adapter

## Structure
- Solution: `<Client>.Web` (site), `<Client>.Core` (services, view models), `<Client>.Tests`.
- Content model via Document Types and Element Types; compositions for shared fields.
- Blocks: Block List / Block Grid with a partial view per block in `Views/Partials/blocks/`.

## Rules
- Schema changes must be exported with uSync and committed (`uSync/v9/...`). The uSync files are the contract.
- Use ModelsBuilder strongly typed models; no magic strings for property aliases.
- Business logic in services registered via composers, not in views or controllers.

## Checks
- `dotnet build`, `dotnet test`, `dotnet format --verify-no-changes`, Playwright E2E.

## Gotchas
- Forgetting the uSync export means the change exists only on one machine.

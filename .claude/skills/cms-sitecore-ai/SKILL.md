---
name: cms-sitecore-ai
description: SitecoreAI / XM Cloud headless conventions - Next.js JSS components, SXA, serialization, renderings and datasources. Use on Sitecore projects.
---
# SitecoreAI (XM Cloud) adapter

## Structure
- Front end: Next.js app using the Sitecore Content SDK / JSS in `src/<site>/`.
- Every component = React component + rendering item + datasource template + (optional) rendering parameters template.
- Items live in source control via Sitecore Content Serialization (SCS) modules in `src/items/`.

## Rules
- After creating templates/renderings, serialize: `dotnet sitecore ser pull` and commit the YAML. Validate with `dotnet sitecore ser validate`.
- Components must render in Pages/Experience Editor: handle empty fields with `<Text field={...} />` helpers, never raw values.
- Keep datasource templates minimal; reuse base templates from the project ADR.
- Personalisation and A/B variants are configured, not coded, unless an ADR says otherwise.

## Checks
- `npm run lint`, `npm run build`, Jest for component tests, Playwright E2E against the rendering host.

## Gotchas
- Serialization drift between environments is the #1 failure. Never "fix" items in the CM UI without pulling back to source.
- No API keys in client-side bundles; use server-side fetch for Edge/GraphQL where tokens are needed.

---
name: cms-mach
description: MACH / composable conventions - Next.js front end, headless CMS schema, commerce and search APIs, contract tests. Use on headless or composable projects.
---
# MACH / headless adapter

## Structure
- Front end: Next.js (App Router) or Astro in `apps/web`; shared UI in `packages/ui`.
- Integrations as thin typed clients in `packages/integrations/<service>` (CMS, commerce, search, DAM).
- CMS schema as code where the vendor supports it (Contentful migrations, Storyblok components JSON, Sanity schema).

## Rules
- Every external API behind a typed client with retries, timeouts and a mock for tests.
- Contract tests for each integration (Pact or schema snapshot) so a vendor change fails CI, not production.
- Server-side fetch for anything needing secret tokens. Only public, read-only keys client-side.
- Caching and revalidation strategy per route, documented in the ADR.

## Checks
- `tsc --noEmit`, lint, unit, contract tests, preview deploy (Vercel/Netlify) with Playwright against the preview URL.

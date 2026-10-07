---
name: frontend-builder
description: Phase 3. Builds UI components from Figma frames or a component spec, with Storybook stories and design tokens.
tools: Read, Grep, Glob, Edit, Write, Bash, mcp__figma
model: opus
---
Use design tokens, never hard-coded colours/spacing. Build mobile-first, semantic HTML, keyboard accessible. One Storybook story per state (default, empty, error, long content, RTL if i18n). Follow the CMS adapter's component pattern. Same branch/PR rules as `developer`.

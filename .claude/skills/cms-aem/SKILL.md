---
name: cms-aem
description: Adobe Experience Manager (AEM as a Cloud Service) conventions - Core Components, HTL, Sling Models, OSGi, dispatcher, Cloud Manager gates. Use on AEM projects.
---
# AEM adapter

## Structure
- Maven multi-module archetype: `core` (Sling Models, services), `ui.apps` (components, HTL), `ui.content`, `ui.config` (OSGi), `dispatcher`.
- Extend Core Components via proxy components in `/apps/<project>/components`; do not copy them.

## Rules
- Logic in Sling Models (`@Model(adaptables = SlingHttpServletRequest.class)`), never in HTL.
- OSGi config per run mode in `ui.config/.../osgiconfig/config.<runmode>`.
- Content Fragments + GraphQL for headless use cases per ADR.
- Dispatcher: explicit allow-list filters; test with the dispatcher SDK validator.

## Checks
- `mvn clean install -PautoInstallPackage` locally; unit tests with AEM Mocks (wcm.io).
- Cloud Manager quality gates: code coverage, SonarQube rules, security. Write tests from day one or the pipeline fails.

## Gotchas
- Never write to `/libs`. Mutable vs immutable content: `/apps` is immutable at runtime in AEMaaCS.

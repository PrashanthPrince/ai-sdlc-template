---
name: cms-drupal
description: Drupal 10/11 conventions for agents - modules, themes, config management, Composer, coding standards and tests. Use on any Drupal project.
---
# Drupal adapter

## Structure
- Custom code in `web/modules/custom/<client>_<feature>` and `web/themes/custom/<theme>`.
- Dependencies via Composer only (`composer require drupal/<module>`). Never commit `vendor/` or contrib code.
- Prefer Paragraphs / Layout Builder / SDC (Single Directory Components) per the project ADR.

## Config is code
- Any change made through the UI or API must be exported: `drush cex -y`, and the YAML committed in `config/sync`.
- Never edit config YAML UUIDs by hand. Check `drush config:status` is clean before opening a PR.

## Standards and checks
- `vendor/bin/phpcs --standard=Drupal,DrupalPractice`
- `vendor/bin/phpstan analyse` (level from `phpstan.neon`)
- `vendor/bin/phpunit` for unit/kernel tests; Playwright for E2E.

## Security gotchas
- Always use access checks on routes (`_permission`, `_entity_access`), never `_access: 'TRUE'` for non-public routes.
- Render user input via render arrays / Twig autoescape. No `#markup` with raw input; no `|raw` in Twig.
- Use the Database API with placeholders; never string-concatenate SQL.

## Hosting
- Acquia / Pantheon / Platform.sh: deploy via their pipelines; run `drush updb -y && drush cim -y && drush cr` post-deploy.

# Placeholders — never commit filled values

Replace locally. Empty in git is correct.

## Prices (required tokens for this pack)

Official help: Catalog prices may range from **$5 USD to $500,000 USD**.
That is a platform bound, not a quote. Leave these empty until a human sets them.

```
{{TIER_STARTER_USD}}
{{TIER_STANDARD_USD}}
{{TIER_PREMIUM_USD}}
{{TIER_ADVANCED_USD}}
{{ADDON_FAST_USD}}
{{ADDON_REVISION_USD}}
{{ADDON_EXTRA_WORKFLOW_USD}}
{{ADDON_MIGRATION_PLAN_USD}}
```

`{{TIER_PREMIUM_USD}}` and `{{TIER_ADVANCED_USD}}` are the **same slot**.
Use Premium in this polish. Keep Advanced as an alias so sibling packs
(`earn-upwork-catalog-draft-20260916/`, CU handoff `02-upwork-catalog.md`)
still match.

If a live field will not accept `{{…}}` text: leave the box empty, park
`rate_required`, do not type a guessed number, do not Submit.

## Shared identity / location (do not paste into Catalog as contact)

```
{{FULL_LEGAL_NAME}}
{{DISPLAY_NAME}}
{{EMAIL}}
{{GOOGLE_ACCOUNT_EMAIL}}
{{PASSWORD_DO_NOT_STORE}}
{{COUNTRY}}
{{CITY}}
{{TIMEZONE}}
{{PHONE_E164}}
```

Do not put `{{EMAIL}}`, `{{PHONE_E164}}`, or a website-as-inbox line in
title, tags, tier text, summary, FAQ, or requirements.

## Public URLs (already public; still not Catalog contact methods)

- `{{WEBSITE_URL}}` → `https://yutalab.dev/`
- `{{GITHUB_URL}}` → `https://github.com/rimone0511`
- `{{GITHUB_REPO_AUTOPILOT}}` → `https://github.com/rimone0511/autopilot-log`

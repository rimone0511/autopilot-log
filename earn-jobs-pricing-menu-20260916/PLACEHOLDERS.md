# Placeholders — never commit filled values

Replace locally. Empty in git is correct.

## Price tokens (required for this pack)

These are **not** live prices. Do not invent market rates as facts.
A relative ladder lives in [SKU-MENU-EN.md](SKU-MENU-EN.md) / [SKU-MENU-JA.md](SKU-MENU-JA.md) under **DRAFT SUGGESTION** — rank only.

```
{{PRICE_JPY_SKU_STARTER}}
{{PRICE_JPY_SKU_CLASSIFIER}}
{{PRICE_JPY_SKU_APPROVAL}}
{{PRICE_JPY_SKU_DOCS}}
{{PRICE_USD_SKU_STARTER}}
{{PRICE_USD_SKU_CLASSIFIER}}
{{PRICE_USD_SKU_APPROVAL}}
{{PRICE_USD_SKU_DOCS}}
{{PRICE_JPY_DISPLAY_SKU_STARTER}}
{{PRICE_JPY_DISPLAY_SKU_CLASSIFIER}}
{{PRICE_JPY_DISPLAY_SKU_APPROVAL}}
{{PRICE_JPY_DISPLAY_SKU_DOCS}}
{{PRICE_ADDON_REVISION_JPY}}
{{PRICE_ADDON_REVISION_USD}}
{{PRICE_ADDON_FAST_JPY}}
{{PRICE_ADDON_FAST_USD}}
{{HOURLY_USD}}
{{PRICE_YEN_DRAFT}}
```

| Token family | Desk | Notes |
|---|---|---|
| `{{PRICE_JPY_SKU_*}}` | Coconala price box | Yen. Category floor from official table at click-time. Not a quote. |
| `{{PRICE_USD_SKU_*}}` | Gumroad price box; Contra one-time if used | USD. Gumroad help bound: free or up to USD 5,000. Not a quote. |
| `{{PRICE_JPY_DISPLAY_SKU_*}}` | Gumroad description only | Optional JP display line. Not a second checkout currency unless Gumroad shows it. |
| `{{PRICE_ADDON_*}}` | Coconala 有料オプション / Contra add-on text | Extra revision or faster delivery. Still placeholders. |
| `{{HOURLY_USD}}` | Contra ongoing | Prefer empty or **Contact for pricing** until a human chooses. |
| `{{PRICE_YEN_DRAFT}}` | Coconala 見積もり料金欄 | Same rule as JP proposal packs. Do not send. |

Aliases (same slot, keep both so sibling packs still match):

```
{{PRICE_USD}}          → use the SKU-specific {{PRICE_USD_SKU_*}} for that product
{{PRICE_JPY_DISPLAY}}  → use {{PRICE_JPY_DISPLAY_SKU_*}}
{{TIER_STARTER_USD}}   → not this menu (Upwork Catalog sibling). Do not copy here as a fact.
```

If a live field will not accept `{{…}}` text: leave the box empty, park `rate_required` or `rate_empty`, do not type a guessed number, do not publish.

## Delivery / revision (not prices)

```
{{LEAD_TIME_DRAFT}}
{{LEAD_DAYS_SKU_STARTER}}
{{LEAD_DAYS_SKU_CLASSIFIER}}
{{LEAD_DAYS_SKU_APPROVAL}}
{{LEAD_DAYS_SKU_DOCS}}
{{REVISIONS_SKU_STARTER}}
{{REVISIONS_SKU_CLASSIFIER}}
{{REVISIONS_SKU_APPROVAL}}
{{REVISIONS_SKU_DOCS}}
```

Draft-suggestion **counts** (operator hypothesis for custom desks; not a Coconala/Gumroad/Contra official default):

| SKU | Calendar days (draft suggestion) | Revisions included (draft suggestion) |
|---|---|---|
| starter | 7 | 1 |
| classifier | 7 | 1 |
| approval-gate | 10 | 2 |
| docs | 5 | 1 |

Gumroad digital download does not use these delivery days. Contra / Coconala custom work may. Live form wins.

## Shared identity (do not paste into listings as contact)

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

Do not put `{{EMAIL}}`, `{{PHONE_E164}}`, or a website-as-inbox line in Coconala サービス内容, Gumroad description, or Contra service description.

## Desk-only

```
{{COCONALA_SERVICE_URL_DO_NOT_ANNOUNCE}}
{{GUMROAD_PERMALINK_SKU_STARTER}}
{{GUMROAD_PERMALINK_SKU_CLASSIFIER}}
{{GUMROAD_PERMALINK_SKU_APPROVAL}}
{{GUMROAD_PERMALINK_SKU_DOCS}}
{{CONTRA_SERVICE_URL_DO_NOT_ANNOUNCE}}
{{N8N_BASE_URL}}
{{TABLE_KIND}}
{{TABLE_ID_DO_NOT_COMMIT}}
{{SHEET_NAME}}
{{OPERATOR_NOTIFY_CHANNEL}}
{{PLATFORM_FEE_NOTE}}
{{JOB_TITLE}}
{{SCOPE_ONE_LINER}}
{{QUESTION_1}}
{{QUESTION_2}}
{{PORTFOLIO_URL}}
{{WEBSITE_URL}}
{{GITHUB_REPO_AUTOPILOT}}
```

Suggested public fills (already public; still not a live checkout URL):

- `{{PORTFOLIO_URL}}` / `{{WEBSITE_URL}}` → `https://yutalab.dev/`
- `{{GITHUB_REPO_AUTOPILOT}}` → `https://github.com/rimone0511/autopilot-log`
- `{{DISPLAY_NAME}}` → 石田祐太 / Yuta Ishida

`{{PLATFORM_FEE_NOTE}}`: read the desk’s current fee help immediately before a human publish. Do not freeze a fee percentage in this pack.

Coconala `guide_sell` (fetched 2026-09-16) cites **22%** on トークルーム完了時. That is a cite to re-check, not a number to paste as a forever fact.

Contra independents help (12642699): client payment fees **$15** under $500 and **$29** over $500, waived with Pro. Cite only. **Do not buy Pro** from this pack. Live pricing wins.

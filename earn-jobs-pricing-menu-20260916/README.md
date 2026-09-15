# Seller pricing menu — DRAFT_ONLY (2026-09-16)

Pack: `earn-jobs-pricing-menu-20260916/`  
Seller: Yuta Ishida / 石田祐太 / ユタラボ  
Desks: **Coconala** (JP listing + estimate), **Gumroad** (digital product), **Contra** (Independent / Share work)  
Mode: **DRAFT_ONLY**. Do not publish, enable, submit, or send.

This folder is a bilingual **seller pricing menu** for four SKUs. It is paste text.
It is not a live listing, not a quote, not a market study, and not permission to sell.

## SKUs in this menu

| Code | Short name | What it is (one line) |
|---|---|---|
| `SKU-STARTER` | n8n starter | Form / webhook → table → notify. A person sends. |
| `SKU-CLASSIFIER` | classifier | Inbound text → labels + **uncertain / hold**. No auto-reply. |
| `SKU-APPROVAL` | approval-gate | Human **approve** required before any outbound. Fail closed. |
| `SKU-DOCS` | docs | Operator SOP / runbook for a workflow the buyer already has. No new flow. |

Sibling Gumroad product packs (do not replace; this menu only adds a pricing overlay):

| SKU here | Sibling pack (if present) | PR |
|---|---|---|
| n8n starter | SKU-0 starter intake (form → table → notify). **No product pack on `master`.** Shape only, from SKU-1 text. | QA [#55](https://github.com/rimone0511/autopilot-log/pull/55) |
| classifier | `earn-sku1-n8n-pack-draft-20260916/` | [#37](https://github.com/rimone0511/autopilot-log/pull/37) |
| approval-gate | `earn-sku2-approval-gate-pack-draft-20260916/` | [#46](https://github.com/rimone0511/autopilot-log/pull/46) |
| docs | none — docs-only SKU in this menu | — |

**Not in this menu:** Gumroad SKU-3 Google Sheet sync ([#52](https://github.com/rimone0511/autopilot-log/pull/52)). Do not add it to Coconala / Contra paste from this pack.

## Files

| File | Audience | Purpose |
|---|---|---|
| [SKU-MENU-JA.md](SKU-MENU-JA.md) | Operator + JP paste | JP menu: SKU list, `{{PRICE}}`, include/exclude, revisions |
| [SKU-MENU-EN.md](SKU-MENU-EN.md) | Operator + EN paste | EN menu: same four SKUs |
| [COCONALA-PASTE.md](COCONALA-PASTE.md) | Operator | Coconala listing fields + estimate reply |
| [GUMROAD-PASTE.md](GUMROAD-PASTE.md) | Operator | Gumroad name / summary / price tokens (EN + JA) |
| [CONTRA-PASTE.md](CONTRA-PASTE.md) | Operator | Contra Independent services, unpublished |
| [PLACEHOLDERS.md](PLACEHOLDERS.md) | Operator | Every `{{…}}` token. Empty in git is correct |
| [DRAFT_ONLY.md](DRAFT_ONLY.md) | Operator | No publish / no KYC / no secrets |

## Hard rules

- **DRAFT_ONLY.** Leave Coconala 受付休止 or unpublished, Gumroad unpublished, Contra **Save as unpublished**.
- **No secrets** in these files or in git (no real passwords, API keys, IDs, tax numbers, bank, webhook tokens).
- Prices stay placeholders (`{{PRICE_JPY_SKU_*}}`, `{{PRICE_USD_SKU_*}}`). Do not invent a live quote in git.
- **No invented market rates as facts.** Any relative ladder is a **draft suggestion** — not a comparable, not a going rate, not GMV.
- Do not freeze platform fee percentages. Re-read official help immediately before a human publish.
- No fake n8n / Coconala / Gumroad / Contra / AI-lab partnership badges.
- No income, win-rate, time-saved, or accuracy % claims.
- MAIN Google only (`{{GOOGLE_ACCOUNT_EMAIL}}`).
- Buyer-facing fenced paste does **not** say “unpublished draft” (it must stay valid if a human later publishes). Operator notes outside fences may say DRAFT_ONLY.

## Public help cited (re-check at paste time; live form wins)

| Desk | Topic | URL |
|---|---|---|
| Coconala | 出品ガイド（通常サービス、キャッチコピー 30 字、販売価格 500円〜1,000,000円 ※カテゴリによる、有料オプション最大 10） | https://coconala.com/pages/guide_sell |
| Coconala | タイトル分割（提供内容の説明 最大 25 字・語尾「ます」、キャッチコピー 最大 30 字） | https://coconala.com/news/170 |
| Coconala | 説明文の通常上限（ニュース: 通常 1,000 字。セラーサポート時 1,500 字。本パックは通常枠） | https://coconala.com/news/1220 |
| Coconala | カテゴリごとの最低サービス価格 | https://help.coconala.com/hc/ja/articles/360020963554 |
| Gumroad | Adding a product | https://gumroad.com/help/article/149-adding-a-product |
| Contra | How to add services (one-time / ongoing / Contact for pricing; Save as unpublished) | https://help.contra.com/en/articles/9322412-how-to-add-services-to-your-contra-profile |
| Contra | Fees for independents (re-read; do not buy Pro from this pack) | https://help.contra.com/en/articles/12642699-fees-on-contra-for-independents |
| n8n | Export and import | https://docs.n8n.io/build/manage-workflows/export-and-import/ |

Public seller URLs (already public; still not a live product permalink):

- https://yutalab.dev/
- https://github.com/rimone0511/autopilot-log

## Out of scope

- Logging into Coconala / Gumroad / Contra from this agent
- Filling live yen or USD
- Publish / Enable / 公開 / Submit / 見積もり送信
- KYC, bank, tax, Persona, My Number
- Buying Contra Pro, Gumroad Discover, Coconala ads, Seller Support
- Zipping operator files into a customer download
- Changing Python posting-gate tests

## Counts (this pack)

Python `len()` on fenced paste, 2026-09-16. Placeholders unsubstituted. Live form wins.

| Desk | Tightest cited cap used | Result |
|---|---|---|
| Coconala 提供内容 | 25（news 170） | 16 / 14 / 14 / 14 |
| Coconala キャッチコピー | 30（guide_sell / news 170） | 13 / 12 / 15 / 12 |
| Coconala サービス内容 | 通常 1,000（news 1220） | 454 / 321 / 281 / 303 |
| Gumroad name EN | sibling SKU-1/2 kept 60 | 49 / 60 / 60 / 57 |
| Contra service names | help: straight to the point | 45 / 53 / 50 / 52 |

## Verification

- [x] Folder `earn-jobs-pricing-menu-20260916/` with eight markdown files
- [x] Every price is a `{{PRICE_*}}` token (platform bounds are cited, not quotes)
- [x] Relative ladder labeled **DRAFT SUGGESTION** / 仮説 — not a market fact
- [x] No live emails, phones, passwords, or API keys in paste fences
- [x] Python posting-gate tests unchanged
- [ ] Human: paste locally; do not publish; do not send estimates
- [ ] Do not merge until Yuta reviews; keep draft

Keep draft until Yuta reviews. Do not merge as “listed” or “on sale.”

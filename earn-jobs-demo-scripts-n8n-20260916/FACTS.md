> **Operator fact table. Do not paste this file into a Loom or a chat.**  
> No secrets. No live rates. No real buyer names.

# Pack facts — JOBS n8n demo scripts

These are the only seller facts the three outlines may lean on. If a fact is not here, do not invent it on camera.

## Seller (public)

| key | value in this repo |
|---|---|
| display_name | `{{DISPLAY_NAME}}` — recommended Yuta Ishida / 石田祐太 |
| location | Japan; do not spoof US/EU |
| timezone | `{{TIMEZONE}}` — local ledger example: `JST` |
| languages | Japanese and English (async) |
| public_site | https://yutalab.dev/ |
| public_github | https://github.com/rimone0511 |
| public_tool | https://github.com/rimone0511/autopilot-log |

Do not say a legal name, login mailbox, phone, or “text me at…” on camera.

## Offer (honest, no badges)

| demo | what it is | what it is not |
|---|---|---|
| 01 form → sheet → notify | One inbound form becomes a row a person can see; a ping is a **hold**, not a send | Browser bots, live list-mail, partner-badge impersonation |
| 02 lead classify | Tags the buyer already uses + an **uncertain** bucket a person reviews | Auto-reply, scraped lists, fake accuracy % |
| 03 approval gate | A draft sits until a person says `approve`; reject / missing / timeout **fail closed** | Auto-send-on-timeout, SLA, live outbound |

Work after a contract still uses **official APIs / documented n8n connectors** only. The buyer’s n8n, the buyer’s credentials.

## Related drafts (do not copy bodies here)

| sibling folder | role |
|---|---|
| `earn-sku1-n8n-pack-draft-20260916/` | Gumroad SKU-1 classifier zip (unpublished) |
| `earn-sku2-approval-gate-pack-draft-20260916/` | Gumroad SKU-2 approval-gate zip (unpublished) |
| `earn-sku3-sheet-sync-pack-draft-20260916/` | Gumroad SKU-3 sheet-sync zip (unpublished) |
| `earn-en-proposal-wave2-20260916/` | EN marketplace cover letters (DO NOT SEND) |
| `earn-jp-proposal-wave2-20260916/` | JP marketplace proposals (送信禁止) |

SKU-0 (starter intake: form → table → notify) is the **shape** of demo 01. A full SKU-0 zip is not in this repository. Do not invent a Gumroad URL for it.

## Placeholders (local ledger only)

| token | on camera? |
|---|---|
| `{{DISPLAY_NAME}}` | yes |
| `{{ONE_SPECIFIC_DETAIL}}` | yes — rewrite per conversation |
| `{{TIMEZONE}}` | yes if asked |
| `{{PORTFOLIO_URL}}` | spoken or end card only; public site |
| `{{GITHUB_REPO_AUTOPILOT}}` | spoken or end card only; public repo |
| `{{CLIENT_LABEL}}` | fact table only (`Client A` …) |
| `{{HOURLY_RATE_USD}}` `{{PRICE_YEN_DRAFT}}` | **never** in the script |
| `{{LOOM_URL_DO_NOT_COMMIT}}` | **never** in git |
| `{{N8N_BASE_URL}}` `{{WEBHOOK_PATH_*}}` | crop / blur; do not read aloud |
| `{{GOOGLE_SHEET_ID_DO_NOT_COMMIT}}` | **never** |

## Fictional props in this pack (not real)

- Sheet tab: `EXAMPLE-ONLY`
- Senders: `example-sender`, `example-operator`
- Rows: “office closed tomorrow”, “What time do you answer email?”
- Labels: `Client A` / `依頼者A` (demo 01), `Client B` / `依頼者B` (demo 02), `Client C` / `依頼者C` (demo 03)

Do not replace these with live buyer names, company names, or production sheet IDs in git.

## Explicit non-facts (do not say)

- Client counts, years in business, GMV, hours saved, close rate
- “n8n Expert”, “n8n Partner”, “Top Rated”, lab affiliation
- A guaranteed price or delivery SLA
- That this PR recorded, uploaded, or booked a call
- That Autopilot Log posts TikTok unattended (inbox upload is the default)
- Accuracy % for classification
- “Timeout counts as approve”

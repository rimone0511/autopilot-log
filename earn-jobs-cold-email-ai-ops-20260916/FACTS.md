> **Operator fact table. Do not paste this file into an email.**  
> No secrets. No live rates. No real recipient names or mailboxes.  
> If a claim is not in this table, do not invent it in a draft.

# Pack facts — cold email AI ops / n8n (SMBs)

These are the only seller facts the ten drafts may lean on.

## Seller (public)

| key | value in this repo |
|---|---|
| display_name | `{{DISPLAY_NAME}}` — recommended Yuta Ishida / 石田祐太 |
| legal_name | `{{FULL_LEGAL_NAME}}` — footer / From identity; never a fake US/EU firm |
| location | Japan; city `{{CITY}}`, country `{{COUNTRY}}` — do not spoof US/EU |
| timezone | `{{TIMEZONE}}` — example local ledger: `JST` |
| languages | Japanese and English (async) |
| public_site | https://yutalab.dev/ |
| public_github | https://github.com/rimone0511 |
| public_tool | https://github.com/rimone0511/autopilot-log |
| postal_address | `{{POSTAL_ADDRESS}}` — **required in a real commercial footer; never invent a street in git** |
| sender_mailbox | `{{SENDER_EMAIL}}` — From / Reply-To; login mailbox is **not** committed |
| opt_out_contact | `{{OPT_OUT_CONTACT}}` — usually the same as From; placeholder only |
| independent | yes — not an n8n / Zapier / Make / xAI / OpenAI partner or employee |

Do not commit filled `{{SENDER_EMAIL}}`, `{{POSTAL_ADDRESS}}`, phone, OTP, or passwords.

## Offer (honest, no badges, no case-study metrics)

| theme | what it is | what it is not |
|---|---|---|
| n8n workflow | Official APIs / documented connectors in the **client** workspace + operator notes a second person can rerun + a human stop before send/publish | Browser bots, unofficial scrapers, partner-badge impersonation, n8n hosting |
| AI ops | Brief → draft → inspect → **human** approve before send or publish | Fully autonomous outbound, invented citations, KYC-by-proxy |
| lead classify | Tags + route + **unsure** bucket a person reviews | Auto-reply, auto-invoice, scraped lists, fake intent scores |

Work stays a scoped freelance setup. Keys stay in the client’s n8n. This pack does not send customer mail for the buyer.

## Public tool facts (Autopilot Log — cite, do not inflate)

From the public README of https://github.com/rimone0511/autopilot-log (this repository):

| claim allowed | claim forbidden |
|---|---|
| Unattended **YouTube** upload through YouTube Data API v3 after one human consent click per channel | That every upload is a published video (unaudited API projects stay **private**) |
| TikTok default is **inbox upload**; the operator reviews and posts in the TikTok app | That TikTok posting in this repo is unattended by default |
| Direct TikTok post is a separate command, fail-closed behind a posting-gate file | That the gate is open, or that an unaudited client can bypass `SELF_ONLY` |
| Missing / malformed gate → private-only / refuse non-private | That “the automation is running” means “it may publish” |
| Secrets are not printed or logged; no browser automation, no scraping, no like/follow/view bots | That the tool is a growth bot or a LinkedIn/email sender |

This is a **public repo habit**, not a client case study. Do not attach fake “hours saved” or “N studios live.”

## n8n facts (product, not partnership)

| allowed | forbidden |
|---|---|
| Client-owned Cloud or self-hosted n8n | “Official n8n Expert / Partner” unless a live badge exists (it is not in this pack) |
| Documented nodes / first-party webhooks / official APIs | Browser automation of sites with no API |
| Workflows imported **inactive**; human turns them on | Agent or seller remotely enabling production send |
| Dummy payload before production | Guaranteed classification accuracy |

n8n import docs (re-check live): https://docs.n8n.io/build/manage-workflows/export-and-import/

## Placeholders (local ledger only)

| token | in fenced email body? |
|---|---|
| `{{DISPLAY_NAME}}` | yes |
| `{{ONE_SPECIFIC_DETAIL}}` | **required** — from **this** public page |
| `{{RECIPIENT_NAME}}` / `{{RECIPIENT_ROLE}}` | yes, from the public page; skip if unknown |
| `{{PUBLIC_PAGE_KIND}}` | yes (contact page, help, booking, about) |
| `{{SMB_LABEL}}` | fact table only (fictional `SMB-A` … `SMB-J`) |
| `{{RECIPIENT_EMAIL}}` | **headers / operator table only** — never commit a live mailbox |
| `{{QUESTION_1}}` | yes |
| `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}` | yes |
| `{{TIMEZONE}}` `{{CITY}}` `{{COUNTRY}}` | yes |
| `{{POSTAL_ADDRESS}}` `{{OPT_OUT_CONTACT}}` | footer only; placeholders in git |
| `{{SENDER_EMAIL}}` | From header, not a second pitch in the body |
| `{{HOURLY_RATE_USD}}` `{{PRICE_YEN_DRAFT}}` | **never** in prose |
| `{{PHONE_E164}}` | **never** |

## Fictional SMBs in this pack (not real)

`SMB-A` … `SMB-J`. Do not replace these with live company names, domains, or mailboxes in git.

## Explicit non-facts (do not write)

- Client counts, years in business, revenue, GMV, “hours saved”, open rates, reply rates, win rates
- Named case studies with metrics (even “anonymized 40%”)
- “n8n Expert”, “Zapier Partner”, “Top Rated”, xAI / OpenAI staff
- A US/EU HQ or a fake LLC
- That an agent will send, publish, or take payment without a human stop
- That this PR sent mail, warmed a domain, or measured demand
- Legal advice (“Art. 3(1)(iv) always covers this address”)

> **Operator fact table. Do not paste this file into LinkedIn.**  
> No secrets. No live rates. No real recipient names.

# Pack facts — LinkedIn outreach Wave 2

These are the only seller facts the twelve drafts may lean on. If a fact is not in this table, do not invent it in a note or a proposal.

## Seller (public)

| key | value in this repo |
|---|---|
| display_name | `{{DISPLAY_NAME}}` — recommended Yuta Ishida / 石田祐太 |
| legal_name | `{{FULL_LEGAL_NAME}}` — never in a connection note |
| location | Japan; city `{{CITY}}`, country `{{COUNTRY}}` — do not spoof US/EU |
| timezone | `{{TIMEZONE}}` — example local ledger: `JST` |
| languages | Japanese and English (async) |
| public_site | https://yutalab.dev/ |
| public_github | https://github.com/rimone0511 |
| public_tool | https://github.com/rimone0511/autopilot-log |
| linkedin_account | existing personal profile on MAIN Google (`{{GOOGLE_ACCOUNT_EMAIL}}` for **login only**) |
| linkedin_product | Services on a **personal** profile, if it already exists; not Jobs; not a Company Page |

Do not commit filled `{{GOOGLE_ACCOUNT_EMAIL}}`, phone, OTP, or passwords. Do not put the login mailbox in a connection note or a proposal.

## Offer (honest, no badges)

| theme | what it is | what it is not |
|---|---|---|
| n8n workflow | Official APIs / documented connectors + operator notes a second person can rerun + a human stop before send/publish | Browser bots, unofficial scrapers, partner-badge impersonation |
| AI ops | Brief → draft → inspect → human approve before send or publish | Fully autonomous outbound, invented citations, KYC-by-proxy |
| lead classify | Tags + route + **unsure** bucket a person reviews | Auto-spam sequences, scraped lists, fake intent scores |

Work stays on LinkedIn Messages / Services admin until a contract exists. LinkedIn Help notes that providers and clients may later finalize terms off-platform; **this pack still does not put email, phone, or WhatsApp in the first paste.**

## LinkedIn limits used as facts (re-check live)

| fact | value used here | source |
|---|---|---|
| Basic connection note | 200 characters | [a563153](https://www.linkedin.com/help/linkedin/answer/a563153) |
| Basic personalized notes / month | 3 (older page: 5; live composer wins) | same |
| InMail | 200 / 1900 — **not used** | [a411986](https://www.linkedin.com/help/linkedin/answer/a411986) |
| Services RFP contact info | requester must not include phone/email in the request; discuss on LinkedIn | [a798014](https://www.linkedin.com/help/linkedin/answer/a798014) |
| Save on a personal Service Page | official help: Save makes the page **viewable** | sibling CU pack + [a569554](https://www.linkedin.com/help/linkedin/answer/a569554) |

Unverified third-party figures (About ≈500, DM ≈8000, Premium note ≈300) are **not** treated as facts. Live counter wins.

## Placeholders (local ledger only)

| token | in connection note? | in Services paste? |
|---|---|---|
| `{{DISPLAY_NAME}}` | yes | yes |
| `{{ONE_SPECIFIC_DETAIL}}` | **required** | **required** |
| `{{RECIPIENT_LABEL}}` | fact table only (fictional) | fact table only |
| `{{ROLE_OR_HEADLINE}}` | optional, if it fits 200 | optional |
| `{{SERVICE_REQUEST_SUMMARY}}` | no | fact table / first line |
| `{{QUESTION_1}}` `{{QUESTION_2}}` | no (no room) | yes, Services only |
| `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}` | **no** (notes reject / look like spam) | yes |
| `{{TIMEZONE}}` `{{CITY}}` `{{COUNTRY}}` | city/country only if room; usually “Japan” | yes |
| `{{HOURLY_RATE_USD}}` `{{FIXED_PRICE_USD}}` `{{PRICE_YEN_DRAFT}}` | **never** | form fields only |
| `{{LEAD_TIME_DRAFT}}` | never | form fields only |
| `{{EMAIL}}` `{{PHONE_E164}}` | **never** | **never** |

## Fictional people in this pack (not real)

Connection examples: `Person A` … `Person F`.  
Services examples: `Request G` … `Request L`.

Do not replace these with live profile URLs, company names, or member IDs in git.

## Explicit non-facts (do not write)

- Client counts, years in business, revenue, hours saved
- “n8n Expert”, “Top Rated”, “OpenAI partner”, xAI staff
- A guaranteed hourly shown as a quote (LinkedIn starting hourly is a minimum shown to buyers, not a guarantee — sibling Services pack uses **Contact for pricing**)
- That this PR sent, published, or measured demand (“N buyers in your area”)

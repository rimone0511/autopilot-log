# Upwork Catalog 3-tier polish — DRAFT_ONLY

Pack date: 2026-09-16
Desk: Upwork Project Catalog
Seller: Yuta Ishida / 石田祐太
Offer: n8n automation + operator docs
Language: English buyer-facing paste
Mode: **DRAFT_ONLY**. Do **not** Submit. Do **not** publish.

This folder polishes the **Pricing and scope** paste for an unpublished
three-tier Catalog project. It is not a live listing, not a review
submission, and not an identity file.

Sibling bodies (do not replace unless this pack says so):

| Pack | Role |
|---|---|
| `earn-upwork-catalog-draft-20260916/` | Original Catalog draft (title, tags, 800-word overview, Starter / Standard / **Advanced**) |
| `earn-upwork-linkedin-cu-handoff-20260916/02-upwork-catalog.md` | CU field map of the same Catalog copy |
| `earn-fiverr-gig-draft-20260916/` | Fiverr packages Basic / Standard / Premium (same offer, different desk) |

Buyer-facing paste in this folder uses **Starter / Standard / Premium**.
Upwork public help names the three package columns **Starter, Standard,
Advanced**. If the live form says Advanced, paste the Premium column there.
See [TIERS-PASTE.md](TIERS-PASTE.md).

## Files

| File | What it is |
|---|---|
| [TIERS-PASTE.md](TIERS-PASTE.md) | Package titles, descriptions, matrix, add-ons, price placeholders |
| [SUPPORTING-PASTE.md](SUPPORTING-PASTE.md) | Title recap, 800-character summary, workroom steps, FAQ, requirements |
| [PLACEHOLDERS.md](PLACEHOLDERS.md) | `{{…}}` tokens only — never fill in git |
| [DRAFT_ONLY.md](DRAFT_ONLY.md) | Stop list: no Submit, no KYC upload, no Connects, no secrets |

## Hard rules

- No secrets in these files or in git (no real passwords, API keys, IDs, tax numbers).
- Prices stay placeholders. Do not invent USD. Official help range is **$5 to $500,000 USD**; that is a bound, not a quote.
- If the create form requires a number to proceed and placeholders are empty: fill the **text** fields, park `rate_required`, **do not Submit**.
- Do not buy Connects, boosts, or the identity badge from this pack.
- Do not put phone, email, or off-platform payment in any Catalog box.
- Buyer-facing paste does not mention draft status (it must stay valid if a human later publishes).
- Cite **public help / public resources only**. No third-party “fill these boxes” blogs as facts.

## Public help cited (2026-09-16)

Re-check at click-time. Live form wins.

| Topic | URL |
|---|---|
| Create a project (tiers named Starter / Standard / Advanced; $5–$500,000; add-ons; delivery days; revisions; Submit → review) | https://support.upwork.com/hc/en-us/articles/360057397533-Create-a-project |
| How to create a project (title after “You will get”, max 75; one or three tiers; calendar days; gallery logo rules; requirements types; 48-hour cancel; finalize) | https://www.upwork.com/resources/how-to-create-project-catalog-service |
| Project summary length (longer than 120 characters, up to 1,200) | https://www.upwork.com/resources/catalog-product-description |
| Best-project tips | https://support.upwork.com/hc/en-us/articles/360058122033-How-to-build-your-best-project-in-Project-Catalog |
| Review process | https://support.upwork.com/hc/en-us/articles/4408644453395-How-we-review-your-Project-Catalog-project |
| Images / video (no contact info, no logos other than yours, no other-company marks) | https://support.upwork.com/hc/en-us/articles/1500011309082-How-to-add-images-and-video-to-your-Project-Catalog-project |
| Freelancer Catalog intro | https://support.upwork.com/hc/en-us/articles/360058234233-How-to-get-started-with-Project-Catalog-as-a-freelancer |

Home / Catalog (product still treated as alive; browse from this environment may hit a verification wall):

- https://www.upwork.com/
- https://www.upwork.com/catalog

## Counts (this pack)

Measured with Python `len()` on fenced paste (spaces count; fences do not).
Placeholder tokens count as written (`{{TIER_STARTER_USD}}` is 20 characters).

| Block | This pack | Rule |
|---|---|---|
| Title after “You will get” | 58 | ≤ 75 (resources) |
| Catalog summary | 800 | 121–1,200 (resources: longer than 120, max 1,200) |
| Package titles | 39 / 47 / 43 | keep short; live form wins |
| Starter / Standard / Premium descriptions | 651 / 517 / 557 | no official ceiling in cited help; stay scannable |
| Tiers | 3 | help: one **or** three; this pack is three |
| Search tags | 5 | help: up to five, standardized list |

## Out of scope

- Logging into Upwork from this agent
- Filling live USD prices
- Gallery uploads, KYC, tax, payout
- Boost / Connects / proposals
- Clicking **Submit** (review queue = publish path)

Keep draft until Yuta reviews. Do not merge as “listed.”

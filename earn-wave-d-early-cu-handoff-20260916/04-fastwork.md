> DRAFT_ONLY paste pack. NO secrets. NO marketplace login from this authoring PR. NO publish.
> Public start-selling page: register with **ID and bank**. If that form appears, STOP (`kyc_wait`). Do not upload.
> Online AI automation category only. Face-to-face TH services: do not touch.
> Seller commission % unread — do not invent. Starting prices on category cards are not GMV.

# PACK — Fastwork — this-folder play 4

| Key | Value |
|---|---|
| inventory | 04 |
| cu_serial | **unindexed** |
| queue | D6 Wave D (TH/SEA marketplace; automation packs fit; JP clients unproven — do not invent) |
| activity_gate | **alive** (PR#22 + this GET: `/en/ai-automation` n8n / make.com) |
| self_serve | mixed — “Sign up as a freelancer” is public; **ID + bank at register** per start-selling copy |
| cu_ready | true (pack exists. **not registered**) |
| official | https://fastwork.co/en |
| start_selling | https://fastwork.co/en/start-selling |
| ai_category | https://fastwork.co/en/ai-automation |
| signup_legacy | https://fastwork.co/en/signup → **404** this GET (SPA; not dead) |
| login_legacy | https://fastwork.co/en/login → **404** this GET |
| how | https://static.fastwork.co/contents/how |
| google_signup_preference | **needs_check** (start-selling Sign Up button `disabled` in this HTML; no Continue-with-Google label) |
| worker_fee_public | **unknown**. Identity-before-hire copy only. Do not treat BYOB “0% commission” marketing as the seller fee table |
| paid | **NO** (Specialist / boosts / BYOB paid) |
| stop_at_kyc | **STOP** (ID + bank at register; pre-hire identity) |
| draft | true |
| observed | 2026-09-16 public GET |

Start-selling visible steps (this GET):

1. Sign Up as a Freelancer — “Register with your ID and bank details for verification. Post your services immediately.”
2. Post Your Services — team approval within 48 hours (**publish path — do not**).
3–6. Seller Center / work / review / payout.

Home also: “Freelancers verify their identity in the system before hiring begins.”

## needs_check

- Google / LINE / Facebook / email buttons after the Sign Up control hydrates.
- Whether any account can exist **without** ID+bank. **Do not pay or upload to find out.** If the next required fields are ID or bank → `kyc_wait`.
- Seller fee %. Terms URL this GET returned an empty static body.

## CU handoff

1. Open https://fastwork.co/en/start-selling (English). Do not use `/en/signup` (404).
2. Freelancer, not buyer.
3. If **Google** is visible → MAIN account. Else MAIN mailbox email. Do not create LINE/Facebook just for this desk.
4. As soon as **national ID, book bank, selfie-for-ID, or “verification to post”** appears: close. Code `kyc_wait`. Hand desk + screen to morning.
5. Do **not** post a service (48h approval = listing submit).
6. Do **not** open massage / housekeeping / on-site categories even if the catalog mixes them.
7. Keep the service copy below in git only.

If the session is identity-locked, skip to 99freelas only after closing Fastwork tabs.

## Field map (placeholders) — use only if a non-KYC draft profile exists

### Account

| UI field | Paste | Notes |
|---|---|---|
| Intent | Freelancer / start selling | Not hire. |
| Google | `{{GOOGLE_ACCOUNT_EMAIL}}` if present | `needs_check`. |
| Email | `{{EMAIL}}` | MAIN mailbox. |
| Password | `{{PASSWORD_DO_NOT_STORE}}` | |
| Display name | `{{DISPLAY_NAME}}` | |
| National ID / bank | **do not fill** | STOP. |
| Location | `{{CITY}}, {{COUNTRY}}` | Honest JP OK. Do not fake TH. |

### Service draft (do not submit)

Keep this text in the pack. Do not click Post / Submit for review.

| UI field | Paste | Notes |
|---|---|---|
| Category | AI Automation / n8n / make.com if still listed | Online only. |
| Title | `n8n / make.com automation plus operator docs` | English or Thai UI — paste English unless the form forbids it. |
| Description | Service paste below | |
| Starting price | `{{STARTING_BUDGET_USD}}` or leave | Do not invent THB. `rate_required` if mandatory. |
| Portfolio | `{{PORTFOLIO_URL}}` | |

### Service description paste (not posted)

```
I design, build, and document n8n (or make.com) workflows so operators can run them without me.

Typical work:
- Map the current manual process
- Build the workflow (triggers, APIs, error handling)
- Hand over a short operator guide (what breaks, how to rerun, where secrets live)

I do not scrape platforms that have no official API, and I do not ship unpublished social posts.

Starting at {{STARTING_BUDGET_USD}}. I stay on Fastwork chat and files.
```

## EN bios

### Short

```
n8n / make.com automation with operator docs. Remote. I do not take work off Fastwork.
```

### Long

```
I set up n8n or make.com workflows and write the instructions your team actually uses.

Typical first pack: one production workflow, retries, a failure alert, and a short SOP. Based in {{CITY}}, {{COUNTRY}}, timezone {{TIMEZONE}}. Working language: English. Japanese notes on request.

I do not automate likes/follows, scrape closed APIs, or complete identity uploads from a CU session.
```

## STOP

Allowed: open start-selling; Google/email **until** ID/bank.

Do NOT: ID, bank, selfie, post services, Specialist paywall, face-to-face gigs, invent commission %.

## Activity note

PR#22 **alive** (AI automation category). Signup URL remains SPA 404; entry is `/en/start-selling`. `thin_site_skip: false`. Likely outcome of a later CU: `kyc_at_signup` / `kyc_wait`.

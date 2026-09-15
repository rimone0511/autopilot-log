> **DRAFT_ONLY.** No signup. No secrets. No KYC upload. No 応募 / proposal / Catalog Submit / LinkedIn Save-if-viewable / X post / bid spray.  
> This folder **mirrors** the 10 SWE-2 High wave5 prompt goals as thick deliverable drafts on `autopilot-log`.  
> Sibling PRs remain the original bake; this pack is the wave5 **mirror** (verify notes + Devin queue + self-contained paste).  
> Mirror-bake date: **2026-09-16**. Agent did **not** create marketplace accounts.

# SWE-2 High wave5 — mirror bake (2026-09-16)

Folder: `earn-swe2-wave5-mirror-bake-20260916/`

This pack is markdown only. It does not change YouTube/TikTok posting-gate code. It is **not** an applied production bake for ORCH / CLI / GrokBOT desired-state.

## The 10 goals

| # | Goal (wave5 prompt) | This folder | Sibling PR (source bake) | Live Devin? |
|---|---|---|---|---|
| 01 | CW fieldmap **verify notes** | [01-cw-fieldmap-verify-notes/](01-cw-fieldmap-verify-notes/) | [#32](https://github.com/rimone0511/autopilot-log/pull/32) | **Yes** — post-email member wizard + worker editor are login-gated |
| 02 | Upwork catalog **verify** | [02-upwork-catalog-verify/](02-upwork-catalog-verify/) | [#10](https://github.com/rimone0511/autopilot-log/pull/10) · CU paste also [#16](https://github.com/rimone0511/autopilot-log/pull/16) | **Yes** — www.upwork.com and Help returned **403** here; picker labels unproven |
| 03 | LinkedIn Services | [03-linkedin-services/](03-linkedin-services/) | [#16](https://github.com/rimone0511/autopilot-log/pull/16) | **Yes** — personal Service Page editor + unpublished-draft control |
| 04 | TT / Contra / Craudia **STOP** | [04-tt-contra-craudia-stop/](04-tt-contra-craudia-stop/) | [#18](https://github.com/rimone0511/autopilot-log/pull/18) | **Yes** — ticket / Independent / worker profile drafts. KYC = morning human, not Devin |
| 05 | Freelancer notes | [05-freelancer-notes/](05-freelancer-notes/) | [#19](https://github.com/rimone0511/autopilot-log/pull/19) | **Yes** — profile editor. **No bids** unless a later human GO |
| 06 | WaveB JP | [06-waveb-jp/](06-waveb-jp/) | [#12](https://github.com/rimone0511/autopilot-log/pull/12) | **Yes** — 8 desks still `needs_check` (SPA / WAF / login) |
| 07 | world keywords | [07-world-keywords/](07-world-keywords/) | [#25](https://github.com/rimone0511/autopilot-log/pull/25) | **Partial** — Fiverr/Upwork hubs 403; Freelancer `/jobs/n8n` public 200 |
| 08 | X rubric | [08-x-rubric/](08-x-rubric/) | [#27](https://github.com/rimone0511/autopilot-log/pull/27) | **Human Latest paste**, not Devin CU. This agent makes **no** X API calls |
| 09 | parallel-cap bake from **adaptive Pro rules** | [09-parallel-cap-bake/](09-parallel-cap-bake/) | [#23](https://github.com/rimone0511/autopilot-log/pull/23) | **No Devin.** Live **observation** of shared cap still `{{UNKNOWN}}`. Do not bake 10/10 max |
| 10 | grok-head bake **placeholders** | [10-grok-head-bake-placeholders/](10-grok-head-bake-placeholders/) | [#26](https://github.com/rimone0511/autopilot-log/pull/26) | **No Devin.** Blocked on Pro reply. `{{PRO_RULE}}` stays |

Consolidated queue: [LIVE-DEVIN-STILL-NEEDED.md](LIVE-DEVIN-STILL-NEEDED.md)  
Public GET log for this bake: [MIRROR-LIVECHECK.md](MIRROR-LIVECHECK.md)  
Shared tokens: [01-cw-fieldmap-verify-notes/PLACEHOLDERS.md](01-cw-fieldmap-verify-notes/PLACEHOLDERS.md)

## Hard rules (all 10)

- **MAIN Google only** (`{{GOOGLE_ACCOUNT_EMAIL}}`). Do not create a second mailbox or a second LinkedIn.
- **DRAFT_ONLY.** Saving an unpublished profile/ticket is the ceiling. Catalog **Submit**, LinkedIn **Save** when help says Save = viewable, TimeTicket 発行完了, Freelancer bids, X replies: **stop**.
- **No secrets.** No live email/phone/OTP/password/ID/bank/tax in git. Placeholders only.
- **No invented rates, fees, GMV, or job counts.** Empty `{{HOURLY_USD}}` / `{{TIER_*_USD}}`. Fee pages are cited, not copied as a payment plan.
- **Stop KYC.** Identity / liveness / My Number / Persona / selfie / payout = morning operator. Devin confirms the **label** then closes.
- **Fail-closed.** Unread live form → `needs_check`. Screen wins over this pack.

## What “mirror” means

1. The original wave5 prompts already have sibling draft PRs (Grok HANDS, 2026-09-16).
2. This pack **copies the thick paste/source into one folder** so a reviewer does not have to open ten branches.
3. It **re-ran public GET** on cited URLs from this environment and wrote verify notes.
4. It **does not** claim those sibling PRs are “registered” or “applied.”
5. It **marks** every desk that still needs a logged-in Computer-Use (Devin) pass.

## Out of scope

- Account create / OTP complete / Google OAuth start
- Marketplace publish, proposals, Connects purchase, wallet fund
- X API, posting, likes, follows, DMs
- Constitution / CLI COMMON / GrokBOT desired-state production APPLY
- Filling `{{PRO_RULE}}` or replacing `{{UNKNOWN}}` with 10/10
- Changing `tests/test_gate.py` / `tests/test_tiktok_gate.py`

## Verification (this PR)

- Markdown under this folder only.
- Catalog overview fence = **800 words**. Catalog summary fence = **800 characters**. LinkedIn About fence = **362 characters**.
- Grok-head `{{PRO_RULE}}` count in COMMON + WINDOW + CHECKLIST = **20** (placeholders not invented-away).
- Parallel-cap tokens remain `{{UNKNOWN}}` / `{{ADAPTIVE}}` / `{{LEGACY_UNVERIFIED}}`. CU = **1 always**.
- Existing Python posting-gate tests unchanged.

Keep draft until Yuta reviews. Do not merge as “registered” or “baked to production.”

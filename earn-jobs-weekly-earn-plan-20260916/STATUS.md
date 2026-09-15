# STATUS — four `draft_saved` desks (JOBS week 2026-09-16)

Snapshot: **2026-09-16** (plan pack; not a new live CU unless noted)  
Folder: `earn-jobs-weekly-earn-plan-20260916/`  
State: **DRAFT_ONLY**

Forbidden here: secrets, live emails / phones / OTP, KYC files, invented permalinks, GMV, “will earn ¥…”.

This STATUS is the inventory for **this week’s earn calendar**. It does not rewrite sibling folders.

---

## Desk table

| Desk | CU / QUEUE | Hint used this week | What is already parked | Missing in git (do not invent) | Next CU serial |
|---|---|---|---|---|---|
| ココナラ Coconala | A1 · QUEUE `done-draft` | `draft_saved` | MAIN Google login confirmed 2026-09-16 JST. Profile / listing left unpublished ([#1](https://github.com/rimone0511/autopilot-log/pull/1) [#43](https://github.com/rimone0511/autopilot-log/pull/43) [#54](https://github.com/rimone0511/autopilot-log/pull/54)) | **Listing body pack** (サービス内容 1000字). Estimate pastes exist; they are not the listing. No live service URL in git | Not this week. Do not reopen to publish without GO |
| Gumroad SKU-0 | A+ · QUEUE `done-draft` · does not occupy CU-11 | `draft_saved` | Desk login `done-draft`. SKU-0 **shape**: starter intake, form → table → notify, unpublished ([#55](https://github.com/rimone0511/autopilot-log/pull/55) [#63](https://github.com/rimone0511/autopilot-log/pull/63)) | **SKU-0 product pack** (`earn-sku0-*` / `ops/earn/sku-0*`). INDEX placeholder `earn-packs/gumroad/` missing. No `gumroad.com/l/...`. Live look-pass **not run** from those QA agents | Not this week as register CU |
| Contra Independent | CU-08 / A8 | `draft_saved` **live** 2026-09-16 ([#64](https://github.com/rimone0511/autopilot-log/pull/64)) | MAIN Google. **Free** plan. Name / one-liner / bio / topics **saved**. About profile **reached**. Location **Kent, USA** (Japan change = identity verification → intentional stop). No Persona, no wallet, no publish, no apply | Do not invent `contra.com/@…`. Rate not recorded. Wallet not opened | Sibling next CU is Craudia — **out of this JOBS week** |
| LinkedIn **profile** | A6 surface (same account as Services) | `draft_saved` **this JOBS week** (operator-named in-scope desk) | Existing personal LinkedIn only. Services paste pack exists ([#16](https://github.com/rimone0511/autopilot-log/pull/16)). Outreach pastes exist ([#38](https://github.com/rimone0511/autopilot-log/pull/38)). Neither pack sent or Saved-as-viewable | **No dedicated headline/About profile paste pack** in git. Do not invent one. No profile URL in git | Register live boxes still listed login `blocked_skip` **reCAPTCHA** ([#49](https://github.com/rimone0511/autopilot-log/pull/49) [#54](https://github.com/rimone0511/autopilot-log/pull/54)). If the box appears: human. Image puzzle = human. Do not make a second LinkedIn |

Hint meanings in this folder:

| Hint | Meaning here |
|---|---|
| `draft_saved` | Unpublished / saved fields exist. Do not treat as live inventory. |
| `kyc_wait` | Optional morning ID **only** if a payout, NDA, or (Contra) Japan-location screen is already in the way. Not required to keep the draft. |
| `blocked_skip` | **Not** a fourth earn desk this week. Sibling skip reasons stay skipped (Fiverr hold, Lancers captcha, CW 403, Upwork Google block, TimeTicket DOB). |
| `pending` | Other Wave A desks. Out of scope. |

---

## LinkedIn: profile vs Services vs login box

This week’s in-scope desk is **LinkedIn profile**, as named in the JOBS prompt.

- **Profile** (headline / About / experience already on the account): look-don't-publish. There is no in-repo profile paste to dump. Do not write a new headline into git.
- **Services** (personal Service Page): sibling A6 pack. Official help: **Save can make the page viewable**. If there is no unpublished control, record `no_draft_path` and do not Save. That click is a **human GO**, not Day-5 “draft work”.
- **Login reCAPTCHA**: sibling Wave A boxes marked skip. [PR#53](https://github.com/rimone0511/autopilot-log/pull/53) allows checkbox/Press&Hold try-first for **register CU**, not this earn calendar. From this folder: parent operator handles the box; **do not click image tiles from an agent**; do not open a second account.

This STATUS does **not** claim a new live LinkedIn CU ran. It does not override #54’s skip log for Fiverr / Lancers / CrowdWorks / Upwork / TimeTicket.

---

## What this week will not pretend exists

| Missing | Do not |
|---|---|
| Coconala listing 1000-word pack | Invent サービス内容 and call it “ready to 公開する” |
| Gumroad SKU-0 listing paste / buyer zip / cover files | Click **New product** to fill the gap |
| Filled `{{PRICE_USD_SKU0}}` / `{{PRICE_YEN_DRAFT}}` | Commit yen or USD |
| Live product / profile / service URLs | Write `coconala.com/services/…`, `gumroad.com/l/…`, `contra.com/@…`, `linkedin.com/in/…` |
| Look-pass ticks from this agent | Claim title/price/icons/files were inspected here |
| Revenue | Write last-week sales, expected GMV, or “Day 7 cash” |

---

## Auth / plan / KYC (secret-free)

```
auth: MAIN Google
second_account: no
coconala: draft_saved (listing unpublished)
gumroad_sku0: draft_saved (unpublished; product pack missing in git)
contra: draft_saved (free; Kent USA leftover intentional)
contra_pro: no
linkedin_profile: draft_saved (this JOBS week; no profile paste pack)
linkedin_premium: no
linkedin_services_save: no (GO-gated; Save may be viewable)
publish: no
apply: no
invoice: no
payout_kyc: not this pack (slip only if screen already appeared)
```

---

## This PR does not

- Reopen Contra to publish or to “fix” Kent, USA
- Create Gumroad SKU-0 if the unpublished draft is absent
- Send Coconala estimates or Contra applications
- Save a LinkedIn Service Page that becomes viewable
- Retry Fiverr Press&Hold / Lancers captcha / CrowdWorks 403 / Upwork Google access block / TimeTicket DOB

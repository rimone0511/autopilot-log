# RANKED — where the next human+agent hour goes (2026-09-16 JST)

Pack: `earn-jobs-apply-queue-today-20260916/`  
State: **DRAFT_ONLY.** Rank is **not** a send/publish GO.

Proximity used (qualitative, **no GMV**):

1. A seller draft already exists (`draft_saved` / QUEUE `done-draft`).
2. A sibling paste pack exists for **that** desk’s next money click.
3. The next click can be a **real thread** (見積もり / Job-feed apply / inbound Services) rather than a new registration.
4. Hard walls (no account, image captcha, ship-blocker zip, `blocked_skip`) drop the rank or park it.

Do not treat “letters exist in git” as “a bid was sent.”

---

## Rank table (today)

| Rank | Desk | Spend today | Agent | Human | Default GO |
|---|---|---|---|---|---|
| **1** | ココナラ | If a **live** 見積もり相談 exists: one local paste. If none: look-don't-publish the existing listing, then stop. | Point at sibling estimate files. Do not send. | Open official 相談. Fill `{{ONE_SPECIFIC_DETAIL}}` locally **or skip**. | `coconala_send_estimate: false` · `coconala_publish_listing: false` |
| **2** | Contra Independent | Do **not** re-paste bio. Prepare **one** Job-feed apply **text**. | Point at JOBS letters. Do not Apply. | One listing, one style. Skip if the detail won’t fill. Stay **Free**. | `contra_apply_opportunity: false` |
| **3** | Gumroad SKU-0 | Unpublished look + optional listing polish paste. **Not** Publish. | Point at polish / look packs. Do not attach zip. | Title / price / icons look. Keep unpublished. Content zip is a **ship-blocker**. | `gumroad_publish_sku0: false` |
| **4** | LinkedIn | Only if login works **without** an image/tile puzzle. Fill locally. Stop before Save-if-viewable. | Point at Service Page + inbound replies. Do not Save/Send. | Existing personal profile only. Inbound Services only. | `linkedin_save_services_if_viewable: false` · `linkedin_submit_services_proposal: false` |
| **5** | Freelancer.com | **0 minutes** unless a seller account **already exists**. | Do not signup. If account exists: point at bid letters. Do not Bid. | ACCOUNT-PRECONDITION first. Then one listing per style. | `freelancer_place_bid: false` |

If Rank 1 has no live 見積もり相談, **do not** invent one. Move to Rank 2. Do not open CrowdWorks / Lancers “because the JP paste also fits” — those desks are `blocked_skip` today ([PARK.md](PARK.md)).

---

## Rank 1 — ココナラ Coconala (inbound estimate)

**Why first:** MAIN Google login already confirmed; profile / listing left unpublished (`draft_saved`). A matching 見積もり相談 is the shortest path from a parked JP seller desk to a paid thread. Listing **公開する** is a different, slower click and still gated.

**Missing (do not invent):** a サービス内容 (listing body) pack. Estimate files are **not** the 1000-character gig body. No live service URL in git.

**Today’s DRAFT block**

1. Open ココナラ on MAIN Google. Confirm the existing draft is still unpublished. Do not toggle 公開する.
2. Look at **inbound** 見積もり相談 only. Do not browse-and-spray the request board.
3. If **one** thread matches n8n / LLM-ops / inspect work: pick **one** sibling file ([POINTERS.md](POINTERS.md) Coconala). Personalize locally. Re-count on the live form.
4. If no thread, or `{{ONE_SPECIFIC_DETAIL}}` will not fill in about a minute: **skip**. Log `coconala_estimate: スキップ`. Spend leftover time on Rank 2.

**Human GO (optional, not required to finish today)**

| Gate row | Click |
|---|---|
| `coconala_send_estimate` | 見積もりを送る / 相談に返信して送信 on **that one** thread |
| `coconala_publish_listing` | 公開する on the **existing** draft only. Still no new service if none exists. **Not** the first click today. |

**KYC:** 振込・NDA screen already up → sibling slip [#43](https://github.com/rimone0511/autopilot-log/pull/43) `01-coconala.md`. Otherwise `なし`. Agent does not upload.

---

## Rank 2 — Contra Independent (Job-feed apply text)

**Why second:** Live CU 2026-09-16 parked Independent as `draft_saved` ([#64](https://github.com/rimone0511/autopilot-log/pull/64)): name / one-liner / bio / topics saved, About reached, **apply: no**. JOBS-phase letters exist ([#71](https://github.com/rimone0511/autopilot-log/pull/71)). An account exists, so a personalized Apply is possible **after** a human GO — unlike Freelancer.

**Do not:** re-paste bio; change Kent, USA to Japan (Persona is morning KYC, not earn); buy Pro; Refer & Earn; Labs / Expert / Discover-boost.

**Today’s DRAFT block**

1. Confirm Free plan. Do not open Wallet / Persona from this queue.
2. Open **one** Job-feed posting on contra.com (official UI). Not a scrape dump.
3. Pick **one** style file from [#71](https://github.com/rimone0511/autopilot-log/pull/71). A second job of the same style is spray — close it.
4. Older one-off snippets in [#5](https://github.com/rimone0511/autopilot-log/pull/5) `06` / `07` are fallback if the Job-feed styles do not match. Prefer #71 for JOBS phase.
5. Rates stay in the **form** as `{{HOURLY_RATE_USD}}` / `{{FIXED_PRICE_USD}}`. Empty required rate → park `rate_required`. Do not invent USD in git.

**Human GO (optional)**

| Gate row | Click |
|---|---|
| `contra_apply_opportunity` | Apply / Submit on **that** posting |
| `contra_send_inquiry_reply` | Reply on an **inbound** inquiry only |
| `contra_publish_feed` / `contra_discoverable_on` | Not required to apply. Stay off unless 祐太 flips them. |

`contra_buy_pro` and `contra_persona_wallet` stay **false**.

---

## Rank 3 — Gumroad SKU-0 (unpublished polish, not a storefront GO)

**Why third:** Desk is `draft_saved`, but money needs a **buyer zip** plus a later Publish. Today’s useful work is look-don't-ship and optional listing paste into the **existing** unpublished product. That is inventory hygiene, not a bid.

**Ship-blocker (unchanged):** Content-tab files / buyer zip are **not** this queue. Do not zip operator folders. Do not attach covers from an agent. [#74](https://github.com/rimone0511/autopilot-log/pull/74) authors listing copy; it does **not** attach files.

**Today’s DRAFT block**

1. Products list, MAIN Google. Find **one** unpublished SKU-0 (form → table → notify). If several: stop and pick with a human. If none: **do not** click New product. Log `sku0_live_draft_missing`. Rank 3 then ends.
2. Two-minute parent look: title / price / icons ([#63](https://github.com/rimone0511/autopilot-log/pull/63)). Matches weekly Day 1. Do not open Content tab from that card.
3. Optional: paste EN and/or JA listing + FAQ from [#74](https://github.com/rimone0511/autopilot-log/pull/74) into that unpublished editor. Price: keep **$39** if already set; else local `{{PRICE}}`. Do not publish at $0. Do not commit the live title, price, or `gumroad.com/l/...`.
4. Close unpublished.

**Human GO (not today’s recommended click)**

| Gate row | Click |
|---|---|
| `gumroad_publish_sku0` | Publish / Enable **after** every ship-blocker on the sibling CHECKLIST is green **and** 祐太 decides. Not implied by Rank 3. |
| `gumroad_new_product_if_missing` | **Always false** in this pack. |

Payout / Stripe KYC: only if a live payout screen already appeared ([#43](https://github.com/rimone0511/autopilot-log/pull/43) `06-gumroad.md`). Draft product ≠ open Payout.

---

## Rank 4 — LinkedIn (Services fill / inbound only)

**Why fourth:** JOBS phase includes this desk in the `draft_saved` set, but two walls sit in front of money: (1) register-loop boxes still say login `blocked_skip` **reCAPTCHA** ([#49](https://github.com/rimone0511/autopilot-log/pull/49) [#54](https://github.com/rimone0511/autopilot-log/pull/54)); (2) official help: **Save** on a personal Service Page can make it **viewable**. Easy Apply Jobs are **out of desk**.

[#75](https://github.com/rimone0511/autopilot-log/pull/75) STATUS is `paste_ready`, **not** a claim that the live Service Page is `draft_saved`. This queue does not overwrite that.

**Today’s DRAFT block**

1. Existing recovered personal LinkedIn / MAIN Google only. No Company Page. No second account.
2. Captcha: checkbox / Press & Hold may be tried **once** (sibling [#53](https://github.com/rimone0511/autopilot-log/pull/53)). **Image / tile puzzle → stop**, human only. Do not retry from this folder.
3. If login fails: park Rank 4. Do not spend the hour on Easy Apply.
4. If login works: Service Page editor — fill from [#75](https://github.com/rimone0511/autopilot-log/pull/75) CATEGORIES / ABOUT / CTA. Pricing = **Contact for pricing**. Empty required rate → `rate_required`.
5. If Save = viewable (`no_draft_path`): **stop**. Clear fields if you typed. Close.
6. Inbound Services request in Admin → New requests: local paste from [#38](https://github.com/rimone0511/autopilot-log/pull/38) `07`–`12`. No inbound request → do not DM. Connection notes `01`–`06` are optional local rehearsal only (Basic note cap exists; do not send a blank invite).

**Human GO (optional)**

| Gate row | Click |
|---|---|
| `linkedin_save_services_if_viewable` | Save that members can see |
| `linkedin_save_profile_if_viewable` | Profile Save that publishes |
| `linkedin_submit_services_proposal` | Submit on **one inbound** request |
| `linkedin_send_connection` | Send on **one** invitation with a filled `{{ONE_SPECIFIC_DETAIL}}` |

`linkedin_buy_premium`, `linkedin_share_to_feed`, `linkedin_open_to_work_or_easy_apply` stay **false**.

---

## Rank 5 — Freelancer.com surgical bids (account-ready gate)

**Why last:** Bid letters are paste-ready ([#68](https://github.com/rimone0511/autopilot-log/pull/68)), but Wave A still lists this desk `pending`. Sibling CU notes still say **No bids / No contests**. “Letters exist” ≠ “account exists” ≠ “Bid was clicked.”

**Today:** If you cannot sign in as the seller on MAIN Google → **stop**. Use register / profile packs later. **Do not** spend the JOBS hour on signup, KYC, or wallet.

If a seller account **already exists** (human confirms; this pack does not claim it):

1. Read [ACCOUNT-PRECONDITION](https://github.com/rimone0511/autopilot-log/pull/68) on that branch.
2. Open **one** project in the official UI. One style file. Skip if `{{ONE_SPECIFIC_DETAIL}}` will not fill.
3. Bid amount / hourly / delivery stay in **form fields**. Cite https://www.freelancer.com/feesandcharges only. Do not copy fee amounts or invent a wallet / leftover-bid balance.
4. If the form demands wallet funding, KYC, membership, or Sponsored / Highlight / Sealed → **stop**.

**Human GO (optional, only after account exists)**

| Gate row | Click |
|---|---|
| `freelancer_place_bid` | Bid / Place Bid on **that one** project |

`freelancer_signup`, `freelancer_wallet_fund`, `freelancer_contest`, `freelancer_buy_upgrade` stay **false**.

---

## Suggested time split (one work block, still DRAFT)

Not a quota. Skip a row if the wall is up.

| Slice | Rank | If blocked, skip to |
|---|---|---|
| First | 1 Coconala live 見積もり? | Rank 2 |
| Next | 2 Contra one Job-feed text | Rank 3 |
| Short | 3 Gumroad 2-minute look | Rank 4 only if login is already open |
| Only if login already works | 4 LinkedIn fill, no Save | Rank 5 only if account already exists |
| Only if signed in as seller | 5 Freelancer one letter | PARK |

Do **not** stack 公開する + Publish + Apply + Save + Bid in the same block even if several GO rows were flipped. One live send/publish click per block, and only after GO-GATES.

---

## Daily stop (copy locally; do not commit secrets)

```
date_jst: 2026-09-16
rank_reached:
look_only: yes
gate_row_flipped: none
publish_or_apply_or_bid_clicked: no
coconala_live_estimate: none / one / skip
contra_job_feed: none / one / skip
sku0_live_draft: yes / no / not_checked / missing
linkedin_login: ok / captcha / not_opened
freelancer_account_exists: no / yes / not_checked
one_specific_detail_filled: yes / skip
gmv_written: no
secret_committed: no
```

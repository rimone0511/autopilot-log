# WEEK — 7-day earn calendar (2026-09-16 JST → 2026-09-22 JST)

**DRAFT_ONLY.** Every day below is look / local paste / unpublished save unless 祐太 flips the matching row in [GO-GATES.md](GO-GATES.md) **and** clicks the live control.

No GMV targets. No “N applies per day will convert.” Cap is **attention**, not invented pipeline volume.

Timezone: **JST**. One primary desk per day. Optional 15-minute look on a second desk is allowed; a second **GO** the same day is not the default.

If a day is missed, do **not** stack two GOs the next morning. Finish the missed DRAFT look, then park.

---

## At a glance

| Day | Date | Primary desk | DRAFT this day (no GO) | Human GO (only if gate row is `true`) |
|---|---|---|---|---|
| 1 | Wed 2026-09-16 | All four (inventory) | Confirm unpublished. Gumroad 2-minute title/price/icons look | None. Do not publish “because the week started” |
| 2 | Thu 2026-09-17 | ココナラ | Listing look-don't-ship. Local estimate paste (do not send) | `coconala_publish_listing` and/or `coconala_send_estimate` |
| 3 | Fri 2026-09-18 | Gumroad SKU-0 | Full look-don't-ship QA. Leave unpublished | `gumroad_publish_sku0` / `gumroad_enable_permalink` — still not New product |
| 4 | Sat 2026-09-19 | Contra | Do not re-paste bio. One opportunity apply **text** locally | `contra_apply_opportunity` / Discoverable / feed Publish |
| 5 | Sun 2026-09-20 | LinkedIn profile | Profile look. Services fill only if unpublished path exists | Save-if-viewable, Send connection, Submit inbound proposal |
| 6 | Mon 2026-09-21 | Coconala + Contra | Personalize **at most one** estimate DRAFT and **at most one** Contra apply DRAFT | Send those two **only** with gates on; skip if detail won’t fill |
| 7 | Tue 2026-09-22 | Review | Fill [LOG.md](LOG.md) locally. Park all four `draft_saved` | Payout KYC **only** if a live payout/NDA screen already appeared |

Agent never clicks the GO column.

---

## Day 1 — Wed 2026-09-16 — Inventory (look-don't-ship)

**Goal:** Know what is actually unpublished. Do not “start earning” by publishing.

**DRAFT**

1. Read [STATUS.md](STATUS.md) and [GO-GATES.md](GO-GATES.md). Confirm every publish/apply flag is `false`.
2. **Gumroad (≤2 min):** parent-only [PR#63](https://github.com/rimone0511/autopilot-log/pull/63) card — title / price / icons. Do not open Content. Do not New product. If the unpublished SKU-0-shaped draft is missing: local `sku0_live_draft_missing`. **Stop.**
3. **ココナラ:** open the existing unpublished listing/profile. Confirm 公開する was not pressed. Do not rewrite サービス内容 from memory (listing pack is missing).
4. **Contra:** do not reopen to edit name/bio/topics ([#64](https://github.com/rimone0511/autopilot-log/pull/64) already saved). Do not “fix” Kent, USA.
5. **LinkedIn:** sign in to the **existing** personal profile only. If login reCAPTCHA is an **image puzzle**, stop for a human. Do not Save Services today.

**Human GO this day:** none.

**Stop lights:** payout, Persona, Premium, Publish, 公開する, Apply.

---

## Day 2 — Thu 2026-09-17 — ココナラ (listing look + estimate DRAFT)

**Goal:** Listing stays unpublished unless a GO. Prepare **one** estimate reply locally.

**DRAFT**

1. Listing look-don't-ship: title, category, photos already on the draft. Do not upload new ID-ish photos. Do not invent a 1000-word サービス内容 into git.
2. Pick **one** sibling estimate file (do not copy the body into this folder):
   - Wave 1 LLM 型: [PR#11](https://github.com/rimone0511/autopilot-log/pull/11) `03-llm-ops-coconala-estimate.md`
   - Wave 2 n8n 請求受付 / 書類タグ / AI 検品: [PR#28](https://github.com/rimone0511/autopilot-log/pull/28) `03` / `07` / `10`
3. Personalize **locally**: `{{JOB_TITLE}}`, `{{SCOPE_ONE_LINER}}`, `{{QUESTION_1}}`. Leave `{{PRICE_YEN_DRAFT}}` / `{{LEAD_TIME_DRAFT}}` empty until the live form, and still do not commit them.
4. If no live 見積もり相談 matches: **skip**. Do not browse-and-spray.

**Human GO (optional, not required to finish the day)**

| Gate row | Click |
|---|---|
| `coconala_publish_listing` | 公開する on the **existing** draft only. Still no new service if none exists |
| `coconala_send_estimate` | 見積もりを送る on **one** thread after the send-gate boxes in GO-GATES |

**KYC:** 振込・NDA screen only → sibling slip [#43](https://github.com/rimone0511/autopilot-log/pull/43) `01-coconala.md`. Otherwise `なし`.

---

## Day 3 — Fri 2026-09-18 — Gumroad SKU-0 (full look, still unpublished)

**Goal:** QA the existing unpublished SKU. Shipping is a separate GO.

**DRAFT**

1. If Day 1 noted `sku0_live_draft_missing`: **do not create**. Day 3 is then “pack still missing.” Stop.
2. Else run [PR#55](https://github.com/rimone0511/autopilot-log/pull/55) CHECKLIST: title, price, cover/thumbnail, Content files. Fill a **local** GAPS copy. Do not commit live title, price, or permalink.
3. Confirm still unpublished. Do not attach SKU-1/2/3 stubs.
4. Do not open Payout because “QA is done.”

**Human GO (optional)**

| Gate row | Click |
|---|---|
| `gumroad_publish_sku0` | Publish / Enable on **that** SKU-0 draft |
| `gumroad_enable_permalink` | Treat a custom permalink as live (still do not write the URL into git) |

`gumroad_new_product_if_missing` stays **false** even after a GO on another row.

**Do not** announce a `gumroad.com/l/...` URL on X / note / BOOTH from this plan.

---

## Day 4 — Sat 2026-09-19 — Contra (park + one apply DRAFT)

**Goal:** Keep Independent draft. Optionally prepare **one** public-opportunity application text.

**DRAFT**

1. Do not re-paste name / one-liner / bio / topics.
2. Location stays **Kent, USA** unless 祐太 separately wants Japan + Persona (morning, sibling [#64](https://github.com/rimone0511/autopilot-log/pull/64) RESUME-NOTES). That is not an earn GO.
3. Open **one** public opportunity on contra.com. If `{{ONE_SPECIFIC_DETAIL}}` will not fill in about a minute: skip.
4. Local paste from [PR#5](https://github.com/rimone0511/autopilot-log/pull/5) `06-contra-opportunity-apply.md`. Clear the form if you typed into it. Stay on **Free**. No Pro.

**Human GO (optional)**

| Gate row | Click |
|---|---|
| `contra_apply_opportunity` | Apply / Submit on **that** opportunity |
| `contra_send_inquiry_reply` | Reply on an **inbound** inquiry only (`07-contra-inquiry-reply.md`) |
| `contra_publish_feed` / `contra_discoverable_on` | Feed or Discoverable. Not required to apply |

`contra_buy_pro` and `contra_persona_wallet` stay false.

---

## Day 5 — Sun 2026-09-20 — LinkedIn profile (look; Services Save is GO)

**Goal:** Profile stays a parked draft. Do not turn Save into accidental publish.

**DRAFT**

1. Existing personal profile only. No Company Page. No second LinkedIn.
2. **Profile:** look at headline / About already on the account. There is **no** in-repo profile paste — do not invent one into git. If a control is clearly unpublished-save, you may save **only** when it does not make the profile newly public. When unsure: close.
3. **Services:** you may fill fields from [PR#16](https://github.com/rimone0511/autopilot-log/pull/16) `03-linkedin-services.md` **if** an unpublished path exists. Pricing stays “Contact for pricing.” If Save = viewable (`no_draft_path`): **stop**.
4. Rehearse **at most one** connection note locally from [PR#38](https://github.com/rimone0511/autopilot-log/pull/38) `01`–`06`. Peer context, not a pitch. Plan for **200** characters (Basic). Do not Send.
5. Services proposal files `07`–`12` are **inbound Admin → New requests only**. No RFP → do not DM them.

**Human GO (optional)**

| Gate row | Click |
|---|---|
| `linkedin_save_profile_if_viewable` | Profile Save that publishes |
| `linkedin_save_services_if_viewable` | Service Page Save that members can see |
| `linkedin_send_connection` | Send on **one** invitation with a filled `{{ONE_SPECIFIC_DETAIL}}` |
| `linkedin_submit_services_proposal` | Submit on **one inbound** request |
| `linkedin_share_to_feed` | Share / notify network |

`linkedin_buy_premium` stays false. No InMail.

**Captcha:** image/tile puzzle → human only. Do not start Easy Apply Jobs (out of scope).

---

## Day 6 — Mon 2026-09-21 — Apply / estimate DRAFT queue (still gated)

**Goal:** At most **two** personalized drafts (Coconala estimate + Contra apply). Sending is GO, not a quota.

**DRAFT**

1. **ココナラ:** if Day 2 already has a local estimate matching a **live** 見積もり相談, re-count characters on the live form. If the thread is gone or the detail won’t fill: skip. Do not open CrowdWorks / Lancers “because the paste also fits.”
2. **Contra:** if Day 4’s opportunity is still open and the detail still matches, keep that one draft. Do not add a second opportunity “to increase odds.”
3. **Gumroad / LinkedIn:** no extra publish pass unless a leftover **look** gap from Day 3 / Day 5. Still no New product, still no Save-if-viewable.

**Human GO (optional, max two clicks)**

| Gate row | Click |
|---|---|
| `coconala_send_estimate` | One Coconala 見積もり送信 |
| `contra_apply_opportunity` | One Contra Apply |

Do not also flip listing Publish, Gumroad Publish, and LinkedIn Save the same morning.

---

## Day 7 — Tue 2026-09-22 — Review and park

**Goal:** Write what happened without inventing outcomes. Park `draft_saved`.

**DRAFT**

1. Fill a **local** [LOG.md](LOG.md): which DRAFT looks ran, which GO rows were flipped, which skips (missing SKU-0, no matching estimate, captcha, KYC screen).
2. Confirm git still has no live URLs, prices, or ID files.
3. Leave all four desks unpublished unless a GO already happened (do not unpublish from an agent).
4. Next week is a **new** plan pack. Do not keep these gate rows `true` by habit.

**Human GO this day**

- No new publish/apply by default.
- `any_payout_kyc_upload` only if a **live** payout / NDA / (Contra) Japan-location screen already appeared. Use sibling slips. Documents on the site only.

**Out of week:** Wave B serial, Craudia, Freelancer.com, SKU-1/2/3 publish, Fiverr hold retry.

---

## Daily stop checklist (copy to local)

```
date_jst:
desk:
look_only: yes / no
gate_row_flipped: none / (name)
publish_or_apply_clicked: no / yes (human)
sku0_live_draft: yes / no / not_checked / missing
coconala_listing_still_unpublished: yes / no / not_checked
contra_kent_usa_left: yes / n/a
linkedin_save_if_viewable_clicked: no
one_specific_detail_filled: yes / skip
payout_screen: no / closed
gmv_written: no
secret_committed: no
```

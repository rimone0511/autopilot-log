> **STOP. Gate is closed.**  
> Missing, unread, or half-filled = do not publish, do not apply, do not send, do not bid.

# GO-GATES — TODAY apply queue 2026-09-16

Mirror of the Autopilot Log posting gate: **fail closed**.  
“Drafts are saved” / “this rank is #1” is not “the marketplace may go live.”

This file is the switch. [RANKED.md](RANKED.md) is the work order. Neither file is a GO until the matching row is `true` **and** 祐太 clicks the live control.

Sibling week calendar ([#76](https://github.com/rimone0511/autopilot-log/pull/76) `GO-GATES.md`) uses the same idea. **This file is the switch for this folder.** Do not infer a GO from the week pack, a merged PR, or a `draft_saved` hint.

Default (commit this way):

```
jobs_today_apply_queue_gate:
  pack: earn-jobs-apply-queue-today-20260916
  date_jst: 2026-09-16
  draft_only: true
  coconala_publish_listing: false
  coconala_send_estimate: false
  gumroad_publish_sku0: false
  gumroad_enable_permalink: false
  gumroad_new_product_if_missing: false
  contra_publish_feed: false
  contra_discoverable_on: false
  contra_apply_opportunity: false
  contra_send_inquiry_reply: false
  contra_buy_pro: false
  contra_persona_wallet: false
  linkedin_save_profile_if_viewable: false
  linkedin_save_services_if_viewable: false
  linkedin_send_connection: false
  linkedin_submit_services_proposal: false
  linkedin_share_to_feed: false
  linkedin_buy_premium: false
  linkedin_open_to_work_or_easy_apply: false
  freelancer_place_bid: false
  freelancer_signup: false
  freelancer_wallet_fund: false
  freelancer_contest: false
  freelancer_buy_upgrade: false
  any_payout_kyc_upload: false
```

If this file is deleted, treat every action flag as `false`.

---

## UI labels that mean publish / apply / bid (stop)

Do not click. Log `stopped_at_publish` locally. Leave.

**ココナラ**

- 公開する / 出品を公開 / 公開中にする
- 見積もりを送る / 提案する / 相談に返信して送信

**Gumroad**

- Publish / Enable / Unpause / go-live
- New product (when SKU-0 draft is missing)
- Discover, boost, custom domain checkout

**Contra**

- Publish (feed or service)
- Turn Discoverable on
- Apply / Submit on a Job-feed posting or opportunity
- Send on an inquiry
- Upgrade to Pro / Max
- Persona / Verify identity / Wallet add-account (not an earn click; morning KYC only)

**LinkedIn**

- Save on a Service Page when help or UI says the page becomes **viewable**
- Save / Publish on profile sections when that is the public toggle
- Send / 送信 on a connection invitation or InMail
- Submit proposal / 提案を送信 on a Services request
- Share / Notify network / Create a post about your services
- Premium / Sales Nav / Recruiter trial
- Easy Apply / Open to work

**Freelancer.com**

- Bid / Place Bid / Submit bid
- Contest entry
- Fund Site wallet / Minimum Account Balance
- Sponsored / Highlight / Sealed / extra bids / membership checkout
- Verify my Identity / Preferred Freelancer exam

**All desks**

- Any government-ID, liveness, tax, bank, or ads-billing form

---

## What DRAFT work is allowed without flipping a row

1. Open the official site (MAIN Google).
2. Look at an **already unpublished** draft, or a Job-feed / 見積もり thread you will **not** submit.
3. Paste into a **local** editor, or into a field you will **clear**.
4. Use 下書き保存 / unpublished save when that control does **not** make the listing public.
5. Watch the character counter.
6. Close.

If the field cannot be cleared safely, do not paste into the site. Keep the draft in the sibling pack.

---

## One-thread rule (estimate / apply / bid / inbound Services)

Skip if any box is false. Even after a GO, still one at a time.

- [ ] I opened **this** listing / opportunity / estimate / project on the **official** site (not a scraper, not a third-party apply tool).
- [ ] `{{ONE_SPECIFIC_DETAIL}}` is a fact from **this** page. If I cannot name one in about a minute, I skip.
- [ ] This is the **only** live thread I will use this style file on today.
- [ ] Leftover placeholders from a previous person are gone.
- [ ] No email, phone, WhatsApp, Telegram, Slack, Discord in the paste.
- [ ] No off-platform payment pitch.
- [ ] Price / date / bid tokens stay local. I do not commit them. I do not invent GMV.
- [ ] The matching GO-GATES row is still `false` unless 祐太 flipped it for **this** click.
- [ ] I will click Send / Apply / Bid / Save-if-viewable **myself**. Nothing in this folder submits for me.

---

## Paid / boost (always false this pack)

Do not buy to “finish the rank”:

- Contra Pro / Max
- LinkedIn Premium, InMail credits, Sales Navigator, Recruiter
- Gumroad Discover, boosts, custom domain
- Coconala paid options / ads
- Freelancer leftover-bid spray, Sponsored / Highlight / Sealed, membership, wallet top-up
- Upwork Connects (desk out of this queue)

---

## KYC / payout

`any_payout_kyc_upload` stays `false` here.

If a payout or NDA screen **already** blocked a GO you flipped, use sibling slips ([#43](https://github.com/rimone0511/autopilot-log/pull/43) Coconala / Gumroad, [#64](https://github.com/rimone0511/autopilot-log/pull/64) Contra location/Persona only, [#66](https://github.com/rimone0511/autopilot-log/pull/66) Freelancer STOP-KYC). Documents stay on the **site screen**. Not in git. Not in chat. Not in an agent.

---

## Fail-closed test (operator)

Ask: “Did 祐太 write a dated GO that **this** click may leave the account (send / publish / viewable Save / Bid)?”  
If the answer is no, missing, or “the PR is merged so it must be OK” → **do not click**.

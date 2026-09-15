> **STOP. Gate is closed.**  
> Missing, unread, or half-filled = do not publish, do not apply, do not send.

# GO-GATES — JOBS week 2026-09-16

Mirror of the Autopilot Log posting gate: **fail closed**.  
“Drafts are saved” is not “the marketplace may go live.”

This file is the switch. [WEEK.md](WEEK.md) is the calendar. Neither file is a GO until the matching row is `true` **and** 祐太 clicks the live control.

Default (commit this way):

```
jobs_week_gate:
  pack: earn-jobs-weekly-earn-plan-20260916
  week: 2026-09-16/2026-09-22
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
  any_payout_kyc_upload: false
```

If this file is deleted, treat every row as `false`. Do not infer permission from a merged PR, a `draft_saved` hint, or “it’s Day 6.”

---

## UI labels that mean publish / apply (stop)

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
- Apply / Submit on an opportunity
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

**All desks**

- Any government-ID, liveness, tax, bank, or ads-billing form

---

## What DRAFT work is allowed without flipping a row

1. Open the official site (MAIN Google).
2. Look at an **already unpublished** draft.
3. Paste into a **local** editor, or into a field you will **clear**.
4. Use 下書き保存 / unpublished save when that control does **not** make the listing public.
5. Watch the character counter.
6. Close.

If the field cannot be cleared safely, do not paste into the site. Keep the draft in the sibling pack.

---

## One-listing rule (apply / estimate)

Skip the thread if any box is false. Even after a GO, still one at a time.

- [ ] I opened **this** listing / opportunity / estimate thread on the **official** site (not a scraper).
- [ ] `{{ONE_SPECIFIC_DETAIL}}` is a fact from **this** page. If I cannot name one in about a minute, I skip.
- [ ] Leftover placeholders from a previous person are gone.
- [ ] No email, phone, WhatsApp, Telegram, Slack, Discord in the paste.
- [ ] No off-platform payment pitch.
- [ ] Price / date tokens stay local (`{{PRICE_YEN_DRAFT}}`, `{{FIXED_PRICE_USD}}`, `{{LEAD_TIME_DRAFT}}`). I do not commit them.
- [ ] The matching GO-GATES row is still `false` unless 祐太 flipped it for **this** click.

---

## Paid / boost (always false this pack)

Do not buy to “finish the week”:

- Contra Pro / Max
- LinkedIn Premium, InMail credits, Sales Navigator, Recruiter
- Gumroad Discover, boosts, custom domain
- Coconala paid options / ads
- Any Connects-like spend on desks **out of this week**

---

## KYC / payout

`any_payout_kyc_upload` stays `false` here.  
If a payout or NDA screen **already** blocked a GO you flipped, use sibling slips ([#43](https://github.com/rimone0511/autopilot-log/pull/43) Coconala / Gumroad, [#64](https://github.com/rimone0511/autopilot-log/pull/64) Contra location/Persona only). Documents stay on the **site screen**. Not in git. Not in chat. Not in an agent.

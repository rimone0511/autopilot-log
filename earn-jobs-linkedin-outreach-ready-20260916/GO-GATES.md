> **STOP. Gate is closed.**
> Missing, unread, or half-filled = do not Save, do not Send, do not Submit.

# GO-GATES — LinkedIn outreach-ready (JOBS 2026-09-16)

Mirror of the Autopilot Log posting gate: **fail closed**.  
“Drafts are sequenced in git” is not “LinkedIn may go viewable or send.”

This file is the switch. [OPERATOR-ORDER.md](OPERATOR-ORDER.md) is the serial. Neither file is a GO until the matching row is `true` **and** 祐太 clicks the live control.

Default (commit this way):

```
linkedin_outreach_ready_gate:
  pack: earn-jobs-linkedin-outreach-ready-20260916
  phase: JOBS
  draft_only: true
  existing_recovered_profile_only: true
  linkedin_save_profile_if_viewable: false
  linkedin_save_services_if_viewable: false
  linkedin_send_connection: false
  linkedin_submit_services_proposal: false
  linkedin_message_from_services_admin: false
  linkedin_share_to_feed: false
  linkedin_notify_network: false
  linkedin_create_post_about_services: false
  linkedin_unpublish_as_draft_trick: false
  linkedin_send_inmail: false
  linkedin_send_blank_invite_as_workaround: false
  linkedin_buy_premium: false
  linkedin_choose_company_page: false
  linkedin_open_to_work_or_easy_apply: false
  any_payout_kyc_upload: false
```

If this file is deleted, treat every row as `false`. Do not infer permission from a merged PR, from “#75 is paste_ready”, or from JOBS week Day 5.

Sibling gates (do not copy, still closed):

- [#75](https://github.com/rimone0511/autopilot-log/pull/75) `STOP-AT-SAVE.md` — `save_service_page_if_viewable: false`
- [#38](https://github.com/rimone0511/autopilot-log/pull/38) `STOP-AT-PUBLISH.md` — send / Submit / Save-if-viewable all `false`
- [#76](https://github.com/rimone0511/autopilot-log/pull/76) `GO-GATES.md` — week-level LinkedIn rows stay `false`

This pack does not flip those files.

---

## UI labels that mean publish / send (stop)

Do not click. Log `stopped_at_save` / `stopped_at_publish` locally. Leave.

**Save (profile / Services)**

- **Save** / **保存** when help or the UI says the page or section becomes **viewable**
- **Publish** / **公開** / **Make viewable**
- **Unpublish** used as a workaround (removes a **live** page; not a draft control)

**Services (inbound proposal)**

- **Submit** / **Submit proposal** / **提案を送信**
- **Send** on a message compose opened from Services admin
- **Request services** used **outbound** (this desk is seller-side inbound replies only)

**Connections**

- **Send** / **送信** on a connection invitation (with or without a note)
- **Send** on InMail
- Blank **Connect** with no note, used to dodge the monthly note cap

**Feed / paid / Jobs**

- **Share** / **Notify network** / **Create a post about your services**
- **Upgrade** / **Premium** / **Start free trial** / Sales Navigator / Recruiter
- **Easy Apply** / **Open to work**

**All**

- Any government-ID, liveness, tax, bank, or ads-billing form

---

## What DRAFT work is allowed without flipping a row

1. Do **not** require a live LinkedIn session from **this** authoring PR.
2. Later human/CU: open the **official** site (MAIN Google, recovered personal profile).
3. Look at headline / About **already on the account**.
4. Paste #75 fields into a **local** editor, or into a field you will **clear**.
5. Rehearse **at most one** #38 connection note the same way. Peer context, not a pitch.
6. Open Services **07–12** only when Admin → New requests already has **this** RFP; still clear or stay local.
7. Watch the character counter.
8. Close.

If the field cannot be cleared safely, do not paste into LinkedIn. Keep the draft in the sibling pack.

A true unpublished Service Page control, if visible, still does **not** authorize Save from this PR.

---

## One-thread rule (Send / Submit — still off)

Skip the person or request if any box is false. Even after a later GO, still one at a time.

- [ ] I opened **this** profile or **this** Services request on **linkedin.com** (not a scraper, not Sales Nav automation).
- [ ] This GO-GATES file is still all `false` unless 祐太 flipped the **matching** row for **this** click.
- [ ] I replaced `{{ONE_SPECIFIC_DETAIL}}` with a fact from **this** public post / headline / RFP. If I cannot name one in about a minute, I skip.
- [ ] For 01–06: I am not using the note to sell. No URL, no “Request services”, no calendar link.
- [ ] For 07–12: a **New request** already exists. I did not cold-message this copy.
- [ ] Leftover placeholders from a previous person are gone.
- [ ] No email, phone, WhatsApp, Telegram, Slack, Discord in the paste.
- [ ] No InMail. No Premium trial. No second LinkedIn. No blank invite as a workaround.
- [ ] The live character counter still has room **after** substitutions (connection notes: plan for **200** on Basic).
- [ ] I will click **Send / Submit / Save** myself only after a GO **outside** this folder. Nothing here submits.

---

## Paid / boost (always false this pack)

Do not buy to “become outreach-ready”:

- LinkedIn Premium, InMail credits, Sales Navigator, Recruiter Lite
- Ads identity / billing to unlock a badge
- Any Connects-like spend on other desks from this folder

---

## KYC / payout

`any_payout_kyc_upload` stays `false`.  
LinkedIn has **no** morning slip in [#43](https://github.com/rimone0511/autopilot-log/pull/43). If a verification-badge or ads-identity screen appears: close the picker **without a file**. Hand desk + screen type to morning. Documents stay on the **site screen**. Not in git. Not in chat. Not in an agent.

---

## Fail-closed test (operator)

Ask: “Did a human outside this repo write a dated GO that **this** Save may make the Service Page viewable, or that **this** recipient / **this** RFP may be sent?”  
If the answer is no, missing, or “the PR is merged so it must be OK” → **do not Save, do not Send, do not Submit**.

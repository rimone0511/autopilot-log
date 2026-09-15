# DRAFT_ONLY — sales-call one-pager (JOBS)

Pack date: 2026-09-16  
Phase: **JOBS** (sales conversation, not marketplace register)  
Folder: `earn-jobs-sales-call-one-pager-20260916/`

**This folder is an operator sheet and talk tracks. It is not a booking, not a quote, not a Loom, and not a send.**

No agent session may:

- Join, schedule, or record a call (Zoom / Meet / phone / Coconala 電話相談)
- Record, upload, or share a Loom / YouTube / TikTok / Drive video
- Click marketplace **Submit / Send / 見積もり送信 / Publish / Enable / 公開する / Apply**
- Speak a live yen or USD figure from git
- Invent case metrics (GMV, hours saved, win rate, accuracy %, client counts)
- Add email, phone, WhatsApp, or a second desk “so we can talk properly”
- Attach live n8n / Google / Slack / mail credentials
- Claim partnership with n8n, Coconala, Gumroad, Contra, Loom, or an AI lab

## Allowed for this pack

- [ ] Read this one-pager and the sibling outlines it points at
- [ ] Rehearse out loud with **dummy** data only (`EXAMPLE-ONLY`, `Client A`–`C`)
- [ ] Replace `{{DISPLAY_NAME}}` and `{{ONE_SPECIFIC_DETAIL}}` on a **local** copy
- [ ] Stop

A later human may talk or record after a GO **outside** this repository. Until then every control stays off:

```
sales_call_gate:
  pack: earn-jobs-sales-call-one-pager-20260916
  draft_only: true
  join_or_schedule_call: false
  record_call: false
  record_loom: false
  upload_loom: false
  share_loom_url: false
  post_to_x_or_note: false
  post_via_autopilot_log: false
  activate_n8n_workflow: false
  attach_live_credentials: false
  send_marketplace_message: false
  send_coconala_estimate: false
  publish_coconala: false
  publish_gumroad: false
  publish_contra_service: false
  apply_contra: false
  speak_live_price: false
  invent_case_metrics: false
  add_off_desk_contact: false
```

A missing gate file means the same as every flag `false`. Do not infer permission from a merged PR.

## Hard stop — do NOT

Money / proof:

- [ ] Read `{{PRICE_*}}` as a researched rate
- [ ] Quote `$39`, `¥500`, Contra Pro fees, or any competitor’s number as “what I charge”
- [ ] Promise income, SLA, or “this sold last week”
- [ ] Collect payout, bank, tax, Persona, or ID from a prospect

Live systems:

- [ ] Open a production sheet, inbox, or n8n that holds real customer rows
- [ ] Turn a workflow **Active** “so the call looks finished”
- [ ] Send mail / Slack / LINE / a public post from the demo path

Channel:

- [ ] Move a Coconala トーク / Gumroad message / Contra thread onto email or Zoom from this pack
- [ ] Create a Coconala 電話相談 or video service so the call has a “native” button

## Secrets policy

Do not put live emails, phones, webhook tokens, sheet IDs, passwords, bank, or tax IDs into git or onto a shared canvas.

If a filled secret appears in a working copy, delete it before commit and rotate the credential.

## Verification of this PR

Markdown only. No video files. Python posting-gate tests are unchanged. No call was joined. No Loom was recorded. No marketplace message was sent. No listing was published.

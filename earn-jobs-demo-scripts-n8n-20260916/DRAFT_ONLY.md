# DRAFT_ONLY — n8n demo scripts (JOBS)

Pack date: 2026-09-16  
Phase: **JOBS** (sales conversation, not marketplace register)  
Folder: `earn-jobs-demo-scripts-n8n-20260916/`

**This folder is spoken outlines and shot lists. It is not a recording, not a Loom URL, and not a send.**

No agent session may:

- Record, upload, or publish a Loom / YouTube / TikTok / Drive / note video from this pack
- Announce a live `loom.com/share/...` or `youtu.be/...` URL
- Click marketplace **Submit / Send / Publish Gig / Enable product**
- Attach live n8n, Google, Slack, or mail credentials
- Turn a workflow **Active** on a shared or production instance
- Put secrets into git or onto a shared canvas
- Claim partnership with n8n, Google, Slack, Loom, or an AI lab

## Allowed for this pack

- [ ] Read the three outlines
- [ ] Rehearse out loud with **dummy** data only
- [ ] Replace `{{DISPLAY_NAME}}` and `{{ONE_SPECIFIC_DETAIL}}` on a **local** copy
- [ ] Stop

A later human may record after a GO **outside** this repository. Until then every control stays off:

```
jobs_demo_gate:
  pack: earn-jobs-demo-scripts-n8n-20260916
  draft_only: true
  record_loom: false
  upload_loom: false
  share_loom_url: false
  post_to_x_or_note: false
  post_via_autopilot_log: false
  activate_n8n_workflow: false
  attach_live_credentials: false
  send_marketplace_proposal: false
  publish_gumroad: false
```

A missing gate file means the same as every flag `false`. Do not infer permission from a merged PR.

## Hard stop — do NOT

Record / publish:

- [ ] Start Loom / OBS / phone camera from an agent session
- [ ] Upload the file to Loom, YouTube, TikTok inbox, Drive, or a marketplace message
- [ ] Paste a share URL into git, a profile, or X
- [ ] Use Autopilot Log to post the demo (YouTube unattended or TikTok inbox)

Live systems:

- [ ] Open a production Google Sheet that holds real customer rows
- [ ] Paste a live spreadsheet ID, webhook token, or n8n API key
- [ ] Send mail, Slack, LINE, or a public post “to make the demo look real”
- [ ] Import sibling SKU stubs onto a buyer’s instance from this pack

Money / identity:

- [ ] Quote a live USD / JPY amount in the spoken script
- [ ] Collect payout, bank, tax, or ID from a prospect
- [ ] Buy n8n Cloud, Gumroad Discover, or a Loom paid plan from this pack

## Secrets policy

Demo payloads in this folder are **fictional**. Labels look like `EXAMPLE-ONLY`, `Client A`, `example-sender`.

If a filled secret appears in a working copy (token in a webhook URL, sheet ID, mailbox, phone), delete it before commit and rotate the credential.

## Verification of this PR

Markdown outlines only. No video files (`*.mp4` / `*.mov` are gitignored). Python posting-gate tests are unchanged. No Loom was recorded. No marketplace message was sent.

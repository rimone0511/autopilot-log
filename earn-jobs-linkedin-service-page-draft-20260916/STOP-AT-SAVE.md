> **STOP. Gate is closed.**
> Missing, unread, or half-filled = do not Save, do not publish, do not send.

# Stop-at-Save — LinkedIn Service Page (JOBS)

Mirror of the Autopilot Log posting gate: **fail closed**.  
“Drafts are written in git” is not “LinkedIn may go viewable.”

Official personal-profile help ([a569554](https://www.linkedin.com/help/linkedin/answer/a569554)): click **Save** to make the Service Page **viewable by members**. Edit help ([a570566](https://www.linkedin.com/help/linkedin/answer/a570566)): Edit page → adjust → **Save**. Unpublish ([a1362963](https://www.linkedin.com/help/linkedin/answer/a1362963)) removes a **live** page; it is not a draft control.

This file is the switch. [README.md](README.md) restates it. Neither file is a GO.

## Default (commit this way)

| control | committed value | if ignored |
|---|---|---|
| `draft_only` | `true` | pack is unused |
| `save_service_page_if_viewable` | `false` | page becomes viewable |
| `publish_service_page` | `false` | same as Save-as-viewable |
| `unpublish_as_draft_trick` | `false` | still a live-page action |
| `share_to_feed` / `notify_network` | `false` | public post |
| `create_post_about_services` | `false` | public post |
| `buy_premium` | `false` | paid identity / Request services CTA |
| `choose_company_page` | `false` | locked choice |
| `open_to_work_or_easy_apply` | `false` | LinkedIn Jobs — not this desk |
| `send_inmail_or_connection_blast` | `false` | outreach; sibling pack only, still no-send |

If this file is deleted, treat every row as `false`.

```
linkedin_service_page_gate:
  pack: earn-jobs-linkedin-service-page-draft-20260916
  phase: JOBS
  draft_only: true
  existing_recovered_profile_only: true
  save_service_page_if_viewable: false
  publish_service_page: false
  unpublish_as_draft_trick: false
  share_to_feed: false
  notify_network: false
  create_post_about_services: false
  buy_premium: false
  choose_company_page: false
  open_to_work_or_easy_apply: false
  send_inmail_or_connection_blast: false
  contact_for_pricing: true
```

A missing gate file means the same as every action flag `false`. Do not infer permission from a merged PR.

## UI labels that mean “publish”

Stop. Do not click. Log `stopped_at_save` / `no_draft_path` and leave.

- **Save** / **保存** when help or the UI says the page becomes viewable
- **Publish** / **公開** / **Make viewable**
- **Unpublish** used as a workaround
- **Share** / **Notify network** / **Create a post about your services**
- **Upgrade** / **Premium** / **Start free trial** / Sales Navigator / Recruiter
- **Easy Apply** / **Open to work**
- **Send** on connection, InMail, or a Services proposal

## What “rehearse a paste” is allowed to do

1. Open the official Service Page editor on the **existing recovered personal** profile.
2. Paste categories / About / CTA into fields you will **clear**, or into a local editor.
3. Watch the live character counter.
4. Close without Save / Publish / Share.

If the field cannot be cleared safely, do not paste into LinkedIn at all. Keep the draft in this folder.

If a true **unpublished / draft** control is visible and it does **not** make the page viewable: filling still does not require a GO from this PR. Leave Save-if-viewable `false` until a human GO exists **outside** this repo.

## KYC / paywall (morning operator)

Hand desk + screen type only. Do not upload. Do not store ID screenshots.

- Government photo ID, liveness, selfie, proof of address
- LinkedIn verification badge that demands ID
- Ads billing / card for a Premium trial
- Tax, bank, payout

## Fail-closed test (operator)

Ask: “Did a human outside this repo write a dated GO that Save may make this Service Page viewable?”  
If the answer is no, missing, or “the PR is merged so it must be OK” → **do not Save**.

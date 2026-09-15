> **STOP. Gate is closed.**  
> Missing, unread, or half-filled = do not send, do not publish.

# Stop-at-publish — LinkedIn outreach Wave 2

Mirror of the Autopilot Log posting gate: **fail closed**.  
“Drafts are written” is not “LinkedIn may send.”

This file is the switch. [README.md](README.md) restates it. Neither file is a GO.

## Default (commit this way)

| control | committed value | if ignored |
|---|---|---|
| `draft_only` | `true` | pack is unused |
| `send_connection_request` | `false` | invitation leaves the account |
| `attach_note_and_send` | `false` | counts against the monthly personalized-note cap |
| `send_blank_invite_as_workaround` | `false` | still an unsolicited invite; PCP spam risk |
| `send_inmail` | `false` | spends Premium credits this pack does not buy |
| `submit_services_proposal` | `false` | LinkedIn starts a project in admin view |
| `message_from_services_admin` | `false` | outbound message |
| `save_service_page_if_viewable` | `false` | official help: Save can make a personal Service Page **viewable** |
| `share_to_feed` / `notify_network` | `false` | public post |
| `buy_premium` | `false` | paid identity / extra RFPs |

If this file is deleted, treat every row as `false`.

## UI labels that mean “publish” or “send”

Stop. Do not click. Log `stopped_at_publish` and leave.

- **Send** / **送信** on a connection invitation
- **Send** on InMail or a message compose box
- **Submit** / **Submit proposal** / **提案を送信** on a Services request
- **Save** on a Service Page when help or the UI says the page becomes viewable
- **Publish** / **公開** / **Unpublish** (unpublish is not a draft trick)
- **Share** / **Notify network** / **Create a post about your services**
- **Request services** used **outbound** (this pack is seller-side inbound replies only)
- Any **Upgrade** / **Premium** / **Start free trial** / Sales Navigator / Recruiter

KYC, liveness, tax, ads billing: stop. That is the morning operator, not this folder.

## What “rehearse a paste” is allowed to do

1. Open the official composer.
2. Paste into a **local** editor or a field you will **clear**.
3. Watch the character counter.
4. Close without Send / Submit / Save-as-viewable.

If the field cannot be cleared safely, do not paste into LinkedIn at all. Keep the draft in this folder.

## Monthly note cap

Basic accounts: LinkedIn Help currently says **up to three** personalized invitation notes per month ([a563153](https://www.linkedin.com/help/linkedin/answer/a563153)). If the composer hides the note box or upsells Premium:

- Do **not** send a blank invite to “use” this pack
- Do **not** buy Premium from this pack
- Park `note_cap_hit` and stop

## Fail-closed test (operator)

Ask: “Did a human outside this repo write a dated GO for **this** recipient or **this** RFP?”  
If the answer is no, missing, or “the PR is merged so it must be OK” → **do not send**.

> **STOP. Gate is closed.**  
> Missing, unread, or half-filled = do not send.  
> `DRAFT_ONLY` / do-not-send. This pull request is not a send GO.

# Stop-at-send — cold email AI ops / n8n (SMBs)

Mirror of the Autopilot Log posting gate: **fail closed**.  
“Ten drafts exist in git” is not “mail may leave the account.”

This file is the switch. [README.md](README.md) restates it. Neither file is a GO.  
There is no send script. The agent does not create, update, or send live mail from this pack.

## Default (commit this way)

| control | committed value | if ignored |
|---|---|---|
| `draft_only` | `true` | pack is unused |
| `do_not_send` | `true` | a commercial message leaves the account |
| `gmail_create_draft` | `false` | a mailbox draft is still a step toward send |
| `gmail_send` / `smtp_send` | `false` | CAN-SPAM / 特定電子メール法 attach on send, not on git |
| `sequence_or_drip` | `false` | a blast, not one human note |
| `purchased_or_harvested_list` | `false` | aggravated CAN-SPAM risk; JP opt-in miss |
| `invent_case_study_metrics` | `false` | false advertising |
| `fill_live_recipient_in_git` | `false` | PII in the repo |
| `calendar_or_whatsapp_in_body` | `false` | off-thread contact harvest |

If this file is deleted, treat every row as **do not send**.

```
cold_email_gate:
  pack: earn-jobs-cold-email-ai-ops-20260916
  draft_only: true
  do_not_send: true
  gmail_create_draft: false
  gmail_send: false
  smtp_send: false
  sequence_or_drip: false
  purchased_or_harvested_list: false
  invent_case_study_metrics: false
  fill_live_recipient_in_git: false
```

A missing gate file means the same as every send flag `false`. Do not “infer” permission from a merged PR.

## UI labels that mean “send”

Stop. Do not click. Log `stopped_at_send` and leave.

- **Send** / **送信** / **Send anyway** in Gmail, Apple Mail, Outlook, or a phone client
- **Schedule send** / **送信予約**
- SMTP, API, n8n, Zapier, Make, or any workflow that delivers mail
- “Create draft” in a live mailbox from this agent (still a send-adjacent step)
- Importing a CSV into a sequencer (Mailchimp, HubSpot, Instantly, Smartlead, etc.)
- BCCing a list “just this once”

KYC, domain warm-up products, purchased inboxes, or a second Gmail to dodge reputation: stop. Morning operator, not this folder.

## What “rehearse a paste” is allowed to do

1. Read this folder and [FACTS.md](FACTS.md).
2. Rewrite `{{ONE_SPECIFIC_DETAIL}}` in a **local** editor from one public page.
3. Watch length. Clear the editor.
4. Do **not** paste into Gmail unless a dated GO **outside** this repo names **this** recipient. This pack still defaults to no.

If the field cannot be cleared safely, keep the draft in this folder only.

## Fail-closed test (operator)

Ask: “Did a human outside this repo write a dated GO for **this** recipient, and can I name the legal basis without stretching?”  
If the answer is no, missing, or “the PR is merged so it must be OK” → **do not send**.

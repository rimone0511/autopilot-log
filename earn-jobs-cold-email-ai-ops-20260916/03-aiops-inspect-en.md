> **DRAFT_ONLY. DO NOT SEND.**  
> No secrets. No fake “AI saved N hours.” Agent does not send.

# CE-03 — AI ops inspect-before-send (EN)

## Operator table (do not paste)

| key | value |
|---|---|
| pack | earn-jobs-cold-email-ai-ops-20260916 |
| id | CE-03 |
| theme | AI ops |
| lang | EN |
| mode | DRAFT_ONLY, HANDS |
| send | **forbidden** |
| smb_label | `SMB-C` (fictional) |
| chars_subject | short 53 / std 60 |
| chars_short | 615 |
| chars_standard | 1205 |

Facts: [FACTS.md](FACTS.md). Gate: [DRAFT_ONLY.md](DRAFT_ONLY.md).

Assumed public page: the SMB already drafts replies or posts and wants speed **without** letting a model hit Send.

Out of scope: fully autonomous outbound, invented citations, KYC-by-proxy.

---

## Headers (not committed live)

| field | value |
|---|---|
| To | `{{RECIPIENT_EMAIL}}` — **empty in git** |
| From | `{{SENDER_EMAIL}}` |
| Subject | short or standard subject fence below |

---

## Send gate

- [ ] Public page open; `{{ONE_SPECIFIC_DETAIL}}` is from **this** page
- [ ] Legal basis named, or skip
- [ ] I do **not** click Send

---

## Subject (short)

```
AI draft, human send — inspect before anything leaves
```

## Subject (standard)

```
{{ONE_SPECIFIC_DETAIL}} — a review queue, not an auto-sender
```

---

## Short body

```
{{RECIPIENT_NAME}} — I saw {{ONE_SPECIFIC_DETAIL}} on your public {{PUBLIC_PAGE_KIND}}.

The work I take is AI ops with a human stop: brief → draft → inspect → a person approves before send or publish. I do not let a model email your customers for you.

{{DISPLAY_NAME}}, Japan, async {{TIMEZONE}}. Notes: {{PORTFOLIO_URL}}

Out of scope: ungated outbound, made-up sources, identity checks for someone else.

{{QUESTION_1}}

One-off draft. Not a sequence.

---
Advertisement (freelance AI ops). Not sent.
{{DISPLAY_NAME}} · Japan · {{POSTAL_ADDRESS}}
Stop further marketing email: reply STOP to {{OPT_OUT_CONTACT}}.
```

---

## Standard body

```
{{RECIPIENT_NAME}} — I saw {{ONE_SPECIFIC_DETAIL}} on your public {{PUBLIC_PAGE_KIND}}.

I am {{DISPLAY_NAME}}. I set up a loop a second operator can rerun: a model may suggest a draft; a person reads it; send and publish stay human. I do not claim hours saved. I do not invent citations. I do not click Send in your mailbox.

Public notes: {{PORTFOLIO_URL}}. A public example of the same split (“running” vs “allowed to go public”) on official video APIs: {{GITHUB_REPO_AUTOPILOT}}. TikTok in that tool defaults to inbox upload, not unattended posting.

If we ever scoped a small job, deliverables would be operator notes, an inspect step, and a closed gate until you open it. Not a fully autonomous agent.

Japan-based, English or Japanese, async {{TIMEZONE}}. Independent. Not an employee of a model vendor.

{{QUESTION_1}}

This is a one-off note. Ignore it if you already have an internal owner for that stop.

---
This message is an advertisement for freelance AI ops (draft → inspect → human approve). It is a git draft and has not been sent.
{{DISPLAY_NAME}} · {{CITY}}, {{COUNTRY}} · {{POSTAL_ADDRESS}}
To stop further marketing email, reply STOP to {{OPT_OUT_CONTACT}}.
Public: {{PORTFOLIO_URL}}
```

---

## Fictional fill (not a real SMB; do not send)

- Label: `SMB-C`
- `{{PUBLIC_PAGE_KIND}}` example: `support / FAQ page`
- `{{ONE_SPECIFIC_DETAIL}}` example: `you ask people to email a named inbox instead of a chatbot`
- `{{QUESTION_1}}` example: `Who is allowed to press send on a drafted reply today?`

---

## STOP

- Do not write “our agent sent 1,000 emails”
- Do not send

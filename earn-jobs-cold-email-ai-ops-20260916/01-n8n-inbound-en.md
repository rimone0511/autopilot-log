> **DRAFT_ONLY. DO NOT SEND.**  
> No secrets. No client PII. No fake metrics. Agent does not send.

# CE-01 — n8n inbound form (EN)

## Operator table (do not paste)

| key | value |
|---|---|
| pack | earn-jobs-cold-email-ai-ops-20260916 |
| id | CE-01 |
| theme | n8n workflow |
| lang | EN |
| mode | DRAFT_ONLY, HANDS |
| send | **forbidden** |
| smb_label | `SMB-A` (fictional) |
| chars_subject | short 42 / std 57 |
| chars_short | 628 |
| chars_standard | 1259 |

Facts: [FACTS.md](FACTS.md). Gate: [DRAFT_ONLY.md](DRAFT_ONLY.md).

Assumed public page (not a real company): a contact or inquiry form is visible; the ask is form → sheet → notify, with a **person** sending the first reply.

Out of scope: browser bots, scraping, auto-reply, ungated outbound.

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
- [ ] I can name a legal basis without stretching — or I skip
- [ ] No list, no sequence, no Gmail draft from this pack
- [ ] I do **not** click Send

---

## Subject (short)

```
Form to sheet, human send — not auto-reply
```

## Subject (standard)

```
Saw {{ONE_SPECIFIC_DETAIL}} — n8n setup with a human stop
```

---

## Short body

```
{{RECIPIENT_NAME}} — I saw {{ONE_SPECIFIC_DETAIL}} on your public {{PUBLIC_PAGE_KIND}}.

I set up n8n in the client's workspace: official connectors, a dummy run, then a hold queue. A person presses send. I do not click the live site for you. I do not keep keys.

{{DISPLAY_NAME}}, Japan, async {{TIMEZONE}}. Notes: {{PORTFOLIO_URL}}

Out of scope: bots, scraping, likes/follows.

{{QUESTION_1}}

This is a one-off draft, not a sequence. Ignore if it is a mismatch.

---
Advertisement (freelance n8n setup). Not sent.
{{DISPLAY_NAME}} · Japan · {{POSTAL_ADDRESS}}
Stop further marketing email: reply STOP to {{OPT_OUT_CONTACT}}.
```

---

## Standard body

```
{{RECIPIENT_NAME}} — I saw {{ONE_SPECIFIC_DETAIL}} on your public {{PUBLIC_PAGE_KIND}}.

I am {{DISPLAY_NAME}}. I build n8n workflows in the client's own Cloud or self-hosted instance: documented connectors and official APIs only. New inquiries land in a sheet or inbox you already use. Unclear rows wait. A person sends the first reply. I do not auto-reply. I do not scrape. I do not store your secrets.

Public notes: {{PORTFOLIO_URL}}. Same fail-closed habit on an official-API tool (private until a human gate opens; TikTok default is inbox, not unattended post): {{GITHUB_REPO_AUTOPILOT}}.

What I would name in a short scope, if you ever want one:
- Workflow in your n8n, imported off
- Connector list with secrets omitted
- Stop / rerun notes
- A check that the live sheet was not overwritten

I am Japan-based, English or Japanese, async {{TIMEZONE}}. Independent — not an n8n partner.

{{QUESTION_1}}

This is a one-off note, not a drip. If the page is the wrong desk, ignore it.

---
This message is an advertisement for freelance n8n / workflow setup. It is a git draft and has not been sent.
{{DISPLAY_NAME}} · {{CITY}}, {{COUNTRY}} · {{POSTAL_ADDRESS}}
To stop further marketing email, reply STOP to {{OPT_OUT_CONTACT}}.
Public: {{PORTFOLIO_URL}}
```

---

## Fictional fill (not a real SMB; do not send)

- Label: `SMB-A`
- `{{PUBLIC_PAGE_KIND}}` example: `contact page`
- `{{ONE_SPECIFIC_DETAIL}}` example: `the inquiry form promises a reply on business days`
- `{{QUESTION_1}}` example: `Which product holds new inquiries today, and who is allowed to send the first reply?`

---

## STOP

- No public hook → do not use
- Do not invent “we automated 20 agencies”
- Do not send

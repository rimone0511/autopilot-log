> **DRAFT_ONLY. DO NOT SEND.**  
> No fake intent scores. No auto-reply claims. Agent does not send.

# CE-05 — lead classify (EN)

## Operator table (do not paste)

| key | value |
|---|---|
| pack | earn-jobs-cold-email-ai-ops-20260916 |
| id | CE-05 |
| theme | lead classify |
| lang | EN |
| mode | DRAFT_ONLY, HANDS |
| send | **forbidden** |
| smb_label | `SMB-E` (fictional) |
| chars_subject | short 44 / std 68 |
| chars_short | 624 |
| chars_standard | 1083 |

Facts: [FACTS.md](FACTS.md). Gate: [DRAFT_ONLY.md](DRAFT_ONLY.md).

Assumed public page: mixed inbound (billing / support / sales) lands in one box.

Out of scope: auto-spam sequences, scraped lists, fake confidence percentages.

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
Labels plus an unsure bucket — no auto-reply
```

## Subject (standard)

```
{{ONE_SPECIFIC_DETAIL}} — route inbound, keep humans on unclear rows
```

---

## Short body

```
{{RECIPIENT_NAME}} — I saw {{ONE_SPECIFIC_DETAIL}} on your public {{PUBLIC_PAGE_KIND}}.

I set up inbound classify on your labels: billing / support / sales, plus an unsure bucket a person reviews. Nothing auto-replies. Nothing invoices. Accuracy is not guaranteed.

{{DISPLAY_NAME}}, Japan, async {{TIMEZONE}}. Notes: {{PORTFOLIO_URL}}

Out of scope: scraped lists, outbound sequences, fake intent scores.

{{QUESTION_1}}

One-off draft. Not a sequence.

---
Advertisement (freelance inbound classify). Not sent.
{{DISPLAY_NAME}} · Japan · {{POSTAL_ADDRESS}}
Stop further marketing email: reply STOP to {{OPT_OUT_CONTACT}}.
```

---

## Standard body

```
{{RECIPIENT_NAME}} — I saw {{ONE_SPECIFIC_DETAIL}} on your public {{PUBLIC_PAGE_KIND}}.

I am {{DISPLAY_NAME}}. The job is tagging and routing mail you already receive, on labels you already use. Unclear messages wait. A person decides. I do not buy lists. I do not score “intent” with a made-up number. I do not send the customer a reply.

Typical shape (n8n in your workspace, official connectors): inbound text in → label out → hold if unsure. AI is optional and off unless you add a suggest-only step you still review.

Public notes: {{PORTFOLIO_URL}}. Fail-closed official-API example: {{GITHUB_REPO_AUTOPILOT}}.

Japan-based, English or Japanese, async {{TIMEZONE}}. Independent. Not an n8n partner.

{{QUESTION_1}}

This is a one-off note. If inbound already has an owner and a queue, ignore it.

---
This message is an advertisement for freelance inbound classify / route setup. It is a git draft and has not been sent.
{{DISPLAY_NAME}} · {{CITY}}, {{COUNTRY}} · {{POSTAL_ADDRESS}}
To stop further marketing email, reply STOP to {{OPT_OUT_CONTACT}}.
Public: {{PORTFOLIO_URL}}
```

---

## Fictional fill (not a real SMB; do not send)

- Label: `SMB-E`
- `{{PUBLIC_PAGE_KIND}}` example: `contact page with one shared address`
- `{{ONE_SPECIFIC_DETAIL}}` example: `sales, press, and support share the same form`
- `{{QUESTION_1}}` example: `What labels do you already use, and who reviews the unsure pile?`

---

## STOP

- Do not write “92% accurate classifier”
- Do not send

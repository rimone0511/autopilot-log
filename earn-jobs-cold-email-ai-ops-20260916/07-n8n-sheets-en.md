> **DRAFT_ONLY. DO NOT SEND.**  
> No “we never lose a row” guarantees. Agent does not send.

# CE-07 — n8n sheets without overwrite (EN)

## Operator table (do not paste)

| key | value |
|---|---|
| pack | earn-jobs-cold-email-ai-ops-20260916 |
| id | CE-07 |
| theme | n8n workflow |
| lang | EN | 
| mode | DRAFT_ONLY, HANDS |
| send | **forbidden** |
| smb_label | `SMB-G` (fictional) |
| chars_subject | short 49 / std 60 |
| chars_short | 645 |
| chars_standard | 1129 |

Facts: [FACTS.md](FACTS.md). Gate: [DRAFT_ONLY.md](DRAFT_ONLY.md).

Assumed public page: a spreadsheet, booking table, or “we keep requests in a sheet” is described in public copy.

Out of scope: wiping production sheets, unofficial Google scrapers, partner-badge impersonation.

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
Append new rows — dummy run before the live sheet
```

## Subject (standard)

```
{{ONE_SPECIFIC_DETAIL}} — n8n append, not a silent overwrite
```

---

## Short body

```
{{RECIPIENT_NAME}} — I saw {{ONE_SPECIFIC_DETAIL}} on your public {{PUBLIC_PAGE_KIND}}.

I wire n8n to append rows with official connectors, on a copy first. The live sheet is not the dummy. A person confirms the mapping. I do not “clean up” production data as a surprise.

{{DISPLAY_NAME}}, Japan, async {{TIMEZONE}}. Notes: {{PORTFOLIO_URL}}

Out of scope: scrapers, bots that click the sheet UI, guaranteed zero data loss.

{{QUESTION_1}}

One-off draft. Not a sequence.

---
Advertisement (freelance n8n / sheet wiring). Not sent.
{{DISPLAY_NAME}} · Japan · {{POSTAL_ADDRESS}}
Stop further marketing email: reply STOP to {{OPT_OUT_CONTACT}}.
```

---

## Standard body

```
{{RECIPIENT_NAME}} — I saw {{ONE_SPECIFIC_DETAIL}} on your public {{PUBLIC_PAGE_KIND}}.

I am {{DISPLAY_NAME}}. Small ops jobs I take look like: form or mail in, documented Google/Sheets (or equivalent) connector, append-only until a human says otherwise. First run is dummy data. Then a check that existing rows are still there. Secrets stay in your n8n. I do not keep a copy of the workbook.

Public notes: {{PORTFOLIO_URL}}. Same “do not publish by accident” split on official APIs: {{GITHUB_REPO_AUTOPILOT}}.

Deliverables I would name if we ever scoped it: workflow (off), column map with secrets omitted, rerun notes, a written check that the live tab was not replaced.

Japan-based, English or Japanese, async {{TIMEZONE}}. Independent. Not a Google or n8n partner.

{{QUESTION_1}}

This is a one-off note. If a staffer already owns that sheet, ignore it.

---
This message is an advertisement for freelance n8n sheet wiring. It is a git draft and has not been sent.
{{DISPLAY_NAME}} · {{CITY}}, {{COUNTRY}} · {{POSTAL_ADDRESS}}
To stop further marketing email, reply STOP to {{OPT_OUT_CONTACT}}.
Public: {{PORTFOLIO_URL}}
```

---

## Fictional fill (not a real SMB; do not send)

- Label: `SMB-G`
- `{{PUBLIC_PAGE_KIND}}` example: `booking / request page`
- `{{ONE_SPECIFIC_DETAIL}}` example: `requests are collected in a spreadsheet you mention by name`
- `{{QUESTION_1}}` example: `Which tab is production, and is there already a copy we must not touch?`

---

## STOP

- Do not write “zero downtime for 40 shops”
- Do not send

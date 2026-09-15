> **DRAFT_ONLY. DO NOT SEND.**  
> No live invitations. No secrets. No recipient PII. Agent does not click Send.

# LI-W2-01 — Connection note: n8n (EN)

## Fact table (operator; do not paste)

| key | value |
|---|---|
| pack | earn-linkedin-outreach-wave2-20260916 |
| id | LI-W2-01 |
| desk | LinkedIn personal profile |
| type | Connection invitation **note** |
| seller_theme | n8n workflow |
| lang | EN |
| mode | DRAFT_ONLY, HANDS paste |
| draft | true |
| send | **forbidden** |
| promotional_note | **forbidden** (PCP) |
| urls_in_note | no |
| rate_in_prose | no |
| char_limit | 200 (Basic; live counter wins) |
| chars_note | 138 |
| detail_budget | keep `{{ONE_SPECIFIC_DETAIL}}` short; re-count after fill |

Assumed hook (not a real person): a public post or headline about n8n, webhooks, or official-API automation. Skip if you cannot point at one line on **this** profile.

Out of scope: Services pitch, InMail, “book a call”, scraping, partner badges.

---

## Composer fields (separate from prose)

| UI field | Paste / action |
|---|---|
| Add a note | fenced block below |
| Send / 送信 | **do not click** — [STOP-AT-PUBLISH.md](STOP-AT-PUBLISH.md) |
| InMail | do not open |

Empty hook → skip. Monthly note cap hit → park `note_cap_hit`. Do not send a blank invite.

---

## Send gate

- [ ] Profile opened on linkedin.com
- [ ] `{{ONE_SPECIFIC_DETAIL}}` is from **this** public post or headline
- [ ] Note is peer context, not a sell
- [ ] No URL, email, phone, or calendar link
- [ ] Live counter ≤ 200 after substitutions
- [ ] I do **not** click Send from this pack

---

## Connection note (≤200 after fill)

```
Saw {{ONE_SPECIFIC_DETAIL}}. I keep n8n on official APIs and a human stop before send. {{DISPLAY_NAME}}, Japan. Peer connect, not a pitch.
```

---

## Fictional fill (not a real member; do not send)

- Label: `Person A` (fictional)
- `{{ONE_SPECIFIC_DETAIL}}` example: `your note on webhook retries in n8n`
- `{{DISPLAY_NAME}}` example: `Yuta Ishida`

Filled example (for counting only): `Saw your note on webhook retries in n8n. I keep n8n on official APIs and a human stop before send. Yuta Ishida, Japan. Peer connect, not a pitch.`

---

## STOP

- Do not attach this note to a stranger with no public hook
- Do not rewrite it into a Services CTA
- Do not send

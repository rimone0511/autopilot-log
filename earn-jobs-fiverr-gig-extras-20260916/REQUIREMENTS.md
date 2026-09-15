# Requirements paste — unpublished Gig `build n8n automation with operator docs you can rerun`

JOBS PHASE. DRAFT_ONLY. English. Six required Free-text questions, then two optional extras.

Fiverr help: collect what you need before work starts; mark critical questions required; keep the list short. Do not ask for passwords, API keys, ID scans, or bank details.

Conservative ceiling: 200 characters per question (unofficial; this pack stays ≤ 135). Spaces count.

Voice matches the existing operator-docs n8n Gig (PR #6), not a different listing.

---

## R1 — Apps to connect

| UI | Value |
|---|---|
| Type | Free text |
| Required | Yes |
| Characters | 135 |

```
Which apps should this n8n automation connect? List each name and say if it has an official API (example: Gmail, Google Sheets, Slack).
```

---

## R2 — Manual steps today

| UI | Value |
|---|---|
| Type | Free text |
| Required | Yes |
| Characters | 120 |

```
What are the manual steps you do today, in order? Start with the trigger. End with the last action you still do by hand.
```

---

## R3 — Definition of done (workflow + operator notes)

| UI | Value |
|---|---|
| Type | Free text |
| Required | Yes |
| Characters | 116 |

```
What is done for this order? Name the happy-path result and the operator notes you must be able to rerun without me.
```

---

## R4 — No passwords in chat

| UI | Value |
|---|---|
| Type | Free text |
| Required | Yes |
| Characters | 127 |

```
Do not paste passwords, API keys, tokens, or login links here or in chat. Type exactly: I will enter credentials in n8n myself.
```

---

## R5 — Where n8n lives

| UI | Value |
|---|---|
| Type | Free text |
| Required | Yes |
| Characters | 79 |

```
Where will the workflow live: n8n Cloud, self-hosted n8n, or not installed yet?
```

---

## R6 — AI opt-in and failure path

| UI | Value |
|---|---|
| Type | Free text |
| Required | Yes |
| Characters | 116 |

```
Is this a no-AI order, or may I add a light classify, summarize, or draft step? If a step fails, what should happen?
```

---

## Optional extras (not required)

Fiverr help: add a multiple-choice row that introduces **one** Gig Extra, and an optional free-text “how did you find this Gig”. Do not stack several extras here. Do not invent live USD prices.

### RX — One Gig Extra (optional)

| UI | Value |
|---|---|
| Type | Multiple choice |
| Required | No |
| Characters | 75 |

```
Would you like one extra related n8n workflow as a Gig Extra on this order?
```

Choices (paste as options, not as the question):

```
No thanks
```

```
Yes, send a custom offer
```

```
Tell me more
```

Price stays a placeholder on the existing Gig extras row (`{{PRICE_EXTRA_WORKFLOW_USD}}` in PR #6). Do not type a dollar amount into this question.

### RD — How found (optional)

| UI | Value |
|---|---|
| Type | Free text |
| Required | No |
| Characters | 80 |

```
How did you find this Gig (Fiverr search, web search, profile, or repeat order)?
```

---

## Operator check

- [ ] Six required rows, order R1–R6
- [ ] Each of R1–R6 is Free text, not Multiple choice, not File
- [ ] Required is on for all six
- [ ] RX is Multiple choice, Required off; only one extra introduced
- [ ] RD is Free text, Required off
- [ ] No password, key, or ID request except the R4 refusal + typed confirmation
- [ ] Gig left **Draft** / unpublished

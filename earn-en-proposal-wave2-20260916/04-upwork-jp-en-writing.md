> **DRAFT_ONLY. DO NOT SEND.**  
> No live bids. No secrets. No client PII. Rates stay placeholders. Agent does not submit.

# EN-W2-04 — Upwork: JP/EN writing assist (cover letter)

## Fact table (operator; do not paste)

| key | value |
|---|---|
| pack | earn-en-proposal-wave2-20260916 |
| id | EN-W2-04 |
| desk | Upwork |
| type | Job proposal / cover letter |
| seller_theme | JP/EN writing assist |
| mode | DRAFT_ONLY, HANDS paste |
| draft | true |
| send | **forbidden** |
| rate_in_prose | no — form field only |
| chars_preview | 132 |
| chars_short | 644 |
| chars_standard | 1162 |

Assumed listing type (not a real job): bilingual operator docs, SOP, EN marketplace copy for a JP-origin process, or JP summaries of EN tickets. Writing assist — not “I am a US native in California.”

Out of scope: fake reviews, academic ghostwriting, location spoof, SEO spam farms, filling someone else’s KYC forms.

---

## Form fields (separate from prose)

| UI field | Paste / action |
|---|---|
| Bid type | Live form: hourly **or** fixed |
| Hourly (USD) | `{{HOURLY_RATE_USD}}` |
| Fixed price (USD) | `{{FIXED_PRICE_USD}}` |
| Duration | `{{DELIVERY_DAYS}}` |

Empty required rate → park `rate_required`. Do not invent USD in git.

---

## Send gate

- [ ] Job opened on upwork.com
- [ ] `{{ONE_SPECIFIC_DETAIL}}` is from this post
- [ ] The ask is operator / product / process writing, not review fraud
- [ ] Japan location stays honest
- [ ] I click Submit myself

---

## List preview (first line; rewrite first)

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". I would write that as bilingual operator text a second person can follow.
```

---

## Short paste

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". I would write that as bilingual operator text a second person can follow.

I am {{DISPLAY_NAME}}, Japan-based. Japanese is native; I work in English on-platform. I assist with JP/EN operator docs: SOPs, runbooks, listing copy that matches a real workflow, and short JP summaries of EN tickets. I do not invent a US city. I do not write fake reviews.

Public notes: {{PORTFOLIO_URL}}. Example of plain-language ops writing next to a real tool: {{GITHUB_REPO_AUTOPILOT}}.

Please keep scoping on Upwork Messages. Async in {{TIMEZONE}}.

Two questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}
```

---

## Standard paste

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". {{SCOPE_ONE_LINER}}

I am {{DISPLAY_NAME}}. JP/EN writing assist, here, means: take a process you already run (often n8n, a sheet, or an inbox) and leave text a non-engineer can rerun in the language the operator actually uses. I can draft EN for a JP-origin SOP, or JP notes for an EN ticket, and mark what I did not verify. I will not claim native US English or hide that I am in Japan.

I will not write testimonials you did not earn, academic papers, or “sound local” location lies. I will not put contact details in pre-contract copy. Secrets stay out of the document; I will flag any that appear in source material instead of copying them forward.

Deliverables I would outline:
1. Audience + tone one-pager (who presses the button)
2. The bilingual draft (EN working copy + JP operator notes, or the reverse — you choose)
3. A short change log of terms we must not invent (rates, metrics, partner badges)

Public notes: {{PORTFOLIO_URL}}. {{GITHUB_REPO_AUTOPILOT}}.

Price stays in the Upwork form fields. English + Japanese, async in {{TIMEZONE}}.

Questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}
```

---

## Fictional fill (not a real job; do not send)

- Label: `Client D` (fictional)
- Title example: `[FICTION] EN SOP for an n8n form-to-sheet path; JP sidebar for the operator`
- `{{SCOPE_ONE_LINER}}` example: `The workflow exists; the missing piece is a bilingual note of what to edit and what never to send.`
- `{{QUESTION_1}}` example: `Should the operator-facing page be Japanese-first with an English appendix, or the reverse?`
- `{{QUESTION_2}}` example: `Which terms must stay in English (API field names) even in the JP page?`

---

## STOP

- Do not spoof location or “native US copywriter” identity
- Do not paste the client’s unpublished copy into git
- Do not send

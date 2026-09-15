> **DRAFT_ONLY. DO NOT SEND.**  
> JOBS PHASE. Upwork cover letter only. No live bids. No secrets. No client PII.  
> Rates stay placeholders. Account may be blocked — agent does not submit.

# JOBS-06 — Upwork: operator docs / SOP (cover letter)

## Fact table (operator; do not paste)

See pack-level [FACT-TABLE.md](FACT-TABLE.md). Per-file copy:

| key | value |
|---|---|
| pack | earn-jobs-upwork-cover-letters-20260916 |
| id | JOBS-06 |
| desk | Upwork |
| type | Job proposal / cover letter |
| seller_theme | operator docs / SOP |
| phase | JOBS |
| mode | DRAFT_ONLY, HANDS paste |
| draft | true |
| send | **forbidden** (account may be blocked; even if not, this file does not send) |
| rate_in_prose | no — form field only |
| chars_preview | 140 |
| chars_short | 670 |
| chars_standard | 1233 |

Assumed listing type (not a real job): the workflow already exists (often n8n, a sheet, or an inbox). The missing piece is operator text a second person can follow — SOP, runbook, bilingual notes, change log. Writing assist, not “I am a US native in California.”

Out of scope: fake reviews, academic ghostwriting, location spoof, SEO spam farms, filling someone else’s KYC forms, dumping secrets into the doc.

---

## Form fields (separate from prose)

| UI field | Paste / action |
|---|---|
| Bid type | Live form: hourly **or** fixed |
| Hourly (USD) | `{{HOURLY_RATE_USD}}` |
| Fixed price (USD) | `{{FIXED_PRICE_USD}}` |
| Duration | `{{DELIVERY_DAYS}}` |
| Connects | Human per-job choice later. This pack: **do not spend, do not send** |

Empty required rate → park `rate_required`. Do not invent USD in git.

---

## Send gate

- [ ] Upwork account is actually usable (today: treat as **may be blocked**)
- [ ] Job opened on upwork.com
- [ ] `{{ONE_SPECIFIC_DETAIL}}` is from this post
- [ ] The ask is operator / process writing, not review fraud
- [ ] Japan location stays honest
- [ ] I would click Submit myself — **not now**

---

## List preview (first line; rewrite first)

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". I would write the SOP a second operator can follow, including what never to send.
```

---

## Short paste

```
You mentioned {{ONE_SPECIFIC_DETAIL}} on "{{JOB_TITLE}}". I would write the SOP a second operator can follow, including what never to send.

I am {{DISPLAY_NAME}}, Japan-based. Japanese is native; I work in English on-platform. I write operator docs next to real workflows: what starts it, what is safe to edit, where secrets live (not in the page), and how to rerun a failure. I do not invent a US city. I do not write fake reviews.

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

I am {{DISPLAY_NAME}}. Operator docs, here, means: take a process you already run (often n8n, a sheet, or an inbox) and leave text a non-engineer can rerun in the language the operator actually uses. I can draft EN for a JP-origin SOP, or JP notes for an EN ticket, and mark what I did not verify. I will not claim native US English or hide that I am in Japan.

I will not write testimonials you did not earn, academic papers, or “sound local” location lies. I will not put contact details in pre-contract copy. Secrets stay out of the document; I will flag any that appear in source material instead of copying them forward. Rates and partner badges stay out of the SOP unless you already published them.

Deliverables I would outline:
1. Audience + tone one-pager (who presses the button)
2. The SOP / runbook (EN working copy + JP operator notes, or the reverse — you choose)
3. A short change log of terms we must not invent (rates, metrics, partner badges)

Public notes: {{PORTFOLIO_URL}}. {{GITHUB_REPO_AUTOPILOT}}.

Price stays in the Upwork form fields. English + Japanese, async in {{TIMEZONE}}.

Questions:
1. {{QUESTION_1}}
2. {{QUESTION_2}}
```

---

## Fictional fill (not a real job; do not send)

- Label: `Job-F` (fictional)
- Title example: `[FICTION] EN SOP for an n8n form-to-sheet path; JP sidebar for the operator`
- `{{SCOPE_ONE_LINER}}` example: `The workflow exists; the missing piece is a bilingual note of what to edit and what never to send.`
- `{{QUESTION_1}}` example: `Should the operator-facing page be Japanese-first with an English appendix, or the reverse?`
- `{{QUESTION_2}}` example: `Which terms must stay in English (API field names) even in the JP page?`

---

## STOP

- Do not spoof location or “native US copywriter” identity
- Do not paste the client’s unpublished copy into git
- Do not send

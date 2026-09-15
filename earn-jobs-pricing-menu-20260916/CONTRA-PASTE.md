# Contra Independent paste — DRAFT_ONLY

Desk: Contra Independent / Share work  
Pack: 2026-09-16  
Mode: **DRAFT_ONLY. Save as unpublished. Do not Publish. Do not buy Pro.**

Help — add services: https://help.contra.com/en/articles/9322412-how-to-add-services-to-your-contra-profile  
Help — fees (re-read; do not freeze): https://help.contra.com/en/articles/12642699-fees-on-contra-for-independents  
Public pricing (Pro cited; **do not buy**): https://contra.com/pricing

From help 9322412 (dateModified 2026-02-13 on the article page):

1. Service name and cover image  
2. Tags: 1–3 Role, 1–5 Tools, optionally 1–3 Industry  
3. Description (process, deliverables, requirements; FAQ optional)  
4. Payment: **one-time**, **ongoing** (hour / week / month), or **Contact for pricing**  
5. **Publish** or **Save as unpublished** ← this pack stops at unpublished

Cover image: skip from this agent. No partner logos (n8n, Contra, AI labs).  
Wallet / Persona / Add account: [DRAFT_ONLY.md](DRAFT_ONLY.md).  
MAIN Google only. Profile is **Independent / Share work**, not Hire.

---

## 0. Pricing control (do not invent USD)

**Preferred until a human chooses a number:** **Contact for pricing** (official option).

If the human already has a private ledger amount, paste `{{PRICE_USD_SKU_*}}` as **one-time**. Do not commit the filled number.

Do not use ongoing hourly unless the human sets `{{HOURLY_USD}}` locally. Empty hourly → `rate_empty`.

Do not paste Coconala yen into Contra. Do not paste Gumroad tokens into a Contra hourly box.

Four **separate** unpublished services (a menu of skills, per help). Do not publish four identical clones.

---

## Shared tags (all four)

Help: 1–3 Role, 1–5 Tools, 0–3 Industry. Live list wins. Skip any tag the picker does not offer. Do not invent IDs.

```
Role: Automation Specialist
Role: Technical Writer
Tools: n8n
Tools: Google Sheets
Tools: Notion
Industry: (skip if unsure)
```

Maximum two Role tags per service. Starter / classifier / approval-gate: **Automation Specialist** only. Docs: **Technical Writer** + **Automation Specialist** if the picker allows two.

Do not tag xAI, Grok, ChatGPT as a partner.

---

## 1. n8n starter

### Service name

```
n8n starter intake — table + notify, you send
```

### Payment

Contact for pricing  
(or one-time `{{PRICE_USD_SKU_STARTER}}` if a human already chose)

Draft-suggestion delivery (custom work, not a platform default): 7 calendar days, 1 revision.

### Description (buyer-facing; no “unpublished”)

```
I build one n8n intake path on your instance: form, webhook, or sheet row into a table, then notify a person. You send. I do not auto-reply or post in your name.

You get the workflow shape (official APIs and webhooks only) and a short SOP: what starts it, what to edit, where secrets live, how to rerun. I do not drive browsers, scrape sites, or automate likes, follows, or views.

Includes: one trigger, one path, notify-a-human, 1 revision during the delivery window.
Does not include: classifier labels, approval-before-send, n8n hosting, accuracy %, or unattended publishing.

Start with a short write-up of the manual steps and whether you already have n8n Cloud or self-hosted. Enter credentials in n8n. Do not paste keys in Contra chat.

I am an independent. I am not a partner of n8n or Contra.
```

### Requirements

```
1. A short write-up of the current manual intake (input, store, who sends).
2. n8n Cloud or self-hosted — or say if it is not installed yet.
3. Dummy sample with personal data removed.
Do not send passwords, API keys, or ID documents in chat.
```

---

## 2. classifier

### Service name

```
n8n inquiry classifier — labels + hold, no auto-reply
```

### Payment

Contact for pricing (or one-time `{{PRICE_USD_SKU_CLASSIFIER}}`)

Draft suggestion: 7 calendar days, 1 revision.

### Description

```
I map inbound text onto labels you already use. Anything unclear goes to an uncertain / hold queue. You send. There is no auto-reply.

Official APIs and webhooks only. AI is optional; default is rules or a human-reviewed step. I will not add a model call if you say no AI.

Includes: label mapping, hold queue, notify-a-human, 1 same-scope revision.
Does not include: auto-send, an approval gate, hosting, or an accuracy percentage.

I am an independent, not an n8n partner.
```

### Requirements

```
1. Your existing label list (for example billing / support / sales).
2. Where unclear items should sit.
3. Dummy inbound samples with names removed.
Do not paste secrets in chat.
```

---

## 3. approval-gate

### Service name

```
n8n approval gate — human must approve before send
```

### Payment

Contact for pricing (or one-time `{{PRICE_USD_SKU_APPROVAL}}`)

Draft suggestion: 10 calendar days, 2 revisions.

### Description

```
I add a fail-closed approval step in n8n. Nothing goes outbound until a person approves. Reject, missing, unknown, and timeout do not send. There is no auto-send-on-timeout.

You keep live notify credentials in your n8n. I hand over the gate shape, failure notes, and a short SOP.

Includes: approve-required gate, fail-closed paths, 2 revisions in the delivery window.
Does not include: company-wide approval platforms, SLA minutes, hosting, scraping, or engagement bots.

I am an independent, not an n8n partner.
```

### Requirements

```
1. Who approves, and where (sheet, chat, or mail).
2. What must never send without a person.
3. Dummy payload with secrets removed.
Do not paste live notify tokens in chat.
```

---

## 4. docs

### Service name

```
n8n operator docs — SOP and rerun notes, no new flow
```

### Payment

Contact for pricing (or one-time `{{PRICE_USD_SKU_DOCS}}`)

Draft suggestion: 5 calendar days, 1 revision.

### Description

```
I write operator docs for a workflow you already have. I do not build a new n8n flow in this service.

You get Markdown: what starts it, secret vs editable fields, how to rerun, what to do on failure. English, or a short JA/EN pair if you ask.

Includes: one-flow SOP, optional change log, 1 revision.
Does not include: a new workflow, hosting purchase, or unrelated source code.

Send screenshots with secrets hidden. I am an independent, not an n8n partner.
```

### Requirements

```
1. Screenshots or an export with secrets hidden.
2. Who will rerun the flow (operator, not only you).
3. Language: English, Japanese, or both.
Do not send live credentials.
```

---

## 5. Optional FAQ (same for all four; skip if the form is long)

**Q: Do you use AI?**  
Only if you ask. Default is a human-designed n8n path plus docs. If you want no AI, say so. I do not deliver unmodified model output.

**Q: Are you affiliated with n8n or Contra?**  
No. Independent seller. No partner badges.

**Q: Will you publish to my social accounts?**  
Not as an unattended public post. Official APIs only. You keep the publish switch.

**Q: How do revisions work?**  
Same-scope fixes inside the delivery window (1 or 2 depending on the service). A new workflow is a new service. Extra revisions are a separate line (`{{PRICE_ADDON_REVISION_USD}}` if a human later sets it).

---

## 6. One-page menu (if Contra allows a single service instead of four)

Only if the human decides **not** to create four cards. Still **Save as unpublished**. Prefer **Contact for pricing**.

Name:

```
n8n menu — intake, classifier, approval gate, or docs
```

Description: paste the English short menu fence in [SKU-MENU-EN.md](SKU-MENU-EN.md).

---

## 7. Character counts (fenced paste, `len()`, 2026-09-16)

Help 9322412 does not cite a hard description cap. Keep scannable. Live form wins.

| Block | This pack |
|---|---|
| Service name starter / classifier / approval / docs / combo | 45 / 53 / 50 / 52 / 53 |
| Description ×4 | 803 / 474 / 514 / 459 |
| Requirements ×4 | 242 / 178 / 172 / 172 |

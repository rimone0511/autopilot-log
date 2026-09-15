# Seller pricing menu (English) — DRAFT_ONLY

Pack date: 2026-09-16  
Desks: Coconala / Gumroad / Contra Independent  
Mode: **DRAFT_ONLY. Do not publish. Do not send an estimate.**

Every price is a `{{PRICE_*}}` token. Do not commit yen or USD.
The ladder below is a **draft suggestion**. It is not a market study.

---

## DRAFT SUGGESTION ladder (not a market fact)

Do not treat this as a comparable, a going rate, or a GMV forecast.
Do not copy a competitor’s number into git.

Hypothesis order (narrower / cheaper → heavier / dearer):

1. **docs** — no new workflow; SOP / runbook only
2. **n8n starter** — intake → table → notify; a person sends
3. **classifier** — labels + uncertain / hold; no auto-reply
4. **approval-gate** — human approve before outbound; fail closed

Do not paste the same number onto all three desks. The product is not the same.

| Desk | What this menu is selling | Draft hint (hypothesis, not a quote) |
|---|---|---|
| Coconala | Custom work (or an estimate reply) | Category floor from official table. ¥500 on `guide_sell` is a platform minimum, not a recommended price |
| Gumroad | Digital download (stubs / markdown) | May sit below custom-build. Do not publish at $0 “to test checkout” |
| Contra | Independent **Service** | Official **Contact for pricing** is allowed until a human chooses a number |

A human fills `{{PRICE_*}}` on a private ledger. Do not commit the filled values.

---

## SKU list

| Code | Short name | One line | JPY token | USD token |
|---|---|---|---|---|
| `SKU-STARTER` | n8n starter | Intake lands in a table; a person is notified; a person sends | `{{PRICE_JPY_SKU_STARTER}}` | `{{PRICE_USD_SKU_STARTER}}` |
| `SKU-CLASSIFIER` | classifier | Inbound text → labels; unclear goes to uncertain / hold | `{{PRICE_JPY_SKU_CLASSIFIER}}` | `{{PRICE_USD_SKU_CLASSIFIER}}` |
| `SKU-APPROVAL` | approval-gate | Human **approve** before outbound; reject / missing / timeout fail closed | `{{PRICE_JPY_SKU_APPROVAL}}` | `{{PRICE_USD_SKU_APPROVAL}}` |
| `SKU-DOCS` | docs | Operator SOP for a workflow the buyer already has; no new flow | `{{PRICE_JPY_SKU_DOCS}}` | `{{PRICE_USD_SKU_DOCS}}` |

Delivery / revisions (**draft suggestion** for custom desks, not an official default; unused on Gumroad download):

| SKU | Calendar days | Revisions included |
|---|---|---|
| starter | 7 | 1 |
| classifier | 7 | 1 |
| approval-gate | 10 | 2 |
| docs | 5 | 1 |

Extra revision: `{{PRICE_ADDON_REVISION_JPY}}` / `{{PRICE_ADDON_REVISION_USD}}` (separate line item. No unlimited revisions).

---

## Inclusions / exclusions

### n8n starter

**Includes**

- One trigger (form, webhook, or sheet row)
- One path into a table (or equivalent store)
- Notify a human (mail / chat / sheet — buyer chooses)
- Short SOP: what starts it, what to edit, where secrets live, how to rerun
- Official connectors / official APIs / webhooks only

**Does not include**

- Auto-reply, auto-send, unattended public posting
- Classification labels or an approval gate (those are other SKUs)
- Browser automation, scraping, likes / follows / view bots
- Buying n8n hosting
- Accuracy %, SLA, or income promises

### classifier

**Includes**

- Map inbound text onto labels the buyer already uses
- Unclear items go to **uncertain / hold**
- Notify a human. The buyer sends
- Stubs or equivalent notes (Gumroad: inactive JSON)

**Does not include**

- Auto-reply, auto-invoice, posting in the buyer’s name
- A numeric accuracy guarantee
- Approve-then-send (that is approval-gate)
- Required AI. Stubs ship with AI off. If a model is added later, a person still reviews

### approval-gate

**Includes**

- A human **approve** is required before anything goes outbound
- Reject / missing / unknown / timeout **fail closed** (nothing sends)
- A shape for the post-approve notify path (live send nodes stay in the buyer’s n8n; drafts here are NoOp)
- Short failure notes

**Does not include**

- Auto-send on timeout
- Live notify credentials
- A company-wide approval platform
- An SLA (approve within N minutes, and so on)

### docs

**Includes**

- An SOP / runbook for one existing workflow (or screens the buyer provides)
- Rerun steps, secret vs editable fields, what to do on failure
- A change log if the buyer asks (what changed, what to re-test)
- English, or a short JA/EN pair if the buyer asks

**Does not include**

- Building a new n8n workflow (that is starter / classifier / approval-gate)
- Source code of unrelated products
- Buying hosting in the buyer’s name

### Out of scope for all four

- Browser automation and scraping
- Engagement automation (likes, follows, views, comments)
- Unattended social publishing, or posting content the buyer does not have rights to
- Entering passwords, API keys, or ID documents for the buyer
- Fake partner badges (n8n / Coconala / Gumroad / Contra / AI labs)
- Sheet-sync pack (Gumroad SKU-3) — not this menu

---

## Revision policy (English paste)

Buyer-facing. Do not write “unpublished draft” inside the fence.

```
A revision is a same-scope fix. A new workflow or a new label set is a new estimate.

- starter / classifier / docs: 1 revision during the delivery window
- approval-gate: 2 revisions during the delivery window
- Extra revisions: paid add-on (amount in the price field, not in this paragraph)
- Unlimited revisions and free post-delivery rebuilds are not included
- Do not paste secrets (keys, passwords, ID) in chat. Enter them in n8n
- Changing the flow into auto-send or unattended publish is out of scope
```

Coconala’s platform “return of a formal delivery” (guide: one buyer return) is not the same counter as the work revisions above. The live form wins.

---

## Paste-ready short menu (English)

For a Contra service description, a Gumroad “additional details” box, or an operator one-pager. Prices stay tokens. Do not write “draft” inside this fence.

```
n8n work menu. Official APIs and webhooks only. A person sends and a person publishes.

1. Starter intake — form or sheet in, notify a person. You send. Price {{PRICE_USD_SKU_STARTER}}
2. Classifier — map inbound text to your labels; unclear goes to hold. No auto-reply. Price {{PRICE_USD_SKU_CLASSIFIER}}
3. Approval-gate — nothing outbound until a person approves. Missing or unknown fails closed. Price {{PRICE_USD_SKU_APPROVAL}}
4. Docs — rerun notes for a workflow you already have. No new flow. Price {{PRICE_USD_SKU_DOCS}}

Not included: browser bots, scraping, engagement automation, hosting purchase, accuracy %.
Revisions: 1–2 depending on SKU. Extra revisions are a separate line. Do not paste keys in chat.
```

---

## Do not do from this file

- Publish on Coconala, Gumroad, or Contra
- State a yen or USD figure as a researched rate
- Real client names, live emails, or secrets

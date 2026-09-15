# Three-tier paste — Starter / Standard / Premium

Desk: Upwork Project Catalog  
Pack: 2026-09-16  
Mode: **DRAFT_ONLY — do not Submit**  
Buyer-facing language: English

Public help (create-project): offer **one or three** package tiers named
**Starter, Standard, Advanced**; prices **$5–$500,000 USD**; add-ons;
delivery in **calendar days** (weekends count); revisions during delivery.

This polish keeps three tiers. Buyer-facing labels are
**Starter / Standard / Premium** (aligned with the Fiverr sibling’s
Premium column). If the live form column is **Advanced**, paste the
Premium block there. Do not create a fourth column.

Prices stay `{{…}}`. Do not invent a live quote.

---

## 0. Form mapping

| This pack | Official help column | Sibling Catalog draft | Fiverr sibling package name |
|---|---|---|---|
| Starter | Starter | Starter | Basic — `Starter workflow` |
| Standard (default) | Standard | Standard | Standard — `Production workflow` |
| Premium | Advanced | Advanced | Premium — `Workflow and SOP` |

Keep **Upwork** scope numbers (Premium = up to **3** related workflows,
14 calendar days). Do not copy Fiverr’s “up to 2 / 7 days” into this form.

If category-specific **service tier option** checkboxes appear, map them
from the matrix below. Do not invent hidden option IDs. Skip any option
that does not fit (resources: you do not have to include every suggested
option).

---

## 1. Matrix

| | Starter | Standard | Premium |
|---|---|---|---|
| Package title | Single-path n8n workflow plus short SOP | Production n8n workflow plus SOP and change log | Related n8n workflows plus operator runbook |
| Price USD | `{{TIER_STARTER_USD}}` | `{{TIER_STANDARD_USD}}` | `{{TIER_PREMIUM_USD}}` (alias `{{TIER_ADVANCED_USD}}`) |
| Delivery (calendar days) | 7 | 10 | 14 |
| Revisions | 1 | 2 | 3 |
| n8n workflows | 1 | 1 | up to 3, same process family |
| Failure handling | notify **or** retry | retries **and** a failure alert | retries, alert, plus failure-drill notes |
| Docs | short SOP | SOP + change log + written async handoff | runbook + change log + failure-drill notes |
| AI steps | none unless the buyer named one classify / summarize / draft step in requirements | same, still one process | same, still one process family |
| Zapier / Make rebuild | no | no | no (written plan is an add-on only) |
| n8n hosting purchase | no | no | no |
| Scraping / engagement / unattended publish | no | no | no |

Standard is the default most buyers should pick. Starter is a single trail.
Premium is still one process **family**, not a company rebuild.

---

## 2. Starter — paste

Package title (39 characters):

```
Single-path n8n workflow plus short SOP
```

Package description (651 characters):

```
One named process. One n8n workflow. One short operator SOP.

Includes:
- One trigger (form, webhook, schedule, or sheet row)
- Steps for that single path (official APIs, sheets, or mail/chat notify)
- Notify or retry on failure (you choose in requirements)
- A short SOP: what starts it, what to edit, where secrets live, how to rerun
- One revision during the delivery window

Does not include:
- A second workflow, or retries and a failure alert together (that is Standard)
- Company-wide automation
- Scraping a site with no official API
- Social engagement (likes, follows, comments, fake views)
- Publishing to YouTube, TikTok, or other channels
```

---

## 3. Standard — paste (default)

Package title (47 characters):

```
Production n8n workflow plus SOP and change log
```

Package description (517 characters):

```
One production path a non-engineer can rerun without me in the chat.

Includes:
- One n8n workflow for one named process
- Retries and a failure alert (inbox, sheet, or chat -- you choose in requirements)
- Operator SOP
- Change log (what changed, why, what to re-test)
- Written async handoff (not an open retainer)
- Two revisions during the delivery window

Does not include:
- A second unrelated process
- A Zapier or Make rebuild
- Unofficial scraping
- Engagement automation
- Publishing on your social accounts
```

---

## 4. Premium — paste (Advanced column if the form uses that name)

Package title (43 characters):

```
Related n8n workflows plus operator runbook
```

Package description (557 characters):

```
Up to three related n8n workflows in one process family, plus a runbook.

Includes:
- Up to three workflows that share the same trigger family or the same destination
- Retries, a failure alert, and short failure-drill notes
- Operator runbook a non-engineer can follow
- Change log
- Three revisions during the delivery window

Does not include:
- An all-department rebuild
- Partner-directory status (n8n / Zapier / Make)
- Scraping, engagement automation, or unattended social publishing
- Source code of unrelated products
- Buying n8n Cloud or a server
```

---

## 5. Add-ons (draft text only; do not pay to feature)

Public help lists faster delivery, extra revisions, and extra deliverables
as common add-ons. Skip anything that looks like a **boost**, **featured
listing**, or **Connects** purchase.

```
Extra-fast delivery (set calendar days in the form) -- {{ADDON_FAST_USD}}

Extra revision after the operator tests the workflow -- {{ADDON_REVISION_USD}}, +2 calendar days

Second small workflow on the same stack -- {{ADDON_EXTRA_WORKFLOW_USD}}, +4 calendar days

Written Zapier or Make to n8n migration plan (document only, not the rebuild) -- {{ADDON_MIGRATION_PLAN_USD}}, +3 calendar days
```

---

## 6. What changed vs the original Catalog draft

| Item | Original (`…-catalog-draft-…`) | This polish |
|---|---|---|
| Third-tier **buyer** name | Advanced | Premium (Advanced = form alias) |
| Third-tier price token | `{{TIER_ADVANCED_USD}}` only | `{{TIER_PREMIUM_USD}}` + Advanced alias |
| Standard title | `Production n8n workflow, SOP, and change log` | `Production n8n workflow plus SOP and change log` |
| Premium title | `Operator pack: related workflows plus runbook` | `Related n8n workflows plus operator runbook` |
| Starter exclude | listed “second workflow” only | names Standard as the retries+alert step-up |
| Premium exclude | no hosting line | adds “Buying n8n Cloud or a server” |
| Add-ons | three | four (extra-fast delivery, help-listed) |
| Prices | placeholders | still placeholders; empty → `rate_required` |

Scope counts (1 / 1 / up to 3 workflows; 7 / 10 / 14 days; 1 / 2 / 3 revisions)
are unchanged so CU handoff and the original draft stay compatible.

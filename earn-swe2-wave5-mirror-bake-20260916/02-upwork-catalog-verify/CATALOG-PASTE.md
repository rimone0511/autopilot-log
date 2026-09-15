# Upwork Project Catalog -- 3-tier DRAFT paste

Desk: Upwork Project Catalog
Seller: Yuta Ishida / 石田祐太
Offer: n8n + AI automation + operator docs
Pack: 2026-09-16
Mode: **DRAFT ONLY -- do not submit**

Public entry (re-check at click-time):

- Home: https://www.upwork.com/
- Catalog: https://www.upwork.com/catalog
- Create project (help): https://support.upwork.com/hc/en-us/articles/360057397533-Create-a-project
- Best-project tips: https://support.upwork.com/hc/en-us/articles/360058122033-How-to-build-your-best-project-in-Project-Catalog
- Review process: https://support.upwork.com/hc/en-us/articles/4408644453395-How-we-review-your-Project-Catalog-project
- Description length: https://www.upwork.com/resources/catalog-product-description (121–1,200 characters)
- Title: "You will get" is prepended; **do not type those three words**; max **75 characters** after them
- Freelancer Catalog intro: https://support.upwork.com/hc/en-us/articles/360058234233-How-to-get-started-with-Project-Catalog-as-a-freelancer

Path if a human later types into the UI (still do not submit): Find Work → Your services → Create Project.

---

## 1. Project overview fields

| UI field | Paste value | Notes |
|---|---|---|
| Title (after "You will get") | `a production n8n workflow plus operator docs you can rerun` | 58 characters. Do not repeat "You will get". Regular capitalization. |
| Category | confirm in live picker | First try: Development & IT → Scripts & Utilities → Scripting & Automation. If the 2026 picker shows a closer Automation / n8n specialty, use that. Do not pick Other. |
| Attributes | Language: English. Platform: n8n if listed | Confirm checkboxes in UI. Do not invent hidden IDs. |
| Search tags (max 5) | pick from the **standardized** list: `n8n`, `automation`, `API`, `documentation`, `SOP` | Type-to-search; if a token is missing, use the nearest official tag. |
| Specifics / image tags | only if the category offers them | No client PII in sample images. No other-company logos (Catalog image rules). |

Do not put `{{EMAIL}}`, `{{PHONE_E164}}`, or a "message me off Upwork" line anywhere below.

---

## 2. Three tiers (Starter / Standard / Advanced)

Prices stay placeholders. Do not invent a live quote in git. Delivery is **calendar days** (Upwork counts weekends). Revisions are during the delivery window.

### 2.1 Matrix

| | Starter | Standard | Advanced |
|---|---|---|---|
| Package title | Single-path n8n workflow plus short SOP | Production n8n workflow, SOP, and change log | Operator pack: related workflows plus runbook |
| Price USD | `{{TIER_STARTER_USD}}` | `{{TIER_STANDARD_USD}}` | `{{TIER_ADVANCED_USD}}` |
| Delivery (calendar days) | 7 | 10 | 14 |
| Revisions | 1 | 2 | 3 |
| n8n workflows | 1 | 1 | up to 3, same process family |
| Failure handling | notify **or** retry | retries **and** a failure alert | retries, alert, plus failure-drill notes |
| Docs | short SOP | SOP + change log + written async handoff | runbook + change log + failure-drill notes |
| AI steps | none unless the buyer named one classify/summarize/draft step in requirements | same, still one process | same, still one process family |
| Zapier/Make rebuild | no | no | no (written plan is an add-on only) |

### 2.2 Starter -- paste

Package title:

```
Single-path n8n workflow plus short SOP
```

Package description:

```
One process, one n8n workflow, one short SOP.

Includes:
- One trigger (form, webhook, schedule, or sheet row)
- Up to the steps needed for that single path (APIs, sheets, or mail/chat notify)
- A short operator SOP: what starts it, what to edit, where secrets live, how to rerun
- One revision during delivery

Does not include:
- A second workflow
- Company-wide automation
- Scraping a site with no official API
- Social engagement (likes, follows, comments, fake views)
- Publishing to YouTube, TikTok, or other channels
```

### 2.3 Standard -- paste (default)

Package title:

```
Production n8n workflow, SOP, and change log
```

Package description:

```
One production path a non-engineer can rerun without me in the chat.

Includes:
- One n8n workflow for one named process
- Retries and a failure alert (inbox, sheet, or chat -- you choose in requirements)
- Operator SOP
- Change log (what changed, why, what to re-test)
- Written async handoff (not an open retainer)
- Two revisions during delivery

Does not include:
- A second unrelated process
- A Zapier or Make rebuild
- Unofficial scraping
- Engagement automation
- Publishing on your social accounts
```

### 2.4 Advanced -- paste

Package title:

```
Operator pack: related workflows plus runbook
```

Package description:

```
Up to three related n8n workflows in one process family, plus a runbook.

Includes:
- Up to three workflows that share the same trigger family or the same destination
- Retries, a failure alert, and short failure-drill notes
- Operator runbook a non-engineer can follow
- Change log
- Three revisions during delivery

Does not include:
- An all-department rebuild
- Partner-directory status (n8n / Zapier / Make)
- Scraping, engagement automation, or unattended social publishing
- Source code of unrelated products
```

### 2.5 Add-ons (draft text only; do not pay to feature)

```
Extra revision after the operator tests the workflow -- {{ADDON_REVISION_USD}}, +2 calendar days

Second small workflow on the same stack -- {{ADDON_EXTRA_WORKFLOW_USD}}, +4 calendar days

Written Zapier or Make to n8n migration plan (document only, not the rebuild) -- {{ADDON_MIGRATION_PLAN_USD}}, +3 calendar days
```

Skip anything that looks like a **boost**, **featured listing**, or **Connects** purchase.

---

## 3. Project summary -- 800 characters (Catalog box)

Upwork public guide: longer than 120 characters, max 1,200. This paste is **800 characters**.
Working 800-word overview: [overview-en-800.md](overview-en-800.md).

```
I build n8n workflows and the operator docs a non-engineer can follow after I leave.

You get one scoped process, not a company rebuild: a trigger, honest API or sheet steps, a failure alert or retry, and a short SOP covering what starts it, what to edit, where secrets live, and how to rerun. I do not scrape unofficial surfaces, automate likes or follows, or publish to your social accounts. Upload and publish stay separate.

English, async, {{TIMEZONE}}. Location: {{CITY}}, {{COUNTRY}}. Work stays on Upwork. Extra scope is a higher tier or a new project.

Pick Starter for one simple path, Standard for production retries plus a change log, Advanced for up to three related workflows and a runbook. Fill the requirements with the process in bullets and tool names. Please do not send passwords.
```

---

## 4. Project steps (workroom)

Upwork already shows getting started / doing the work / final review. Extra steps to add:

```
1. Lock scope from the requirements (process, tools, n8n Cloud vs self-host, good vs bad output).
2. Build the workflow and dry-run with placeholder credentials.
3. Write the SOP (and change log / runbook for the paid tier).
4. Apply included revisions from the operator test notes.
```

---

## 5. FAQs (max useful set; keep on-platform)

**Q. Do you scrape websites or automate likes and follows?**
A. No. Official APIs, documented webhooks, or first-party connectors only. No engagement automation.

**Q. Will you publish to my YouTube or TikTok?**
A. Not in this project. Upload and publish stay separate. You keep the posting switch.

**Q. What if my process is bigger than these tiers?**
A. Do not force Starter. Use Standard or Advanced, or a later custom contract. Catalog is predefined work.

**Q. What do you need before the delivery clock starts?**
A. The mandatory requirements below. Upwork cancels the project if those are not met within 48 hours.

**Q. Can we work off Upwork?**
A. No. Chat, files, and payment stay on Upwork.

---

## 6. Requirements for the client (mandatory unless noted)

Delivery starts when mandatory requirements are met.

1. **(mandatory, free text)** Describe the one process in 5–10 bullets: trigger, steps, done.
2. **(mandatory, free text)** Name the tools to connect. Names only. No passwords.
3. **(mandatory, multiple choice)** n8n hosting: `n8n Cloud` / `self-host` / `not sure -- advise in SOP`.
4. **(mandatory, free text)** One example of a good output and one example of a bad output.
5. **(optional, attachment)** Screenshot of the current manual steps, secrets cropped.
6. **(optional, free text)** Preferred failure channel: email, sheet row, or chat tool name.

Do not ask for live credentials in this form. Placeholder credentials only until a later paid job actually starts -- and this pack does not start a job.

---

## 7. Gallery (do not upload ID)

If a human later adds gallery files from a local folder (not git):

- Original diagram or screenshot of a **sanitized** demo workflow (no tokens, no inbox contents, no client names).
- Optional PDF of a sample SOP with secrets already cropped.
- Cover image: your own diagram, not a stock collage, not the Upwork logo, not the n8n logo.

Do not attach Autopilot Log as if this Catalog item were that CLI. It is a public example of the fail-closed habit, not the deliverable.

---

## 8. Finalize screen -- leave it

| Field | Draft stance |
|---|---|
| Concurrent projects | `1` if asked, then stop |
| Rights confirmation | do not submit |
| Terms checkbox | do not submit |
| Submit for review | **STOP** |

Submitting puts the listing in Upwork's review queue. That is publish. Out of scope.

---

## 9. Activity note

Verdict: **needs_check** for Catalog browse from this environment; marketplace product is **not treated as closed**.

Evidence (2026-09-15), no traffic totals invented:

- Upwork help articles for creating, reviewing, and writing Catalog projects returned live content.
- `https://www.upwork.com/catalog` from this environment presented a JavaScript / verification interstitial, so listing freshness was **not** counted here (same class of block as a Cloudflare wall: not proof the desk is dead).
- Wave A queue already marks Upwork as an alive seller desk (`next`, MAIN Google, KYC → morning stop).

Do not write GMV, job counts, or "Connects required to list." Confirm at click-time whether Create Project is visible on the logged-in freelancer account -- and still do not submit.

---

## 10. Operator notes (JP / EN)

- English listing. Legal name and location stay accurate (`{{COUNTRY}}` / `{{CITY}}`). Japan is fine.
- MAIN Google only. Do not open a second Upwork account for this pack.
- Profile overview is a different box from this Catalog summary. If you paste a profile bio, use the 800-word file only after cutting contact methods; the Catalog summary must stay the 800-character block.
- n8n Experts / Zapier / Make partner applications are Wave C **LATE** and are not this listing.

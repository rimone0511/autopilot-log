# Categories — LinkedIn Service Page (JOBS DRAFT)

Desk: LinkedIn **Services** on the existing recovered **personal** profile  
Mode: **`DRAFT_ONLY`** — fill the picker; **do not Save** if Save publishes ([STOP-AT-SAVE.md](STOP-AT-SAVE.md))  
Cap: **up to 10** (LinkedIn taxonomy). Prefer **3–6 honest** types.

Official create help: add the services you provide ([a569554](https://www.linkedin.com/help/linkedin/answer/a569554)). Company-Page help notes: if a category is missing, it may not be available ([a7433052](https://www.linkedin.com/help/linkedin/answer/a7433052)). Same rule on personal: **type-to-search only**. Do not invent category IDs. Do not type a custom free-text category.

`n8n` may **not** exist as a LinkedIn service type. Use Software Development / Automation neighbours.

## Search-for order (live picker wins)

| Priority | Search for | Use if… |
|---|---|---|
| 1 | Software Development | listed |
| 2 | Automation / Workflow / Integration | closest token to n8n |
| 3 | IT consulting / Consulting | only if it is clearly software/process, not life coaching |
| 4 | Technical writing / Documentation | if listed as a service type |
| 5 | API / Web development | only if listed and accurate |

Stop adding once 3–6 honest matches are on. Do not stuff ten vague umbrellas.

## Do not pick

Home Improvement, Photography, Real Estate, coaching-as-life-advice, recruiting, “I do everything,” or any category that is not this seller’s work (n8n workflows, official APIs, operator docs).

## Already a member

If the recovered profile already has categories from an old experiment: **do not add extras** to complete this pack. Log `already_member_draft` and stop. Editing a live page still hits Save = viewable unless a true draft control exists.

## Not this file

- LinkedIn **Jobs** title / job function (different product)
- Skills on the main profile (not the Service Page picker)
- Company Page categories

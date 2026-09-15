> **DRAFT_ONLY. DO NOT SEND.**  
> Gates are necessary, not sufficient. This file is **not** a SEND GO.

# GO gates — Contra JOBS apply playbook

Who ticks boxes: **the human operator**. Agents do not grant GO.  
Live box: PR#64 `draft_saved` / **`apply: no`**.  
Paste pack: PR#71. Rules: [PLAYBOOK.md](PLAYBOOK.md) · [STOP.md](STOP.md).

Skip (park, do not send) if **any** box in the active set is false.

---

## A. LOOK gates (browse the Job feed)

All must be true **before** opening the Job feed with apply intent. LOOK does **not** allow Apply.

- [ ] I am the human operator (or I am an agent that will **only** look and will **not** submit).
- [ ] The live Independent already exists on **MAIN Google**. I will not create a second Contra or a second Google identity.
- [ ] PR#64 still matches live: **`draft_saved`**, **Free**, **`apply: no`**, **`publish: no`**. Location may still be Kent, USA.
- [ ] I will not Publish, invoice, buy Pro, open Wallet / Persona, or change country to Japan on this play.
- [ ] PR#71 folder `earn-jobs-contra-proposals-20260916/` is readable (five style files + README + HANDS-AND-TOS). I will not invent paste if a file is missing.
- [ ] I will use the official signed-in Job feed on contra.com only (not a scrape, not a third-party apply tool).
- [ ] I will not click **Refer & Earn**, Labs, Expert programs, Discover boost, or a Job Network video/Loom submit from this pack.
- [ ] Default remains **do-not-send**. I do not treat this checkbox list as permission to Apply.

If any LOOK box is false: park `look_blocked` (or the matching STOP code) and close.

---

## B. PREP gates (rewrite one PR#71 style for one posting)

All must be true **before** rewriting paste for **this** listing. PREP does **not** allow Apply.

- [ ] LOOK gates are still true.
- [ ] I opened **this** job on contra.com (Job feed / opportunity UI).
- [ ] I picked **exactly one** PR#71 style file that matches the ask (`01` … `05`). I am not stacking styles.
- [ ] This is the **only** listing I will use this style file on (no identical-blast, no “daily habit” extras).
- [ ] I can replace `{{ONE_SPECIFIC_DETAIL}}` with a fact from **this** posting in about a minute. If not: skip. Do not reuse another listing’s detail or a `[FICTION]` example.
- [ ] Leftover placeholders from a previous listing are gone.
- [ ] No email, phone, WhatsApp, Telegram, Slack, Discord, or “text me at…” will go in the paste. Platform-owned email slots stay platform-owned.
- [ ] No off-platform payment, crypto-to-wallet, or “pay me outside.”
- [ ] Rate / timeline stay `{{HOURLY_RATE_USD}}` / `{{FIXED_PRICE_USD}}` / `{{DELIVERY_DAYS}}` from the **local ledger**. Git has no live USD. Empty required rate → park `rate_required` (do not invent).
- [ ] The work is official APIs / documented connectors + docs. Scraping, likes/follows/views, ungated posting, or fully autonomous outbound → **Dismiss** (do not PREP).
- [ ] The live form does **not** require Contra Pro / Max, wallet funding, Persona / identity upload, or a card wall to continue composing. If it does: **stop** (do not PREP around the wall).
- [ ] I am rewriting in a local editor or the live composer as a **draft**. I will not click **Apply** from PREP.

If any PREP box is false: skip this listing / this style. Do not stretch the paste.

---

## C. SEND gates (Apply click) — default FALSE

This pack’s SEND GO is **off**. Do not tick these as a ritual. They exist so a **later dated human note** can reuse the same list.

Until that note exists, treat every box as **unchecked** even if LOOK and PREP passed.

- [ ] A **dated human SEND GO** exists **outside this PR** and names this one listing + this one style. **This folder is not that GO.**
- [ ] LOOK and PREP are true **right now** for that same listing (re-tick; do not reuse yesterday’s memory).
- [ ] I re-read [Applying to jobs on Contra](https://help.contra.com/en/articles/9322973-applying-to-jobs-on-contra). I am on the official Apply control, not Refer & Earn.
- [ ] If a paid-project / proposal form appears, I re-read [Paid projects](https://help.contra.com/en/articles/9322763-paid-projects) and did **not** copy the fee table into the letter or into git.
- [ ] I will click **Apply** myself. Nothing in this repo, no agent, no extension, no API submits for me.
- [ ] After this one Apply I will **stop** this style (one listing per style, then stop).

**Default: all SEND boxes stay empty. `apply: no`.**

---

## Gate → outcome

| If | Outcome code | Send? |
|---|---|---|
| LOOK false | `look_blocked` / STOP code | no |
| LOOK true, feed walled | `pro_wall` `card_wall` `wallet_wall` `persona_wall` `kyc_wall` `job_network_wall` `labs_or_expert_wall` | no |
| LOOK true, no matching posting | `style_skipped` | no |
| `{{ONE_SPECIFIC_DETAIL}}` empty | `detail_empty` | no |
| Style already used this wave | `style_already_used` | no |
| PREP true, SEND GO absent | `prepped_not_sent` (**normal**) | **no** |
| Live rate required, ledger empty | `rate_required` | no |
| SEND GO present + all C boxes true | later human may Apply **once** | only then |
| Agent / script would submit | `auto_apply_forbidden` | **no** |

`prepped_not_sent` is a **successful** play. It is not a failed apply.

---

## What is never a GO

- PR#71 existing (drafts are copy text, send **forbidden** in that pack)
- This playbook existing (LOOK/PREP only)
- First-client help Step 5 “make applying a habit”
- Contra marketing about Job feed / Pro / Expert badges
- A computer-use agent finishing the serial
- “The composer already has text in it”
- Fictional `Client A`–`E` fills
- Sibling Wave 2 Contra cover letters (different pack; still do-not-send)

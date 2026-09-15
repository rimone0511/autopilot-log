# Fiverr gig extras — JOBS PHASE, DRAFT_ONLY

Pack date: 2026-09-16
Desk: Fiverr
Phase: **JOBS** (listing extras for an existing unpublished Gig). Not a CU register walkthrough.
Language: English buyer-facing paste
Mode: **DRAFT_ONLY**. Unpublished. No account login from this agent. No secrets.

This folder polishes **Requirements**, **FAQ (10)**, **search tags**, and **search SEO notes** for the existing n8n Gig draft. It does not create a second Gig, retitle the listing, or publish anything.

Existing Gig body (title, packages, description, gallery skip): `earn-fiverr-gig-draft-20260916/` on branch `cursor/earn-fiverr-gig-draft-91ed` ([PR #6](https://github.com/rimone0511/autopilot-log/pull/6)).

Sibling Requirements + FAQ polish aimed at a simpler title voice (`set-up-a-simple-n8n-workflow`): `earn-fiverr-requirements-faq-polish-20260916/` ([PR #15](https://github.com/rimone0511/autopilot-log/pull/15)). This JOBS pack targets the **operator-docs** Gig from PR #6 and **adds tags + search SEO**, which #15 left out of scope.

## Files

| File | What to paste |
|---|---|
| [REQUIREMENTS.md](REQUIREMENTS.md) | 6 Free-text questions, all **Required**, plus 2 optional extras |
| [FAQ.md](FAQ.md) | 10 FAQ pairs (Question + Answer fields) |
| [TAGS.md](TAGS.md) | 5 search tags + optional 5 metadata phrases |
| [SEARCH-SEO.md](SEARCH-SEO.md) | Overview keyword map. Do not rewrite the Gig description from here |

## Existing Gig identity (do not fork)

| Field | Value from PR #6 |
|---|---|
| Title field (after `I will`) | `build n8n automation with operator docs you can rerun` |
| Display | `I will build n8n automation with operator docs you can rerun` |
| Category | Programming & Tech → Software Development → Automations & Workflows |
| Packages | Starter workflow / Production workflow / Workflow and SOP |
| Status to keep | **Draft**. Do not click Publish Gig |

Paste extras into that unpublished Gig only. Do not open a second listing to “test SEO”.

## Hard rules

- English paste only on buyer-facing fields.
- **DRAFT_ONLY.** Leave the Gig unpublished. Do not click Publish Gig, Promote, or Seller Plus.
- **No account login from this agent.** A human may paste later. This pack is copy, not a live session.
- No secrets in these files or in git (no real passwords, API keys, IDs, tax numbers, emails).
- No fake n8n / xAI / OpenAI / Google / Fiverr partnership. Do not tag `xAI`, `Grok`, or `ChatGPT`.
- Requirements type is **Free text** for R1–R6. Mark every R1–R6 row **Required**.
- Stay inside the field limits below. Counts next to each paste were measured with Python `len()` on the fenced text (spaces count; fences do not).
- Do not send this text to Fiverr by automation.

## Field limits (official vs conservative)

Official [Creating a Gig](https://help.fiverr.com/hc/en-us/articles/360010451397-Creating-a-Gig) (public help, 2026-09-16 read from this agent; no Fiverr account):

| Field | Official |
|---|---|
| Title | complete the pre-filled `I will…`; avoid `&` `/` `"` `+` |
| Search tags | up to five; use all five |
| Metadata phrases | up to five words or short phrases |
| Gig description | up to 1,200 characters (**not** rewritten in this folder) |
| FAQ entries | up to 10 |
| Requirements | ask what you need before work starts; mark individual questions required |
| Gig Extra in requirements | optional multiple-choice that introduces **one** extra |
| How-found question | optional free-text for marketing channel |
| Gig text language | English required |
| Publish | needs gallery image, verification, tax where applicable — **out of scope** |

Fiverr help does **not** state FAQ Q/A, Requirements question, or tag character ceilings. This pack uses the same conservative form ceilings as the sibling Gig pack:

| Paste field | Conservative ceiling | This pack |
|---|---|---|
| FAQ question | 70 | max 46 |
| FAQ answer | 300 | max 239 |
| Requirements question | 200 (unofficial; stay well under) | max 135 |
| Search tag | 20 (common form) | max 19 |
| Search tag count | 5 | 5 |
| FAQ count | 10 | 10 |
| Required Free-text rows | keep short | 6 |

If a live field is shorter than these ceilings, trim from the end of the paste. Do not add keyword walls to fill space.

## Where this paste goes

| Gig create step (help names) | Paste |
|---|---|
| Step 1 — Overview | [TAGS.md](TAGS.md) only (not the title) |
| Step 3 — Description & FAQ | [FAQ.md](FAQ.md) only (not the Gig description) |
| Step 4 — Requirements | [REQUIREMENTS.md](REQUIREMENTS.md) |

[SEARCH-SEO.md](SEARCH-SEO.md) is operator notes. Do not paste it into a buyer-facing field.

## Out of scope

- Account create, login, KYC, tax, phone verify, W-9/DAC7, bank, Seller Plus
- Publish, Promoted Gigs, paid boosts, gallery, video
- New title, new category, new package prices, new description body
- Any instruction to create, save-as-publish, or submit a Gig
- Secrets, client names, or live USD prices

## Verification (this agent)

- Character counts re-measured; claimed figures match fenced paste
- Python posting-gate tests unchanged
- No Fiverr account was used. Public `fiverr.com` category/search URLs returned a bot challenge (`PXCR10002539`); SEO evidence is public Help Center + public web snippets, not a logged-in autocomplete scrape
- No secrets in this folder

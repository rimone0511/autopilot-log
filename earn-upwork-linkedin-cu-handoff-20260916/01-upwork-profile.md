# Upwork freelancer profile — DRAFT paste

Desk: Upwork (Wave A5)  
Seller: Yuta Ishida / 石田祐太  
Pack: 2026-09-16  
Mode: **DRAFT_ONLY — not a proposal, not Catalog submit**

This is the **profile** box (title, overview, skills, rate placeholder). Catalog listing copy is [02-upwork-catalog.md](02-upwork-catalog.md).

Public help (re-check at click-time):

- Register as a freelancer: https://support.upwork.com/hc/en-us/articles/24492534968211-Register-as-a-freelancer
- Title and overview: https://support.upwork.com/hc/en-us/articles/34925678839827-Your-profile-title-and-overview
- Profile essentials: https://support.upwork.com/hc/en-us/articles/360016252373-How-to-build-your-freelancer-profile-the-essentials
- Identity (stop): https://support.upwork.com/hc/en-us/articles/360001176427-How-to-verify-your-identity-as-a-freelancer

Do not put `{{EMAIL}}`, `{{PHONE_E164}}`, or “message me off Upwork” anywhere below.

---

## 1. Account / name

| UI field | Paste / action | Notes |
|---|---|---|
| Sign up | Continue with Google | MAIN Google only |
| I want to | Work as a freelancer | Not Hire. Not Agency. |
| First / last name | `{{FULL_LEGAL_NAME}}` split as the form asks | Honest legal name. Japan is fine. Do not spoof a US name. |
| Display name | `{{DISPLAY_NAME}}` | If the form has one |
| Country | `{{COUNTRY}}` | Must be able to match ID later. Do not fake US/EU. |
| City | `{{CITY}}` | Honest |
| Professional photo | `{{PROFILE_PHOTO_LOCAL_PATH}}` | Real current photo of the operator. Not a logo, cartoon, or ID crop. Skip if the picker is an ID flow. |

---

## 2. Title (≤ 70 characters)

Upwork prepends nothing here (unlike Catalog “You will get”). Paste **only**:

```
n8n automation with operator docs you can rerun
```

| Count | Value |
|---|---|
| Title | 47 characters (limit 70) |

Do not keyword-stuff xAI / Grok / “10 years / 500 clients.”

---

## 3. Hourly rate — placeholder, not a fact

| UI field | Value |
|---|---|
| Profile hourly (USD) | `{{HOURLY_USD}}` |

This is a **starting-point field**, not a quote and not Catalog tier prices. Do not invent a number in git. Do not copy someone else’s public rate.

If the live form **blocks save** with an empty rate: park `rate_required`. Morning operator types a local number later. CU does not guess.

---

## 4. Skills (pick in the live list)

Public writeups disagree on 15 vs 20. **Live picker wins.** Do not invent skill IDs.

Type-to-search, in this preference order, until the cap:

1. `n8n` (or nearest Automation / Workflow token)
2. `API Integration` / `API`
3. `Automation`
4. `Technical Writing` or `Documentation`
5. `SOP` if listed; else skip
6. `Google Workspace` if listed
7. `Webhooks` if listed
8. `Zapier` — only as a **migration** skill, not as the product you sell
9. `Make` / `Make.com` — same
10. `Python` only if listed **and** you will actually use it on a job

Do not add social-media growth, “get likes,” crypto trading, or scraping skills.

---

## 5. Overview — paste

Search lists often show roughly the **first 250 characters**. The hook below is 196 characters. Full block is for the profile editor, **not** the Catalog 1,200-character box.

```
I am Yuta Ishida. I build n8n automations and the operator documentation that lets a non-engineer run them after I leave. Official APIs only. No scraping, no engagement bots, no social publishing.

The offer is a scoped workflow plus an SOP, not an unbounded retainer and not a lecture about AI. You should be able to point at one process and receive something you can rerun without me sitting in chat.

I work in English, async-first, in {{TIMEZONE}}. Location: {{CITY}}, {{COUNTRY}}. I do not invent a United States or European address to look closer to a buyer.

Typical pieces: a trigger (form, webhook, schedule, or a new sheet row); honest steps through tools you already use; a destination (inbox, sheet, CRM field, or internal API); retries or a failure alert; a short SOP that names what starts it, what is safe to edit, where secrets live, and how to rerun. Secrets stay in the credential store. The SOP does not paste them.

I connect tools that have an official API, a documented webhook, or a first-party connector. I will not scrape a site that has no public API. I will not automate likes, follows, comments, or fake views. I will not publish to YouTube, TikTok, or any other channel on your behalf unless you hold the posting switch. Upload and publish are different acts.

A public example of that stance is Autopilot Log, a small CLI that talks only to official posting APIs and fails closed if the posting gate is missing. I am not selling that CLI as this profile. I am selling the same habit. Public writing: yutalab.dev. Chat and files stay on Upwork.

I will not write unverified client counts, invented years of experience, traffic numbers, or ranking promises. I will not claim n8n Expert, Zapier Partner, or Make Partner status. Hourly on this profile is a placeholder starting point, not a guaranteed quote — Catalog work uses fixed tiers when a listing exists.

If you need a whole department migrated off Zapier or Make, that is a custom contract, not a profile click. If you need a predefined packaged project, use Project Catalog when it is live; until then, do not treat this overview as a submitted Catalog item.
```

---

## 6. Other profile sections

| Section | Draft stance |
|---|---|
| Experience / employment | Independent / ユタラボ only if true. Do not invent employers or dates. Skip if optional. |
| Education | Skip unless required. Do not invent degrees. |
| Languages | English (professional working) + Japanese (native) if the picker exists. Confirm live labels. |
| Video intro | Skip. |
| Other experiences | Skip. |
| Certificates | Skip unless a real, current certificate exists locally. No fake badges. |
| Employment availability | Prefer part-time / as-needed if asked. Do not promise 40h without a later human GO. |
| Profile visibility / “submit profile” | If submit **opens ID / vetting**, treat as KYC and **stop**. Saving in-progress is OK. |

Portfolio: optional later. Title ≤ 70, description ≤ 600, no contact details in files ([portfolio help](https://support.upwork.com/hc/en-us/articles/360016144974-How-to-enhance-your-freelancer-profile)). Do not attach ID. Do not attach Autopilot Log as if it were the Catalog deliverable.

---

## 7. What this profile is **not**

- Not a proposal. Do not open a job and paste this overview as a cover letter.
- Not Connects spend. Find Work stays closed for this pack.
- Not auto-bid configuration. There is no “apply settings” to turn on.

Proposals, if a human later sends one: sibling `earn-en-proposal-drafts-20260916/` — **you click Submit**, one listing at a time, no spray.

---

## 8. Activity note

Verdict: marketplace **not treated as closed**. Catalog browse from some environments hits a JS / verification interstitial (same class as a Cloudflare wall: **not** proof the desk is dead).

Evidence (2026-09-15), no GMV or job counts invented:

- Upwork home and freelancer-registration help returned live content in sibling packs.
- Wave A queue already marks Upwork `next`, MAIN Google, KYC → morning stop.

Confirm at click-time whether the logged-in freelancer can edit a profile **without** ID. Still do not submit Catalog. Still spend **0** Connects.

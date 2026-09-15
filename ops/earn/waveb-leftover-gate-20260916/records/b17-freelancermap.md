# B17 — Freelancermap

**DRAFT_ONLY.** Logged out. Did not register. Did not apply. No secrets.

This-folder ID **B17** = QUEUE **B12** = INDEX **CU-23**.  
QUEUE B17 is ITプロパートナーズ — different desk.

```
日付（JST）: 2026-09-16
机: Freelancermap
公式URL: https://www.freelancermap.com/
公開ページを見たか: yes
ログインしたか: no
signup_open: yes（https://www.freelancermap.com/registration HTTP 200 title “Sign up to freelancermap - IT freelancers & projects”. 完走していない）
fee_page: yes（https://www.freelancermap.com/pricing/freelancer 200）. Basis 0,00 €/月. Premium 13,99 €/月 on Jährlich toggle. Persona verify 50€/年 Premium, 75€/年 Basis. Help: no commission fees
open_jobs_heuristic: /projects 200. Payload created ISO on 2026-09-15 (examples 18:24:49+02:00 and 17:03:11+02:00). Homepage “over 14,600 open projects” ignored
last_blog_news: /blog/freelance-profile-tips-examples/ title “(2026)” — blog, not a card date
fit_still_ok: yes（IT project board, remote and on-site mixed. Filter later; desk not thin）
1 生きている: yes
2 寄せ集めではない: yes
3 現地だけではない: yes（remote/hybrid copy on cards; on-site also present）
4 本人専用ではない: yes
5 活動の目視: yes
   見たもの: created 2026-09-15 ISO next to project titles on /projects
6 KYC: 出ていない（Persona verify is a paid optional path on pricing HTML — do not open）
7 本線: yes
gate_result: pass
action: park until Wave A. Later: free Basis only. No Premium. No verify. No Apply.
公開したか: no
Google: NOT_OFFERED_OAUTH on public register/login HTML (GTM/ads only). Use MAIN mailbox as email
有料: Basis 0,00 €. Do not buy Premium or Persona
SKIP thin: no
```

Sibling paste pack (not copied): [PR#29](https://github.com/rimone0511/autopilot-log/pull/29) `05-freelancermap.md`.

## Official URL

- Home: https://www.freelancermap.com/ — 200
- Projects: https://www.freelancermap.com/projects — 200
- Registration: https://www.freelancermap.com/registration — 200
- Login: https://www.freelancermap.com/login — 200
- Pricing (freelancer): https://www.freelancermap.com/pricing/freelancer — 200
- Help: https://www.freelancermap.com/help.html — 200
- For freelancer: https://www.freelancermap.com/for-freelancer — 200
- Privacy: https://www.freelancermap.com/data-privacy.html — 200
- Do **not** use Project provider account type

Home marketing (“Currently over 14,600 open projects”, “Over 116,700 freelancer profiles”, “2,000 projects weekly”) is vendor copy. **Not used as a count.**

## Public jobs / dates — what this GET actually saw

`GET /projects` returned HTML that embeds a project payload. Fields seen next to titles include `created` (ISO) and `updated` (unix). Examples **this GET** actually read:

| `created` (payload) | Public `title` (trimmed) | Note |
|---|---|---|
| 2026-09-15T18:24:49+02:00 | EU-based freelance developer C# and VBS | Nearby `updated` unix → 2026-09-15T16:29:21Z |
| 2026-09-15T17:03:11+02:00 | AI Manager | Description copy: Eindhoven; “Hybrid - 3 days onsite per week”; contract type Freelance |
| 2026-09-15T16:32:12+02:00 | Software Quality engineer | Title only recorded |
| 2026-09-15T16:25:03+02:00 | Private Hire Taxi Driver | On-site/local may appear. **Filter later.** Desk not SKIP thin |

Those four are **examples**, not a census. Payload cardinality is not traffic.

`/api/projects` without login redirected to `/login`. `projectSearch.json` 404. Recency is taken from the public `/projects` HTML, not from an authed API.

DE/EU cities appear (examples in the same payload: Ingolstadt, München, Belgium). Japan as a country is not re-proven here; sibling pack said JP is in a country list — **this GET did not re-open that API**. Keep `{{COUNTRY}}` honest. Do not fake Berlin.

## Signup path

Static `/registration` HTML:

- Heading **Create your free account**
- Account type radios: **Freelancer / Agency** (“seeking projects”) vs **Project provider**
- Buttons: Cancel / Continue
- Further fields (email/password) were **not** in this first-step HTML

Google / Facebook / LinkedIn / Apple **OAuth buttons: not present.** “Google” strings on the page are Analytics, Tag Manager, and ads conversion snippets only.

Login HTML: **Email address or username**, **Password**, **Login link by email**. No OAuth button.

CU should use MAIN Google **mailbox** as email. If a Google button appears at click-time despite this GET: PREFER_GOOGLE, still MAIN only, and record the label change. Do not create a new SNS account.

Help: account is inactive until the activation link is clicked. This PR did not send mail.

## Fee notes (official pages only)

From https://www.freelancermap.com/pricing/freelancer (this GET):

- **Basis**: **0,00 €** pro Monat. 10 Bewerbungen pro Monat. 「Kostenlos starten」
- **Premium**: **13,99 €** pro Monat on the **Jährlich** toggle (page also says 20 % sparen bei jährlicher Zahlung). JSON on the same HTML includes `lowestPremium: 13.99` for `PM12/12`
- Profile verification: 「Für Premium-Mitglieder 50€ pro Jahr, für Basis-Nutzer 75€. … Weder freelancermap noch **Persona** speichert …」

From https://www.freelancermap.com/help.html:

- Basic membership is free
- Premium starting at **€13.99/month, billed annually**
- **No commission fees**
- Extra costs for optional profile verification or Featured Project
- Basic: apply for up to **10 projects/month** (and limited contact requests). That cap is **not** a reason to apply from this pack

**Do not subscribe** to Premium to “see if it is worth it.” **Do not pay** Persona verification.

## CU tip

1. Wave A still owns the live box. This gate does **not** start CU-23.
2. When Wave B GLOBAL reaches QUEUE B12: Freelancer/Agency only. Email = MAIN mailbox. Stay **Basis**.
3. Profile draft. Prefer inactive / private / anonymous if offered. Help: apply requires an active profile — we are not applying.
4. Stop before Verify profile, IBAN/PayPal/SEPA, VAT ID submit, Get Premium, Apply / AI one-click apply.
5. On-site DE/EU / taxi-style cards: skip those rows. Do not SKIP the desk.
6. Sibling paste pack in PR#29 may be used later as a field map. This record is not that pack.

## Checklist (PR#1 template)

1 生きている: yes  
2 寄せ集めではない: yes  
3 現地だけではない: yes（hybrid/remote copy present; on-site also present）  
4 本人専用ではない: yes  
5 活動の目視: yes（`created` 2026-09-15）  
6 KYC: 有料任意 Persona。開かない  
7 本線: yes  

判定: **pass**  
QUEUE: Wave B12 のまま。  
Google: **NOT_OFFERED_OAUTH** this GET  
有料: Basis 無料。Premium / verify 買わない  
SKIP thin: no

## Gate

**pass**

> DRAFT_ONLY paste pack. NO secrets. NO marketplace login from this authoring PR. NO publish.
> Free GULP Basisprofil only. Do not buy Membership. 0 applications.
> Do not apply to onsite CH / local-presence cards. Desk is not a shift-work board.
> “7 Euro Servicegebühr / Freelancer-Stunde” is GULP Direkt **client** copy, not a seller plan.

# PACK — Gulp (Randstad Professional) — this-folder play 6

| Key | Value |
|---|---|
| inventory | 06 |
| cu_serial | **unindexed** |
| queue | D-early gate add (PR#22 keep) |
| activity_gate | **alive** (this GET: `/freelancing/projekte` cards **NEU**, Start ab **01.09.2026** / **14.09.2026** / **02.11.2026**) |
| self_serve | yes (public Freelancer “Jetzt kostenlos registrieren”) |
| cu_ready | true (pack exists. **not registered**) |
| official | https://www.gulp.de/ |
| register_landing | https://www.gulp.de/registrieren |
| register_form | https://www.gulp.de/gulp2/g/neu/experten/registrieren (JS required this GET) |
| projects | https://www.gulp.de/freelancing/projekte |
| membership | https://www.gulp.de/freelancing/gulp-membership |
| google_signup_preference | **NOT_OFFERED_OAUTH** (public registrieren HTML 2026-09-16: no Google control) → MAIN mailbox email |
| worker_fee_public | Basisprofil **kostenlos** (membership page). GULP Direkt client: platform free until hire; **7 Euro Servicegebühr pro Freelancer-Stunde** at Beauftragung (**client**). Membership **120 Euro netto / 6 Monate**, **180 Euro netto / 12 Monate** — do not buy. **No freelancer % invented.** |
| paid | **NO** |
| stop_at_kyc | **STOP** |
| draft | true |
| observed | 2026-09-16 public GET |

Brand: **Randstad Professional (vormals GULP)**. Freelancer box vs Unternehmen vs Bewerber — use Freelancer only. Do not enter GULP Corporate or the jobs-board Bewerber path.

Onsite / CH examples visible this GET (do **not** apply): Wallisellen, Zollikofen BE, Zürich, Bern, St. Margrethen, Basel, Winterthur, Raum St. Gallen. Start ab dates are **project start**, not post dates. Homepage “714 Jobs / 876 Projekte / 4.768 Freiberufler” is marketing — unused.

## needs_check

- Live gulp2 register fields (this GET: “JavaScript ist in Ihrem Browser deaktiviert”).
- Whether a Google button appears after JS. Default remains email = MAIN mailbox unless a Google control is actually visible.
- Hidden / inactive profile control.

## CU handoff

1. Open https://www.gulp.de/registrieren → **Freelancer** “Jetzt kostenlos registrieren”.
2. Email `{{EMAIL}}` = MAIN mailbox. Password `{{PASSWORD_DO_NOT_STORE}}`. Activation via parent Gmail MCP.
3. If a Google button **is** painted at click-time, use it (still MAIN). Do not create a DE-only mailbox.
4. Draft Basisprofil: DE or EN bio, skills, remote-first, honest JP location.
5. Close Membership / Haftpflicht upsells.
6. **0 Bewerbungen.** Do not click apply on CH / onsite / “80-100%” local cards.
7. STOP at Steuer-ID upload, passport, bank, or e-sign identity.

## Field map (placeholders)

### Account

| UI field | Paste | Notes |
|---|---|---|
| Role | Freelancer / Experte | Not Unternehmen, not Bewerber job seeker. |
| Email | `{{EMAIL}}` | MAIN mailbox. **NOT_OFFERED_OAUTH** on public HTML. |
| Password | `{{PASSWORD_DO_NOT_STORE}}` | Never commit. |
| First / last name | split `{{FULL_LEGAL_NAME}}` | |
| Country | `{{COUNTRY}}` | Honest JP. Do not fake DE/CH. |

### Basisprofil

| UI field | Paste | Notes |
|---|---|---|
| Headline | Short bio | EN OK; DE UI may want DE — live form wins; do not invent fluent DE if unsure (paste EN). |
| About | Long bio | |
| Skills | `n8n, Automation, API, Dokumentation, SOP, Cloud, Python` | |
| Stundensatz | `{{HOURLY_RATE_EUR}}` | Empty → `rate_required`. Do not invent. |
| Einsatzort | Remote / `{{CITY}}` | Do not claim onsite CH. |
| Verfügbarkeit | remote-first, by agreement | Honest. |
| Photo | `{{PROFILE_PHOTO_LOCAL_PATH}}` | Face. |
| Membership | **Basis / frei** | Do not pay 120/180 Euro. |
| Visibility | incomplete / not searchable if offered | Draft. |

## EN bios

### Short

```
n8n / automation freelancer with operator docs. Remote-first. English. I do not take onsite CH shifts from this pack.
```

### Long

```
I design, build, and document automation (n8n and official APIs) so an operator can rerun the workflow without me.

Typical engagement: one production workflow, retries, a failure alert, and a short SOP. I work in English from {{CITY}}, {{COUNTRY}} ({{TIMEZONE}}). German UI is fine; I do not claim native DE. I am not available for on-site Switzerland / local-presence contracts from this draft profile.

I will not:
- Apply to GULP/Randstad project cards from this CU session
- Buy GULP Membership
- Upload ID, tax, or bank documents
- Automate engagement or scrape closed APIs

Public work: https://yutalab.dev/ and Autopilot Log (YouTube Data API v3 + TikTok Content Posting API, fail-closed posting gate).
```

## STOP

Do NOT: Membership 120/180 Euro, Haftpflicht checkout, Bewerbungen (especially CH onsite), Steuer/ID/bank, invent freelancer 7 Euro as “I pay this”.

Allowed: email Basisprofil draft, remote-honest location.

## Activity note

PR#22 **alive**. This GET: register 200, projekte 200 with 2026 start dates, membership pricing public. gulp2 form needs JS. `thin_site_skip: false`.

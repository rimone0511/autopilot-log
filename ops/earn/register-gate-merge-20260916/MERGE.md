# MERGE — morning activity-gate PRs #58 / #59 / #61 / #62

Stamp: **2026-09-16 JST**  
Folder: `ops/earn/register-gate-merge-20260916/`  
State: **DRAFT_ONLY**

High-level rollup of four finished morning gate PRs. Public GET records only. **No secrets. No signup. No paid plans.** Sibling pack bodies are **not** copied. Listing counts, GMV, rankings, and “○万人” are **not invented** here (and were not invented in the source PRs).

This sheet does **not** replace Wave A live box [PR#54](https://github.com/rimone0511/autopilot-log/pull/54). It does not rewrite [PR#1](https://github.com/rimone0511/autopilot-log/pull/1) QUEUE letters. CU numbers stay [PR#8](https://github.com/rimone0511/autopilot-log/pull/8).

Same-folder companions: [STATUS.md](STATUS.md) · [NEXT-CU.md](NEXT-CU.md).

## Labels (this merge)

Source PRs use `pass` / `alive` / `keep_queue` for a public freshness clue. This sheet maps them as follows:

| Label | Meaning here |
|---|---|
| `alive` | Public page showed a freshness clue the source GET actually read (dated card, `publishAt`, official dated catalog / blog). Draft-only later. Not a CU GO from this merge. |
| `needs_check` | Site is up, but listing dates were unread, SPA-empty, WAF, or login-walled. Do not guess `alive` or SKIP. |
| `thin` | Public work does not fit this earn line **and** evidence was written. **0 across all four PRs.** |
| `dead` | Closed URL / dedicated desk 404 / brand is a different product with no public freelance board. Evidence required. |
| `blocked_paid_plan` | Marketplace may look alive; **do not subscribe.** Not `thin`. Not `dead`. |

Unread SPA / WAF / login wall is **not** `dead` and **not** `thin`. Marketing totals are not activity proof.

## Source PRs (folders not copied)

| PR | Title (short) | Folder | Slice |
|---|---|---|---|
| [#58](https://github.com/rimone0511/autopilot-log/pull/58) | Wave D-early activity-gate sample | `ops/earn/waved-early-gate-sample-20260916/` | D02 カイコク, D03 note, D04 Braintrust, D07 Twago, D08 99freelas, D09 Gulp, D10 Xing Projects |
| [#59](https://github.com/rimone0511/autopilot-log/pull/59) | Wave B GLOBAL (PPH / Workana / YOUTRUST) | `ops/earn/waveb-global-gate-20260916/` | folder B14/B16/B18 ≠ QUEUE B14/B16/B18 |
| [#61](https://github.com/rimone0511/autopilot-log/pull/61) | Wave B JP batch 2 (Anycrew / MENTA / ストアカ) | `ops/earn/waveb-activity-gate-batch2-20260916/` | folder B10–B12 = QUEUE B5/B6/B7 = CU-15/16/17 |
| [#62](https://github.com/rimone0511/autopilot-log/pull/62) | Wave B JP batch 1 (複業クラウド / CrowdLinks / AI CrowdWorks) | `ops/earn/waveb-activity-gate-batch1-20260916/` | folder B03–B05; B05 here = AI CrowdWorks (not Anycrew) |

Independent GETs, same morning window (~2026-09-16 JST). Bodies are not merged into this folder.

## Counts (this merge only)

| Bucket | n | From |
|---|---|---|
| `alive` | **6** | note, Braintrust, 99freelas, Gulp (#58) · MENTA, ストアカ (#61) |
| marketplace-alive + seller `blocked_paid_plan` | **1** | PeoplePerHour (#59) — not a seller GO |
| `needs_check` | **7** | カイコク (#58) · Workana, YOUTRUST (#59) · Anycrew (#61) · 複業クラウド, CrowdLinks, AI CrowdWorks (#62) |
| `thin` | **0** | — |
| `dead` | **2** | Twago, Xing Projects (#58) |

6 + 1 + 7 + 0 + 2 = **16 desks** in the four PRs. No desk was labeled `thin`.

Wave B JP desks that already `pass`ed in [PR#12](https://github.com/rimone0511/autopilot-log/pull/12) (Workship, SOKUDAN, Skill Shift, ITプロパートナーズ, Offers) were **not** in these four PRs. They stay `alive`/`pass` on that earlier gate. See [NEXT-CU.md](NEXT-CU.md).

---

## PR#58 — Wave D-early sample

Starting operator label for all seven: `needs_activity_check`. After GET:

| Desk | Label | High-level (source GET only) |
|---|---|---|
| D03 note | **`alive`** | Top HTML `publishAt` 2026-09-14 / 15 (+09:00). `/signup` 200. Paid notes / memberships stay draft. |
| D04 Braintrust | **`alive`** | Talent “$0 fees”; `/jobs` role cards; blog heading Sep 14, 2026. ID-verified / Certified → STOP. |
| D08 99freelas | **`alive`** | Public project headings. Fee copy 5–20% on official page. `/register/freelancer` CF 403 this IP — home `Cadastre-se`. Do not bid. Premium not bought. |
| D09 Gulp | **`alive`** | Public project cards (NEU / Start ab 2026-09·11). Membership 120/180 Euro netto **not bought**. Skip on-site CH. |
| D02 カイコク | **`needs_check`** | Free-register path open. Public “案件事例” have no listing dates. Marketing 登録者数 / 掲載数 unused. Not SKIP. |
| D07 Twago | **`dead`** | `twago.com` 301 → talent-pool.com enterprise Talent Pool. No public freelance board. `twago.de` 404. |
| D10 Xing Projects | **`dead`** | `xing.com/projects` 404. Current XING is a jobs network. Do not fall over to Jobs. |

`thin`: **0**. keep_queue is **behind Wave A/B**. This PR does not start D-early CU.

D01 Shufti / D05 Twine / D06 Fastwork: out of that sample.

---

## PR#59 — Wave B GLOBAL slice

This-folder IDs are **not** QUEUE letters (QUEUE B14 is Offers; B16 is Skill Shift).

| This folder | Desk | QUEUE / CU | Label | High-level (source GET only) |
|---|---|---|---|---|
| B14 | PeoplePerHour | B9 / CU-20 | marketplace **`alive`** · seller **`blocked_paid_plan`** | `/freelance-jobs` title includes Sep 2026; HTML `posted_dt` on 2026-09-15. Public Terms (last modified September 11, 2026): **PPH Basic** is a **non-refundable annual** subscription (amount “indicated on the subscription sign up” — checkout **not** opened). TopAccess is a second annual plan. **Do not subscribe.** |
| B16 | Workana | B11 / CU-22 | **`needs_check`** | HTML paths Cloudflare 403. `robots.txt` 200 (host not parked). Job recency unread. WAF ≠ dead. |
| B18 | YOUTRUST | B13 / CU-24 | **`needs_check`** | `/recruitment_posts` SPA; card dates unread; API 401. Official recruiter paid path: do not buy. No 「話を聞きたい」. |

`thin` / `dead` / SKIP: **0** this slice.

Guru / Malt / Freelancermap: sibling GLOBAL packs, not this GET.

---

## PR#61 — Wave B JP batch 2

Re-check of three desks [PR#12](https://github.com/rimone0511/autopilot-log/pull/12) left `needs_check`. Folder B10–B12 ≠ QUEUE B10 Malt / B11 Workana / B12 Freelancermap.

| This folder | Desk | QUEUE / CU | Label | High-level (source GET only) |
|---|---|---|---|---|
| B11 | MENTA | B6 / CU-16 | **`alive`** (`pass`) | Public `/plan` plan cards with **NEW** labels. Register face open. Plan submit / Stripe identity: do not. |
| B12 | ストアカ | B7 / CU-17 | **`alive`** (`pass`) | `/online/all` class cards with session times (example: **9月16日(水)**). Date filter JSON **2026-09-16**. Google OAuth not offered → MAIN Google mailbox + email register. No class publish / face-photo certificate. |
| B10 | Anycrew | B5 / CU-15 | **`needs_check`** | App is up. 「Googleでログイン」. `/offers` React empty shell. Company news 2026-08-31 / blog 2026.08.26 are **not** job-card dates. |

`thin` / fail / `blocked_paid_plan`: **0**. vs PR#12: MENTA and ストアカ promoted to `pass`; Anycrew stays unread catalog.

---

## PR#62 — Wave B JP batch 1

Re-check of three other PR#12 `needs_check` desks. **None promoted.**

| This folder | Desk | Label | High-level (source GET only) |
|---|---|---|---|
| B03 | 複業クラウド | **`needs_check`** | Individual job **titles** (incl. フルリモート). No listing `created_at`. Image CDN folders up to 2026-05-15 are **not** card dates. TOS: タレント無料. Worker % **not** on TOS → unstated. |
| B04 | CrowdLinks | **`needs_check`** | Listing is a login wall. Sample project pages embed `publishedDateTime` 2026-03-31…2026-05-21 with `publishedEndDate` already past this GET. Help FAQ 2026/8/3. Worker 無料; listed pay not commission-cut. No yen table. Do not buy 有料会員. |
| B05 | AI CrowdWorks | **`needs_check`** | `/projects/` and `/ai-workers/` =「読み込み中」. Official news 2026.8.20. Pre-reg LP redirects home. Register JS: CW ID or email. Do not copy main CrowdWorks 5–20%. Not `dead`. |

`alive` / `thin` / `dead`: **0** this batch.

---

## What this merge does not do

- Create accounts, complete OAuth, or send MAIN Google
- Upload KYC / bank / tax IDs
- Publish profiles, plans, classes, notes, or listings
- Bid / apply / 応募 / 「話を聞きたい」
- Subscribe to PPH Basic / TopAccess / Workana Priority / YOUTRUST 公式リクルーター / Gulp Membership / CrowdLinks 有料会員
- Copy sibling paste-pack bodies or HTTP dumps
- Invent listing counts, GMV, or traffic
- Start Wave B / C / D CU (Wave A serial still owns the live box until Freelancer parks)
- Merge or un-draft the four source PRs

# STATUS — Wave D-early sample (D02 / D03 / D04 / D07)

Stamp: **2026-09-16 JST**  
Folder: `earn-waved-early-gates-20260916/`  
State: **DRAFT_ONLY**

Independent public GET (this IP). Sibling bodies not copied.

## keep_queue (2) — `alive`, CU `early`

Behind Wave A/B. Parent QUEUE for both is Wave **C**. Draft only if a later CU opens them. This PR does not register.

| # | Desk | Parent QUEUE | Freshness seen this GET | Stop |
|---|---|---|---|---|
| D03 | note | C (C4) | Top HTML `publishAt` **2026-09-14** / **2026-09-15** (+09:00) | Do not publish paid notes / memberships. 口座 → morning |
| D04 | Braintrust | C (C8) | `/jobs` role cards; blog heading date **Sep 14, 2026** | ID-verified / Certified / screening UI → STOP. Do not apply |

CU `early` here means “Wave D-early KEEP batch after A/B”, not “jump the live A serial”.

## skip_log (1) — `dead`, CU `skip`

Detail: [SKIP.md](SKIP.md). Do not return this to QUEUE unless the operator explicitly GO-s a **different** desk.

| # | Desk | gate_result | Evidence (this GET) |
|---|---|---|---|
| D07 | Twago | `dead` | `twago.com` **301** → `talent-pool.com` (“complete Talent Pool solution”, white-label, Official Fieldglass Partner). No public freelance job board. `twago.de` **404** |

## needs_check (1) — CU `late`

| # | Desk | Why not alive / not SKIP |
|---|---|---|
| D02 | カイコク | LP + 無料登録 CTA live. Register `会員登録前` 200. Public “案件事例” have **no listing dates**. CMS logo `publishedAt` 2025-08-18 is not a job card. LP “登録者数 / 累計案件掲載数” is marketing — unused. Not closed. |

## Out of this sample

| # | Desk | This pack | Elsewhere |
|---|---|---|---|
| D05 | Twine | not re-opened | PR#22 `alive` · PR#13 pass |
| D06 | Fastwork | not re-opened | PR#22 `alive` · PR#13 pass |

`thin`: **0**

## Live CU pointer (not this folder)

This sample does **not** move the Wave A live box. Do not start D-early CU while Wave A `pending` / `blocked_skip` rows are open.

## Not done

Account create · OAuth finish · KYC upload · publish · bid · paid subscribe · secret commit · traffic invention.

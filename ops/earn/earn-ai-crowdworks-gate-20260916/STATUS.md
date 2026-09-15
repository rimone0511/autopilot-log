# STATUS — B05 AI CrowdWorks (activity-gate + CU NO-GO)

> ## NO-GO / NOT A LIVE CU
>
> **2026-09-16.** Dedicated re-GET of **AI CrowdWorks** (`ai.crowdworks.jp`).
> **CU: skip profile draft.** Gate stays **`needs_check`**.
> Pre-reg **ended**. Email register **surface** is open (JS). Public job details **not** readable logged-out.
> Do **not** treat this pack as next live CU after Freelancer.com (A10 / CU-10).
> Wave B register serial remains **REGISTER-CU-CUT** ([PR#72](https://github.com/rimone0511/autopilot-log/pull/72)). Prefer JOBS phase (do-not-send).
> Keep **DRAFT_ONLY**.

Snapshot: **2026-09-16 JST**  
Folder: `ops/earn/earn-ai-crowdworks-gate-20260916/`  
State: **DRAFT_ONLY** / **`needs_check`** / **CU NO-GO**  
Authoring: logged-out public GET only. **No signup. No OAuth. No POST. Cookie values not saved.**

Forbidden: secrets, passwords, OTP, CSRF, Keen write keys, KYC files, signup from this authoring agent, 興味がある, 仕事依頼, paid plans, invented traffic/GMV/fee %.

Python posting-gate tests were **not** edited.

---

## Verdict

| Item | Status |
|---|---|
| This folder | **ready · draft** (markdown only) |
| Gate this folder | **`needs_check`** |
| Sibling activity-gate | **needs_check** (PR#12 / PR#62). This GET did **not** promote to `alive` |
| Pre-reg LP | **closed** (301 → home) |
| Email signup surface | **open in JS**; form **not** submitted |
| Public job HTML | **読み込み中** — no titles / dates |
| Public list/detail API | **401** logged-out |
| Live CU / profile draft | **not_run** — **skip** |
| Account claimed | **no** |

## CU hint (this desk)

| Hint | Meaning here |
|---|---|
| `pack_ready` | One-pager + NOTE + STOP exist. **Not** a play GO |
| `pending` | Live CU has **not** marked a draft from **this** folder |
| `park_until_board_readable` | Human must see dated `/projects/` cards before any draft |
| `kyc_wait` | 本人確認 / 口座. Morning user. No upload |
| `register_cu_cut` | Wave B register serial cut. **Not** next live CU. Prefer JOBS |

Current row (authoring time):

| ID | Desk | QUEUE | CU | Google | Gate | CU hint | Next |
|---|---|---|---|---|---|---|---|
| B05 | AI CrowdWorks | **B15** | CU-26 | EMAIL_ONLY (register JS). Google listed on **login** JS; `/aicw/auth/google` 404 | **`needs_check`** | `pack_ready` + `pending` + **park** | **Do not CU-play.** If a human later GOs **after** a readable board: email `{{EMAIL}}` → profile **draft** → **STOP before 興味がある / KYC** |

Do **not** confuse:

| Label | Desk |
|---|---|
| this folder **B05** | AI CrowdWorks |
| QUEUE **B5** | Anycrew |
| QUEUE **B15** | AI CrowdWorks (canonical WAVE letter) |
| QUEUE **A4** / PR#17 | Main CrowdWorks (`crowdworks.jp`) |
| B04 | CrowdLinks (`crowdlinks.jp`) |

## Pack files

| File | Role |
|---|---|
| [CU-ONE-PAGER.md](CU-ONE-PAGER.md) | Go / no-go |
| [NOTE.md](NOTE.md) | Evidence. Pointers; no bios copied |
| [STOP.md](STOP.md) | 興味がある / 依頼 / KYC / old LP |
| [STATUS.md](STATUS.md) | This box |

## Complement (bodies not copied)

| PR | Relation |
|---|---|
| [#12](https://github.com/rimone0511/autopilot-log/pull/12) | JP Wave B gate `needs_check` (`records/09`) |
| [#62](https://github.com/rimone0511/autopilot-log/pull/62) | Batch1 B03/B04/B05 still `needs_check` |
| [#34](https://github.com/rimone0511/autopilot-log/pull/34) | CU-26 paste + JA bios |
| [#65](https://github.com/rimone0511/autopilot-log/pull/65) | NEXT-CU: this desk not a GO |
| [#72](https://github.com/rimone0511/autopilot-log/pull/72) | Alive serial; **REGISTER-CU-CUT**; skips B03–B05 |

`alive` catalog / `dead` / `thin`: **0 this folder** (single desk; `needs_check`).

---

## This GET (logged out)

UA: ordinary desktop Chrome string. No login cookie on API calls. CSRF / session values / analytics write keys were **not** stored.

| URL | HTTP | Note |
|---|---|---|
| https://ai.crowdworks.jp/ | 200 | Title 人材マッチング. Nav ログイン / 会員登録 / 仕事一覧. Marketing 10,000名. Category「現在募集中」examples |
| https://ai.crowdworks.jp/projects/ | 200 | 「読み込み中」twice. 興味がある copy. No cards |
| https://ai.crowdworks.jp/ai-workers/ | 200 | 「読み込み中」. No cards |
| https://ai.crowdworks.jp/lp/pre-registration/ | 301 → `/` | Pre-reg closed |
| https://ai.crowdworks.jp/_astro/202609/AicwProjectsApp.9mAtjQ-G.js | 200 | Login-gate copy + hardcoded teaser `publishedAt` 2026-09-04 `url:null` |
| https://crowdworks.jp/aicw/register/new_email | 200 | Noscript shell; register JS 無料メール / CW ID |
| https://crowdworks.jp/aicw/login | 200 | Noscript shell; login JS lists Google / Yahoo / Facebook |
| https://crowdworks.jp/aicw/auth/google | 404 | Not a register form |
| https://crowdworks.jp/aicw/register | 404 | Wrong path |
| https://crowdworks.jp/aicw/register/enable_aicw | 200 (HEAD) | Existing-CW enable. Not used |
| https://crowdworks.jp/aicw/consult | 200 | Title 仕事を依頼する. Client |
| https://cw-assets.crowdworks.jp/vite/2026-09/1/packs/raw_pages/aicw/register/new_email.ts-DFNN0VPZ.js | 200 | 「カンタン無料会員登録」 |
| https://cw-assets.crowdworks.jp/vite/2026-09/1/packs/raw_pages/aicw/login.ts-heVGr2pB.js | 200 | Google listed as login `serviceName` |
| https://crowdworks.jp/api/v3/public/aicw/projects/list | **401** | `authentication_method: not_yet` |
| https://crowdworks.jp/api/v3/public/aicw/ai_workers/list | **401** | same |
| https://crowdworks.jp/api/v3/public/aicw/project/1/detail | **401** | same |
| https://ai.crowdworks.jp/projects/1/ | 404 | |
| https://ai.crowdworks.jp/api/projects/ | 404 | |
| https://ai.crowdworks.jp/projects.json | 404 | |
| https://ai.crowdworks.jp/sitemap.xml | 404 | |
| https://crowdworks.co.jp/news/akdv13x1sf/ | 200 | Formal release **2026.8.20** |
| https://crowdworks.co.jp/news/oo-gssosbypi/ | 200 | Pre-reg **2026.5.14**. Q5 完全無料 |

Signed asset query strings, session cookie values, and third-party write keys were **not** stored.

Fees: register heading 無料; pre-reg Q5 無料 (closed LP). Formal-release news: no worker %. Home FAQ 費用 = client お見積り. Main-site `/fees` **not opened**.

---

## After live CU (leave blank until a run)

Fill only secret-free keys. Do not paste OTP, ID, a phone, CSRF, or cookies.

```
desk: AI CrowdWorks
pack: ops/earn/earn-ai-crowdworks-gate-20260916/
auth:
otp:
kyc:
board_readable:
draft_profile:
publish: no
interest_click: no
apply: no
next:
```

Outcome so far: **not_run** (NO-GO).

---

## Next (human)

1. **Do not CU-play this desk from this PR.** Keep draft.
2. Optional glance: open https://ai.crowdworks.jp/projects/ in a real browser. If cards + dates appear, re-label then. If still empty / login-walled, **stay parked**.
3. Do not merge until Yuta reviews.
4. Do not rewrite QUEUE B5 (Anycrew) or A4 (main CrowdWorks).

## This PR / pack will not

- Copy sibling paste bios
- Create a marketplace account
- Click 興味がある / 仕事を依頼する / Jicoo
- Upload ID / selfie / bank / My Number
- Invent fee % or listing counts
- Change Python posting-gate tests
- Start Wave B register CU after Freelancer (cut; prefer JOBS)

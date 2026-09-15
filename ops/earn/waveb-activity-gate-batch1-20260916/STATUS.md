# STATUS — Wave B activity-gate batch 1

Observed: **2026-09-16 JST**. Login: **no**. Signup: **no**. Publish: **no**. Secrets: **none**.

Python posting-gate tests were **not** edited. `python3 tests/test_gate.py` and `python3 tests/test_tiktok_gate.py` still pass on this branch.

## Rollup

| Gate | Count | Desks |
|---|---|---|
| `alive` | **0** | — |
| `needs_check` | **3** | B03 複業クラウド, B04 CrowdLinks, B05 AI CrowdWorks |
| `thin` | **0** | — |
| `dead` | **0** | — |

None of the three were promoted from PR #12 `needs_check`. Public job **titles** exist on B03 and B04; **recent open-card dates** still were not confirmed on a logged-out listing.

## One-line each

| ID | Official URL | Public jobs / dates (what this GET saw) | Signup path | Fees (official page only) | CU tip | Gate |
|---|---|---|---|---|---|---|
| B03 | https://talent.aw-anotherworks.com/ | Individual `/projects/{id}` titles (incl. フルリモート). No listing `created_at`. Image CDN folders include `2026-05-15` — **not** a card date. `/projects/` 404. | Public JS: Google / Apple / Facebook「…でサインイン」+ email field. Buttons not in static HTML. | TOS 第2.1条1: 登録タレントは無料. Worker % **not** on TOS → unstated. | Talent domain only. Confirm Google on `/sign_up`. Draft only. Do not apply. | **needs_check** |
| B04 | https://crowdlinks.jp/ (worker app) | `/worker/projects/` and `/projects` = filters + login wall, **no cards**. Individual pages have titles + embedded `publishedDateTime` **2026-03-31…2026-05-21** (35-URL sample); matching `publishedEndDate` **2026-05-22…2026-07-17** (already past this GET). Help FAQ updated **2026/8/3**. | Signup JS:「Googleで登録する」and「メールアドレスで登録する」. Login JS:「Googleでログイン」/ Facebook. | FAQ: worker use 無料; listed pay is not commission-cut. TOS: 無料会員 / 有料会員 (no yen table on pages opened). | Worker `/signup/` only. Prefer Google (FAQ: cannot switch). Do not buy 有料会員. Do not apply. | **needs_check** |
| B05 | https://ai.crowdworks.jp/ | `/projects/` and `/ai-workers/` =「読み込み中」. No dated job cards. Official news **2026.8.20** formal release. Pre-reg LP now redirects home. | Register JS:「カンタン無料会員登録」= クラウドワークスID **or**「メールアドレスで登録する」. Login JS also lists Google / Yahoo / Facebook under「他のアカウントでログイン」. `/aicw/auth/google` **404**. | Register heading 無料. Pre-reg news Q5 (2026.5.14)「一切かかりません」. Formal-release news has **no** worker %. Do not copy main CrowdWorks 5–20%. | Not main CrowdWorks. Do not submit register. Human opens `/projects/` in a browser before any CU. | **needs_check** |

## HTTP log (public GET only)

UA: ordinary desktop Chrome string. No login cookie.

| URL | HTTP | Note |
|---|---|---|
| https://talent.aw-anotherworks.com/ | 200 | SPA shell. Title 複業クラウド. OG says 完全無料 (marketing; TOS is the fee cite) |
| https://talent.aw-anotherworks.com/sign_up | 200 | Title 新規登録. Buttons not in static HTML |
| https://talent.aw-anotherworks.com/login | 200 | Title サインイン |
| https://talent.aw-anotherworks.com/_next/static/chunks/2ft1bogak3uo6.js | 200 | `signInGoogle` / label「Googleでサインイン」 |
| https://talent.aw-anotherworks.com/projects/91374 | 200 | Title 法人SNS運用ディレクター募集. Body loader |
| https://talent.aw-anotherworks.com/_next/data/8xWpf_UM-Ow_9wUJEAg3E/projects/91374.json | 200 | title + imageUrl only. No posting date field |
| https://talent.aw-anotherworks.com/projects/ | 404 | Sitemap lists this path; it 404s |
| https://talent.aw-anotherworks.com/sitemap.xml | 200 | Home + `/projects/` only. No lastmod |
| https://cl.aw-anotherworks.com/user_tos | 200 | 第2.1条1 タレント無料 |
| https://crowdlinks.jp/ | 200 → https://start.crowdlinks.jp/ | Marketing LP |
| https://crowdlinks.jp/worker/signup/ | 200 | Title 新規登録【クラウドリンクス】. SPA |
| https://crowdlinks.jp/login/ | 200 → `/worker/login/` | SPA loader in HTML |
| https://crowdlinks.jp/worker/projects/ | 200 | Filters incl. 新着順. No cards |
| https://crowdlinks.jp/projects | 200 | 「ご登録いただくと、プロジェクトのすべての情報をご覧いただけます」 |
| https://crowdlinks.jp/projects/SCBqKcJyW5fdUXOoGX7U | 200 | Title + `publishedDateTime` / `publishedEndDate` in HTML. Also AWS `X-Amz-Date` — **not** a job date |
| https://crowdlinks.jp/sitemap.xml | 200 | 299 project locs. **No lastmod** |
| https://crowdlinks.jp/worker/_next/static/chunks/pages/signup-654dee2220da40e7.js | 200 | Google / email register labels |
| https://crowdlinks.jp/worker/_next/static/chunks/pages/login-d30fd72bc87effc8.js | 200 | Google / Facebook login labels |
| https://help.crowdlinks.jp/ | 200 | User FAQ index shows 2026/8/1 13:50 |
| https://help.crowdlinks.jp/0029649d31534622a6d95ffe53df18dd | 200 | Article timestamps 2024/7/29 and **2026/8/3 13:50** |
| https://crowdlinks.jp/terms | 200 | 無料会員 / 有料会員. 実務経験 2年 condition |
| https://ai.crowdworks.jp/ | 200 | Client-facing LP. Nav: ログイン / 会員登録 / 仕事一覧 |
| https://ai.crowdworks.jp/projects/ | 200 | 「読み込み中」twice. No cards |
| https://ai.crowdworks.jp/ai-workers/ | 200 | 「読み込み中」. No expert cards |
| https://ai.crowdworks.jp/lp/pre-registration/ | 200 → `/` | Pre-reg closed |
| https://crowdworks.jp/aicw/register/new_email | 200 | Curl noscript error; register JS still fetched |
| https://crowdworks.jp/aicw/login | 200 | Same noscript; login JS lists Google |
| https://crowdworks.jp/aicw/auth/google | 404 | Direct path not a register form |
| https://cw-assets.crowdworks.jp/vite/2026-09/1/packs/raw_pages/aicw/register/new_email.ts-DFNN0VPZ.js | 200 | 「カンタン無料会員登録」 |
| https://crowdworks.co.jp/news/akdv13x1sf/ | 200 | Formal release **2026.8.20** |
| https://crowdworks.co.jp/news/oo-gssosbypi/ | 200 | Pre-reg **2026.5.14**. Q5 worker 登録無料 |

Signed asset query strings were **not** stored.

## Next (human)

1. Do not CU-play these three from this folder.
2. B03 / B04: glance at **one logged-in or fully rendered listing date** before any draft register.
3. B05: open `/projects/` in a real browser; if still empty, park. Do not treat as `dead`.
4. Keep PR draft. Do not merge until Yuta reviews.

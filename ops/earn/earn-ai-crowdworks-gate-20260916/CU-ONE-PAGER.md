> **DRAFT_ONLY. CU NO-GO.** This authoring session did not sign up, did not POST, did not start OAuth, did not press 興味がある.
> **MAIN Google mailbox only** if a later human GO names this desk — as `{{EMAIL}}`. Register JS has **no** Google control.
> **No secrets.** No session cookies, OTP, CSRF, Keen keys, or ID photos in git.
> **No invented traffic / fees.** Marketing「10,000名」and teaser `feeMin`/`feeMax` are **not** activity or a worker %.

# CU go / no-go — B05 AI CrowdWorks（AIクラウドワークス）

Stamp: **2026-09-16 JST** (~2026-09-15 21:06–21:08 UTC this env)  
Folder: `ops/earn/earn-ai-crowdworks-gate-20260916/`  
Official: https://ai.crowdworks.jp/

| | |
|---|---|
| **CU** | **NO-GO** — do not play from this folder |
| Gate | **`needs_check`** |
| Profile draft | **SKIP** until a human sees dated cards on `/projects/` |
| skip-agent / `thin` / `dead` | **no** (origin + register URL + 2026.8.20 news are up) |

This is **not** main CrowdWorks (`crowdworks.jp` / QUEUE **A4**). Do not paste A4 bids or main-site system fees here.

## Five answers (this GET only)

| Question | Answer | Evidence (this GET) |
|---|---|---|
| Pre-reg ended? | **Yes.** | https://ai.crowdworks.jp/lp/pre-registration/ → **301** → `https://ai.crowdworks.jp/`. Formal-release news **2026.8.20**. Do not hunt the old LP form. |
| Free email signup open? | **Surface yes. Not submitted.** | https://crowdworks.jp/aicw/register/new_email **200**. HTML here is the noscript / “enable JavaScript” shell. Public register JS (asset folder `vite/2026-09/1`) heading **「カンタン無料会員登録」** + **「メールアドレスで登録する」** + existing **「クラウドワークスIDで登録する」**. POST **not** sent. |
| Public job detail readable? | **No (logged out).** | `/projects/` **200** visible text: heading「仕事一覧」+「『興味がある』…会員の方から」+ **「読み込み中」「読み込み中」**. No titles, no dates in HTML. `GET /api/v3/public/aicw/projects/list` and `/api/v3/public/aicw/project/1/detail` → **401** `ApiV3::UnauthorizedError` `authentication_method: not_yet`. `/projects/1/` **404**. |
| Google vs email? | **Email (register). Google on login JS only.** | Register JS: **no** `Google` / Yahoo / Facebook. Login JS section **「他のアカウントでログイン」** lists `serviceName: "Google"` / `"Yahoo! JAPAN ID"` / `"Facebook"`. Direct https://crowdworks.jp/aicw/auth/google → **404** title「ページが見つかりませんでした【クラウドワークス】」. OAuth **not** started. |
| CU profile draft or skip? | **Skip.** | Board unread + REGISTER-CU-CUT + QUEUE “目視してから”. Signup being a **free-looking surface** is not a play GO. |

## Why not `alive` / not `dead`

- Official news https://crowdworks.co.jp/news/akdv13x1sf/ dated **2026.8.20**: formal release. Used as **company date**, not as a job card.
- Home「事前登録AI技術者・専門家 10,000名以上」and the same news headcount: **marketing**. Not traffic proof.
- Home「現在募集中の仕事」is **category examples** (Claude Code利用支援, Gemini Enterprise構築, …), not dated cards.
- Public JS `ProjectsLoginGate` embeds a **hardcoded teaser** (`url: null`, `aria-hidden`) with `publishedAt: "2026-09-04T10:00:00+09:00"`. Overlay copy: **「すべての仕事を閲覧するには会員登録またはログインが必要です」** / **「会員登録(無料)」**. That teaser is **not** a live public job. Yen fields on it are **not** copied here (not a worker %; not a live listing).
- Unread SPA + 401 list is **not** `dead` and **not** `thin`.

## ID crosswalk (do not mix)

| Label | Desk |
|---|---|
| this folder **B05** | AI CrowdWorks (`ai.crowdworks.jp`) — same numbering as [PR#62](https://github.com/rimone0511/autopilot-log/pull/62) |
| QUEUE **B15** | AI CrowdWorks — canonical WAVE letter. **CU-26** |
| QUEUE **B5** | **Anycrew** — different desk |
| QUEUE **A4** | Main CrowdWorks (`crowdworks.jp`) — different desk |
| PR#12 `records/09` | Same product, older short gate row |
| PR#12 `records/05` | Anycrew |

## If a human later types GO (not this PR)

1. Open `/projects/` in a **browser**. If still「読み込み中」or empty of dates → **stay parked**.
2. Only then: https://crowdworks.jp/aicw/register/new_email — **メール** `{{EMAIL}}` (MAIN mailbox) **or** existing CrowdWorks ID. Do not invent a new Yahoo / Facebook. If a Google **login** control appears, MAIN Google only — still **after** the board is worth a draft.
3. Profile **draft**. **0** 興味がある. **0** 応募. Client「仕事を依頼する」/ 無料相談 / Jicoo: **close**.
4. KYC / 口座 / 本人確認: **STOP** ([STOP.md](STOP.md)). Morning user.
5. Worker %: this GET did **not** see an AI-CW page that states it. **Do not** copy main CrowdWorks 5–20%.

Sibling paste (do **not** copy bodies): [PR#34 `04-ai-crowdworks.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-week2-rest-cu-paste-e6ce/earn-week2-rest-cu-paste-20260916/04-ai-crowdworks.md).

## This PR will not

- Create an account, finish OAuth, or submit the email form
- Treat `needs_check` as `alive` or as skip-agent
- Play Wave B register serial ([PR#72](https://github.com/rimone0511/autopilot-log/pull/72) **REGISTER-CU-CUT**)
- Rewrite PR#12 / PR#62 folders

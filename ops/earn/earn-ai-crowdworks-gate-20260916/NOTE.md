> **DRAFT_ONLY.** Logged out. Did not register. Did not apply. No secrets.
> **CU NO-GO** — see [CU-ONE-PAGER.md](CU-ONE-PAGER.md). Skip profile draft from this folder.
> **Not** main CrowdWorks. Do not copy main-site worker system fees onto this desk.

# NOTE — B05 AI CrowdWorks（AIクラウドワークス）

Stamp: **2026-09-16 JST**  
Folder: `ops/earn/earn-ai-crowdworks-gate-20260916/`  
Gate here: **`needs_check`**. **Not** skip-agent. **Not** a live register GO.

| キー | 値 |
|---|---|
| this_folder | **B05** (PR#62 numbering; **not** QUEUE B5 Anycrew) |
| QUEUE | **B15** |
| cu_serial | **CU-26** |
| activity_gate (siblings) | **needs_check** ([PR#12](https://github.com/rimone0511/autopilot-log/pull/12) `records/09`; [PR#62](https://github.com/rimone0511/autopilot-log/pull/62) `b05`) |
| gate **this folder** | **`needs_check`** — public cards still unread; APIs 401 logged-out |
| Google | **EMAIL_ONLY** on register JS. Login JS lists Google / Yahoo / Facebook. `/aicw/auth/google` **404**. OAuth not started |
| self_serve | **unknown** until the board is readable. Public copy is 運営アサイン / 興味がある (member) |
| official | https://ai.crowdworks.jp/ |
| signup | https://crowdworks.jp/aicw/register/new_email |
| login | https://crowdworks.jp/aicw/login |
| projects | https://ai.crowdworks.jp/projects/ |
| workers | https://ai.crowdworks.jp/ai-workers/ |
| news_release | https://crowdworks.co.jp/news/akdv13x1sf/ (**2026.8.20**) |
| news_prereg | https://crowdworks.co.jp/news/oo-gssosbypi/ (**2026.5.14**) |
| CU hint | `pack_ready` is **false** as a play GO. `pending` + **park** |

## Official URLs (this GET)

Product origin nav (home 200): ログイン, 会員登録, 仕事一覧, AI技術者・専門家一覧, 仕事依頼, 無料相談.

| URL | HTTP | What this GET actually saw |
|---|---|---|
| https://ai.crowdworks.jp/ | 200 | Title「AIクラウドワークス - AI特化版人材マッチングプラットフォーム」. `Last-Modified: Tue, 15 Sep 2026 07:27:43 GMT` is **static asset**, not a job date. |
| https://ai.crowdworks.jp/projects/ | 200 | Title「仕事一覧 - AIクラウドワークス」. **「読み込み中」×2**. No job titles. |
| https://ai.crowdworks.jp/ai-workers/ | 200 | Title「AI技術者・専門家一覧」. **「読み込み中」×2**. No expert cards. |
| https://ai.crowdworks.jp/lp/pre-registration/ | **301 → /** | Pre-reg **closed**. |
| https://crowdworks.jp/aicw/register/new_email | 200 | Title「AIクラウドワークス」. Visible HTML: JavaScript-required error shell. Register JS still loaded. |
| https://crowdworks.jp/aicw/login | 200 | Title「ログイン - AIクラウドワークス」. Same noscript shell. Login JS loaded. |
| https://crowdworks.jp/aicw/auth/google | **404** | Title「ページが見つかりませんでした【クラウドワークス】」. |
| https://crowdworks.jp/aicw/consult | 200 | Title「仕事を依頼する - AIクラウドワークス」. **Client.** Out of scope. |
| https://crowdworks.jp/aicw/register | **404** | Not the register entry. Use `/aicw/register/new_email`. |
| https://ai.crowdworks.jp/register/ · `/signup/` · `/login/` | **404** | Product origin has no those paths. |
| https://crowdworks.co.jp/news/akdv13x1sf/ | 200 | **2026.8.20** プレスリリース「本日正式リリース」. |
| https://crowdworks.co.jp/news/oo-gssosbypi/ | 200 | **2026.5.14** 事前登録開始. Q5 worker 登録 **「一切かかりません。完全無料です。」** Form URL in that article is the **closed** LP. |
| `GET /api/v3/public/aicw/projects/list` | **401** | JSON `ApiV3::UnauthorizedError`, `authentication_method: "not_yet"`. Cookie **not** sent. |
| `GET /api/v3/public/aicw/ai_workers/list` | **401** | Same. |
| `GET /api/v3/public/aicw/project/1/detail` | **401** | Same. |
| https://ai.crowdworks.jp/projects/1/ | **404** | Guessed id. Not a readable detail page. |
| https://ai.crowdworks.jp/api/projects/ · `/projects.json` · `/sitemap.xml` | **404** | S3 `NoSuchKey`. |

Home hrefs this GET (seller vs client):

- 会員登録 → `https://crowdworks.jp/aicw/register/new_email`
- ログイン → `https://crowdworks.jp/aicw/login`
- 仕事一覧 → `/projects/`
- 仕事依頼 / 無料相談 → `https://crowdworks.jp/aicw/consult` and Jicoo `https://www.jicoo.com/t/cw_ai_bpo/e/aicwtop` — **client booking. Do not open as CU.**

## Public jobs / dates

HTML of `/projects/` did **not** show cards. Public list/detail APIs **401** logged-out.

Public JS `AicwProjectsApp` (`/_astro/202609/AicwProjectsApp.9mAtjQ-G.js`):

- Copy:「AIクラウドワークスの最新の仕事を表示しています。登録することですべての仕事を見ることができます。」
- Copy:「『興味がある』ボタンを押していただいた会員の方から、優先的に仕事をご案内いたします。」
- Component `ProjectsLoginGate`: overlay **「すべての仕事を閲覧するには会員登録またはログインが必要です」** + CTA **「会員登録(無料)」**
- Teaser object in that gate: `url: null`, `aria-hidden`, `publishedAt: "2026-09-04T10:00:00+09:00"`. **Hardcoded teaser, not a live listing.** Do not treat as activity. Do not copy its yen fields.

Home「現在募集中の仕事」:「注目の新規案件が続々と公開中。一部案件をご紹介します。」then **ご依頼可能な仕事例** (AI社内規定策定, Claude Code利用支援, Gemini Enterprise構築, 広告レポート…, ルーチンワーク自動化). Category examples. **Not** dated board rows.

`thin_site_skip`: **false**.

## Signup path

**Register JS** (`…/aicw/register/new_email.ts-….js`, asset folder `2026-09/1`):

- Heading **「カンタン無料会員登録」**
- **「すでにクラウドワークスをご利用の方」** → **「クラウドワークスIDで登録する」**
- **「クラウドワークスIDをお持ちでない方」** → **「メールアドレス」** + **「メールアドレスで登録する」**
- Note: after register, main CrowdWorks services may also be available
- Agree to 利用規約 + 個人情報の取り扱い
- After submit (not done):「仮登録ありがとうございます」/ confirm mail / URL valid **24 hours** / allow `@crowdworks.jp`
- **No Google control**

**Login JS** (`…/aicw/login.ts-….js`):

- メールアドレス + パスワード +「ログイン」+「ログイン状態を保存する（30日間）」
- 「クラウドワークスのアカウントでログインが可能です。」
- 「他のアカウントでログイン」: `serviceName: "Google"`, `"Yahoo! JAPAN ID"`, `"Facebook"`
- Imports `useAwsWafLoginProtection` — do not loop login
- Direct `/aicw/auth/google` **404**. OAuth URL constructors were **not** followed.

CU: seller entry is **email or existing CrowdWorks ID**. Do not create Yahoo / Facebook for this desk. Do not start Google from this agent.

`HEAD` https://crowdworks.jp/aicw/register/enable_aicw → **200**. Existing-CW enable path. **Not** used. Do not convert accounts from this note.

Session cookie name `_cw_session_id` was **issued** by HTML GET to crowdworks.jp. **Value not stored.** Further API calls in this session were sent **without** that cookie.

## Fee notes (official pages only)

1. Register JS heading: **「カンタン無料会員登録」**. Login-gate CTA: **「会員登録(無料)」**.
2. Pre-reg news (2026.5.14) Q5: worker 登録 **「一切かかりません。完全無料です。」** That article’s signup URL is the **closed** LP. Cite the news page, not a live form.
3. Formal-release news (2026.8.20): **no worker fee %** in the text this GET read. Client CTA「まずは無料相談」.
4. Home FAQ「費用はどのくらいかかりますか？」: **client / 依頼** — ご予算 / お見積り / 無料相談 or 仕事依頼フォーム. Not a worker rate.
5. Public JS also lists main-site paths `/fees` and `/pages/guides/employer/pricing`. Those are **CrowdWorks proper / client**. **Not opened.** **Do not** copy main-site worker system fees onto AI CrowdWorks unless an AI-CW page states them. This GET did not see that %.

## Pointers (do not copy paste bodies)

| Sibling | What it is | Use |
|---|---|---|
| [PR#12 `records/09-ai-crowdworks.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-activity-gate-waveb-jp-fced/earn-activity-gate-waveB-20260916/records/09-ai-crowdworks.md) | First JP Wave B gate row | `needs_check`. This folder re-GETs; does not rewrite #12 |
| [PR#62 `b05-ai-crowdworks.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/waveb-activity-gate-batch1-7559/ops/earn/waveb-activity-gate-batch1-20260916/b05-ai-crowdworks.md) | Batch1 three-desk gate | Same product. This folder is the **CU one-pager**, not a copy of that file |
| [PR#34 `04-ai-crowdworks.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-week2-rest-cu-paste-e6ce/earn-week2-rest-cu-paste-20260916/04-ai-crowdworks.md) | CU-26 paste + JA bios | Paste **only** if a later human GO happens after the board is readable. Bios **not** duplicated |
| [PR#72](https://github.com/rimone0511/autopilot-log/pull/72) | Wave B alive serial | **REGISTER-CU-CUT**. Skips B03–B05 `needs_check`. Do not chain Freelancer → this desk |
| [PR#65](https://github.com/rimone0511/autopilot-log/pull/65) | Morning merge NEXT-CU | AI CrowdWorks: register CU cut; `needs_check` still not a GO |
| [PR#17](https://github.com/rimone0511/autopilot-log/pull/17) | Lancers + **main** CrowdWorks | Different desk (A4) |

This folder does **not** rewrite those PRs.

## Skip / park this desk if

Board still「読み込み中」 / API still 401 / OTP missing / 本人確認 / 興味がある is the only next step / client 相談 UI. Then **do not** invent a next Wave B register desk from here (cut; prefer JOBS). Record secret-free keys in [STATUS.md](STATUS.md).

> **MAIN Google only if a later human CU happens.** Official help lists **Googleアカウント連携**. `/sign_in` static HTML is a SPA shell — Google **button not in HTML** this GET (GTM ≠ OAuth). Facebook / LINE: do not use.
> **DRAFT_ONLY.** Public GET. **No live signup.**
> **Warm intro / scout shape.** Talent conversion this GET is 「話を聞きたい」→ カジュアル面談, or inbound **スカウト** (recruiter-side). Not a self-serve bid catalog.
> **STOP.** See [STOP.md](STOP.md). Do not send 「話を聞きたい」. Do not post a job. Do not buy 公式リクルーター.
> **No secrets.** No CSRF / cookies / passwords / OTP in git.
> **No invented fees / traffic.** Poster-side: ジョブ 1件まで無料 (help). Applicant % **unread**. Scout 通数 is recruiter-plan copy — not a talent fee.

# NOTE — B18 YOUTRUST (activity gate)

Stamp: **2026-09-16 06:07 JST**  
Folder: `earn-youtrust-gate-20260916/`  
State: **DRAFT_ONLY**

This is an **activity-gate note** for one desk. It records what a **logged-out** GET showed. It is **not** a live register GO.

| キー | 値 |
|---|---|
| this_folder | **B18** |
| QUEUE | **B13** |
| cu_serial | **CU-24** |
| official | https://youtrust.jp/ (this GET: **302 → `/lp` 200**) |
| sign_in | https://youtrust.jp/sign_in (**200** SPA) |
| signup | https://youtrust.jp/signup (**404**. Do not use) |
| jobs_list | https://youtrust.jp/recruitment_posts (**200** SPA shell) |
| jobs_api | `GET https://youtrust.jp/api/recruitment_posts` (**401** JSON) |
| help_create | https://help.youtrust.jp/user/account/create/ |
| help_jobs | https://help.youtrust.jp/user/message/search-jobs/ |
| help_talk | https://help.youtrust.jp/user/message/want-to-talk/ |
| sibling_gate | [PR#12](https://github.com/rimone0511/autopilot-log/pull/12) + [PR#59](https://github.com/rimone0511/autopilot-log/pull/59) both **`needs_check`** |
| gate **this GET** | **`needs_check`** (API 401; card dates unread). **Not** `pass`. **Not** `thin` / `dead` |
| product_shape | **warm_intro_scout** (help + jobs meta). Not bid. Not interview-agent |
| CU **this pass** | **`skip_live_cu`** — see below |
| CU **if later human GO** | **`profile_only`** — draft only. Not skip-as-thin |

Sibling paste pack (bodies **not** copied): [PR#30](https://github.com/rimone0511/autopilot-log/pull/30) `05-youtrust.md`.

---

## Product shape (evidence): warm intro / scout

This GET did **not** show a marketplace 応募 form with a public bid button. Public copy points to **interest notify + casual talk**, plus a **recruiter scout** product on the company side.

**Jobs list meta** (`/recruitment_posts` 200):

> YOUTRUSTに掲載中の副業・転職のジョブ（旧：募集）一覧です。気になる内容があれば気軽に「話を聞きたい」をして、カジュアル面談に進みましょう！

**Help — 「話を聞きたい！」** (`want-to-talk/` 200):

- Button notifies the **poster** (企業・個人) that you are interested.
- **Logged out (Web):** job detail 「話を聞きたい！」 → **新規登録画面**. After create, interest is notified.
- **Logged in:** button → メッセージ送信画面. Send = notify.
- Help: fill the profile first; a blank profile may get no reply. Reply is **not** guaranteed.
- Next step named: **カジュアル面談**.

**Help — カジュアル面談 vs 面接** (`casual-vs-interview/` 200): カジュアル面談 = 選考前の情報交換. 副業・業務委託ではカジュアル面談の合意から契約に進むケースもある、とヘルプは書く. That is **not** a CU GO to book 面談.

**Help — ジョブは公開** (`search-jobs/` 200): 「ジョブは全てのユーザーに公開され、アプリとWebの両方から確認できます。」  
Public-to-all ≠ dates in logged-out HTML. Cards were **not** in the static shell this GET.

**LP meta** (`/lp` 200): 仕事専用SNS. 「プロフィールを埋めるだけで新しいビジネスチャンスに出会える」. Marketing line — **not** activity proof and **not** a traffic number.

**Recruiter scout** (`recruiter/faq/scout/` + `scout-vs-message/` 200): company-side 「スカウトルーム」 vs 「メッセージルーム」. 有料スカウト consumes 通数 (友達の友達 等). **Talent CU does not buy this.** Plan names (ライト / スタンダード / プレミアム) are recruiter copy. Amounts **not** on these pages → not invented.

**公式リクルーター** (`user/other/official-recruiter/` 200): 「有料プランをご契約の上、自社の採用活動を行っている企業の担当者」. **Do not buy.**

This is **not** the interview-agent `profile_only` of ITプロパートナーズ ([PR#97](https://github.com/rimone0511/autopilot-log/pull/97)): there is no official 「エージェント面談予約」 as the seller path. The talent action that converts is still an **outbound warm intro** (or waiting for inbound scout). CU may not send that intro.

---

## Logged-out API 401 (evidence)

Jobs HTML is a React shell (`#react-application`). No ISO / `2026-09` card dates in the HTML this GET.

| Request | HTTP | Body (full; no secrets) |
|---|---|---|
| `GET /api/recruitment_posts` | **401** | `{"error":"You need to sign in or sign up before continuing."}` |
| `GET /api/recruitment_posts.json` | **401** | same JSON |

`Content-Type: application/json; charset=utf-8`. Set-Cookie: **not** present on these two.  
This is a **login wall**, not a listing. It does **not** prove the jobs catalog is empty. It does **not** prove the catalog is fresh.

Also this GET (not used as listings):

| Request | HTTP | Note |
|---|---|---|
| `GET /recruitment_posts` | **200** | Title 副業・転職のジョブ（募集）一覧. Cards/dates **absent** from HTML |
| `GET /recruitment_posts.json` | **406** | `{"status":406,"error":"Not Acceptable"}` — not a listing |
| `GET /api/v1/recruitment_posts` | **404** | HTML ページが見つかりません. Wrong path |

Do **not** login to re-hit `/api/recruitment_posts` from this pack. A human may view **one job card date** in a browser later; that is the only way this GET knows to move `needs_check` → `pass`. Unreadable ≠ thin.

CSRF meta tags are present on `/lp`, `/sign_in`, `/recruitment_posts`. **Values not stored.**

---

## Activity-gate template (this GET)

```
日付（JST）: 2026-09-16
机: YOUTRUST
公式URL: https://youtrust.jp/
公開ページを見たか: yes（/lp, /sign_in, /recruitment_posts, help, GET /api/recruitment_posts）
ログインしたか: no
signup_open: yes-help / unknown-button（help: メール / Facebook / Google / LINE. /sign_in SPA — Google button not in static HTML. /signup 404）
fee_page: yes（poster side）. cost + how-to-post: ジョブは1つまで無料公開. manage-applicants: 1アカウント1件無料、掲載30日、複数同時は有料契約. Applicant % not on these pages — not invented
open_jobs_heuristic: unknown（list 200 SPA; API 401; card dates unread）
last_blog_news: not fetched
fit_still_ok: yes-help（副業・転職ジョブ. 転職専用とはヘルプ上書いていない）
1 生きている: yes
2 寄せ集めではない: yes（自前 SNS のジョブ、とヘルプ）
3 現地だけではない: unknown（カード未読）
4 本人専用ではない: yes
5 活動の目視: unknown
   見たもの: LP 200; jobs shell 200; API 401 sign-in required; help「ジョブは全てのユーザーに公開」
6 KYC: 出ていない
7 本線: yes（副業ジョブがある机、とヘルプ）
gate_result: needs_check
product_shape: warm_intro_scout
action: skip live CU this pass. If later human GO: profile draft only. Human may view one job card date before pass. Do not send 話を聞きたい. Do not post a job. Do not buy 公式リクルーター. SNS 実名連携 if demanded → record. KYC → stop.
公開したか: no
Google: help yes; button on /sign_in needs_check (SPA)
有料: official recruiter / extra simultaneous jobs = paid in help. Do not buy. Applicant % unread
SKIP thin: no
```

This GET **matches** PR#12 / PR#59 (`needs_check`). It does **not** upgrade to `pass`.

---

## CU profile-only vs skip (this GET only)

Question asked: is a **CU profile-only** pass worth it, or **skip**?

Two different skips. Do not mix them.

| Option | Meaning | This GET |
|---|---|---|
| **skip_log / thin / dead** | Desk is closed or not a seller line | **No.** `/lp` 200, jobs shell 200, help 200, robots 200 (`Sitemap: https://youtrust.jp/sitemap`). API **401 ≠ dead** |
| **skip_live_cu this pass** | Do not open a CU session now | **Yes.** Wave B register is **REGISTER-CU-CUT** ([PR#72](https://github.com/rimone0511/autopilot-log/pull/72) / [PR#94](https://github.com/rimone0511/autopilot-log/pull/94)). Prefer JOBS on desks that already have `draft_saved`. YOUTRUST conversion this GET is 「話を聞きたい」 or inbound scout — CU must not send the intro |
| **profile_only if later human GO** | Allowed later slice = profile **draft** | **Yes, as the cap — not as a reason to start now.** Help: fill profile before 「話を聞きたい」; inbound messages 「届きやすくなる」. That is qualitative help copy, **not** a measured inbound rate. Do not invent traffic |

**Verdict this folder**

1. **Activity gate:** keep **`needs_check`**. Human card-date view still required for `pass`.
2. **Live CU this pass:** **`skip_live_cu`**. Not next after Freelancer. Not a JOBS apply desk.
3. **Desk skip:** **do not** `skip_log`. `SKIP thin: no`.
4. **If a human later names this desk:** **`profile_only`**. Google (click-time) or MAIN mailbox per help. Draft profile. **Stop** before 「話を聞きたい」, つながりばらまき, ジョブ投稿, 公式リクルーター, Google連絡先一括, KYC.
5. **Worth it?** Evidence does **not** show a self-serve earn loop without the warm-intro send. Help **does** say a filled profile is the inbound hook. This GET cannot score that hook (would invent traffic). So: **park**. Profile-only is optional later presence, not a jobs-phase converter.

Do **not** treat LP 「プロフィールを埋めるだけ」 as proof that CU should run.

---

## Pointers (do not copy bodies)

| Sibling | What it is | Use |
|---|---|---|
| [PR#1 QUEUE B13](https://github.com/rimone0511/autopilot-log/pull/1) | Canonical WAVE letter | プロフィール下書き. SNS 実名連携 → 記録. KYC → 停止 |
| [PR#8 CU-24](https://github.com/rimone0511/autopilot-log/pull/8) | INDEX serial | `week-2` / `unknown`. Do not invent CU-29+ |
| [PR#12 `records/11-youtrust.md`](https://github.com/rimone0511/autopilot-log/pull/12) | JP Wave B gate | Same `needs_check` class (API 401, cards unread) |
| [PR#59 `records/b18-youtrust.md`](https://github.com/rimone0511/autopilot-log/pull/59) | GLOBAL-slice B18 label | Same GET class. This folder deepens shape + CU vs skip |
| [PR#30 `05-youtrust.md`](https://github.com/rimone0511/autopilot-log/pull/30) | Thick CU-24 paste | Paste **if** a later human GO. Bios **not** duplicated here |
| [PR#72](https://github.com/rimone0511/autopilot-log/pull/72) / [PR#94](https://github.com/rimone0511/autopilot-log/pull/94) | REGISTER-CU-CUT / jobs-first | Why live CU is skipped this pass |

## Early CU — forbidden even on a later GO

See [STOP.md](STOP.md). Short list: 「話を聞きたい」送信, ジョブ投稿 (無料枠でも), 公式リクルーター課金, Google連絡先インポート, つながりばらまき, KYC upload, `/signup`.

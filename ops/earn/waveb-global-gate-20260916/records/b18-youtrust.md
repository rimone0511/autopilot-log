# B18 — YOUTRUST

DRAFT_ONLY. No login. No signup. No paid subscribe. No secrets.

This-folder ID **B18** = QUEUE **B13** = INDEX **CU-24**.  
There is no QUEUE B18.

```
日付（JST）: 2026-09-16
机: YOUTRUST
公式URL: https://youtrust.jp/
公開ページを見たか: yes（LP、sign_in、jobs list URL、help）
ログインしたか: no
signup_open: yes-help / unknown-button（help.youtrust.jp/user/account/create/ HTTP 200 lists Googleアカウント連携. /sign_in HTTP 200 SPA — button not in static HTML. /signup HTTP 404）
fee_page: yes（poster side only）. how-to-post: ジョブは1投稿まで無料で公開可能. manage-applicants: 1アカウント1件まで無料、掲載30日、複数同時は有料契約. Applicant / 話を聞きたい fee % not on these pages — not invented
open_jobs_heuristic: unknown（/recruitment_posts HTTP 200 title 副業・転職のジョブ（募集）一覧; cards/dates not in HTML. GET /api/recruitment_posts 401 JSON sign-in required）
last_blog_news: not fetched
fit_still_ok: yes-help（副業・転職ジョブ. 転職専用とはヘルプ上書いていない）
1 生きている: yes
2 寄せ集めではない: yes（自前 SNS のジョブ、とヘルプ）
3 現地だけではない: unknown（カード未読）
4 本人専用ではない: yes
5 活動の目視: unknown
   見たもの: LP 200; jobs list shell 200; API 401; help「ジョブは全てのユーザーに公開」
6 KYC: 出ていない
7 本線: yes（副業ジョブがある机、とヘルプ）
gate_result: needs_check
action: human views one job card date before pass. Profile draft only later. Do not post a job (free slot is poster-side). Do not send 話を聞きたい. Do not buy 公式リクルーター. SNS 実名連携 if demanded → record. KYC → stop.
公開したか: no
Google: help yes; button on /sign_in needs_check
有料: official recruiter / extra simultaneous jobs = paid in help. Do not buy. Applicant % unread
SKIP thin: no
```

Sibling: PR#12 already scored YOUTRUST `needs_check` (API 401, cards unread). This GET matches that class of evidence; it does not upgrade to `pass`.

Sibling paste pack (not copied): PR#30 `05-youtrust.md`.

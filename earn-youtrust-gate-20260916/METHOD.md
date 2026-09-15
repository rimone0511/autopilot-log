# METHOD — public GET only (no marketplace login)

Datetime: **2026-09-15 21:07 UTC / 2026-09-16 06:07 JST**  
UA: ordinary desktop Chrome string. **No login cookies used. No OAuth. No account create. No POST.**

Did: GET official public URLs. Record HTTP status, `<title>` / JSON body, and help sentences that arrived in the body.  
Did not: marketplace login, Google OAuth, paid checkout, KYC, 「話を聞きたい」, job post, inventing job counts / GMV / applicant %, inventing scout 通数 prices.

Vendor marketing totals and LP 「プロフィールを埋めるだけ」 are **not** activity proof.  
401 on the jobs API is a **login wall**, not proof the catalog is dead or thin.  
CSRF tokens and Set-Cookie **values were not saved.** HTML pages under `youtrust.jp` had Set-Cookie **present** (values omitted). Help hosts and the 401 JSON responses did not set cookies this GET.

## App / API

| URL | HTTP | Memo |
|---|---|---|
| https://youtrust.jp/ | **302 → `/lp` 200** | Title `YOUTRUST｜仕事専用SNS`. React shell (`#react-application`) |
| https://youtrust.jp/lp | **200** | Same LP. Meta: 仕事専用SNS / つながり・メッセージ. Google **string** = GTM, not an OAuth button |
| https://youtrust.jp/sign_in | **200** | Title `ログイン｜YOUTRUST（ユートラスト）`. SPA shell. Google **button not in static HTML** |
| https://youtrust.jp/signup | **404** | Title `ページが見つかりません - YOUTRUST`. Not the register entry |
| https://youtrust.jp/recruitment_posts | **200** | Title `副業・転職のジョブ（募集）一覧｜YOUTRUST（ユートラスト）`. Meta names 「話を聞きたい」→カジュアル面談. **No card dates** in HTML (`2026-09` / ISO: none) |
| https://youtrust.jp/api/recruitment_posts | **401** | `Content-Type: application/json`. Body: `{"error":"You need to sign in or sign up before continuing."}` |
| https://youtrust.jp/api/recruitment_posts.json | **401** | Same JSON. Still not a listing |
| https://youtrust.jp/recruitment_posts.json | **406** | `{"status":406,"error":"Not Acceptable"}`. Not a listing |
| https://youtrust.jp/api/v1/recruitment_posts | **404** | HTML ページが見つかりません. Unused path |
| https://youtrust.jp/robots.txt | **200** | Body: `Sitemap: https://youtrust.jp/sitemap` |

## Help (user / recruiter copy)

| URL | HTTP | Memo |
|---|---|---|
| https://help.youtrust.jp/user/account/create/ | **200** | Mail / Facebook / **Google** / LINE. Gmail signup ≠ Google OAuth. hotmail/outlook / disposable blocked for mail path |
| https://help.youtrust.jp/user/message/search-jobs/ | **200** | ジョブは全てのユーザーに公開. Filter dims include カジュアル面談 or メンバー募集 |
| https://help.youtrust.jp/user/message/want-to-talk/ | **200** | Logged-out 「話を聞きたい」→ 新規登録 then notify. Logged-in → メッセージ送信. カジュアル面談 |
| https://help.youtrust.jp/user/message/casual-vs-interview/ | **200** | カジュアル面談 = 選考前の情報交換 |
| https://help.youtrust.jp/user/message/interview-step/ | **200** | 応募 → メッセージ → カジュアル面談 → 本面談 (応募詳細; not used) |
| https://help.youtrust.jp/user/post/how-to-post/ | **200** | ジョブは1投稿まで無料（**poster**）. 有料公式リクルーターは公開ジョブ無制限 |
| https://help.youtrust.jp/user/post/manage-applicants/ | **200** | 1アカウント1件無料、掲載30日. 「話を聞きたい」した人が応募者管理に出る |
| https://help.youtrust.jp/user/post/cost/ | **200** | ジョブは無料で1つまで公開. Extra = 有料契約 / 問合せ. No applicant % |
| https://help.youtrust.jp/user/other/official-recruiter/ | **200** | 公式リクルーター = 有料プランの採用担当. Do not buy |
| https://help.youtrust.jp/user/privacy/career-interest-visibility/ | **200** | 副業・転職意欲の非公開範囲 (同僚 / 指定企業 / ブロック / 非友達かつ非リクルーター) |
| https://help.youtrust.jp/user/connection/google-contacts-candidate/ | **200** | Google連絡先 → 「知り合いかも？」. **Do not import** from CU |
| https://help.youtrust.jp/recruiter/faq/scout/ | **200** | Recruiter scout index |
| https://help.youtrust.jp/recruiter/faq/scout/scout-vs-message/ | **200** | メッセージ vs 無料スカウト vs 有料スカウト（通数）. Recruiter-side. Amounts unread |

`https://help.youtrust.jp/users/post-paid-or-free` was **not** fetched this run (sibling PR#59: 404). Do not cite as live.

## Gate labels used in this folder

| Label | Meaning |
|---|---|
| `needs_check` | SPA / API 401 / missing dates. Do not guess `pass` or `thin` |
| `skip_live_cu` | Do not open CU this pass (jobs-first / conversion is warm intro) |
| `profile_only` | Later human GO cap: profile draft. Not skip-as-thin |
| `skip_log` / `thin` / `dead` | **Not used.** Evidence missing for those |

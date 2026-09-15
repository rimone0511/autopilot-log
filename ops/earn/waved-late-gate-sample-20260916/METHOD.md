# METHOD — public GET only

Stamp: **2026-09-16 JST**  
UA: ordinary desktop Chrome string. **No login cookies.** No POST. No OAuth.

Did: GET official public URLs (follow redirects unless noted). Read titles, visible copy, listing headings, help/news dates that appeared in HTML.

Did not: create accounts, complete Google login, buy plans, apply, book 面談, publish, store secrets, cookies, CSRF tokens, or Cloudflare Ray IDs.

Do not treat homepage marketing totals (members, “○件”, “プロ○名”) as activity proof.

Catalog: parent QUEUE `earn-register-expand-20260916/QUEUE.md`. D-late sample IDs follow the operator list D21 / D23 / D24 / D25 / D32. Sibling D11–D20 gate: [PR#20](https://github.com/rimone0511/autopilot-log/pull/20). This GET is independent; **the URL opened here is source of truth**.

## GET log (this IP)

| Desk | URL | HTTP | Note |
|---|---|---|---|
| D21 | https://shmatsu-worker.jp/ (and shu-matsu-worker.jp variants) | DNS fail | Wrong host. Unused |
| D21 | https://shuuumatu-worker.jp/ | 200 | Title シューマツワーカー \| エンジニア・デザイナーの副業・複業案件紹介. CTA 無料ではじめる. Flow: ヒアリング → エントリー → 企業と面談 |
| D21 | https://shuuumatu-worker.jp/signup | 200 | Title 新規会員登録. Facebook / GitHub / メールアドレス で登録. **No Google label** |
| D21 | https://shuuumatu-worker.jp/signup/email | 200 | Title メールアドレスで新規会員登録. Form not submitted |
| D21 | https://shuuumatu-worker.jp/login | 200 | Title ログイン. Facebook / GitHub / メール. 新規登録はこちら（無料） |
| D21 | https://shuuumatu-worker.jp/projects | 200 | Title 副業・複業求人・案件一覧. **更新日：2026-09-15**. NEW cards. Flow Step3 初回スタッフ面談 |
| D21 | https://shuuumatu-worker.jp/projects/18941 | 403 | Individual card blocked this IP. Not used as dead |
| D21 | https://shuuumatu-worker.jp/faq | 200 | コンシェルジュ / ほぼフルリモート / 報酬は稼動月の翌月末振込. Worker % **not** on FAQ |
| D21 | https://shuuumatu-worker.jp/about \| /fee \| /terms \| /news | 404 | Unused |
| D21 | https://freelancedays.shuuumatu-worker.jp/ | 200 | Title `freelancedays`. SPA shell only. FAQ points フリーランス向け here. Not signed up |
| D21 | https://company.shuuumatu-worker.jp/ | 200 | Corporate. Privacy `/privacy/` 200 |
| D23 | https://freelance.levtech.jp/ | 200 | Title 【公式】レバテックフリーランス. 「簡単30秒 / 無料登録」. ご利用の流れ ヒアリング → 商談. 個別相談会 nav |
| D23 | https://freelance.levtech.jp/member/input/chat/ | 200 | Title 無料サポート登録. Chat questionnaire. 「会員の方はこちらからログイン」. **Not submitted** |
| D23 | https://freelance.levtech.jp/consultation/detail/2/ | 200 | Title 【個別相談会】フリーランスになりたいと考えている方向け. 1時間. 経歴・希望ヒアリング |
| D23 | https://freelance.levtech.jp/project/aps-1/ | 200 | Title Tomcatのフリーランス求人・案件一覧. Public skill cards. Calendar dates unread |
| D23 | https://freelance.levtech.jp/service/ | 200 | Title サービス紹介. 「エージェントサービス」. コーディネーターがヒアリング |
| D23 | https://freelance.levtech.jp/guide/ | 200 | お役立ちコンテンツ hub |
| D23 | https://freelance.levtech.jp/login/ \| /signup/ \| /project/ | 404 | SPA fallback title = home. Dedicated paths unused |
| D23 | https://levtech.jp/ | 200 | Parent レバテック転職 LP. Not this freelance desk |
| D24 | https://geechs-job.com/ | 200 | Title ITフリーランスの案件・求人ならGEECHS JOB. 無料登録 / 独立相談会 |
| D24 | https://geechs-job.com/entry/ | 200 | Title 無料登録フォーム. 「ご記入いただいた内容をもとに、弊社担当よりご連絡」. **Not submitted** |
| D24 | https://geechs-job.com/project/ | 200 | Title 案件一覧. h3 skill cards (Java / AWS / TypeScript…). Listing ISO dates unread |
| D24 | https://geechs-job.com/project/java | 200 | Java 案件一覧 title. Same SPA pattern |
| D24 | https://geechs-job.com/guide | 200 | ご利用の流れ: エントリー → 個別説明会 → 案件紹介 → 商談 |
| D24 | https://geechs-job.com/faq/ | 200 | Q「案件紹介を受けると料金がかかりますか？」A **エントリー、案件紹介に至るまですべて無料** |
| D24 | https://geechs-job.com/news/ | 200 | お知らせ一覧. Home also listed **2026/08/18** event notice |
| D24 | https://geechs-job.com/news/4 | 200 | 2026年ゴールデンウィーク休業（5/2–5/6 コピー） |
| D24 | https://geechs-job.com/news/6 | 200 | 【ITエンジニア向けイベント開催情報】2026年8月22日 AI HACKATHON 2026 |
| D24 | https://geechs-job.com/event | 200 | 独立相談会「随時募集」. Not booked |
| D24 | https://geechs-job.com/about/ | 403 | CloudFront. Unused |
| D25 | https://mid-works.com/ | 200 | Title Midworks｜フリーランスエンジニア専門の案件・求人サイト. Nav 会員登録 / ログイン |
| D25 | https://mid-works.com/projects/ | 200 | Title 案件・求人情報一覧. Public NEW titles. Heading count unused |
| D25 | https://mid-works.com/about/ | 200 | Midworksとは. Flow 面談（1〜3回）→ 商談. 「IT系のフリーランスエンジニア専門のエージェントサービス」 |
| D25 | https://mid-works.com/users/registration | 200 | Title 無料会員登録. Email + reCAPTCHA (Google **privacy/terms** links, not OAuth). **Not submitted** |
| D25 | https://mid-works.com/user_policy | 200 | 利用規約. Branding Engineer. 最終改訂日：2018年3月24日. Worker % **not** on this page |
| D25 | https://mid-works.com/columns/ | 200 | お役立ちコラム hub. Per-post dates unread on index |
| D25 | https://mid-works.com/login \| /users/login \| /users/sign_in | 404 | Login URL unread. Nav still says ログイン |
| D25 | https://www.mid-works.com/ | 200 | Same site |
| D32 | https://www.circu.co.jp/ | 301 → 200 | → https://circu.co.jp/ |
| D32 | https://circu.co.jp/ | 200 | Title 株式会社サーキュレーション. News **2026.9.10**. Talent CTA via ProSharing |
| D32 | https://circu.co.jp/pro-sharing/ | 200 | 法人向けプロシェアリング. Flow: 課題ヒアリング → **プレ面談（スクリーニング）** → プロ人材との面談 |
| D32 | https://circu.co.jp/pro-sharing/professional/ | 200 | プロ人材向け. 無料登録はこちら → `pro.circu.info/register/basic`. Flow: ヒアリング → **企業との面談** |
| D32 | https://circu.co.jp/news/ | 200 | NEWS. **2026.9.10** 北海道新聞 / 札幌市IT受託 |
| D32 | https://circu.co.jp/news/20260910-6443/ | 200 | 北海道新聞掲載記事ページ |
| D32 | https://circu.co.jp/service/ | 200 | サービス一覧. 「対面での面談実施」copy. 法人問い合わせ / プロフェッショナル登録 |
| D32 | https://pro.circu.info/ | 200 → `/login` | Title 会員ログイン｜サーキュレーション PROポータル. Email / password. 新規登録はこちら |
| D32 | https://pro.circu.info/register/basic | 200 | Title プロ人材登録フォーム. 姓名 / 生年月日 / 所在地 / メール / 携帯 / 就労状況. **Not submitted**. No Google button |
| D32 | https://pro.circu.co.jp/ \| professional.circu.co.jp | DNS fail | Unused |
| D32 | https://probase.work/ | 200 | Title PROBASE｜副業/フリーランスとのやりとりを効率的に一元管理. **Client ops tool**. Not the talent desk |

Redirects recorded as 301 Location only. No cookies saved. CSRF `_token` on the Circulation register HTML was **not** stored.

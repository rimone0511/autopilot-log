# 観測メモ（方法だけ）

日時: 2026-09-16 JST  
UA: 通常のブラウザ相当。ログイン Cookie なし。

やったこと: 公式の公開 URL に GET。ヘルプ記事を読む。登録フォームの送信はしていない。OAuth を完走していない。

やらなかったこと: アカウント作成、有料、KYC、応募、出品公開、CV アップロード、資料請求フォームの送信。

10机の選び方: オペレーター指定の D11–D20。親 QUEUE の D1–D8 と Wave C LATE は含めない。D-late 行は QUEUE に無かったので足していない。

## 公開 GET の結果（要約）

| URL | HTTP | メモ |
|---|---|---|
| www.comet.co/ | 200 | Webflow LP。Last Published 2026-09-15 UTC（サイト公開日時。案件日ではない） |
| www.comet.co/fr および /fr/freelance /fr/missions | 404 | 「Notre ancien site a fermé ses portes」 |
| www.comet.co/freelance | 200（`/consultant` へ） | 「Nos dernières missions」はプレースホルダ文 |
| www.comet.co/contact | 200 | 「Déposer votre CV」「Rejoindre la communauté freelances」。送信していない |
| app.comet.co/ | 200 | 「votre espace personnel est clôturé」 |
| comet.crisp.help/.../onboarding | 402 | Helpdesk plugin inactive |
| replit.com/bounties | 301 → contra.com/replit 200 | タイトル「Hire Replit Experts for Your Web Project」 |
| replit.com/site/bounties | 同上 301 | 同上 |
| replit.com/experts | 404 | Replit 本体の 404 ページ |
| superpeer.com/ および www.superpeer.com/ | 301 → skillshare.com 403（このIP） | CF challenge |
| help.skillshare.com/.../Sunsetting-Superpeer... | 200（WebFetch） / 403（このIP curl） | sunset by December 31, 2024 |
| www.skillshare.com/teach | 200 | Skillshare 講師応募。Superpeer ではない。完走していない |
| weworkremotely.com/ および /remote-jobs | 403（このIP curl） | CF。Web 取得では求人ボード本文 |
| remoteok.com/ | 200 | 求人ボード。og:updated_time 2026-09-03 |
| remoteok.com/remote-freelance-jobs | 200（トップへ戻る） | 別の freelance 机は開かない |
| himalayas.app/ | 200 | Remote Job Board。Sign up with Google |
| himalayas.app/jobs | 403（このIP） | CF challenge |
| tech.coconala.com/ | 200 | エージェント LP。公開案件例 |
| tech.coconala.com/job-postings | 200 | NEW カード。件数見出しはマーケなので使わない |
| tech.coconala.com/signup | 404 | 登録は LP の `/#Registration` |
| freelance.findy-code.io/ | 200 | 案件例。「Googleで登録し案件を探す」 |
| freelance.findy-code.io/jobs および /signup | 404 | 入口はトップ |
| imitsu.jp/ | 200 | 発注者向け一括見積。2023-09-01 改名コピー |
| imitsu.jp/partner | 404 | 404 ページ自体に「PRONIアイミツに掲載する」 |
| partner.imitsu.jp/ | 200 | タイトル「パートナー向け（受注企業）サイト」。本文は SPA 空 |
| hikaku-biz.com/ | 200 | 会計ソフトの記事サイト。最新記事表示 2024-11-29。机が違う |
| www.biz.ne.jp/ | 200 | 比較ビズ本機。見積依頼カード |
| www.biz.ne.jp/seller/ | 200 | 受注者は掲載・資料請求 |
| www.biz.ne.jp/subject/ | 200 | 公開の見積依頼例 |

署名付き URL、Cookie、CSRF、Ray ID は保存していない。

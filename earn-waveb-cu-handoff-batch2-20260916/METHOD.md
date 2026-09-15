> **MAIN Google only.** Public GET does not log in. No OAuth completion.
> **DRAFT_ONLY.** These rows are URL confirmation, not accounts.
> **STOP-KYC.** No identity pages were submitted.
> **No secrets.** Response bodies were not saved as cookies or tokens.
> **No invented fees.** HTTP codes and visible headings only. Marketing totals are not activity proof.
> **No publish.** No forms were posted.

# 観測メモ（方法だけ）

日時: 2026-09-16  
UA: 通常のブラウザ相当。ログイン Cookie なし。  
やったこと: 公式の公開 URL に GET。HTML に出た見出し・リンク・FAQ だけ記録。  
やらなかったこと: アカウント作成、OAuth 完走、有料、KYC、応募、出品、企業コンソール。

件数・「○万人」・ホームページのマーケ％は活動証明に使わない。

| URL | HTTP | メモ |
|---|---|---|
| https://goworkship.com/ | 200 | タイトル「フリーランス・副業向けマッチングサービス」。案件カードへのリンクあり |
| https://goworkship.com/signup | 200 | タイトル「フリーランス登録をする」。見出し「SNSで登録」。FirebaseUI コンテナ。Google ラベルは静的HTMLに未描画 |
| https://goworkship.com/help/how_to/44 | 200 | 「アカウントを新規登録したい」。SNSのアイコン。確認メール24時間 |
| https://goworkship.com/flow | 200 | お仕事開始までの流れ。プロフィール案内 |
| https://goworkship.com/portal/search | 200 | 活動ゲート（PR#12）の pass 根拠。このGETでも200 |
| https://goworkship.com/help/agreement/95 | 200 | 前払いオプション。**本人確認が必要**。手数料％は「確認の上」とだけ。数字なし |
| https://goworkship.com/help/agreement/105 | 200 | 三者間契約。成約報告のあと |
| https://start.crowdlinks.jp/ | 200 | マーケLP。`crowdlinks.jp/` はここへリダイレクト |
| https://crowdlinks.jp/worker/signup/ | 200 | タイトル「新規登録【クラウドリンクス】」。Next シェル。ボタン未描画 |
| https://crowdlinks.jp/worker/login/ | 200 | ワーカーログイン・シェル |
| https://help.crowdlinks.jp/ | 200 | ユーザー向けFAQ更新 **2026/8/1 13:50**（ページ見出し） |
| https://help.crowdlinks.jp/0029649d31534622a6d95ffe53df18dd | 200 | Google認証 / 変更不可。ワーカー利用は「すべて無料」（企業から利用料）。報酬額から手数料は引かれない、とFAQ |
| https://crowdlinks.jp/terms | 200 | 無料会員 / 有料会員。無料会員条件に実務経験 **2年以上**、満18歳、学生でないこと |
| https://itpropartners.com/ | 200 | フリーランス専門エージェント |
| https://itpropartners.com/register | 200 | 職種選択（エンジニア…）。Google ボタンなし |
| https://itpropartners.com/register/step1/pre | 200 | 同上 |
| https://itpropartners.com/login | 200 | 「facebookログインの提供は終了」。メール／パスワード。Google なし |
| https://itpropartners.com/signup | 200 | 案件一覧シェル（登録フォームではない）。`/signup` を入口にしない |
| https://itpropartners.com/blog/flow-itpropartners/ | 200 | 登録・利用は無料。流れは登録→面談→推薦→契約 |
| https://itpropartners.com/job/sale-4 | 200 | 最終更新日 **2026/09/08** のカード例あり（PR#12 と同じ手がかり） |
| https://itpropartners.com/terms | 200 | この環境では案件シェルが返り本文が薄い。手数料％は未取得 → `needs_check` |
| https://offers.jp/ | 200 | トップは転職コピー。ヘッダに `/worker/signup` |
| https://offers.jp/worker/signup | 200 | **「Google で登録する」** 可視。`/oauth/worker_signup/google`。GitHub / X / LinkedIn / メールも |
| https://offers.jp/jobs/engineer/side-job | 200 | 業務委託カード。例: 更新日 **2026-09-10**「【フルリモート】AI×FDE」。時給レンジは **案件カードでありプロフィール単価にコピーしない** |
| https://offers.jp/terms | 200 | マッチング成功報酬は **クライアントが** 当社指定の手数料を払う。％は未記載 |
| https://offers.jp/signup | 404 | 入口は `/worker/signup` |
| https://youtrust.jp/ | 200 | `/lp` へリダイレクト。SPA |
| https://youtrust.jp/sign_in | 200 | ログイン／新規の公式入口。静的HTMLはシェル。ヘルプが Google / Facebook / LINE / メールを列挙 |
| https://youtrust.jp/signup | 404 | 使わない |
| https://youtrust.jp/recruitment_posts | 200 | タイトル「副業・転職のジョブ（募集）一覧」。カード本文はSPA |
| https://help.youtrust.jp/user/account/create/ | 200 | Googleアカウント連携の公式手順。メール登録と Google 連携は別 |
| https://help.youtrust.jp/user/message/search-jobs/ | 200 | ジョブ検索ヘルプ。応募は「話を聞きたい」（このパックでは送らない） |

`/api/recruitment_posts` は PR#12 で未ログイン 401。このバッチでは再ログイン相当のAPIは叩いていない（公開HTMLの確認に限定）。

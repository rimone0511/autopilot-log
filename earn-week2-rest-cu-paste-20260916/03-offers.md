> DRAFT-ONLY paste pack. NO secrets. NO browser signup. NO publish.
> Human paste only. Agent does not create accounts.
> `thin_site_skip: false` unless public evidence shows the product is dead.
> Stop at KYC: do not upload ID, My Number, bank, Stripe identity, or e-sign identity contracts.

# CU-25 PACK — Offers

| キー | 値 |
|---|---|
| cu_serial | CU-25（QUEUE B14） |
| inventory | 03 |
| activity_gate | **pass**（PR#12。Jobs 業務委託カード） |
| official | https://offers.jp/ |
| signup | https://offers.jp/worker/signup |
| login | https://offers.jp/worker/login |
| jobs_side | https://offers.jp/jobs/engineer/side-job |
| jobs | https://offers.jp/jobs |
| terms | https://offers.jp/terms |
| privacy | https://offers.jp/privacypolicy |
| google_oauth | https://offers.jp/oauth/worker_signup/google |
| google_signup_preference | **PREFER_GOOGLE** |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP** |
| draft | true |
| observed | 2026-09-16 JST 公開 GET |

## Google signup preference

公開登録面の文言: 「Google で登録する」。リンク `/oauth/worker_signup/google`。

他の SNS: GitHub / X / LinkedIn もある。**MAIN Google を優先**。GitHub は公開リポジトリと一致するなら次点。X / LinkedIn をこの仕事のためだけに新規作成しない。

フォールバック: 「メールアドレスで登録する」→ `{{EMAIL}}`。

企業側 `/client/` は使わない。人材（worker）だけ。

## 転職導線について

トップは「AI時代のハイクラスエンジニア**転職**」。QUEUE の「転職導線だけならゲート再判定」は、Jobs を見て判定する。

公開 `https://offers.jp/jobs/engineer/side-job` に業務委託カードがある。例（見出しのみ）:

- 「【フルリモート】AI×FDE｜事業課題を解くフルスタックエンジニア募集」更新日 **2026-09-10**
- 「【フルリモート／業務委託】AI×新規事業を牽引するシニアエンジニア募集」

利用規約第3条もマッチング対象に「業務を引き受け」と「求職」の両方を書く。転職だけではない。応募はしない。

マーケの「登録ユーザー数 35,000」等は活動証明に使わない。

## Field map（プレースホルダ）

登録初面は OAuth。以降の項目はライブフォームを正とする。

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | Google | 必須 | PREFER_GOOGLE |
| メール | `{{EMAIL}}` | Googleから来る | |
| 氏名 | `{{LEGAL_NAME_KANJI}}` | 高 | |
| 表示名 | `{{DISPLAY_NAME}}` | 高 | |
| 生年月日 | `{{BIRTH_YEAR}}-{{BIRTH_MONTH}}-{{BIRTH_DAY}}` | 任意〜高 | |
| 居住地 | `{{PREFECTURE}}` `{{CITY}}` | 高 | |
| 電話 | `{{PHONE}}` | 高 | SMS OTP はユーザーチャット待ち。推測しない |
| 職種 | エンジニア / 業務自動化 の最寄り | 高 | |
| スキル | Claude Code, n8n, Python, 公式API連携, 運用ドキュメント | 高 | 未経験を書かない |
| 希望の働き方 | 業務委託・副業・リモート | 高 | 転職専願にしない |
| 自己紹介 | 下記 200 / 800 | 高 | |
| ポートフォリオ | `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}` | 任意 | |
| GitHub 連携 | 任意 | 任意 | 公開リポジトリと一致するときだけ |

共通プレースホルダは [INDEX.md](INDEX.md)。

## JA bio 200（200字）

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIによる業務自動化の手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIだけを使う動画アップロード道具も公開中です。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。公開は人が決めます。秘密は貼りません。根拠を残す方針です。
```

## JA bio 800（800字）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIを使って毎日の作業を自動化する手順、つまずいた点、確認できた結果を、むずかしい言葉を避けて公開しています。売り物は「動いたように見える自動化」ではなく、人が検品できる仕組みです。公開している実録と道具を、業務委託の成果物の根拠にします。提供できること：（1）繰り返し作業の自動化設計。目的・範囲・合格条件・停止条件を先に切り、実装後に回帰確認まで残します。（2）Claude CodeやCodexなど、AIに実装を任せるときの指示の書き方、検品、失敗時の切り分け。（3）YouTubeとTikTokへの公式API投稿の仕組みづくり。ブラウザ自動操作とスクレイピングは対象外です。（4）鍵の扱い、公開事故、トークン期限など、自動化が止まりやすい箇所の点検。公開している道具の例：Autopilot Log（https://github.com/rimone0511/autopilot-log）。YouTube Data API v3 と TikTok Content Posting API のみを使い、投稿の門番は壊れても非公開側に倒れます。受けないこと：いいねやフォローの自動化、権利のない投稿代行、本人確認書類・口座・マイナンバーの代理入力、未確認のままの公開。進め方はテキスト中心です。根拠と反証を残し、公開スイッチは依頼者または本人の手に置きます。リモート可。週次の稼働時間は案件ごとに相談します。未確認の件数や年数は書きません。確認できた公開物だけを貼ります。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。英語の一次資料は必要なら要約して渡します。契約前に範囲外を一文で確定します。納期は着手前に合意します。作業の記録を残す。
```

## STOP-AT-KYC

ここまでやってよい: Google 登録、プロフィール下書き。

ここで止める:

- 求人・業務委託への応募、カジュアル面談の申込
- 身分証・職務経歴書の必須アップロード（任意なら後回し）
- 有料ブース・優先表示
- クライアント（発注者）登録
- 規約のシステム利用料・成功報酬は **クライアント側** の条項。売り手が課金画面に入ったら止める。数字は再確認するまで書かない

## thin_site_skip

false。2026-09-16 に worker signup 200、「Google で登録する」あり。side-job 一覧に業務委託カードと更新日 **2026-09-10**。

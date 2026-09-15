> DRAFT-ONLY paste pack. NO secrets. NO browser signup. NO publish.
> Human paste only. Agent does not create accounts.
> `thin_site_skip: false` unless public evidence shows the product is dead.
> Stop at KYC: do not upload ID, My Number, bank, Stripe identity, or e-sign identity contracts.

# CU-28 PACK — ITプロパートナーズ

| キー | 値 |
|---|---|
| cu_serial | CU-28（QUEUE B17） |
| inventory | 06 |
| activity_gate | **pass**（PR#12） |
| official | https://itpropartners.com/ |
| signup | https://itpropartners.com/register |
| login | https://itpropartners.com/login |
| jobs_sample | https://itpropartners.com/job/sale-4 |
| privacy | https://www.hajimari.inc/pii |
| company_policy | https://hajimari.inc/policy |
| terms | トップの「利用規約」はモーダル（`openTermsOfServiceModal()`）。`/terms` は 200 だが本文は「お探しのページは見つかりませんでした」 |
| google_signup_preference | **NOT_OFFERED_OAUTH** |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP** |
| draft | true |
| observed | 2026-09-16 JST 公開 GET |

## Google signup preference

`/register` 初面は「あなたの職種を教えてください」。職種カード: エンジニア / マーケター / デザイナー / 事業責任者・プロデューサー / 人事・総務 / 経理・財務 / 広報・PR / 営業・コンサルタント / ディレクター / 経営者・CXO。

公開 HTML に Google で登録するボタンは無い（Tag Manager のみ）。`/signup` `/entry` は PR#12 どおり 404。

経路: 職種 **エンジニア** を選んだあと、メールフォーム（`{{EMAIL}}`）。パスワード欄が出たら `{{PASSWORD_DO_NOT_STORE}}`。ライブフォームを正とする。

トップコピー「まずは、Emailで無料登録」と一致する。

## エージェント型

自前の業務委託カードがある（寄せ集め専用ではない）。紹介・面談は **朝の本人**。エージェントが面談を完走しない。身分証が乗ったら STOP。

マーケの「8,000件以上」「9割が直案件」は活動証明に使わない。

## Field map（プレースホルダ）

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 職種 | エンジニア | 必須 | 初面。複数なら最も比重の高いもの |
| メール | `{{EMAIL}}` | 必須 | Email 無料登録 |
| 氏名 | `{{LEGAL_NAME_KANJI}}` | 高 | |
| 氏名カナ | `{{LEGAL_NAME_KANA}}` | 高 | |
| 電話 | `{{PHONE}}` | 高 | SMS OTP はチャット待ち |
| 生年月日 | `{{BIRTH_YEAR}}-{{BIRTH_MONTH}}-{{BIRTH_DAY}}` | 高 | |
| 居住地 | `{{PREFECTURE}}` `{{CITY}}` | 高 | |
| スキル | Python, n8n, 業務自動化, API 連携, ドキュメント | 高 | 未経験を書かない |
| 希望稼働 | リモート可。週次は要相談 | 高 | トップは「週2日から」。数字を捏造して週2固定と書かない |
| 自己紹介 | 下記 200 / 800 | 高 | |
| ポートフォリオ | `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}` | 任意 | |
| 履歴書・職務経歴書 | 出さない | — | 必須と言われたら STOP（KYC/書類） |

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

ここまでやってよい: 無料登録、プロフィール下書き。

ここで止める:

- 案件詳細の「気になる」「詳細を確認」からの応募
- 専属エージェント面談で身分証・マイナンバー・口座が出たとき
- 契約書の電子サインで本人確認が乗ったとき
- 週5常駐のみのカードへの手挙げ（リモート行はある。例: 最終更新日 **2026/09/08**「コーポレートIT／社内情報システム」基本リモート一部出社、**2026/09/05**「M&A事業部…アポ獲得」フルリモート）

## thin_site_skip

false。2026-09-16 にトップ 200、`/register` 200、`/job/sale-4` に最終更新日 **2026/09/08** ほかの業務委託カード。

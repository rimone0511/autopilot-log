> **MAIN Google only.** Public register has **no Google button**. Use MAIN Google **mailbox** as `{{EMAIL}}`. Do not create Facebook (login ended) or a desk-only address.
> **DRAFT_ONLY.** 職種選択〜プロフィール入力まで。応募しない。エージェント面談に出ない。
> **STOP-KYC.** 面談・契約で身分証 / NDA署名の本人確認が出たら上げない。See [STOP-KYC.md](STOP-KYC.md).
> **No secrets.** パスワード設定リンクの中身を git に書かない。
> **No invented fees.** 公式ブログ: 登録・利用は無料。**仲介マージン％は公式に数字なし → 作らない**（第三者の10〜25%を貼らない）。
> **No publish.** Agent desk. このPRでは登録していない。

# CU-28 PACK — ITプロパートナーズ

| キー | 値 |
|---|---|
| inventory | 03 |
| cu_serial | CU-28（本番 INDEX B17。このフォルダの貼る順では 2番＝pass） |
| activity_gate | **pass**（PR#12。公開カードの最終更新日 2026/09/08 など。このGETでも `/job/sale-4` に同日表示） |
| self_serve | **partial**（Web登録は開いている。その後はエージェント面談。CUは面談しない） |
| cu_ready | **true**（パックあり。登録済みではない） |
| official | https://itpropartners.com/ |
| signup | https://itpropartners.com/register （職種選択。`/signup` は案件シェルなので入口にしない） |
| login | https://itpropartners.com/login |
| flow | https://itpropartners.com/blog/flow-itpropartners/ |
| jobs_example | https://itpropartners.com/job/sale-4 |
| google_signup_preference | **NOT_OFFERED_OAUTH** → Google mailbox + メール登録 |
| worker_fee_public | 公式ブログ「ご登録やサービスのご利用は無料」。マージン％ **needs_check**（公式HTMLに数字なし） |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP** |
| draft | true |
| observed | 2026-09-16 公開 GET |

## needs_check

- 仲介マージン％: 公式の公開ページに数字なし。推測しない。
- `/terms` はこの環境で案件シェルが返り、規約本文が薄い。貼る直前に画面で規約を開く。
- 登録後の「担当者からご連絡」は営業。CUは電話に出ない。朝メモだけ。

## CU handoff（この机）

やってよい（下書きのみ・後続CU）:

1. https://itpropartners.com/register で職種 **エンジニア**（最寄り。AIだけにしない）
2. メールは `{{EMAIL}}`（MAIN Google）。パスワードはファイルに書かない。ログイン面は Facebook 終了・メール経路
3. スキル・稼働・自己紹介を Field map どおり。**下書き／入力まで**
4. 「登録を完了する」がアカウント作成になる画面でも、このPRの著者は押していない。後続CUは人間OTP経路があるときだけ。完了後も **応募しない・面談しない**

使わない: `/signup` を登録入口にする。企業向けの採用担当導線。

## Field map（プレースホルダ）

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 職種（初面） | エンジニア | 必須 | 公開面の選択肢 |
| メール | `{{EMAIL}}` | 必須 | MAIN Google メール。OAuthなし |
| パスワード | 書かない | メール経路 | ログインはパスワード設定リンク（公式ログイン文） |
| 氏名 | `{{LEGAL_NAME_KANJI}}` `{{LEGAL_NAME_KANA}}` | 高 | |
| 電話 | `{{PHONE}}` | 高 | SMS待ちなら park |
| 生年月日 | `{{BIRTH_YEAR}}-{{BIRTH_MONTH}}-{{BIRTH_DAY}}` | 高 | |
| 居住地 | `{{PREFECTURE}}` `{{CITY}}` | 高 | |
| メイン職種 / スキル | Python, API, 業務自動化, Claude Code, Codex, 技術執筆 | 高 | 画面のスキルタグから最寄り。未経験を経験と書かない |
| 勤務状況 | フリーランス / 複業の画面値 | 高 | |
| 稼働日数 | リモート可。週次は要相談 | 高 | 数字の創作禁止 |
| 希望開始 | 要相談 | 任意 | |
| 希望単価 | `{{HOURLY_YEN_DRAFT}}` / `{{PRICE_YEN_DRAFT}}` | 任意 | 空。案件カードの月額をプロフィールにコピーしない |
| 自己紹介 | 下記 200 / 800 | 高 | |
| ポートフォリオ | `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}` | 高 | |
| 個人情報・規約 | 本人が読む | 必須 | エージェントは同意クリックしない（後続CUは人が読む） |

共通プレースホルダは [README.md](README.md)。

## JA bio 200（200字）

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIによる業務自動化の手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIだけを使う動画アップロード道具も公開中です。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。公開は人が決めます。秘密は貼りません。根拠を残す方針です。
```

## JA bio 800（800字）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIを使って毎日の作業を自動化する手順、つまずいた点、確認できた結果を、むずかしい言葉を避けて公開しています。売り物は「動いたように見える自動化」ではなく、人が検品できる仕組みです。公開している実録と道具を、業務委託の成果物の根拠にします。提供できること：（1）繰り返し作業の自動化設計。目的・範囲・合格条件・停止条件を先に切り、実装後に回帰確認まで残します。（2）Claude CodeやCodexなど、AIに実装を任せるときの指示の書き方、検品、失敗時の切り分け。（3）YouTubeとTikTokへの公式API投稿の仕組みづくり。ブラウザ自動操作とスクレイピングは対象外です。（4）鍵の扱い、公開事故、トークン期限など、自動化が止まりやすい箇所の点検。公開している道具の例：Autopilot Log（https://github.com/rimone0511/autopilot-log）。YouTube Data API v3 と TikTok Content Posting API のみを使い、投稿の門番は壊れても非公開側に倒れます。受けないこと：いいねやフォローの自動化、権利のない投稿代行、本人確認書類・口座・マイナンバーの代理入力、未確認のままの公開。進め方はテキスト中心です。根拠と反証を残し、公開スイッチは依頼者または本人の手に置きます。リモート可。週次の稼働時間は案件ごとに相談します。未確認の件数や年数は書きません。確認できた公開物だけを貼ります。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。英語の一次資料は必要なら要約して渡します。契約前に範囲外を一文で確定します。納期は着手前に合意します。作業の記録を残す。
```

## STOP-AT-KYC

ここまでやってよい: 職種選択、メール（MAIN Google）、スキル、自己紹介、公開URL。入力の保存。

ここで止める:

- エージェント面談（公式フロー②）。身分証が乗ったら即停止
- 企業面談の日程調整をCUが確定すること
- 個別契約書・NDA の代行署名
- 口座・マイナンバー
- 案件カードからの応募

面談は本人。パック完了は「下書き入力まで」または `kyc_wait`。

## thin_site_skip

false。2026-09-16 に `/register` が HTTP 200。職種選択が見える。公開案件カードに 2026/09/08 の最終更新日。

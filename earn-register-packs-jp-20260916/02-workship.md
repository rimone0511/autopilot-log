> DRAFT-ONLY paste pack. NO secrets. NO browser signup. NO publish.
> Human paste only. Agent does not create accounts.
> `thin_site_skip: false` unless public evidence shows the product is dead.
> Stop at KYC: do not upload ID, My Number, bank, Stripe identity, or e-sign identity contracts.

# CU-11 PACK — Workship（ワークシップ）

| キー | 値 |
|---|---|
| cu_serial | CU-11 |
| inventory | 02 |
| official | https://goworkship.com/ |
| signup | https://goworkship.com/signup |
| help_signup | https://goworkship.com/help/how_to/44 |
| flow | https://goworkship.com/flow |
| google_signup_preference | **PREFER_GOOGLE**（SNSアイコン。貼る人が Google ラベルを目視） |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP** |
| age_gate | 公開解説: 18歳未満は登録不可 |
| draft | true |

## Google signup preference

優先: 登録ページ「SNSで登録」の **Google**。公式ヘルプは「SNSのアイコン」。第三者解説（2025）は Google 可と明記。

貼る直前: アイコンに Google と書いてあることだけ確認する。無ければメール登録に倒す。メールは `{{EMAIL}}`。

招待コード `{{INVITE_CODE}}` は空でよい。reCAPTCHA は人が解く。エージェントは解かない。

## Field map（プレースホルダ）

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| SNS / Google | Googleアカウント `{{EMAIL}}` | 優先 | |
| メール | `{{EMAIL}}` | メール経路なら必須 | 確認URLは24時間 |
| パスワード | メール経路のみ。このファイルに書かない | メール経路 | ローカル台帳 |
| 招待コード | `{{INVITE_CODE}}` | 任意 | 空 |
| 利用規約同意 | 本人が読む | 必須 | エージェントは同意しない |
| 生年月日 | `{{BIRTH_YEAR}}-{{BIRTH_MONTH}}-{{BIRTH_DAY}}` | 高 | 18歳未満不可 |
| 職種 | エンジニア / 業務自動化 / ディレクター系の最寄り | 高 | |
| 働き方 | フリーランスまたは複業の画面値 | 高 | 本業の就業規則は本人判断 |
| 自己紹介 | 下記 200 / 800 | 高 | https://goworkship.com/flow が自己紹介・職歴・ポートフォリオを案内 |
| 職歴 | 公開実録の範囲のみ | 高 | 年数創作禁止 |
| スキル | Claude Code, Codex, Python, API連携, 業務自動化, 技術記事 | 高 | |
| ポートフォリオ | `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}` | 高 | |
| 希望単価 | 空または「要相談」 | 任意 | 未確認の時給を書かない |
| 顔写真 | `{{PHOTO_LOCAL_PATH}}` | 任意 | コミット禁止 |

公式ヘルプ: 成約後に機密保持契約と三者間の準委任契約。これは登録KYCではないが、**署名画面に本人確認が乗ったら止める**。


共通プレースホルダ（実値はローカルの本人台帳だけ。このリポジトリには書かない）:

- `{{LEGAL_NAME_KANJI}}` 戸籍上の氏名（漢字）
- `{{LEGAL_NAME_KANA}}` 氏名カナ
- `{{DISPLAY_NAME}}` 表示名。推奨: `石田祐太`
- `{{EMAIL}}` Googleメール（ログイン用）
- `{{PHONE}}` 日本の携帯電話
- `{{POSTAL_CODE}}` 郵便番号
- `{{PREFECTURE}}` 都道府県
- `{{CITY}}` 市区町村以下
- `{{BIRTH_YEAR}}` / `{{BIRTH_MONTH}}` / `{{BIRTH_DAY}}` 生年月日
- `{{PORTFOLIO_URL}}` 推奨公開: `https://yutalab.dev/`
- `{{GITHUB_URL}}` 推奨公開: `https://github.com/rimone0511`
- `{{GITHUB_REPO_AUTOPILOT}}` `https://github.com/rimone0511/autopilot-log`
- `{{PHOTO_LOCAL_PATH}}` 顔写真のローカルパス（コミット禁止）
- `{{INVITE_CODE}}` 招待コード。無ければ空


## JA bio 200（200字）

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIによる業務自動化の手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIだけを使う動画アップロード道具も公開中です。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。公開は人が決めます。秘密は貼りません。根拠を残す方針です。
```

## JA bio 800（800字）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIを使って毎日の作業を自動化する手順、つまずいた点、確認できた結果を、むずかしい言葉を避けて公開しています。売り物は「動いたように見える自動化」ではなく、人が検品できる仕組みです。公開している実録と道具を、業務委託の成果物の根拠にします。提供できること：（1）繰り返し作業の自動化設計。目的・範囲・合格条件・停止条件を先に切り、実装後に回帰確認まで残します。（2）Claude CodeやCodexなど、AIに実装を任せるときの指示の書き方、検品、失敗時の切り分け。（3）YouTubeとTikTokへの公式API投稿の仕組みづくり。ブラウザ自動操作とスクレイピングは対象外です。（4）鍵の扱い、公開事故、トークン期限など、自動化が止まりやすい箇所の点検。公開している道具の例：Autopilot Log（https://github.com/rimone0511/autopilot-log）。YouTube Data API v3 と TikTok Content Posting API のみを使い、投稿の門番は壊れても非公開側に倒れます。受けないこと：いいねやフォローの自動化、権利のない投稿代行、本人確認書類・口座・マイナンバーの代理入力、未確認のままの公開。進め方はテキスト中心です。根拠と反証を残し、公開スイッチは依頼者または本人の手に置きます。リモート可。週次の稼働時間は案件ごとに相談します。未確認の件数や年数は書きません。確認できた公開物だけを貼ります。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。英語の一次資料は必要なら要約して渡します。契約前に範囲外を一文で確定します。納期は着手前に合意します。作業の記録を残す。
```

## STOP-AT-KYC

ここまでやってよい: SNS登録、メール確認、プロフィール、職歴、スキル、ポートフォリオURL。

ここで止める:

- 契約管理の署名で身分証や印鑑証明を求められたとき
- 口座・振込先
- マイナンバー
- 成約報告の先の本人確認

お祝い金や成約フローは、KYCが出た時点でパック完了。

## thin_site_skip

false。2026-09-15 に https://goworkship.com/signup が HTTP 200。公式ヘルプがアカウント作成手順を掲載。

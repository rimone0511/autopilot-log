> DRAFT-ONLY paste pack. NO secrets. NO browser signup. NO publish.
> Human paste only. Agent does not create accounts.
> `thin_site_skip: false` unless public evidence shows the product is dead.
> Stop at KYC: do not upload ID, My Number, bank, Stripe identity, or e-sign identity contracts.

# CU-14 PACK — CrowdLinks / クラウドリンクス

| キー | 値 |
|---|---|
| cu_serial | CU-14 |
| inventory | 04 |
| marketing | https://start.crowdlinks.jp （crowdlinks.jp トップから遷移） |
| worker_signup | https://crowdlinks.jp/worker/signup/ |
| worker_login | https://crowdlinks.jp/worker/login/ |
| help | https://help.crowdlinks.jp/ |
| terms | https://crowdlinks.jp/terms |
| google_signup_preference | **PREFER_GOOGLE** |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP** |
| tos_note | 無料会員条件に「プロフィール上の業務について実務経験が2年以上」とある。未確認なら経験年数を盛らない。該当しないと判断したらこのパックは登録しない |
| draft | true |

## Google signup preference

優先: 「Googleでログイン / 新規登録」。公式: Google または Facebook で新規登録するとパスワードは未設定。以後も同じGoogle。Googleアカウントの付け替えは不可とヘルプにある。

フォールバック: メール。パスワードは英数字と指定記号を含む8文字以上（ヘルプ）。パスワードはファイルに書かない。

## Field map（プレースホルダ）

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | Google | 必須 | 変更できないので初回を間違えない |
| 氏名 | `{{LEGAL_NAME_KANJI}}` | 推奨 | ヘルプ: 本名必須ではないが推奨 |
| 生年月日 | `{{BIRTH_YEAR}}-{{BIRTH_MONTH}}-{{BIRTH_DAY}}` | 高 | 第三者解説が登録時の名前・生年月日に言及 |
| 連絡用メール | `{{EMAIL}}` | 高 | ログイン用と連絡用が分かれうる。両方 Googleメールで揃える |
| 経歴 | 1件以上必須（ヘルプ） | 必須 | 公開実録の範囲。2年条件は本人判断 |
| スキル | 業務自動化, API, Python, Claude Code, Codex, 技術執筆 | 高 | |
| キャリア概要 | 下記 200 | 高 | |
| 自己紹介 | 下記 800 | 高 | |
| ポートフォリオ | `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}` | 高 | |
| 稼働可能時間 | リモート、週次は要相談 | 任意 | |
| プロフィール公開範囲 | クラウドリンクス内公開 | 任意 | 一般公開は後回し |


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

ここまでやってよい: Google登録、経歴1件、スキル、概要、公開範囲。

ここで止める:

- 有料会員化
- 規約が言う追加書類
- 口座・本人確認
- 企業との直接契約で身分証を求められたとき

CrowdLinks は契約・報酬が企業と直接（公式FAQ）。プラットフォーム外のKYCも STOP。

## thin_site_skip

false。2026-09-15 に worker signup が HTTP 200。ヘルプFAQ更新 2026-08-01。トップが Studio の LP に飛ぶのは死滅ではなくマーケ導線。

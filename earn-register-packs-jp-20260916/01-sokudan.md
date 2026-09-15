> DRAFT-ONLY paste pack. NO secrets. NO browser signup. NO publish.
> Human paste only. Agent does not create accounts.
> `thin_site_skip: false` unless public evidence shows the product is dead.
> Stop at KYC: do not upload ID, My Number, bank, Stripe identity, or e-sign identity contracts.

# CU-13 PACK — SOKUDAN（ソクダン）

| キー | 値 |
|---|---|
| cu_serial | CU-13（直列は INDEX を正とする） |
| inventory | 01 |
| official | https://sokudan.work/ |
| signup | https://sokudan.work/signup/pro |
| login | https://sokudan.work/login |
| terms | https://sokudan.work/pages/terms |
| operator | 公開ページ上のマッチングサービス。フリーランス・副業向け登録面あり |
| google_signup_preference | **PREFER_GOOGLE** |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP** |
| draft | true |

## Google signup preference

優先: 新規登録面の「Google」連携（ログイン面表記: Google でログイン。登録面は Facebook 無料登録に加え Google の `/users/auth/google?category=signup`）。

フォールバック: メールで無料登録。メールは `{{EMAIL}}`（Googleメール）。

使わない: 新しいSNSアカウントをこの仕事のためだけに作ること。GitHub連携は Google の次点（公開リポジトリと一致するなら可）。

## Field map（プレースホルダ）

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | Google | 必須 | PREFER_GOOGLE |
| メール | `{{EMAIL}}` | Googleから来る | 別アドレスを新規作成しない |
| 氏名 | `{{LEGAL_NAME_KANJI}}` | 高 | 公開名が分かれる画面なら表示は `{{DISPLAY_NAME}}` |
| 生年月 | `{{BIRTH_YEAR}}` / `{{BIRTH_MONTH}}` | 高 | 日が無ければ空 |
| 居住地 | `{{PREFECTURE}}` `{{CITY}}` | 高 | 番地まで出さなくてよい画面なら市区まで |
| 電話番号 | `{{PHONE}}` | 高 | |
| 職種 | エンジニア / 自動化 / 業務改善 から画面の最寄り | 高 | 「AI」だけにせず、自動化・実装に寄せる |
| 所有スキル | Claude Code, Codex, Python, YouTube Data API, TikTok Content Posting API, 業務自動化 | 高 | 未経験を経験と書かない |
| 経験年数 | `{{YEARS_AUTOMATION_PUBLIC}}` | 高 | 未確認なら空、または「公開実録の期間のみ」 |
| 職務経歴 | 下記 800字を短縮して貼る | 高 | |
| 職務経歴書・ポートフォリオ | `{{PORTFOLIO_URL}}` と `{{GITHUB_REPO_AUTOPILOT}}` | 任意〜高 | ファイルアップロードはローカルPDF。リポジトリに置かない |
| 稼働条件 | リモート可。週次は要相談 | 高 | 数字の創作禁止 |
| SNS | `{{GITHUB_URL}}` | 任意 | |
| 招待コード | `{{INVITE_CODE}}` | 任意 | 空でよい |


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

ここまでやってよい: Google登録、プロフィール、スキル、公開URL。

ここで止める:

- 利用規約第4条が言う「審査に必要な書類」の提出
- 免許証・マイナンバーカード・住民票・顔写真付き証明書
- 口座・振込先
- 本人確認アプリ

書類提出を求められたらパック完了扱い。出金が必要になるまで再開しない。

## thin_site_skip

false。2026-09-15 に https://sokudan.work/signup/pro が HTTP 200。Google 登録リンクあり。

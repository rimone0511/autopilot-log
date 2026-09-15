# FIELD-MAP — Anycrew 人材下書き（JA bio · 石田祐太 · n8n/AI）

> **DRAFT_ONLY.** Paste-ready JA. No secrets. **No apply. No publish.** Live form wins.  
> Seller-brand = 石田祐太 / ユタラボ / **n8n と AI** / 公式APIのみ / 人が検品できる仕組み / 未確認の数字は書かない / **応募しない** / **公開しない**。  
> 実パスワード・OTP・電話・番地・口座・身分証番号は **このリポジトリに書かない**。

CU 手順: [PLAYBOOK.md](PLAYBOOK.md)  
停止: [STOP.md](STOP.md)

公式の自己紹介字数は公開 GET / 規約に無い（**needs_check**）。超過したら短いフェンスへ降りる。URL も字数に含む。

**Safe paste の既定:** 自己紹介は **URL 無し**。公開 URL はポートフォリオ / GitHub 欄。画面が URL を受け、カウンターが足りるときだけ「URL あり」200/800。

---

## Shared placeholders

Replace locally. Never commit filled private values.

```
{{FULL_LEGAL_NAME}}
{{LEGAL_NAME_KANJI}}
{{LEGAL_NAME_KANA}}
{{DISPLAY_NAME}}
{{HANDLE}}
{{EMAIL}}
{{GOOGLE_ACCOUNT_EMAIL}}
{{PASSWORD_DO_NOT_STORE}}
{{COUNTRY}}
{{CITY}}
{{PREFECTURE}}
{{TIMEZONE}}
{{PHONE}}
{{BIRTH_YEAR}}
{{BIRTH_MONTH}}
{{BIRTH_DAY}}
{{PHOTO_LOCAL_PATH}}
{{PORTFOLIO_URL}}
{{WEBSITE_URL}}
{{GITHUB_URL}}
{{GITHUB_REPO_AUTOPILOT}}
{{YEARS_AUTOMATION_PUBLIC}}
{{HOURLY_YEN_DRAFT}}
```

Public defaults（ログイン識別と公開 URL だけ。受信箱の中身は秘密）:

| Token | Public default |
|---|---|
| `{{GOOGLE_ACCOUNT_EMAIL}}` / `{{EMAIL}}` | `rimone0511@gmail.com` |
| `{{DISPLAY_NAME}}` | `石田祐太` |
| `{{COUNTRY}}` | `Japan` |
| `{{TIMEZONE}}` | `Asia/Tokyo` |
| `{{PORTFOLIO_URL}}` / `{{WEBSITE_URL}}` | `https://yutalab.dev/` |
| `{{GITHUB_URL}}` | `https://github.com/rimone0511` |
| `{{GITHUB_REPO_AUTOPILOT}}` | `https://github.com/rimone0511/autopilot-log` |
| `{{HOURLY_YEN_DRAFT}}` | **empty** — 円額を創作しない |
| `{{YEARS_AUTOMATION_PUBLIC}}` | **empty** — 未確認なら空 |
| `{{PHONE}}` | **empty in git** — ライブが下書きを止めるときだけ台帳。成功ログに残さない |

`required_guess` はログイン後の必須マークではない。

| Token | Meaning |
|---|---|
| `required (docs)` | 公開登録面または規約が登録に必要と書く |
| `high` | プロフィール完成に近い。下書き保存はまだ通るかもしれない |
| `optional` | 公開面がスキップを許す / 任意連携 |
| `needs_check` | ログイン後フォーム未観測 |
| `STOP` | 貼らない |

---

## Seller one-liners（brand · n8n/AI）

短い欄（**12** 字。キャッチがさらに短いとき）:

```
n8nとAI自動化手順書
```

短い欄（**23** 字。キャッチ / ひとこと）:

```
n8nとAI自動化。公式APIのみ。応募しない
```

日本語（**66** 字）:

```
n8nとAI業務自動化の手順書。公式APIのみ。ブラウザ自動操作はしません。未確認の数字は書きません。応募はこの下書きではしません。
```

English（任意欄が英語のときだけ。字数 needs_check）:

```
n8n / AI automation + operator docs. Official APIs only. No browser scraping. No engagement bots. Draft profile only. Do not apply from this desk.
```

連絡先を足さない。

---

## A. Signup / 基本情報

出典: 公開 `app.any-crew.com/` モーダル、`id.any-crew.com/signup` シェル + ID バンドル、規約第3条（2026-09-16 GET）。必須マークは画面を正とする。

| 画面の項目 | 貼る値 | 必須見込み | Evidence |
|---|---|---|---|
| 登録 URL | https://id.any-crew.com/signup?auth_entry_source=front | `required (docs)` | アプリ CTA「会員登録」「会員登録(無料)」「新規会員登録はこちら」 |
| 登録経路 | Google | `required (docs)` | アプリ「FacebookかGoogleのアカウントで利用登録」。ID JS **Googleで登録する**。規約第3条 外部 SNS |
| ログイン（既存） | Googleでログイン | control | アプリモーダル POST `https://base.any-crew.com/auth/google_oauth2?state=auth_entry_source_front`。この GET は 404（POST 専用）。**POST しない** |
| 個人 / 法人 | **個人向け** | `required (docs)` | ID JS「個人向けログイン」「法人向けログイン」。法人は STOP |
| メール | `{{GOOGLE_ACCOUNT_EMAIL}}` | Google から / メール経路 | ID JS「メールアドレスで登録する」。規約は SNS 主経路 → メール単独は `needs_check`。Google 失敗なら park |
| パスワード | `{{PASSWORD_DO_NOT_STORE}}` | メール経路 | git に書かない。CSRF をコピーしない |
| Facebook で登録する | 使わない | `STOP` | 新規身分にしない |
| 氏名 | `{{LEGAL_NAME_KANJI}}` | `high` | プライバシー「氏名」 |
| 表示名 | `{{DISPLAY_NAME}}` | `high` | 推奨 `石田祐太`。資格を創作して括弧付けしない |
| 生年月日 | `{{BIRTH_YEAR}}` / `{{BIRTH_MONTH}}` / `{{BIRTH_DAY}}` | `high` | ポリシー収集項目。偽らない |
| 活動拠点 | `{{PREFECTURE}}` `{{CITY}}` | `high` | 番地は出さなくてよい画面なら市区まで |
| 電話 | `{{PHONE}}` | `STOP` unless 下書きが止まる | ポリシーは **応募・契約時** に電話番号。登録 JS に「電話番号」「SMS」なし。ライブが壁なら `sms_wait_user`。実番号を git に残さない |
| 利用規約 / 個人情報 | 人が読む | `required (docs)` | https://www.any-crew.com/terms · /privacy |
| 法人登録 | しない | `STOP` | `biz.any-crew.com` |

確認メール（ID JS）: 「確認用のメールを送りました」「メール内にあるリンクをクリックして」。OTP は親 Gmail。CU は Gmail を開かない。

---

## B. プロフィール編集（ログイン後は needs_check + ライブ）

ログイン後フォームはこの authoring では未観測。ラベルは公開 FAQ / ポリシー + ライブ。

公式 FAQ（アプリ）: 「Web上でプロフィールを入力頂くだけで、面談や職務経歴書は不要です。ただし、エージェントが仲介をする一部の案件では応募時に、面談や職務経歴書が必要になります。」  
「表示範囲の設定が可能です。検索結果への表示を「非公開」「公開」から選ぶことができます。」

| 画面の項目 | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| キャッチ / ひとこと | 上記 **12** / **23** | `optional`〜`high` | 公式字数 needs_check |
| 自己紹介 | 下記 **URL 無し** 150 / 200 / 255 / 800 | `high` | **safe paste 既定。** n8n/AI。URL は別欄 |
| スキル | n8n, AI, 業務自動化, Claude Code, Codex, Python, API（チップがあるものだけ） | `high` | 未経験を書かない |
| 職業 | 業務自動化 / エンジニアの最寄り | `high` | 「AI」だけにしない |
| 所属・職歴 | 公開実録の範囲。`{{YEARS_AUTOMATION_PUBLIC}}` | `high` | 年数創作禁止。空可 |
| 転職・就職の意向 | 複業・業務委託の最寄り | `optional` | ポリシーに項目あり。転職専願にしない |
| 稼働可能時間 | 空または要相談 | `high` | 数字の創作禁止 |
| GitHub | `{{GITHUB_URL}}` `{{GITHUB_REPO_AUTOPILOT}}` | `optional` | 公開と一致するとき |
| ポートフォリオ | `{{PORTFOLIO_URL}}` | `high` | 公開 URL のみ。身分証を置かない |
| 希望単価 | `{{HOURLY_YEN_DRAFT}}` | `optional` | **空。** 第三者の時給をコピーしない |
| プロフィール画像 | `{{PHOTO_LOCAL_PATH}}` | `optional` | 顔写真可。KYC 自撮りは不可 |
| 検索結果の表示 | **非公開** | `high`（あれば） | FAQ の二択。**公開にしない** |
| 職務経歴書 | スキップ | `optional` | 仲介必須なら応募しないので通常出ない |
| 求人応募 | しない | `STOP` | `/offers` カードがあっても |
| スカウト返信 | しない | `STOP` | このパスでは送らない |
| 電話 / SMS | やらない | `STOP` | [STOP.md](STOP.md) |
| 本人確認 | やらない | `STOP` | |
| 口座 / 出金 | やらない | `STOP` | |
| 法人切替 | やらない | `STOP` | |

---

## C. Paste — 自己紹介（URL 無し = **safe paste 既定**）

自己紹介欄の第一候補。公開 URL はポートフォリオ欄へ。測済み。超過したら短いフェンスへ。**n8n / AI。**

### 150 字

```
石田祐太です。n8nとAIによる業務自動化と手順書を扱います。売り物は動いたように見える自動化ではなく、人が検品できる仕組みです。公式APIのみ。ブラウザ自動操作・いいね自動化はしません。リモート可。週次時間は案件ごとに相談。未確認の件数は書きません。秘密は貼りません。応募はこの下書きではしません。
```

### 200 字（自己紹介の既定）

```
石田祐太。個人サイト「ユタラボ」にて、n8nとAIによる業務自動化の手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIだけを使う道具も公開中です。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。公開は人が決めます。秘密は貼りません。応募はこの下書きではしません。根拠を残す方針です。下書き保存までです。
```

### 255 字（カウンターが 255 前後のとき）

```
石田祐太。個人サイト「ユタラボ」で、n8nとAIによる業務自動化の手順・つまずき・確認できた結果を公開しています。公式APIだけを使う道具も公開中です。ブラウザ自動操作・いいね自動化はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。秘密は貼りません。公開は人が決めます。応募とスカウト返信はこの下書きではしません。公開URLはポートフォリオ欄です。作業記録を残す方針です。公開スイッチは人手側です。下書き保存までです。連絡先は本文に書きません。下書きです。非公開
```

### 800 字（カウンターがそれ以上のときだけ。切って使う）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」にて、n8nとAIで毎日の作業を自動化する手順、つまずいた点、確認できた結果を、むずかしい言葉を避けて公開しています。売り物は「動いたように見える自動化」ではなく、人が検品できる仕組みです。公開している実録と道具を、業務委託の成果物の根拠にします。提供できること：（1）n8nの繰り返し作業の自動化設計。目的・範囲・合格条件・停止条件を先に切り、実装後に回帰確認まで残します。（2）Claude CodeやCodexなど、AIに実装を任せるときの指示の書き方、検品、失敗時の切り分け。（3）YouTubeとTikTokへの公式API投稿の仕組みづくり。ブラウザ自動操作とスクレイピングは対象外です。（4）鍵の扱い、公開事故、トークン期限など、自動化が止まりやすい箇所の点検。公開している道具の例：Autopilot Log（ポートフォリオ欄）。YouTube Data API v3 と TikTok Content Posting API のみを使い、投稿の門番は壊れても非公開側に倒れます。受けないこと：いいねやフォローの自動化、権利のない投稿代行、本人確認・口座・マイナンバーの代理入力、未確認のままの公開。進め方はテキスト中心です。根拠と反証を残し、公開スイッチは依頼者または本人の手に置きます。リモート可。週次の稼働時間は案件ごとに相談します。未確認の件数や年数は書きません。確認できた公開物だけを貼ります。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。英語の一次資料は必要なら要約して渡します。契約前に範囲外を一文で確定します。納期は着手前に合意します。公開サイトとGitHubの実URLはポートフォリオ欄にだけ置きます。自己紹介欄には貼りません。応募はこの下書きではしません。
```

`{{TIMEZONE}}` を画面が別欄で求めるときは `Asia/Tokyo`。git に住所を足さない。

---

## D. Paste — URL あり（ポートフォリオ欄 / URL を受け付ける欄だけ）

自己紹介で弾かれたら使わない。測済み **200** / **800**。

### JA bio 200（URL あり）

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、n8nとAIによる業務自動化の手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIだけを使う道具も公開中です。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。公開は人が決めます。秘密は貼りません。根拠を残す方針です。下書き。
```

### JA bio 800（URL あり）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）にて、n8nとAIで毎日の作業を自動化する手順、つまずいた点、確認できた結果を、むずかしい言葉を避けて公開しています。売り物は「動いたように見える自動化」ではなく、人が検品できる仕組みです。公開している実録と道具を、業務委託の成果物の根拠にします。提供できること：（1）n8nの繰り返し作業の自動化設計。目的・範囲・合格条件・停止条件を先に切り、実装後に回帰確認まで残します。（2）Claude CodeやCodexなど、AIに実装を任せるときの指示の書き方、検品、失敗時の切り分け。（3）YouTubeとTikTokへの公式API投稿の仕組みづくり。ブラウザ自動操作とスクレイピングは対象外です。（4）鍵の扱い、公開事故、トークン期限など、自動化が止まりやすい箇所の点検。公開している道具の例：Autopilot Log（https://github.com/rimone0511/autopilot-log）。YouTube Data API v3 と TikTok Content Posting API のみを使い、投稿の門番は壊れても非公開側に倒れます。受けないこと：いいねやフォローの自動化、権利のない投稿代行、本人確認・口座・マイナンバーの代理入力、未確認のままの公開。進め方はテキスト中心です。根拠と反証を残し、公開スイッチは依頼者または本人の手に置きます。リモート可。週次の稼働時間は案件ごとに相談します。未確認の件数や年数は書きません。確認できた公開物だけを貼ります。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。英語の一次資料は要約して渡します。契約前に範囲外を一文で確定します。納期は着手前に合意します。作業の記録を残す。
```

---

## E. Skills chips (profile only — not a job apply)

ライブに無いチップは作らない。あるものから選ぶ:

- n8n
- AI
- 業務自動化
- Claude Code
- Codex
- Python
- API
- YouTube Data API
- 運用ドキュメント

「TikTok 無人投稿」とは書かない（このリポジトリの TikTok 既定は受信箱アップロード）。いいね / フォロー自動化は書かない。

---

## F. Fees — official public pages only

| Claim | Status | Source | Quote / note |
|---|---|---|---|
| 仕事を受ける側は費用なし | **cited** | アプリ FAQ https://app.any-crew.com/ | 「仕事を受けるフリーランス・副業人材の方には一切費用はかかりません。」 |
| 基本無料 | **cited** | 規約第5条 https://www.any-crew.com/terms | 「利用者は、本サービスを基本的に無料で利用することが出来ます。」求人事業者は希望により有料プラン |
| 人材側の成果報酬％ | **needs_check** | 公開規約・人材 FAQ に％なし | 企業向け成功報酬を人材プロフィールに転記しない。**作らない** |

# FIELD-MAP — Offers worker 下書き（JA bio safe paste）

> **DRAFT_ONLY.** Paste-ready JA. No secrets. **No apply.** Live form wins.  
> Seller-brand = 石田祐太 / ユタラボ / 公式APIのみ / 人が検品できる仕組み / 未確認の数字は書かない / **応募しない**。  
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
| `{{HOURLY_YEN_DRAFT}}` | **empty** — 円額を創作しない。Jobs カードの時給を貼らない |
| `{{YEARS_AUTOMATION_PUBLIC}}` | **empty** — 未確認なら空 |

`required_guess` はログイン後の必須マークではない。

| Token | Meaning |
|---|---|
| `required (docs)` | 公開登録面または規約が登録に必要と書く |
| `high` | プロフィール完成に近い。下書き保存はまだ通るかもしれない |
| `optional` | 公開面がスキップを許す / 任意連携 |
| `needs_check` | ログイン後フォーム未観測 |
| `STOP` | 貼らない |

---

## Seller one-liners（brand）

短い欄（**12** 字。キャッチがさらに短いとき）:

```
公式API自動化と手順書
```

短い欄（**23** 字。キャッチ / ひとこと）:

```
公式API自動化と手順書。応募しない方針です。
```

日本語（**66** 字）:

```
AI業務自動化と手順書。公式APIのみ。ブラウザ自動操作はしません。未確認の数字は書きません。応募はこの下書きではしません。方針です
```

English（任意欄が英語のときだけ。字数 needs_check）:

```
n8n / AI automation + operator docs. Official APIs only. No browser scraping. No engagement bots. Draft profile only. Do not apply from this desk.
```

連絡先を足さない。

---

## A. Signup / 基本情報

出典: 公開 `/worker/signup` `/worker/login` `/terms`（2026-09-16 GET）。必須マークは画面を正とする。

| 画面の項目 | 貼る値 | 必須見込み | Evidence |
|---|---|---|---|
| 登録経路 | Google | `required (docs)` | `/worker/signup` `data-testid="auth-google"` 「Googleで登録する」 `/oauth/worker_signup/google` |
| メール | `{{GOOGLE_ACCOUNT_EMAIL}}` | Google から / メール経路 | 公開ボタン「メールアドレスで登録する」 |
| パスワード | `{{PASSWORD_DO_NOT_STORE}}` | メール経路 | git に書かない |
| 既存アカウント | ログイン | control | 「既にアカウントをお持ちの方はコチラ」→ `/worker/login` |
| GitHub で登録する | 使わない（あとで任意連携） | `optional` | `data-testid="auth-github"`。公開リポジトリ一致時のみ後で |
| X / LinkedIn で登録する | 使わない | `STOP` | 新規身分にしない |
| 氏名 | `{{LEGAL_NAME_KANJI}}` | `high` | 規約第4条「必要な情報」。ライブを正とする |
| 表示名 | `{{DISPLAY_NAME}}` | `high` | 推奨 `石田祐太`。資格を創作して括弧付けしない |
| 生年月日 | `{{BIRTH_YEAR}}` / `{{BIRTH_MONTH}}` / `{{BIRTH_DAY}}` | `high` | 第三者解説あり。偽らない。画面を正とする |
| 活動拠点 | `{{PREFECTURE}}` `{{CITY}}` | `high` | 番地は出さなくてよい画面なら市区まで |
| 電話 | `{{PHONE}}` | 画面が下書きを止めるときだけ | 実番号を git に残さない。SMS=`sms_wait_user` |
| 業種 / 職種 | エンジニア / 自動化 / 業務改善の最寄り | `high` | 無いチップを作らない。「AI」だけにしない |
| 個人/法人 | 個人 | `high` | 法人・採用担当を名乗らない |
| 利用規約 / 個人情報 | 人が読む | `required (docs)` | footer「個人情報のお取り扱いについて」。エージェントは箱を捏造しない |
| 企業登録 | しない | `STOP` | `/client/` |

---

## B. プロフィール編集（ログイン後は needs_check + ライブ）

ログイン後フォームはこの authoring では未観測。ラベルは厚パック / LP の公開文言 + ライブ。

| 画面の項目 | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| キャッチ / ひとこと | 上記 **12** / **23** | `optional`〜`high` | 公式字数 needs_check |
| 自己紹介 | 下記 **URL 無し** 150 / 200 / 255 / 800 | `high` | **safe paste 既定。** URL は別欄 |
| スキル | Claude Code, Codex, Python, API, 業務自動化, YouTube Data API, n8n（チップがあるものだけ） | `high` | 未経験を書かない |
| 働ける職種 | エンジニア / 自動化の最寄り | `high` | |
| 業務委託（副業）意欲 | 検討する、の最寄り | `high` | 盛らない |
| 転職意欲 | 急いでいない / 良い話があれば の最寄り | `optional` | 転職だけに振り切らない |
| 希望の働き方 | 業務委託・副業・リモートの最寄り | `high` | 転職専願にしない |
| GitHub | `{{GITHUB_URL}}` `{{GITHUB_REPO_AUTOPILOT}}` | `optional` | Google のあと。公開と一致するとき |
| ポートフォリオ | `{{PORTFOLIO_URL}}` | `high` | 公開 URL のみ。身分証を置かない |
| 経歴 | 公開実録の期間だけ。`{{YEARS_AUTOMATION_PUBLIC}}` | `high` | 空可。年数創作禁止。800 を短縮して貼る |
| 希望単価 | `{{HOURLY_YEN_DRAFT}}` | `optional` | **空。** カードの時給をコピーしない |
| 年収診断 | 空で進む / park | `STOP` if submit required | 数値創作禁止 |
| プロフィール画像 | `{{PHOTO_LOCAL_PATH}}` | `optional` | 顔写真可。KYC 自撮りは不可 |
| 公開設定 | 非公開 / 下書き | `high`（あれば） | トグルが無ければ needs_check |
| 求人応募 | しない | `STOP` | 「登録して求人に応募する」 |
| スカウト返信 | しない | `STOP` | このパスでは送らない |
| 本人確認 | やらない | `STOP` | [STOP.md](STOP.md) |
| 口座 / 出金 | やらない | `STOP` | |
| 有料ブース | やらない | `STOP` | |
| クライアント切替 | やらない | `STOP` | |

---

## C. Paste — 自己紹介（URL 無し = **safe paste 既定**）

自己紹介欄の第一候補。公開 URL はポートフォリオ欄へ。測済み。超過したら短いフェンスへ。

### 150 字

```
石田祐太です。AIによる業務自動化と手順書を扱います。売り物は動いたように見える自動化ではなく、人が検品できる仕組みです。公式APIのみ。ブラウザ自動操作・いいね自動化はしません。リモート可。週次時間は案件ごとに相談。未確認の件数は書きません。秘密は貼りません。応募はこの下書きではしません。下書き。
```

### 200 字（自己紹介の既定）

```
石田祐太。個人サイト「ユタラボ」で、AIによる業務自動化の手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIだけを使う動画アップロード道具も公開中です。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。公開は人が決めます。秘密は貼りません。応募はこの下書きではしません。根拠を残す方針です。下書き保存まで
```

### 255 字（カウンターが 255 前後のとき）

```
石田祐太。個人サイト「ユタラボ」で、AIによる業務自動化の手順・つまずき・確認できた結果を公開しています。公式APIだけを使う動画アップロード道具も公開中です。ブラウザ自動操作・いいね自動化はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。秘密は貼りません。公開は人が決めます。応募とスカウト返信はこの下書きではしません。公開URLはポートフォリオ欄です。作業記録を残す方針です。公開スイッチは人手側です。下書き保存までです。連絡先は本文に書きません。下書きです
```

### 800 字（カウンターがそれ以上のときだけ。切って使う）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」で、AIを使って毎日の作業を自動化する手順、つまずいた点、確認できた結果を、むずかしい言葉を避けて公開しています。売り物は「動いたように見える自動化」ではなく、人が検品できる仕組みです。公開している実録と道具を、業務委託の成果物の根拠にします。提供できること：（1）繰り返し作業の自動化設計。目的・範囲・合格条件・停止条件を先に切り、実装後に回帰確認まで残します。（2）Claude CodeやCodexなど、AIに実装を任せるときの指示の書き方、検品、失敗時の切り分け。（3）YouTubeとTikTokへの公式API投稿の仕組みづくり。ブラウザ自動操作とスクレイピングは対象外です。（4）鍵の扱い、公開事故、トークン期限など、自動化が止まりやすい箇所の点検。公開している道具の例：Autopilot Log（ポートフォリオ欄）。YouTube Data API v3 と TikTok Content Posting API のみを使い、投稿の門番は壊れても非公開側に倒れます。受けないこと：いいねやフォローの自動化、権利のない投稿代行、本人確認書類・口座・マイナンバーの代理入力、未確認のままの公開。進め方はテキスト中心です。根拠と反証を残し、公開スイッチは依頼者または本人の手に置きます。リモート可。週次の稼働時間は案件ごとに相談します。未確認の件数や年数は書きません。確認できた公開物だけを貼ります。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。英語の一次資料は必要なら要約して渡します。契約前に範囲外を一文で確定します。納期は着手前に合意します。公開サイトとGitHubの実URLはポートフォリオ欄にだけ置きます。自己紹介欄には貼りません。応募はこの下書きではしません。下書き。
```

`{{TIMEZONE}}` を画面が別欄で求めるときは `Asia/Tokyo`。git に住所を足さない。

---

## D. Paste — URL あり（ポートフォリオ欄 / URL を受け付ける欄だけ）

自己紹介で弾かれたら使わない。測済み **200** / **800**（PR#30 と同文。字数確認済み）。

### JA bio 200（URL あり）

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIによる業務自動化の手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIだけを使う動画アップロード道具も公開中です。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。公開は人が決めます。秘密は貼りません。根拠を残す方針です。
```

### JA bio 800（URL あり）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIを使って毎日の作業を自動化する手順、つまずいた点、確認できた結果を、むずかしい言葉を避けて公開しています。売り物は「動いたように見える自動化」ではなく、人が検品できる仕組みです。公開している実録と道具を、業務委託の成果物の根拠にします。提供できること：（1）繰り返し作業の自動化設計。目的・範囲・合格条件・停止条件を先に切り、実装後に回帰確認まで残します。（2）Claude CodeやCodexなど、AIに実装を任せるときの指示の書き方、検品、失敗時の切り分け。（3）YouTubeとTikTokへの公式API投稿の仕組みづくり。ブラウザ自動操作とスクレイピングは対象外です。（4）鍵の扱い、公開事故、トークン期限など、自動化が止まりやすい箇所の点検。公開している道具の例：Autopilot Log（https://github.com/rimone0511/autopilot-log）。YouTube Data API v3 と TikTok Content Posting API のみを使い、投稿の門番は壊れても非公開側に倒れます。受けないこと：いいねやフォローの自動化、権利のない投稿代行、本人確認書類・口座・マイナンバーの代理入力、未確認のままの公開。進め方はテキスト中心です。根拠と反証を残し、公開スイッチは依頼者または本人の手に置きます。リモート可。週次の稼働時間は案件ごとに相談します。未確認の件数や年数は書きません。確認できた公開物だけを貼ります。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。英語の一次資料は必要なら要約して渡します。契約前に範囲外を一文で確定します。納期は着手前に合意します。作業の記録を残す。
```

---

## E. Skills chips (profile only — not a job apply)

ライブに無いチップは作らない。あるものから選ぶ:

- Claude Code
- Codex
- Python
- API
- 業務自動化
- YouTube Data API
- n8n
- 運用ドキュメント

「TikTok 無人投稿」とは書かない（このリポジトリの TikTok 既定は受信箱アップロード）。いいね / フォロー自動化は書かない。

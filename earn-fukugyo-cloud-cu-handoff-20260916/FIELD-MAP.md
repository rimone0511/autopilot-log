> DRAFT_ONLY field map. NO login in the authoring session. NO secrets. NO invented credentials.  
> Paste values for CU. Stops: [STOP.md](STOP.md). Step order: [PLAYBOOK.md](PLAYBOOK.md).  
> Labels come from **public `/sign_up` JS** + **TOS** (2026-09-16). Logged-in profile widgets were **not** opened. Live wizard wins.

# FIELD-MAP — 複業クラウド talent / B03

Desk: 複業クラウド（旧 Another Works） B03 / CU-12  
Livecheck: 2026-09-16, public talent HTML/JS + TOS (no account created)

`required_guess` is **not** a logged-in required-field dump. Values:

| Token | Meaning |
|---|---|
| `required (docs)` | TOS or public signup JS names the control as part of creating the talent account |
| `high` | TOS says プロフィールを設定する必要がある / third-party onboarding lists it; draft save may still work without it |
| `optional (docs)` | Third-party public writeup marks 任意. Confirm live |
| `needs_check` | Official HTML/JS silent, or the live widget was not opened logged-in |
| `STOP` | Do not fill. Not a paste target |

Placeholders stay empty of secrets in git. Fill only from the operator’s local ledger at paste time.

Paste bios: **石田祐太 / AI自動化・n8n**. Recount after placeholder fill. Counts below are committed Japanese character counts (no secrets).

---

## A. Sign up (public `/sign_up` JS + TOS 第1.3条)

Public signup https://talent.aw-anotherworks.com/sign_up (retrieved 2026-09-16): title **新規登録**; static HTML is a Next.js loader (`buildId` `8xWpf_UM-Ow_9wUJEAg3E`); public chunk `2ft1bogak3uo6.js` paints the form in the browser.

| UI label (public JS / TOS) | `required_guess` | DRAFT_ONLY paste | Cite / gap |
|---|---|---|---|
| 外部サービスでサインイン → **Googleでサインイン** | preferred path | MAIN `{{GOOGLE_ACCOUNT_EMAIL}}` only. Same Google every later login | Signup chunk `handleClickGoogle` / `signInGoogle` / **「Googleでサインイン」**. Icon label **`needs_check` until click** (static HTML has no buttons) |
| Facebookでサインイン | `STOP` as new identity | Do not use | Same chunk |
| Appleでサインイン | `STOP` as new identity | Do not use | Same chunk |
| メールアドレス | fallback `required (docs)` on email path | Same MAIN `{{EMAIL}}`. No new mailbox | Public JS. Toast: メールアドレスが既に登録されています |
| パスワード | email path | `{{PASSWORD_DO_NOT_STORE}}`. Never in git. JS: 半角英数字8文字以上、半角英字・半角数字をそれぞれ1文字以上 | Public JS |
| パスワードの確認 | email path | Same password. Never in git | Public JS. Toast: パスワードが一致しません |
| 利用規約 / プライバシーポリシー に同意 | `required (docs)` | Human reads. Live CU may tick after GO. Toast: 利用規約等に同意が必要です | TOS 第1.3条1. Links: live `constants.Tos` / `PrivacyPolicy`. Cite https://cl.aw-anotherworks.com/user_tos and https://anotherworks.co.jp/user_privacy |
| 登録 | control | Email path. Google path uses the Google button | Public JS children **登録** / **新規登録** |
| サインインはこちら | control | Existing MAIN → `/login` | Public JS |
| 新規登録はこちら (login page) | control | `/sign_up` | Login chunk |
| reCAPTCHA / Press & Hold | gate if painted | PLAYBOOK skip → **`blocked_skip`**. Do **not** copy site keys / tokens into git | Signup-specific chunk: **no** recaptcha string. Shared Firebase chunk has `RECAPTCHA_NOT_ENABLED` SDK errors — **not** proof `/sign_up` paints captcha |
| 電話番号 / SMS | `needs_check` | Only if draft save blocks. `{{PHONE}}` from user chat. Else skip | Not in signup chunk. [STOP.md](STOP.md) |
| 企業採用担当者の方はこちら | `STOP` | Close | Home/nav JS. `cl.aw-anotherworks.com` |

Google / email / password values are **never** committed. Do not write a sample password.

---

## B. Profile after account (TOS + third-party labels — live form wins)

TOS 第2.1条2: 登録タレントはプロフィールを設定する必要がある. 当社が定める項目は **全ての登録事業者に公開**. Extra toggles stay off if the live form offers 非公開.

Logged-in field names were **not** scraped this session. The table below is a paste order for CU. Third-party columns are marked. **Do not treat third-party as official required.**

### B1. Identity (not bank)

| Label (source) | `required_guess` | DRAFT_ONLY paste | Cite |
|---|---|---|---|
| 氏名 | `high` | `{{LEGAL_NAME_KANJI}}` 戸籍上の氏名（漢字） | Third-party onboarding (BCN / gusare). Live form |
| 氏名カナ | `needs_check` | `{{LEGAL_NAME_KANA}}` if asked | Live form |
| ニックネーム / 表示名 | `needs_check` | `{{DISPLAY_NAME}}` 推奨 **石田祐太** if the form splits from legal name | gusare. Live form |
| メール | account field | MAIN only. Do not “fix” to a different inbox this pass | Signup JS |
| 生年月日 | `needs_check` | `{{BIRTH_YEAR}}-{{BIRTH_MONTH}}-{{BIRTH_DAY}}` if asked. Do not invent | Live form |
| 居住地 | `optional (docs)` third-party | `{{PREFECTURE}}` / `{{CITY}}`. **No street in git**. Skip if save works without it | freelance-board 任意 list. Live form |
| 電話 | `needs_check` | `{{PHONE}}` only if **draft save** blocks. User-chat wait. If ID/selfie appears → KYC STOP | [STOP.md](STOP.md) |
| 顔写真 | `optional (docs)` third-party | `{{PHOTO_LOCAL_PATH}}` local face photo. Not an ID | freelance-board / ITプロ. Live form |
| 非表示にしたい企業 | `optional (docs)` third-party | `{{BLOCK_COMPANY_NAMES}}` from ledger. Real names stay off git | freelance-board 任意 |
| 経験のある企業 | `optional (docs)` third-party | Public facts only. Skip if empty | freelance-board 任意 |

### B2. Profile body (this pass)

| Label (source) | `required_guess` | DRAFT_ONLY paste | Cite |
|---|---|---|---|
| ひとこと / キャッチ | `needs_check` | Fence **25** below if a short field exists | Live form. Official max length **not** on public GET |
| 自己紹介 | `high` | Fence **200** (default) or **800**. n8n / AI自動化. URL-ok if the counter accepts URLs; else URL-free | TOS 第2.1条2 (must set a profile). Length **needs_check** |
| 職種 | `high` | エンジニア / 業務自動化 / 最寄り **existing** chip | Company LP「80以上の職種」(marketing). gusare: 職種 + 経験年数 + 得意領域最大3. Live chips only |
| 経験年数 | `needs_check` | `{{YEARS_AUTOMATION_PUBLIC}}` or skip. Do not invent | gusare. Empty ledger → skip |
| 得意領域 | `needs_check` | Max 3 **existing** chips if the widget exists. n8n / 業務自動化 / API の最寄り | gusare third-party |
| スキル | `high` | Existing chips: n8n, Claude Code, Codex, Python, API, 業務自動化 | Live DB. No 追加リクエスト this pass |
| 希望する働き方 / 稼働 | `needs_check` | リモート可. 週次は要相談. Follow live selects | gusare: 単価・稼働日数・時間帯 are selects. Do not invent hours |
| 希望単価 | `optional (docs)` third-party | `{{HOURLY_YEN_DRAFT}}` **empty** / 要相談. Job-title 円 is not a profile rate. Else `rate_empty` | freelance-board 任意. OG mentions 希望単価 as a **search filter**, not a required paste |
| 転職の意向度 | `optional (docs)` third-party | 複業・業務委託の最寄り. Not 今すぐ転職 | freelance-board 任意. TOS 第2.1条5 転職スカウト = company-side |
| ポートフォリオ | `optional (docs)` third-party | Public URLs below | freelance-board 任意. BCN: skippable |
| 最終学歴 | `needs_check` | Skip unless asked and ledger has it | gusare |
| 職歴 | `needs_check` | Public facts only. Empty years if ledger empty | gusare: 企業名 / ポジション / 期間 |
| 公開／非公開 | `needs_check` | Prefer 非公開 / 下書き if visible. TOS: some items still go to all registered companies | TOS 第2.1条2 |
| 自己紹介テンプレート | skip | Do not use unless human asks; then **read before save** | BCN / ITプロ mention templates |

### B3. Apply / catalog / money — not paste targets

| Label | `required_guess` | DRAFT_ONLY paste | Cite |
|---|---|---|---|
| エントリー / 応募する | **STOP** | Do not press | TOS 第2.1条3 / 第3.1条2 |
| キニナル / キニナル済 | **STOP** | Do not press | Public JS like-control |
| スカウト返信 / オファー返信 | **STOP** | Do not pitch | TOS 第2.1条4 |
| ソリューション投稿 | **STOP** | Catalog/publish. Not this pass | Company LP ソリューション. ITプロ / gusare |
| 本人確認 | **STOP** | Note screen type only | Not on public TOS/privacy GET. Live still wins |
| 口座 / 出金 | **STOP** | — | Not on public TOS GET |
| 事業者プラン | **STOP** | Close | TOS 第3.2条 |

---

## Placeholders (empty in git)

- `{{GOOGLE_ACCOUNT_EMAIL}}` / `{{EMAIL}}` MAIN Google mailbox
- `{{PASSWORD_DO_NOT_STORE}}` email path only
- `{{LEGAL_NAME_KANJI}}` 戸籍上の氏名（漢字）
- `{{LEGAL_NAME_KANA}}` 氏名カナ if asked
- `{{DISPLAY_NAME}}` 表示名。推奨: `石田祐太`
- `{{PHONE}}` 日本の携帯電話 — only if draft save blocks
- `{{PREFECTURE}}` / `{{CITY}}` 住所を求められたとき。番地は git に書かない
- `{{BIRTH_YEAR}}` / `{{BIRTH_MONTH}}` / `{{BIRTH_DAY}}`
- `{{PORTFOLIO_URL}}` 推奨公開: `https://yutalab.dev/`
- `{{GITHUB_URL}}` 推奨公開: `https://github.com/rimone0511`
- `{{GITHUB_REPO_AUTOPILOT}}` `https://github.com/rimone0511/autopilot-log`
- `{{PHOTO_LOCAL_PATH}}` 顔写真のローカルパス（コミット禁止）
- `{{HOURLY_YEN_DRAFT}}` 空なら空 / 要相談 / `rate_empty`
- `{{YEARS_AUTOMATION_PUBLIC}}` 空なら職歴年数を作らない
- `{{BLOCK_COMPANY_NAMES}}` 実名を git に書かない

---

## Paste fences — 石田祐太 / AI自動化・n8n

Official 自己紹介 max length was **not** on the public GET → `needs_check`. Default **200**. Use **800** only if the counter is that large. If the field rejects URLs, use the URL-free pair. Public URLs still go in ポートフォリオ.

### ひとこと（25字。短い欄があるときだけ）

```
n8nとAIで、人が検品できる業務自動化をします。
```

### 自己紹介 200（200字・URL あり・既定）

```
石田祐太。n8nとAIで業務自動化します。個人サイト「ユタラボ」（https://yutalab.dev/）で、手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIのみ。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。公開は人が決めます。秘密は貼りません。根拠を残す方針です。下書き保存まで。検品を優先。
```

### 自己紹介 800（800字・URL あり）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、n8nとAIで毎日の作業を自動化する手順、つまずいた点、確認できた結果を、むずかしい言葉を避けて公開しています。売り物は「動いたように見える自動化」ではなく、人が検品できる仕組みです。公開している実録と道具を、業務委託の成果物の根拠にします。提供できること：（1）n8n中心の繰り返し作業の自動化設計。目的・範囲・合格条件・停止条件を先に切り、実装後に回帰確認まで残します。（2）Claude CodeやCodexなど、AIに実装を任せるときの指示の書き方、検品、失敗時の切り分け。（3）YouTubeとTikTokへの公式API投稿の仕組みづくり。ブラウザ自動操作とスクレイピングは対象外です。（4）鍵の扱い、公開事故、トークン期限など、自動化が止まりやすい箇所の点検。公開している道具の例：Autopilot Log（https://github.com/rimone0511/autopilot-log）。YouTube Data API v3 と TikTok Content Posting API のみを使い、投稿の門番は壊れても非公開側に倒れます。受けないこと：いいねやフォローの自動化、権利のない投稿代行、本人確認書類・口座・マイナンバーの代理入力、未確認のままの公開。進め方はテキスト中心です。根拠と反証を残し、公開スイッチは依頼者または本人の手に置きます。リモート可。週次の稼働時間は案件ごとに相談します。未確認の件数や年数は書きません。確認できた公開物だけを貼ります。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。英語資料は要約して渡します。契約前に範囲外を一文で確定します。納期は着手前に合意します。作業の記録を残す。
```

### 自己紹介 200（200字・URL 無し）

```
石田祐太。n8nとAIで業務自動化します。個人サイト「ユタラボ」で、手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIのみ。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。公開は人が決めます。秘密は貼りません。根拠を残す方針です。下書き保存まで。応募はこの下書きではしません。URLは別欄です。下書き。
```

### 自己紹介 800（800字・URL 無し）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」で、n8nとAIで毎日の作業を自動化する手順、つまずいた点、確認できた結果を、むずかしい言葉を避けて公開しています。売り物は「動いたように見える自動化」ではなく、人が検品できる仕組みです。公開している実録と道具を、業務委託の成果物の根拠にします。提供できること：（1）n8n中心の繰り返し作業の自動化設計。目的・範囲・合格条件・停止条件を先に切り、実装後に回帰確認まで残します。（2）Claude CodeやCodexなど、AIに実装を任せるときの指示の書き方、検品、失敗時の切り分け。（3）YouTubeとTikTokへの公式API投稿の仕組みづくり。ブラウザ自動操作とスクレイピングは対象外です。（4）鍵の扱い、公開事故、トークン期限など、自動化が止まりやすい箇所の点検。公開している道具の例：Autopilot Log（ポートフォリオ欄）。YouTube Data API v3 と TikTok Content Posting API のみを使い、投稿の門番は壊れても非公開側に倒れます。受けないこと：いいねやフォローの自動化、権利のない投稿代行、本人確認書類・口座・マイナンバーの代理入力、未確認のままの公開。進め方はテキスト中心です。根拠と反証を残し、公開スイッチは依頼者または本人の手に置きます。リモート可。週次の稼働時間は案件ごとに相談します。未確認の件数や年数は書きません。確認できた公開物だけを貼ります。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。英語資料は要約して渡します。契約前に範囲外を一文で確定します。納期は着手前に合意します。作業の記録を残す。公開URLは自己紹介に貼らずポートフォリオ欄へ。応募とキニナルはこの下書きではしません。下書き保存まで。検品優先。
```

English (only if a live field is English):

```
n8n / AI automation + operator docs. Official APIs only. No browser scraping. No engagement bots. Draft profile only. Do not apply from this desk.
```

連絡先を自己紹介本文に足さない。

### スキル chips (pick live matches only)

`n8n` · `Claude Code` · `Codex` · `Python` · `API連携` · `業務自動化` · `技術記事`

If a chip is missing from the DB: **skip**. Do not file 追加リクエスト this pass. 経験年数 = ledger or skip.

Do not claim TikTok posting from this repo is unattended.

### ポートフォリオ rows

| Title (public) | URL |
|---|---|
| ユタラボ | `{{PORTFOLIO_URL}}` → https://yutalab.dev/ |
| Autopilot Log | `{{GITHUB_REPO_AUTOPILOT}}` → https://github.com/rimone0511/autopilot-log |

---

## Sources (public)

- Signup UI: https://talent.aw-anotherworks.com/sign_up (`SIGN_UP:"/sign_up"`; chunk labels Google / Facebook / Apple / メール)
- Login UI: https://talent.aw-anotherworks.com/login （新規登録はこちら）
- TOS: https://cl.aw-anotherworks.com/user_tos （第1.3条 登録 / 第2.1条 タレント無料・プロフィール・応募）
- Privacy (TOS footer): https://anotherworks.co.jp/user_privacy
- Talent origin OG: 完全無料 / 中間マージンなどは一切発生しません — marketing; not a ％ table
- Third-party field lists (not official required): gusare profile/tsukaikata, BCN 2022 onboarding, freelance-board, ITプロマガジン — live form wins
- STOP URLs / KYC notes: [STOP.md](STOP.md)

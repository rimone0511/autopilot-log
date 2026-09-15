> **REGISTER-CU-CUT.** Not next live CU. Jobs-first. Do not autoplay. Banner: [STATUS.md](STATUS.md).  
> DRAFT_ONLY field map. NO login in the authoring session. NO secrets. NO invented credentials.  
> Paste values only after a later **human GO**. Stops: [STOP.md](STOP.md). Step order: [PLAYBOOK.md](PLAYBOOK.md).  
> Labels come from **public `/signup` HTML** + **Workship Help** (2026-09-16). Live wizard wins.

# FIELD-MAP — Workship freelance / B02

Desk: Workship（ワークシップ） B02 / QUEUE B2 / CU-11  
Livecheck: 2026-09-16, public help + https://goworkship.com/signup (no account created)

`required_guess` is **not** a logged-in required-field dump. Values:

| Token | Meaning |
|---|---|
| `required (docs)` | Help or public signup names the control as part of creating the freelance account |
| `high` | Help lists it on プロフィールを編集 / flow STEP2; draft save may still work without it |
| `optional (docs)` | Help documents skip / later / 任意 |
| `needs_check` | Help is silent or the live widget was not opened logged-in |
| `STOP` | Do not fill. Not a paste target |

Placeholders stay empty of secrets in git. Fill only from the operator’s local ledger at paste time.

---

## A. Sign up (public page + help/44)

Public signup (https://goworkship.com/signup, retrieved 2026-09-16): title **フリーランス登録をする | Workship**; heading **SNSで登録**; `#firebaseui-auth-container`; JS `firebase.auth.GoogleAuthProvider.PROVIDER_ID`; then **メールアドレス 必須**, **パスワード 必須** (placeholder 「8〜20文字の半角英数字記号で入力」), **招待コード** (placeholder 「招待コードがあれば入力してください」), agree プライバシーポリシー + 利用規約 + 個人情報の取り扱いについて, button **登録する**, reCAPTCHA.

Static HTML does **not** print the word “Google” on the SNS icons. Headless render of the same URL (no login) showed the FirebaseUI **Google G** button under **SNSで登録**. **If the live icon is missing, fall back to email.**

| UI label (help / public HTML) | `required_guess` | DRAFT_ONLY paste | Cite / gap |
|---|---|---|---|
| SNSで登録 → Google G | preferred path | MAIN `{{GOOGLE_ACCOUNT_EMAIL}}` only. Same Google every later login | Public `/signup` + Firebase `GoogleAuthProvider.PROVIDER_ID`. Headless render showed the G button. If missing live → email |
| メールアドレス（必須） | fallback `required (docs)` on email path | Same MAIN `{{EMAIL}}`. No new mailbox | Public `/signup` rendered **必須** · [help/44](https://goworkship.com/help/how_to/44) |
| パスワード（必須） | email path | `{{PASSWORD_DO_NOT_STORE}}`. UI hint 8–20 半角英数字記号. Never in git | Public `/signup` |
| 招待コード | `optional (docs)` | `{{INVITE_CODE}}` empty unless ledger has one | Public placeholder |
| プライバシーポリシー / 利用規約 / 個人情報の取り扱い に同意する | `required (docs)` | Human reads. Live CU may tick after GO | `/privacy-policy` · `/guide` · `/handling-of-personal-information` |
| 登録する | control | Email path only. Google path uses FirebaseUI | Public `/signup` |
| reCAPTCHA | gate | Human. Hold: `holdDurationMs` 1800 / retry 2500 | Public `/signup`. **Do not copy site keys / tokens into git** |
| ログイン → SNSでログイン | control | If MAIN already has Workship → login. No second account | Public `/login` |
| 採用担当者はこちら | `STOP` | Close | Public `/login` |
| ENTERPRISE | `STOP` | Close | https://enterprise.goworkship.com/ |

Google / email / password values are **never** committed. Do not write a sample password. Do not record CSRF `_Token` or reCAPTCHA response values.

Help/44 also names older chrome 「アカウントを作成する」. Live button this GET is **登録する**. **Live form wins.**

---

## B. Profile after account (help labels)

Flow STEP2: 自己紹介 · 職歴 · 受賞歴 · ポートフォリオ · スキル · 公開範囲 ([flow](https://goworkship.com/flow)). Path: 画面右上 → **プロフィールを編集**.

### B1. Identity (not bank)

| Help label | `required_guess` | DRAFT_ONLY paste | Cite |
|---|---|---|---|
| 登録名 | `required (docs)` as contract name | `{{LEGAL_NAME_KANJI}}` 本名 or 旧姓 from ledger. Display everyday `{{DISPLAY_NAME}}` only if the form splits | [活動名不可](https://goworkship.com/help/edit_profile/69) |
| 活動名 / 通称名 / 屋号 | `STOP` | Do not use | Same article |
| 登録名 visibility | n/a | Before エントリー, help says initials (例「K.H」). 公開／非公開 **cannot** be set on 登録名. Do not エントリー to “reveal” the name | [公開範囲](https://goworkship.com/help/edit_profile/58) |
| メール | account field | MAIN only. Do not “fix” to a different inbox this pass. Confirm URL = parent Gmail | [help/44](https://goworkship.com/help/how_to/44) |
| 生年月日 | `needs_check` (not on public `/signup` HTML this GET) | `{{BIRTH_YEAR}}-{{BIRTH_MONTH}}-{{BIRTH_DAY}}` if the live form asks. Follow live age gate. Do not invent | Live form |
| 住所 | `needs_check` | パーソナル情報 may include 住所 ([account_config](https://goworkship.com/help/account_config)). `{{PREFECTURE}}` / `{{CITY}}` if asked. **No street in git**. Skip if save works without it | Help index; live form |
| 電話 | `needs_check` | `{{PHONE}}` only if **draft save** blocks. User-chat wait. If ID/selfie appears → KYC STOP | Live form |
| facebook / twitter URL (パーソナル情報) | `optional (docs)` | Skip new SNS. Do not bind a new Facebook/Twitter identity | [account_config](https://goworkship.com/help/account_config) |
| プロフィール画像 | `optional (docs)` | `{{PHOTO_LOCAL_PATH}}` local face photo. Skip if wizard allows. Not an ID | [account_config](https://goworkship.com/help/account_config) |
| プライバシー企業 / 企業ブロック | `optional (docs)` | `{{BLOCK_COMPANY_NAMES}}` from ledger. Real names stay off git | [account_config](https://goworkship.com/help/account_config) |

### B2. プロフィールを編集 (STEP2 — this pass)

| Help label | `required_guess` | DRAFT_ONLY paste | Cite |
|---|---|---|---|
| 自己紹介 | `high` | Fence **200** or **800** below. Save **更新する**. Do not use **AIで自動入力する** unless human asks; then read before save | [help/52](https://goworkship.com/help/edit_profile/52) |
| やってみたいこと | `high` | Short fence below. **更新する** | [help/53](https://goworkship.com/help/edit_profile/53) |
| 職歴 | `high` | Public facts only. **追加する**. Empty years if `{{YEARS_AUTOMATION_PUBLIC}}` empty | [help/75](https://goworkship.com/help/edit_profile/75) |
| ポートフォリオ | `high` | Public URLs. **追加する** | [help/54](https://goworkship.com/help/edit_profile/54) |
| スキル | `high` | Existing chips only. Help: **経験年数** and **スキルレベル** required on the widget. Ledger or skip chip. No **追加リクエスト** this pass | [help/56](https://goworkship.com/help/edit_profile/56) |
| 受賞歴 | `optional (docs)` | Skip unless ledger has a public award | [help/55](https://goworkship.com/help/edit_profile/55) |
| 学歴 | `optional (docs)` | Skip unless asked and ledger has it | [help/57](https://goworkship.com/help/edit_profile/57) |
| 公開／非公開 (人物マーク → 鍵) | `high` if control visible | Prefer 非公開 / 鍵 on 職歴・ポートフォリオ・受賞歴・学歴・スキル | [help/58](https://goworkship.com/help/edit_profile/58) |
| 希望単価 / 時給 | `needs_check` | `{{HOURLY_YEN_DRAFT}}` or 要相談 / empty. Else `rate_empty` | Live form. Do not invent 円 |
| 職種 | `needs_check` | エンジニア / 業務自動化 / ディレクター系の **existing** chip | Live form |
| 働き方 | `needs_check` | フリーランス or 複業 as the live value. Employment rules = human | Live form |
| エージェント 提案希望 | `STOP` | Do not apply this pass | [about index](https://goworkship.com/help/about_workship) |

Help/52 note: do not put past client/case names in 自己紹介 if that would break NDA.

### B3. Apply / money — not paste targets

| Help label | `required_guess` | DRAFT_ONLY paste | Cite |
|---|---|---|---|
| 気になる！ | **STOP** | Official = エントリー完了 + メッセージルーム | [help/72](https://goworkship.com/help/how_to/72) |
| エントリー | **STOP** | Same stop | [help/77](https://goworkship.com/help/how_to/77) |
| スカウト返信 | **STOP** | Do not pitch | help/72 · help/77 |
| 成約報告 | **STOP** | Needs エントリー/スカウト first | [help/86](https://goworkship.com/help/agreement/86) |
| 契約管理 署名をする | **STOP** | 機密保持契約 / 準委任契約 | [help/44](https://goworkship.com/help/how_to/44) · [help/105](https://goworkship.com/help/agreement/105) |
| 前払いオプション | **STOP** | 本人確認が必要. 手数料％ not copied | [help/95](https://goworkship.com/help/agreement/95) |
| 振込先口座 | **STOP** | Reward + お祝い金 path | [help/118](https://goworkship.com/help/agreement/118) · [help/100](https://goworkship.com/help/agreement/100) |
| 帳票の振込先 (ドキュメント設定) | **STOP** | Help says this is **separate** from Workship payout. Still skip this pass | [document](https://goworkship.com/help/document) |
| LINE 通知連携 | skip | New identity risk | [account_config](https://goworkship.com/help/account_config) |

---

## Placeholders (empty in git)

Same family as Week2 packs. Values live only in the operator ledger.

- `{{GOOGLE_ACCOUNT_EMAIL}}` / `{{EMAIL}}` MAIN Google mailbox
- `{{PASSWORD_DO_NOT_STORE}}` email path only
- `{{INVITE_CODE}}` empty OK
- `{{LEGAL_NAME_KANJI}}` 戸籍上の氏名（漢字）— 本名 or 旧姓
- `{{LEGAL_NAME_KANA}}` 氏名カナ if asked
- `{{DISPLAY_NAME}}` 表示名。推奨: `石田祐太` (only if the form is not the contract 登録名)
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

## Paste fences

Recount after placeholder fill. 200 / 800 counts below are the committed Japanese character counts (no secrets). Same bodies as PR#30 thick pack.

### 自己紹介 200（200字）

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIによる業務自動化の手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIだけを使う動画アップロード道具も公開中です。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。公開は人が決めます。秘密は貼りません。根拠を残す方針です。
```

### 自己紹介 800（800字）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIを使って毎日の作業を自動化する手順、つまずいた点、確認できた結果を、むずかしい言葉を避けて公開しています。売り物は「動いたように見える自動化」ではなく、人が検品できる仕組みです。公開している実録と道具を、業務委託の成果物の根拠にします。提供できること：（1）繰り返し作業の自動化設計。目的・範囲・合格条件・停止条件を先に切り、実装後に回帰確認まで残します。（2）Claude CodeやCodexなど、AIに実装を任せるときの指示の書き方、検品、失敗時の切り分け。（3）YouTubeとTikTokへの公式API投稿の仕組みづくり。ブラウザ自動操作とスクレイピングは対象外です。（4）鍵の扱い、公開事故、トークン期限など、自動化が止まりやすい箇所の点検。公開している道具の例：Autopilot Log（https://github.com/rimone0511/autopilot-log）。YouTube Data API v3 と TikTok Content Posting API のみを使い、投稿の門番は壊れても非公開側に倒れます。受けないこと：いいねやフォローの自動化、権利のない投稿代行、本人確認書類・口座・マイナンバーの代理入力、未確認のままの公開。進め方はテキスト中心です。根拠と反証を残し、公開スイッチは依頼者または本人の手に置きます。リモート可。週次の稼働時間は案件ごとに相談します。未確認の件数や年数は書きません。確認できた公開物だけを貼ります。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。英語の一次資料は必要なら要約して渡します。契約前に範囲外を一文で確定します。納期は着手前に合意します。作業の記録を残す。
```

### やってみたいこと（短文）

```
人が検品できる業務自動化（繰り返し作業の設計・合格条件・停止条件）。Claude Code / Codex での実装指示と検品。公式APIだけの投稿導線。ブラウザ自動操作・スクレイピング・未確認数字の公開はやりません。
```

### スキル chips (pick live matches only)

`Claude Code` · `Codex` · `Python` · `API連携` · `業務自動化` · `技術記事`

If a chip is missing from the DB: **skip**. Do not file 追加リクエスト this pass. 経験年数 = ledger or skip.

### ポートフォリオ rows

| Title (public) | URL |
|---|---|
| ユタラボ | `{{PORTFOLIO_URL}}` → https://yutalab.dev/ |
| Autopilot Log | `{{GITHUB_REPO_AUTOPILOT}}` → https://github.com/rimone0511/autopilot-log |

Do not claim TikTok posting from this repo is unattended.

---

## Sources (public)

- Signup UI: https://goworkship.com/signup (`SNSで登録` + FirebaseUI Google provider id)
- Login UI: https://goworkship.com/login (`SNSでログイン`; 採用担当者はこちら = close)
- Flow: https://goworkship.com/flow (this pack = STEP1–2 only)
- 新規登録: https://goworkship.com/help/how_to/44
- 気になる = エントリー: https://goworkship.com/help/how_to/72
- エントリー後: https://goworkship.com/help/how_to/77
- 自己紹介 / やってみたいこと / 職歴 / ポートフォリオ / スキル / 公開範囲 / 本名: `/help/edit_profile/52` `53` `75` `54` `56` `58` `69`
- 無料: https://goworkship.com/help/about_workship/41
- 国内住民票+本人名義口座（資格の引用。口座は今は開けない）: https://goworkship.com/help/about_workship/71
- STOP URLs: listed in [STOP.md](STOP.md)

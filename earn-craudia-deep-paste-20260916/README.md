# Deep CU paste — クラウディア（Craudia）worker profile

Pack date: 2026-09-16  
Public-page check: 2026-09-16（**公開 GET / 公式ヘルプのみ**。アカウント作成なし。ログイン Cookie なし。OAuth 未完走）  
Audience: Computer-use（CU）直列の **後続エージェント**、および人が貼る下書き  
Operator: 石田祐太 / Yuta Ishida (`rimone0511`)  
Mode: **DRAFT_ONLY**. このフォルダは手渡しパック。アカウントではない。KYC ではない。公開 GO ではない。応募ではない。スキル出品ではない。

対象 1 机（QUEUE Wave A。INDEX の CU 番号は兄弟索引を正とする）:

```
クラウディア（Craudia）ワーカー  = this pack, desk 1  / CU-09  / QUEUE A9
```

これは薄い CU-09 パック（`earn-timeticket-contra-craudia-handoff-20260916/09-craudia.md`）の **深掘り**。TimeTicket / Contra は入れない（兄弟 `earn-contra-timeticket-deep-paste-20260916/`）。本文を `earn-packs/craudia/` へ複製しない。

厚くした点:

- **Bio lengths** — フェンス内の文字数を測った。自己紹介の公式字数は公開 FAQ に無い → **needs_check**。**23 / 200 / 255 / 800** を用意し、画面カウンターで切る。
- **Skills vs スキル出品** — プロフィールの得意種別・スキル欄だけ。マイページ「スキルを出品する」（FAQ 175 / 出品ガイド）は **STOP**。タイトル 25 字・公開ボタンに入らない。
- **STOP-KYC** — マイページ設定 → 本人確認。顔付き公的書類 **+ 自撮り必須**（FAQ 93）。朝の本人へパスだけ。
- **No apply.** 参加申請（FAQ 89）・納品する・見積もり提案を送らない。
- **No off-platform pay.** FAQ 164 / ガイドライン / 規約第12条4–5。
- **Fees cited or needs_check.** 階段は公式「システム手数料について」本文のみ。創作しない。

これらのファイルは貼り付け文法である。Craudia / エムフロ / n8n / Google / xAI との雇用・提携ではない。

---

## Hard rules

- No secrets in these files or in git（実パスワード、API 鍵、身分証番号、OTP 数字、口座なし）。
- PLACEHOLDER のみ。ローカル台帳で置換。埋めた値をコミットしない。
- **MAIN Google only**（`{{GOOGLE_ACCOUNT_EMAIL}}` = `rimone0511@gmail.com`）。机専用メールを作らない。
- **Gmail OTP = parent**（Gmail MCP）。CU は `mail.google.com` を開かない。i2iID 認証メールも親 Gmail。
- **SMS OTP = user chat.** 推測しない。二台目の電話を使わない。電話認証（FAQ 156）が下書きを止めるときだけ。
- **STOP at KYC.** 書類 + **自撮り**。[STOP-KYC.md](STOP-KYC.md)。朝へパス。
- **Do not publish / apply / スキル出品.** 参加申請しない。スキルの **公開** ボタンを押さない。Craudia PRO に入らない。
- Press & Hold: 必ず **`holdDurationMs`**。[00-google-otp-hold.md](00-google-otp-hold.md)。reCAPTCHA が hold でないなら人待ち。
- **手数料％は公式の公開ページに出た文言だけ。** 出ていなければ `needs_check`。ブログ・記憶・他机の料率を転記しない。
- この markdown を書いているエージェントは **登録しない**。CU 直列だけが、これらの規則の下でブラウザに入力してよい。

## Files

| File | What it is |
|---|---|
| [CU-PROMPT.md](CU-PROMPT.md) | 後続 CU への貼りスタブ |
| [00-google-otp-hold.md](00-google-otp-hold.md) | MAIN Google、Gmail 親、SMS=user、`holdDurationMs` |
| [01-craudia.md](01-craudia.md) | CU-09 ワーカー。プロフィール + スキル欄。応募しない。出品しない |
| [STOP-KYC.md](STOP-KYC.md) | 本人確認（書類+自撮り）/ 口座 / 出金 |
| [HANDS-AND-TOS.md](HANDS-AND-TOS.md) | 直接取引 / 直接連絡 / 中抜き |
| [INDEX.md](INDEX.md) | このパック内の貼る順 |
| [METHOD.md](METHOD.md) | 観測方法と HTTP |

## Shared placeholders

Replace locally. Never commit filled values.

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
{{PHONE_E164}}
{{BIRTH_YEAR}}
{{BIRTH_MONTH}}
{{BIRTH_DAY}}
{{PHOTO_LOCAL_PATH}}
{{PORTFOLIO_URL}}
{{WEBSITE_URL}}
{{GITHUB_URL}}
{{GITHUB_REPO_AUTOPILOT}}
{{YEARS_AUTOMATION_PUBLIC}}
{{HOURLY_JPY}}
{{ONE_SPECIFIC_DETAIL}}
```

Suggested public URLs（すでに公開。机に打ってよい）:

- Site: `https://yutalab.dev/`
- GitHub: `https://github.com/rimone0511`
- Tooling example: `https://github.com/rimone0511/autopilot-log`

Do not type a real phone, ID number, or tax ID into git.

Public defaults（CU チャットに出してよい）:

| Token | Public default |
|---|---|
| `{{GOOGLE_ACCOUNT_EMAIL}}` / `{{EMAIL}}` | `rimone0511@gmail.com`（ログイン識別。受信箱の中身は秘密） |
| `{{DISPLAY_NAME}}` | `石田祐太` |
| `{{COUNTRY}}` | `Japan` |
| `{{TIMEZONE}}` | `Asia/Tokyo` |
| `{{PORTFOLIO_URL}}` / `{{WEBSITE_URL}}` | `https://yutalab.dev/` |
| `{{GITHUB_URL}}` | `https://github.com/rimone0511` |
| `{{GITHUB_REPO_AUTOPILOT}}` | `https://github.com/rimone0511/autopilot-log` |
| `{{HOURLY_JPY}}` | **empty** — 円額を創作しない |
| `{{YEARS_AUTOMATION_PUBLIC}}` | **empty** — 未確認なら空 |

## Signup URLs — confirmed vs guess

**Use confirmed URLs first.** Guess 行はプレースホルダ。発明した OAuth コールバックを打たない。`/signup` と `/app/signup` は this env **404**。

| Desk | Status | URL |
|---|---|---|
| Craudia home | confirmed 200 | https://www.craudia.com/ |
| Worker LP | confirmed 200 | https://www.craudia.com/worker |
| 会員登録（仮登録） | confirmed 200。Google ボタン `auth=3` 目視 | https://www.craudia.com/app/auth/register-temp |
| ログイン | confirmed 200（実体 `app.craudia.com/auth/login-form`） | https://www.craudia.com/login |
| FAQ 会員登録 | confirmed 200 | https://www.craudia.com/app/faq/contents/151 |
| 規約 | confirmed 200 | https://www.craudia.com/app/agreement |
| 手数料（クラウドソーシング） | confirmed 200 | https://www.craudia.com/app/guide/crowdsourcing-price |
| 手数料（スキル販売。出品しない） | confirmed 200 | https://www.craudia.com/app/guide/skill-price |
| 本人確認 FAQ | confirmed 200 | https://www.craudia.com/app/faq/contents/93 |
| 本人確認 UI | FAQ 156 が URL を出す。this env 未ログイン GET はトップへ。**開いて上げない** | https://www.craudia.com/mypage/setting/person |
| 出金 FAQ | confirmed 200。**開かない** | https://www.craudia.com/app/faq/contents/110 |

Reject lookalikes: `craudia.jp` 誤綴り、クライアント募集フォーム（`mypage/work/register`）、スキル出品（`mypage/services/add`）、Craudia PRO LP からの有料マッチング登録。

## Activity note

件数・GMV・「○万人」・PRO LP の「時給5,000円以上」例は活動証明に使わない。

| Desk | This pack | Public evidence 2026-09-16 |
|---|---|---|
| クラウディア | **alive**（`thin_site_skip: false`） | FAQ 151 / 103 / 93 / 72 / 164 / 89 / 175 / 39 が HTTP 200。手数料ガイドに階段。register-temp に Google ボタン |

## Seller one-liners

English: n8n / AI automation + operator docs. Official APIs only. No browser scraping. No engagement bots. Stay on Craudia for payment.

日本語: AI業務自動化と手順書。公式APIのみ。ブラウザ自動操作・いいね自動化はしない。やり取りと支払いはクラウディア内。公開は人が決める。

## Sibling packs（複製しない。あれば参照）

| Placeholder | Expected path |
|---|---|
| `{{QUEUE}}` | `earn-register-expand-20260916/QUEUE.md` |
| `{{CU_RUNBOOK}}` | `earn-cu-runbook-20260916/RUNBOOK.md` |
| `{{THIN_TT_CONTRA_CRAUDIA}}` | `earn-timeticket-contra-craudia-handoff-20260916/` |
| `{{DEEP_TT_CONTRA}}` | `earn-contra-timeticket-deep-paste-20260916/` |
| `{{KYC_MORNING}}` | `earn-kyc-morning-checklist-20260916/` |
| `{{MASTER_INDEX}}` | `earn-register-pack-master-index-20260916/` |

兄弟が無くても **このフォルダだけで CU-09 を走れる**。ライブフォームを正とする。

## What this pack will not do

- TimeTicket / Contra をこの直列に入れる
- Wave B 机を再開する
- **参加申請・納品・見積もり提案**
- **スキル出品・スキル公開**
- Craudia PRO / 有料オプションの購入
- 本人確認（書類+自撮り）・口座・出金
- 手数料％や時給円額の創作
- この authoring エージェントからの signup

## Verification (this PR)

Markdown handoff only. Python posting-gate tests are unchanged. No account was created from this authoring agent.

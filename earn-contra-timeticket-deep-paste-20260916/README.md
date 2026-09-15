# Deep CU paste — Contra Independent + TimeTicket host

Pack date: 2026-09-16  
Public-page check: 2026-09-16（**公開 GET / 公式ヘルプのみ**。アカウント作成なし。ログイン Cookie なし）  
Audience: Computer-use（CU）直列の **後続エージェント**、および人が貼る下書き  
Operator: 石田祐太 / Yuta Ishida (`rimone0511`)  
Mode: **DRAFT_ONLY**. このフォルダは手渡しパック。アカウントではない。KYC ではない。公開 GO ではない。Pro 課金ではない。

対象 2 机（QUEUE Wave A。INDEX の CU 番号は兄弟索引を正とする）:

```
TimeTicket（タイムチケット）ホスト  = this pack, desk 1  / CU-07  / QUEUE A7
Contra Independent / Share work     = this pack, desk 2  / CU-08  / QUEUE A8
```

これは薄い CU-07/08 パック（`earn-timeticket-contra-craudia-handoff-20260916/`）の **深掘り**。クラウディア（CU-09）は入れない。本文を `earn-packs/timeticket/` や `earn-packs/contra/` へ複製しない。

厚くした点:

- **Bio lengths** — フェンス内の文字数を測った。Contra About は公式 **400 character** 上限。TimeTicket 自己紹介の公式字数は公開ヘルプに無い → **200 / 想定255 / 800** を用意し、画面カウンターで切る。
- **Rate placeholders** — 円も USD も git に実額を書かない。下限・上限・手数料％は公式ページを **cited** するだけ。フォームが金額必須で台帳が空なら `rate_empty` で止める。
- **STOP-KYC** — TimeTicket `identifications/edit`。Contra Wallet → Add account → Persona。
- **No Pro upgrade** — Contra は **Free until a client**。Pricing の Pro は読んでも買わない。
- **Async ticket only** — TimeTicket は **通常チケット × メッセージ**。電話相談チケット・対面・電話・オンライン（Zoom）は付けない。

これらのファイルは貼り付け文法である。TimeTicket / Contra / n8n / Google / xAI との雇用・提携ではない。

---

## Hard rules

- No secrets in these files or in git（実パスワード、API 鍵、身分証番号、OTP 数字、口座なし）。
- PLACEHOLDER のみ。ローカル台帳で置換。埋めた値をコミットしない。
- **MAIN Google only**（`{{GOOGLE_ACCOUNT_EMAIL}}` = `rimone0511@gmail.com`）。机専用メールを作らない。
- **Gmail OTP = parent**（Gmail MCP）。CU は `mail.google.com` を開かない。
- **SMS OTP = user chat.** 推測しない。二台目の電話を使わない。
- **STOP at KYC.** [STOP-KYC.md](STOP-KYC.md)。
- **Do not publish.** TimeTicket の **発行完了** を押さない。Contra の Discoverable を意図してオンにしない。応募・invoice・payment link をこのフォルダから送らない。
- **No Contra Pro / Max.** カードを手数料対策で入れない。
- **Async ticket only** on TimeTicket. 電話相談チケットを作らない。
- Press & Hold: 必ず **`holdDurationMs`**。[00-google-otp-hold.md](00-google-otp-hold.md)。
- **手数料％は公式の公開ページに出た文言だけ。** 出ていなければ `needs_check`。ブログ・記憶・他机の料率を転記しない。
- この markdown を書いているエージェントは **登録しない**。CU 直列だけが、これらの規則の下でブラウザに入力してよい。

## Files

| File | What it is |
|---|---|
| [CU-PROMPT.md](CU-PROMPT.md) | 後続 CU への貼りスタブ |
| [00-google-otp-hold.md](00-google-otp-hold.md) | MAIN Google、Gmail 親、SMS=user、`holdDurationMs` |
| [01-timeticket.md](01-timeticket.md) | CU-07 ホスト。async メッセージ通常チケット下書き |
| [02-contra.md](02-contra.md) | CU-08 Independent / Share work。**Free**。Pro 禁止 |
| [STOP-KYC.md](STOP-KYC.md) | 身分証 / マイナ裏面 / Persona / 口座 |
| [HANDS-AND-TOS.md](HANDS-AND-TOS.md) | 中抜き / 直接取引 / Contra stay-on-platform |
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
{{TICKET_PRICE_JPY}}
{{HOURLY_USD}}
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
| `{{DISPLAY_NAME}}` | TimeTicket: `石田祐太`。Contra: `Yuta Ishida` |
| `{{COUNTRY}}` | `Japan` |
| `{{TIMEZONE}}` | `Asia/Tokyo` |
| `{{PORTFOLIO_URL}}` / `{{WEBSITE_URL}}` | `https://yutalab.dev/` |
| `{{GITHUB_URL}}` | `https://github.com/rimone0511` |
| `{{GITHUB_REPO_AUTOPILOT}}` | `https://github.com/rimone0511/autopilot-log` |
| `{{TICKET_PRICE_JPY}}` | **empty** — 円額を創作しない |
| `{{HOURLY_USD}}` | **empty** — USD 額を創作しない |

## Signup URLs — confirmed vs guess

**Use confirmed URLs first.** Guess 行はプレースホルダ。発明した OAuth コールバックを打たない。

| Desk | Status | URL |
|---|---|---|
| TimeTicket home | confirmed（WebFetch 本文。this env curl は HTTP 202 空） | https://www.timeticket.jp/ |
| TimeTicket カテゴリ | confirmed（WebFetch: `IT/プログラミング` 実在） | https://www.timeticket.jp/categories/ |
| TimeTicket 登録 | confirmed URL。this env GET **202 空** → 画面を正とする | https://www.timeticket.jp/users/sign_up |
| TimeTicket ログイン | confirmed URL。this env GET **202 空** | https://www.timeticket.jp/users/sign_in |
| TimeTicket 規約 | confirmed（WebFetch: 第8条 プロフィール既定公開） | https://www.timeticket.jp/terms |
| TimeTicket 本人確認 UI | confirmed URL（ヘルプ 19398）。this env GET **202 空**（未ログイン） | https://www.timeticket.jp/users/identifications/edit |
| TimeTicket 出金 | confirmed URL（ヘルプ 19376）。**開かない** | https://www.timeticket.jp/payouts/new |
| Contra home | confirmed 200 | https://contra.com/ |
| Contra Independent | confirmed 200 | https://contra.com/how-it-works/independents |
| Contra pricing | confirmed 200 | https://contra.com/pricing |
| Contra terms | confirmed 200 | https://contra.com/policies/terms |
| Contra wallet（公開シェル） | confirmed 200。**中に入って Add account しない** | https://contra.com/independent/wallet |

Reject lookalikes: `timeticket.com` 誤綴り、`contra.io`、Hire ワークスペースを Independent の代わりにする。

## Activity note

件数・GMV・「○万人」・`$100K+ earned` テスティモニアルは活動証明に使わない。

| Desk | This pack | Public evidence 2026-09-16 |
|---|---|---|
| TimeTicket | **alive**（`thin_site_skip: false`） | ヘルプ 19374 / 19386 / 19398 / 19400 / 19461 / 113228 が HTTP 200。WebFetch のトップに 2026/09/09〜09/16 の売上ランキング。カテゴリに `IT/プログラミング` |
| Contra | **alive**（`thin_site_skip: false`） | pricing / independents / terms / onboarding / bios / identity / paid-projects / wallet ヘルプが HTTP 200 |

## Seller one-liners

English: n8n / AI automation + operator docs. Official APIs only. No browser scraping. No engagement bots. Stay on Contra for payment.

日本語: AI業務自動化と手順書。公式APIのみ。ブラウザ自動操作・いいね自動化はしない。タイムチケットはメッセージ（非同期）のみ。公開は人が決める。

## Sibling packs（複製しない。あれば参照）

| Placeholder | Expected path |
|---|---|
| `{{QUEUE}}` | `earn-register-expand-20260916/QUEUE.md` |
| `{{CU_RUNBOOK}}` | `earn-cu-runbook-20260916/RUNBOOK.md` |
| `{{THIN_TT_CONTRA}}` | `earn-timeticket-contra-craudia-handoff-20260916/` |
| `{{EN_PROPOSAL}}` | `earn-en-proposal-drafts-20260916/`（Contra 応募文。**このフォルダからは送らない**） |
| `{{KYC_MORNING}}` | `earn-kyc-morning-checklist-20260916/` |
| `{{MASTER_INDEX}}` | `earn-register-pack-master-index-20260916/` |

兄弟が無くても **このフォルダだけで 2 机を走れる**。ライブフォームを正とする。

## What this pack will not do

- CU-09 クラウディアをこの直列に入れる
- Wave B 机を再開する
- TimeTicket の **電話相談チケット** / 対面 / 電話 / Zoom 付き通常チケット
- Contra Pro / Max の購入、Discover 課金
- 本人確認・Persona・口座・出金
- 提案送信・案件応募・チケット発行完了
- 手数料％や時給・チケット円額の創作
- この authoring エージェントからの signup

## Verification (this PR)

Markdown handoff only. Python posting-gate tests are unchanged. No account was created from this authoring agent.

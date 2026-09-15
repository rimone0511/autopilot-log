# CU-08 — Contra Independent / Share work

Desk: Contra  
Role: **Independent / Share work**。Hire 側に入らない  
Official: https://contra.com/  
CU serial: **CU-08**（QUEUE **A8**）  
Checked: 2026-09-16（公開 HTML / 公式ヘルプ HTTP 200。**登録していない**）  
Mode: **DRAFT_ONLY** — fill, save, **never publish / never Pro**  
Language: **English** on the Independent page  
Google: **PREFER_GOOGLE**  
OTP: Rare with Google. Else **Gmail parent**  
plan: **Free** until a client. **No Pro / Max**  
`thin_site_skip: false`

---

## 0. How far to go (then stop)

1. https://contra.com/ — Continue with Google as MAIN。
2. **What brings you to Contra?** → **Share work**（Independent）。Hire creative talent は選ばない。
3. プロフィール写真: `{{PHOTO_LOCAL_PATH}}`（ローカル。git に置かない）。無ければスキップ可ならスキップ。
4. One-liner: 下記 short（公式は brief。字数数字なし → 画面で切る）。
5. Create account: **Free**。**Contra Pro を契約しない**。公式: sign up for Pro *or* proceed with a free account。Pricing は Pro `$29 / month` または `$199 / year`。このパックは買わない。
6. Topics: 自動化・API・documentation に近い公式トピックだけ。無いものは作らない。
7. About / bio: 公式 **400-character limit**。200 か 400 を貼る。800 は置かない。
8. Cover、公開リポジトリ URL、rate は **空または `{{HOURLY_USD}}`**。Discoverable **off**。
9. **Verify identity & set up your wallet は開かない。** Persona に入ったら閉じて朝メモ。
10. 案件応募・invoice・payment link はしない（応募文は sibling `earn-en-proposal-drafts-20260916/`）。

Feed に Work を **投稿** するのは公開に近い。プロフィールに公開 URL を足すだけにする。4 pieces of work が必須で投稿しか無いなら、公開 GitHub / yutalab を case study 下書きまでにして **Publish to feed はしない**。詰まればプロフィール途中で完了。

Timebox: 15–25 minutes. Stuck > 10 minutes: park.

---

## 1. URLs

### Confirmed (use these)

| What | URL |
|---|---|
| Home | https://contra.com/ |
| Independents | https://contra.com/how-it-works/independents |
| Pricing（読む。買わない） | https://contra.com/pricing |
| Terms | https://contra.com/policies/terms |
| Onboarding Independent | https://help.contra.com/en/articles/9322381-onboarding-and-completing-your-profile |
| One-liner の書き方 | https://help.contra.com/en/articles/9322675-writing-your-one-liner-on-contra |
| Bios（**400-character limit**） | https://help.contra.com/en/articles/9322626-bios-on-contra |
| Identity / Persona | https://help.contra.com/en/articles/9322955-how-to-verify-your-identity-on-contra |
| Wallet 手順（開いて Add しない） | https://help.contra.com/en/articles/9322950-your-contra-wallet |
| Paid projects（請求しない） | https://help.contra.com/en/articles/9322763-paid-projects |
| Wallet シェル（公開 GET 200） | https://contra.com/independent/wallet |

### Guess only

```
{{URL_GUESS_CONTRA_PROFILE_EDIT}}   # ログイン後 Profile。ライブメニューを正とする
{{SIGNUP_URL_GUESS_CONTRA_HIRE}}    # Hire — 選ばない
```

---

## 2. Google MAIN notes (this desk)

公開観測:

- Independents / pricing は Sign up / Log in。
- 公開 wallet シェルに `googleSigninClientId`（2026-09-16 GET 200）。
- Onboarding ヘルプ（2026-01-27）: workspace = Share work vs Hire creative talent。

方針:

1. https://contra.com/ — **Continue with Google** as `rimone0511@gmail.com`
2. Share work。Hire に落ちたら戻す。Agency を別人格で作らない。
3. Free。Get Pro / upgrade を押さない。カード壁 = `card_wall`。
4. フォールバック: 同じ MAIN メール。OTP は親 Gmail。
5. **この authoring セッションでは Create account を押さない。** CU 直列だけ。
6. Already a member: ログイン。二件目を作らない（Terms: multiple accounts to dodge rate limits = violation）。

---

## 3. Profile paste fields (EN)

出典: オンボーディングヘルプ + Bios ヘルプ。ライブフォームを正とする。

| 画面の項目 | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| Workspace | **Share work** | 必須 | Independent page |
| Google | `{{GOOGLE_ACCOUNT_EMAIL}}` | 必須 | PREFER_GOOGLE |
| Plan | **Free** / skip Pro | 必須 | 「Free until client」。Pro $29/mo または $199/yr は **買わない** |
| Display name | `{{DISPLAY_NAME}}` | 必須 | 推奨: `Yuta Ishida` |
| Photo | `{{PHOTO_LOCAL_PATH}}` | 高 | 身分証禁止 |
| One-liner | 下記 short | 必須 | 公式例は短い職種文。字数 **needs_check** |
| About / bio | 下記 **400**（または短い欄なら **200**） | 高 | 公式 **400-character limit**（cited） |
| Location | Japan / `{{PREFECTURE}}` 相当 | 高 | 番地なし |
| Topics | Automation, APIs, documentation, 画面の最寄り | 高 | 無いトピックを作らない |
| Cover | 公開サイトのスクショ（秘密なし）またはスキップ | 任意 | ID 写真不可 |
| Work samples | 公開 URL のみ。feed 投稿しない | 任意〜高 | `{{PORTFOLIO_URL}}`, `{{GITHUB_REPO_AUTOPILOT}}` |
| Hourly rate | `{{HOURLY_USD}}` | 完成チェック用 | **git に実額を書かない**。空で保存できるなら空。必須で台帳が空なら `rate_empty` |
| Social | `{{PORTFOLIO_URL}}` と `{{GITHUB_URL}}` | 高 | LinkedIn を新規投稿しない。既存 URL なら可 |
| Discoverable | **off** | 必須（あれば） | 完成チェックの最後が wallet。埋めない |
| Wallet / Add account | やらない | STOP | Persona。発行国は居住国ではない |
| Expert verification | やらない | STOP | |
| Apply to opportunity | やらない | STOP | 兄弟 EN pack |

---

## 4. Paste — bio lengths（測済み）

### One-liner A（63 字。公式例に近い短さ）

公式ガイド: brief elevator pitch。字数数字なし。例: "Creative Graphic Designer Specializing in Brand Identity"。

```
Japan-based: n8n and official-API automation plus operator docs
```

### One-liner B（68 字。価値が画面に収まるとき）

```
Official-API automation plus operator docs a non-engineer can follow
```

画面が更に短いときは A を切る。連絡先を足さない。

### About 200（短い Description 欄）

公式上限は 400。200 は短い欄・余白用。

```
I am Yuta Ishida (Japan). I replace copy-paste with n8n or official-API workflows plus operator docs. Notes: https://yutalab.dev/ I do not scrape or take Contra work off-platform. Async in Asia/Tokyo.
```

### About 400（公式上限。Bios ヘルプ cited）

https://help.contra.com/en/articles/9322626-bios-on-contra — “Please note that there is a 400-character limit.”

```
I am Yuta Ishida, a Japan-based independent. I help small teams replace copy-paste with an n8n or official-API workflow plus docs a non-engineer can follow. Public notes: https://yutalab.dev/ Tool: Autopilot Log (YouTube Data API v3 + TikTok Content Posting API, fail-closed gate). I do not scrape, fake engagement, or move Contra-originated work off Contra. Async text in Asia/Tokyo. Scope is first.
```

**800 字の About は置かない。** 公式 400 を超える。

`{{TIMEZONE}}` を画面が別欄で求めるときは `Asia/Tokyo`。git に住所を足さない。

### Work sample titles (if the form needs one line)

| Sample | URL | Title line |
|---|---|---|
| 1 | `{{PORTFOLIO_URL}}` | Operator-facing notes on AI automation (Japanese, public) |
| 2 | `{{GITHUB_REPO_AUTOPILOT}}` | Autopilot Log — YouTube Data API v3 + TikTok Content Posting API, fail-closed gate |

Do not upload private videos, client files, or ID. Do not Publish to feed.

---

## 5. Fees and rate placeholders — official public pages only

時給欄に入れるのは **`{{HOURLY_USD}}` だけ**。業界平均をこのパックが決めてはいけない。

| Claim | Status | Source | Quote / note |
|---|---|---|---|
| Independent プロフィールは無料 | **cited** | https://contra.com/how-it-works/independents | “Your Contra profile is free and doesn’t cost you a dime!” / “Join Contra for free” on pricing |
| Free のまま進める | **cited** | Onboarding 2026-01-27 https://help.contra.com/en/articles/9322381-onboarding-and-completing-your-profile | “You can sign up for Contra Pro or proceed with a free account.” **proceed with free** |
| Pro の表示価格 | **cited** | https://contra.com/pricing | `$29 / month` または `$199 / year (save 43%)`。**買わない** |
| Commission-free for creatives | **cited** | pricing / independents | “Contra is always commission-free for all creatives.” 同時に Free では client payment fees あり |
| Non-Pro プロジェクト手数料表 | **cited but unused** | Paid projects 2026-05-12 https://help.contra.com/en/articles/9322763-paid-projects | $1–199 → $2。$200–499 → $5。$500–999 → $10。> $1000 → $29。**請求しないので「今払う額」にしない** |
| 時給の実額 | **placeholder** | Onboarding Step 3 “Add your rate” | `{{HOURLY_USD}}`。空で保存。必須で台帳が空なら **`rate_empty`**（Discover 完成のために数字を創作しない） |
| Processing fees（第三者） | **cited** | pricing 脚注 | “This does not include payment processing fees charged by third-party providers.” 数字は pricing を再読。創作しない |

Do not buy Pro to waive fees. Do not paste the paid-projects table into the About field.

---

## 6. Explicit do-not (this desk)

- Hire creative talent / client workspace を Independent の代わりにする
- Get Pro / Max / カード入力
- Wallet → Add account / Persona / Airwallex
- Discoverable を意図してオン
- Publish to feed
- Apply / invoice / payment link（このフォルダ）
- 400 字を超える About
- `{{HOURLY_USD}}` を数字で埋めてコミットすること
- Contra 起点の仕事をメールや銀行へ逃がす文

---

## 7. What success looks like **before stop**

| Outcome | Meaning |
|---|---|
| `done-draft` | MAIN Google。Share work。Free。one-liner + About ≤400。公開 URL。Discoverable off。wallet なし。Pro なし |
| `already_member_draft` | 同じメールで既存。プロフィール確認。Pro に上げない |
| `kyc_wait` | Wallet / Persona。閉じて朝へ |
| `rate_empty` | 時給必須で台帳が空。USD を創作せず停止 |
| `card_wall` | Pro がカードを要求。閉じる |
| `otp_missing` | メール確認なし |

```
desk: Contra
pack: earn-contra-timeticket-deep-paste-20260916/02-contra.md
auth: google-main | email-same-mailbox | already_member | blocked
otp: gmail-parent | sms-chat | none | otp_missing | sms_wait_user
kyc: none | wait-morning + wallet_add_account | persona
draft_profile: yes/no
ticket_or_page: contra-free-independent
async_only: n/a
pro_upgrade: no
publish: no
apply: no
rate: empty | placeholder-from-ledger | rate_empty
next: stop
```

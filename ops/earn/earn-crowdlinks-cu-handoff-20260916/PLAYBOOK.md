> DRAFT_ONLY CU handoff. NO secrets. NO invented credentials. NO live signup from this authoring agent.  
> Human / CU paste only. Live form wins.  
> Desk: クラウドリンクス / CrowdLinks（**B04** / QUEUE **Wave B** / **CU-14**).  
> Auth: **MAIN Google** on public https://crowdlinks.jp/worker/signup/ (`Googleで登録する` at click-time).  
> This pass: **free-member profile draft only**. **Do not 応募 / 話を聞きたい / マッチング報告.**  
> Stop: [STOP.md](STOP.md) (apply + KYC + phone-as-ID + paid plan). Fields: [FIELD-MAP.md](FIELD-MAP.md). Session box: [STATUS.md](STATUS.md).

# PLAYBOOK — CrowdLinks worker signup (B04)

| Key | Value |
|---|---|
| Desk | クラウドリンクス / CrowdLinks **worker**. Not `/client/` 契約企業 |
| IDs | **B04** · QUEUE **Wave B** · **CU-14** |
| Not | CrowdWorks (`crowdworks.jp`) 総合クラウドソーシング. Do not mix |
| Mode | **DRAFT_ONLY** |
| Language | **日本語** |
| Google | **PREFER_GOOGLE** — MAIN only. Public signup JS: **Googleで登録する**. FAQ: Google認証は **別アカウントへ付け替え不可** |
| Email fallback | Same MAIN mailbox (`メールアドレスで登録する`). Password **not** in git. OTP = parent Gmail |
| Plan | **無料会員 only**. FAQ: worker use is free; listed pay is not commission-cut. **No yen / % invented.** Do not buy 有料会員 |
| This pass | Account (if needed) → プロフィール下書き保存. Stop before 応募 |
| Hard no | **応募フォームへ** · **話を聞きたい** · スカウト返信 · マッチング報告 · 有料会員化 · 追加書類 · 口座 · 電話を本人確認に使う |
| Activity gate | **needs_check** — observed evidence only. See [STATUS.md](STATUS.md). Do not call the desk `alive` |
| `thin_site_skip` | **false** (public pages live this GET) |
| Authoring session | Public GET / help / TOS only. **Did not create an account** |

Sibling packs (bodies **not** required to open this runner; n8n paste fences live in [FIELD-MAP.md](FIELD-MAP.md)):

| Sibling | Path / PR |
|---|---|
| Thick CU-14 | `earn-waveb-cu-handoff-batch2-20260916/02-crowdlinks.md` ([#30](https://github.com/rimone0511/autopilot-log/pull/30)) |
| Thin Week2 | `earn-register-packs-jp-20260916/04-crowdlinks.md` ([#3](https://github.com/rimone0511/autopilot-log/pull/3)) |
| Gate record (JP Wave B) | `earn-activity-gate-waveB-20260916/records/04-crowdlinks.md` ([#12](https://github.com/rimone0511/autopilot-log/pull/12)) **needs_check** |
| Gate note (batch1) | `ops/earn/waveb-activity-gate-batch1-20260916/b04-crowdlinks.md` ([#62](https://github.com/rimone0511/autopilot-log/pull/62)) **needs_check** |

This playbook is the **step order**. Placeholders stay empty of secrets in git.

---

## Hard rules (read before the first click)

1. **MAIN Google.** Open [crowdlinks.jp/worker/signup/](https://crowdlinks.jp/worker/signup/). Click the control that **says Googleで登録する**. Use `{{GOOGLE_ACCOUNT_EMAIL}}` — MAIN mailbox only. Facebook as a **new** identity: no. FAQ: Google認証を別アカウントに変更することは現状できかねます.
2. **Email is the same person.** If the Google button is missing, unlabeled, or OAuth fails: same-page **メールアドレスで登録する** `{{EMAIL}}` = MAIN mailbox, password `{{PASSWORD_DO_NOT_STORE}}`. Never commit it. Confirm mail stays in **parent Gmail**. Do not paste codes into git.
3. **Worker only.** Stay on `crowdlinks.jp/worker/`. Close [crowdlinks.jp/client/](https://crowdlinks.jp/client/) and company tools.
4. **無料会員 only.** User FAQ says worker use is free and listed 報酬額 is not commission-cut. TOS defines 有料会員 with **no yen table** on pages this GET opened. **Do not invent 円 or 手数料％. Do not buy.**
5. **DRAFT_ONLY this pass.** Fill キャリアの概要 / 課題解決できること / 経歴・実績 (1+) / スキルタグ. Save. Do **not** 応募.
6. **TOS 2-year gate.** 無料会員条件 includes プロフィール上に記載する業務について **実務経験が2年以上**. If `{{YEARS_AUTOMATION_PUBLIC}}` is empty, **do not invent years** — skip the chip / park this desk. Do not pick **2年以上** to satisfy the rule.
7. **Real name + 副業.** FAQ: 本名は必須ではないが推奨. TOS: 自己の所属する組織体の規則に反した行為をしていないこと. Keep visibility **クラウドリンクス内**. Do not 一般公開. Use 企業ブロック for `{{BLOCK_COMPANY_NAMES}}` (names stay off git). See caveats below.
8. **STOP before KYC / phone-as-ID / bank.** TOS 第3条4 追加の書類等の提出, 第4条 有料会員審査, 口座, マイナンバー — close. Phone in アカウント設定 is **not** a reason to start SMS. See [STOP.md](STOP.md).
9. **No credentials in git.** OTP, passwords, backup codes, bank digits, My Number, government ID, CSRF, reCAPTCHA tokens, AWS signed asset URLs — none of those belong in this repo.

Already a member on MAIN: **ログイン** ([/worker/login/](https://crowdlinks.jp/worker/login/) **Googleでログイン**, or same mailbox). Do not open a second account (help: アカウントが二重). Outcome `already_member_draft`.

---

## Real-name / 副業 caveats (cite, not a procedure)

CrowdLinks is a **副業マッチング** desk. Official pages say all of the following. CU does **not** decide employment-rule compliance.

| Caveat | Official cite | This pass |
|---|---|---|
| 本名は必須ではないが推奨。非本名だとマッチングしづらい傾向 | [User FAQ](https://help.crowdlinks.jp/0029649d31534622a6d95ffe53df18dd) | Paste `{{LEGAL_NAME_KANJI}}` if the human already chose 本名. Do **not** invent a 通称 to “hide” 副業 |
| 所属組織の規則に反した行為をしていないこと | TOS 第3条2(9) · [案件応募ガイドライン](https://help.crowdlinks.jp/entry_guidelines) | If side-job is not allowed at the current org, **park**. This pack does not register around a ban |
| プロフィール公開範囲: 一般公開 / クラウドリンクス内 / 限定公開 | Same FAQ | **クラウドリンクス内**. Not 一般公開 |
| 特定企業をブロックできる（正式名称、株式会社を含む） | [企業ブロック](https://help.crowdlinks.jp/corporate_block) | Optional `{{BLOCK_COMPANY_NAMES}}`. Real names **off git** |
| 社員が個人契約するのは可。企業間契約はお断り | User FAQ | Do not register as a company team. Do not 法人契約 this pass |
| クライアント向け文言に「実名登録・現職記載」がある | [client LP](https://crowdlinks.jp/client/) (marketing, not worker FAQ) | Treat 現職 as **sensitive**. Skip current-employer name unless the ledger already marks it public |

Do not write “副業OKです” into the bio. Do not list a current employer to look more ハイクラス.

---

## Step order

Live wizard order wins if it differs. Timebox: 15–25 minutes. Stuck > 10 minutes on one modal: park and write [STATUS.md](STATUS.md).

### A. Create or open the worker account

Public GET 2026-09-16 JST (no POST): `/worker/signup/` title **新規登録【クラウドリンクス】**. Static HTML is a Next.js loader — **Google の文字列は静的HTMLに無い**. Signup chunk `signup-654dee2220da40e7.js` (this GET) includes:

- **Googleで登録する** (`alt:"google"`)
- **Facebookで登録する** (`alt:"facebook"`) — do **not** use as a new identity
- **メールアドレスで登録する** / placeholder **メールアドレスを入力**
- 利用規約 (`/worker/terms/`) および 個人情報の取り扱い (`https://crowdworks.co.jp/privacy_policy/01/`) について同意します
- Submit **同意して会員登録する** (email path)
- すでに登録済みの方は **ログイン**
- Password regex copy: **半角の英字、数字、記号を含む8文字以上**

Login chunk `login-d30fd72bc87effc8.js`: **Googleでログイン** / **Facebookでログイン** / メールアドレス / パスワード.

| # | Do | Do not |
|---|---|---|
| 1 | Open https://crowdlinks.jp/worker/signup/ (existing member: https://crowdlinks.jp/worker/login/) | `/client/`, CrowdWorks.jp, company 採用ツール |
| 2 | **Googleで登録する**. MAIN `{{GOOGLE_ACCOUNT_EMAIL}}` | Facebook / 新規Gmail. Guest |
| 3 | OAuth consent: basic profile / email. Deny Gmail-read-all / Drive / Contacts dump | Extra scopes “to finish signup” |
| 4 | Fallback: **メールアドレスで登録する** `{{EMAIL}}` (same MAIN), password `{{PASSWORD_DO_NOT_STORE}}`, human reads 同意, **同意して会員登録する** | New mailbox. Password in git. Skip 同意 without the human reading |
| 5 | OTP / confirm mail = **parent Gmail**. Resend at most once | Paste OTP into git / STATUS |
| 6 | Phone / SMS: **not** on public signup JS this GET. If it appears, see [STOP.md](STOP.md) | Invent `{{PHONE}}`. Start carrier KYC |
| 7 | Role stays **ワーカー**. If a 契約企業 wizard appears, back out | `/client/` 企業登録 |
| 8 | TOS eligibility cite (not a form): 満18歳, 学生でない, 記載業務の実務経験2年以上. Empty years → **park** | Invent 2年. Register a team |

Account exists after a typical confirm. That is **not** permission to 応募. Stop is still before apply and KYC.

Agent does **not** tick 利用規約 for the user in the authoring session. Live CU: the **human** reads, then the runner may tick if the human already said GO for this desk.

### B. Fill the profile (draft — this pass ends here)

Help path: マイページ → 各項目の鉛筆. Sample field names: [プロフィール記入サンプル](https://help.crowdlinks.jp/guide/resume-sample). Save controls: live **保存する**. [FIELD-MAP.md](FIELD-MAP.md).

| # | Do | Do not |
|---|---|---|
| 1 | 氏名 = `{{LEGAL_NAME_KANJI}}` from ledger. FAQ 本名推奨 | Brand-only name invented to hide 副業 |
| 2 | キャリアの概要・略歴: paste **n8n 200** from FIELD-MAP. URL `https://crowdlinks.jp/worker/profiles/edit/self_introduction/` | Client names / confidential case detail. Unverified 〇件 |
| 3 | 課題解決できること: paste **capability** or **n8n 800** if the box is long. URL `.../edit/capability/` | Promise 応募 |
| 4 | 経歴・実績: **1つ以上必須** (FAQ). Public facts only. Empty years → do not invent tenure | Fake 2年 to pass TOS |
| 5 | スキルタグ: nearest **existing** chips only (n8n / 業務自動化 / Python / API / Claude Code / Codex if listed). Help years: 1年未満 / 1年以上 / 2年以上 / 3〜5年 / 5年以上. Ledger years or **skip the chip** | Invent a tag. Pick **2年以上** with empty ledger |
| 6 | ポートフォリオ: public URLs `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}` | Private repos. Login-walled demos |
| 7 | 公開範囲: person icon. **クラウドリンクス内で公開**. Not 一般公開 | Hunt 一般公開 “for SEO” |
| 8 | 企業ブロック: optional. Names off git | Commit employer legal names |
| 9 | 顔写真 `{{PHOTO_LOCAL_PATH}}` optional. Not an ID. Help: `.../profiles/edit/base/` | Passport / license / selfie-for-KYC |
| 10 | 希望単価: `{{HOURLY_YEN_DRAFT}}` or empty. If required and ledger empty → `rate_empty` | Invent 円 |
| 11 | 電話: skip unless **draft save** blocks. Then user-chat wait. If ID appears → KYC STOP | Fill アカウント設定 連絡先 “to be complete” |

希望職種 / ワークスタイル: **needs_check** (not labeled on the official sample this GET). If the live wizard shows them, pick existing chips only (エンジニア / 業務自動化 / リモート). Do not invent labels.

### C. Stop (do not continue into apply)

Do **not**:

- Press **応募フォームへ** (current user FAQ + sampled project HTML this GET)
- Press **話を聞きたい** (older [faq-worker](https://help.crowdlinks.jp/faq-worker) wording — treat as the same stop)
- Reply to スカウト / pitch in メッセージ
- マッチング報告 / 「報告する」
- 有料会員化 / 規約第4条の追加書類
- 口座 / マイナンバー / 身分証
- Start SMS to “finish profile”

Write the success line. Stop.

---

## Fees (cite only — do not pay, do not invent 円 / %)

| Claim | Status | Source |
|---|---|---|
| Worker use is free（企業から利用料） | **cited, qualitative** | [User FAQ](https://help.crowdlinks.jp/0029649d31534622a6d95ffe53df18dd) |
| 掲載報酬額から手数料は引かれない（直接契約） | **cited, qualitative** | Same FAQ. **No ％ on the page → do not invent one** |
| 無料会員 / 有料会員 | **cited, unused** | [TOS](https://crowdlinks.jp/terms) 第2条・第3条・第4条. **No yen table this GET** |
| Hourly 円 | **placeholder** | `{{HOURLY_YEN_DRAFT}}` only. Empty save, else ledger, else `rate_empty` |
| Sitemap 299 `/projects/{id}` locs | **not GMV** | Count is not traffic. Do not paste as volume |

---

## Activity gate (observed only — this GET)

Do **not** invent open-job volume, 会員数, or 手数料.

What this authoring GET actually saw (logged out, no POST):

- `/worker/projects/` 200, title プロジェクト一覧. Filters in JS: **募集中のみ表示 / 職種 / 稼働時間 / リモート可否 / おすすめ順 / 新着順**. Next `pageProps` **empty**. **No cards.**
- `/projects` 200. Listing shell; not used as a live board.
- Sitemap 200: **299** `/projects/{id}` locs, **0** `<lastmod>`.
- Sampled public project HTML (titles + embedded dates only):

| Title (trimmed) | publishedDateTime | publishedEndDate |
|---|---|---|
| （ID1056）SharePoint社内ポータルのUI/UX設計・実装パートナー | 2026-05-21T01:46:09.004Z | 2026-06-19 |
| （ID1055）急成長BPOのBPR・マニュアル整備PJリーダー | 2026-05-21T01:46:01.747Z | 2026-06-19 |
| 社長秘書募集！【代表直下】経営を支える秘書・バックオフィス募集 | 2026-05-19T06:53:18.737Z | 2026-06-17 |

Those `publishedEndDate` values are **already past** on this observation date. HTML also contains `X-Amz-Date=20260915T210830Z` (and nearby). That is an **AWS signature clock**, not a job date.

Help center **is** recently touched (FAQ article timestamps **2026/8/3**). Site maintenance ≠ open-job recency.

**Gate stays `needs_check`.** Not `alive`. Not `dead`. Not `thin`. Do not 応募 to “check if the board is live.”

---

## Explicit do-not

- `/client/` 契約企業 workspace
- CrowdWorks.jp by mistake
- New Facebook identity
- Second CrowdLinks account
- **応募フォームへ** / **話を聞きたい** / スカウト返信 / マッチング報告
- 有料会員化 / 追加書類 / 身分証 / 口座 / マイナンバー
- Invent `{{HOURLY_YEN_DRAFT}}`, worker 手数料％, 会員数, or GMV
- Invent 実務経験2年 / スキル **2年以上**
- 一般公開 the profile
- That Autopilot Log posts TikTok unattended (inbox upload is the default; direct post is gated)
- Browser automation / scraper as a CrowdLinks applicant bot
- This authoring agent POSTing `/worker/signup/`

---

## Success line (secret-free)

Valid outcomes: `done-draft` | `already_member_draft` | `kyc_wait` | `apply_stop` | `sms_wait_user` | `no_draft_path` | `otp_missing` | `oauth_overreach` | `rate_empty` | `google_icon_missing` | `years_empty_park`.

Not success: “応募した,” “話を聞きたい,” “スカウト返信,” “有料会員,” “口座登録,” “書類提出.”

```
desk: CrowdLinks
pack: ops/earn/earn-crowdlinks-cu-handoff-20260916/
ids: B04 / QUEUE-Wave-B / CU-14
auth: google-main | email-same-mailbox | already_member | blocked | google_icon_missing
otp: gmail-parent | sms-chat | none | otp_missing | sms_wait_user
kyc: none | wait-morning + extra_docs | paid_review | bank | photo_id
draft_profile: yes/no
entry: no
scout_reply: no
matching_report: no
publish: no
visibility: crowdlinks-internal | unknown
plan: free
paid: no
bank: no
phone: skipped | sms_wait_user | blocked
rate: empty | placeholder-from-ledger | rate_empty
years: empty | ledger | years_empty_park
next: stop
```

Copy the same keys into [STATUS.md](STATUS.md) after a live run. Do not put OTP digits, passwords, ID numbers, a live phone, or a bank amount there.

---

## URLs (public; re-open before CU)

| What | URL |
|---|---|
| Marketing home | https://start.crowdlinks.jp/ (`crowdlinks.jp/` 302 → here) |
| Worker signup (this pack) | https://crowdlinks.jp/worker/signup/ |
| Worker login | https://crowdlinks.jp/worker/login/ (`/login/` → here) |
| Worker listing (do not 応募) | https://crowdlinks.jp/worker/projects/ |
| Older listing shell | https://crowdlinks.jp/projects |
| Help index | https://help.crowdlinks.jp/ |
| User FAQ | https://help.crowdlinks.jp/0029649d31534622a6d95ffe53df18dd |
| User FAQ (alt slug) | https://help.crowdlinks.jp/faq-worker |
| ご利用ガイド | https://help.crowdlinks.jp/guide |
| プロフィール記入サンプル | https://help.crowdlinks.jp/guide/resume-sample |
| スキルタグ | https://help.crowdlinks.jp/642ef850db334df8a4ee93a2f330a09a |
| 企業ブロック | https://help.crowdlinks.jp/corporate_block |
| プロフィール写真 / 氏名 | https://help.crowdlinks.jp/15c33f48ad3041ce9a0975ba863b6c32 |
| 電話・メール変更（STOP unless draft-blocked） | https://help.crowdlinks.jp/change-mail-tel |
| 案件応募ガイドライン **STOP apply** | https://help.crowdlinks.jp/entry_guidelines |
| TOS | https://crowdlinks.jp/terms |
| Worker TOS (signup link) | https://crowdlinks.jp/worker/terms/ |
| Privacy (signup link) | https://crowdworks.co.jp/privacy_policy/01/ |
| Profile: 氏名 / 写真 | https://crowdlinks.jp/worker/profiles/edit/base/ |
| Profile: キャリアの概要 | https://crowdlinks.jp/worker/profiles/edit/self_introduction/ |
| Profile: 課題解決できること | https://crowdlinks.jp/worker/profiles/edit/capability/ |
| Profile: スキルタグ | https://crowdlinks.jp/worker/profiles/edit/skill_tag/ |
| Account settings | https://crowdlinks.jp/worker/user/account_setting/ |
| Client LP (close) | https://crowdlinks.jp/client/ |

---

## 日本語（運用だけ）

下書きのみ。このエージェントは登録しない。入口は https://crowdlinks.jp/worker/signup/ 。**MAIN Google**（ボタンに「Googleで登録する」と書いてあること。静的HTMLには無い）。無ければ同じメール。プロフィールは保存まで。**応募フォームへ / 話を聞きたいは押さない**。スカウト返信・マッチング報告・有料会員・追加書類・口座はしない。手数料％と案件件数は捏造しない。実務経験2年は台帳が空なら盛らない。公開範囲はクラウドリンクス内。一般公開しない。本名と副業の可否は本人が決める。電話のSMSは下書き保存が止まらない限り触らない。

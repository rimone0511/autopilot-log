> DRAFT_ONLY CU handoff. NO secrets. NO invented credentials. NO live signup from this authoring agent.  
> Human / CU paste only. Live form wins.  
> Desk: **複業クラウド**（旧 Another Works） / **B03** / **CU-12**.  
> Auth: **MAIN Google** likely — public JS label **「Googleでサインイン」** on `/sign_up`. Icon must say Google at click-time.  
> This pass: **talent profile draft only**. Do not エントリー. Do not キニナル.  
> **REGISTER-CU-CUT / jobs-first:** do **not** open this desk as next live CU. Banner: [STATUS.md](STATUS.md) `register_cu_cut`.  
> Stop: [STOP.md](STOP.md) (apply + KYC + phone/SMS-as-ID). Fields: [FIELD-MAP.md](FIELD-MAP.md). Session box: [STATUS.md](STATUS.md).

# PLAYBOOK — 複業クラウド talent signup (B03)

| Key | Value |
|---|---|
| Desk | 複業クラウド（fukugyo cloud / 旧 Another Works） / **talent worker**. Not company / 採用担当 |
| IDs | **B03** · Wave B · **CU-12** |
| Not | Company console `cl.aw-anotherworks.com` (except TOS). Not Workship. Not CrowdWorks |
| Mode | **DRAFT_ONLY** |
| Language | **日本語** paste on profile fields. Internal notes may be English |
| Google | **PREFER_GOOGLE / MAIN SSO likely** — public chunk label **「Googleでサインイン」**. Static HTML is a loader; **click-time** confirmation |
| Email fallback | Same MAIN mailbox on the same `/sign_up` form (`メールアドレス` / `パスワード` / `パスワードの確認`). OTP = parent Gmail |
| Plan | Talent use **cited free** (TOS 第2.1条1). Worker success-fee **% not on TOS** → do not invent. Company plans = close |
| This pass | Account (if needed) → プロフィール下書き保存. Stop before 応募 / キニナル / オファー返信 |
| Hard no | **エントリー** · **キニナル** · スカウト返信 · ソリューション公開 · 本人確認書類 · 口座 · マイナンバー |
| Activity gate | **`needs_check`** (this GET). Not `alive`. Not `thin`. See [STATUS.md](STATUS.md) |
| `thin_site_skip` | **false** (talent 200 + public job **titles**. Unread listing dates ≠ thin) |
| Skip | Captcha / press-hold that does not clear in one session → **`blocked_skip`**. Do not retry this pass |
| Serial | **`register_cu_cut`** — not next live CU. Prefer JOBS phase ([#72](https://github.com/rimone0511/autopilot-log/pull/72)) |
| Authoring session | Public GET / TOS / JS labels only. **Did not create an account** |

Sibling packs (bodies **not** copied; paste fences for 自己紹介 live in [FIELD-MAP.md](FIELD-MAP.md)):

| Sibling | PR |
|---|---|
| Thick CU-12 sample paste | `earn-waveb-alive-handoff-sample-20260916/02-fukugyo-cloud.md` ([#21](https://github.com/rimone0511/autopilot-log/pull/21)) |
| Activity-gate record | `earn-activity-gate-waveB-20260916/records/03-fukugyo-cloud.md` ([#12](https://github.com/rimone0511/autopilot-log/pull/12)) |
| Activity-gate re-GET | `ops/earn/waveb-activity-gate-batch1-20260916/b03-fukugyo-cloud.md` ([#62](https://github.com/rimone0511/autopilot-log/pull/62)) |
| REGISTER-CU-CUT serial | `ops/earn/waveb-alive-cu-serial-20260916/` ([#72](https://github.com/rimone0511/autopilot-log/pull/72)) — **do not play** |

**REGISTER-CU-CUT / jobs-first:** Wave B 登録直列の自動再生は JOBS に譲る。このフォルダは 複業クラウド 机のランナーだが、Freelancer.com（A10）の次に **勝手に開かない。** 人が明示 GO したときだけ PLAYBOOK を踏む。GO しても **エントリー / キニナルはしない。**

This playbook is the **step order**. Placeholders stay empty of secrets in git.

---

## Hard rules (read before the first click)

1. **MAIN Google.** Open [talent.aw-anotherworks.com/sign_up](https://talent.aw-anotherworks.com/sign_up). Under **外部サービスでサインイン**, click the control that **says Googleでサインイン**. Use `{{GOOGLE_ACCOUNT_EMAIL}}` — MAIN mailbox only. Facebook / Apple as a **new** identity: no.
2. **Email is the same person.** If the Google control is missing, unlabeled, or OAuth fails: same-page **メールアドレス** `{{EMAIL}}` = MAIN mailbox, **パスワード** / **パスワードの確認** `{{PASSWORD_DO_NOT_STORE}}`. Never commit it. Confirm mail stays in **parent Gmail**. Do not paste codes into git.
3. **Talent worker only.** Stay on `talent.aw-anotherworks.com`. Close [cl.aw-anotherworks.com](https://cl.aw-anotherworks.com/) **無料デモ / 無料で人材データベースを見てみる / サービス資料**. TOS may be opened read-only.
4. **Do not invent fees or traffic.** TOS 第2.1条1: 登録タレントは本サービスを**無料で**利用できる. Worker 成功報酬％ is **not on that TOS**. OG copy「完全無料」「中間マージンなどは一切発生しません」is marketing on the talent origin — do not turn it into a ％ cell or a GMV number.
5. **DRAFT_ONLY this pass.** Fill 自己紹介 / 職種 / スキル / 公開URL. Save draft. TOS 第2.1条2: some profile items are shown to **all registered companies**. Extra public / ソリューション / 転職スカウト toggles stay off if visible.
6. **エントリー and キニナル are stops.** TOS 第2.1条3 is 応募. Public JS has a **キニナル / キニナル済** control. App Store text treats キニナル as compare; a 2022 article treated it as easy entry. **Do not press either.** Looking at a title is optional.
7. **STOP before KYC / phone-as-ID / SMS-as-ID.** Public TOS and company privacy GET had **no** 「本人確認」「SMS」「口座」「マイナンバー」. If the live wizard asks for ID, selfie, bank, or My Number — close. Phone/SMS only if **draft save** is blocked; then `sms_wait_user`. If the same step asks for ID → KYC STOP. See [STOP.md](STOP.md).
8. **Captcha / press-hold → `blocked_skip`.** One session try only. Do not bypass. Do not hammer. See skip rules below.
9. **No credentials in git.** OTP, passwords, backup codes, bank digits, My Number, government ID, CSRF, reCAPTCHA tokens — none of those belong in this repo.

Already a member on MAIN: **サインイン** ([/login](https://talent.aw-anotherworks.com/login) **Googleでサインイン**, or same mailbox). Do not open a second account. Outcome `already_member_draft`.

---

## Official signup URL(s)

Confirmed this authoring GET (no POST, no OAuth follow):

| What | URL | This GET |
|---|---|---|
| Talent home (CTA host) | https://talent.aw-anotherworks.com/ | 200. Title 複業クラウド. Public JS const `SIGN_UP:"/sign_up"`. Nav copy **無料ではじめる** / **サインイン** / **企業採用担当者の方はこちら** |
| **Worker signup (this pack)** | https://talent.aw-anotherworks.com/sign_up | **200**. Title **新規登録**. `__NEXT_DATA__` `page:"/sign_up"`. Static HTML is a loader |
| Worker login | https://talent.aw-anotherworks.com/login | 200. Title **サインイン**. Login chunk: **新規登録はこちら** |
| `/signup` `/sign-up` `/register` | those paths | **404** this GET — do not use |
| Company console (close) | https://cl.aw-anotherworks.com/ | 200. 無料デモ / 人材DB — **not** talent entry |
| TOS (read-only) | https://cl.aw-anotherworks.com/user_tos | 200 |
| Privacy (TOS footer) | https://anotherworks.co.jp/user_privacy | 200. `cl.aw-anotherworks.com/user_privacy` **404** this GET |
| Company site (not the board) | https://anotherworks.co.jp/ | 200 |

Live `/sign_up` form is SPA. Public chunk `2ft1bogak3uo6.js` (HTTP 200) contains:

- heading copy **複業クラウドへようこそ！** / **新規登録**
- **外部サービスでサインイン**
- **Googleでサインイン** (`handleClickGoogle` / `signInGoogle`)
- **Facebookでサインイン** / **Appleでサインイン**
- **メールアドレス** · **パスワード** · **パスワードの確認**
- password hints: 半角英数字8文字以上 / 半角英字・半角数字をそれぞれ1文字以上
- **利用規約** / **プライバシーポリシー** / toast **利用規約等に同意が必要です**
- **サインインはこちら**
- already-registered toast **メールアドレスが既に登録されています**

This GET did **not** click OAuth and did **not** submit email.

---

## Google MAIN SSO — likely?

**Yes — PREFER_GOOGLE / MAIN SSO likely.** Not a painted static button (loader only). Evidence is the public signup/login JS labels above. CU still **looks at the live control**. If the live label is not Google, park rather than inventing Facebook/Apple as a new identity.

- Use the **same MAIN Google** as the rest of the earn queue.
- Consent: basic profile / email. Deny Gmail-read-all / Drive / Contacts dump → `oauth_overreach`.
- First SNS wins. Do not retry a second provider to “fix” a duplicate-email toast.
- Email fallback = **same MAIN mailbox**, not a new Gmail.

---

## Skip rules → `blocked_skip`

This desk is **not** LinkedIn’s 3-attempt try-first. Captcha / press-hold here **parks the desk**.

| Wall | Agent this session | Then |
|---|---|---|
| No captcha / simple proceed | Continue draft | — |
| Checkbox / “I’m not a robot” / **Press & Hold** | **One** session: `holdDurationMs` **1800**, one retry **2500**. Must send hold, not click+sleep. If the tool has no `holdDurationMs` → STOP `tool_missing_holdDurationMs` | If still failing: **`blocked_skip`** (`hold_failed` / captcha). **Do not retry this pass** |
| Image / tile / select-the-buses puzzle | **Stop.** Do not click tiles. Do not guess | **`blocked_skip`** (`image_puzzle`). Human may solve later on **own** browser. Agent does not reopen this desk this pass |
| WAF / 403 / Cloudflare loop | Do not reGET to burn the box | **`blocked_skip`** (`waf`) |
| Google control missing **and** email path also captcha-blocked | Do not mint Facebook / Apple / a second Google | **`blocked_skip`** (`google_icon_missing` or captcha) |
| SMS / phone for **draft save** | Wait on user chat. Do not guess a number | `sms_wait_user` (not blocked_skip). If user is away: park |
| ID / selfie / 本人確認 on the same wall | Close. No upload | `kyc_wait` — [STOP.md](STOP.md) |

Do **not**: captcha bypass, lockout retries, a second marketplace identity, VPN experiments from this agent, or treating `blocked_skip` as “try Workship’s 気になる trick.”

`blocked_skip` is a valid desk outcome. Write it in [STATUS.md](STATUS.md) and leave.

---

## Step order

Live wizard order wins if it differs. Timebox: 15–25 minutes. Stuck > 10 minutes on one modal: park and write [STATUS.md](STATUS.md).

TOS flow (talent): 登録 (第1.3条) → プロフィール設定 (第2.1条2) → 応募で探索 (第2.1条3). **This pack ends after profile draft save.**

### A. Create or open the talent account

| # | Do | Do not |
|---|---|---|
| 1 | Open https://talent.aw-anotherworks.com/sign_up (existing member: https://talent.aw-anotherworks.com/login) | `cl.aw-anotherworks.com` 無料デモ, `/signup` 404 paths, company `anotherworks.co.jp` as the board |
| 2 | **外部サービスでサインイン** → **Googleでサインイン**. MAIN `{{GOOGLE_ACCOUNT_EMAIL}}` | Facebook / Apple as a new identity. Guest. Invented Gmail |
| 3 | OAuth consent: basic profile / email | Extra scopes “to finish signup” |
| 4 | Fallback if Google missing/unlabeled/fails: **メールアドレス** `{{EMAIL}}` (same MAIN), **パスワード** + **パスワードの確認** `{{PASSWORD_DO_NOT_STORE}}`, tick live 同意 after the **human** reads, submit **登録** / live button | New mailbox. Password in git. Skip 同意 without the human reading |
| 5 | OTP / confirm URL = **parent Gmail**. Resend at most once | Paste OTP into git / STATUS. Open `mail.google.com` unless the live CU has no other way **and** the user already authorized that |
| 6 | Captcha / hold: skip table above. One 1800/2500 pair then **`blocked_skip`** | Guess a bypass. Retry until lockout |
| 7 | Role stays **タレント / 個人**. If a 事業者 / 採用 wizard appears, back out | 登録事業者. 複業クラウド for Enterprise as a new desk |

Account exists after a typical confirm. That is **not** permission to エントリー. Stop is still before apply and KYC.

Agent does **not** tick 利用規約 for the user in the authoring session. Live CU: the **human** reads, then the runner may tick if the human already said GO for this desk.

### B. Fill the profile (draft — this pass ends here)

Live labels win. [FIELD-MAP.md](FIELD-MAP.md).

| # | Do | Do not |
|---|---|---|
| 1 | 氏名 `{{LEGAL_NAME_KANJI}}`. Display `{{DISPLAY_NAME}}` 推奨 **石田祐太** if the form splits | Brand-only fake 屋号 as the legal name |
| 2 | 自己紹介: paste **200** or **800** (n8n / AI自動化) from FIELD-MAP. Skip AI-template unless the human asks; if used, **read before save** | Client names / confidential case detail. Unverified counts. Traffic/GMV |
| 3 | 職種: エンジニア / 業務自動化 / 最寄り existing chip. 得意領域 max-3 is **third-party** — follow live | Invent a chip not in the DB |
| 4 | スキル: Claude Code, Codex, Python, n8n, API, 業務自動化 — **existing chips only** | 未経験. 「TikTok 無人投稿」 |
| 5 | ポートフォリオ: public URLs `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}` | Private repos. Login-walled demos. ID photos |
| 6 | 希望単価: `{{HOURLY_YEN_DRAFT}}` empty / 要相談. Job-card 円 (e.g. 月80〜100万円 on a **title**) is **not** a profile rate | Invent 円 |
| 7 | 稼働 / リモート: リモート可, 週次は要相談. Follow live selects | Fake 週○時間 |
| 8 | 転職意向: 複業・業務委託の最寄り. Do not flip to 複業転職専願 | TOS 第2.1条5 転職スカウト as a GO |
| 9 | 非表示企業 `{{BLOCK_COMPANY_NAMES}}` optional. Real names stay off git | Commit a block-list of employers |
| 10 | 顔写真 `{{PHOTO_LOCAL_PATH}}` optional. Not an ID | Passport / license / selfie-for-KYC |
| 11 | 公開トグル: 非公開 / 下書き if obvious. TOS says some items go to **all registered companies** — do not hunt a global unlisted that the live form does not offer | ソリューション投稿 / 公開 as a catalog listing |

### C. Stop (do not continue into matching)

Do **not**:

- Press **エントリー** / **応募する**
- Press **キニナル** / **キニナル済**
- Reply to スカウト / オファー / メッセージで営業 (TOS 第2.1条4 forbids 迷惑営業)
- Post **ソリューション** (company LP describes it as a talent catalog — treat as publish)
- Open 本人確認 / 口座 / マイナンバー
- Start a company paid plan

Write the success line. Stop.

---

## Fees (cite only — do not pay, do not invent %)

| Claim | Status | Source |
|---|---|---|
| 登録タレントは本サービスを無料で利用できる | **cited** | [TOS 第2.1条1](https://cl.aw-anotherworks.com/user_tos) |
| 成功報酬無料 for **registered companies hiring from the DB** | **cited, not a worker %** | TOS 第1.2条(16)(18) definition text. Do not copy into a talent fee cell |
| Worker success-fee ％ | **unstated** | Not on the TOS this GET opened → `needs_check`. **Do not invent** |
| Company 利用料金 | **company-side** | TOS 第3.2条. Close. Do not open a paid 事業者 plan |
| Talent OG「完全無料」「中間マージンなどは一切発生しません」 | **marketing on official talent meta** | `/sign_up` description. Not a ％ table |
| Listing traffic / GMV / 登録者数 | **do not invent** | This GET did not see a public count to cite. Sitemap has no `<lastmod>` |

Job-title pay ranges (例: 「月80〜100万円」 on `/projects/91375`) are **that card’s headline**, not a profile 希望単価 and not GMV.

---

## Explicit do-not

- Company / 採用担当 workspace (`cl.aw-anotherworks.com` 無料デモ)
- New SNS identity (Facebook / Apple) just for this desk
- Second 複業クラウド account
- **エントリー** / **キニナル** / スカウト返信 / メッセージで営業
- ソリューション公開
- 本人確認書類 / 自撮り / 印鑑証明
- 口座 / マイナンバー / カード
- Invent `{{HOURLY_YEN_DRAFT}}`, worker 手数料％, or traffic
- That Autopilot Log posts TikTok unattended (inbox upload is the default; direct post is gated)
- Browser automation / scraper as a 複業クラウド applicant bot
- This authoring agent POSTing `/sign_up`
- Opening this desk as **next live CU** while `register_cu_cut` is set

---

## Success line (secret-free)

Valid outcomes: `done-draft` | `already_member_draft` | `kyc_wait` | `apply_stop` | `sms_wait_user` | `no_draft_path` | `otp_missing` | `hold_failed` | `blocked_skip` | `oauth_overreach` | `rate_empty` | `google_icon_missing` | `image_puzzle` | `waf` | `not_run`.

Not success: “エントリーした,” “キニナル済,” “スカウト返信,” “ソリューション公開,” “口座登録,” “本人確認提出.”

```
desk: 複業クラウド
pack: earn-fukugyo-cloud-cu-handoff-20260916/
ids: B03 / CU-12
auth: google-main | email-same-mailbox | already_member | blocked | google_icon_missing
otp: gmail-parent | sms-chat | none | otp_missing | sms_wait_user
kyc: none | wait-morning + photo_id | selfie | bank | my_number
draft_profile: yes/no
entry: no
kininaru: no
scout_reply: no
solution_post: no
publish: no
plan: talent-free-cited
bank: no
rate: empty | placeholder-from-ledger | rate_empty
skip: none | blocked_skip + captcha | blocked_skip + hold | blocked_skip + image_puzzle | blocked_skip + waf
register_cu_cut: yes
holdDurationMs_used: <e.g. 1800 or none>
next: stop | jobs-first
```

Copy the same keys into [STATUS.md](STATUS.md) after a live run. Do not put OTP digits, passwords, ID numbers, a live phone, or a bank amount there.

---

## 日本語（運用だけ）

下書きのみ。このエージェントは登録しない。入口は https://talent.aw-anotherworks.com/sign_up 。**MAIN Google**（「Googleでサインイン」と書いてあること）。無ければ同じメール。プロフィール下書き保存まで。**エントリーとキニナルは押さない**。スカウト返信・ソリューション公開・本人確認・口座はしない。手数料％と流入数は捏造しない。キャプチャ / 長押しが一度で通らなければ **`blocked_skip`**。**REGISTER-CU-CUT:** 次のライブ CU としてこの机を開かない（jobs-first）。

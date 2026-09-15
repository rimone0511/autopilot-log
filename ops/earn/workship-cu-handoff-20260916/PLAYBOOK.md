> **REGISTER-CU-CUT.** Workship is **not next live CU**. Jobs-first. **Do not autoplay.** See [STATUS.md](STATUS.md) banner `register_cu_cut`.  
> DRAFT_ONLY CU handoff. NO secrets. NO invented credentials. NO live signup from this authoring agent.  
> Human / CU paste only **after a later human GO**. Live form wins. Default: **do not open `/signup` from this pack**.  
> Desk: Workship / ワークシップ（**B02** / QUEUE **B2** / **CU-11**).  
> Auth: **MAIN Google** on public https://goworkship.com/signup (`SNSで登録` → Google icon at click-time).  
> This pass (only if GO): **profile draft only**. Official help: 「気になる！」= **エントリー完了**. **Do not press 気になる / エントリー.**  
> Stop: [STOP.md](STOP.md) (apply + KYC + bank). Fields: [FIELD-MAP.md](FIELD-MAP.md). Session box: [STATUS.md](STATUS.md).

# PLAYBOOK — Workship freelance signup (B02)

| Key | Value |
|---|---|
| Desk | Workship（ワークシップ） / **freelance worker**. Not ENTERPRISE / 採用担当 |
| IDs | **B02** · QUEUE **B2** · **CU-11** |
| Not | **Workshift** (`workshift-sol.com`, B09). Do not mix |
| Mode | **DRAFT_ONLY** / **REGISTER-CU-CUT**. Default **do not autoplay** |
| Language | **日本語** |
| Google | **PREFER_GOOGLE** — MAIN only. Public `/signup` heading **SNSで登録** + FirebaseUI `GoogleAuthProvider.PROVIDER_ID`. **Icon must say Google** at click-time |
| Email fallback | Same MAIN mailbox on the same `/signup` form (`メールアドレス` / `パスワード`). OTP = parent Gmail. Confirm URL **24 hours** ([help/44](https://goworkship.com/help/how_to/44)) |
| Plan | **Free** ([help/41](https://goworkship.com/help/about_workship/41): フリーランス登録は無料。成約後のサービス利用料も発生しない). Do not invent prepaid 手数料％ |
| This pass | Account (if needed) → プロフィールを編集 → **更新する / 追加する**. Stop at STEP2 of [flow](https://goworkship.com/flow) |
| Hard no | **気になる！** · **エントリー** · スカウト返信 · 成約報告 · 契約署名 · 前払い本人確認 · 振込先口座 |
| `thin_site_skip` | **false** (public pages live 2026-09-16 folder stamp) |
| Authoring session | Public GET / help only. **Did not create an account** |

Sibling packs (bodies **not** required to open this runner; paste fences for 自己紹介 live in [FIELD-MAP.md](FIELD-MAP.md)):

| Sibling | Path / PR |
|---|---|
| Thick CU-11 (field map + JA 200/800) | `earn-waveb-cu-handoff-batch2-20260916/01-workship.md` ([#30](https://github.com/rimone0511/autopilot-log/pull/30)) |
| Thin Week2 | `earn-register-packs-jp-20260916/02-workship.md` ([#3](https://github.com/rimone0511/autopilot-log/pull/3)) |
| Activity gate | `earn-activity-gate-waveB-20260916/records/02-workship.md` ([#12](https://github.com/rimone0511/autopilot-log/pull/12)) **pass** |
| Serial pointer (Workship → SOKUDAN → Offers) | `earn-workship-sokudan-offers-serial-cu-20260916/01-workship.md` ([#50](https://github.com/rimone0511/autopilot-log/pull/50)) |
| Alive serial note B02 | `ops/earn/waveb-alive-cu-serial-20260916/b02-workship/CU-NOTE.md` ([#72](https://github.com/rimone0511/autopilot-log/pull/72)) — **REGISTER-CU-CUT**. Same cut on this desk: not next CU |
| Morning KYC 1枚 | `earn-kyc-morning-checklist-20260916/` ([#4](https://github.com/rimone0511/autopilot-log/pull/4)) |

This playbook is the **step order**. Placeholders stay empty of secrets in git.

---

## Hard rules (read before the first click)

1. **MAIN Google.** Open [goworkship.com/signup](https://goworkship.com/signup). Under **SNSで登録**, click the icon that **says Google**. Use `{{GOOGLE_ACCOUNT_EMAIL}}` — MAIN mailbox only. Facebook / Apple / LINE / Twitter as a **new** identity: no.
2. **Email is the same person.** If the Google icon is missing, unlabeled, or OAuth fails: same-page **メールアドレス** `{{EMAIL}}` = MAIN mailbox, **パスワード** `{{PASSWORD_DO_NOT_STORE}}`. Never commit it. Confirm URL stays in **parent Gmail** (help: 24 hours). Do not paste codes into git.
3. **Freelance worker only.** Stay on `goworkship.com`. Close [enterprise.goworkship.com](https://enterprise.goworkship.com/) and login **採用担当者はこちら**.
4. **Free only.** Help says freelance signup is free and post-contract サービス利用料 is not charged to the worker. Do **not** invent a worker 手数料％. Prepaid option fees: read live, do not copy amounts, **do not apply** this pass.
5. **DRAFT_ONLY this pass.** Fill 自己紹介 / やってみたいこと / 職歴 / スキル / ポートフォリオ URL. Save with **更新する** / **追加する**. Official flow STEP3 is 募集にエントリーする — **do not start STEP3**.
6. **気になる！ is エントリー.** [help/72](https://goworkship.com/help/how_to/72): 各募集にある「気になる！」ボタンを押すと、エントリー完了. That opens a メッセージルーム. Treat **気になる** and **エントリー** as the same stop. See [STOP.md](STOP.md).
7. **STOP before KYC / bank.** 契約管理 **署名をする**, 前払いオプション（本人確認が必要）, 振込先口座, マイナンバー — close. No how-to beyond [STOP.md](STOP.md).
8. **No credentials in git.** OTP, passwords, backup codes, bank digits, My Number, government ID, CSRF, reCAPTCHA tokens — none of those belong in this repo.

Already a member on MAIN: **ログイン** ([/login](https://goworkship.com/login) **SNSでログイン** Google, or same mailbox). Do not open a second account. Outcome `already_member_draft`.

---

## Step order

Live wizard order wins if it differs. Timebox: 15–25 minutes. Stuck > 10 minutes on one modal: park and write [STATUS.md](STATUS.md).

Official [flow](https://goworkship.com/flow) is STEP1 アカウント作成 → STEP2 プロフィールの充実 → STEP3 案件をチェック / エントリー. **This pack ends at STEP2.**

### A. Create or open the freelance account

Public GET 2026-09-16 (no POST): `/signup` title **フリーランス登録をする | Workship**. Visible: **SNSで登録**, `#firebaseui-auth-container`, then **メールアドレス 必須**, **パスワード 必須** (placeholder 8–20文字の半角英数字記号), **招待コード**, agree **プライバシーポリシー** + **利用規約** (`/guide`) + **個人情報の取り扱いについて**, submit **登録する**, reCAPTCHA. JS includes `firebase.auth.GoogleAuthProvider.PROVIDER_ID`. Static HTML does **not** print the word “Google” on the SNS icons. Headless render of the same URL showed the FirebaseUI **Google G** button under **SNSで登録**. **If the live icon is missing, fall back to email.**

| # | Do | Do not |
|---|---|---|
| 1 | Open https://goworkship.com/signup (existing member: https://goworkship.com/login) | `enterprise.goworkship.com`, 採用担当者ログイン, Workshift |
| 2 | **SNSで登録** → icon **Google**. MAIN `{{GOOGLE_ACCOUNT_EMAIL}}` | Facebook / Apple / LINE / Twitter as a new identity. Guest. Invented Gmail |
| 3 | OAuth consent: basic profile / email. Deny Gmail-read-all / Drive / Contacts dump | Extra scopes “to finish signup” |
| 4 | Fallback if Google icon missing/unlabeled/fails: **メールアドレス** `{{EMAIL}}` (same MAIN), **パスワード** `{{PASSWORD_DO_NOT_STORE}}`, tick live 同意, **登録する** | New mailbox. Password in git. Skip 同意 without the human reading |
| 5 | 招待コード: `{{INVITE_CODE}}` empty unless the ledger already has one | Invent an invite |
| 6 | OTP / confirm URL = **parent Gmail**. Resend at most once. Help: URL **24 hours** | Paste OTP into git / STATUS. Open `mail.google.com` unless the live CU has no other way **and** the user already authorized that |
| 7 | reCAPTCHA / hold: wait for the human if it is not a simple checkbox. Press-and-hold: set `holdDurationMs` (example 1800, retry 2500) then park if it still fails | Guess a captcha bypass. Retry until lockout |
| 8 | Role stays **フリーランス**. If a client/採用 wizard appears, back out | ENTERPRISE 採用担当 |
| 9 | Eligibility cite (not a bank form): Japan 住民票 + 本人名義の国内口座 **as a later rule** ([help/71](https://goworkship.com/help/about_workship/71)). Do **not** open 振込先 this pass | Fill bank “because help mentioned it” |

Account exists after a typical confirm. That is **not** permission to 気になる. Stop is still before apply and KYC.

Agent does **not** tick 利用規約 for the user in the authoring session. Live CU: the **human** reads, then the runner may tick if the human already said GO for this desk.

### B. Fill the profile (draft — this pass ends here)

Help path: 画面右上 → **プロフィールを編集**. Save controls: **更新する** (自己紹介 / やってみたいこと / スキル) and **追加する** (職歴 / ポートフォリオ). [FIELD-MAP.md](FIELD-MAP.md).

| # | Do | Do not |
|---|---|---|
| 1 | 登録名 = 本名 or 旧姓 from ledger (`{{LEGAL_NAME_KANJI}}`). Help forbids 活動名 / 通称名 / 屋号 ([help/69](https://goworkship.com/help/edit_profile/69)) | Brand-only name. Fake 屋号 |
| 2 | 自己紹介: paste **200** or **800** from FIELD-MAP. Save **更新する**. Skip **AIで自動入力する** unless the human asks; if used, **read before save** | Client names / confidential case detail. Unverified counts |
| 3 | やってみたいこと: FIELD-MAP short fence. **更新する** | Promise エントリー |
| 4 | 職歴: public facts only. Empty `{{YEARS_AUTOMATION_PUBLIC}}` → leave years empty. **追加する** | Invent tenure. Secret employer names |
| 5 | スキル: nearest **existing** chips (Claude Code, Codex, Python, API連携, 業務自動化, 技術記事 if listed). Help: 経験年数 and スキルレベル are **required** on that widget ([help/56](https://goworkship.com/help/edit_profile/56)). Ledger years or skip the chip | Invent a skill not in DB. Send **追加リクエスト** this pass |
| 6 | ポートフォリオ: public URLs `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}`. **追加する** | Private repos. Login-walled demos |
| 7 | 公開範囲: 職歴 / ポートフォリオ / 受賞歴 / 学歴 / スキル can be 公開／非公開 ([help/58](https://goworkship.com/help/edit_profile/58)). Prefer **鍵 / 非公開** if the control is obvious. 登録名 cannot be hidden | Hunt for a global “unlisted profile” that help does not describe |
| 8 | 顔写真 `{{PHOTO_LOCAL_PATH}}` optional. Not an ID | Passport / license / selfie-for-KYC |
| 9 | 希望単価: `{{HOURLY_YEN_DRAFT}}` or 要相談 / empty. If required and ledger empty → `rate_empty` | Invent 円 |
| 10 | プライバシー企業 `{{BLOCK_COMPANY_NAMES}}` optional. Real names stay off git | Commit a block-list of employers |

Award / 学歴: skip unless the ledger has a public item. エージェント「提案希望」: **do not apply** this pass.

### C. Stop (do not continue the official flow)

Do **not**:

- Open `/portal/search` to click a card (looking is optional; **気になる！** is not)
- Press **気になる！** or **エントリー** ([help/72](https://goworkship.com/help/how_to/72) · [help/77](https://goworkship.com/help/how_to/77))
- Reply to スカウト / open a メッセージルーム to pitch
- 成約報告 ([help/86](https://goworkship.com/help/agreement/86))
- 契約管理 → **署名をする** ([help/44](https://goworkship.com/help/how_to/44) · [help/105](https://goworkship.com/help/agreement/105))
- 前払いオプション ([help/95](https://goworkship.com/help/agreement/95) — 本人確認が必要)
- 振込先口座 / お祝い金口座 ([help/118](https://goworkship.com/help/agreement/118) · [help/100](https://goworkship.com/help/agreement/100))
- LINE 通知連携 as a new identity
- freee 会計連携

Write the success line. Stop. **Default next is JOBS phase, not this desk and not SOKUDAN autoplay.** Do not chain Freelancer → Workship. Human GO only.

---

## Fees (cite only — do not pay, do not copy prepaid %)

| Claim | Status | Source |
|---|---|---|
| Freelance signup is free | **cited** | [利用料金](https://goworkship.com/help/about_workship/41) |
| 成約後のサービス利用料も発生しない（worker） | **cited, qualitative** | Same article. Do not turn this into a made-up マージン％ |
| お祝い金 1万円 at first-month pay | **cited, unused** | [お祝い金](https://goworkship.com/help/agreement/100). Needs 成約 + 口座. **Not this pass** |
| 前払いオプション has 手数料 | **cited, unused, % not copied** | [前払い](https://goworkship.com/help/agreement/95) says 手数料・利用規約を確認の上. Live screen wins. Do not invent ％ |
| Hourly 円 | **placeholder** | `{{HOURLY_YEN_DRAFT}}` only. Empty save, else ledger, else `rate_empty` |

Marketing counts on `/portal/search` (全○件) are **not** GMV. Do not paste them as activity proof.

---

## Explicit do-not

- Autoplay this desk / chain Freelancer.com → Workship (**REGISTER-CU-CUT**; jobs-first)
- ENTERPRISE / 採用担当 workspace
- Workshift (`workshift-sol.com`) by mistake
- New SNS identity (Facebook / Apple / LINE / Twitter) just for this desk
- Second Workship account
- **気になる！** / **エントリー** / スカウト返信 / メッセージで営業
- 成約報告 / お祝い金 flow / 個別契約
- 契約管理 **署名をする** / 身分証 / 印鑑証明
- 前払いオプション / 本人確認手続き
- 振込先口座 / 帳票の振込先 / マイナンバー
- エージェント提案希望 (this pass)
- Invent `{{HOURLY_YEN_DRAFT}}`, worker 手数料％, or GMV
- That Autopilot Log posts TikTok unattended (inbox upload is the default; direct post is gated)
- Browser automation / scraper as a Workship applicant bot
- This authoring agent POSTing `/signup`

---

## Success line (secret-free)

Valid outcomes: `done-draft` | `already_member_draft` | `kyc_wait` | `apply_stop` | `sms_wait_user` | `no_draft_path` | `otp_missing` | `hold_failed` | `oauth_overreach` | `rate_empty` | `google_icon_missing`.

Not success: “気になる pressed,” “エントリー完了,” “スカウト返信,” “署名した,” “口座登録,” “前払い.”

```
desk: Workship
pack: ops/earn/workship-cu-handoff-20260916/
ids: B02 / QUEUE-B2 / CU-11
auth: google-main | email-same-mailbox | already_member | blocked | google_icon_missing
otp: gmail-parent | sms-chat | none | otp_missing | sms_wait_user
kyc: none | wait-morning + contract_sign | prepaid_id | bank
draft_profile: yes/no
entry: no
kininaru: no
scout_reply: no
publish: no
plan: free
prepaid: no
bank: no
rate: empty | placeholder-from-ledger | rate_empty
holdDurationMs_used: <e.g. 1800 or none>
next: jobs-first | stop
```

Copy the same keys into [STATUS.md](STATUS.md) after a live run. Do not put OTP digits, passwords, ID numbers, a live phone, or a bank amount there.

---

## URLs (public; re-open before CU)

| What | URL |
|---|---|
| Home | https://goworkship.com/ |
| Signup (this pack) | https://goworkship.com/signup |
| Login | https://goworkship.com/login |
| Flow (stop after STEP2) | https://goworkship.com/flow |
| Search (do not 気になる) | https://goworkship.com/portal/search |
| Help: 新規登録 | https://goworkship.com/help/how_to/44 |
| Help: 気になる = エントリー | https://goworkship.com/help/how_to/72 |
| Help: エントリー後 | https://goworkship.com/help/how_to/77 |
| Help: 自己紹介（更新する） | https://goworkship.com/help/edit_profile/52 |
| Help: やってみたいこと | https://goworkship.com/help/edit_profile/53 |
| Help: 職歴 | https://goworkship.com/help/edit_profile/75 |
| Help: ポートフォリオ | https://goworkship.com/help/edit_profile/54 |
| Help: スキル | https://goworkship.com/help/edit_profile/56 |
| Help: 公開範囲 | https://goworkship.com/help/edit_profile/58 |
| Help: 本名（屋号不可） | https://goworkship.com/help/edit_profile/69 |
| Help: 無料 | https://goworkship.com/help/about_workship/41 |
| Help: 海外 / 国内口座対象 | https://goworkship.com/help/about_workship/71 |
| Help: 前払い = 本人確認 **STOP** | https://goworkship.com/help/agreement/95 |
| Help: 契約 / 署名 **STOP** | https://goworkship.com/help/agreement/105 |
| Help: 振込先 **STOP** | https://goworkship.com/help/agreement/118 |
| Terms | https://goworkship.com/guide |
| Privacy | https://goworkship.com/privacy-policy |
| ENTERPRISE (close) | https://enterprise.goworkship.com/ |

---

## 日本語（運用だけ）

**REGISTER-CU-CUT。次のライブ CU ではない。JOBS 優先。自動再生しない。** 下書きパックのみ。このエージェントは登録しない。人が GO するまで `/signup` を開かない。GO 後も入口は https://goworkship.com/signup 。**MAIN Google**（アイコンに Google と書いてあること）。無ければ同じメール。プロフィールは **更新する / 追加する** まで。**気になる！とエントリーは押さない**（公式ヘルプでは気になる＝エントリー完了）。スカウト返信・成約報告・契約署名・前払い本人確認・口座はしない。手数料％は捏造しない。

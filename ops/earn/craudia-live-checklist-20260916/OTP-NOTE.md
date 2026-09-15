# OTP-NOTE — クラウディア live register

> **DRAFT_ONLY.** JP OK. No secrets.  
> Pack: `ops/earn/craudia-live-checklist-20260916/`  
> Desk: クラウディア（ワーカー）  
> Audience: CU serial agent

Companion: [CHECKLIST.md](CHECKLIST.md) §2–3.

This note is **tighter on SMS** than sibling `earn-craudia-deep-paste-20260916/00-google-otp-hold.md` ([#51](https://github.com/rimone0511/autopilot-log/pull/51)).  
Here: **Gmail OTP = allowed. SMS = skip** (do not complete phone auth on this pass).

---

## Policy

| Channel | This pack |
|---|---|
| MAIN Google OAuth | Prefer. Picker = `{{GOOGLE_ACCOUNT_EMAIL}}` only |
| Gmail 認証メール / コード / magic-link | **Allowed** via **parent Gmail MCP**. CU does not open Gmail |
| SMS / 電話番号入力 / 050 発信（FAQ 156） | **Skip.** Park if the site blocks even 仮登録 / プロフィール保存 |
| 本人確認で電話を迂回 | **No.** That is KYC. [CHECKLIST.md](CHECKLIST.md) §7.B |

FAQ 103: 会員登録に必要なのは連絡の取れる **PC メール**。電話は登録の条件ではない。  
FAQ 156: 電話認証は取引の不正防止・信頼性向上。このパックは取引しない。発信できなくても **本人確認へ逃げない**。

Do not commit OTP digits, magic-link URLs with tokens, full phone numbers, or `.eml` files.

---

## 1. MAIN Google

The only Google account is **`rimone0511@gmail.com`** (`{{GOOGLE_ACCOUNT_EMAIL}}`).

| Do | Do not |
|---|---|
| register-temp の Google（`auth=3` / `signin_btn_google.svg`） | Use another account で新しい Google を足さない |
| ピッカーはそのアドレスだけ | 机専用 `+desk@` を作る |
| Google が無い/落ちたとき: メール = **同じ** MAIN Gmail | Twitter / Facebook / Yahoo を新規身分にする（`auth=1/2/4`） |
| 既に登録済みならログイン | 同じ机に二件目 |
| 同意は basic profile / email | Gmail read-all / Drive / Contacts dump → `oauth_overreach` |

連携先は画面注記どおり **i2i ID**。i2i を別人格にしない。

If Google says the app is blocked / unverified: STOP. Morning user. Do not click through “unsafe” unless the user types GO in chat for **this desk**.

Browser profile: marketplace only. **Do not also live in Gmail in that profile.**

---

## 2. Gmail OTP — allowed (parent, not the CU browser)

**Parent** = Gmail MCP を持つクラウド側（`rimone0511@gmail.com`）。  
**CU child does not open `mail.google.com`.**

FAQ 151 メール経路: 認証メール → クリック（i2iID 登録完了）→ クラウディアでプロフィール。  
Google 経路でも i2i が追加確認メールを出すことがある。どちらも **Gmail OTP allowed**。

### Sequence

1. CU が register-temp で「認証メール / メールアドレス認証 / 仮登録」を起こす（メール経路）、または i2i が確認メールを出す。
2. CU が親へ（ブラウザ外）:

```
otp_request:
  desk: Craudia
  channel: gmail
  to: MAIN Google (do not print if you already know)
  from_hint: craudia.com | i2i.jp | no-reply@…
  requested_at_jst: <timestamp>
  field: 6-digit | magic-link | unknown
```

3. Parent searches Gmail MCP, for example:

```
newer_than:1d (from:craudia.com OR from:i2i.jp OR subject:(確認 OR 認証 OR 仮登録 OR verify OR confirm OR code OR i2i))
```

公式を装ったフィッシングに注意。スレッドを開く。スパムまがいの別ドメインは使わない。

4. Parent extracts the code or magic-link. Hands it to CU **in the CU session**. Does **not** commit it. Does **not** forward the whole mail.

5. CU types the code **once**, or opens the magic-link **in the same marketplace profile**. Log `gmail_otp: entered` without digits.

6. Nothing in **3 minutes**: parent searches once more. Still empty → STOP (`otp_missing`). User chat. 再送は **1回まで**。

**Forbidden:** Gmail in the marketplace browser; downloading `.eml` into the repo; a second Gmail; pasting OTP into git / STATUS.md / 成功ログ.

Authoring agent of this markdown: **do not POST** register-temp. CU serial only.

---

## 3. SMS — skip

Two pipes. Do not mix them. This pack does **not** complete SMS even if a sibling pack would wait on the user.

FAQ 156 の型: 半角数字と `+`。**こちらから 050 へ発信**（2分以内、番号通知、場合により通話料自己負担）。CU はユーザーの電話を操作できない。

### Sequence

1. Phone / SMS / 電話認証 画面が出る。
2. **Skip / あとで / 閉じる** があればそれを使う。Record `sms: skipped`.
3. Skip が無く、**仮登録・プロフィール保存・スキル下書き保存** が止まる:
   - **Do not** type `{{PHONE}}` / `{{PHONE_E164}}`.
   - **Do not** ask the user for a number on this pass.
   - **Do not** dial 050.
   - Park: `sms_skip_blocked`.
4. 画面が本人確認へ誘導（FAQ 156 の「おすすめ」）→ KYC STOP。自撮りしない。
5. アカウント復旧のための電話もこのパックの外。

If a previous session already verified a number: do not re-trigger SMS to “test”.

Do not use SMS-to-email gateways or a virtual-number service. Do not type a live phone into git.

```
sms_skip:
  desk: Craudia
  pack: ops/earn/craudia-live-checklist-20260916/
  action: skipped | sms_skip_blocked
  kyc_redirect: yes/no
  do_not_send: full number, OTP digits, ID photos, selfie
```

---

## 4. Press & Hold / captcha (not OTP, but on the same register-temp)

register-temp に **reCAPTCHA** がある（GET 2026-09-16）。

- チェックボックス / 画像選択 = hold ではない → 人待ち、または `no_draft_path`。
- Labels: `Press and Hold` / `長押し` / Cloudflare → CU 呼び出しに **`holdDurationMs`** 必須（例 1800、再試行 1 回 2500）。無ければ `tool_missing_holdDurationMs` で STOP。エミュレートしない。
- 2 回失敗 → `hold_failed`。

---

## 5. OTP typing hygiene

- Click the OTP field. Type **once** (no leading spaces).
- Magic-link: same marketplace profile only.
- Do not paste OTP into chat history that will be committed, into this repo, or onto a second site.

---

## 6. Preflight (OTP-related)

1. Parent Gmail MCP is the only inbox for this desk.
2. CU browser has no Gmail tab.
3. SMS skip is already decided — do not “just this once”.
4. No credit card. Craudia PRO = `card_wall`.
5. Timebox includes waiting 3 minutes for mail, not waiting on a phone call.

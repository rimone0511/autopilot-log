# MAIN Google, OTP pipes, Press & Hold

Pack: `earn-contra-timeticket-deep-paste-20260916`  
Desks: TimeTicket（ホスト）→ Contra Independent  
Audience: CU serial agent

---

## 1. MAIN Google `rimone0511`

The only Google account is **`rimone0511@gmail.com`** (`{{GOOGLE_ACCOUNT_EMAIL}}`).

| Do | Do not |
|---|---|
| Google ボタンが見える机では **Googleで登録 / Continue with Google** | **Use another account** で新しい Google を足す |
| ピッカーは **そのアドレスだけ** | 机専用メール（`+desk@…`）を作る |
| Google OAuth が無い / 未確認の机: メール = **同じ** MAIN Gmail | Facebook / LINE / Yahoo / Apple / X を新しい身分にする |
| 既に登録済みなら **ログイン** | 同じ机に二件目を作る（TimeTicket 規約第9条4: 複数会員登録禁止） |
| 同意は basic profile/email だけ | Gmail **read all** / Drive / Contacts dump（`oauth_overreach` → STOP） |

### Per-desk Google preference（公開ページ）

| Desk | Preference | Evidence (2026-09-16, no signup) |
|---|---|---|
| TimeTicket | **EMAIL = MAIN Gmail**（ボタンが目視できたらそのときだけ PREFER_GOOGLE） | `https://www.timeticket.jp/users/sign_up` は this env GET **202 空**。Google OAuth URL を発明しない。CU は登録面を 1 画面見て、Google があれば押す。無ければメール |
| Contra | **PREFER_GOOGLE** | 公開 `https://contra.com/independent/wallet` シェルに `googleSigninClientId`。onboarding ヘルプは Independent の Share work |

Yahoo / Facebook / Apple / LINE: Google がある机（Contra）では **無視**。TimeTicket で LINE しか無くメールが不可能なら **STOP**（朝の本人。ランダム SNS を縛らない）。

If Google says the app is blocked / unverified: STOP. Morning user. Do not click through “unsafe” unless the user types GO in chat for **that desk**.

After login:

- TimeTicket でゲスト専用のままならホスト / チケットを売る側へ。ホストになれず KYC が先なら KYC STOP。
- Contra で **Hire creative talent** / client に落ちたら **Share work** / Independent に戻す。Agency を別人格で作らない。

Browser profile: one marketplace profile. **Do not also live in Gmail in that profile.**

---

## 2. Gmail OTP — parent handles (not the CU browser)

**Parent** = Gmail MCP を持つクラウド側（`rimone0511@gmail.com`）。  
**CU child does not open Gmail.**

TimeTicket はメール登録の確認リンクがあり得る。Contra の Google 経路ならメール OTP は出にくい。

### Sequence

1. CU が「認証メール / メールアドレス認証」を机で起こす。
2. CU が親へ（ブラウザ外）:

```
otp_request:
  desk: TimeTicket | Contra
  channel: gmail
  to: MAIN Google (do not print if you already know)
  from_hint: timeticket.jp | contra.com | no-reply@…
  requested_at_jst: <timestamp>
  field: 6-digit | magic-link | unknown
```

3. Parent searches Gmail MCP, for example:

```
newer_than:1d (from:timeticket.jp OR from:contra.com OR subject:(確認 OR 認証 OR verify OR confirm OR code))
```

Narrow to the desk. Open **the thread**, not spam-looking lookalikes.

4. Parent extracts the code or magic-link. Parent **hands it to CU in the CU session**. Parent does **not** commit it. Parent does **not** forward the whole mail.

5. CU enters the code once, or opens the magic-link **in the same marketplace profile**. CU logs `gmail_otp: entered` without digits.

6. If nothing arrives in **3 minutes**: parent searches again once. If still empty: STOP (`otp_missing`). User chat. 再送は **1回まで**.

**Forbidden:** `mail.google.com` in the marketplace browser; downloading `.eml` into the repo; using a second Gmail.

---

## 3. SMS OTP — user chat only

Two pipes. Do not mix them.

下書き保存が電話なしでできるなら **skip 優先**。

### Sequence

1. CU reaches phone verify. **Prefer skip** if the site allows a **draft profile** without it.
2. If skip exists, skip. Record `sms: skipped`.
3. If the form **blocks draft save** without SMS:
   - Fill `{{PHONE_E164}}` / `{{PHONE}}` from the ledger **only if the user already placed it in chat this session**.
   - If not in chat, ask: “SMS for {desk}. Reply with the E.164 number to use, or say SKIP desk.”
4. After send, CU chats:

```
sms_otp_wait:
  desk: TimeTicket | Contra
  masked_on_screen: ***1234   # only what the page shows
  action_needed: paste the SMS code in this chat
  do_not_send: full number, ID photos
```

5. Wait. Do not poll the phone. Do not use SMS-to-email gateways. Do not use a virtual-number service.
6. User pastes the code. CU enters it once. Log `sms_otp: entered` without digits.
7. If the user is asleep / unavailable: **park the desk** (`sms_wait_user`). Continue to the **next** desk that does not need SMS. Max **one** resend, then park.

If the phone step asks for ID, selfie, or a paid ID vendor, treat it as KYC and **stop**.

Do not type `{{PHONE_E164}}` into git.

---

## 4. Press & Hold — `holdDurationMs` is mandatory

When the UI needs a hold, the CU tool call **must** include **`holdDurationMs`** (integer, milliseconds).

These are **Press & Hold** (or drag), not clicks:

- Labels: `Press and Hold`, `Press & Hold`, `長押し`, `押し続ける`, `Hold to confirm`
- Cloudflare / AWS WAF / bot walls
- Drag-and-drop avatar

**Starting values:**

| UI class | `holdDurationMs` | Then |
|---|---|---|
| Long-press menu | `800` | Release; click the menu item separately |
| Cloudflare / bot “Press & Hold” | `1800` | Retry **once** at `2500`. Second fail → STOP (`hold_failed`) |
| “Hold to confirm” submit | `2000` | Watch for progress ring |
| Drag start (avatar / slider) | `400` hold, then move | Release on drop target |

If the current CU schema has **no** `holdDurationMs` field, **STOP**. Write `tool_missing_holdDurationMs`. Do not emulate.

TimeTicket www は this env で HTTP 202 空。同じ文法の WAF / チャレンジが出たら hold。Captcha that is not a hold: human-in-the-loop.

---

## 5. OTP typing

- Click the OTP field.
- Type the code **once** (no leading spaces).
- Do not paste OTP into chat, git, or a second site.

---

## 6. Preflight (once per session)

1. Confirm you are the CU serial agent for **this** handoff, not a pack-author.
2. Viewport: desktop width ≥ 1280px.
3. If a previous CU left a **different** Google user signed in, sign **out**, then sign in `rimone0511`.
4. No credit card added in this serial. Contra Pro / Max card = `card_wall` → STOP.
5. Timebox: 15–25 minutes per desk. KYC stop ends the desk immediately.
6. One desk at a time. Do not parallelize logins.
7. TimeTicket で LINE を「速いから」選ばない。Contra で Hire を選ばない。

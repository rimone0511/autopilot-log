# MAIN Google, OTP pipes, Press & Hold

Pack: `earn-craudia-deep-paste-20260916`  
Desks: クラウディア（ワーカー）  
Audience: CU serial agent

---

## 1. MAIN Google `rimone0511`

The only Google account is **`rimone0511@gmail.com`** (`{{GOOGLE_ACCOUNT_EMAIL}}`).

| Do | Do not |
|---|---|
| Google ボタンが見える机では **Googleで登録 / signin_btn_google** | **Use another account** で新しい Google を足す |
| ピッカーは **そのアドレスだけ** | 机専用メール（`+desk@…`）を作る |
| Google OAuth が無いときのフォールバック: メール = **同じ** MAIN Gmail | Facebook / Twitter / Yahoo を新しい身分にする |
| 既に登録済みなら **ログイン** | 同じ机に二件目を作る |
| 同意は basic profile/email だけ | Gmail **read all** / Drive / Contacts dump（`oauth_overreach` → STOP） |

### Per-desk Google preference（公開ページ）

| Desk | Preference | Evidence (2026-09-16, no signup) |
|---|---|---|
| クラウディア | **PREFER_GOOGLE** | FAQ 151: Twitter / facebook / Google / Yahoo! **または** PC メール。`https://www.craudia.com/app/auth/register-temp` GET 200 に `signin_btn_google.svg` と i2i `login_auth.php?auth=3`。ログイン面も同じ Google ボタン |

Yahoo / Facebook / Twitter: Google があるこの机では **無視**。連携先は画面注記どおり **i2i ID** と表示される。i2i を別人格にしない。

If Google says the app is blocked / unverified: STOP. Morning user. Do not click through “unsafe” unless the user types GO in chat for **that desk**.

After login:

- ワーカー側に留まる。クライアントの「仕事を依頼する」（`mypage/work/register`）に入らない。
- Craudia PRO LP からのマッチング登録に進まない。
- スキル出品（`mypage/services/add` 相当）に進まない。

Browser profile: one marketplace profile. **Do not also live in Gmail in that profile.**

---

## 2. Gmail OTP — parent handles (not the CU browser)

**Parent** = Gmail MCP を持つクラウド側（`rimone0511@gmail.com`）。  
**CU child does not open Gmail.**

FAQ 151 のメール経路: 認証メール → クリック（**i2iID の登録が完了**）→ クラウディアでプロフィール → 登録完了。Google 経路ならメール OTP は出にくいが、i2i が追加確認を出すことがある。

### Sequence

1. CU が「認証メール / メールアドレス認証 / 仮登録」を机で起こす。
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

Narrow to the desk. Open **the thread**, not spam-looking lookalikes（公式注意喚起: クラウディアを装ったフィッシング）。

4. Parent extracts the code or magic-link. Parent **hands it to CU in the CU session**. Parent does **not** commit it. Parent does **not** forward the whole mail.

5. CU enters the code once, or opens the magic-link **in the same marketplace profile**. CU logs `gmail_otp: entered` without digits.

6. If nothing arrives in **3 minutes**: parent searches again once. If still empty: STOP (`otp_missing`). User chat. 再送は **1回まで**.

**Forbidden:** `mail.google.com` in the marketplace browser; downloading `.eml` into the repo; using a second Gmail.

Authoring agent of this markdown: **do not POST** `register-temp-post`. CU serial only.

---

## 3. SMS OTP — user chat only

Two pipes. Do not mix them.

下書き保存が電話なしでできるなら **skip 優先**。FAQ 103: 登録そのものに必要なのは PC メール。電話認証（FAQ 156）は取引の信頼性向上。このパックは取引しない。

### Sequence

1. CU reaches phone verify. **Prefer skip** if the site allows a **draft profile** without it.
2. If skip exists, skip. Record `sms: skipped`.
3. If the form **blocks draft save** without SMS / 電話認証:
   - Fill `{{PHONE_E164}}` / `{{PHONE}}` from the ledger **only if the user already placed it in chat this session**.
   - If not in chat, ask: “SMS/電話認証 for Craudia. Reply with the E.164 number to use, or say SKIP desk.”
4. After send, CU chats:

```
sms_otp_wait:
  desk: Craudia
  masked_on_screen: ***1234   # only what the page shows
  action_needed: paste the SMS code in this chat (or confirm the outbound-call step yourself)
  do_not_send: full number, ID photos, selfie
```

FAQ 156 の電話認証は **こちらから 050 へ発信**する型もある。CU はユーザーの電話を操作できない。その画面 = `sms_wait_user`。朝の本人。

5. Wait. Do not poll the phone. Do not use SMS-to-email gateways. Do not use a virtual-number service.
6. User pastes the code (or completes the call). CU enters it once if a field exists. Log `sms_otp: entered` without digits.
7. If the user is asleep / unavailable: **park the desk** (`sms_wait_user`). Max **one** resend, then park.

If the phone step asks for ID, **selfie**, or a paid ID vendor, or FAQ 156 どおり本人確認へ誘導されたら、treat it as KYC and **stop**.

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

register-temp に **reCAPTCHA** がある。チェックボックス / 画像選択は hold ではない → 人が解くか `no_draft_path`。Captcha that is not a hold: human-in-the-loop.

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
4. No credit card added in this serial. Craudia PRO / 有料オプション = `card_wall` → STOP.
5. Timebox: 15–25 minutes. KYC stop ends the desk immediately.
6. One desk at a time. Do not parallelize logins.
7. クライアント募集・スキル出品・PRO を「速いから」選ばない。

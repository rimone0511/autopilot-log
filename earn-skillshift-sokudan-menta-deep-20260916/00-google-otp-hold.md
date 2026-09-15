# MAIN Google, OTP pipes, Press & Hold

Pack: `earn-skillshift-sokudan-menta-deep-20260916`  
Desks: Skill Shift → SOKUDAN → Anycrew → MENTA → ストアカ  
Audience: CU serial agent

---

## 1. MAIN Google `rimone0511`

The only Google account is **`rimone0511@gmail.com`** (`{{GOOGLE_ACCOUNT_EMAIL}}`).

| Do | Do not |
|---|---|
| Google ボタンが見える机では **Googleで登録 / Googleでログイン** | **Use another account** で新しい Google を足す |
| ピッカーは **そのアドレスだけ** | 机専用メール（`+desk@…`）を作る |
| Google OAuth が無い机: メール = **同じ** MAIN Gmail | Facebook / LINE / Yahoo / Apple / X を新しい身分にする |
| 既に登録済みなら **ログイン** | 同じ机に二件目を作る |
| 同意は basic profile/email だけ | Gmail **read all** / Drive / Contacts dump（`oauth_overreach` → STOP） |

### Per-desk Google preference（公開ページ）

| Desk | Preference | Evidence (2026-09-16, no signup) |
|---|---|---|
| Skill Shift | **NOT_OFFERED_OAUTH** | 公開 `app.js` の個人登録は **メール + パスワード**。`Facebookで登録する` はある。`oauth` 文字列なし。Google は Maps/Forms のみ。**メール欄に MAIN Gmail** |
| SOKUDAN | **PREFER_GOOGLE** | `/signup/pro` に `alt="Google で登録"` → `/users/auth/google?category=signup&usage_type_id=1`。Facebook は「推奨」だが使わない。GitHub は Google の次点 |
| Anycrew | **PREFER_GOOGLE** | `app.any-crew.com` 「FacebookかGoogleのアカウントで利用登録」「Googleでログイン」。規約第3条: 登録には外部 SNS アカウント |
| MENTA | **PREFER_GOOGLE** | `register/choose` 「Googleアカウントで登録する」→ `/index.php/oauth/google`。X / Facebook / Apple / Lancers / メールは使わない |
| ストアカ | **NOT_OFFERED_OAUTH** | 公式ヘルプ（PC）: **LINE / Facebook / メールアドレス**。Google OAuth は案内に無い。**メールアドレスで登録** + MAIN Gmail |

Yahoo / Facebook / Apple / LINE / X: Google がある机では **無視**。ストアカと Skill Shift では Facebook/LINE を新規紐付けしない。

If Google says the app is blocked / unverified: STOP. Morning user. Do not click through “unsafe” unless the user types GO in chat for **that desk**.

After login, if you land on **企業 / 求人事業者 / クライアント / 発注者**: switch to 個人 / 人材 / メンター / 先生. If you cannot switch without KYC, treat as KYC and stop.

Browser profile: one marketplace profile. **Do not also live in Gmail in that profile.**

---

## 2. Gmail OTP — parent handles (not the CU browser)

**Parent** = Gmail MCP を持つクラウド側（`rimone0511@gmail.com`）。  
**CU child does not open Gmail.**

Skill Shift は公開 JS が仮登録メール → 「本登録はコチラ」型。SOKUDAN / ストアカのメール登録もマジックリンクがあり得る。MENTA / Anycrew は Google 経路ならメール OTP は出にくい。

### Sequence

1. CU が「認証メール / 仮登録 / メールアドレス認証」を机で起こす。
2. CU が親へ（ブラウザ外）:

```
otp_request:
  desk: SkillShift | SOKUDAN | Anycrew | MENTA | Storeka
  channel: gmail
  to: MAIN Google (do not print if you already know)
  from_hint: skill-shift.com | sokudan.work | any-crew.com | menta.work | street-academy.com | no-reply@…
  requested_at_jst: <timestamp>
  field: 6-digit | magic-link | unknown
```

3. Parent searches Gmail MCP, for example:

```
newer_than:1d (from:skill-shift.com OR from:sokudan.work OR from:any-crew.com OR from:menta.work OR from:street-academy.com OR subject:(仮登録 OR 本登録 OR 確認 OR 認証 OR verify OR code))
```

Narrow to the desk. Open **the thread**, not spam-looking lookalikes.

4. Parent extracts the code or magic-link. Parent **hands it to CU in the CU session**. Parent does **not** commit it. Parent does **not** forward the whole mail.

5. CU enters the code once, or opens the magic-link **in the same marketplace profile**. CU logs `gmail_otp: entered` without digits.

6. If nothing arrives in **3 minutes**: parent searches again once. If still empty: STOP (`otp_missing`). User chat. 再送は **1回まで**.

**Forbidden:** `mail.google.com` in the marketplace browser; downloading `.eml` into the repo; using a second Gmail.

Skill Shift 公開 JS: 「ご登録いただいたメールアドレスに、仮登録メールを送信しました。」→ URL クリックで本登録。期限の公式秒数は公開ページに無い → 切れても再送 1 回、それから park。

---

## 3. SMS OTP — user chat only

Two pipes. Do not mix them.

Skill Shift 個人登録の公開ラベルは **携帯連絡先 (必須)**。OTP かどうかはライブ画面。番号を git に書かない。下書き保存が電話なしでできるなら **skip 優先**。

### Sequence

1. CU reaches phone verify. **Prefer skip** if the site allows a **draft profile** without it.
2. If skip exists, skip. Record `sms: skipped`.
3. If the form **blocks draft save** without SMS:
   - Fill `{{PHONE_E164}}` / `{{PHONE}}` from the ledger **only if the user already placed it in chat this session**.
   - If not in chat, ask: “SMS for {desk}. Reply with the E.164 number to use, or say SKIP desk.”
4. After send, CU chats:

```
sms_otp_wait:
  desk: SkillShift | SOKUDAN | Anycrew | MENTA | Storeka
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

ストアカ www と MENTA 一部面は WAF が観測済み。同じ文法。Captcha that is not a hold: human-in-the-loop.

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
4. No credit card added in this serial. Card-for-signup = `card_wall` → STOP.
5. Timebox: 15–25 minutes per desk. KYC stop ends the desk immediately.
6. One desk at a time. Do not parallelize logins.
7. Skill Shift で Facebook、ストアカで LINE を「速いから」選ばない。

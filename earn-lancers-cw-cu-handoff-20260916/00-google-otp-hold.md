# MAIN Google, OTP pipes, Press & Hold

Pack: `earn-lancers-cw-cu-handoff-20260916`  
Desks: Lancers → CrowdWorks  
Audience: CU serial agent

---

## 1. MAIN Google `rimone0511`

The only Google account is **`rimone0511@gmail.com`** (`{{GOOGLE_ACCOUNT_EMAIL}}`).

| Do | Do not |
|---|---|
| Prefer **Googleで登録 / Googleではじめる / Continue with Google** when the button is visible | Click **Use another account** to add a new Google user |
| On the account picker, click **that address only** | Create a marketplace-only mailbox (`+desk@…`) |
| If Google is missing: email = the **same** MAIN Gmail | Invent Facebook / Yahoo / Apple / LINE as a new identity |
| If the address is already registered: **Sign in** | Create a second Lancers or CrowdWorks user |
| Allow only basic profile/email on the consent screen | Allow Gmail **read all mail**, Drive, or Contacts dump (`oauth_overreach` → STOP) |

Yahoo / Facebook / Apple / LINE on these two desks: **ignore** when Google is present.

If Google says the app is blocked / unverified: STOP. Morning user. Do not click through “unsafe” unless the user types GO in chat for **that desk**.

After login, if you land on a **client / 依頼者 / クライアント** home: switch to ランサー / ワーカー. If you cannot switch without KYC, treat as KYC and stop.

Browser profile: one marketplace profile. **Do not also live in Gmail in that profile.**

---

## 2. Gmail OTP — parent handles (not the CU browser)

**Parent** = the cloud agent that holds **Gmail MCP** as `rimone0511@gmail.com`.  
**CU child does not open Gmail.**

### Sequence

1. CU triggers “send code / 認証メール / メールアドレス認証” on the marketplace.
2. CU chats the parent (out of band of the browser):

```
otp_request:
  desk: Lancers | CrowdWorks
  channel: gmail
  to: MAIN Google (do not print if you already know)
  from_hint: lancers.jp / crowdworks.jp / no-reply@…
  requested_at_jst: <timestamp>
  field: 6-digit | magic-link | unknown
```

3. Parent searches Gmail MCP, for example:

```
newer_than:1d (from:lancers.jp OR from:crowdworks.jp OR subject:(code OR verify OR 確認 OR 認証 OR ワンタイム OR 本登録))
```

Narrow to the desk. Open **the thread**, not spam-looking lookalikes.

4. Parent extracts the code or magic-link. Parent **hands it to CU in the CU session**. Parent does **not** commit it. Parent does **not** forward the whole mail.

5. CU enters the code once. CU logs `gmail_otp: entered` without digits.

6. If nothing arrives in **3 minutes**: parent searches again once (Promotions / Updates via query, not by CU clicking Gmail). If still empty: STOP (`otp_missing`). User chat.

**Forbidden:** `mail.google.com` in the marketplace browser; downloading `.eml` into the repo; using a second Gmail.

Magic-link exception: if the mail is **only** a link, parent returns the URL to CU. CU opens it **in the same marketplace profile**. Third-party blogs say Lancers confirmation mail can expire in **48 hours** — if expired, CU may click 再送 **once**, then park.

Lancers official FAQ: social login (Google / Yahoo / Facebook / LinkedIn) sets **no password** at signup. Do not invent one. Do not run password-reset unless the morning user asks. Help: https://www.lancers.jp/faq/A1011/649

---

## 3. SMS OTP — user chat only

Two pipes. Do not mix them. Do not use phone-as-email. Do not use Gmail to receive SMS.

### Sequence

1. CU reaches phone verify. **Prefer skip** if the site allows a **draft profile** without it. We are not publishing and not withdrawing.
2. If skip exists, skip. Record `sms: skipped`.
3. If the form **blocks draft save** without SMS:
   - Fill `{{PHONE_E164}}` from the ledger **only if the user already placed it in chat this session**.
   - If not in chat, ask: “SMS for {desk}. Reply with the E.164 number to use, or say SKIP desk.”
4. After send, CU chats:

```
sms_otp_wait:
  desk: Lancers | CrowdWorks
  masked_on_screen: ***1234   # only what the page shows
  action_needed: paste the SMS code in this chat
  do_not_send: full number, ID photos
```

5. Wait. Do not poll the phone. Do not use SMS-to-email gateways. Do not use a virtual-number service.
6. User pastes the code. CU enters it once. Log `sms_otp: entered` without digits.
7. If the user is asleep / unavailable: **park the desk** (`sms_wait_user`). Continue to the **next** desk that does not need SMS. Max **one** resend, then park.

Voice-call fallback: treat as SMS (user must listen). CU does not place the call.

If the phone step asks for ID, selfie, or a paid ID vendor, treat it as KYC and **stop**.

Do not type `{{PHONE_E164}}` into git.

---

## 4. Press & Hold — `holdDurationMs` is mandatory

When the UI needs a hold, the CU tool call **must** include **`holdDurationMs`** (integer, milliseconds).

These are **Press & Hold** (or drag), not clicks:

- Labels: `Press and Hold`, `Press & Hold`, `長押し`, `押し続ける`, `Hold to confirm`, `Hold the button`
- Cloudflare / some bot walls: **Press & Hold** to continue
- Long-press to open a context menu
- Slider thumbs that only move after a grab
- Drag-and-drop avatar: **press (hold) → move → release**

Do **not**:

- Click, `sleep`, click again
- Repeat `mouse_down` without a duration
- Assume 100ms is enough because a click is 100ms
- Hammer the checkbox

**Starting values (adjust once, then record):**

| UI class | `holdDurationMs` | Then |
|---|---|---|
| Long-press menu | `800` | Release; click the menu item separately |
| Cloudflare / bot “Press & Hold” | `1800` | If it fails, retry **once** at `2500`. Second fail → STOP (`hold_failed`) |
| “Hold to confirm” submit | `2000` | Watch for progress ring; do not release early |
| Drag start (avatar / slider) | `400` hold, then move | Release on drop target |
| Mobile-style tab bar long-press | `600` | Rare on desktop; still set the param |

**Tool-call shape (logical; map onto the live CU schema):**

```yaml
action: press_and_hold          # or mouse_down / pointer_down — live schema wins
target: <visible button whose label is Press & Hold / 長押し>
holdDurationMs: 1800            # REQUIRED — never omit on hold intents
# optional:
reason: "Cloudflare press-and-hold on CrowdWorks signup"
```

If the current CU schema has **no** `holdDurationMs` field, **STOP**. Write `tool_missing_holdDurationMs`. Do not emulate. The morning user must switch the CU tool, not you.

After a successful hold, log:

```
hold: yes | target: "Press & Hold" | holdDurationMs: 1800 | result: passed
```

CrowdWorks WAF / Press & Hold is **expected**. Lancers may also show a bot wall. Same grammar.

Captcha that is not a hold: human-in-the-loop. Do not farm it.

---

## 5. OTP typing

- Click the OTP field.
- Type the code **once** (no leading spaces).
- Do not paste OTP into chat, git, or a second site.
- If the field is one box per digit, type sequentially; do not click the first box 6 times without characters.

---

## 6. Preflight (once per session)

1. Confirm you are the CU serial agent for **this** handoff, not a pack-author.
2. Viewport: desktop width ≥ 1280px.
3. If a previous CU left a **different** Google user signed in, sign **out**, then sign in `rimone0511`. If you cannot tell which user, STOP and ask.
4. No credit card added in this serial. Card-for-signup = `card_wall` → STOP.
5. Timebox: 15–25 minutes per desk. KYC stop ends the desk immediately.
6. One desk at a time. Do not parallelize logins.

# MAIN Google, OTP pipes, Press & Hold（Coconala JOBS）

Pack: `earn-jobs-coconala-first-gig-full-paste-20260916`  
Desk: ココナラ（already registered / QUEUE `done-draft`）  
Audience: CU agent filling the **first service 下書き**

---

## 1. MAIN Google `rimone0511`

The only Google account is **`rimone0511@gmail.com`** (`{{GOOGLE_ACCOUNT_EMAIL}}`).

| Do | Do not |
|---|---|
| Click **Googleでログイン / Googleではじめる** when visible | **新規会員登録** as a second identity |
| Picker: **that address only** | `Use another account` to add a new Google user |
| If already in: stay in. Fill the listing | Create `+coconala@` or a desk-only mailbox |
| Allow basic profile/email only | Gmail read-all / Drive / Contacts dump (`oauth_overreach` → STOP) |

Yahoo / Facebook / Apple / LINE: **ignore** when Google is present.

If the session lands on 購入者ホーム: switch to 出品者 / 出品モード. If switch requires KYC, stop.

Browser profile: marketplace only. **Do not also live in Gmail in that profile.**

---

## 2. Gmail OTP — parent handles (not the CU browser)

**Parent** = the cloud agent that holds **Gmail MCP** as `rimone0511@gmail.com`.  
**CU child does not open Gmail.**

1. CU triggers メール認証 if it appears.
2. CU chats the parent:

```
otp_request:
  desk: Coconala
  channel: gmail
  from_hint: coconala.com / no-reply@
  requested_at_jst: <timestamp>
  field: 6-digit | magic-link | unknown
```

3. Parent searches Gmail MCP, for example:

```
newer_than:1d (from:coconala.com OR subject:(確認 OR 認証 OR コード OR verify))
```

4. Parent hands the code or magic-link to CU. Do not commit it.
5. CU enters once. Log `gmail_otp: entered` without digits.
6. Empty after **3 minutes** + one parent re-search: `otp_missing`. Stop.

**Forbidden:** `mail.google.com` in the marketplace browser; `.eml` in git; a second Gmail.

---

## 3. SMS OTP — user chat only

Prefer **skip** if a 下書き can save without phone. We are not publishing and not withdrawing.

If SMS blocks even a draft:

```
sms_otp_wait:
  desk: Coconala
  masked_on_screen: ***1234
  action_needed: paste the SMS code in this chat
  do_not_send: full number, ID photos
```

Wait. One resend max, then `sms_wait_user`. Do not use virtual numbers.

---

## 4. Press & Hold

Coconala / Cloudflare interstitial is possible. Always set **`holdDurationMs`**.

- First try: `1800`
- One retry: `2500`
- Schema has no field: **STOP the session** (do not click through a bot wall blindly)

---

## 5. What this file is not

Not a signup pack. Not a GO to 公開. Not a reason to complete 本人確認 so that 「出品できるようにする」.

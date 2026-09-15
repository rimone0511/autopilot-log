# MAIN Google, OTP pipes, Press & Hold — this 3-desk serial

Pack: `earn-workship-sokudan-offers-serial-cu-20260916`  
Desks: **Workship → SOKUDAN → Offers**  
Audience: CU serial agent

Full protocol (holdDurationMs, parent Gmail search shape, resend-once) は本文複製しない。正本:

[PR#33 `00-google-otp-hold.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-skillshift-sokudan-menta-deep-0734/earn-skillshift-sokudan-menta-deep-20260916/00-google-otp-hold.md)

Skill Shift / ストアカの `NOT_OFFERED_OAUTH` 行は **この直列では使わない**（3机とも PREFER_GOOGLE）。

---

## 1. MAIN Google

The only Google account is **`{{GOOGLE_ACCOUNT_EMAIL}}`** (QUEUE / runbook と同じ MAIN。ピッカーに出る既知の運用アドレス以外を選ばない).

| Do | Do not |
|---|---|
| 3机とも **Googleで登録 / Googleでログイン** | **Use another account** で新しい Google を足す |
| ピッカーは **そのアドレスだけ** | 机専用メール（`+desk@…`）を作る |
| 既に登録済みなら **ログイン** | 同じ机に二件目を作る |
| 同意は basic profile/email だけ | Gmail **read all** / Drive / Contacts dump（`oauth_overreach` → STOP） |
| Workship でアイコンに Google と書いてあることだけ確認 | Facebook / LINE / Apple / X を新しい身分にする |

If Google says the app is blocked / unverified: STOP. Morning user. Do not click through “unsafe” unless the user types GO in chat for **that desk**.

After login, if you land on **企業 / 求人事業者 / クライアント / 発注者**: switch to 個人 / 人材 / ワーカー. If you cannot switch without KYC, treat as KYC and stop.

Browser profile: one marketplace profile. **Do not also live in Gmail in that profile.**

### Per-desk Google (this-run public GET, no signup)

| Desk | Preference | Evidence (2026-09-16) |
|---|---|---|
| Workship | **PREFER_GOOGLE** | `/signup` は `SNSで登録` + FirebaseUI コンテナ。静的 HTML に Google 文字列なし。ヘルプ how_to/44 は SNS アイコン。**クリック時に Google ラベルを目視**。無ければメール = 同じ MAIN Gmail |
| SOKUDAN | **PREFER_GOOGLE** | `/signup/pro` `alt="Google で登録"` → `/users/auth/google?category=signup&usage_type_id=1`。Facebook「推奨」は使わない。GitHub は公開リポジトリと一致するときだけ次点 |
| Offers | **PREFER_GOOGLE** | `/worker/signup` 「**Google**で登録する」→ `/oauth/worker_signup/google`。GitHub は次点可。X / LinkedIn を新規に作らない。`/signup` は 404 |

---

## 2. Gmail OTP — parent handles (not the CU browser)

**Parent** = Gmail MCP を持つクラウド側。  
**CU child does not open Gmail.**

Workship 公式ヘルプ: 確認 URL は **24時間**。切れても再送 **1回**、それから `otp_missing`。

SOKUDAN / Offers は Google 経路ならメール OTP は出にくい。メールフォールバック時だけ親に `otp_request`。

`from_hint` の例（秘密ではないドメイン）: `goworkship.com` | `sokudan.work` | `offers.jp` | `no-reply@…`

CU logs `gmail_otp: entered` **without digits**.

---

## 3. SMS

User chat. Do not guess. One resend then `sms_wait_user` and park **that desk**. You may continue to the next desk if the browser profile is not locked.

---

## 4. Press & Hold

If Press & Hold / 長押し / Cloudflare hold appears, the tool call **must** include `holdDurationMs` (start **1800**; one retry **2500**). Click+sleep is not a hold. If the schema has no such field: STOP (`tool_missing_holdDurationMs`).

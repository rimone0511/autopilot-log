# ORDER — Wave B alive CU serial (prep)

**DRAFT_ONLY.** Prep for a later computer-use (CU) pass. This folder’s authoring agent did **not** sign up, log in, apply, or publish.

| | |
|---|---|
| Folder | `ops/earn/waveb-alive-cu-serial-20260916/` |
| Observed | **2026-09-16 JST** (logged-out public GET only) |
| Live CU | **not started.** Wave A `pending` / `blocked_skip` still blocks Wave B play ([PR#54](https://github.com/rimone0511/autopilot-log/pull/54)) |
| Secrets | none. No CSRF / OTP / tokens in git |

Desk **IDs in this folder are local labels.** Canonical WAVE letters stay in [PR#1](https://github.com/rimone0511/autopilot-log/pull/1) `QUEUE.md`. Canonical CU numbers stay in [PR#8](https://github.com/rimone0511/autopilot-log/pull/8). **Do not invent CU-29+.**

---

## ID crosswalk (read first)

| This folder | Desk | QUEUE | INDEX CU | Sibling gate |
|---|---|---|---|---|
| **B01** | SOKUDAN | **B1** | **CU-13** | [PR#12](https://github.com/rimone0511/autopilot-log/pull/12) `pass` |
| **B02** | Workship（ワークシップ） | **B2** | **CU-11** | PR#12 `pass` |
| **B06** | Skill Shift | **B16** | **CU-27** | PR#12 `pass` (host = `skill-shift.com`) |
| **B07** | ITプロパートナーズ | **B17** | **CU-28** | PR#12 `pass` |
| **B09** | Workshift（ワークシフト） | **not in QUEUE** | **none — do not invent** | [PR#13](https://github.com/rimone0511/autopilot-log/pull/13) `pass` |
| **B19** | Offers | **B14** | **CU-25** | PR#12 `pass` |

Do **not** confuse:

| This-folder ID | is not |
|---|---|
| B02 Workship `goworkship.com` | B09 Workshift `workshift-sol.com` |
| B06 Skill Shift | QUEUE B6 = MENTA ([PR#61](https://github.com/rimone0511/autopilot-log/pull/61) local B11) |
| B07 ITプロパートナーズ | QUEUE B7 = ストアカ (PR#61 local B12) |
| B09 Workshift | QUEUE B9 = PeoplePerHour ([PR#59](https://github.com/rimone0511/autopilot-log/pull/59) local B14) |
| B19 Offers | PR#59 local B14 = PeoplePerHour |
| B09 Workshift | DMM 生成AI人材バンク (QUEUE外, still `needs_check` in [PR#19](https://github.com/rimone0511/autopilot-log/pull/19)) |

[PR#50](https://github.com/rimone0511/autopilot-log/pull/50) is a **3-desk subset** (Workship → SOKUDAN → Offers = pass ∩ PREFER_GOOGLE). This folder is the **six alive desks**, including mailbox-only desks. Do not play PR#50 as if Skill Shift / ITプロ / Workshift were in it.

---

## Serial (this folder)

When Wave A `pending` rows are `draft_saved` or still parked `blocked_skip`, play **one desk at a time**:

```
B02 Workship
 → B01 SOKUDAN
 → B19 Offers
 → B06 Skill Shift
 → B07 ITプロパートナーズ
 → B09 Workshift
```

| Play | ID | Desk | Google this GET | Entry (worker / 人材) |
|---|---|---|---|---|
| 1 | B02 | Workship | **PREFER_GOOGLE** (FirebaseUI `GoogleAuthProvider`; icon label at click-time) | https://goworkship.com/signup |
| 2 | B01 | SOKUDAN | **PREFER_GOOGLE** (`alt="Google で登録"`) | https://sokudan.work/signup/pro |
| 3 | B19 | Offers | **PREFER_GOOGLE** (`data-testid="auth-google"` → `/oauth/worker_signup/google`) | https://offers.jp/worker/signup |
| 4 | B06 | Skill Shift | **NOT_OFFERED_OAUTH** → MAIN mailbox | https://www.skill-shift.com/sign-up |
| 5 | B07 | ITプロパートナーズ | **NOT_OFFERED_OAUTH** → MAIN mailbox | https://itpropartners.com/register |
| 6 | B09 | Workshift | **NOT_OFFERED_OAUTH** this GET (mail / Facebook / LinkedIn / GitHub; **no** `/google/login`) | https://workshift-sol.com/registration/mail_start |

Why this order (not folder-ID order, not QUEUE B1-first):

1. INDEX CU-11 Workship is the Week2 start ([PR#8](https://github.com/rimone0511/autopilot-log/pull/8)).
2. The three PREFER_GOOGLE desks match PR#50, then mailbox desks.
3. Workshift last: QUEUE外, Google unconfirmed, 現地カード混在, `/jobs/search` CAPTCHA.

Timebox: **15–25 min / desk**. Stuck > 10 min on one modal → park, next desk.

Paste bodies live in sibling packs. **Do not duplicate bios here.** Live form wins. Short notes: each desk’s `CU-NOTE.md`. Shared identity wall: [STOP-KYC.md](STOP-KYC.md). Box: [STATUS.md](STATUS.md).

---

## Skip rules (hard)

Skip = park that desk (`blocked_skip` / `kyc_wait` / `otp_missing` / `sms_wait_user` / `blocked_paid_plan` / `no_draft_path`). **Then the next desk in this serial is allowed** unless the whole browser session is locked.

### Do not open (not this serial)

| Skip | Why |
|---|---|
| Wave A desks | Still the live CU box ([PR#54](https://github.com/rimone0511/autopilot-log/pull/54): Contra → Craudia → Freelancer.com). This folder does not jump the queue. |
| B03 複業クラウド / B04 CrowdLinks / B05 AI CrowdWorks | [PR#62](https://github.com/rimone0511/autopilot-log/pull/62) still `needs_check` |
| Anycrew / MENTA / ストアカ | PR#61 gate records. Not these six. |
| Guru / PPH / Malt / Workana / Freelancermap / YOUTRUST | GLOBAL / other local B-ids. PPH seller `blocked_paid_plan` in PR#59 |
| Shufti / カイコク / DMM 生成AI人材バンク | Not this list. DMM remains `needs_check` (PR#19) |
| Client / 企業 / 発注者 consoles | Wrong role. Leave. |
| `skillshift.jp` | DNS fail this GET and PR#12. Use `www.skill-shift.com` |
| Offers `/signup` | **404** this GET. Worker path is `/worker/signup` |
| Workship `enterprise.goworkship.com` | Client marketing |

### Skip on the live desk (then next)

| Trigger | Code | Do |
|---|---|---|
| 免許 / マイナンバー / 顔 / 住民票 / 口座 / eKYC / 自撮り | `kyc_wait` | Close upload. Morning user. See [STOP-KYC.md](STOP-KYC.md) |
| 有料会員 / 前払い必須 / ブース / 審査スキップ SKU | `blocked_paid_plan` | Do not pay. Do not invent yen |
| 応募 / エントリー / 話を聞きたい / スカウト承諾 | — | Never. Looking at a card ≠ applying |
| 現地のみ / 常駐のみ / 展示会現地カード | — | Do not apply that row. Desk stays in serial |
| Gmail OTP needed | `otp_missing` until parent Gmail MCP | CU does **not** open `mail.google.com` |
| SMS OTP, user away | `sms_wait_user` | Wait on user chat. Do not guess |
| Press & Hold without `holdDurationMs` | `hold_failed` / `tool_missing_holdDurationMs` | Do not fake click+sleep |
| Google picker “Use another account” | — | STOP. No second identity |
| OAuth wants Gmail-read-all / Drive / Contacts dump | `oauth_overreach` | Deny. Park |
| Facebook / LINE / Apple / new X as identity | — | Skip. Workshift: **email = MAIN mailbox**, not new Facebook |
| Rate / fee % missing and form requires a number | `rate_empty` | Park. Do not invent |
| Already a member on MAIN Google / same mailbox | `already_member_draft` | Login, draft only, no second account |
| Pack file missing in checkout | `pack_missing` | Use live form + this CU-NOTE. Do not invent a third bio |

### Never (all six)

- Secrets in git / session log (OTP, password, phone digits, CSRF, ID crop)
- Invented traffic, GMV, 「○万人」, sitemap counts, pagination totals as activity proof
- Invented worker fee % (cite official page or leave `needs_check`)
- Publishing profiles / listings
- Autopilot Log posting-gate changes
- Signup from **this** markdown-authoring pass

---

## GO / NO-GO (one screen)

| Switch | Value |
|---|---|
| Account | MAIN Google `{{GOOGLE_ACCOUNT_EMAIL}}` only. Mailbox desks use the **same** mailbox |
| Publish | `DRAFT_ONLY` |
| KYC | Stop. No uploads |
| This PR | Prep. Not a signup GO |

Viewport: desktop **≥ 1280px**.

OTP: mail → parent Gmail MCP. SMS → user chat. Hold: `holdDurationMs` 1800, one retry 2500.

---

## After each desk (secret-free)

```
desk: Workship | SOKUDAN | Offers | Skill Shift | ITプロパートナーズ | Workshift
pack: ops/earn/waveb-alive-cu-serial-20260916/bXX-.../CU-NOTE.md
auth: google-main | email-same-mailbox | already_member | blocked
otp: gmail-parent | sms-chat | none | otp_missing | sms_wait_user
kyc: none | wait-morning + type
draft_profile: yes/no
publish: no
apply: no
next: <next play desk | stop>
```

Valid outcomes: `done-draft` | `already_member_draft` | `kyc_wait` | `sms_wait_user` | `no_draft_path` | `otp_missing` | `hold_failed` | `card_wall` | `oauth_overreach` | `rate_empty` | `blocked_paid_plan`.

Not success: 「応募した」「公開した」「本人確認済み」「有料にした」。

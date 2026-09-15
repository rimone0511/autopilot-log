# STATUS — Skill Shift + Workshift short CU notes

> **DRAFT_ONLY.** Profile-draft notes only. **No signup from this PR.** No publish. No 応募.
> **No secrets.** No passwords, OTP, CSRF, cookies, phone digits, ID photos.
> **No invented fees / traffic / GMV.** Pagination `meta` totals are not activity proof — do not write them.
> **MAIN Google mailbox only.** `{{EMAIL}}` / `{{GOOGLE_ACCOUNT_EMAIL}}`. Do not create Facebook / LinkedIn / GitHub for these desks.

Snapshot: **2026-09-16 JST**  
Folder: `ops/earn/skillshift-workshift-cu-notes-20260916/`  
State: **DRAFT_ONLY** / `pack_ready` + `pending`  
Authoring: logged-out public GET + URLs already confirmed in sibling packs. **No POST. No cookies saved.**

This box is **two short CU notes** (B06 Skill Shift, B09 Workshift). It does not copy thick JA bios. It is **not** a signup GO.

Wave B **register** serial in [PR#72](https://github.com/rimone0511/autopilot-log/pull/72) is **REGISTER-CU-CUT**. Default after Freelancer.com: stay on **JOBS** (do-not-send). Do **not** treat this folder as next live CU unless a human types GO for **one** of these desks.

Python posting-gate tests were **not** edited.

---

## CU hint (this folder)

| Hint | Meaning here |
|---|---|
| `pack_ready` | The two `CU-NOTE.md` files exist. **Not** a play GO |
| `pending` | Live CU has **not** marked a draft on these desks from **this** folder |
| `draft_saved` | Fill only after a real CU run |
| `blocked_skip` | Skip this pass for the listed reason |
| `kyc_wait` | Identity screen. Morning user. No upload |
| `register_cu_cut` | Register serial cut (PR#72). Prefer JOBS unless human GO |

Current rows (authoring time): both `pack_ready` + `pending`.

---

## ID crosswalk (read first)

These folder ids are **local labels**. Do not mix with QUEUE letters.

| This folder | Desk | QUEUE (PR#1) | INDEX CU (PR#8) | Do not confuse with |
|---|---|---|---|---|
| **B06** | Skill Shift | **B16** | **CU-27** | QUEUE **B6 = MENTA** |
| **B09** | Workshift（ワークシフト） | **not in QUEUE** | **none — do not invent CU-29** | **Workship** `goworkship.com` (B02 / CU-11). QUEUE **B9 = PeoplePerHour**. DMM 生成AI人材バンク |

---

## Rollup

| This folder | Official | Google this GET | activity_gate (sibling) | Signup path | Fees | CU hint |
|---|---|---|---|---|---|---|
| B06 Skill Shift | https://www.skill-shift.com/ | **NOT_OFFERED_OAUTH** (GTM / Analytics / Fonts only in signup HTML). Mailbox = MAIN | **pass** [PR#12](https://github.com/rimone0511/autopilot-log/pull/12) | https://www.skill-shift.com/sign-up | 個人％ **unstated** this GET → 作らない | `pack_ready` + `pending` |
| B09 Workshift | https://workshift-sol.com/ | **NOT_OFFERED_OAUTH** (mail / Facebook / LinkedIn / GitHub; **no** `/google/login`) | **pass** [PR#13](https://github.com/rimone0511/autopilot-log/pull/13) | https://workshift-sol.com/registration/mail_start | ％ **unstated** this GET → 作らない | `pack_ready` + `pending` |

Live CU `draft_saved` from this folder: **0**.

---

## This GET (2026-09-16, no login)

### B06 Skill Shift

- `https://www.skill-shift.com/` **200** — title「【Skill Shift】地方副業で貢献を｜地域企業✕副業プロジェクト」
- `/sign-up` **200** SPA shell. meta:「Skill Shiftの個人登録ページです。」 Google strings = Tag Manager / Analytics / Fonts. **No** OAuth control in this HTML
- `/terms-of-service` **200** — title「利用規約」
- `GET /api/jobs` **200** — `is_recruiting: true`. Leading `created_at` **2026-09-14 / 13 / 12 / 11**. Example position「AI活用で業務効率化！業務棚卸しから始めるAIアドバイザー」（`side_job_style`: オンライン想定). Another: リモート中心（必要に応じて現地訪問のご相談あり）
- `https://skillshift.jp/` **DNS fail** (same as PR#12 / PR#19 / PR#33 / PR#72)

**Do not write** `meta` / pagination totals.

### B09 Workshift

- `https://workshift-sol.com/` **200** — title「クラウドソーシングで海外進出支援「ワークシフト」Workshift」。 Links `/jobs/view/13758`, `13757`, `13756`
- Company site `https://workshift-sol.co.jp/` **200** — 会社. **Not** the worker signup
- `/jobs/view/13758` **200** — SIAL Paris 現地日英通訳 (10/17–10/21). 仕事掲載日 **2026-09-11**. 「本人確認: 無し」on **this** card. **Do not apply** (現地)
- `/jobs/search` **200** — CAPTCHA / reCAPTCHA present. Listing dates unread here. Path `/job/search` is wrong (PR#13: 404)
- `/registration/mail_start` **200** — `facebook/login`, `linkedin/login`, `github/login`, mail_start. **No** `/google/login`
- `/pages/term` **200** — **2026年4月11日改定**

Fee % unstated this GET → 作らない. Company-page headcount is marketing, not activity.

---

## Google path (both desks)

| Desk | Path | If a Google button appears live |
|---|---|---|
| B06 | Email = `{{EMAIL}}` (same MAIN mailbox). Skip new Facebook | Then and only then **PREFER_GOOGLE**. Note it. Still no second account |
| B09 | Email = `{{EMAIL}}` at `/registration/mail_start`. Skip new Facebook / LinkedIn / GitHub | Same: only if a `/google/login` (or labeled Google) is **visible**. This GET: not offered |

Picker: MAIN only. **Use another account** = STOP. OAuth Gmail-read-all / Drive / Contacts = `oauth_overreach` → deny.

OTP: mail → parent Gmail MCP. CU does **not** open `mail.google.com`. SMS → user chat. Do not guess.

---

## Stop rules (shared)

Skip = park that desk. Do **not** invent a workaround.

| Trigger | Code | Do |
|---|---|---|
| 免許 / マイナンバー / 顔 / 住民票 / 口座 / eKYC / パスポート / 自撮り | `kyc_wait` | Close upload. Morning user. No file |
| Skill Shift「本人確認サービス」資料 | `kyc_wait` | Stop. See B06 note |
| Workshift card「本人確認: Yes」or upload | `kyc_wait` | Stop even if another card said 無し |
| 有料会員 / 前払い必須 / ウォレット最低残高 | `blocked_paid_plan` | Do not pay. Do not invent yen |
| 応募 / 提案 / エントリー / スカウト承諾 | — | Never. Looking at a card ≠ applying |
| 現地のみ / 常駐のみ / 展示会現地カード | — | Do not apply that row. Desk may stay |
| Gmail OTP needed | `otp_missing` until parent Gmail MCP | No `mail.google.com` in the CU browser |
| SMS OTP, user away | `sms_wait_user` | Wait on user chat |
| Press & Hold without `holdDurationMs` | `hold_failed` | Do not fake click+sleep |
| Facebook / LINE / Apple / new X as identity | — | Skip. Mailbox = MAIN |
| Rate / fee % missing and form requires a number | `rate_empty` | Park. Do not invent |
| Already a member on MAIN mailbox | `already_member_draft` | Login, draft only, no second account |
| `skillshift.jp` / `skillshift.global` | — | Wrong host. Use `www.skill-shift.com` |
| Workship `goworkship.com` | — | Wrong desk. Do not paste Workship bios here |
| Client / 企業 / 発注者 consoles | — | Leave |
| Human GO missing (default) | `register_cu_cut` | Prefer JOBS. Do not start from this PR |

### Never (both)

- Secrets in git / session log (OTP, password, phone digits, CSRF, ID crop)
- Invented traffic, GMV, 「○万人」, sitemap counts, pagination totals as activity proof
- Invented worker fee %
- Publishing profiles / listings
- Autopilot Log posting-gate changes
- Signup from **this** markdown-authoring pass

---

## Files

| File | Role |
|---|---|
| [b06-skill-shift/CU-NOTE.md](b06-skill-shift/CU-NOTE.md) | Short CU note: URLs, Google path, stop rules |
| [b09-workshift/CU-NOTE.md](b09-workshift/CU-NOTE.md) | Short CU note: URLs, Google path, stop rules |

Thick paste bodies stay in siblings. **Do not duplicate bios here.** Live form wins.

| Desk | Thick / gate (pointer only) |
|---|---|
| B06 | [PR#33 `01-skill-shift.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-skillshift-sokudan-menta-deep-0734/earn-skillshift-sokudan-menta-deep-20260916/01-skill-shift.md) · [PR#12 gate](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-activity-gate-waveb-jp-fced/earn-activity-gate-waveB-20260916/records/08-skill-shift.md) · [PR#72 serial note](https://github.com/rimone0511/autopilot-log/blob/cursor/waveb-alive-cu-serial-5788/ops/earn/waveb-alive-cu-serial-20260916/b06-skill-shift/CU-NOTE.md) |
| B09 | [PR#13 gate](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-activity-gate-waved-b552/earn-activity-gate-waveD-20260916/records/08-workshift.md) · [PR#19 catalog-gap](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-freelancer-waveb-gap-notes-40b7/earn-freelancer-waveb-gap-notes-20260916/waveb-catalog-gap/04-workshift.md) · [PR#72 serial note](https://github.com/rimone0511/autopilot-log/blob/cursor/waveb-alive-cu-serial-5788/ops/earn/waveb-alive-cu-serial-20260916/b09-workshift/CU-NOTE.md). **No thick JA bio pack.** Do not invent a bio |

---

## After a live desk (secret-free; only if human GO)

```
desk: Skill Shift | Workshift
pack: ops/earn/skillshift-workshift-cu-notes-20260916/bXX-.../CU-NOTE.md
auth: email-same-mailbox | already_member | blocked
otp: gmail-parent | sms-chat | none | otp_missing | sms_wait_user
kyc: none | wait-morning + type
draft_profile: yes/no
publish: no
apply: no
next: park | other desk | stop
```

Valid outcomes: `done-draft` | `already_member_draft` | `kyc_wait` | `sms_wait_user` | `no_draft_path` | `otp_missing` | `hold_failed` | `oauth_overreach` | `rate_empty` | `blocked_paid_plan` | `register_cu_cut`.

Not success: 「応募した」「公開した」「本人確認済み」「有料にした」。

---

## This PR does not

- Create accounts or complete OAuth
- Upload KYC
- Apply / publish / pay
- Add Workshift to QUEUE or invent CU-29
- Copy sibling bios
- Claim Skill Shift job counts or Workshift GMV
- Start Wave B register serial (cut in PR#72)

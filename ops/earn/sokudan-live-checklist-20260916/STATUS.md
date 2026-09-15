# STATUS — SOKUDAN live-register field checklist

> ## REGISTER-CU-CUT
>
> **2026-09-16.** This SOKUDAN **register** checklist is **not** next live CU.
> Prefer **JOBS phase** (`register-winddown` / jobs-first).
> **Do not** open `sokudan.work` / `/signup/pro` / Google OAuth from this folder.
> After Freelancer (or any Wave A park): stay on JOBS (do-not-send bids / listings / week plan). Do **not** chain into B01 SOKUDAN.
> Field order below stays **DRAFT_ONLY** archive for a later human GO. **Not a signup GO.**

Snapshot: **2026-09-16**  
Folder: `ops/earn/sokudan-live-checklist-20260916/`  
State: **DRAFT_ONLY** / **REGISTER-CU-CUT** (prep, not next CU)  
Authoring: 公開 GET / 公式 FAQ（トップ） / 規約 / プライバシーのみ。**アカウント作成なし。OAuth 未完走。POST なし。**

This file is a desk box for **CU-13 / QUEUE B1**. It does not claim a SOKUDAN account exists. It does not rewrite Wave B snapshots in sibling PRs. **Cut overrides play:** do not start this desk from a Freelancer `done-draft` or as the next live CU.

Forbidden: secrets, live phones/passwords/OTP/DOB, KYC files, signup from this authoring agent, 応募, 審査書類アップロード, invented traffic/GMV/fee %.

---

## Verdict

| Item | Status |
|---|---|
| This checklist pack | **ready · draft** (markdown only). **REGISTER-CU-CUT** |
| Live CU Google → profile draft | **not run** — **do not run next**. Prefer JOBS |
| SOKUDAN account | **not claimed** |
| Phone / DOB | **do not type** — required → STOP |
| 審査書類 / 応募 | **STOP — not this pack** |
| Gmail OTP | **allowed** (parent MCP; not used this authoring session) |
| SMS | **skip** (no phone) |

---

## CU hint (this desk)

| Hint | Meaning here |
|---|---|
| `pack_ready` | Files exist. **Not** a play GO. Default `register_cu_cut` |
| `pending` | Live CU has **not** marked a draft from **this** folder |
| `register_cu_cut` | Register cut. **Not** next live CU. Prefer JOBS phase |
| `draft_saved` | Talent profile parked unpublished (fill only after a later human GO + real CU run) |
| `phone_required_stop` | Phone required to save; this pack does not type a number |
| `dob_required_stop` | DOB required to save; this pack does not invent a date |
| `blocked_skip` | Skip this pass. Do not retry the listed reason |
| `kyc_wait` | 審査書類 / 本人確認画面。朝の本人。アップロードなし |
| `apply_stop` | 応募 / エントリー / スカウト返信 CTA。押していない |

Current row (authoring time):

| # | desk | CU hint | reason | next action |
|---|---|---|---|---|
| B1 / CU-13 | SOKUDAN ソクダン | `pack_ready` + `register_cu_cut` | Checklist written. **Do not play.** | Stay JOBS-first. Do **not** open SOKUDAN as next live CU |

Wave B context (pointers only): activity gate [PR#12](https://github.com/rimone0511/autopilot-log/pull/12) = **pass**. Serial [PR#50](https://github.com/rimone0511/autopilot-log/pull/50) places this desk after Workship, before Offers. Wave B serial [PR#72](https://github.com/rimone0511/autopilot-log/pull/72) is already **REGISTER-CU-CUT**. This pack does **not** start those desks and does **not** reopen the serial.

JOBS-first (do-not-send): [PR#88](https://github.com/rimone0511/autopilot-log/pull/88) TODAY apply queue · [PR#76](https://github.com/rimone0511/autopilot-log/pull/76) 7-day week plan · [PR#80](https://github.com/rimone0511/autopilot-log/pull/80) board scan · [PR#68](https://github.com/rimone0511/autopilot-log/pull/68) Freelancer bids.

---

## Pack files

| File | What CU does |
|---|---|
| [CHECKLIST.md](CHECKLIST.md) | Field order **on file**. Default **do not play**. STOP 電話必須 / 生年月日必須 / KYC / 応募 |
| [FIELD-MAP.md](FIELD-MAP.md) | Safe JA paste（キャッチ 30/12、bio 200/800/nourl、スキル）。phone/DOB empty. For a later GO only |
| [STATUS.md](STATUS.md) | This box. **REGISTER-CU-CUT.** Not a live-run log |

---

## Complement (bodies not copied as source of truth)

| PR | Folder | Relation |
|---|---|---|
| [#33](https://github.com/rimone0511/autopilot-log/pull/33) | `earn-skillshift-sokudan-menta-deep-20260916/` | Thick paste. This pack **tightens** phone/DOB: do not type |
| [#50](https://github.com/rimone0511/autopilot-log/pull/50) | `earn-workship-sokudan-offers-serial-cu-20260916/` | 3-desk serial card. Pointer only |
| [#21](https://github.com/rimone0511/autopilot-log/pull/21) | `earn-waveb-alive-handoff-sample-20260916/` | Sample CU-13 first |
| [#3](https://github.com/rimone0511/autopilot-log/pull/3) | `earn-register-packs-jp-20260916/` | Thin inventory 01 |
| [#12](https://github.com/rimone0511/autopilot-log/pull/12) | `earn-activity-gate-waveB-20260916/records/01-sokudan.md` | Gate **pass** |
| [#72](https://github.com/rimone0511/autopilot-log/pull/72) | `ops/earn/waveb-alive-cu-serial-20260916/` | Wave B ORDER. Not this field checklist |
| [#4](https://github.com/rimone0511/autopilot-log/pull/4) | `earn-kyc-morning-checklist-20260916/` | Morning user KYC slip. This pack does not open 審査書類 |
| [#67](https://github.com/rimone0511/autopilot-log/pull/67) | `ops/earn/craudia-live-checklist-20260916/` | Sibling **pattern** (different desk) |

This folder does **not** replace those packs. It archives the live **field order** and a phone/DOB required stop. **Cut overrides play.**

---

## Public GET (this authoring session)

`thin_site_skip: false`.

UA: ordinary desktop Chrome string. No login cookie. CSRF / `authenticity_token` / reCAPTCHA sitekey values were **not** stored in git.

| URL | HTTP | Note |
|---|---|---|
| https://sokudan.work/signup/pro | 200 | 無料新規登録 ─ フリーランス・副業の方向け。IE 不可。Facebook 推奨 + Google/LinkedIn/X/GitHub。`#user_email` `#user_password`。`user[usage_type_id]=1`。`form action="/signup"`。reCAPTCHA。**POST していない** |
| https://sokudan.work/login | 200 | ログイン ─ 全ユーザー共通。Google でログイン `category=login` |
| https://sokudan.work/signup | 200 → `/login` | `/signup/pro` を使う |
| https://sokudan.work/users/confirmation/new | 200 | 認証メールの再送。`#user_email`。**POST していない** |
| https://sokudan.work/ | 200 | FAQ 人材「すべて無料」。同じ会社名は互いに見えない。案件 `updatedAt` **2026-09-15**。マーケ「リモート案件 92%」は実績に使わない |
| https://sokudan.work/pages/terms | 200 | CAMELORS株式会社。第4条 審査書類・代理人不可。第7条 AI 自己紹介。第10条 料率（％なし）。第13条 未成年者。第14条 期中審査。第24条 直接契約違約金 |
| https://sokudan.work/pages/policy | 200 | 第2条: 生年月日・電話番号は取得しうる種類。必須ラベルではない |
| https://sokudan.work/pages/privacy | **404** | `/pages/policy` を使う |
| https://sokudan.work/pages/faq | 200 → Notion | トップ HTML の FAQ を正とする |
| https://sokudan.work/business | 200 → `business.sokudan.work` | 発注者 LP。**入らない** |
| https://sokudan.work/top/projects/20955 | 200 | ログイン前 SPA。本文に「▼応募後の流れ」。**応募しない** |

Google 開始 URL は HTML 上 `data-method="post"`。この authoring セッションでは踏んでいない。

---

## After live CU (leave blank — default: do not run)

Fill only the secret-free keys. Do not paste OTP, ID, a phone, or a date of birth.

```
desk: SOKUDAN
pack: ops/earn/sokudan-live-checklist-20260916/
auth:
otp:
phone: skipped
dob: skipped
kyc: none
draft_profile:
publish: no
apply: no
holdDurationMs_used:
next: stop
saved_draft: yes/no/unknown
apply_clicked: no
kyc_opened: no
phone_typed: no
dob_typed: no
upload: none
```

Outcome so far: **not run** / **REGISTER-CU-CUT**. Valid later values (only after a human GO): `done-draft` | `already_member_draft` | `phone_required_stop` | `dob_required_stop` | `kyc_wait` | `apply_stop` | `no_draft_path` | `otp_missing` | `hold_failed` | `oauth_overreach` | `already_applied`.

---

## Next (human / CU)

1. **REGISTER-CU-CUT.** Do not open SOKUDAN as next live CU. Prefer JOBS phase.
2. Keep DRAFT. Do not merge until Yuta reviews.
3. JOBS: do-not-send pastes / week plan / apply queue on desks that already have `draft_saved`. Do not start Wave B register from this folder.
4. If register CU is ever re-opened by a **human GO**, then and only then follow [CHECKLIST.md](CHECKLIST.md) + [FIELD-MAP.md](FIELD-MAP.md). Default is **cut**.
5. Do not continue this folder into Offers / Workship.

---

## This PR / pack will not

- Copy sibling pack bodies into `earn-packs/`
- Create a marketplace account from the authoring agent
- Type a phone number or date of birth (invented or from ledger)
- Upload ID / selfie / bank / My Number
- Complete SMS
- 応募 / スカウト返信 / 発注者申込
- Invent fee % or yen rates or paste 「92%」 into the bio
- Rewrite the Wave B activity-gate pass
- Start SOKUDAN (or Wave B register serial) as next live CU after Freelancer
- Change Python posting-gate tests

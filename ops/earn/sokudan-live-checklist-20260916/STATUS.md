# STATUS — SOKUDAN live-register field checklist

Snapshot: **2026-09-16**  
Folder: `ops/earn/sokudan-live-checklist-20260916/`  
State: **DRAFT_ONLY**  
Authoring: 公開 GET / 公式 FAQ（トップ） / 規約 / プライバシーのみ。**アカウント作成なし。OAuth 未完走。POST なし。**

This file is a desk box for **CU-13 / QUEUE B1**. It does not claim a SOKUDAN account exists. It does not rewrite Wave B snapshots in sibling PRs.

Forbidden: secrets, live phones/passwords/OTP/DOB, KYC files, signup from this authoring agent, 応募, 審査書類アップロード, invented traffic/GMV/fee %.

---

## Verdict

| Item | Status |
|---|---|
| This checklist pack | **ready · draft** (markdown only) |
| Live CU Google → profile draft | **not run** from this agent |
| SOKUDAN account | **not claimed** |
| Phone / DOB | **do not type** — required → STOP |
| 審査書類 / 応募 | **STOP — not this pack** |
| Gmail OTP | **allowed** (parent MCP; not used this authoring session) |
| SMS | **skip** (no phone) |

---

## CU hint (this desk)

| Hint | Meaning here |
|---|---|
| `pack_ready` | This 3-file checklist is field-ordered. CU may type under CHECKLIST rules |
| `pending` | Live CU has **not** marked a draft from **this** folder |
| `draft_saved` | Talent profile parked unpublished (fill after a real CU run) |
| `phone_required_stop` | Phone required to save; this pack does not type a number |
| `dob_required_stop` | DOB required to save; this pack does not invent a date |
| `blocked_skip` | Skip this pass. Do not retry the listed reason |
| `kyc_wait` | 審査書類 / 本人確認画面。朝の本人。アップロードなし |
| `apply_stop` | 応募 / エントリー / スカウト返信 CTA。押していない |

Current row (authoring time):

| # | desk | CU hint | reason | next action |
|---|---|---|---|---|
| B1 / CU-13 | SOKUDAN ソクダン | `pack_ready` + `pending` | Live checklist written. No signup from this agent | CU: Google `/signup/pro` → profile **draft**. STOP if phone/DOB required. STOP KYC. STOP apply |

Wave B context (pointers only): activity gate [PR#12](https://github.com/rimone0511/autopilot-log/pull/12) = **pass**. Serial [PR#50](https://github.com/rimone0511/autopilot-log/pull/50) places this desk after Workship, before Offers. This pack does **not** start those desks.

---

## Pack files

| File | What CU does |
|---|---|
| [CHECKLIST.md](CHECKLIST.md) | Ordered fields: Google で登録 → プロフィール下書き。STOP 電話必須 / 生年月日必須 / KYC / 応募 |
| [FIELD-MAP.md](FIELD-MAP.md) | Safe JA paste（キャッチ 30/12、bio 200/800/nourl、スキル）。phone/DOB empty |
| [STATUS.md](STATUS.md) | This box. Fill the success line after a live run |

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

This folder does **not** replace those packs. It adds the live **field order** and a phone/DOB required stop.

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

## After live CU (leave blank until a run)

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

Outcome so far: **not run**. Valid later values: `done-draft` | `already_member_draft` | `phone_required_stop` | `dob_required_stop` | `kyc_wait` | `apply_stop` | `no_draft_path` | `otp_missing` | `hold_failed` | `oauth_overreach` | `already_applied`.

---

## Next (human / CU)

1. Keep DRAFT. Do not merge until Yuta reviews.
2. CU: [CHECKLIST.md](CHECKLIST.md) in order. Paste from [FIELD-MAP.md](FIELD-MAP.md). Gmail OTP via parent. Phone/DOB empty.
3. Stop if phone or DOB is required to save. Stop before 審査書類 / 応募.
4. Do not continue this folder into Offers / Workship.
5. Next Wave B desk in the serial is Offers — **not this folder**.

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
- Change Python posting-gate tests

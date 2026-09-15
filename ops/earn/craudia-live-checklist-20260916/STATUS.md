# STATUS — クラウディア live-register field checklist

Snapshot: **2026-09-16**  
Folder: `ops/earn/craudia-live-checklist-20260916/`  
State: **DRAFT_ONLY**  
Authoring: 公開 GET / 公式 FAQ / 出品ガイド / Crarepo のみ。**アカウント作成なし。OAuth 未完走。POST なし。**

This file is a desk box for **CU-09 / QUEUE A9**. It does not claim a Craudia account exists. It does not rewrite Wave A snapshots in sibling PRs.

Forbidden: secrets, live phones/passwords/OTP, KYC files, signup from this authoring agent, スキル公開, 本人確認アップロード, NDA 同意, paid plans, invented traffic/GMV.

---

## Verdict

| Item | Status |
|---|---|
| This checklist pack | **ready · draft** (markdown only) |
| Live CU register-temp → profile → skill draft | **not run** from this agent |
| Craudia account | **not claimed** |
| スキル公開 / 本人確認 / NDA | **STOP — not this pack** |
| SMS | **skip policy** ([OTP-NOTE.md](OTP-NOTE.md)) |
| Gmail OTP | **allowed** (parent MCP; not used this authoring session) |

---

## CU hint (this desk)

| Hint | Meaning here |
|---|---|
| `pack_ready` | This 3-file checklist is field-ordered. CU may type under CHECKLIST rules |
| `pending` | Live CU has **not** marked a draft from **this** folder |
| `draft_saved` | Worker profile parked unpublished (fill after a real CU run) |
| `skill_draft_saved` | Skill form saved without 公開 (fill after a real CU run) |
| `skill_draft_no_save_path` | Fields filled; live UI had no 下書き保存; 公開 not clicked |
| `blocked_skip` | Skip this pass. Do not retry the listed reason |
| `sms_skip_blocked` | Phone auth required for save; this pack does not SMS |
| `kyc_wait` | 本人確認 / 自撮り画面。朝の本人。アップロードなし |
| `nda_stop` | Extra NDA / クローズド / 非公開閲覧同意。同意なし |

Current row (authoring time):

| # | desk | CU hint | reason | next action |
|---|---|---|---|---|
| A9 / CU-09 | クラウディア Craudia | `pack_ready` + `pending` | Live checklist written. No signup from this agent | CU: register-temp → profile → skill **draft**. STOP before 公開 / 本人確認 / NDA. SMS skip |

Wave A context (pointers only): sibling board [PR#24](https://github.com/rimone0511/autopilot-log/pull/24) lists this desk `pending` after Contra. This pack does **not** start TimeTicket / Contra. It does not skip earlier `blocked_skip` desks.

---

## Pack files

| File | What CU does |
|---|---|
| [CHECKLIST.md](CHECKLIST.md) | Ordered fields: register-temp → 基本情報 / プロフィール → スキル下書き。STOP 公開 / 本人確認 / NDA |
| [OTP-NOTE.md](OTP-NOTE.md) | Gmail OTP allowed (parent MCP). SMS skip |
| [STATUS.md](STATUS.md) | This box. Fill the success line after a live run |

---

## Complement (bodies not copied)

| PR | Folder | Relation |
|---|---|---|
| [#18](https://github.com/rimone0511/autopilot-log/pull/18) | `earn-timeticket-contra-craudia-handoff-20260916/` | Thin CU-09. スキル出品しない |
| [#51](https://github.com/rimone0511/autopilot-log/pull/51) | `earn-craudia-deep-paste-20260916/` | Bio / skills paste. SMS may wait if draft is blocked |
| [#60](https://github.com/rimone0511/autopilot-log/pull/60) | `ops/earn/craudia-cu-handoff-20260916/` | PLAYBOOK + FIELD-MAP. Stop-at-KYC; スキル出品しない |
| [#4](https://github.com/rimone0511/autopilot-log/pull/4) | `earn-kyc-morning-checklist-20260916/` | Morning user KYC slip. This pack does not open 本人確認 |

This folder does **not** replace those packs. It adds the live **field order** and allows skill **draft fill** only.

---

## Public GET (this authoring session)

`thin_site_skip: false`.

| URL | HTTP | Note |
|---|---|---|
| https://www.craudia.com/app/auth/register-temp | 200 | STEP1–4 ウィザード。`#email`。Google `auth=3`。Twitter/Facebook/Yahoo `auth=1/2/4`。reCAPTCHA。**POST していない** |
| https://www.craudia.com/login | 200 | → `app.craudia.com/auth/login-form` |
| https://www.craudia.com/app/faq/contents/151 | 200 | Google / メール / SNS。認証メール → i2i |
| https://www.craudia.com/app/faq/contents/103 | 200 | 登録 = PC メール。出金時に本人確認 |
| https://www.craudia.com/app/faq/contents/47 | 200 | 満18歳以上 |
| https://www.craudia.com/app/faq/contents/92 | 200 | プロフィール編集 FAQ（見出し） |
| https://www.craudia.com/app/faq/contents/78 | 200 | ポートフォリオ = 公開可能な実績 |
| https://www.craudia.com/app/faq/contents/156 | 200 | 電話認証。**このパックは skip**。失敗時の本人確認リンクは使わない |
| https://www.craudia.com/app/faq/contents/93 | 200 | 本人確認。顔付き公的書類 + 自撮り。**入らない** |
| https://www.craudia.com/app/faq/contents/175 | 200 | スキル出品入口。下書きまで |
| https://www.craudia.com/app/guide/service/sell | 200 | ステップ1–7 入力可。ステップ8 **公開** = STOP |
| https://www.craudia.com/app/guide/skill-price | 200 | 3–15% cited unused。価格を発明しない |
| https://www.craudia.com/app/agreement | 200 | 第18条 機密保持 ≠ 追加 NDA 画面への同意 |
| https://www.craudia.com/crarepo/archives/3678 | 200 | 自己紹介に URL 不可。職歴・資格・ポートフォリオは別欄 |
| https://www.craudia.com/app/signup | 404 | register-temp を使う |

---

## After live CU (leave blank until a run)

Fill only the secret-free keys. Do not paste OTP, ID, NDA text, or a phone.

```
desk: Craudia
pack: ops/earn/craudia-live-checklist-20260916/
auth:
otp:
sms: skipped
kyc: none
nda: none
draft_profile:
skill_draft:
skill_listing_public: no
apply: no
publish: no
pro_upgrade: no
rate:
next: stop
saved_draft: yes/no/unknown
skill_publish_clicked: no
kyc_opened: no
nda_agreed: no
upload: none
```

Outcome so far: **not run**. Valid later values: `done-draft` | `already_member_draft` | `skill_draft_saved` | `skill_draft_no_save_path` | `kyc_wait` | `sms_skip_blocked` | `nda_stop` | `no_draft_path` | `otp_missing` | `hold_failed` | `card_wall` | `oauth_overreach` | `rate_empty`.

---

## Next (human / CU)

1. Keep DRAFT. Do not merge until Yuta reviews.
2. CU: [CHECKLIST.md](CHECKLIST.md) in order. Gmail OTP via parent. SMS skip.
3. Stop before 公開 / 本人確認 / NDA.
4. Do not apply. Do not buy PRO.
5. Next Wave A desk is Freelancer.com — **not this folder**.

---

## This PR / pack will not

- Copy sibling pack bodies into `earn-packs/craudia/`
- Create a marketplace account from the authoring agent
- Upload ID / selfie / bank / My Number
- Complete SMS / 050 発信
- 参加申請 / スキル **公開** / Craudia PRO
- Sign NDA / accept クローズド案件
- Invent fee % or yen rates
- Retry Wave A `blocked_skip` desks (Fiverr hold, Lancers captcha, CrowdWorks 403, Upwork Google SSO, LinkedIn reCAPTCHA)
- Change Python posting-gate tests

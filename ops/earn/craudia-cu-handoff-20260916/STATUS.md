# STATUS — クラウディア CU handoff desk

Snapshot: **2026-09-16**  
Folder: `ops/earn/craudia-cu-handoff-20260916/`  
State: **DRAFT_ONLY**  
Authoring: 公開 GET / 公式 FAQ / Crarepo / 手数料ガイドのみ。**アカウント作成なし。OAuth 未完走。POST なし。**

This file is a desk box for **CU-09 / QUEUE A9**. It does not claim a Craudia account exists. It does not rewrite Wave A snapshots in sibling PRs.

Forbidden: secrets, live phones/passwords/OTP, KYC files, signup from this authoring agent, publish, paid plans, invented traffic/GMV.

---

## CU hint (this desk)

| Hint | Meaning here |
|---|---|
| `pack_ready` | This 4-file handoff is paste-ready. CU may type under PLAYBOOK rules |
| `pending` | Live CU has **not** marked a draft on this desk from **this** folder |
| `draft_saved` | Seller/worker profile parked unpublished (fill after a real CU run) |
| `blocked_skip` | Skip this pass. Do not retry the listed reason |
| `kyc_wait` | 本人確認 / 自撮り画面。朝の本人。アップロードなし |

Current row (authoring time):

| # | desk | CU hint | reason | next action |
|---|---|---|---|---|
| A9 / CU-09 | クラウディア Craudia | `pack_ready` + `pending` | Handoff written. No live signup from this agent | CU: worker profile draft only. Stop at 本人確認. Do not apply. Do not スキル出品 |

Wave A context (not copied; pointers only): sibling snapshot [PR#49](https://github.com/rimone0511/autopilot-log/pull/49) last listed this desk `pending` after Contra. This pack does **not** start TimeTicket / Contra. It does not skip earlier `blocked_skip` desks.

---

## Pack files

| File | What CU does |
|---|---|
| [PLAYBOOK.md](PLAYBOOK.md) | Register/login (MAIN Google) → 基本情報 / プロフィール → save draft → stop |
| [FIELD-MAP.md](FIELD-MAP.md) | Paste-ready JA bios (URL-free 自己紹介 + URL-ok portfolio) + field table |
| [STOP-KYC.md](STOP-KYC.md) | マイページ設定 → 本人確認。書類 + 自撮り **上げない** |
| [STATUS.md](STATUS.md) | This box. Fill the success line after a live run |

---

## Public GET (this authoring session)

`thin_site_skip: false`.

| URL | HTTP | Note |
|---|---|---|
| https://www.craudia.com/app/auth/register-temp | 200 | 仮登録。Google `auth=3`。**POST していない** |
| https://www.craudia.com/app/faq/contents/92 | 200 | プロフィール編集 FAQ |
| https://www.craudia.com/app/faq/contents/93 | 200 | 本人確認。顔付き公的書類 + 自撮り必須 |
| https://www.craudia.com/app/faq/contents/103 | 200 | 登録 = PC メール。出金時に本人確認 |
| https://www.craudia.com/app/faq/contents/151 | 200 | Google / メール / SNS |
| https://www.craudia.com/app/faq/contents/78 | 200 | ポートフォリオ = 公開可能な実績 |
| https://www.craudia.com/app/faq/contents/175 | 200 | スキル出品導線。**入らない** |
| https://www.craudia.com/crarepo/archives/3678 | 200 | 自己紹介に URL 不可。職歴・資格・ポートフォリオは別欄 |

---

## After live CU (leave blank until a run)

Fill only the secret-free keys. Do not paste OTP, ID, or a phone.

```
desk: Craudia
pack: ops/earn/craudia-cu-handoff-20260916/
auth:
otp:
kyc:
draft_profile:
skill_listing: no
apply: no
publish: no
pro_upgrade: no
rate:
next: stop
saved_draft: yes/no/unknown
kyc_shown: yes/no
upload: none
```

Outcome so far: **not run**. Valid later values: `done-draft` | `already_member_draft` | `kyc_wait` | `sms_wait_user` | `no_draft_path` | `otp_missing` | `hold_failed` | `card_wall` | `oauth_overreach` | `rate_empty`.

---

## This PR / pack will not

- Copy sibling pack bodies into `earn-packs/craudia/`
- Create a marketplace account from the authoring agent
- Upload ID / selfie / bank / My Number
- 参加申請 / スキル出品 / Craudia PRO
- Invent fee % or yen rates
- Retry Wave A `blocked_skip` desks (Fiverr hold, Lancers captcha, CrowdWorks 403, Upwork Google SSO, LinkedIn reCAPTCHA)
- Change Python posting-gate tests

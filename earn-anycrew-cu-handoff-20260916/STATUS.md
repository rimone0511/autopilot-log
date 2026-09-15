# STATUS — Anycrew（B10）CU handoff desk

> ## REGISTER-CU-CUT
>
> **2026-09-16.** Anycrew is **not** next live CU.
> Prefer **JOBS phase** (`register-winddown` / jobs-first).
> **Do not** treat this pack as next live CU after Freelancer.com (A10 / CU-10).
> After Freelancer parks: stay on JOBS (do-not-send bids / listings / week plan). Do **not** open B10 Anycrew from here.
> This folder stays **DRAFT_ONLY**. Not a signup GO. `register_cu_cut` overrides play.

Snapshot: **2026-09-16**（JST folder stamp）  
Folder: `earn-anycrew-cu-handoff-20260916/`  
State: **DRAFT_ONLY** / **REGISTER-CU-CUT** (pack exists; **not** next CU)  
Authoring: 公開 GET / 利用規約 / ID バンドル文字列のみ。**アカウント作成なし。OAuth 未完走。POST なし。応募なし。公開なし。**

This file is a desk box for **B10 / QUEUE B5 / CU-15 Anycrew talent**. It does not claim an Anycrew account exists. It does not rewrite Wave B serial STATUS in sibling PRs. **Cut overrides play:** do not start this desk from a Freelancer `done-draft`.

Forbidden: secrets, live phones/passwords/OTP, KYC files, signup from this authoring agent, **apply**, **publish**, GraphQL POST, invented traffic/GMV/fee %.

---

## CU hint (this desk)

| Hint | Meaning here |
|---|---|
| `pack_ready` | Files exist. **Not** a play GO. Default `register_cu_cut` |
| `register_cu_cut` | Register cut. **Not** next live CU. Prefer JOBS phase |
| `pending` | Live CU has **not** marked a draft on this desk from **this** folder |
| `needs_check` | `/offers` SPA empty this GET. Do not promote to `pass` |
| `draft_saved` | Fill only after a real CU run **and** a human GO that lifts the cut |
| `blocked_skip` | Skip this pass. Do not retry the listed reason |
| `kyc_wait` | 本人確認画面。朝の本人。アップロードなし |
| `phone_wall` / `sms_wait_user` | 電話・SMS。番号を git に書かない |
| `apply_wall` | Save required apply — **do not apply** |

Current row (authoring time):

| # | desk | CU hint | reason | next action |
|---|---|---|---|---|
| B10 / B5 / CU-15 | Anycrew | `pack_ready` + `register_cu_cut` + `pending` + `needs_check` | Cut. `/offers` 429B shell. No live signup / apply / publish from this agent | **Do not play.** Prefer JOBS. Keep draft. Human GO required before any paste |

Do **not** chain: Freelancer.com → Anycrew. Prefer JOBS siblings, including [PR#68](https://github.com/rimone0511/autopilot-log/pull/68) (Freelancer bid DRAFTs, do-not-send) and [PR#76](https://github.com/rimone0511/autopilot-log/pull/76) (JOBS week on `draft_saved` desks). Wave B serial skip of this desk remains [PR#72](https://github.com/rimone0511/autopilot-log/pull/72). This STATUS is not a signup GO.

IDs: **B10 = Anycrew** in this folder and PR#61. QUEUE **B5** = Anycrew（PR#1）。CU-**15**。QUEUE の Malt **B10** ではない。Offers.jp（B19）ではない。

---

## Pack files

| File | What CU does |
|---|---|
| [PLAYBOOK.md](PLAYBOOK.md) | Signup URL + MAIN Google → talent プロフィール → save draft → stop |
| [FIELD-MAP.md](FIELD-MAP.md) | JA bio **safe paste**（n8n/AI。URL 無し 150/200/255/800 + URL あり 200/800）+ field table |
| [STOP.md](STOP.md) | **No apply. No publish.** KYC / phone / 法人も停止 |
| [STATUS.md](STATUS.md) | This box. Fill the success line after a live run |

---

## Public GET (this authoring session)

`thin_site_skip: false`. No login. No POST. Google OAuth **not** completed. GraphQL **not** called.

### Signup + Google SSO

| URL | HTTP | Note |
|---|---|---|
| https://app.any-crew.com/ | 200 59625B | Last-Modified **Tue, 15 Sep 2026 10:51:28 GMT**。「会員登録」href=`https://id.any-crew.com/signup?auth_entry_source=front`。流れ「FacebookかGoogleのアカウントで利用登録」。モーダル **Googleでログイン** POST `https://base.any-crew.com/auth/google_oauth2?state=auth_entry_source_front`。FAQ 人材「一切費用はかかりません」。検索表示「非公開／公開」 |
| https://id.any-crew.com/signup?auth_entry_source=front | 200 **481B** | React `<div id="root">` のみ。Last-Modified **Tue, 15 Sep 2026 10:50:44 GMT**。`noindex` |
| https://id.any-crew.com/ | 200 481B | 同じシェル |
| https://id.any-crew.com/login | 200 481B | 同じシェル |
| https://id.any-crew.com/assets/index-a4a9d4ef.js | 200 | 文字列のみ観測（鍵は git に書かない）: **Googleで登録する** / Facebookで登録する / メールアドレスで登録する / 個人向けログイン / 法人向けログイン / `https://base.any-crew.com/auth/google_oauth2?state=auth_entry_source_${t}` / 「確認用のメールを送りました」。**電話番号・SMS・本人確認の文字列なし** |
| https://base.any-crew.com/auth/google_oauth2?state=auth_entry_source_front | GET **404** | フォームは POST。この GET は開始確認のみ。**POST していない。Google 同意へ入っていない** |
| https://app.any-crew.com/signup | 200 429B | アプリ SPA 空。signup URL は ID を正とする |

### /offers SPA (activity evidence only)

| URL | HTTP | Note |
|---|---|---|
| https://app.any-crew.com/offers | 200 **429B** | `<title>Anycrew</title>` + `<div id="root"></div>` + `/assets/react-12a6720f.js`。案件タイトル・日付 **なし** |
| https://app.any-crew.com/offers/_software_engineer | **301** → `/offers/professions/software_engineer` | 続く GET **200 429B** 同じ空シェル |
| https://app.any-crew.com/offers/_remote | **301** → `/offers/workstyles/remote` | 続く GET **200 429B** 同じ空シェル |

**Job cards unread.** Alive シェル ≠ dated catalog. ニュース / ブログ日付を掲載鮮度に使わない。

### Activity-adjacent (not job cards)

| URL | HTTP | Note |
|---|---|---|
| https://www.any-crew.com/news | 200 | メディア掲載 **2026-08-31**。job-board ではない |
| https://blog.any-crew.com/ | 200 | 新着 **2026.08.26**。job-board ではない |
| https://www.any-crew.com/terms | 200 | 第3条 SNS 登録。第5条 基本無料。改定 **2024-11-14**。％なし |
| https://www.any-crew.com/privacy | 200 | 登録: 氏名・メール・職歴・生年月日等。**電話は応募・契約。** 利用目的に本人確認 |
| https://www.any-crew.com/faq | **404** | アプリ FAQ を正とする |
| https://biz.any-crew.com/ | 200 | 採用 LP。人材パスではない |
| https://biz.any-crew.com/login | 200 429B | 採用 SPA。使わない |

Gate context (not re-run as a new verdict): PR#12 / PR#61 `needs_check`. This GET still shows `/offers` empty. Do not promote to `pass`.

---

## After live CU (leave blank until a run)

Fill only the secret-free keys. Do not paste OTP, ID, or a phone.

```
desk: Anycrew
id: B10
queue: B5
cu: CU-15
pack: earn-anycrew-cu-handoff-20260916/
hint: register_cu_cut
auth:
otp:
kyc:
phone:
draft_profile:
search_visibility:
apply: no
scout_reply: no
publish: no
biz: no
offers_spa:
card_date_seen:
next: stop
saved_draft: yes/no/unknown
kyc_shown: yes/no
upload: none
apply_clicked: no
publish_clicked: no
phone_entered: no
```

Outcome so far: **not_run** / **register_cu_cut**. Valid later values: `done-draft` | `already_member_draft` | `kyc_wait` | `sms_wait_user` | `phone_wall` | `no_draft_path` | `otp_missing` | `hold_failed` | `oauth_overreach` | `apply_wall` | `needs_check_offers`.

---

## Next (human)

1. **REGISTER-CU-CUT.** Do not CU-play Anycrew as the step after Freelancer. Prefer JOBS phase.
2. JOBS: do-not-send pastes / week plan on desks that already have `draft_saved`. Do not start Wave B register from this folder.
3. Keep this PR **draft**. Do not merge until Yuta reviews.
4. If register CU is ever re-opened by a human GO, then and only then follow [PLAYBOOK.md](PLAYBOOK.md) + [STOP.md](STOP.md). Default is **cut**. Still no apply / no publish / no secrets.

---

## This PR / pack will not

- Create an Anycrew account from the authoring agent
- POST Google / Facebook OAuth or GraphQL
- Click 応募 or 公開 or send a scout reply
- Type a live phone or upload ID / selfie / bank / My Number
- Invent talent fee %
- Open `biz.any-crew.com` as the talent path
- Treat news/blog dates as `/offers` freshness
- Copy sibling pack bodies into this folder
- Play Workship → SOKUDAN serial as live CU
- Start Anycrew register CU after Freelancer (cut; prefer JOBS)
- Change Python posting-gate tests

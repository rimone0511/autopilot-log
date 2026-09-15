# STATUS — Anycrew（B10）CU handoff desk

Snapshot: **2026-09-16**（JST folder stamp）  
Folder: `earn-anycrew-cu-handoff-20260916/`  
State: **DRAFT_ONLY**  
Authoring: 公開 GET / 利用規約 / ID バンドル文字列のみ。**アカウント作成なし。OAuth 未完走。POST なし。応募なし。公開なし。**

This file is a desk box for **B10 / QUEUE B5 / CU-15 Anycrew talent**. It does not claim an Anycrew account exists. It does not rewrite Wave B serial STATUS in sibling PRs.

Forbidden: secrets, live phones/passwords/OTP, KYC files, signup from this authoring agent, **apply**, **publish**, GraphQL POST, invented traffic/GMV/fee %.

---

## CU hint (this desk)

| Hint | Meaning here |
|---|---|
| `pack_ready` | This 4-file handoff is paste-ready. CU may type under PLAYBOOK rules **after a human GO** |
| `pending` | Live CU has **not** marked a draft on this desk from **this** folder |
| `needs_check` | `/offers` SPA empty this GET. Do not promote to `pass` |
| `draft_saved` | Talent profile parked unpublished (fill after a real CU run) |
| `blocked_skip` | Skip this pass. Do not retry the listed reason |
| `kyc_wait` | 本人確認画面。朝の本人。アップロードなし |
| `phone_wall` / `sms_wait_user` | 電話・SMS。番号を git に書かない |
| `apply_wall` | Save required apply — **do not apply** |

Current row (authoring time):

| # | desk | CU hint | reason | next action |
|---|---|---|---|---|
| B10 / B5 / CU-15 | Anycrew | `pack_ready` + `pending` + `needs_check` | Handoff written. `/offers` 429B shell. No live signup / apply / publish from this agent | Human GO → talent profile draft only. **No apply. No publish.** Stop at KYC / phone / biz. One dated card before treating gate as pass |

**REGISTER-CU-CUT（PR#72）:** Wave B 登録直列は jobs-first に譲る。このパックを Freelancer.com（A10）の次の自動 CU にしない。人が GO するまで `pending`。PR#72 はこの机を skip する。GO しても応募しない。

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

Outcome so far: **not_run**. Valid later values: `done-draft` | `already_member_draft` | `kyc_wait` | `sms_wait_user` | `phone_wall` | `no_draft_path` | `otp_missing` | `hold_failed` | `oauth_overreach` | `apply_wall` | `needs_check_offers`.

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
- Change Python posting-gate tests

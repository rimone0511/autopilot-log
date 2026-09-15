# STATUS — 複業クラウド (B03) CU handoff

> ## REGISTER-CU-CUT
>
> **2026-09-16.** Wave B **register** CU is **superseded** by register-winddown / **jobs-first** ([#72](https://github.com/rimone0511/autopilot-log/pull/72)).
> **Do not** open 複業クラウド (B03 / CU-12) as **next live CU** after Freelancer.com (A10 / CU-10) or from Wave B serial autoplay.
> After Freelancer parks: stay on **JOBS phase** (do-not-send). Do **not** start this folder.
> Hint: `register_cu_cut`. This folder stays **DRAFT_ONLY**. Not a signup GO. No secrets.

Snapshot: **2026-09-16** (folder stamp)  
Folder: `earn-fukugyo-cloud-cu-handoff-20260916/`  
State: **DRAFT_ONLY** / **REGISTER-CU-CUT** (pack exists; **not** next CU)  
Authoring session: public talent HTML/JS + TOS + company privacy only. **No login. No POST. No OAuth follow. No credentials invented or stored.**

This file is the desk box for **B03 / CU-12 複業クラウド（fukugyo cloud / 旧 Another Works）**. It is not a signup log and **does not claim an account exists**. **Cut overrides play:** do not treat `pack_ready` as a live GO.

---

## Desk hint

| Field | Value |
|---|---|
| Desk | 複業クラウド talent worker（旧 Another Works） |
| IDs | **B03** · Wave B · **CU-12** |
| Not | Company console / 採用担当. Not Workship. Not CrowdWorks |
| CU hint | `pack_ready` + **`register_cu_cut`** — files exist; **do not play** as next live CU |
| Activity gate | **`needs_check`** (this GET + [#12](https://github.com/rimone0511/autopilot-log/pull/12) / [#62](https://github.com/rimone0511/autopilot-log/pull/62)). Not `alive`. Not `thin` |
| Google | **MAIN SSO likely** (`PREFER_GOOGLE`). Public JS **「Googleでサインイン」**. Click-time |
| Plan | Talent **cited free** (TOS 第2.1条1). Worker ％ **unstated** — do not invent |
| Stop | **エントリー / キニナル** + KYC/phone/SMS-as-ID — [STOP.md](STOP.md) |
| Skip | Captcha / press-hold fail → **`blocked_skip`** — [PLAYBOOK.md](PLAYBOOK.md) |
| Runner | [PLAYBOOK.md](PLAYBOOK.md) · [FIELD-MAP.md](FIELD-MAP.md) |

| Hint | Meaning here |
|---|---|
| `pack_ready` | Files exist. **Not** a play GO while `register_cu_cut` is set |
| `register_cu_cut` | Register serial cut. **Not** next live CU. Prefer JOBS phase |
| `pending` | Live CU has **not** marked a draft on this desk from **this** folder |
| `draft_saved` | Talent profile parked unpublished (fill after a real CU run) |
| `blocked_skip` | Skip this pass. Do not retry the listed reason (captcha / hold / image puzzle / waf) |
| `kyc_wait` | 本人確認画面。朝の本人。アップロードなし |
| `sms_wait_user` | Phone/SMS required for draft save. User chat. Do not guess |
| `apply_stop` | エントリー or キニナル pressed by mistake — stop |

Current row (authoring time):

| # | desk | CU hint | reason | next action |
|---|---|---|---|---|
| B03 / CU-12 | 複業クラウド | `pack_ready` + **`register_cu_cut`** | Handoff written. REGISTER-CU-CUT / jobs-first | **Do not open** as next live CU. Stay on JOBS. Human GO later still = profile draft only; no エントリー |

Do **not** chain: Freelancer.com → this desk. Prefer JOBS siblings ([#68](https://github.com/rimone0511/autopilot-log/pull/68) Freelancer bid DRAFTs do-not-send; [#76](https://github.com/rimone0511/autopilot-log/pull/76) JOBS week). Wave B serial cut: [#72](https://github.com/rimone0511/autopilot-log/pull/72). This STATUS is not a signup GO.

Sibling paste (bodies not merged here except 自己紹介 fences already in FIELD-MAP):

| Pack | PR |
|---|---|
| Thick CU-12 sample | [#21](https://github.com/rimone0511/autopilot-log/pull/21) |
| Gate record | [#12](https://github.com/rimone0511/autopilot-log/pull/12) |
| Gate re-GET | [#62](https://github.com/rimone0511/autopilot-log/pull/62) |
| REGISTER-CU-CUT serial | [#72](https://github.com/rimone0511/autopilot-log/pull/72) |

---

## Activity gate (observed evidence only)

**Verdict: `needs_check`.** Do not promote to `alive`. Do not mark `thin` / `dead`. `thin_site_skip: false`.

What this GET **did** see (logged out, no POST):

| Evidence | Observation |
|---|---|
| Talent origin | https://talent.aw-anotherworks.com/ HTTP **200**. Title「複業クラウド \| 複業・業務委託特化型マッチングプラットフォーム」. Next.js SPA, `buildId` `8xWpf_UM-Ow_9wUJEAg3E`. Home `__NEXT_DATA__` `pageProps` empty. No job cards and **no listing dates** on `/` |
| `/projects/` and `/projects` | **404** (sitemap loc). Body「404: This page could not be found」 |
| Sitemap | `/` and `/projects/` only. **No `<lastmod>`** |
| Individual jobs | Public `<title>` **without login**. `__NEXT_DATA__` keys: `title`, `imageUrl`, `description`, `isSuspended`. **No** `created_at` / `updated_at` / 掲載日 |
| `/projects/91374` | Title「【面白いこと、BUZZで。】法人SNS運用ディレクター募集♪」. `isSuspended:false`. CDN folder `2025-12-18` (**not** a posting date). OG text includes「2024年11月には上場企業グループに参画」— company history, not a card date |
| `/projects/91375` | Title「【週5日/月80〜100万円】社内チャット内製化テックリード」. Resource upload path (no `YYYY-MM-DD` folder). Headline 円 is **not** GMV and **not** a profile rate |
| `/projects/94000` | Title「【フルリモート】ディレクター…」. CDN `2025-11-22` |
| `/projects/98000` | Title「ＤＸスクール事業における行政・教育機関との橋渡しをお願いします」. CDN `2026-04-07` |
| `/projects/101000` | Title「【稼働自由・紹介するだけ】…」. CDN `2026-05-15` (latest image-folder date this GET; **still not a 新着 stamp**) |
| `/projects/79324` `/79325` | Generic talent OG title this GET (no job-specific `<title>`) — do not treat as a live card |

So: public job **titles** (including フルリモート) exist. **Recent listing dates on rendered cards were not seen.** Image-folder dates are CDN paths. Unread SPA is **not** thin.

**Do not invent** 登録者数 / 流入 / GMV. This GET did not see a public count to cite.

A human should glance at one **rendered listing date** before treating this desk as `alive`.

---

## Public livecheck (authoring, 2026-09-16, no login, no POST)

| URL | HTTP | Result used |
|---|---|---|
| https://talent.aw-anotherworks.com/ | 200 | Talent host. SPA loader. JS `SIGN_UP:"/sign_up"`. **無料ではじめる** |
| https://talent.aw-anotherworks.com/sign_up | 200 | Title **新規登録**. Chunk: **Googleでサインイン** / Facebook / Apple / メール / パスワードの確認 / 利用規約 |
| https://talent.aw-anotherworks.com/login | 200 | Title **サインイン**. **新規登録はこちら** |
| https://talent.aw-anotherworks.com/signup | **404** | Do not use |
| https://talent.aw-anotherworks.com/sign-up | **404** | Do not use |
| https://talent.aw-anotherworks.com/register | **404** | Do not use |
| https://talent.aw-anotherworks.com/projects/ | **404** | Sitemap loc |
| https://talent.aw-anotherworks.com/sitemap.xml | 200 | `/` + `/projects/` . No lastmod |
| https://cl.aw-anotherworks.com/user_tos | 200 | 第2.1条1 タレント無料. 第2.1条2 プロフィール. 第2.1条3 応募. 本人確認/SMS/口座 **0 hits** |
| https://cl.aw-anotherworks.com/ | 200 | Company. **Close** as entry |
| https://cl.aw-anotherworks.com/user_privacy | **404** | Do not cite as live |
| https://anotherworks.co.jp/user_privacy | 200 | TOS footer. 本人確認/SMS/口座 **0 hits** |
| https://anotherworks.co.jp/ | 200 | Company site, not the job board |
| https://talent.aw-anotherworks.com/_next/static/chunks/2ft1bogak3uo6.js | 200 | Signup labels |

CSRF tokens, reCAPTCHA site keys, and Firebase API keys are **not** recorded here.

Google OAuth was **not** started (no 302 follow).

---

## Live CU outcome (empty — do not run while `register_cu_cut`)

Do not pre-fill success. Default this folder: **`register_cu_cut` / `not_run`**. Valid later values match PLAYBOOK **only after an explicit human GO** (still not next auto CU):

```
desk: 複業クラウド
pack: earn-fukugyo-cloud-cu-handoff-20260916/
ids: B03 / CU-12
auth:
otp:
kyc:
draft_profile:
entry: no
kininaru: no
scout_reply: no
solution_post: no
publish: no
plan: talent-free-cited
bank: no
rate:
skip:
register_cu_cut: yes
next: stop | jobs-first
```

Current: **`register_cu_cut` / `not_run`**. Do not open as next live CU.

---

## This PR does not

- Create or log into a 複業クラウド account
- Invent or commit Google / email / password / OTP / phone / bank / My Number
- Press **エントリー** or **キニナル**
- Reply to スカウト or post ソリューション
- Open 本人確認 / 口座
- Buy a company plan or invent worker 手数料％ / traffic / GMV
- Promote the activity gate from `needs_check` to `alive` without a rendered listing date
- Copy sibling pack folders
- Change Python posting-gate tests
- Open 複業クラウド as **next live CU** (REGISTER-CU-CUT / jobs-first)

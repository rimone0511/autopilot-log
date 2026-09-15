# B03 — 複業クラウド（旧 Another Works）

**DRAFT_ONLY.** Logged out. Did not register. Did not apply. No secrets.

```
date (JST): 2026-09-16
desk: 複業クラウド（旧 Another Works）
official_url: https://talent.aw-anotherworks.com/
public_pages_opened: yes
logged_in: no
signup_path: Google / Apple / Facebook labels in public JS; email field also in same chunk. Buttons not painted in static HTML.
fee_notes: TOS 第2.1条1 — registered talent uses the service for free. Worker success-fee % not on that TOS.
cu_tip: Stay on talent domain. Confirm Google on /sign_up. Draft profile only. Do not apply. Stop at KYC.
gate: needs_check
published: no
```

## Official URL

- Talent (worker): https://talent.aw-anotherworks.com/ — HTTP 200. Title「複業クラウド \| 複業・業務委託特化型マッチングプラットフォーム」
- Sign up: https://talent.aw-anotherworks.com/sign_up — 200, title「新規登録」
- Sign in: https://talent.aw-anotherworks.com/login — 200, title「サインイン」
- TOS: https://cl.aw-anotherworks.com/user_tos — 200
- Company site: https://anotherworks.co.jp/ — 200 (company page, not the job board)
- Do **not** use the company console https://cl.aw-anotherworks.com/ as the seller entry

OG on the talent origin:「完全無料の複業マッチングプラットフォーム」「中間マージンなどは一切発生しません」. Treat that as marketing copy on the official talent page. The **cite** for talent-side price is TOS 第2.1条1 below.

## Public jobs / dates — what this GET actually saw

Logged-out HTML is a Next.js SPA (`buildId` `8xWpf_UM-Ow_9wUJEAg3E`). Home `__NEXT_DATA__` has empty `pageProps`. No job cards and **no listing dates** on `/`.

`https://talent.aw-anotherworks.com/projects/` (sitemap loc) returned **404**.

Individual job URLs **do** return titles without login. Examples this GET opened:

| id | Public `<title>` (trimmed) | Public `imageUrl` folder (CDN path, **not** a posting date) |
|---|---|---|
| 91374 | 【面白いこと、BUZZで。】法人SNS運用ディレクター募集♪ | `.../public/images/2025-12-18/...` |
| 91375 | 【週5日/月80〜100万円】社内チャット内製化テックリード | resource upload path (no `YYYY-MM-DD` folder) |
| 94000 | 【フルリモート】ディレクター｜\| 大手案件も！提案力と実績作り | `2025-11-22` |
| 98000 | ＤＸスクール事業における行政・教育機関との橋渡しをお願いします | `2026-04-07` |
| 101000 | 【稼働自由・紹介するだけ】採用コストを抑えたい企業をご紹介ください！ | `2026-05-15` |

Public Next data for `/projects/91374.json` fields seen: `title`, `imageUrl`, `description`, `isSuspended:false`. **No** `created_at` / `updated_at` / 掲載日.

OG description on 91374 includes「2024年11月には上場企業グループに参画」— company history in the blurbs, **not** a job card date.

Sitemap has only `/` and `/projects/` and **no `<lastmod>`**.

So: public job **titles** (including フルリモート) exist. **Recent listing dates on cards were not seen.** Image-folder dates go as late as `2026-05-15`; that is a CDN path, not a「新着」stamp. Gate stays `needs_check` (not `alive`, not `dead`, not `thin`).

## Signup path

Static `/sign_up` HTML does not paint buttons (SPA). Public chunk `2ft1bogak3uo6.js` (HTTP 200) contains:

- `handleClickGoogle` / `signInGoogle`
- button label **「Googleでサインイン」**
- also **「Facebookでサインイン」** / **「Appleでサインイン」**
- a **メールアドレス** field (validation / already-registered toasts)

This GET did **not** click OAuth and did **not** submit email. CU should prefer Google **if the live button is visible**, same MAIN Google mailbox as the rest of the queue. Do not create a new SNS account. If Google is missing at paste time, park rather than inventing a path.

## Fee notes (official pages only)

Cited from https://cl.aw-anotherworks.com/user_tos 第2.1条1:

> 登録タレントは、タレント利用契約の有効期間中、本規約に従って、当社の定めるところ(当社が別途定めるガイドラインを含みますが、これに限られません。)に従い、本サービスを無料で利用することができます。

TOS also describes 成功報酬無料 **for registered companies hiring from the DB** (definition text). That is **not** a worker % and is not copied into a talent fee cell.

Worker success-fee %: **not on the TOS this GET opened** → leave unstated (`needs_check`). Do not invent.

Do not open a paid company plan from this desk.

## CU tip

1. Talent host only. Close company demo / `cl.aw-anotherworks.com` except TOS.
2. If「Googleでサインイン」is on screen, use MAIN Google. First SNS wins.
3. Draft profile. TOS 第2.1条2: some profile items are shown to **all registered companies**. Extra public toggles stay off.
4. Do not 応募 / オファー返信.
5. Stop if ID / bank / My Number / 顔写真 verification is requested.
6. Do not promote this desk to `alive` until a human sees a **listing date** on a rendered board.

## Gate

**needs_check**

# STATUS — Wave B alive CU serial (prep)

> ## REGISTER-CU-CUT
>
> **2026-09-16.** Wave B **register** CU serial in this folder is **superseded**.
> Prefer **JOBS phase** (`register-winddown` / jobs-first).
> **Do not** treat this pack as next live CU after Freelancer.com (A10 / CU-10).
> After Freelancer parks: stay on JOBS (do-not-send bids / listings / week plan). Do **not** open B02 Workship from here.
> This folder stays **DRAFT_ONLY** archive + URL pointers. Not a signup GO.

Snapshot: **2026-09-16 JST**  
Folder: `ops/earn/waveb-alive-cu-serial-20260916/`  
State: **DRAFT_ONLY** / **REGISTER-CU-CUT** (prep, not next CU)  
Authoring: logged-out public GET only. **No signup. No OAuth. No POST. No cookies saved.**

This is a serial **prep box**, not a live CU log and not an activity-gate re-judge. Sibling gates already marked these desks `pass` (PR#12 JP Wave B except Workshift; PR#13 for Workshift). This GET only re-cites public URLs. **Cut overrides play:** do not start this serial from a Freelancer `done-draft`.

Forbidden: secrets, live phones/passwords/OTP/CSRF, KYC files, signup from this authoring agent, publish, paid plans, invented traffic/GMV/fee %.

Python posting-gate tests were **not** edited.

---

## CU hint (this folder)

| Hint | Meaning here |
|---|---|
| `pack_ready` | Files exist. **Not** a play GO. Default `register_cu_cut` |
| `pending` | Live CU has **not** marked a draft on these desks from **this** folder |
| `draft_saved` | Fill only after a real CU run |
| `blocked_skip` | Skip this pass for the listed reason |
| `kyc_wait` | Identity screen. Morning user. No upload |
| `register_cu_cut` | Register serial cut. **Not** next live CU. Prefer JOBS phase |

Current rows (authoring time): **all six** `pack_ready` + `register_cu_cut` (files exist; **do not play**).

Do **not** chain: Freelancer.com → this Wave B serial. Prefer JOBS siblings, including [PR#68](https://github.com/rimone0511/autopilot-log/pull/68) (Freelancer bid DRAFTs, do-not-send) and [PR#76](https://github.com/rimone0511/autopilot-log/pull/76) (JOBS week on `draft_saved` desks). Wave A live box remains [PR#54](https://github.com/rimone0511/autopilot-log/pull/54) / Freelancer handoff [PR#66](https://github.com/rimone0511/autopilot-log/pull/66). This STATUS is not a signup GO.

---

## Rollup

| Gate (sibling, not re-scored) | Count | Desks |
|---|---|---|
| `pass` / alive for this serial | **6** | B01 SOKUDAN, B02 Workship, B06 Skill Shift, B07 ITプロパートナーズ, B09 Workshift, B19 Offers |
| `needs_check` in this folder | **0** | — |
| Live CU `draft_saved` | **0** | not run |

Marketing totals and pagination counts are **not** activity proof and are not written here.

---

## One-line each

| Play | ID | Official | This GET (logged out) | Signup path | Fees | CU tip | CU hint |
|---|---|---|---|---|---|---|---|
| 1 | B02 | https://goworkship.com/ | `/portal/search` 200. Headings include リモ可 / LLM 業務効率化カード. **No card `2026-09-*` date in this HTML** (PR#12 used this listing as `pass`; this GET does not add a date) | `/signup` 200「フリーランス登録をする」「SNSで登録」+ FirebaseUI. Page JS includes `GoogleAuthProvider.PROVIDER_ID` | 前払いヘルプに％なし → 作らない | Not enterprise. Confirm Google **icon label** before click | `register_cu_cut` |
| 2 | B01 | https://sokudan.work/ | Home 200. Embedded `contractType: outsourcing` + `createdAt` **2026-09-15**. Titles include 基本リモ FDE | `/signup/pro` 200「無料新規登録」`alt="Google で登録"` → `/users/auth/google?category=signup` | 規約に「手数料」語のみ、％なし → 作らない | Not 企業. Facebook「推奨」無視 | `register_cu_cut` |
| 3 | B19 | https://offers.jp/ | `/jobs/engineer/side-job` 200. 業務委託カード「【フルリモート】AI×FDE…」更新日文字列 **2026-09-10** (also 09-08 / 09-07). `/signup` **404** | `/worker/signup` 200. `data-testid="auth-google"` → `/oauth/worker_signup/google`. Heading「メールアドレスで登録する」 | 規約: マッチング成功報酬はクライアント側の語. ユーザー％ **unstated** → 作らない | Not `/client/`. Do not 応募 | `register_cu_cut` |
| 4 | B06 | https://www.skill-shift.com/ | `GET /api/jobs` 200. Leading `created_at` **2026-09-14 / 13 / 12 / 11**, `is_recruiting: true`. Example position「AI活用で業務効率化！業務棚卸しから始めるAIアドバイザー」（オンライン想定）. `skillshift.jp` **DNS fail** | `/sign-up` 200 SPA shell (meta「個人登録ページ」). Google OAuth **not** in this HTML | ％ **unstated** this GET → 作らない | Email = MAIN mailbox. Facebook 新規禁止. 現場のみ行は応募しない | `register_cu_cut` |
| 5 | B07 | https://itpropartners.com/ | `/job/sale-4` 200. 最終更新日 **2026/09/08**「コーポレートIT／社内情報システム」、**2026/09/05**「M&A事業部…アポ獲得」 | `/register` 200「あなたの職種を教えてください」（エンジニア / マーケター / デザイナー）. Register HTML has **no** Google signup control (GTM only) | 公式フロー「登録・利用は無料」（sibling). 仲介％ **needs_check** | Agent desk. CU does not attend 面談. Do not apply | `register_cu_cut` |
| 6 | B09 | https://workshift-sol.com/ | Home 200. Cards link `/jobs/view/13758` etc. That view 200: title SIAL Paris 現地通訳, date string **2026-09-11**,「本人確認: 無し」. **Do not apply that row.** `/jobs/search` 200 + CAPTCHA (listing dates unread there) | `/registration/mail_start` 200. Links: mail_start / `facebook/login` / `linkedin/login` / `github/login`. **No** `/google/login` | ％ **unstated** this GET → 作らない | ≠ Workship. Email = MAIN mailbox. 現地カード回避 | `register_cu_cut` |

Card yen / monthly bands on ITプロ are **that job’s listed pay**, not a profile rate and not GMV. Do not copy into the bio.

---

## HTTP log (public GET only)

UA: ordinary desktop Chrome string. No login cookie. CSRF / `_token` / `x-app-token` values were **not** stored.

| URL | HTTP | Note |
|---|---|---|
| https://goworkship.com/signup | 200 | Title フリーランス登録をする. SNSで登録. `#firebaseui` / GoogleAuthProvider in JS |
| https://goworkship.com/portal/search | 200 | 業務委託案件. Headings with リモ / LLM |
| https://goworkship.com/help/agreement/95 | 200 | 「前払いオプションを利用するには、本人確認が必要です」 |
| https://sokudan.work/ | 200 | Title SOKUDAN. outsourcing `createdAt` 2026-09-15 |
| https://sokudan.work/signup/pro | 200 | 無料新規登録. Google で登録 |
| https://sokudan.work/pages/terms | 200 | 審査書類 / 代理人登録不可. 手数料％なし |
| https://offers.jp/worker/signup | 200 | Title 新規登録. auth-google + メールアドレスで登録する |
| https://offers.jp/jobs/engineer/side-job | 200 | 副業・業務委託カード. 更新日 2026-09-10 |
| https://offers.jp/terms | 200 | 成功報酬はクライアント側の語 |
| https://offers.jp/signup | **404** | Do not use |
| https://www.skill-shift.com/ | 200 | SPA shell. Title Skill Shift |
| https://www.skill-shift.com/sign-up | 200 | SPA. description 個人登録ページ |
| https://www.skill-shift.com/terms-of-service | 200 | SPA shell (body in JS) |
| https://www.skill-shift.com/api/jobs | 200 | JSON. Dates cited above. **pagination.total not written** |
| https://skillshift.jp/ | **fail** | Could not resolve host |
| https://itpropartners.com/ | 200 | フリーランス専門エージェント |
| https://itpropartners.com/register | 200 | 職種選択. POST action exists — **not submitted** |
| https://itpropartners.com/job/sale-4 | 200 | 最終更新日 2026/09/08 など |
| https://itpropartners.com/blog/flow-itpropartners/ | 200 | 利用の流れ（面談・契約は本人） |
| https://workshift-sol.com/ | 200 | Title ワークシフト Workshift |
| https://workshift-sol.com/registration/mail_start | 200 | Mail / Facebook / LinkedIn / GitHub |
| https://workshift-sol.com/jobs/search | 200 | CAPTCHA. Dates unread on this HTML |
| https://workshift-sol.com/jobs/view/13758 | 200 | 現地カード. 2026-09-11. 本人確認 無し |
| https://workshift-sol.com/pages/term | 200 | 2026年4月11日改定 |

---

## After live CU (leave blank until a run)

Fill only secret-free keys. Do not paste OTP, ID, or a phone.

```
desk:
pack: ops/earn/waveb-alive-cu-serial-20260916/
auth:
otp:
kyc:
draft_profile:
publish: no
apply: no
next:
```

Outcome so far: **not_run**.

---

## Next (human)

1. **REGISTER-CU-CUT.** Do not CU-play this serial as the step after Freelancer. Prefer JOBS phase.
2. JOBS: do-not-send pastes / week plan on desks that already have `draft_saved`. Do not start Wave B register from this folder.
3. Keep this PR **draft**. Do not merge until Yuta reviews.
4. If register CU is ever re-opened by a human GO, then and only then follow [ORDER.md](ORDER.md) + [STOP-KYC.md](STOP-KYC.md). Default is **cut**.

## This PR / pack will not

- Copy sibling paste bios or field maps
- Create marketplace accounts
- Upload ID / selfie / bank / My Number
- Apply / publish / buy paid plans
- Invent fee % or traffic
- Rewrite QUEUE letters or invent CU-29 for Workshift
- Change Python posting-gate tests
- Start Wave B register CU after Freelancer (cut; prefer JOBS)

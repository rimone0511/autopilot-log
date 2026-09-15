# ACTIVITY-GATE — B14 PeoplePerHour / B16 Workana / B18 YOUTRUST

Observed: **2026-09-16 JST**  
Method: public URL GET. No login. No signup. No paid checkout.  
Folder: `ops/earn/waveb-global-gate-20260916/`

IDs in the first column are **this-folder labels**. QUEUE letters: B9 / B11 / B13. See [INDEX.md](INDEX.md).

---

## Summary

| This folder | Desk | Official | Activity this GET | Google | Free seller path | Gate |
|---|---|---|---|---|---|---|
| B14 | PeoplePerHour | https://www.peopleperhour.com/ | Jobs page title **Freelance Jobs, Work & Projects in Sep 2026**. HTML `posted_dt` on **2026-09-15** (examples `11:26:06` … `20:00:02`). Sample Hourlie URL still 200 | Register HTML: **Continue with GOOGLE**, Sign up with Facebook, Sign up with email. Role: I want to (buyer vs freelancer) | Register page has no checkout in this HTML. Public Terms: freelancer access under **PPH Basic** (paid annual). Checkout amount **not read** | marketplace **pass** · seller **`blocked_paid_plan`** (do not subscribe) |
| B16 | Workana | https://www.workana.com/ | HTML `/`, `/en/`, `/en/jobs`, `/en/signup`, `/en/login`, help.workana.com **403** CF. `robots.txt` **200** | Unread this GET (403). Sibling PR#2 recorded Google on `/en/login` HTML — **not re-read** | Unread this GET. Do not invent “free to bid” | **needs_check** |
| B18 | YOUTRUST | https://youtrust.jp/ | `/` → `/lp` 200 title 仕事専用SNS. Jobs list URL 200, cards not in HTML. API 401 | Official help: **Googleアカウント連携**. `/sign_in` is SPA (button not in static HTML) | Help: ジョブは **1投稿まで無料** (poster side; CU does not post). Applicant % **unread** | **needs_check** |

`fail` (closed): **0**  
`SKIP thin`: **0**  
`blocked_paid_plan`: **PeoplePerHour seller path only**

---

## Per-desk evidence (this GET)

Marketing “1 million…” copy is not used as activity proof. Headings and dates below are from HTML/help that actually arrived.

### B14 PeoplePerHour — marketplace pass, paid-plan block

- Home https://www.peopleperhour.com/ HTTP 200. Register link present. Hourlie product URLs still in the homepage HTML.
- Register https://www.peopleperhour.com/site/register HTTP 200 title “Register with PeoplePerHour.com”. Controls in HTML: **Continue with GOOGLE**, Sign up with Facebook, Sign up with email.
- Jobs https://www.peopleperhour.com/freelance-jobs HTTP 200 title includes **Sep 2026**. `posted_dt` strings on **2026-09-15**. Example card titles in the same payload (not a count): “I need a 2 minute professional voice over for a video”, “Meeting Notes & Action Tracking Assistant”. `expiry_dt` values such as 2026-10-15 are **deadlines**, not post dates.
- Sample Offer/Hourlie https://www.peopleperhour.com/hourlie/be-your-wordpress-ninja-for-30-minutes/304215 HTTP 200. Bare `/hourlie/` is 404 — use a real Hourlie URL, not the directory slash.
- Terms https://www.peopleperhour.com/static/terms HTTP 200, **last modified: September 11, 2026**. Quote (public page):

  > Freelancer access to the PPH Services is available under a subscription plan (“PPH Basic”). PPH Basic is a non-refundable annual subscription fee in the amount indicated on the subscription sign up (or communicated to you thereafter), which can be paid in full or in monthly payments for the twelve (12) month period (the “Annual Term”).

  > By subscribing to PPH Basic, you will receive fifteen (15) project proposals credits per month

  TopAccess is a second **non-refundable annual** subscription in the same document. Extra proposal credits are described as purchasable after the allotment. **Price figures on the sign-up screen were not opened.** Do not invent GBP/EUR/USD. **Do not subscribe** to find out.

- Support articles on `support.peopleperhour.com` were Cloudflare 403 this GET. Application-process details stay `needs_check` at click-time.
- `/pricing` is 404. Do not treat a missing marketing page as “free”.

**Action:** park. Fill application text locally if a later CU happens. Stop at choose-your-subscription. If submit requires a plan → keep `blocked_paid_plan` and close.

### B16 Workana — needs_check

- https://www.workana.com/ and `/en/jobs`, `/en/signup`, `/en/login`, `/how-it-works/freelancer`, `help.workana.com` (home + three help articles) all **HTTP 403** Cloudflare challenge HTML (“Just a moment…”).
- https://www.workana.com/robots.txt **HTTP 200** text. Disallows `/api/`, some login/signup query URLs. Declares `Sitemap: https://www.workana.com/sitemap_index.xml`. The sitemap URL itself was **403** this GET.
- That is enough to say the **hostname is not a parked blank**. It is **not** enough to score job recency, Google button, or fees.
- Sibling [#2](https://github.com/rimone0511/autopilot-log/pull/2) / [#29](https://github.com/rimone0511/autopilot-log/pull/29): living marketing site; `/en/login` Google/Facebook/Apple in HTML on an earlier GET; jobs unread (Cloudflare). **This run does not reconfirm those HTML strings.**
- Worker fee % / Priority Moderation price: **not on any page that returned 200 here**. Not invented. If a later human sees Priority Moderation, do not buy it.

**Action:** do not signup from this PR. Human `/en/jobs` after Cloudflare. Unreadable ≠ `fail-thin`.

### B18 YOUTRUST — needs_check

- https://youtrust.jp/ **302** → https://youtrust.jp/lp **200** title `YOUTRUST｜仕事専用SNS`.
- https://youtrust.jp/sign_in **200** title `ログイン｜YOUTRUST`. Static HTML is a SPA shell. Google **button not rendered** in this GET. GTM strings are not a signup control.
- https://youtrust.jp/signup **404**.
- https://youtrust.jp/recruitment_posts **200** title `副業・転職のジョブ（募集）一覧`. Card dates **not in HTML**.
- https://youtrust.jp/api/recruitment_posts **401** JSON `{"error":"You need to sign in or sign up before continuing."}` — not used as a listing.
- Help https://help.youtrust.jp/user/message/search-jobs/ **200**: 「ジョブは全てのユーザーに公開され、アプリとWebの両方から確認できます。」
- Help https://help.youtrust.jp/user/account/create/ **200**: four create paths, including **Googleアカウント連携**. Note on the same page: Google **mail** register ≠ Google **account** linking. Facebook / LINE exist; this ops line prefers MAIN Google and does not create extra SNS accounts.
- Help https://help.youtrust.jp/user/post/how-to-post/ **200**: 「ジョブは1投稿まで無料で公開可能です。」 Help https://help.youtrust.jp/user/post/manage-applicants/ **200**: 「1アカウント、1件まで無料でジョブを公開できます。無料掲載期間は公開日から30日です。」 That is **poster** policy. This gate does **not** post jobs. Applicant / 「話を聞きたい」 fee % is **not on these pages** → not invented.
- Official recruiter unlimited jobs = paid path in the same help. **Do not buy.**

**Action:** activity stays `needs_check` until a human sees a card date. Not marked thin. SNS 実名連携 if demanded → record. KYC → stop.

---

## Auth / stop (all three)

1. MAIN Google only. Do not mint extra accounts.
2. Passport / license / My Number / face / bank → do not upload.
3. Paid membership, featured listing, review skip, extra credits → do not buy.
4. No profile publish, no proposals, no 「話を聞きたい」, no job posts.
5. Missing listing dates stay `needs_check`. Do not fill with a guessed number.

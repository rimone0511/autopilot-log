# SKIP-LOG — Wave A `blocked_skip` (morning loop)

Snapshot: **2026-09-16 morning loop**  
Folder: `ops/earn/register-wave-a-status-20260916/`  
State: **DRAFT-ONLY**  
Live box: [STATUS.md](STATUS.md) · next CU: [NEXT-CU.md](NEXT-CU.md)

Six Wave A desks parked `blocked_skip`. Desk set/order: [PR#1](https://github.com/rimone0511/autopilot-log/pull/1) `QUEUE.md`. CU labels: [PR#8](https://github.com/rimone0511/autopilot-log/pull/8). Pack pointers are **folder-bearing sibling PRs only** (bodies not copied). This file is not a signup log and does not claim an account exists.

**No invented recoveries.** A skip stays a skip until a later human observation writes a new snapshot. This log does not lift hold, solve captcha, clear 403, pass Google access, pass reCAPTCHA, or supply a date of birth.

Forbidden: secrets, OTP, phones, passwords, KYC files, signup, publish, paid plans, bids/proposals, invented traffic/GMV, invented 生年月日.

This page **overrides** older next-CU hints that still pointed at these desks: [PR#24](https://github.com/rimone0511/autopilot-log/pull/24) CrowdWorks, [PR#35](https://github.com/rimone0511/autopilot-log/pull/35) Upwork, [PR#43](https://github.com/rimone0511/autopilot-log/pull/43) / [PR#49](https://github.com/rimone0511/autopilot-log/pull/49) / [PR#53](https://github.com/rimone0511/autopilot-log/pull/53) TimeTicket-current. QUEUE rows are not rewritten here.

## Split

| Split | Meaning |
|---|---|
| **Human can unblock later** | Operator’s **own** browser and network. MAIN Google. After a gate lifts, open a morning KYC slip **only if** an ID screen appears. Leave listings unpublished. For TimeTicket DOB: operator types **own** 生年月日; agent never guesses. |
| **Do-not-retry from agent** | CU / this environment does **not** reload, hold-press, SSO-loop, captcha-loop, or invent missing profile fields. No second Google / second marketplace account. Park and leave. |

KYC morning slips (human, not CU): [PR#43](https://github.com/rimone0511/autopilot-log/pull/43) `earn-morning-kyc-slip-refresh-20260916/` (Fiverr / Lancers / CrowdWorks / Upwork). LinkedIn has **no** slip in that folder. TimeTicket / Contra / Craudia / Freelancer KYC text stays [PR#4](https://github.com/rimone0511/autopilot-log/pull/4). DOB-missing is a **form field skip**, not a KYC upload.

## Six parked desks — agent never retries these reasons

| # | desk | reason | Do-not-retry from agent | Human can unblock later | pack PR (folder only) |
|---|---|---|---|---|---|
| A2 / CU-02 | Fiverr | **Press&Hold** | Do not retry hold / Press & Hold / signup / Identity Verify / **Publish Gig**. Gig + FAQ stay unpublished. | Own browser, VPN **off**. After hold lifts: live photo ID **on the site only**. Gig stays Draft until a separate human GO. | [#6](https://github.com/rimone0511/autopilot-log/pull/6) [#15](https://github.com/rimone0511/autopilot-log/pull/15) · slip `02-fiverr.md` |
| A3 / CU-03 | ランサーズ Lancers | **captcha** | Do not retry captcha / Cloudflare / Press & Hold. Do not signup. Do not 完了-as-publish. | Operator solves captcha in **own** browser. Then profile / パッケージ **draft** only. ID screen → slip `03-lancers.md`. | [#17](https://github.com/rimone0511/autopilot-log/pull/17) |
| A4 / CU-04 | クラウドワークス CrowdWorks | **403** | Do not reGET signup/homepage from this box (live **Forbidden**). Do not complete signup. No 応募. Do not open AI CrowdWorks or PARK (`park.jp`). | Operator opens from **own line**. If the page loads: worker profile **draft** only. ID screen → slip `04-crowdworks.md`. | [#17](https://github.com/rimone0511/autopilot-log/pull/17) [#32](https://github.com/rimone0511/autopilot-log/pull/32) |
| A5 / CU-05 | Upwork | **Google access block** | Do not retry “Your Google account cannot be accessed at this time”. Do not mint a second Google. Catalog **Submit** stays off. **0 Connects**. No proposals. | Operator signs in with MAIN Google on **own device**. After access works: profile / Catalog **draft** only. ID screen → slip `05-upwork.md`. | [#10](https://github.com/rimone0511/autopilot-log/pull/10) [#16](https://github.com/rimone0511/autopilot-log/pull/16) |
| A6 / CU-06 | LinkedIn | **reCAPTCHA** | Do not retry **login** reCAPTCHA. **Not next.** Do not Save a Service Page. Jobs / feed out of scope. Do not mint a second LinkedIn. Services stay GO-gated / not enabled. | Operator solves login reCAPTCHA in **own** browser. Services still wait for a human GO. Outreach drafts exist; they are not this CU. | [#16](https://github.com/rimone0511/autopilot-log/pull/16) [#38](https://github.com/rimone0511/autopilot-log/pull/38) |
| A7 / CU-07 | TimeTicket | **DOB missing** | Do not invent `{{BIRTH_YEAR}}` / month / day. Do not signup to skip the field. Do not 発行完了. Do not upload identifications. Host + ticket packs stay unused this pass. | Operator enters **own** 生年月日 on **own** browser when ready. Profile / ticket stay **draft**. ID screen → PR#4 TimeTicket stop. This log does not record that fill. | [#18](https://github.com/rimone0511/autopilot-log/pull/18) [#41](https://github.com/rimone0511/autopilot-log/pull/41) |

Same six, one line: **Fiverr Press&Hold / Lancers captcha / CrowdWorks 403 / Upwork Google access block / LinkedIn reCAPTCHA / TimeTicket DOB missing — agent does not retry.**

Prior sibling labels (same skips, not recoveries): Fiverr `hold`; Upwork `Google SSO`. TimeTicket was `in_progress` in [PR#49](https://github.com/rimone0511/autopilot-log/pull/49); this morning loop **parks** it. No draft_saved claim.

## Not in this skip log

- Coconala / Gumroad = `draft_saved` (QUEUE `done-draft`). Not a skip.
- Contra / Craudia / Freelancer.com = `pending` open path. See [NEXT-CU.md](NEXT-CU.md).
- Wave B–D activity-gate `dead` / `thin` desks live in those gate SKIP files, not here.

## This PR does not

- Copy or merge sibling PR bodies
- Create marketplace accounts or complete signup
- Store secrets, OTP, phone, bank, ID, or a date of birth
- Send proposals / invites / bids / 応募
- Buy Connects / Seller Plus / Premium / Pro / partner seats
- Change Python posting-gate tests
- Retry Fiverr Press&Hold / Lancers captcha / CrowdWorks 403 / Upwork Google access block / LinkedIn reCAPTCHA / TimeTicket DOB

# RUNBOOK — Wave A `blocked_skip` desks

Date: **2026-09-16**  
Folder: `earn-wave-a-blocked-skip-runbook-20260916/`  
State: **DRAFT-ONLY**  
Live box: [PR#49](https://github.com/rimone0511/autopilot-log/pull/49) `earn-register-status-snapshot-20260916-0519/STATUS.md` (05:19 JST; 05:22 LinkedIn correction)

One page for the five Wave A desks parked `blocked_skip`. Desk set/order: [PR#1](https://github.com/rimone0511/autopilot-log/pull/1) `QUEUE.md`. CU labels: [PR#8](https://github.com/rimone0511/autopilot-log/pull/8). Pack pointers are **folder-bearing sibling PRs only** (bodies not copied). This file is not a signup log and does not claim an account exists.

**MAIN Google only.** Do not invent a second account to walk around a gate.  
**DRAFT_ONLY.** Profiles, gigs, tickets, Catalog, Services stay unpublished.  
Forbidden: secrets, OTP, phones, passwords, KYC files, signup, publish, paid plans, bids/proposals, invented traffic/GMV.

This page **overrides** older “next CU” hints: [PR#24](https://github.com/rimone0511/autopilot-log/pull/24) CrowdWorks-next, [PR#35](https://github.com/rimone0511/autopilot-log/pull/35) Upwork-next, [PR#43](https://github.com/rimone0511/autopilot-log/pull/43) Upwork-pending, LinkedIn-as-next. QUEUE rows are not rewritten here.

## Split

| Split | Meaning |
|---|---|
| **Human can unblock later** | Operator’s **own** browser and network. MAIN Google. After the gate lifts, open the morning KYC slip **only if** an ID screen appears. Leave listings unpublished. |
| **Do-not-retry from agent** | CU / this environment does **not** reload, hold-press, SSO-loop, or captcha-loop the parked reason. No second Google / second marketplace account. Park and leave. |

KYC morning slips (human, not CU): [PR#43](https://github.com/rimone0511/autopilot-log/pull/43) `earn-morning-kyc-slip-refresh-20260916/` (Fiverr / Lancers / CrowdWorks / Upwork). LinkedIn has **no** slip in that folder. TimeTicket / Contra / Craudia / Freelancer KYC text stays [PR#4](https://github.com/rimone0511/autopilot-log/pull/4).

## Five parked desks — agent never retries these reasons

| # | desk | reason | Do-not-retry from agent | Human can unblock later | pack PR (folder only) |
|---|---|---|---|---|---|
| A2 / CU-02 | Fiverr | **hold** | Do not retry hold / Press & Hold / signup / Identity Verify / **Publish Gig**. Gig + FAQ stay unpublished. | Own browser, VPN **off**. After hold lifts: live photo ID **on the site only**. Gig stays Draft until a separate human GO. | [#6](https://github.com/rimone0511/autopilot-log/pull/6) [#15](https://github.com/rimone0511/autopilot-log/pull/15) · slip `02-fiverr.md` |
| A3 / CU-03 | ランサーズ Lancers | **captcha** | Do not retry captcha / Cloudflare / Press & Hold. Do not signup. Do not 完了-as-publish. | Operator solves captcha in **own** browser. Then profile / パッケージ **draft** only. ID screen → slip `03-lancers.md`. | [#17](https://github.com/rimone0511/autopilot-log/pull/17) |
| A4 / CU-04 | クラウドワークス CrowdWorks | **403** | Do not reGET signup/homepage from this box (live **Forbidden**). Do not complete signup. No 応募. Do not open AI CrowdWorks or PARK (`park.jp`). | Operator opens from **own line**. If the page loads: worker profile **draft** only. ID screen → slip `04-crowdworks.md`. | [#17](https://github.com/rimone0511/autopilot-log/pull/17) [#32](https://github.com/rimone0511/autopilot-log/pull/32) |
| A5 / CU-05 | Upwork | **Google SSO** | Do not retry “Your Google account cannot be accessed at this time”. Do not mint a second Google. Catalog **Submit** stays off. **0 Connects**. No proposals. | Operator signs in with MAIN Google on **own device**. After SSO works: profile / Catalog **draft** only. ID screen → slip `05-upwork.md`. | [#10](https://github.com/rimone0511/autopilot-log/pull/10) [#16](https://github.com/rimone0511/autopilot-log/pull/16) |
| A6 / CU-06 | LinkedIn | **reCAPTCHA** | Do not retry **login** reCAPTCHA. **Not next.** Do not Save a Service Page. Jobs / feed out of scope. Do not mint a second LinkedIn. Services stay GO-gated / not enabled. | Operator solves login reCAPTCHA in **own** browser. Services still wait for a human GO. Outreach drafts exist; they are not this CU. | [#16](https://github.com/rimone0511/autopilot-log/pull/16) [#38](https://github.com/rimone0511/autopilot-log/pull/38) |

Same five, one line: **Fiverr hold / Lancers captcha / CrowdWorks 403 / Upwork Google SSO / LinkedIn reCAPTCHA — agent does not retry.**

## Next agent CU (open path)

**TimeTicket → Contra → Craudia → Freelancer.com**

LinkedIn is **not** in this chain. Do not insert it between Upwork and TimeTicket.

| Order | desk | CU hint | This pass | pack PR |
|---|---|---|---|---|
| 1 | TimeTicket (A7 / CU-07) | `in_progress` **current CU** | Host + ticket **draft**. Prefer message (async). No 対面/電話. **No 発行完了.** Do not signup. Stop at KYC. | [#18](https://github.com/rimone0511/autopilot-log/pull/18) [#41](https://github.com/rimone0511/autopilot-log/pull/41) |
| 2 | Contra (A8 / CU-08) | `pending` | After TimeTicket parks. Independent / Share work **draft**. No Pro. Stop at wallet / Persona. | [#18](https://github.com/rimone0511/autopilot-log/pull/18) [#41](https://github.com/rimone0511/autopilot-log/pull/41) |
| 3 | クラウディア Craudia (A9 / CU-09) | `pending` | After Contra. Worker **profile** only. No apply / skill listing. Stop at 本人確認. | [#18](https://github.com/rimone0511/autopilot-log/pull/18) [#51](https://github.com/rimone0511/autopilot-log/pull/51) |
| 4 | Freelancer.com (A10 / CU-10) | `pending` | After Craudia. Profile **draft**. **No bids / contests / Verify Identity.** Surgical-bid templates stay unused this pass. | [#19](https://github.com/rimone0511/autopilot-log/pull/19) [#47](https://github.com/rimone0511/autopilot-log/pull/47) |

Coconala (A1) and Gumroad (A+) stay `draft_saved` (QUEUE `done-draft`). Do not reopen to publish.

Do not start Wave B/C/D CU until Wave A `pending` rows are `draft_saved` or still parked `blocked_skip`.

OTP: Gmail codes = parent (CU does not open Gmail). SMS = wait on user chat; if the user is away, park the live desk and keep this skip map. KYC / liveness / tax / payout → close the tab, pass desk name + screen type to morning operator, do not upload.

## This PR does not

- Copy or merge sibling PR bodies
- Create marketplace accounts or complete signup
- Store secrets, OTP, phone, bank, or ID
- Send proposals / invites / bids / 応募
- Buy Connects / Seller Plus / Premium / Pro / partner seats
- Change Python posting-gate tests
- Retry Fiverr hold / Lancers captcha / CrowdWorks 403 / Upwork Google SSO / LinkedIn reCAPTCHA

# STATUS — Wave A morning-loop snapshot

Snapshot: **2026-09-16 morning loop**  
Folder: `ops/earn/register-wave-a-status-20260916/`  
State: **DRAFT-ONLY**

One-page CU box for Wave A desks after the morning reconcile. Desk set and order come from [PR#1](https://github.com/rimone0511/autopilot-log/pull/1) `QUEUE.md`. CU labels come from [PR#8](https://github.com/rimone0511/autopilot-log/pull/8). Pack pointers are **folder-bearing sibling PRs only** (bodies not copied). This file is not a signup log and does not claim an account exists.

Forbidden: secrets, real emails/phones/passwords, KYC files, signup, publish, paid plans, invented traffic/GMV, invented recoveries (no hold-lift, no captcha-solved, no 403-cleared, no SSO-pass, no reCAPTCHA-pass, no invented 生年月日).

This snapshot **overrides** older “next CU” hints:

- [PR#24](https://github.com/rimone0511/autopilot-log/pull/24) CrowdWorks-next
- [PR#35](https://github.com/rimone0511/autopilot-log/pull/35) Upwork-next
- [PR#43](https://github.com/rimone0511/autopilot-log/pull/43) TimeTicket-next / Upwork-pending
- [PR#49](https://github.com/rimone0511/autopilot-log/pull/49) 05:19/05:22 box (TimeTicket `in_progress`)
- [PR#53](https://github.com/rimone0511/autopilot-log/pull/53) TimeTicket as first next-agent CU

QUEUE `done-draft` / `next` rows are not rewritten here.

Same-folder companions: [NEXT-CU.md](NEXT-CU.md) (open path) · [SKIP-LOG.md](SKIP-LOG.md) (six parked desks).

## CU hint

| Hint | Use |
|---|---|
| `draft_saved` | Seller draft already parked unpublished. Do not reopen to publish |
| `blocked_skip` | Skip this desk this pass. Do not retry the listed reason. Do not invent a recovery |
| `pending` | Not started. Do not open until earlier serial desks are parked |

No Wave A desk is `in_progress` in this box. TimeTicket left `in_progress` (PR#49) and is now `blocked_skip` **DOB missing**.

## Wave A — Top10 + Gumroad

| # | desk | CU hint | reason | pack PR | next action |
|---|---|---|---|---|---|
| A1 / CU-01 | ココナラ Coconala | `draft_saved` | QUEUE `done-draft` | — | Leave listing/profile unpublished. Do not reopen to publish |
| A2 / CU-02 | Fiverr | `blocked_skip` | **Press&Hold** | [#6](https://github.com/rimone0511/autopilot-log/pull/6) [#15](https://github.com/rimone0511/autopilot-log/pull/15) | Park. Do not retry hold / Press & Hold. Gig/FAQ packs stay unpublished |
| A3 / CU-03 | ランサーズ Lancers | `blocked_skip` | **captcha** | [#17](https://github.com/rimone0511/autopilot-log/pull/17) | Park. Do not retry captcha. Do not signup |
| A4 / CU-04 | クラウドワークス CrowdWorks | `blocked_skip` | **403** | [#17](https://github.com/rimone0511/autopilot-log/pull/17) [#32](https://github.com/rimone0511/autopilot-log/pull/32) | Park. Live box Forbidden. Do not retry. No 応募 |
| A5 / CU-05 | Upwork | `blocked_skip` | **Google access block** | [#10](https://github.com/rimone0511/autopilot-log/pull/10) [#16](https://github.com/rimone0511/autopilot-log/pull/16) | Park. Do not retry SSO / “cannot be accessed”. Catalog Submit stays off. 0 Connects |
| A6 / CU-06 | LinkedIn | `blocked_skip` | **reCAPTCHA** | [#16](https://github.com/rimone0511/autopilot-log/pull/16) [#38](https://github.com/rimone0511/autopilot-log/pull/38) | Park. Do not retry reCAPTCHA. Do not Save a Service Page. Jobs / feed out of scope |
| A7 / CU-07 | TimeTicket | `blocked_skip` | **DOB missing** | [#18](https://github.com/rimone0511/autopilot-log/pull/18) [#41](https://github.com/rimone0511/autopilot-log/pull/41) | Park. Do not invent 生年月日. Do not signup. No 発行完了 |
| A8 / CU-08 | Contra | `pending` | — | [#18](https://github.com/rimone0511/autopilot-log/pull/18) [#41](https://github.com/rimone0511/autopilot-log/pull/41) | **Open desk.** Independent / Share work **draft**; no Pro; stop at wallet/Persona |
| A9 / CU-09 | クラウディア Craudia | `pending` | — | [#18](https://github.com/rimone0511/autopilot-log/pull/18) [#51](https://github.com/rimone0511/autopilot-log/pull/51) | After Contra. Worker profile only; no apply; stop at 本人確認 |
| A10 / CU-10 | Freelancer.com | `pending` | — | [#19](https://github.com/rimone0511/autopilot-log/pull/19) [#47](https://github.com/rimone0511/autopilot-log/pull/47) | After Craudia. Profile **draft**; no bids/contests; stop at identity |
| A+ | Gumroad | `draft_saved` | QUEUE `done-draft` | — | Leave product unpublished. Does not occupy CU-11 |

Counts this box: `draft_saved` 2 · `blocked_skip` 6 · `in_progress` 0 · `pending` 3.

LinkedIn pack pointer for outreach drafts is [#38](https://github.com/rimone0511/autopilot-log/pull/38); that pack is not this CU.

## This pass

1. Skip Fiverr (`Press&Hold`), Lancers (`captcha`), CrowdWorks (`403`), Upwork (`Google access block`), LinkedIn (`reCAPTCHA`), TimeTicket (`DOB missing`). No retry. No invented recovery.
2. Open desk is **Contra** (A8 / CU-08). Independent / Share work draft only. Not Pro. Not Persona.
3. After Contra parks: **Craudia → Freelancer.com**.
4. Do not signup. Stop at KYC. Leave profiles/listings unpublished.
5. Do not start Wave B/C/D CU until Wave A `pending` rows are `draft_saved` or still parked `blocked_skip`.

Reason labels of record (this folder). Older sibling wording is the same skip, not a recovery:

| This box | Prior sibling label (same skip) |
|---|---|
| Fiverr **Press&Hold** | `hold` ([PR#49](https://github.com/rimone0511/autopilot-log/pull/49) / [PR#53](https://github.com/rimone0511/autopilot-log/pull/53)) |
| Upwork **Google access block** | `Google SSO` / “Your Google account cannot be accessed at this time” |
| TimeTicket **DOB missing** | was `in_progress` **current CU** in PR#49 — **not** recovered here |

## This PR does not

- Copy or merge sibling PR bodies
- Create marketplace accounts or complete signup
- Store secrets, OTP, phone, bank, ID, or a date of birth
- Send proposals / invites / bids / 応募
- Buy Connects / Seller Plus / Premium / Pro / partner seats
- Change Python posting-gate tests
- Retry Fiverr Press&Hold / Lancers captcha / CrowdWorks 403 / Upwork Google access block / LinkedIn reCAPTCHA / TimeTicket DOB
- Invent a TimeTicket 生年月日 or mark any parked desk `draft_saved`

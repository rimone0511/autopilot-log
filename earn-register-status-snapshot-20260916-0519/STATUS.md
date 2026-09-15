# STATUS — Wave A live snapshot

Snapshot: **2026-09-16 05:19 JST**  
Folder: `earn-register-status-snapshot-20260916-0519/`  
State: **DRAFT-ONLY**

One-page CU box for Wave A desks. Desk set and order come from [PR#1](https://github.com/rimone0511/autopilot-log/pull/1) `QUEUE.md`. CU labels come from [PR#8](https://github.com/rimone0511/autopilot-log/pull/8). Pack pointers are **folder-bearing sibling PRs only** (bodies not copied). This file is not a signup log and does not claim an account exists.

Forbidden: secrets, real emails/phones/passwords, KYC files, signup, publish, paid plans, invented traffic/GMV.

This snapshot **overrides** older “next CU” hints: [PR#24](https://github.com/rimone0511/autopilot-log/pull/24) CrowdWorks-next, [PR#35](https://github.com/rimone0511/autopilot-log/pull/35) Upwork-next, [PR#43](https://github.com/rimone0511/autopilot-log/pull/43) Upwork-pending. QUEUE `done-draft` / `next` rows are not rewritten here.

## CU hint

| Hint | Use |
|---|---|
| `draft_saved` | Seller draft already parked unpublished. Do not reopen to publish |
| `blocked_skip` | Skip this desk this pass. Do not retry the listed reason |
| `in_progress` | Live CU is on this desk, with the scope in the reason column |
| `pending` | Not started. Do not open until earlier serial desks are parked |

## Wave A — Top10 + Gumroad

| # | desk | CU hint | reason | pack PR | next action |
|---|---|---|---|---|---|
| A1 / CU-01 | ココナラ Coconala | `draft_saved` | QUEUE `done-draft` | — | Leave listing/profile unpublished. Do not reopen to publish |
| A2 / CU-02 | Fiverr | `blocked_skip` | **hold** | [#6](https://github.com/rimone0511/autopilot-log/pull/6) [#15](https://github.com/rimone0511/autopilot-log/pull/15) | Park. Do not retry CU. Gig/FAQ packs stay unpublished |
| A3 / CU-03 | ランサーズ Lancers | `blocked_skip` | **captcha** | [#17](https://github.com/rimone0511/autopilot-log/pull/17) | Park. Do not retry CU. Do not signup |
| A4 / CU-04 | クラウドワークス CrowdWorks | `blocked_skip` | **403** | [#17](https://github.com/rimone0511/autopilot-log/pull/17) | Park. Live box Forbidden. Do not retry. No 応募 |
| A5 / CU-05 | Upwork | `blocked_skip` | **Google SSO** | [#10](https://github.com/rimone0511/autopilot-log/pull/10) [#16](https://github.com/rimone0511/autopilot-log/pull/16) | Park. Do not retry SSO. Catalog Submit stays off. 0 Connects |
| A6 / CU-06 | LinkedIn | `in_progress` | **profile-only** | [#16](https://github.com/rimone0511/autopilot-log/pull/16) | Continue personal profile fields only. Do not Save a Service Page if Save makes it viewable. Jobs / feed out of scope |
| A7 / CU-07 | TimeTicket | `pending` | — | [#18](https://github.com/rimone0511/autopilot-log/pull/18) | After LinkedIn parks. Host + ticket **draft**; prefer message (async); no 発行完了 |
| A8 / CU-08 | Contra | `pending` | — | [#18](https://github.com/rimone0511/autopilot-log/pull/18) | After TimeTicket. Independent / Share work **draft**; no Pro; stop at wallet/Persona |
| A9 / CU-09 | クラウディア Craudia | `pending` | — | [#18](https://github.com/rimone0511/autopilot-log/pull/18) | After Contra. Worker profile only; no apply; stop at 本人確認 |
| A10 / CU-10 | Freelancer.com | `pending` | — | [#19](https://github.com/rimone0511/autopilot-log/pull/19) | After Craudia. Profile **draft**; no bids/contests; stop at identity |
| A+ | Gumroad | `draft_saved` | QUEUE `done-draft` | — | Leave product unpublished. Does not occupy CU-11 |

Counts this box: `draft_saved` 2 · `blocked_skip` 4 · `in_progress` 1 · `pending` 4.

## This pass

1. Skip Fiverr (`hold`), Lancers (`captcha`), CrowdWorks (`403`), Upwork (`Google SSO`). No retry.
2. Open desk is **LinkedIn, profile-only**. Not Services publish. Not Jobs.
3. First remaining `pending` after LinkedIn parks is **TimeTicket** (A7). Then Contra → Craudia → Freelancer.com.
4. Do not signup. Stop at KYC. Leave profiles/listings unpublished.
5. Do not start Wave B/C/D CU until Wave A `pending` rows are `draft_saved` or still parked `blocked_skip`.

## This PR does not

- Copy or merge sibling PR bodies
- Create marketplace accounts or complete signup
- Store secrets, OTP, phone, bank, or ID
- Send proposals / invites / bids
- Buy Connects / Seller Plus / Premium / partner seats
- Change Python posting-gate tests

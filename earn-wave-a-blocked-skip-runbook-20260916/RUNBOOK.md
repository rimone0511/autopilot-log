# RUNBOOK — Wave A `blocked_skip` desks

Date: **2026-09-16**  
Correction: **2026-09-16** — LinkedIn reCAPTCHA is **not** permanently never-retry. User ordered **captcha try-first**. TimeTicket is **DOB-waiting**, not current CU.  
Folder: `earn-wave-a-blocked-skip-runbook-20260916/`  
State: **DRAFT-ONLY**  
Prior live box: [PR#49](https://github.com/rimone0511/autopilot-log/pull/49) (TimeTicket `in_progress` — **stale**). Morning-loop sibling: [PR#54](https://github.com/rimone0511/autopilot-log/pull/54) (TimeTicket DOB park — **keep**; LinkedIn never-retry — **override here**).

One page for Wave A desks that are parked `blocked_skip` **or** on a try-first captcha. Desk set/order: [PR#1](https://github.com/rimone0511/autopilot-log/pull/1) `QUEUE.md`. CU labels: [PR#8](https://github.com/rimone0511/autopilot-log/pull/8). Pack pointers are **folder-bearing sibling PRs only** (bodies not copied). This file is not a signup log and does not claim an account exists.

**MAIN Google only.** Do not invent a second account to walk around a gate.  
**DRAFT_ONLY.** Profiles, gigs, tickets, Catalog, Services stay unpublished.  
Forbidden: secrets, OTP, phones, passwords, KYC files, signup, publish, paid plans, bids/proposals, invented traffic/GMV, invented 生年月日.

This page **overrides** older “next CU” hints: [PR#24](https://github.com/rimone0511/autopilot-log/pull/24) CrowdWorks-next, [PR#35](https://github.com/rimone0511/autopilot-log/pull/35) Upwork-next, [PR#43](https://github.com/rimone0511/autopilot-log/pull/43) TimeTicket-next, [PR#49](https://github.com/rimone0511/autopilot-log/pull/49) TimeTicket-current, this file’s first revision (LinkedIn never-retry + TimeTicket-first), and [PR#54](https://github.com/rimone0511/autopilot-log/pull/54) LinkedIn-never / Contra-only-open. QUEUE rows are not rewritten here.

## Split

| Split | Meaning |
|---|---|
| **Agent try-first** | **LinkedIn login captcha only.** Checkbox / Press & Hold: agent tries. Image / tile puzzle: **stop** and hand the box to a human. After **3** failed agent attempts, park again. |
| **Do-not-retry from agent** | Fiverr hold · Lancers captcha · CrowdWorks 403 · Upwork Google SSO · TimeTicket DOB. CU does **not** reload, SSO-loop, or invent a date of birth. No second Google / second marketplace account. |
| **Human can unblock later** | Operator’s **own** browser and network. MAIN Google. After the gate lifts, open the morning KYC slip **only if** an ID screen appears. Leave listings unpublished. |

KYC morning slips (human, not CU): [PR#43](https://github.com/rimone0511/autopilot-log/pull/43) `earn-morning-kyc-slip-refresh-20260916/` (Fiverr / Lancers / CrowdWorks / Upwork). LinkedIn has **no** slip there. TimeTicket / Contra / Craudia / Freelancer KYC text stays [PR#4](https://github.com/rimone0511/autopilot-log/pull/4).

## LinkedIn (A6 / CU-06) — captcha try-first

**Current live CU may be this desk** (login reCAPTCHA retry). It is **not** a permanent `blocked_skip`.

User order 2026-09-16: try-first. Click / Press & Hold by the agent. Image puzzle → box handoff.

| Step | Agent | Human |
|---|---|---|
| Checkbox / “I’m not a robot” / Press & Hold | **Try.** Pointer hold **must** send `holdDurationMs` (start **1800**; **one retry this session** at **2500**). Do not fake a hold with click+sleep. If the schema has no `holdDurationMs`: STOP (`tool_missing_holdDurationMs`). **Once per session** — do not hammer. | — |
| Image / tile / select-the-buses puzzle | **Stop.** Do not click tiles. Do not guess. Write `image_puzzle` and **hand the box to a human**. | Solve the puzzle in the same box, then return the session. |
| Checkbox/hold **fails** | Count **1 attempt** (the 1800+2500 pair is one session, one attempt). Leave. Next CU session may retry. | — |
| **3 failed agent attempts** | Park again as `blocked_skip` **reCAPTCHA**. Stop opening this desk this pass. | Own browser later, if still gated. |
| Captcha **passes** | Continue A6 **draft** only. Pack [#16](https://github.com/rimone0511/autopilot-log/pull/16) [#38](https://github.com/rimone0511/autopilot-log/pull/38). **Do not Save** a Service Page if Save = viewable. Jobs / feed out of scope. No second LinkedIn. Services stay GO-gated / not enabled until a human GO. | — |

Do not mint a second LinkedIn to skip the wall.

## Parked — agent never retries these reasons

| # | desk | reason | Do-not-retry from agent | Human can unblock later | pack PR (folder only) |
|---|---|---|---|---|---|
| A2 / CU-02 | Fiverr | **hold** | Do not retry hold / Press & Hold / signup / Identity Verify / **Publish Gig**. Gig + FAQ stay unpublished. | Own browser, VPN **off**. After hold lifts: live photo ID **on the site only**. Gig stays Draft until a separate human GO. | [#6](https://github.com/rimone0511/autopilot-log/pull/6) [#15](https://github.com/rimone0511/autopilot-log/pull/15) · slip `02-fiverr.md` |
| A3 / CU-03 | ランサーズ Lancers | **captcha** | Do not retry captcha / Cloudflare / Press & Hold. Do not signup. Do not 完了-as-publish. (Try-first is **LinkedIn only**.) | Operator solves captcha in **own** browser. Then profile / パッケージ **draft** only. ID screen → slip `03-lancers.md`. | [#17](https://github.com/rimone0511/autopilot-log/pull/17) |
| A4 / CU-04 | クラウドワークス CrowdWorks | **403** | Do not reGET signup/homepage from this box (live **Forbidden**). Do not complete signup. No 応募. Do not open AI CrowdWorks or PARK (`park.jp`). | Operator opens from **own line**. If the page loads: worker profile **draft** only. ID screen → slip `04-crowdworks.md`. | [#17](https://github.com/rimone0511/autopilot-log/pull/17) [#32](https://github.com/rimone0511/autopilot-log/pull/32) |
| A5 / CU-05 | Upwork | **Google SSO** | Do not retry “Your Google account cannot be accessed at this time”. Do not mint a second Google. Catalog **Submit** stays off. **0 Connects**. No proposals. | Operator signs in with MAIN Google on **own device**. After SSO works: profile / Catalog **draft** only. ID screen → slip `05-upwork.md`. | [#10](https://github.com/rimone0511/autopilot-log/pull/10) [#16](https://github.com/rimone0511/autopilot-log/pull/16) |
| A7 / CU-07 | TimeTicket | **DOB-waiting** | **Not current CU.** Do not invent `{{BIRTH_YEAR}}` / month / day. Do not signup to skip the field. **No 発行完了.** Host + ticket packs unused until DOB is filled. | Operator enters **own** 生年月日 on **own** browser when ready. Profile / ticket stay **draft**. ID screen → PR#4. This page does not record that fill. | [#18](https://github.com/rimone0511/autopilot-log/pull/18) [#41](https://github.com/rimone0511/autopilot-log/pull/41) |

Never-retry line: **Fiverr hold / Lancers captcha / CrowdWorks 403 / Upwork Google SSO / TimeTicket DOB — agent does not retry.**  
LinkedIn is **not** on that line.

## Next agent CU (open path)

**Live (may be current): LinkedIn captcha retry** → then **Contra → Craudia → Freelancer.com**.

TimeTicket is **out of this chain** until a human fills DOB. Do not insert it between LinkedIn and Contra.

| Order | desk | CU hint | This pass | pack PR |
|---|---|---|---|---|
| 0 | LinkedIn (A6 / CU-06) | **try-first** (may be **current CU**) | Login captcha per the table above. If it passes: Services **draft** only; no Save-as-publish. If image puzzle: box handoff. After 3 failed agent attempts: park again. | [#16](https://github.com/rimone0511/autopilot-log/pull/16) [#38](https://github.com/rimone0511/autopilot-log/pull/38) |
| — | TimeTicket (A7 / CU-07) | `blocked_skip` **DOB-waiting** | Skip. Not current CU. | [#18](https://github.com/rimone0511/autopilot-log/pull/18) [#41](https://github.com/rimone0511/autopilot-log/pull/41) |
| 1 | Contra (A8 / CU-08) | `pending` | After LinkedIn parks (pass, image handoff done, or 3-fail skip). Independent / Share work **draft**. No Pro. Stop at wallet / Persona. | [#18](https://github.com/rimone0511/autopilot-log/pull/18) [#41](https://github.com/rimone0511/autopilot-log/pull/41) |
| 2 | クラウディア Craudia (A9 / CU-09) | `pending` | After Contra. Worker **profile** only. No apply / skill listing. Stop at 本人確認. | [#18](https://github.com/rimone0511/autopilot-log/pull/18) [#51](https://github.com/rimone0511/autopilot-log/pull/51) |
| 3 | Freelancer.com (A10 / CU-10) | `pending` | After Craudia. Profile **draft**. **No bids / contests / Verify Identity.** Surgical-bid templates stay unused this pass. | [#19](https://github.com/rimone0511/autopilot-log/pull/19) [#47](https://github.com/rimone0511/autopilot-log/pull/47) |

Coconala (A1) and Gumroad (A+) stay `draft_saved` (QUEUE `done-draft`). Do not reopen to publish.

Do not start Wave B/C/D CU until Wave A `pending` rows are `draft_saved` or still parked `blocked_skip` (LinkedIn counts as parked only after a 3-fail or an explicit park).

OTP: Gmail codes = parent (CU does not open Gmail). SMS = wait on user chat; if the user is away, park the live desk. KYC / liveness / tax / payout / TimeTicket 生年月日 → close the tab, pass desk name + screen type to morning operator, do not upload, do not invent a date.

## This PR does not

- Copy or merge sibling PR bodies
- Create marketplace accounts or complete signup
- Store secrets, OTP, phone, bank, ID, or a date of birth
- Send proposals / invites / bids / 応募
- Buy Connects / Seller Plus / Premium / Pro / partner seats
- Change Python posting-gate tests
- Retry Fiverr hold / Lancers captcha / CrowdWorks 403 / Upwork Google SSO / TimeTicket DOB
- Click LinkedIn **image-puzzle** tiles, or hammer LinkedIn checkbox/hold more than **once per session**, or reopen LinkedIn after **3** failed agent attempts

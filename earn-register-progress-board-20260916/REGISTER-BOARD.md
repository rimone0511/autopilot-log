# REGISTER-BOARD — Wave A–D CU status

Board date: 2026-09-16  
Folder: `earn-register-progress-board-20260916/`  
State: **DRAFT-ONLY**

This file is a desk map. It does **not** copy sibling PR bodies. Waves come from [PR#1](https://github.com/rimone0511/autopilot-log/pull/1) `earn-register-expand-20260916/QUEUE.md`. Pack PRs are the folder-bearing PRs among **#1–#22**. CU status is a hint for the next computer-use pass, not a claim that an account exists.

Forbidden here: secrets, real emails/phones/passwords, KYC files, signup, publish, paid plans, invented traffic/GMV.

## Columns

| Column | Meaning |
|---|---|
| desk | Marketplace / seller-side desk name |
| wave | QUEUE wave (`A` / `B` / `C` / `C-LATE` / `D` / `D-ext`) |
| pack PR if any | Sibling PR number whose **folder** holds a paste/handoff/listing pack for that desk. `—` = no pack folder among #1–#22. Gate/index/runbook PRs are not packs |
| CU status hint | `pending` / `blocked_skip` / `draft` only (see below) |
| next action | One CU/operator step. Not a signup script |

### CU status hint

| Hint | Use |
|---|---|
| `draft` | QUEUE already `done-draft`. Leave unpublished. Do not re-open to publish |
| `blocked_skip` | CU must skip this desk this pass |
| `pending` | CU has not finished a seller draft. Do not start until earlier `blocked_skip` / serial desks are parked |

Operator locks for this board:

- **Fiverr** = `blocked_skip` **hold**
- **Lancers** = `blocked_skip` **captcha**

Serial (PR#7 runbook, not copied): Fiverr → Lancers → CrowdWorks → Upwork → LinkedIn Services → TimeTicket → Contra → Craudia → Freelancer.com → Wave B **gate `pass` only**. This board does not start Wave B while Wave A still has `pending` desks.

---

## PR#1–#22 folder names (no bodies)

| PR | Folder |
|---|---|
| [#1](https://github.com/rimone0511/autopilot-log/pull/1) | `earn-register-expand-20260916/` |
| [#2](https://github.com/rimone0511/autopilot-log/pull/2) | `earn-register-packs-20260916/` |
| [#3](https://github.com/rimone0511/autopilot-log/pull/3) | `earn-register-packs-jp-20260916/` |
| [#4](https://github.com/rimone0511/autopilot-log/pull/4) | `earn-kyc-morning-checklist-20260916/` |
| [#5](https://github.com/rimone0511/autopilot-log/pull/5) | `earn-en-proposal-drafts-20260916/` |
| [#6](https://github.com/rimone0511/autopilot-log/pull/6) | `earn-fiverr-gig-draft-20260916/` |
| [#7](https://github.com/rimone0511/autopilot-log/pull/7) | `earn-cu-runbook-20260916/` |
| [#8](https://github.com/rimone0511/autopilot-log/pull/8) | `earn-register-pack-index-20260916/` |
| [#9](https://github.com/rimone0511/autopilot-log/pull/9) | `ops-bake-orch-cli-20260916/` (not a market desk) |
| [#10](https://github.com/rimone0511/autopilot-log/pull/10) | `earn-upwork-catalog-draft-20260916/` |
| [#11](https://github.com/rimone0511/autopilot-log/pull/11) | `earn-jp-proposal-drafts-20260916/` |
| [#12](https://github.com/rimone0511/autopilot-log/pull/12) | `earn-activity-gate-waveB-20260916/` |
| [#13](https://github.com/rimone0511/autopilot-log/pull/13) | `earn-activity-gate-waveD-20260916/` |
| [#14](https://github.com/rimone0511/autopilot-log/pull/14) | `earn-register-pack-master-index-20260916/` |
| [#15](https://github.com/rimone0511/autopilot-log/pull/15) | `earn-fiverr-requirements-faq-polish-20260916/` |
| [#16](https://github.com/rimone0511/autopilot-log/pull/16) | `earn-upwork-linkedin-cu-handoff-20260916/` |
| [#17](https://github.com/rimone0511/autopilot-log/pull/17) | `earn-lancers-cw-cu-handoff-20260916/` |
| [#18](https://github.com/rimone0511/autopilot-log/pull/18) | `earn-timeticket-contra-craudia-handoff-20260916/` |
| [#19](https://github.com/rimone0511/autopilot-log/pull/19) | `earn-freelancer-waveb-gap-notes-20260916/` |
| [#20](https://github.com/rimone0511/autopilot-log/pull/20) | `earn-activity-gate-wave-d-late-20260916/` |
| [#21](https://github.com/rimone0511/autopilot-log/pull/21) | `earn-waveb-alive-handoff-sample-20260916/` |
| [#22](https://github.com/rimone0511/autopilot-log/pull/22) | `earn-activity-gate-wave-d-early-20260916/` |

Prep-only (not “pack PR” in the desk table): #1 QUEUE, #4 KYC morning, #5/#11 HANDS (do not send), #7 runbook, #8/#14 indexes, #9 ops-bake, #12/#13/#20/#22 activity-gates.

---

## Wave A — Top10 + Gumroad

| desk | wave | pack PR if any | CU status hint | next action |
|---|---|---|---|---|
| ココナラ Coconala | A | — | `draft` | Leave listing/profile unpublished. Do not reopen to publish |
| Fiverr | A | #6 #15 | `blocked_skip` | **hold.** Park. Do not retry CU. Do not signup. Gig/FAQ packs stay unpublished |
| ランサーズ Lancers | A | #17 | `blocked_skip` | **captcha.** Park. Do not retry CU. Do not signup |
| クラウドワークス CrowdWorks | A | #17 | `pending` | **First pending after the two skips.** Seller profile draft only when CU runs; no 応募; stop at KYC |
| Upwork | A | #10 #16 | `pending` | After CrowdWorks. Catalog/profile draft; 0 Connects; do not Submit |
| LinkedIn Services | A | #16 | `pending` | After Upwork. Service Page draft; Jobs/feed out of scope |
| TimeTicket | A | #18 | `pending` | After LinkedIn. Host profile + ticket **draft**; prefer message (async); no 発行完了 |
| Contra | A | #18 | `pending` | After TimeTicket. Independent / Share work **draft**; no Pro; stop at wallet/Persona |
| クラウディア Craudia | A | #18 | `pending` | After Contra. Worker profile only; no apply; stop at 本人確認 |
| Freelancer.com | A | #19 | `pending` | After Craudia. Profile **draft**; no bids/contests; stop at identity |
| Gumroad | A+ | — | `draft` | Leave product unpublished. Do not reopen to publish. Does not occupy CU-11 |

CU-01–CU-10 labels live in `earn-register-pack-index-20260916/` (PR#8). This board does not renumber them.

---

## Wave B — Week-2

Do not CU-register Wave B until Wave A `pending` desks are `draft` or parked `blocked_skip`. Runbook: only activity-gate **`pass`** desks. `needs_check` stays park-until-re-read (PR#12). No signup.

| desk | wave | pack PR if any | CU status hint | next action |
|---|---|---|---|---|
| SOKUDAN | B | #3 #21 | `pending` | After Wave A. Gate `pass`. Talent draft; remote-ok check on live form |
| Workship | B | #3 | `pending` | After Wave A. Gate `pass`. Confirm Google icon on live signup **page** (do not complete signup here) |
| 複業クラウド | B | #3 #21 | `pending` | After Wave A. Gate `needs_check`. Talent side only; re-read listing dates before CU |
| CrowdLinks | B | #3 | `pending` | After Wave A. Gate `needs_check`. Worker side; skip `/client/` |
| Anycrew | B | #3 #21 | `pending` | After Wave A. Gate `needs_check`. Talent side; skip biz console |
| MENTA | B | #3 #21 | `pending` | After Wave A. Gate `needs_check`. Mentor **plan draft**; do not publish |
| ストアカ | B | #3 #21 | `pending` | After Wave A. Gate `needs_check`. Lecturer **講座 draft**; WAF ≠ dead |
| Guru.com | B | #2 | `pending` | After JP Week2 pass desks. Gate `pass`. Free Basic only; skip paid verify |
| PeoplePerHour | B | #2 | `pending` | After Guru. Seller path `blocked_paid_plan` on public Terms — do not subscribe; click-time free submit check only |
| Malt.com | B | #2 | `pending` | After PPH decision. EN profile **draft**; stop at AML docs |
| Workana | B | #2 | `pending` | After Malt. Talent **draft**; jobs list `needs_check`; skip paid moderation |
| Freelancermap | B | — | `pending` | After GLOBAL four. No pack folder yet; generic map only; record DE/EU bias |
| YOUTRUST | B | — | `pending` | Gate `needs_check`. Profile draft if CU ever opens; SNS-link ask → record; KYC → stop |
| Offers | B | — | `pending` | Gate `pass`. Talent / 業務委託 side; if Jobs is 転職-only, re-gate |
| AI CrowdWorks | B | #19 | `pending` | Gate `needs_check`. Notes only (not a full pack). Confirm seller entry still open before any CU; closed → drop to `gate` |
| Skill Shift | B | #19 | `pending` | Gate `pass` on skill-shift.com (QUEUE host DNS failed). Notes only. On-site-only cards → SKIP local |
| ITプロパートナーズ | B | — | `pending` | Gate `pass`. Freelance profile **draft** only |

Shufti has a JP pack in #3 but QUEUE wave is **D** (`gate`). It is listed under Wave D, not here.

---

## Wave C — Fit High remainder + LATE

Pack folders among #1–#22: none. note / Braintrust also appear in D-early gate (#22); wave of record stays **C**.

| desk | wave | pack PR if any | CU status hint | next action |
|---|---|---|---|---|
| ビザスク | C | — | `pending` | After Wave B. Advisor profile **draft**. No pack |
| クラウドテック | C | — | `pending` | After Wave B. If agent interview is mandatory → treat as LATE, do not CU-push |
| レバテックフリーランス | C | — | `pending` | After Wave B. Profile **draft** only if a sales desk attaches |
| note | C | — | `pending` | After Wave B. Paid note / membership **draft**; do not publish. D-early #22 keep_queue |
| BOOTH | C | — | `pending` | After Wave B. Product **draft**; do not publish |
| Kwork | C | — | `pending` | After Wave B. Seller service **draft** |
| Codementor | C | — | `pending` | After Wave B. Mentor profile **draft** |
| Braintrust | C | — | `pending` | After Wave B. Talent **draft**; ID verification → stop. D-early #22 keep_queue |
| Zapier Solution Partners | C-LATE | — | `pending` | Morning operator. CU does not submit partner applications |
| Make Partners | C-LATE | — | `pending` | Morning operator. CU does not submit partner applications |
| n8n Experts / Creators | C-LATE | — | `pending` | Morning operator. If entry is community-post only → `gate`. CU does not apply |
| Toptal | C-LATE | — | `pending` | Morning operator. Screening + KYC. Do not register this pass |

---

## Wave D — Fit Med (QUEUE D1–D8)

**No signup.** Gate folders: #13 (Fit-Med), #22 (D-early overlap), #12 (Shufti also on JP Wave B gate). Promote only after `pass`; still behind A/B.

| desk | wave | pack PR if any | CU status hint | next action |
|---|---|---|---|---|
| シュフティ Shufti | D | #3 | `pending` | Stay `gate` / `needs_check`. Pack exists; do not register until listing dates are readable |
| ママワークス | D | — | `pending` | Gate `pass` (#13). Behind A/B. Apply-type board — do not 応募. No pack |
| Twine | D | — | `pending` | Gate `pass` (#13/#22). Direct-post Remote only; skip Ari aggregator path. No pack |
| 99designs | D | — | `blocked_skip` | Gate `fail-thin` (#13). Contest-centric. Stay SKIP |
| Truelancer | D | — | `pending` | Gate `pass` (#13). Behind A/B. Profile **draft** only if CU ever reaches D. No pack |
| Fastwork | D | — | `pending` | Gate `pass` (#13/#22). AI Automation category; stop at pre-hire ID. No pack |
| Dribbble Services | D | — | `pending` | Gate `pass` (#13) for **Services** packs. Jobs board = aggregator skip. No pack |
| Wellfound | D | — | `blocked_skip` | Gate `fail-aggregator` (#13). Startup jobs board only. Stay SKIP |

---

## Wave D extensions (not QUEUE D1–D8)

Desks added by later gate folders. Wave label `D-ext`. Still no signup. D-late (#20) is all skip — CU does not open them.

| desk | wave | pack PR if any | CU status hint | next action |
|---|---|---|---|---|
| SKIMA | D-ext | — | `pending` | Gate `pass` (#13). Behind A/B. Commission listings; Google path on public page. No pack |
| Payhip | D-ext | — | `pending` | Gate `pass` (#13). Invisible draft in help. Behind A/B. No pack |
| Ko-fi | D-ext | — | `pending` | Gate `pass` (#13). Shop/memberships. Behind A/B. No pack |
| ワークシフト | D-ext | — | `pending` | Gate `pass` (#13). Not Workship. Behind A/B. Skip on-site cards. No pack |
| カイコク | D-ext | — | `pending` | D-early #22 `needs_check`. Public jobs are case studies without dates. Do not promote |
| 99freelas | D-ext | — | `pending` | D-early #22 keep_queue. Behind A/B. Draft only. No pack |
| Gulp | D-ext | — | `pending` | D-early #22 keep_queue. Behind A/B. Skip on-site. No pack |
| Twago | D-ext | — | `blocked_skip` | D-early #22 skip_log / dead (talent-pool, no public freelance board) |
| Xing Projects | D-ext | — | `blocked_skip` | D-early #22 skip_log / dead (`/projects` 404) |
| Comet | D-ext | — | `blocked_skip` | D-late #20 fail-closed (personal space closed) |
| Replit Bounties | D-ext | — | `blocked_skip` | D-late #20 fail-closed (redirect off-desk) |
| Superpeer | D-ext | — | `blocked_skip` | D-late #20 fail-closed (sunset) |
| We Work Remotely | D-ext | — | `blocked_skip` | D-late #20 fail-aggregator |
| Remote OK | D-ext | — | `blocked_skip` | D-late #20 fail-aggregator |
| Himalayas | D-ext | — | `blocked_skip` | D-late #20 fail-aggregator |
| ココナラテック | D-ext | — | `blocked_skip` | D-late #20 skip-agent (interview/review). Not Coconala A1 |
| Findy Freelance | D-ext | — | `blocked_skip` | D-late #20 skip-agent |
| PRONI アイミツ | D-ext | — | `blocked_skip` | D-late #20 fail-thin (enterprise quotes) |
| 比較ビズ | D-ext | — | `blocked_skip` | D-late #20 fail-thin |

D-early #22 also gated note, Braintrust, Shufti, Twine, Fastwork — those rows stay in Wave C / D above. Do not duplicate.

Catalog-gap notes in #19 (`AI CrowdWorks`, `Skill Shift`, plus non-QUEUE DMM 生成AI人材バンク / Workshift) are **notes**, not extra Wave D desks. Non-QUEUE pair: do not add to this board as register targets.

---

## This pass (CU)

1. Skip Fiverr (`blocked_skip` **hold**).
2. Skip Lancers (`blocked_skip` **captcha**).
3. First `pending` Wave A desk is CrowdWorks (pack folder `earn-lancers-cw-cu-handoff-20260916/`, PR#17).
4. Do not signup. Stop at KYC. Leave profiles/listings unpublished.
5. Do not start Wave B/C/D CU until Wave A `pending` rows are `draft` or still parked.

---

## This PR does not

- Copy or merge sibling PR bodies
- Create marketplace accounts
- Store secrets, OTP, phone, bank, or ID
- Send proposals (HANDS #5 / #11)
- Buy Connects / Seller Plus / partner seats
- Change Python posting-gate tests

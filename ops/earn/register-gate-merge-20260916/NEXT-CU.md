# NEXT-CU — JOBS phase after Freelancer.com (register-winddown)

Stamp: **2026-09-16 JST**  
Folder: `ops/earn/register-gate-merge-20260916/`  
State: **DRAFT_ONLY**  
Policy: **register-winddown + jobs-first**  
Rollup (gate inventory only): [MERGE.md](MERGE.md) · box: [STATUS.md](STATUS.md)

This page **corrects** the previous Wave B register serial on this folder. After Freelancer.com parks, **do not** queue:

```
Workship (CU-11) → SOKUDAN (CU-13) → Offers (CU-25) → MENTA (CU-16) → ストアカ (CU-17)
```

That chain (and [PR#50](https://github.com/rimone0511/autopilot-log/pull/50) Workship → SOKUDAN → Offers) is **cut**. Wave B **register CU is cut**. Morning gate `alive` / `pass` desks in [MERGE.md](MERGE.md) stay inventory, not a signup queue.

This page is **not** a signup log and does not claim an account exists. **MAIN Google only.** Forbidden: secrets, OTP values, phones, passwords, KYC files, invented traffic/GMV, invented recoveries.

Until Freelancer.com parks (`draft_saved` or a documented stop that is not a retry of a Wave A skip), finish **register** only:

```
Craudia (A9 / CU-09) → Freelancer.com (A10 / CU-10)
```

Contra Independent is already `draft_saved` ([PR#64](https://github.com/rimone0511/autopilot-log/pull/64)). Do not reopen Contra to publish the profile. Do not jump TimeTicket. Wave A `blocked_skip` desks stay parked ([PR#54](https://github.com/rimone0511/autopilot-log/pull/54)).

When Freelancer parks: **registration phase ends.** Switch to **JOBS phase**. No new marketplace register CU (Wave B / C / D).

## JOBS serial (after Freelancer parks)

```
Coconala service draft (publish-ready)
  → Gumroad look (don't ship)
  → Contra / Freelancer proposals
```

| Order | desk | CU hint | This pass | pack PR (pointer only) |
|---|---|---|---|---|
| 1 | ココナラ Coconala (A1 / CU-01) | `draft_saved` (QUEUE `done-draft`) | Existing **service draft → publish-ready**. Fill/check the live 出品 form from sibling paste only. Live form wins. **Publish is operator GO** (this markdown PR does not click 公開). No new account. | [#1](https://github.com/rimone0511/autopilot-log/pull/1) QUEUE · [#11](https://github.com/rimone0511/autopilot-log/pull/11) · [#43](https://github.com/rimone0511/autopilot-log/pull/43) |
| 2 | Gumroad (A+) | `draft_saved` (QUEUE `done-draft`) | **Look-don't-ship.** Title / price / icons on unpublished SKU-0. Do not Publish / Enable. Do not New product if the unpublished SKU is absent. Do not announce a live product URL. Stop at payout / bank / tax / ID. | [#55](https://github.com/rimone0511/autopilot-log/pull/55) [#63](https://github.com/rimone0511/autopilot-log/pull/63) |
| 3a | Contra (A8 / CU-08) | `draft_saved` | **Proposals / opportunity apply** from sibling HANDS packs. Profile stays unpublished. No Pro. No Persona from this sheet. One listing at a time. Skip if `{{ONE_SPECIFIC_DETAIL}}` cannot be filled. Send = human GO in the official UI. | [#5](https://github.com/rimone0511/autopilot-log/pull/5) [#64](https://github.com/rimone0511/autopilot-log/pull/64) |
| 3b | Freelancer.com (A10 / CU-10) | after profile parks | **Surgical proposals** (one listing per style, then stop). Templates stay in siblings. **No contests. No wallet top-up. No Verify my Identity.** Skip if `{{ONE_SPECIFIC_DETAIL}}` missing. Click Bid only on later human GO in the official UI. Stop if the form demands funding / KYC / paid upgrade. | [#47](https://github.com/rimone0511/autopilot-log/pull/47) [#57](https://github.com/rimone0511/autopilot-log/pull/57) [#66](https://github.com/rimone0511/autopilot-log/pull/66) |

Coconala before Gumroad before proposals. Contra and Freelancer proposal desks may run after the two look/publish-ready checks; do not open Wave B register between them.

This authoring PR still **does not** signup, Publish, or send. JOBS CU follows the sibling send/look gates.

## CUT — do not open as next CU

| What | Why cut |
|---|---|
| Workship → SOKUDAN → Offers → MENTA → ストアカ | **Wave B register CU cut.** Not next after Freelancer. |
| PR#50 Google serial (Workship → SOKUDAN → Offers) | Same cut. Prep packs may exist; do not start register CU. |
| Skill Shift · ITプロパートナーズ · Anycrew · 複業クラウド · CrowdLinks · AI CrowdWorks | Register CU cut. `needs_check` still not a GO. |
| PeoplePerHour Basic / TopAccess | `blocked_paid_plan`. Do not subscribe. |
| Workana · YOUTRUST | `needs_check`. No register CU. |
| note · Braintrust · 99freelas · Gulp · カイコク | Wave D-early inventory. Behind. No register CU. |
| Twago · Xing Projects | `dead`. skip_log. |
| Shufti / Wave C–D register | Cut with register-winddown. |
| Wave A `blocked_skip` | Fiverr Press&Hold · Lancers captcha · CrowdWorks 403 · Upwork Google access block · LinkedIn reCAPTCHA · TimeTicket DOB missing. No retry. |

`thin`: **0** in #58/#59/#61/#62. Do not invent a thin skip. Gate labels in [MERGE.md](MERGE.md) are **not** a license to register.

## JOBS rules

1. One browser profile. MAIN Google picker only. Do not open Gmail in that profile.
2. Coconala: existing service draft only. No second identity. No new 出品 from scratch if a draft already exists — finish that draft to **publish-ready**.
3. Gumroad: look only. Unpublished. No Enable / Publish / payout setup.
4. Proposals: official UI, one listing, HANDS. No email / phone / messenger in pre-award paste. No leftover-bid spray, Sponsored / Highlight / Sealed default, contests, or Preferred exam.
5. KYC / liveness / Stripe / 口座 / Persona / Freelancer Verify Identity = **STOP**. Desk name + screen type to morning operator. No upload.
6. Gmail OTP = parent (CU does not open Gmail). SMS = wait on user chat; if away, park the live JOBS desk.
7. Press & Hold: `holdDurationMs` 1800, one retry 2500.
8. Live form wins. Do not invent a third bio, 円, %, traffic, or GMV.
9. Do not buy paid plans.

## This sheet does not

- Copy or merge sibling PR bodies
- Create marketplace accounts or complete new signup
- Store secrets, OTP, phone, bank, or ID
- Click Coconala 公開 / Gumroad Publish from this PR
- Send Contra / Freelancer proposals from this PR
- Start Wave B/C/D **register** CU
- Retry Wave A `blocked_skip` desks
- Open PPH checkout

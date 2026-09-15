> **DRAFT_ONLY. No signup from this file.** Pointers only. Do not copy secrets out of sibling packs (they should contain none). Do not paste CSRF / OTP / passwords into this folder.

# Prior-pack pointer merge

This serial **does not duplicate** JA bio 200/800, full field maps, or STOP-KYC prose from earlier PRs. CU paste uses the **thick** file as source of truth. Live form still wins.

GitHub blob links below are on the **draft branch of that PR**, not `master`. Packs are unmerged as of this writing. If a blob 404s, open the PR files tab.

## Desk → paste source of truth

| This-folder card | INDEX | Thick paste (use this) | Thinner / sample (do not prefer) | Activity gate |
|---|---|---|---|---|
| [01-workship.md](01-workship.md) | CU-11 | [PR#30 `01-workship.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-waveb-cu-handoff-batch2-87d0/earn-waveb-cu-handoff-batch2-20260916/01-workship.md) | [PR#3 `02-workship.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/jp-earn-register-packs-8df7/earn-register-packs-jp-20260916/02-workship.md) | [PR#12 `records/02-workship.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-activity-gate-waveb-jp-fced/earn-activity-gate-waveB-20260916/records/02-workship.md) |
| [02-sokudan.md](02-sokudan.md) | CU-13 | [PR#33 `02-sokudan.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-skillshift-sokudan-menta-deep-0734/earn-skillshift-sokudan-menta-deep-20260916/02-sokudan.md) | [PR#21 `01-sokudan.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-waveb-alive-handoff-a6eb/earn-waveb-alive-handoff-sample-20260916/01-sokudan.md) · [PR#3 `01-sokudan.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/jp-earn-register-packs-8df7/earn-register-packs-jp-20260916/01-sokudan.md) | [PR#12 `records/01-sokudan.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-activity-gate-waveb-jp-fced/earn-activity-gate-waveB-20260916/records/01-sokudan.md) |
| [03-offers.md](03-offers.md) | CU-25 | [PR#30 `04-offers.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-waveb-cu-handoff-batch2-87d0/earn-waveb-cu-handoff-batch2-20260916/04-offers.md) | [PR#34 `03-offers.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-week2-rest-cu-paste-e6ce/earn-week2-rest-cu-paste-20260916/03-offers.md) | [PR#12 `records/12-offers.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-activity-gate-waveb-jp-fced/earn-activity-gate-waveB-20260916/records/12-offers.md) |

INDEX inventory numbering (PR#3 file `01-sokudan` vs CU-13) is **stock order**, not this serial.

## Shared policy siblings (do not copy bodies here)

| Topic | Pointer |
|---|---|
| Thick CU serial runbook (Wave A remaining → Wave B **passes only**) | [PR#7 `RUNBOOK.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-cu-serial-runbook-2e17/earn-cu-runbook-20260916/RUNBOOK.md) §13 |
| CU number map | [PR#8 `INDEX.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-register-pack-index-45e2/earn-register-pack-index-20260916/INDEX.md) |
| JP Wave B gate method | [PR#12 `ACTIVITY-GATE.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-activity-gate-waveb-jp-fced/earn-activity-gate-waveB-20260916/ACTIVITY-GATE.md) |
| Morning KYC 1-pager (Wave A bias) | [PR#4](https://github.com/rimone0511/autopilot-log/pull/4) `earn-kyc-morning-checklist-20260916/` |
| Morning slip refresh (Wave A `draft_saved` / `blocked_skip` only — **not** these 3 desks) | [PR#43](https://github.com/rimone0511/autopilot-log/pull/43) |
| Workship / Offers STOP-KYC prose | [PR#30 `STOP-KYC.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-waveb-cu-handoff-batch2-87d0/earn-waveb-cu-handoff-batch2-20260916/STOP-KYC.md) |
| SOKUDAN Google / OTP / hold protocol | [PR#33 `00-google-otp-hold.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-skillshift-sokudan-menta-deep-0734/earn-skillshift-sokudan-menta-deep-20260916/00-google-otp-hold.md) |
| SOKUDAN STOP-KYC | [PR#33 `STOP-KYC.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-skillshift-sokudan-menta-deep-0734/earn-skillshift-sokudan-menta-deep-20260916/STOP-KYC.md) |
| QUEUE | [PR#1](https://github.com/rimone0511/autopilot-log/pull/1) `earn-register-expand-20260916/QUEUE.md` |
| REGISTER-BOARD | [PR#24](https://github.com/rimone0511/autopilot-log/pull/24) |
| Master index | [PR#14](https://github.com/rimone0511/autopilot-log/pull/14) · [PR#35](https://github.com/rimone0511/autopilot-log/pull/35) |

## What “merge” means

- **Do** follow this folder’s serial: Workship → SOKUDAN → Offers.
- **Do** paste bios / field values from the thick file for that desk.
- **Do not** copy passwords, OTP, phone digits, CSRF hidden fields, or cookies from any HTML GET into git.
- **Do not** treat PR#21 sample order (SOKUDAN first) or PR#30 five-desk pass-first order (Workship → ITプロパートナーズ → Offers) as **this** serial.
- **Do not** skip Workship because a sample pack started at SOKUDAN.

## Conflict rule

If two packs disagree: **this-run public GET** ([METHOD.md](METHOD.md)) + **live form** > thick pack > thin pack > QUEUE one-liner.

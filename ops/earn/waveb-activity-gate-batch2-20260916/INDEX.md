# INDEX — Wave B activity-gate batch 2

Observed: **2026-09-16 JST** (public GET).  
State: **DRAFT_ONLY** / **prep**. Not signed up. Not a CU serial start.

Desk ids **B10–B12** are this folder only. QUEUE ids stay B5 / B6 / B7. CU serial stays CU-15 / CU-16 / CU-17.

## Pack map

| Pack | Path | Desk(s) | CU vs prep | Status | QUEUE | CU | Gate | Sibling (body not copied) |
|---|---|---|---|---|---|---|---|---|
| This batch README | [`README.md`](README.md) | B10–B12 | prep | ready · draft | — | — | — | — |
| This STATUS | [`STATUS.md`](STATUS.md) | B10–B12 | prep | ready · draft | — | — | see STATUS | — |
| This METHOD | [`METHOD.md`](METHOD.md) | B10–B12 | prep | ready · draft | — | — | — | — |
| B10 record | [`records/b10-anycrew.md`](records/b10-anycrew.md) | Anycrew | prep | ready · draft | B5 | CU-15 | `needs_check` | [#12](https://github.com/rimone0511/autopilot-log/pull/12) [#21](https://github.com/rimone0511/autopilot-log/pull/21) [#33](https://github.com/rimone0511/autopilot-log/pull/33) [#39](https://github.com/rimone0511/autopilot-log/pull/39) |
| B11 record | [`records/b11-menta.md`](records/b11-menta.md) | MENTA | prep | ready · draft | B6 | CU-16 | `pass` | [#12](https://github.com/rimone0511/autopilot-log/pull/12) [#21](https://github.com/rimone0511/autopilot-log/pull/21) [#33](https://github.com/rimone0511/autopilot-log/pull/33) |
| B12 record | [`records/b12-street-academy.md`](records/b12-street-academy.md) | ストアカ | prep | ready · draft | B7 | CU-17 | `pass` | [#12](https://github.com/rimone0511/autopilot-log/pull/12) [#21](https://github.com/rimone0511/autopilot-log/pull/21) [#33](https://github.com/rimone0511/autopilot-log/pull/33) [#39](https://github.com/rimone0511/autopilot-log/pull/39) |
| QUEUE (order) | `earn-register-expand-20260916/QUEUE.md` | Wave A–D | CU | ready · sibling | — | — | — | [#1](https://github.com/rimone0511/autopilot-log/pull/1) |
| CU serial INDEX | `earn-register-pack-index-20260916/INDEX.md` | CU-01–CU-28 | prep | ready · sibling | — | — | — | [#8](https://github.com/rimone0511/autopilot-log/pull/8) |
| JP Wave B gate (first) | `earn-activity-gate-waveB-20260916/` | JP Wave B 13 desks | prep | ready · sibling | B1–B7, B13–B17 | — | Anycrew/MENTA/ストアカ were `needs_check` | [#12](https://github.com/rimone0511/autopilot-log/pull/12) |
| Wave A STATUS snapshot | `earn-register-status-snapshot-20260916-0519/STATUS.md` | Wave A | prep | ready · sibling | A1–A10 | CU-01–CU-10 | live box is Wave A | [#49](https://github.com/rimone0511/autopilot-log/pull/49) |

`ready` means files exist. It does **not** mean an account exists.

## CU vs prep

This folder is **prep**. Do not open Anycrew / MENTA / ストアカ in a CU browser because this INDEX exists.

Wave B CU still waits on Wave A (`pending` / `blocked_skip` per PR#49). When Wave B starts, use CU-15/16/17 paste packs in sibling PRs — not these records as field maps.

## Status symbols (this INDEX)

| Symbol | Meaning |
|---|---|
| `ready · draft` | Files in this PR. PR is draft |
| `ready · sibling` | Files live on a sibling branch. Body not copied here |
| `needs_check` | Gate: catalog date unread. Human one-screen before CU |
| `pass` | Gate: public freshness clue. Draft-only later. No publish |

## This INDEX does not

- Rewrite QUEUE B10–B12 (those rows are Malt / Workana / Freelancermap)
- Copy paste-pack bios or field maps
- Mark any desk `done-draft` or `in_progress`

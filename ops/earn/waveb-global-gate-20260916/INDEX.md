# INDEX — Wave B GLOBAL activity-gate slice

Observed: **2026-09-16 JST** (public GET. **No marketplace login.**)  
Folder: `ops/earn/waveb-global-gate-20260916/`  
State: **`DRAFT_ONLY`**. Pack `ready` on a sibling PR means a paste file exists. It does **not** mean registered.

Forbidden: secrets, live signup, paid subscribe, invented traffic / GMV / fee amounts.

## ID crosswalk (read first)

This folder’s B14 / B16 / B18 are **local labels**. Canonical WAVE letters stay in [PR#1](https://github.com/rimone0511/autopilot-log/pull/1) `QUEUE.md`. Canonical CU numbers stay in [PR#8](https://github.com/rimone0511/autopilot-log/pull/8).

| This folder | Desk | QUEUE | INDEX CU | Do not confuse with |
|---|---|---|---|---|
| B14 | PeoplePerHour | **B9** | **CU-20** | QUEUE **B14 = Offers** |
| B16 | Workana | **B11** | **CU-22** | QUEUE **B16 = Skill Shift** |
| B18 | YOUTRUST | **B13** | **CU-24** | (no QUEUE B18) |

## Gate files (this PR)

| This folder | Desk | Record | CU vs prep | Status this run | Sibling pack (body not copied) |
|---|---|---|---|---|---|
| B14 | PeoplePerHour | [records/b14-peopleperhour.md](records/b14-peopleperhour.md) | prep — pack exists elsewhere; **not registered** | marketplace `pass` · seller **`blocked_paid_plan`** | [#2](https://github.com/rimone0511/autopilot-log/pull/2) `02-peopleperhour-hourlies-draft.md` · [#29](https://github.com/rimone0511/autopilot-log/pull/29) `02-peopleperhour.md` |
| B16 | Workana | [records/b16-workana.md](records/b16-workana.md) | prep — pack exists elsewhere; **not registered** | **`needs_check`** (Cloudflare 403 on HTML) | [#2](https://github.com/rimone0511/autopilot-log/pull/2) `04-workana-draft.md` · [#29](https://github.com/rimone0511/autopilot-log/pull/29) `04-workana.md` |
| B18 | YOUTRUST | [records/b18-youtrust.md](records/b18-youtrust.md) | prep — pack exists elsewhere; **not registered** | **`needs_check`** (job cards unread) | [#12](https://github.com/rimone0511/autopilot-log/pull/12) JP gate record · [#30](https://github.com/rimone0511/autopilot-log/pull/30) `05-youtrust.md` |

`prep` = gate + sibling paste only. No CU session from this PR.

## Also in this folder

| File | Role |
|---|---|
| [STATUS.md](STATUS.md) | One-page live box for these three desks |
| [ACTIVITY-GATE.md](ACTIVITY-GATE.md) | Evidence short notes |
| [METHOD.md](METHOD.md) | HTTP GET log |
| [README.md](README.md) | Scope and labels |

## Out of this INDEX

| QUEUE | Desk | Why omitted |
|---|---|---|
| B8 / CU-19 | Guru.com | Sibling GLOBAL pack/gate; not in this GO |
| B10 / CU-21 | Malt.com | Sibling GLOBAL pack/gate; not in this GO |
| B12 / CU-23 | Freelancermap | Sibling GLOBAL pack/gate; not in this GO |
| B14 | Offers | JP Wave B (PR#12 `pass`). Different desk from this-folder B14 |
| B16 | Skill Shift | JP Wave B (PR#12 `pass`). Different desk from this-folder B16 |

## Next (human, not this PR)

1. Do **not** subscribe to PeoplePerHour Basic / TopAccess. If the next click is pay, keep `blocked_paid_plan` and close.
2. Workana `/en/jobs`: human browser after Cloudflare. Unreadable here ≠ dead.
3. YOUTRUST `/recruitment_posts`: human looks at one job card date before treating activity as `pass`.
4. Wave A `pending` / `blocked_skip` still blocks Wave B CU serial ([PR#49](https://github.com/rimone0511/autopilot-log/pull/49) STATUS snapshot). This gate does not jump the queue.

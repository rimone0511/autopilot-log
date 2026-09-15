# Wave B activity-gate — batch 1 (still `needs_check`)

**DRAFT_ONLY.** Public GET notes. No signup. No secrets. No paid plans. No invented fees / traffic / GMV.

| | |
|---|---|
| Folder | `ops/earn/waveb-activity-gate-batch1-20260916/` |
| Observed | **2026-09-16 JST** (HTTP from this environment ~2026-09-15 20:1x–20:3x UTC) |
| Method | Logged-out GET of official public URLs. No form POST. No OAuth. No cookies saved. |
| Prior pack | [PR #12](https://github.com/rimone0511/autopilot-log/pull/12) left these JP Wave B desks `needs_check` because listing dates were unread. This batch re-checks **only** those three IDs as numbered here. |

This folder is an **activity-gate record**, not a paste pack and not a register run.

## Desks in this batch

User numbering for this folder (not the original QUEUE B5=Anycrew):

| ID | Desk | File | Gate (this GET) |
|---|---|---|---|
| B03 | 複業クラウド（旧 Another Works） | [b03-fukugyo-cloud.md](b03-fukugyo-cloud.md) | **needs_check** |
| B04 | クラウドリンクス (CrowdLinks) | [b04-crowdlinks.md](b04-crowdlinks.md) | **needs_check** |
| B05 | AI CrowdWorks（AIクラウドワークス） | [b05-ai-crowdworks.md](b05-ai-crowdworks.md) | **needs_check** |

Summary table and HTTP log: [STATUS.md](STATUS.md).

Sibling JP Wave B gate (13 desks, including Anycrew / MENTA / ストアカ): `earn-activity-gate-waveB-20260916/` in PR #12. This batch does **not** copy that folder and does **not** re-gate those other desks.

## Labels (this folder)

| Label | Meaning here |
|---|---|
| `alive` | Public job/cards (or equivalent dated listing) show **recent** activity we actually read |
| `needs_check` | Site is up, but public listing dates are missing, login-walled, SPA-unrendered, or the dates we did read are **not recent / look ended** |
| `thin` | Public work does not fit this earn line (not used in this batch) |
| `dead` | Closed / gone (not used in this batch) |

Unread SPA / WAF / login wall is **not** `dead` and **not** `thin`.

Marketing totals (登録者○万人, 事前登録 10,000名, sitemap URL counts) are **not** activity proof.

## What this GET did not do

- Browser signup, MAIN Google login, OAuth completion
- KYC / bank / My Number
- Paid membership, priority listing, skip-review SKUs
- Apply / 興味がある / 話を聞きたい / profile publish
- Saving secrets, signed-URL keys, or session cookies

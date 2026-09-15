> No signup. No paid plans. Marketing “○万人” is not a gate count.

# Verify notes — JP Wave B activity-gate

Mirror-bake: 2026-09-16. Sibling observation: 2026-09-16 JST.

## Sibling verdict (unchanged unless this bake contradicts)

**pass (5):** SOKUDAN, Workship, Skill Shift (official domain), ITプロパートナーズ, Offers (Jobs 業務委託).  
**needs_check (8):** 複業クラウド, CrowdLinks, Anycrew, MENTA, ストアカ, AI CrowdWorks, YOUTRUST, Shufti.  
**fail / SKIP thin / blocked_paid_plan:** 0.

## Re-GET this bake

| Desk | Result | Gate impact |
|---|---|---|
| SOKUDAN https://sokudan.work/ | **200** | pass **holds** |
| Workship `/portal/search` | **200** 業務委託案件 | pass **holds** |
| Skill Shift https://www.skill-shift.com/ | **200** | pass **holds** (still not `skillshift.jp`) |
| ITプロパートナーズ | **200** | pass **holds** |
| Offers `/jobs/engineer/side-job` | **200** | pass **holds** as “not 転職-only” |
| Anycrew app | **200** shell title | stays **needs_check** (cards unread) |
| YOUTRUST | **200** but **`/lp`** | stays **needs_check** (jobs API was 401 in sibling) |
| Shufti | **200** → app.shufti.jp | stays **needs_check** |
| MENTA | **202** | stays **needs_check** (WAF). Not fail |
| ストアカ `/teach` | **405** | stays **needs_check** (sibling saw a lecturer form; this bake did not) |
| AI CrowdWorks email register | **200** | stays **needs_check** (register shell ≠ public job cards) |

複業クラウド / CrowdLinks: not re-opened; remain **needs_check**.

## LIVE_DEVIN_NEEDED

Devin is **not** authorized to register these desks from this PR. After a human GO, CU only on **pass** desks, mutex 1, DRAFT_ONLY, stop KYC.

For the eight `needs_check` desks: Devin (or a non-WAF browser) must **read a dated public card or catalog row** before anyone treats the desk as pass. Unread SPA is not `SKIP thin`.

Onsite / 準委任 flags on SOKUDAN/Workship stay in the sibling evidence — do not flatten to “all remote.”

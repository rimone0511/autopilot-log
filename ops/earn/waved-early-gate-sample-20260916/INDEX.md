# INDEX — Wave D-early activity-gate sample

Stamp: **2026-09-16 JST**  
Folder: `ops/earn/waved-early-gate-sample-20260916/`  
State: **DRAFT_ONLY** / `gate` ≠ registered

Public pages only. Login: **no**. Signup: **no**. Paid plan: **not opened to purchase**. Traffic/GMV: **not invented**.

Desk IDs are Wave D-early **D02 / D03 / D04 / D07 / D08 / D09 / D10**. QUEUE Wave D’s D1–D8 is a different list (PR#1). note / Braintrust remain Wave **C** in the parent QUEUE.

## Labels

| Label | Use here |
|---|---|
| `alive` | Public page shows the desk is live **and** a freshness clue (dated card, `publishAt`, official dated blog). Keep behind A/B. Draft only later. |
| `dead` | Closed URL, 404 on the dedicated desk, or the brand is a different product with no public freelance board. Evidence required. |
| `thin` | Public listings missing **and** the desk does not match the seller line. Evidence required. **0 this sample.** |
| `needs_check` | Signup or LP is open, but listing dates are missing / unread. Do not guess `alive` or SKIP. |

`unknown` on a required freshness field stays `needs_check`. Do not promote.

## Desks (this sample)

| # | Desk | Note | Opened URL (this GET) | signup_open | Gate | Next |
|---|---|---|---|---|---|---|
| D02 | カイコク | [notes/d02-kaikoku.md](notes/d02-kaikoku.md) | https://kaikoku.blam.co.jp/ | yes (`/user/register/before` 200) | **needs_check** | Do not register. Do not SKIP thin. Human reads a dated listing if one appears. |
| D03 | note | [notes/d03-note.md](notes/d03-note.md) | https://note.com/ | yes (`/signup` 200) | **alive** | Parent QUEUE = Wave C. Paid note / membership **draft** only. Do not publish. |
| D04 | Braintrust | [notes/d04-braintrust.md](notes/d04-braintrust.md) | https://www.usebraintrust.com/for-talent | yes (Create Your Profile copy; form not submitted) | **alive** | Parent QUEUE = Wave C. Talent draft later. **ID-verified / Certified → STOP.** |
| D07 | Twago | [notes/d07-twago.md](notes/d07-twago.md) | https://www.twago.com/ → https://www.talent-pool.com/ | no public freelancer signup | **dead** | skip_log. Do not enter the enterprise Talent Pool console. |
| D08 | 99freelas | [notes/d08-99freelas.md](notes/d08-99freelas.md) | https://www.99freelas.com.br/projects | yes (home `Cadastre-se`; `/register/freelancer` CF 403 this IP) | **alive** | Behind A/B. Profile draft later. Premium not purchased. Do not bid. |
| D09 | Gulp | [notes/d09-gulp.md](notes/d09-gulp.md) | https://www.gulp.de/freelancing/projekte | yes (`/registrieren` Freelancer) | **alive** | Behind A/B. Skip on-site CH cards. Membership 120/180 Euro netto **not bought**. |
| D10 | Xing Projects | [notes/d10-xing-projects.md](notes/d10-xing-projects.md) | https://www.xing.com/projects | no (dedicated URL 404) | **dead** | skip_log. Do not fall over to XING Jobs. |

Not in this INDEX: D01 Shufti, D05 Twine, D06 Fastwork.

## Counts (see STATUS.md)

keep_queue (`alive`) **4** · skip_log (`dead`) **2** · `needs_check` **1** · `thin` **0** · total **7**

## This PR does not

- Create accounts, complete OAuth, or send MAIN Google
- Upload KYC / bank / tax IDs
- Publish notes, profiles, or listings
- Bid / apply / 応募
- Copy sibling paste-pack bodies
- Invent listing counts, GMV, or “○万人”

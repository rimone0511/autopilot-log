# INDEX — Wave D-early activity-gate sample

Stamp: **2026-09-16 JST**  
Folder: `earn-waved-early-gates-20260916/`  
State: **DRAFT_ONLY** / `gate` ≠ registered

Public pages only. Login: **no**. Signup: **no**. Paid plan: **not opened to purchase**. Traffic/GMV: **not invented**.

Desk IDs are Wave D-early **D02 / D03 / D04 / D07**. QUEUE Wave D’s D1–D8 is a different list (PR#1). note / Braintrust remain Wave **C** in the parent QUEUE.

## Labels

| Label | Use here |
|---|---|
| `alive` | Public page shows the desk is live **and** a freshness clue (dated card, `publishAt`, official dated blog). Keep behind A/B. Draft only later. |
| `dead` | Closed URL, 404 on the dedicated desk, or the brand is a different product with no public freelance board. Evidence required. |
| `thin` | Public listings missing **and** the desk does not match the seller line. Evidence required. **0 this sample.** |
| `needs_check` | Signup or LP is open, but listing dates are missing / unread. Do not guess `alive` or SKIP. |

`unknown` on a required freshness field stays `needs_check`. Do not promote.

## CU priority

| Value | Meaning in this pack |
|---|---|
| `early` | KEEP for a later profile/draft CU **after** Wave A/B. This PR does not start CU. Not interview-agent. |
| `late` | Do not CU yet. Human must read a dated public listing (or equivalent) first. |
| `skip` | No CU. Desk is `dead` (or would be thin). Do not enter a different product. |

## Desks (this sample)

| # | Desk | Opened URL (this GET) | Gate | CU | One-line reason |
|---|---|---|---|---|---|
| D02 | カイコク | https://kaikoku.blam.co.jp/ | **needs_check** | **late** | 無料登録導線は生きているが、公開「案件事例」に掲載日がない |
| D03 | note | https://note.com/ | **alive** | **early** | トップ HTML の `publishAt` が 2026-09-14 / 15。親キューは Wave C。下書きのみ |
| D04 | Braintrust | https://www.usebraintrust.com/for-talent | **alive** | **early** | Talent「$0 fees」。`/jobs` 役割カード。ブログ Sep 14, 2026。ID-verified は STOP |
| D07 | Twago | https://www.twago.com/ → https://www.talent-pool.com/ | **dead** | **skip** | `twago.com` は企業向け Talent Pool。公開フリーランス仕事ボードなし |

Notes: [d02](notes/d02-kaikoku.md) · [d03](notes/d03-note.md) · [d04](notes/d04-braintrust.md) · [d07](notes/d07-twago.md)

Not in this INDEX: D01 Shufti, D05 Twine, D06 Fastwork, D08 99freelas, D09 Gulp, D10 Xing Projects.  
D05 / D06 skipped because already `alive` in PR#22 / PR#13 — not re-opened.

## Counts (see STATUS.md)

keep_queue (`alive`) **2** · skip_log (`dead`) **1** · `needs_check` **1** · `thin` **0** · total **4**

## This PR does not

- Create accounts, complete OAuth, or send MAIN Google
- Upload KYC / bank / tax IDs
- Publish notes, profiles, or listings
- Bid / apply / 応募
- Copy sibling paste-pack bodies
- Invent listing counts, GMV, or “○万人”
- Re-gate D05 Twine / D06 Fastwork

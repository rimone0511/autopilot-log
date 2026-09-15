# TODAY apply queue — 2026-09-16 JST (JOBS / EARN MONEY)

Pack date: **2026-09-16 JST** (Wednesday)  
Folder: `earn-jobs-apply-queue-today-20260916/`  
Who: **祐太 (parent operator)** + agent as paste helper only  
Auth: **MAIN Google only**. No second Coconala / Gumroad / Contra / LinkedIn / Freelancer.  
State: **DRAFT_ONLY.** This folder is a ranked work list, not a GO.

**JOBS PHASE** means: spend the next human+agent block on desks that already have a parked draft, toward a **real paid thread**. Preparing a paste is not sending it. Ranking is **proximity to a live inquiry / apply / unpublished listing** — not a revenue forecast.

Use only:

| In this queue | CU hint used here | Why it is in TODAY |
|---|---|---|
| ココナラ Coconala (A1) | `draft_saved` (QUEUE `done-draft`) | Seller draft exists. Inbound 見積もり is the nearest JP paid path. |
| Gumroad **SKU-0** (A+) | `draft_saved` (QUEUE `done-draft`) | Unpublished starter intake. Listing polish exists. Publish is **not** today’s money click. |
| Contra Independent (A8) | `draft_saved` **live** 2026-09-16 | Name / bio saved. Job-feed letters exist. Apply still `no` until a human GO. |
| LinkedIn **Services / profile** (A6 surface) | JOBS-set `draft_saved` (see STATUS) | Existing recovered personal profile. Save may publish. Captcha may still block. |
| Freelancer.com bids (A10) | **when account ready** | Bid letters exist. Wave A still `pending`. No account → **0 minutes**. |

This pack does **not** rewrite the 7-day calendar ([#76](https://github.com/rimone0511/autopilot-log/pull/76)). That calendar is the week. This folder is **today’s ranked block**.

---

## How to read this folder

| File | Role |
|---|---|
| [RANKED.md](RANKED.md) | Rank 1–5: where the next hour goes. What the agent may do vs what 祐太 clicks. |
| [GO-GATES.md](GO-GATES.md) | Fail-closed send/publish switches. Missing file = every flag `false`. |
| [POINTERS.md](POINTERS.md) | Sibling paste paths. Bodies **not** copied. |
| [PARK.md](PARK.md) | Desks that do **not** get time today (blocked_skip / pending / missing pack). |
| [STATUS.md](STATUS.md) | Inventory used to rank. No invented URLs, GMV, or “will sell”. |

A missing, unread, or half-filled [GO-GATES.md](GO-GATES.md) means **do not send and do not publish**.

---

## Hard rules

1. **DRAFT_ONLY until a human GO outside this folder.** Rank order is not permission.
2. **No invented revenue.** No GMV, conversion %, “this will sell ¥…”, guaranteed hourly, or made-up inquiry counts.
3. **No secrets in git.** No email, OTP, phone, bank, tax IDs, My Number, ID images, live prices, live listing IDs, live `gumroad.com/l/...`, live `contra.com/@…`, live `linkedin.com/in/…`.
4. **MAIN Google only.** Do not create a second identity on any desk.
5. **One live thread at a time.** Skip if `{{ONE_SPECIFIC_DETAIL}}` will not fill in about a minute. Do not spray.
6. **Agent never clicks send/publish/Save-if-viewable/Bid/Apply.** There is no submit script.
7. **KYC is not today’s earn action** unless a live payout / NDA screen already appeared. Documents on the **site** only.
8. **Paid boosts stay off:** Contra Pro, LinkedIn Premium / InMail, Gumroad Discover, Coconala ads, Freelancer leftover-bid / Sponsored / Highlight / Sealed, wallet top-up.

---

## DRAFT vs human GO

| Label | Operator may | Agent may | Example UI |
|---|---|---|---|
| **DRAFT** | Look, unpublished save, paste into a local editor or a field that will be **cleared** | Rank, point, help rewrite a local paste | Coconala 下書き保存, Gumroad unpublished, Contra saved bio, LinkedIn fields not Saved-as-viewable, Freelancer letter in a text file |
| **human GO** | Click the live control **after** flipping the matching row in GO-GATES | Never | 公開する / 見積もり送信 / Publish / Enable / Apply / Save-if-viewable / Send / Bid |

If the live UI has **no unpublished control** (`no_draft_path`), stop. Do not click Save/公開 “to see how it looks”.

---

## 日本語（運用だけ）

今日の1枠は **下書き済みの机** だけ。順番は「いま実在の相談・応募・未公開出品に近いか」。売上見込は書かない。送信・公開・Save-で見える化・Bid は人が GO-GATES を開いてから。秘密は git に置かない。Freelancer はアカウントが無いなら入札に時間を使わない。

---

## This PR does not

- Merge sibling packs or mark them ready-for-review
- Copy paste bodies from sibling PRs
- Register new marketplaces
- Publish, apply, invoice, bid, or send
- Invent listing titles, prices, profile URLs, inquiry counts, or GMV
- Retry Fiverr hold / Lancers captcha / CrowdWorks 403 / Upwork Google block / LinkedIn image captcha
- Change Python posting-gate tests

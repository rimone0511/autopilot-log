> **DRAFT_ONLY. DO NOT SEND.**  
> Operator card. Do **not** paste this file into a listing, proposal, or estimate.  
> Invent no metrics. If a claim is not in the “allowed” column, it is forbidden.

# FACTS — allowed / forbidden

Ticket: `EARN-SHOWCASE-PROPOSAL-PACK-20260916`  
Clock: 2026-09-16 (showcase sample clock)  
Seller in public paste: `{{DISPLAY_NAME}}` (recommended 石田祐太 / Yuta Ishida), Japan, async `{{TIMEZONE}}`.  
Demos: **synthetic, self-made, no live customer, no PII.**

## Cite only these heads

| Pack | PR | Head | QA |
|---|---|---|---|
| P1 inquiry intake | https://github.com/rimone0511/autopilot-log/pull/115 | `541bb18` | #121 PASS |
| P2 weekly CSV + provenance | https://github.com/rimone0511/autopilot-log/pull/117 and https://github.com/rimone0511/autopilot-log/pull/120 | `14b818c` | #121 PASS |
| P3 fail-stop | https://github.com/rimone0511/autopilot-log/pull/116 | `0a822e0` | #121 PASS |
| QA report | https://github.com/rimone0511/autopilot-log/pull/121 `ops/earn/earn-showcase-swe2-qa-20260916/QA-REPORT.md` | — | FACTS-limited **proposal prep** OK |

SOL first looked at older heads and marked CONDITIONAL/FAIL. Fixes landed; #121 re-ran the **fixed** heads.  
A second SOL human review is **optional**. Do **not** claim “SOL cleared twice.”

## Allowed claims (buyer-safe)

Check every paste against this list. Phrasing may be shorter; meaning must stay inside the cell.

| # | Allowed | Where it comes from |
|---|---|---|
| A1 | This is a **human-stop** intake: read inquiry rows → validate → dedupe / collide → a **hold-for-human** list. Ready rows are still not sent. | P1 |
| A2 | Duplicate `inquiry_id` in one batch → **every** collided row is `needs_human` (`DUPLICATE_INQUIRY_ID`). | P1 / #121 |
| A3 | Same bundled fixture as CSV or JSON → same ready / hold IDs and reasons. | P1 / #121 |
| A4 | `python3 run.py --check` regenerates in temp, matches committed `output/`, leaves git clean. `--check` refuses non-bundled input. | P1 / #121 |
| A5 | Weekly CSV can point a summary line back to the **actual** input file: source label, `#Ln`, SHA-256 of that file. | P2 / #120 / #121 |
| A6 | `--timezone` is used for week bounds and is recorded (unknown zone exits; missing `--input` does not silently fall back to the bundled fixture). | P2 / #120 / #121 |
| A7 | On the P3 sample log: timeout ≠ approve. A hold that times out is **not** written to the ledger. | P3 / #121 |
| A8 | Actorless approve, missing event ID, missing time, or a **reused** event ID → non-writing (`needs_human`). First-seen event ID may write once (auditable). | P3 / #121 |
| A9 | n8n JSON in P1/P2/P3 is `active=false`, no send / webhook nodes, no credential objects, synthetic fixtures. Verified runner is local Python. | #121 common |
| A10 | n8n is an **implementation option**. The product is the intake → hold list, not a tool religion. | SYNTHESIS + P1 README |
| A11 | Demos are autonomous / synthetic. Bundled counts (20 rows, 14 fulfilled, 9,600 yen, 12 events, …) are **that fixture’s behavior**, not KPIs. Do not put those numbers in buyer paste. | each FACTS card + #121 |
| A12 | QA #121: FACTS-limited proposal **prep** may start. Publish / apply / send / register / merge / Activate stay blocked until a **separate** GO. | #121 |

## Forbidden claims (hard stop)

If any box would be true, rewrite or skip. Do not send.

| # | Forbidden | Why |
|---|---|---|
| F1 | Revenue, GMV, “sold to N clients”, conversion rate | no sales facts |
| F2 | Time saved, “we saved X hours”, faster replies as a measured result | not measured |
| F3 | Accuracy %, 99%, precision/recall, “AI never mis-labels” | not measured; P1 is rules + hold, not a scored model |
| F4 | “n8n in production”, “n8n 導入済み”, authenticated Sheets/Gmail/Slack, live webhooks | n8n inactive; no send nodes |
| F5 | “SOL cleared twice”, “two independent SOL PASS”, “audit certified” | first SOL was CONDITIONAL/FAIL; #121 is SWE-2 QA; second SOL optional |
| F6 | “We prevented double registration for a real studio” / production fail-stop | P3 is a synthetic log |
| F7 | Fake reviews, star ratings, testimonials | none exist |
| F8 | Real client / company / shop names presented as customers | use `依頼者A` / `Client A` labeled **fictional** only |
| F9 | Partner / Expert / official badge for n8n, Zapier, Make, OpenAI, etc. | not true |
| F10 | Timeout auto-approves, auto-sends, or auto-publishes | P3 is the opposite |
| F11 | Autopilot Log YouTube/TikTok posting is this offer | unrelated |
| F12 | Invented screenshots, loom URLs, or “see attached case PDF” not in [ASSETS-POINTER.md](ASSETS-POINTER.md) | this pack has **no** image assets |
| F13 | Live prices, fee %, Connects cost, Contra Pro as required | placeholders / official help at click-time |
| F14 | “This PR applied / published / merged / Activated n8n” | DRAFT_ONLY |

## Buyer one-liners (safe)

Use these; do not decorate with numbers.

- JP: 人が止める前提で、問い合わせを検査し、重複は要確認一覧へ倒します。自動送信しません。
- JP: 同じ受付番号は、当たった行をすべて人へ戻します。
- JP: 週報が要るときだけ、要約から入力行（出典・行番号・ハッシュ）へ戻れます。
- JP: 待ち時間が切れても承認にはしません。欠けた記録や使い回しは書きません。
- EN: Human-held intake: validate, dedupe, hold-for-human. No send switch on the machine.
- EN: Duplicate intake IDs hold **every** collided row. Timeout is not approve.
- EN: n8n is optional and inactive in the public samples. Python is the verified runner.

## Checklist before a later paste

- [ ] Every sentence maps to A1–A12 or is a question / process / exclusion
- [ ] No F1–F14 phrase, even as “soft” marketing
- [ ] No bundled-fixture counts in the fenced buyer text
- [ ] Showcase links, if used, are only the five PRs in [ASSETS-POINTER.md](ASSETS-POINTER.md) (plus yutalab.dev / repo root)
- [ ] `{{ONE_SPECIFIC_DETAIL}}`, `{{TARGET_URL}}`, `{{PRICE}}` still empty in git
- [ ] Header on the file I am using still says DRAFT_ONLY / DO NOT SEND

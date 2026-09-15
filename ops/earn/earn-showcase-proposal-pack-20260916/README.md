> **DRAFT_ONLY. DO NOT SEND.**  
> Ticket `EARN-SHOWCASE-PROPOSAL-PACK-20260916`.  
> Unsent drafts for 祐太 to GO later. This pack does **not** publish, apply, send, register, merge, Activate, or spend.

# Showcase proposal pack — 2026-09-16

**Next action (operator):** read [FACTS.md](FACTS.md) → pick **one** lane → fill [SEND-CHECKLIST.md](SEND-CHECKLIST.md) **locally** → stop.  
**This PR is not a send GO.**

Wedge (SYNTHESIS): **人が止める前提の、問い合わせ受付〜要確認一覧**.  
n8n is an implementation option, not the brand.

## Pack map

| File | Lane | Role | Status |
|---|---|---|---|
| [FACTS.md](FACTS.md) | all | Allowed / forbidden claims | cite only |
| [ASSETS-POINTER.md](ASSETS-POINTER.md) | all | PRs **#115 / #116 / #117 / #120 / #121** only | no fake screenshots |
| [SEND-CHECKLIST.md](SEND-CHECKLIST.md) | all | What 祐太 fills before any later send | default **do-not-send** |
| [JP/coconala-service-pitch.md](JP/coconala-service-pitch.md) | **Coconala** (active) | Service listing paste. Flagship = P1. P2/P3 optional fail-closed proof | unpublished draft |
| [JP/coconala-inquiry-reply-template.md](JP/coconala-inquiry-reply-template.md) | **Coconala** (active) | Custom-estimate / inquiry reply | unsent |
| [JP/crowdworks-or-lancers-proposal.md](JP/crowdworks-or-lancers-proposal.md) | JP thin | One CrowdWorks-style proposal (Lancers swap note) | parked, unsent |
| [EN/contra-job-proposal-01.md](EN/contra-job-proposal-01.md) | **Contra** (active) | Job-feed apply. PR#71 style 01, rebased to P1–P3 | unsent |
| [EN/contra-service-blurb.md](EN/contra-service-blurb.md) | **Contra** (active) | Independent service / about blurb | unpublished draft |
| [EN/upwork-proposal.md](EN/upwork-proposal.md) | EN thin | One Upwork-style cover letter | parked, unsent |

JP files are Japanese. EN files are English.

## Strategy (max 2 active lanes)

| Slot | Desk | Use this pack for |
|---|---|---|
| Active 1 | Coconala | listing pitch + estimate reply |
| Active 2 | Contra | service blurb + **one** Job-feed paste |
| Thin / parked | CrowdWorks or Lancers | only if a later GO swaps a lane |
| Thin / parked | Upwork | only if a later GO swaps a lane |

Do not open a third active lane from this folder. Older packs (Contra #71, JP #11, Coconala #79/#81) are pre-showcase voice. **Do not mix their n8n-as-religion claims with this pack.**

## FACTS boundary (short)

Cite **only** the completed showcase after QA PASS:

| Demo | PR | Head | Say this, nothing else |
|---|---|---|---|
| P1 intake | [#115](https://github.com/rimone0511/autopilot-log/pull/115) | `541bb18` | validate / dedupe / hold-for-human. Duplicate `inquiry_id` → every collided row `needs_human`. CSV = JSON. `--check` clean |
| P2 weekly CSV | [#117](https://github.com/rimone0511/autopilot-log/pull/117) + [#120](https://github.com/rimone0511/autopilot-log/pull/120) | `14b818c` | source / `#Ln` / SHA-256 of the file actually read. Timezone-aware week bounds |
| P3 fail-stop | [#116](https://github.com/rimone0511/autopilot-log/pull/116) | `0a822e0` | timeout ≠ approve. Actorless / missing / reused event IDs are non-writing |
| QA | [#121](https://github.com/rimone0511/autopilot-log/pull/121) `QA-REPORT.md` | — | **PASS**. FACTS-limited proposal **prep** OK |

SOL’s first pass was CONDITIONAL/FAIL, then the heads above were fixed. A second SOL human review is optional. **Do not write “SOL cleared twice.”**  
Do not write production n8n, revenue, time saved, or accuracy %.  
n8n in the demos: `active=false`, no send nodes, synthetic fixtures only.

Full checklist: [FACTS.md](FACTS.md). Proof links only: [ASSETS-POINTER.md](ASSETS-POINTER.md).

## GO gates

| Gate | Who | This pack |
|---|---|---|
| Showcase QA PASS | already on #121 | unlocks **prep only** |
| Fill `{{ONE_SPECIFIC_DETAIL}}`, target URL, `{{PRICE}}` | 祐太, local ledger | required before any later send |
| [SEND-CHECKLIST.md](SEND-CHECKLIST.md) all boxes | 祐太 | still not a send |
| Explicit human **GO** on that one URL | 祐太 | **not given here** |
| publish / apply / send / register / merge / Activate / spend | 祐太 after GO | **forbidden from this PR** |

Empty required slot → skip. Do not invent the detail, the URL, or the price.

## How to use (ADHD)

1. Open **one** file from the pack map. Close the others.
2. Keep the operator table **out** of the live form. Paste only the fenced block.
3. Replace placeholders on a **local** scrap. Do not commit live prices, job URLs, or real names.
4. Re-count characters on the live form (placeholders grow when filled).
5. Stop. Do not click 公開 / Apply / 提案する / Submit / Spend Connects.

## Shared placeholders

| Token | Meaning | In git |
|---|---|---|
| `{{ONE_SPECIFIC_DETAIL}}` | One fact from **this** listing / inquiry | empty / fictional-example only |
| `{{JOB_TITLE}}` | Short title of that post | fictional examples only |
| `{{TARGET_URL}}` | Official desk URL you opened | empty |
| `{{PRICE}}` | Price **policy** token (see SEND-CHECKLIST) | empty |
| `{{PRICE_YEN}}` / `{{PRICE_YEN_DRAFT}}` | Coconala / JP form yen box | empty |
| `{{FIXED_PRICE_USD}}` / `{{HOURLY_RATE_USD}}` | Contra / Upwork form only | empty |
| `{{LEAD_TIME_DRAFT}}` / `{{LEAD_DAYS}}` / `{{DELIVERY_DAYS}}` | Lead time | empty |
| `{{DISPLAY_NAME}}` | Seller display | recommended 石田祐太 / Yuta Ishida |
| `{{PORTFOLIO_URL}}` | Public notes | recommended `https://yutalab.dev/` |
| `{{GITHUB_REPO_AUTOPILOT}}` | Public repo | `https://github.com/rimone0511/autopilot-log` |
| `{{TIMEZONE}}` | Async zone | example `JST` |
| `{{QUESTION_1}}` `{{QUESTION_2}}` | One real question each | empty until rewrite |
| `{{PLATFORM_FEE_NOTE}}` | Fee one-liner | read official help at click-time; **no rate in git** |

Public links allowed in paste: yutalab.dev, this repo, and the five PRs in [ASSETS-POINTER.md](ASSETS-POINTER.md).

## Out of scope

- Sending, publishing, applying, registering, merging, n8n Activate, Connects / Pro / ads spend
- Fake reviews, invented “Client Yamada” as real, hours saved, 99% accuracy
- Browser bots, scrape lists, off-platform payment pitch
- Claiming Autopilot Log’s YouTube/TikTok gate is this product

## Test plan (this PR)

- [x] Required files present under `ops/earn/earn-showcase-proposal-pack-20260916/`
- [x] Every file header: `DRAFT_ONLY` / `DO NOT SEND`
- [x] Buyer fences stay FACTS-limited; no invented metrics
- [x] Repo Python gates untouched
- [ ] Human: personalize later; **do not send from this PR**
- [ ] Do not merge until 祐太 reviews; keep draft

> **DRAFT_ONLY. DO NOT SEND.**  
> Contra Independent **service / about** paste. Do not publish the Services card from this pack.  
> No fake reviews. No live rates. Agent does not click Publish.

# Contra — service blurb (human-held intake)

| key | value |
|---|---|
| pack | earn-showcase-proposal-pack-20260916 |
| desk | Contra Independent (active lane 2/2) |
| surface | Service title + about / what I do (not a Job-feed apply) |
| offer | Human-held inquiry intake → hold-for-human list |
| draft | true |
| publish | **forbidden** |

**Next action:** paste into a **draft** Services / about field if the UI allows save-without-publish. If publish is the only control, **stop**.

Job-feed letters stay in [contra-job-proposal-01.md](contra-job-proposal-01.md).  
Proof URLs: [ASSETS-POINTER.md](../ASSETS-POINTER.md).

---

## Form fields (not in the blurb)

| UI field | Value |
|---|---|
| Rate / package | `{{PRICE}}` → `{{FIXED_PRICE_USD}}` or **Contact for pricing** |
| Hourly | `{{HOURLY_RATE_USD}}` or leave empty |
| Location | Japan. Do not fake US/EU |
| Languages | Japanese and English (async `{{TIMEZONE}}`) |

Do not buy Contra Pro from this file.

---

## Service title (short)

```
Human-held inquiry intake → hold-for-human list
```

## One-liner

```
Validate and dedupe inbound rows. Ambiguous IDs go to a person. No auto-send. n8n optional.
```

---

## About / service body (paste)

```
I set up a human-held intake: inbound inquiries are validated, duplicates and colliding IDs are surfaced, and a hold-for-human list is the output. Nothing is emailed or published by the machine.

n8n is one implementation option (official connectors only). A spreadsheet plus a small script is also in scope when that is the smaller fit. I do not scrape. I do not run browser bots.

Public synthetic demos (self-made, not client case studies):
- Intake — GitHub PR 115, head 541bb18: validate / dedupe / hold-for-human. Duplicate inquiry_id holds every collided row. CSV matches JSON.
- Optional weekly CSV with source, line number, and SHA-256 of the file actually read (PR 117+120, head 14b818c). Timezone-aware.
- Optional fail-stop (PR 116, head 0a822e0): timeout is not approve. Actorless, missing, or reused event IDs do not write.

n8n samples are inactive, with no send nodes. I do not claim production n8n, revenue, hours saved, or accuracy %.

I am {{DISPLAY_NAME}}, based in Japan. Async {{TIMEZONE}}. Stay on Contra for scoping and payment. Notes: {{PORTFOLIO_URL}}
```

---

## What I do / don’t (optional bullets if the UI has chips)

**Do**

- Intake validation and a review list a person can rerun
- Duplicate / colliding-id hold
- Optional traceable weekly CSV
- Optional write-guard: timeout ≠ approve

**Don’t**

- Auto-reply or auto-publish
- Fake reviews or invented metrics
- Partner-badge impersonation
- Off-platform payment for Contra-originated work

---

## CTA (if the card needs one)

```
Message me on Contra with one example row (PII stripped) and what “hold” should mean. I will not send a quote in this box — use Contra’s official proposal flow.
```

---

## STOP

- Do not publish
- Do not attach a fake screenshot to fill an empty gallery
- Do not paste fixture counts as results

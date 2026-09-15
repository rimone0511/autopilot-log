> **DRAFT_ONLY. DO NOT SEND.**  
> 祐太 fills this **locally**. Do not commit live URLs, prices, or real names.  
> Default remains **do-not-send** even if every box is ticked.

# Send checklist — 祐太 before any later send

**Next action:** copy this list to a local scrap → fill the three slots → if any slot is empty, **skip**.  
This folder still does not click 公開 / Apply / 提案する / Submit.

## 1. Three slots (hard)

| Slot | Token | Rule |
|---|---|---|
| Detail | `{{ONE_SPECIFIC_DETAIL}}` | One fact from **this** listing or inquiry, in about a minute. If you cannot name it, skip. Do not reuse yesterday’s detail. |
| Target URL | `{{TARGET_URL}}` | Official desk URL you opened yourself (Coconala service / request, Contra Job, etc.). Not a scrape dump. Not a third-party apply tool. |
| Price policy | `{{PRICE}}` | Human-chosen policy for **this** form only. Git stays empty. |

`{{PRICE}}` mapping (same empty policy, different boxes):

| Desk | Type this locally into | Alias in the file |
|---|---|---|
| Coconala listing | サービス価格 | `{{PRICE_YEN}}` |
| Coconala estimate | 料金 | `{{PRICE_YEN_DRAFT}}` |
| CrowdWorks / Lancers | 希望報酬 | `{{PRICE_YEN_DRAFT}}` |
| Contra paid-project / rate | official form | `{{FIXED_PRICE_USD}}` or `{{HOURLY_RATE_USD}}` |
| Upwork bid | official form | `{{FIXED_PRICE_USD}}` or `{{HOURLY_RATE_USD}}` |

If the live box will not accept a placeholder: leave it **empty**, park `rate_required`, **do not invent a number**, do not send.

Fee copy: `{{PLATFORM_FEE_NOTE}}` after you re-read the official help. **Do not write a fee % into git.**

## 2. Confirm before a later click

### Identity / FACTS

- [ ] I re-read [FACTS.md](FACTS.md). No F1–F14 phrase is in the paste I would send
- [ ] I did not add fixture counts (20 / 14 / 9,600円 / 12 events) as results
- [ ] I did not write “SOL cleared twice”, production n8n, revenue, time saved, or accuracy %
- [ ] Showcase links, if any, are only [ASSETS-POINTER.md](ASSETS-POINTER.md) (#115 / #116 / #117 / #120 / #121)
- [ ] Fictional labels (`依頼者A`, `Client A`) were **not** replaced with a real name in git

### Target

- [ ] `{{TARGET_URL}}` is open in my browser on the official host
- [ ] `{{JOB_TITLE}}` matches that page
- [ ] `{{ONE_SPECIFIC_DETAIL}}` is unique to that page
- [ ] Theme still matches **human-held intake → hold list** (P1). I am not selling YouTube posting or a generic “n8n Expert” gig
- [ ] Active-lane rule: this send would be **Coconala or Contra**. CrowdWorks / Lancers / Upwork stay parked unless I explicitly swap a lane

### Money / spend (this pack forbids)

- [ ] `{{PRICE}}` is filled on the **local** scrap from my price policy, not from a guessed market rate in this PR
- [ ] Lead time `{{LEAD_TIME_DRAFT}}` / `{{DELIVERY_DAYS}}` is filled or I skip
- [ ] I will **not** buy Contra Pro, spend Upwork Connects, run ads, or pay boosts from this pack
- [ ] I will **not** pitch off-platform payment

### Hands

- [ ] Operator tables stayed out of the fenced paste
- [ ] No email / phone / LINE / WhatsApp in the letter (Coconala = talk room only; Contra / Upwork = platform messages)
- [ ] I re-counted characters on the live form
- [ ] I will click send **myself**, on a later GO — **not from this PR**
- [ ] n8n Activate / import-to-production is **not** part of sending a proposal

## 3. GO line (still blank)

```
GO: no
target: {{TARGET_URL}}
file: {{WHICH_MD}}
detail: {{ONE_SPECIFIC_DETAIL}}
price_policy: {{PRICE}}
signed: {{DISPLAY_NAME}}
date:
```

Leave `GO: no` until 祐太 changes it **outside git** (or a later ticket).  
Agents must not flip this to yes.

## STOP

- Empty detail, URL, or price → do not send
- Desk demands image / KYC / wallet / Pro / Connects spend to continue → stop (different ticket)
- Temptation to “just publish the listing to see how it looks” → still send. Do not.

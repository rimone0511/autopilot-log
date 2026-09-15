> **DRAFT_ONLY. DO NOT SEND. DO NOT PUBLISH.**  
> No connection requests, InMail, Services proposals, feed posts, or Service Page Save-if-viewable from this pack.  
> No secrets. No bots. Rates stay placeholders. Agent does not submit.

# LinkedIn outreach DRAFT pack — Wave 2 (2026-09-16)

Pack date: 2026-09-16  
Desk: LinkedIn **connection notes** + LinkedIn **Services** proposal replies  
Not: LinkedIn **Jobs**, Recruiter, Sales Navigator, Company Page, feed, newsletter  
Mode: **`DRAFT_ONLY`** + **HANDS** (human paste, one person / one inbound request at a time)  
Language: **EN + JP mix** (six of each)  
Seller: `{{DISPLAY_NAME}}` (recommended: Yuta Ishida / 石田祐太)  
Themes: **n8n workflow**, **AI ops**, **lead classify**  
Public notes: https://yutalab.dev/  
Public tool: https://github.com/rimone0511/autopilot-log

Wave 2 here matches the same seller themes as `earn-en-proposal-wave2-20260916/` and `earn-jp-proposal-wave2-20260916/`. It is **not** a blast campaign and it is **not** a Service Page setup pack (that is sibling `earn-upwork-linkedin-cu-handoff-20260916/03-linkedin-services.md`).

**Do not merge this as an outreach bot.** There is no send script. There is no invitation sprayer. There is no Sales Nav sequence.

Rules: [HANDS-AND-TOS.md](HANDS-AND-TOS.md).  
Facts that may be claimed: [FACTS.md](FACTS.md) (do not paste that file into LinkedIn).  
Publish/send switch: [STOP-AT-PUBLISH.md](STOP-AT-PUBLISH.md) — **fail closed**.

---

## Stop-at-publish gate (fail closed)

This repository already treats “the automation is running” and “something may go public” as two switches. LinkedIn gets the same split.

| Switch | This pack |
|---|---|
| Drafts exist in git | yes |
| Human may paste locally | yes, after rewriting `{{ONE_SPECIFIC_DETAIL}}` |
| Send / Submit / Save-as-viewable / Share to feed | **no** — gate is closed |
| Buying Premium / InMail / extra RFP matching | **no** |
| Computer-use or any tool clicks Send | **no** |

**Fail closed:** if [STOP-AT-PUBLISH.md](STOP-AT-PUBLISH.md) is missing, unread, or any row is `true` / unchecked, treat every paste as **not sendable**. This pull request is **not** a publish GO. A later human GO lives outside this repo (morning operator). Until then, every control below stays off:

```
linkedin_outreach_gate:
  pack: earn-linkedin-outreach-wave2-20260916
  draft_only: true
  send_connection_request: false
  attach_note_and_send: false
  send_blank_invite_as_workaround: false
  send_inmail: false
  submit_services_proposal: false
  message_from_services_admin: false
  save_service_page_if_viewable: false
  share_to_feed: false
  notify_network: false
  buy_premium: false
```

A missing gate file means the same as every flag `false`. Do not “infer” permission from a merged PR.

---

## Twelve drafts (3 themes × 2 surfaces × EN/JP)

| # | File | Lang | Surface | Theme | Paste into |
|---|---|---|---|---|---|
| 01 | [01-connect-n8n-en.md](01-connect-n8n-en.md) | EN | Connection note | n8n | Add a note on **Connect** (≤200) |
| 02 | [02-connect-n8n-jp.md](02-connect-n8n-jp.md) | JP | Connection note | n8n | つながり申請のメモ（≤200） |
| 03 | [03-connect-aiops-en.md](03-connect-aiops-en.md) | EN | Connection note | AI ops | Add a note on Connect |
| 04 | [04-connect-aiops-jp.md](04-connect-aiops-jp.md) | JP | Connection note | AI ops | つながり申請のメモ |
| 05 | [05-connect-classify-en.md](05-connect-classify-en.md) | EN | Connection note | lead classify | Add a note on Connect |
| 06 | [06-connect-classify-jp.md](06-connect-classify-jp.md) | JP | Connection note | lead classify | つながり申請のメモ |
| 07 | [07-services-n8n-en.md](07-services-n8n-en.md) | EN | Services proposal | n8n | Admin view → New requests → proposal message |
| 08 | [08-services-n8n-jp.md](08-services-n8n-jp.md) | JP | Services proposal | n8n | サービス管理 → 新しい依頼 → 提案メッセージ |
| 09 | [09-services-aiops-en.md](09-services-aiops-en.md) | EN | Services proposal | AI ops | inbound RFP personal message |
| 10 | [10-services-aiops-jp.md](10-services-aiops-jp.md) | JP | Services proposal | AI ops | 届いた依頼への提案文 |
| 11 | [11-services-classify-en.md](11-services-classify-en.md) | EN | Services proposal | lead classify | inbound RFP personal message |
| 12 | [12-services-classify-jp.md](12-services-classify-jp.md) | JP | Services proposal | lead classify | 届いた依頼への提案文 |

Each file keeps a **fact table** (operator metadata + form-field rates) **outside** the fenced paste. Pack-level facts live in [FACTS.md](FACTS.md). Do not copy either table into LinkedIn.

Connection notes (01–06) are **peer context**, not a Services pitch. LinkedIn’s Professional Community Policies forbid using invitations to send promotional messages to people you do not know.

Services pastes (07–12) are **inbound only**. No RFP in Admin view → do not recycle them as DMs or connection notes.

---

## Send / publish gate (every paste)

Skip the person or request if any box is false. This pack still does **not** send.

- [ ] I opened **this** profile or **this** Services request in **linkedin.com** (not a scraper, not a growth tool, not Sales Nav automation).
- [ ] [STOP-AT-PUBLISH.md](STOP-AT-PUBLISH.md) is still all `false`. I am only rehearsing a paste.
- [ ] I replaced `{{ONE_SPECIFIC_DETAIL}}` with a fact from **this** public post / headline / RFP. If I cannot name one in about a minute, I skip.
- [ ] For 01–06: I am not using the note to sell. No URL, no “Request services”, no calendar link.
- [ ] For 07–12: a **New request** already exists. I did not cold-message this copy.
- [ ] Leftover placeholders from a previous person are gone.
- [ ] No email, phone, WhatsApp, Telegram, Slack, Discord, or “text me at…” in the paste.
- [ ] No InMail. No Premium trial. No second LinkedIn account.
- [ ] The live character counter still has room **after** substitutions (connection notes: plan for **200** on Basic).
- [ ] I will click **Send / Submit / Save** myself only after a GO **outside** this folder. Nothing here submits.

---

## Fact table vs prose

| Layer | Lives in | Contains rates? |
|---|---|---|
| Pack facts | [FACTS.md](FACTS.md) | No live prices |
| Per-file fact table | Markdown **above** the fences | Yes — **placeholders only**, mapped to UI fields |
| Form fields on LinkedIn | Services proposal form (if shown) | Human types the local number later |
| Fenced paste | Connection note / proposal message | **No live prices. No email.** |

If a live Services form **blocks** submit with an empty rate: park `rate_required` and stop. Do not invent USD/JPY in git. Do not send from this PR.

---

## Length (official where cited; live counter wins)

| Surface | Guidance | Source |
|---|---|---|
| Connection note (Basic) | **200 characters** | [Personalize invitations](https://www.linkedin.com/help/linkedin/answer/a563153) |
| Personalized notes / month (Basic) | **up to 3** (older help said 5; **live UI wins**) | same article |
| Premium note length | Current help omits a Premium count; an older comparison page said 300. **Write to 200.** Do not buy Premium from this pack. | [InMail vs invitations](https://www.linkedin.com/help/linkedin/answer/a6239760) |
| InMail | 200 subject / 1900 body | [InMail character limits](https://www.linkedin.com/help/linkedin/answer/a411986) — **out of this pack** |
| Services proposal message | Brief; reference the request | [Best practices for writing a proposal](https://www.linkedin.com/help/linkedin/answer/a570671) |
| Service Page About | Not this pack | Sibling CU handoff; live form wins |

Character counts in each file’s fact table are `len()` of the fenced body (placeholders unsubstituted, 2026-09-16). Filling placeholders **increases** length. Re-count on the live form.

Connection notes leave a **detail budget**: if `{{ONE_SPECIFIC_DETAIL}}` + `{{DISPLAY_NAME}}` would exceed 200, shorten the detail or skip. Do not send a truncated sentence.

Measured this pack (`len` of the fenced body, no trailing-fence newline counted beyond the body, placeholders unsubstituted):

| File | note | short | standard | decline |
|---|---:|---:|---:|---:|
| 01 n8n connect EN | 138 | — | — | — |
| 02 n8n connect JP | 103 | — | — | — |
| 03 AI ops connect EN | 149 | — | — | — |
| 04 AI ops connect JP | 93 | — | — | — |
| 05 classify connect EN | 143 | — | — | — |
| 06 classify connect JP | 87 | — | — | — |
| 07 n8n Services EN | — | 441 | 1150 | 203 |
| 08 n8n Services JP | — | 264 | 594 | 102 |
| 09 AI ops Services EN | — | 399 | 1196 | 199 |
| 10 AI ops Services JP | — | 237 | 650 | 92 |
| 11 classify Services EN | — | 386 | 975 | 170 |
| 12 classify Services JP | — | 221 | 599 | 87 |

Unsubstituted connection notes are all under 200. After fill they grow; the fictional fills in 01–06 stayed ≤155. Services standard pastes are under InMail’s 1900 (this pack still does not send InMail). Live counter wins.

---

## What this pack will not claim

- Years of experience, GMV, review counts, “Top Voice”, or traffic
- A US/EU address (Japan is fine; do not spoof location)
- n8n Expert / Zapier Partner / Make Partner / xAI or model-vendor employment
- That Autopilot Log posts TikTok unattended (inbox upload is the default; direct post is gated)
- That an agent will send customer email, publish, or take payment without a human stop
- Scraping, likes/follows/views, invitation blasting, or InMail sequences
- Income, time-saved, or win-rate guarantees

---

## Out of this folder on purpose

- Creating or **publishing** a Service Page (sibling CU pack; Save may make it viewable)
- LinkedIn Jobs / Easy Apply / Open to Work frame
- Company Page vs personal profile (locked choice — do not pick Company)
- KYC, ads identity, Premium, Sales Nav, Recruiter
- Upwork / Fiverr / CrowdWorks proposal text (other Wave 2 packs)
- Any script, extension, or API call that sends invitations or messages

## 日本語（運用だけ）

下書きのみ。送信しない。公開しない。つながり申請のメモは売り込みに使わない（知らない人への宣伝はポリシー違反）。Services の文は届いた依頼への返信だけ。`{{ONE_SPECIFIC_DETAIL}}` が埋まらなければ捨てる。本文に金額・メール・電話を書かない。月3件のメモ上限に当たったら、空の申請で逃げない。このPRは公開GOではない。

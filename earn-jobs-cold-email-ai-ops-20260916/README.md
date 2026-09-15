> **DRAFT_ONLY. DO NOT SEND.**  
> No Gmail send, no SMTP, no sequencer, no mailbox draft from this agent.  
> No secrets. No live recipient addresses. No invented case studies or fake metrics.  
> Agent does not submit.

# Cold email DRAFT pack — AI ops / n8n for SMBs (2026-09-16)

Pack date: 2026-09-16  
Desk: **one-off cold email copy** (EN + JP mix) for independent freelance setup work  
Audience: small and mid-size businesses (fictional labels only in git)  
Mode: **`DRAFT_ONLY`** + **HANDS** (human rewrite, one public page at a time)  
Language: **5 EN + 5 JP**  
Seller: `{{DISPLAY_NAME}}` (recommended: Yuta Ishida / 石田祐太)  
Themes: **n8n workflow**, **AI ops**, **lead classify**  
Public notes: https://yutalab.dev/  
Public tool: https://github.com/rimone0511/autopilot-log

This is the JOBS-phase sibling of `earn-linkedin-outreach-wave2-20260916/` (LinkedIn notes/Services) and the n8n SKU drafts. It is **not** a mailer. It is **not** a list. It is **not** a legal opinion that a given contact@ is sendable.

**Do not merge this as an outreach bot.** There is no send script. There is no CSV. There is no Gmail call in this PR.

Rules: [HANDS-AND-TOS.md](HANDS-AND-TOS.md).  
Facts that may be claimed: [FACTS.md](FACTS.md) (do not paste that file into mail).  
Send switch: [DRAFT_ONLY.md](DRAFT_ONLY.md) — **fail closed**.

---

## Stop-at-send gate (fail closed)

This repository already treats “the automation is running” and “something may go public” as two switches. Cold email gets the same split.

| Switch | This pack |
|---|---|
| Drafts exist in git | yes |
| Human may rewrite locally | yes, after filling `{{ONE_SPECIFIC_DETAIL}}` from **one** public page |
| Create mailbox draft / Send / Schedule / SMTP | **no** — gate is closed |
| Purchased or harvested list | **no** |
| Invented metrics / fake case studies | **no** |
| Computer-use or any tool clicks Send | **no** |

**Fail closed:** if [DRAFT_ONLY.md](DRAFT_ONLY.md) is missing, unread, or any send row is `true` / unchecked, treat every paste as **not sendable**. This pull request is **not** a send GO. A later human GO lives outside this repo. Until then, every control stays off (see that file).

---

## Ten drafts (EN+JP mix)

| # | File | Lang | Theme | SMB angle (fictional) |
|---|---|---|---|---|
| 01 | [01-n8n-inbound-en.md](01-n8n-inbound-en.md) | EN | n8n | Public contact form → sheet → human send |
| 02 | [02-n8n-inbound-jp.md](02-n8n-inbound-jp.md) | JP | n8n | 公開フォーム → 表 → 人が送る |
| 03 | [03-aiops-inspect-en.md](03-aiops-inspect-en.md) | EN | AI ops | Draft / inspect / human approve |
| 04 | [04-aiops-inspect-jp.md](04-aiops-inspect-jp.md) | JP | AI ops | 下書き→確認→人が承認 |
| 05 | [05-classify-en.md](05-classify-en.md) | EN | lead classify | Labels + unsure bucket, no auto-reply |
| 06 | [06-classify-jp.md](06-classify-jp.md) | JP | lead classify | ラベル＋保留。自動返信なし |
| 07 | [07-n8n-sheets-en.md](07-n8n-sheets-en.md) | EN | n8n | New rows without overwriting the live sheet |
| 08 | [08-n8n-sheets-jp.md](08-n8n-sheets-jp.md) | JP | n8n | 既存の表を壊さないつなぎ |
| 09 | [09-aiops-publish-gate-en.md](09-aiops-publish-gate-en.md) | EN | AI ops | Fail-closed publish / send switch |
| 10 | [10-aiops-publish-gate-jp.md](10-aiops-publish-gate-jp.md) | JP | AI ops | 送信・公開は人手。門は閉じたまま倒れる |

Each file keeps a **thin operator table** above the fences (id, language, send=forbidden, character counts). **Seller facts and rates live only in [FACTS.md](FACTS.md).** Do not copy either table into the message.

---

## Send gate (every paste)

Skip the address if any box is false. This pack still does **not** send.

- [ ] I opened **this** organization’s **public** page in a normal browser (not a scrape dump, not a purchased list).
- [ ] [DRAFT_ONLY.md](DRAFT_ONLY.md) is still all do-not-send. I am only rehearsing a paste.
- [ ] I can name the **legal basis** for **this** address without stretching (JP: opt-in or a statute exception I can point at; US: CAN-SPAM disclosures I can actually fill). If I cannot, I skip.
- [ ] I replaced `{{ONE_SPECIFIC_DETAIL}}` with a fact from **this** public page. If I cannot name one in about a minute, I skip.
- [ ] Leftover placeholders from a previous SMB are gone.
- [ ] No phone, WhatsApp, Telegram, Slack, Discord, or calendar link in the body.
- [ ] No live USD/JPY. No fake “hours saved” / client counts / named case studies.
- [ ] Footer still has `{{POSTAL_ADDRESS}}` and `{{OPT_OUT_CONTACT}}` as placeholders **in git**. I will not commit filled values. I will not Send with placeholders still showing.
- [ ] This is the **only** note I would ever consider for this domain (no follow-up sequence in this pack).
- [ ] I will click **Send** myself only after a GO **outside** this folder. Nothing here submits.

---

## Fact table vs prose

| Layer | Lives in | Contains rates / PII? |
|---|---|---|
| Pack facts | [FACTS.md](FACTS.md) | No live prices; no live mailboxes |
| Per-file operator table | Markdown **above** the fences | Counts only |
| Mail headers (From / To) | Human client, later | Placeholders in git |
| Fenced paste | Subject + body + legal footer | **No live prices. No live PII.** |

Empty required `{{ONE_SPECIFIC_DETAIL}}` → skip. Do not reuse a detail from another domain.

---

## Length (practical; live composer wins)

There is no official “cold email character cap.” Keep the **standard** body short enough to read on a phone. Character counts in each file are `len()` of the fenced **body** (placeholders unsubstituted, 2026-09-16). Filling placeholders **increases** length. Re-count before any future send.

Measured this pack (`len` of the fenced body; subject counted separately):

| File | subject short / std | short body | standard body |
|---|---:|---:|---:|
| 01 n8n inbound EN | 42 / 57 | 628 | 1259 |
| 02 n8n inbound JP | 25 / 48 | 436 | 755 |
| 03 AI ops inspect EN | 53 / 60 | 615 | 1205 |
| 04 AI ops inspect JP | 12 / 47 | 391 | 700 |
| 05 classify EN | 44 / 68 | 624 | 1083 |
| 06 classify JP | 17 / 38 | 398 | 664 |
| 07 n8n sheets EN | 49 / 60 | 645 | 1129 |
| 08 n8n sheets JP | 18 / 45 | 410 | 679 |
| 09 publish-gate EN | 59 / 49 | 735 | 1107 |
| 10 publish-gate JP | 19 / 35 | 468 | 684 |

Counts are filled after the bodies are frozen (same commit).

---

## What this pack will not claim

- Years of experience, GMV, review counts, traffic, or “N SMBs automated”
- Named or anonymized case studies with metrics
- A US/EU address (Japan is fine; do not spoof location)
- n8n Expert / Zapier Partner / Make Partner / xAI or model-vendor employment
- That Autopilot Log posts TikTok unattended (inbox upload is the default; direct post is gated)
- That an agent will send customer email, publish, or take payment without a human stop
- Scraping, likes/follows/views, or list blasting
- Income, time-saved, or win-rate guarantees
- That a published `contact@` is automatically lawful to mail in Japan

---

## Out of this folder on purpose

- Creating Gmail drafts or sending
- LinkedIn connection notes / Services RFPs (sibling Wave 2 pack)
- Upwork / Fiverr / CrowdWorks / Coconala proposals
- Gumroad SKU publish
- Domain warm-up, SPF/DKIM setup runbooks (ops, not this JOBS paste)
- Any script, extension, or API call that delivers mail

## 日本語（運用だけ）

下書きのみ。送信しない。Gmailの下書きも作らない。日本の広告メールは原則オプトイン。例外を自分で条文に当てられない宛先は捨てる。`{{ONE_SPECIFIC_DETAIL}}` が公開ページから取れなければ捨てる。本文に金額・電話・偽の導入事例を書かない。住所と配信停止先はプレースホルダのまま git に残す。このPRは送信GOではない。

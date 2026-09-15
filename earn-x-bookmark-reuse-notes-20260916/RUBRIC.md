> **DRAFT_ONLY.** A person sorts **already bookmarked** posts, one at a time.  
> This agent does not search X, list bookmarks, unbookmark, reply, or post.  
> No counts, GMV, amounts, real handles, or full post text in git.

# RUBRIC — keep vs junk (bookmark reuse notes)

**Source policy:** sibling [PR #27](https://github.com/rimone0511/autopilot-log/pull/27) `RUBRIC.md` (`keep_queue` / `park` / `skip`). That folder is `earn-x-leads-keyword-pack-20260916/` (not merged to master at authoring time).

This file does not replace that pack. It answers a later question: *this post is already in Bookmarks — is it still reusable as an AI-agent earn lead?*

Verdict is **fail-closed**. Unsure → `junk`. `keep` is “human may later draft one reply,” not permission to send.

The note form is [`TEMPLATE.md`](TEMPLATE.md).

---

## 1. Two reuse verdicts (plus a junk subtype)

| `reuse` | Means | Next |
|---|---|---|
| `keep` | Buyer + this desk’s fit + freelance shape + still fresh + one concrete detail | Secret-free note. Reply draft is a **different** pack. This folder does not send |
| `junk` | Not reusable as outreach from this desk | Log subtype. **Do not unbookmark from this pack.** Stop. Do not argue in-thread |

`park` from PR #27 is **not** a third send-queue. Here it is junk subtype `park_not_a_lead`: interesting, not a buyer request. Do not reuse as a lead. Do not treat as “delete this bookmark.”

Do not invent `needs_check`. If the post is gone, locked, or unreadable → `junk` / `locked`.

---

## 2. Map from PR #27

| PR #27 gate | Bookmark `reuse` | `junk_why` if junk |
|---|---|---|
| `keep_queue` and still true **today** (re-read the UI) | `keep` | — |
| `keep_queue` then, but now filled / too old / locked | `junk` | `filled` / `stale` / `locked` |
| `park` | `junk` | `park_not_a_lead` |
| `skip` | `junk` | matching skip type below |
| Same public permalink already noted | `junk` on the later row | `duplicate` |

Re-judge in the bookmarks UI. Do not copy an old `keep_queue` from memory. Bookmarks freeze a moment; the thread may already say “taken.”

---

## 3. `keep` needs all five (same four as PR #27 + still reusable)

Missing any one → not `keep`.

1. **Buyer** — they want work done. They are not selling the same gig.
2. **Fit** — body matches this desk: n8n / official API / ticket+inspect / GAS / an agent a person can stop. See §8.
3. **Shape** — freelance / subcontract / one-shot / short contract. Employee apply-only, onsite-only, unpaid trial → junk.
4. **Fresh** — about **7 days** in the UI relative time, or a thread that still reads open. “Still looking” older than that → usually `stale` (junk). “Hired / 決まりました” → `filled`.
5. **Reusable** — you can write **one non-secret concrete** (`one_detail`) without pasting the whole post. If you cannot, it was never a keep.

Amounts, company names, and legal names are **not** keep conditions. Do not copy them into git.

---

## 4. Immediate `junk` (one hit is enough)

| `junk_why` | Looks like | Why |
|---|---|---|
| `seller` | “I build AI agents”, slots open, DM for rates | Same-desk promo or competitor |
| `bait` | “anyone can make income with 1000 agents” | Info-product / engagement bait |
| `job_board` | Apply / Lever / Greenhouse / 正社員 / new-grad / visa | Not this freelance desk |
| `out_of_scope` | auto-like, scrape, unofficial SNS, “send me your keys” | Same HANDS fence as sibling packs |
| `crypto_adult` | airdrop, NFT, trade bot, adult | Out of scope |
| `copy_mill` | same English on many accounts, short-link spray | Bot |
| `stale` | older than ~2 weeks with no close, or >7 days and cold | Likely filled or abandoned |
| `filled` | thread says hired / closed / “決まり” | Do not pitch |
| `locked` | deleted, private, cannot render | Do not chase |
| `unpaid` | experience-only, equity-only, no cash | Decline |
| `kyc_proxy` | “do my identity check” | Stop. Do not upload ID |
| `park_not_a_lead` | “n8n looks cool”, tool-vs-tool, news QT, no ask | PR #27 `park` |
| `duplicate` | same `permalink` already has a note | One note per URL |
| `other` | anything else that is not keep | Fail closed |

“Full-time ok, also contract” can still be `keep` if the body is a remote project. Jobs-board apply form only → `job_board`.

---

## 5. How to read a bookmarked post (short)

Do this in **your** browser, already signed in. Do not sign into X in an agent browser. Do not paste a Bearer token.

1. Subject: I need / 作ってほしい vs I offer / 始めました
2. Verb: buy vs sell
3. Stack: §8 box vs out of scope
4. Deliverable: flow / code / runbook vs followers
5. Place: remote ok vs five-day office only
6. Time: UI relative only. In the note: `seen_at` + that relative string. Public status permalink optional. **No full body in git** (copyright + secrets)

Quote-repost: judge the **quoter’s** sentence. If the original is a job post and the quote is “anyone want this contract?”, the quoter may be the buyer.

Folders on X are optional and **human-only**. This pack does not create folders via API and does not tell you to sync folders.

---

## 6. Language (for a later human reply, not sent here)

| Post | Later reply language (other pack) |
|---|---|
| Japanese body / `lang:ja` | Japanese |
| English body | English |
| Mixed | The side they wrote more of |

Do not mix languages in one outreach. This folder still does not send.

---

## 7. Reply gate stays closed

`keep` ≠ send.

If a person later replies, same HANDS as `earn-en-proposal-drafts` / `earn-jp-proposal-drafts`:

- One post, one message. No paste-blast DMs
- Paraphrase one concrete from the post. If you cannot, do not send
- No email / phone / WhatsApp on first touch
- Do not take keys or passwords. Client pastes keys in their own vault
- Decline like/follow/scrape jobs
- Do not post, auto-like, or auto-follow from this desk

X’s live terms win. This file is not legal advice. Do not write steps to automate search, bookmark dump, or DM.

### Unbookmark (explicit)

| Allowed | Not this pack |
|---|---|
| A person later taps the bookmark star **on one post they are looking at** | API `delete` / bulk unbookmark / “junk ⇒ remove” scripts |
| Leaving junk bookmarks in place | Treating `junk` as an order to clear the folder |

Default: **leave the star**. Notes are the sort. The UI is not a queue to drain by bot.

---

## 8. `fit_box` (keep only if one of the first four)

| `fit_box` | Can be `keep` | Body that forces junk |
|---|---|---|
| `n8n` | One flow, rerun notes, human stop on failure | Scrape third-party sites |
| `agent_inspect` | Ticket, inspect, regression, pause mid-run | Ship prod with no review; secrets in logs |
| `official_api` | YouTube Data API / TikTok Content Posting. Client holds keys. TikTok explained as inbox-by-default | Browser posting, unofficial client |
| `gas` | Sheets, notify, human-seen exceptions | Bank scrape, password-sitting |
| `other_skip` | never keep | — |

---

## 9. Fictional posts (not real. do not send)

Labels `Bookmark-A` … `Bookmark-F` only. No handles.

### Bookmark-A → `keep`

- Lang: EN
- One-line: missed invoices, wants n8n, looking for a freelancer, they hold the keys
- Why: buyer + n8n + contract + new + one concrete

### Bookmark-B → `keep`

- Lang: JA
- One-line: Claude Code fix broke another screen; wants inspect + ticket outsourced
- Why: `agent_inspect`. Not browser-as-them

### Bookmark-C → `junk` / `park_not_a_lead`

- Lang: EN
- One-line: “agentic workflows are interesting. anyone using them?”
- Why: no order

### Bookmark-D → `junk` / `seller`

- Lang: EN
- One-line: I build production AI agents. Book a call. Slots open
- Why: seller. Bookmarking a competitor does not make them a lead

### Bookmark-E → `junk` / `out_of_scope`

- Lang: JA
- One-line: auto-like to grow followers, “set and forget”
- Why: engagement automation

### Bookmark-F → `junk` / `filled`

- Lang: EN
- One-line: week-old n8n ask; reply from OP “hired last Tuesday”
- Why: was maybe `keep_queue` when starred; not reusable now

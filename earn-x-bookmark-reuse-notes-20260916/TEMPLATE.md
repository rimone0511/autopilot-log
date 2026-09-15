> **DRAFT_ONLY.** Copy one block per bookmarked post. Do not call the X API. Do not unbookmark.  
> Do not paste full post text, amounts, emails, phones, IDs, cookies, or Bearer tokens.

# TEMPLATE — one reuse note per bookmark

Fill using [`RUBRIC.md`](RUBRIC.md). Empty placeholders stay empty. Do not invent a permalink or a `one_detail`.

`reuse` is only `keep` or `junk`. If PR #27 would have said `park`, set `reuse: junk` and `junk_why: park_not_a_lead`.

---

## Blank (copy this)

```text
note_id: {{BM-YYYYMMDD-##}}
seen_at: {{YYYY-MM-DD}}
permalink: {{PUBLIC_STATUS_URL_OR_EMPTY}}
lang: {{ja|en|mixed|unknown}}
ui_fresh: {{UI_RELATIVE_OR_UNKNOWN}}
reuse: {{keep|junk}}
junk_why: {{seller|bait|job_board|out_of_scope|crypto_adult|copy_mill|stale|filled|locked|unpaid|kyc_proxy|park_not_a_lead|duplicate|other|}}
buyer: {{yes|no|unsure}}
fit_box: {{n8n|agent_inspect|official_api|gas|other_skip}}
shape: {{freelance|job_board|seller|unknown}}
one_detail: {{ONE_NON_SECRET_PARAPHRASE_OR_EMPTY}}
star: leave
next: {{human_draft_reply|none}}
```

### Field rules

| Field | Rule |
|---|---|
| `note_id` | Local serial. Not an X snowflake. Example shape `BM-20260916-01` |
| `permalink` | Public `https://x.com/.../status/...` only, or empty. No `/i/bookmarks` dump URLs. Empty is fine |
| `junk_why` | Required when `reuse` is `junk`. Empty when `keep` |
| `buyer` | `unsure` cannot be `keep` → `junk` |
| `one_detail` | One short paraphrase. No quotes of the whole post. No money figures. No legal names |
| `star` | Always `leave` in this pack. Changing it to `remove` is out of scope |
| `next` | `human_draft_reply` only if `reuse` is `keep`. Otherwise `none` |

Do not add: email, WhatsApp, “DM sent”, API pagination tokens, folder ids from the bookmarks API, screenshots of the post body.

---

## Git / chat 1-liner (redacted)

If a line goes in this repo, keep it to the schema above. Prefer dropping `permalink` in public git when in doubt. Never paste the tweet.

```text
date: {{YYYY-MM-DD}}  note_id: {{BM-…}}  reuse: {{keep|junk}}  junk_why: {{or empty}}  fit_box: {{…}}  next: {{human_draft_reply|none}}
```

---

## Fictional filled examples (not real accounts. do not send)

### Example keep (n8n invoice flow)

```text
note_id: BM-20260916-EX1
seen_at: 2026-09-16
permalink:
lang: en
ui_fresh: 2h
reuse: keep
junk_why:
buyer: yes
fit_box: n8n
shape: freelance
one_detail: missed invoices; wants n8n; they hold keys
star: leave
next: human_draft_reply
```

### Example junk (seller, star stays)

```text
note_id: BM-20260916-EX2
seen_at: 2026-09-16
permalink:
lang: en
ui_fresh: 1d
reuse: junk
junk_why: seller
buyer: no
fit_box: other_skip
shape: seller
one_detail: slots-open agent build promo
star: leave
next: none
```

### Example junk (was maybe keep when starred; thread closed)

```text
note_id: BM-20260916-EX3
seen_at: 2026-09-16
permalink:
lang: ja
ui_fresh: 8d
reuse: junk
junk_why: filled
buyer: yes
fit_box: agent_inspect
shape: freelance
one_detail: inspect ticket; OP says already hired
star: leave
next: none
```

Permalink left empty on purpose in examples so this PR does not look like a live harvest.

---

## Batch habit (human, not a script)

1. Open bookmarks in **your** X UI. Do not export via API.
2. From the top, one post → one blank block.
3. Apply the rubric in under a minute. Unsure = junk.
4. Stop after a short pass. Do not “drain the folder” as a goal.
5. `keep` rows may later feed a **human** reply draft in a sibling proposal pack. Not this PR.

No loop, no pagination token, no unbookmark pass at the end.

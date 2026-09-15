# GO — SKU-0 Publish (default NO)

Pack date: 2026-09-16
Phase: JOBS
Desk: Gumroad
SKU: **SKU-0** — starter intake (form → table → notify)
Audience: **parent operator only** (祐太)
Mode: **DRAFT_ONLY**
After: listing polish [#74](https://github.com/rimone0511/autopilot-log/pull/74)

Walk [OPERATOR-CARD.md](OPERATOR-CARD.md) for two minutes. Fill this page on a
**local** copy. Do not commit a live permalink, a filled price ledger, or secrets.

---

## Default

```
GO: NO
publish_clicked: no
```

This pack has **no YES template**. Do not add one. Do not strike `NO` in git.

[#74](https://github.com/rimone0511/autopilot-log/pull/74) already said: green on
that checklist is not permission for an agent to click Publish. This card repeats
that rule after the polish, with the three looks below.

---

## Three looks (preconditions, not a go-live)

| Look | Look-target | If missing | Still publish? |
|---|---|---|---|
| Content files | Buyer zip/stubs **attached** (not operator markdown) | Ship-blocker | **No** |
| Price | **$39** USD, PWYW **off**, not $0 | Ship-blocker | **No** |
| Unpaid draft | Unpublished; payout **not** set up from this card | Desk default | **No** |

All three green ⇒ GO is still **NO** on this card.

Why unpaid draft stays NO:

- You must not sell a $39 download you cannot get paid for **from this pass**.
- You must not open payout / bank / tax / ID to “fix unpaid” from this pass.
- Desk stays `draft_saved`. Next CU is not Gumroad.

---

## Local verdict (do not commit filled)

```
date_jst:
operator: parent
after_pack: PR#74 listing polish
files_attached: yes / no / not_checked
price_39: yes / no / not_checked
unpaid_draft: yes / no / not_checked
cover_thumbnail: present / missing / not_checked
{{GUMROAD_PERMALINK_SKU0}}:
GO: NO
reason: default_do_not_publish
publish_clicked: no
payout_opened: no
```

`reason` stays `default_do_not_publish` even when the three looks are yes.
Optional extra local tags (still not a YES): `content_files_missing`,
`price_not_39`, `payout_screen_appeared`, `already_published`,
`sku0_live_draft_missing`, `several_drafts`, `files_need_human_open`.

---

## What would be a later human Publish (not this pack)

A separate pack, owned by a human click, after:

1. Every ship-blocker on [#74 CHECKLIST](https://github.com/rimone0511/autopilot-log/blob/cursor/gumroad-sku0-listing-polish-56b2/earn-jobs-gumroad-sku0-listing-polish-20260916/CHECKLIST.md) is green.
2. Buyer files are attached and a human has opened the zip locally (no secrets, stubs inactive).
3. Price is $39 (or a human-chosen `{{PRICE}}` typed locally — not $0).
4. Cover / thumbnail policy decided by a human (empty art is a warning, not an agent upload).
5. Payout / KYC owned by a **different** human pack, or an explicit human choice to wait.
6. No live URL announced until the product is actually published **by that human**.

Until that pack exists: **do not publish.**

---

## This page does not

- Authorize Publish / Enable
- Create or duplicate a Gumroad product
- Attach files or covers
- Set up payout
- Invent `gumroad.com/l/...`
- Claim the live editor was opened from this agent

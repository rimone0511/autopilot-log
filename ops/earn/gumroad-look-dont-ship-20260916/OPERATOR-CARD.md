# OPERATOR-CARD — Gumroad look-don't-ship (title / price / icons)

Pack date: 2026-09-16  
Audience: **parent operator only** (祐太). Not computer-use. **Two minutes.**  
Desk: Gumroad (Wave A+). Queue `done-draft`. CU hint `draft_saved`. Does not occupy CU-11.  
SKU: **SKU-0** — starter intake (form → table → notify)  
Mode: **DRAFT_ONLY. Look. Do not ship. Do not set up payout.**  
Scope: **title / price / icons only.** Content-tab files are out of scope.

This card is a 2-minute look at an **already unpublished** digital product. It is not a
Gumroad product, not a buyer zip, not a listing paste, and not a payout / KYC run.

Full look (including Content files): sibling QA pack
[`ops/earn/gumroad-draft-qa-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-gumroad-draft-qa-dc1f/ops/earn/gumroad-draft-qa-20260916)
([PR#55](https://github.com/rimone0511/autopilot-log/pull/55)). Do not copy that
checklist into this card. Do not run the files pass from here.

Google: MAIN only (`{{GOOGLE_ACCOUNT_EMAIL}}`). Do not create a second Gumroad.

---

## Clock (2:00 then stop)

| Min | Look | Do not |
|---|---|---|
| 0:00–0:20 | Hard stop. Find **one** unpublished SKU-0-shaped draft | New product. Publish / Enable. Payout |
| 0:20–0:50 | **Title / name** | Rename. Commit the live string |
| 0:50–1:20 | **Price** | Change the number. $0 “to test”. Commit USD/JPY |
| 1:20–1:50 | **Icons** (cover + thumbnail) | Upload. n8n / Gumroad / lab logo |
| 1:50–2:00 | Still unpublished. **STOP** | Files / Content tab. Discover. Announce a URL |

Tick boxes on a **local** copy. Do not commit a filled live title, price, cover
filename that contains a secret, or a `gumroad.com/l/...` URL.

---

## 0. Hard stop (read before opening Gumroad)

- [ ] This pass is **look-don't-ship**. Unpublished stays unpublished.
- [ ] CU does **not** open Gumroad from this card. Parent only.
- [ ] Do not click **Publish**, **Enable**, **Unpause**, or any go-live control.
- [ ] Do not type or announce a live `gumroad.com/l/...` URL. None is in git.
- [ ] Do not open Payout / Payments / bank / tax / ID upload.
- [ ] Do not buy Discover, boosts, or a custom domain.
- [ ] Do not upload a cover, thumbnail, or buyer zip.
- [ ] Do not open the **Content** tab (files = sibling QA pack, not this card).
- [ ] Do not create a product if none exists.

If a payout or identity screen appears: close it. Local note
`payout_screen_appeared`. Stop.

Public entry (desk, not a product URL): https://gumroad.com/  
Help (product editor): https://gumroad.com/help/article/149-adding-a-product

---

## 1. Find the existing unpublished SKU (do not create)

- [ ] Logged in as MAIN Google (queue already `done-draft`).
- [ ] Open the **products** list (live menu label is the source of truth).
- [ ] Locate **one** unpublished digital product that matches SKU-0 shape
      (starter intake: form → table → notify).
- [ ] Confirm unpublished / draft / not buyable.
- [ ] If several drafts: do not guess. Local note `several_drafts`. Stop.
- [ ] If already published: **do not unpublish from an agent**. Local note
      `already_published`. Stop. A human decides later.
- [ ] If no matching draft: local note `sku0_live_draft_missing`. Stop.
      Do **not** click **New product**.

Permalink: keep local as `{{GUMROAD_PERMALINK_SKU0}}`. Do not paste a real
`gumroad.com/l/...` into git.

SKU-0 pack files are **not in this repo**. Compare against the in-repo shape
only: *starter intake — form → table → notify*, unpublished. Do not invent a
listing title to paste.

---

## 2. Title / name (look only)

Do not rename. No SKU-0 listing paste exists in git.

- [ ] Name is filled (not blank).
- [ ] Name describes starter intake (form → table → notify), **not** SKU-1
      classifier, SKU-2 approval gate, or SKU-3 sheet sync.
- [ ] Name is not keyword-stuffed (`n8n AI agent xAI Grok official partner`).
- [ ] Name does not claim n8n / Gumroad / lab partnership.
- [ ] Name does not say “on sale”, “live”, or include a public product URL.

Local only: `present` / `blank` / `mismatch`. Do not commit the live name.

---

## 3. Price (look only)

Help: a product may be free or up to USD 5,000. A `+` after a minimum is
pay-what-you-want. Do not freeze a fee % in git.

- [ ] If a number is already on the draft, **leave it**.
- [ ] Do not “fix” it to $0 to test checkout. Do not publish at $0.
- [ ] Pay-what-you-want (`+`) is **off** unless a later human pack says otherwise.
- [ ] Compare-at / strikethrough empty (no fake discount).
- [ ] Max purchase count empty (no fake scarcity).
- [ ] No extra paid versions (one digital SKU).
- [ ] No second checkout currency invented. JPY, if any, is display copy only.

Token (owning pack missing): `{{PRICE_USD_SKU0}}`. Do not commit a filled USD
or JPY amount.

---

## 4. Icons — cover and thumbnail (look only)

Help: https://gumroad.com/help/article/60-adding-a-cover-image

Covers advertise the product (PNG, JPEG, MOV, GIF, or a YouTube/Vimeo link).
Up to 8 covers. Not a PDF. Thumbnails are separate; if used, help says at least
600 × 600 px.

- [ ] Cover: **look only**. Do not upload.
- [ ] Thumbnail: **look only**. Do not upload.
- [ ] Empty cover / thumbnail is an **allowed gap**. Local note `cover_missing`
      / `thumbnail_missing`. Do not fill with the n8n logo or any partner mark.
- [ ] If a cover **is** present: original (or clearly licensed), not an n8n /
      Gumroad / lab logo used as a partner badge.
- [ ] Filename has no secret (no email, invoice, ID).
- [ ] Do not embed a private Drive / Sheets URL as a cover.

---

## 5. Still unpublished — then STOP

- [ ] Product status still unpublished / draft.
- [ ] Custom permalink not treated as live. No X / note / BOOTH / profile
      “now on sale” post.
- [ ] Files / Content tab **not opened** on this card.
- [ ] Payout settings were not opened, or were closed without saving.
- [ ] **STOP.** Next CU is **not** Gumroad. Desk stays `draft_saved`.

---

## Out of scope (never this card)

- Content-tab files (use [PR#55](https://github.com/rimone0511/autopilot-log/pull/55) later)
- New product / duplicate SKU-0
- SKU-1 / SKU-2 / SKU-3 live create or publish
- Buyer-zip authoring (SKU-0 pack is missing)
- Rename, reprice, upload cover/thumbnail
- Payout, Stripe KYC, PayPal bank, W-9, My Number
- Gumroad API create/enable (`draft=true` / `POST .../enable` included)

Sibling paste packs (not this look-target):

| SKU | Path (on that PR branch, not `master`) | PR |
|---|---|---|
| SKU-1 n8n inquiry classifier | `earn-sku1-n8n-pack-draft-20260916/` | [#37](https://github.com/rimone0511/autopilot-log/pull/37) |
| SKU-2 n8n approval-gated notify | `earn-sku2-approval-gate-pack-draft-20260916/` | [#46](https://github.com/rimone0511/autopilot-log/pull/46) |
| SKU-3 n8n Google Sheet sync | `earn-sku3-sheet-sync-pack-draft-20260916/` | [#52](https://github.com/rimone0511/autopilot-log/pull/52) |

---

## Local observation (do not commit filled)

```
date_jst:
operator: parent
sku0_live_draft: yes / no / not_checked
title: present / blank / mismatch
{{GUMROAD_PERMALINK_SKU0}}:
{{PRICE_USD_SKU0}}:
pwyw: off / on / not_checked
cover: present / missing / mismatch / not_checked
thumbnail: present / missing / n/a / not_checked
stopped_at: unpublished | payout_screen | already_published | missing_draft | several_drafts
publish_clicked: no
```

---

## Official help (public)

- Adding a product: https://gumroad.com/help/article/149-adding-a-product
- Cover and thumbnail: https://gumroad.com/help/article/60-adding-a-cover-image
- Getting paid (read only; do not set up): https://gumroad.com/help/article/13-getting-paid

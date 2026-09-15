# OPERATOR-CARD — Gumroad SKU-0 Publish GO (2 minutes)

Pack date: 2026-09-16
Audience: **parent operator only** (祐太). Not computer-use. **Two minutes.**
Desk: Gumroad (Wave A+). Queue `done-draft`. CU hint `draft_saved`. Does not occupy CU-11.
SKU: **SKU-0** — starter intake (form → table → notify)
Mode: **DRAFT_ONLY. Default GO = NO. Do not ship. Do not set up payout.**
After: listing polish [#74](https://github.com/rimone0511/autopilot-log/pull/74)

This card is a 2-minute **GO / NO-GO** look at an **already unpublished** digital
product. It is not a Gumroad product, not a buyer zip, not listing paste, and not
a payout / KYC run.

Listing copy lives on the sibling JOBS pack
[`earn-jobs-gumroad-sku0-listing-polish-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/gumroad-sku0-listing-polish-56b2/earn-jobs-gumroad-sku0-listing-polish-20260916)
([PR#74](https://github.com/rimone0511/autopilot-log/pull/74)). Do not re-paste
from this card. Do not treat that pack’s checklist turning green as Publish.

Google: MAIN only (`{{GOOGLE_ACCOUNT_EMAIL}}`). Do not create a second Gumroad.

---

## Default (read this first)

**GO = NO.**

This card never emits YES. Files attached, price $39, and “looks ready” do not
flip it. An unpaid draft stays unpublished. A later human pack — not this one —
would be required before anyone clicks Publish.

Tick boxes on a **local** copy. Do not commit a filled live title, a filled
`$39` ledger, a file name that contains a secret, or a `gumroad.com/l/...` URL.

---

## Clock (2:00 then stop)

| Min | Look | Do not |
|---|---|---|
| 0:00–0:20 | Hard stop. Find **one** unpublished SKU-0-shaped draft. Default = **NO** | New product. Publish / Enable. Payout |
| 0:20–0:50 | **Files** (Content tab): attached? buyer zip, not operator files | Upload. Download secrets. Attach SKU-1/2/3 |
| 0:50–1:20 | **Price $39**, PWYW off, not $0 | Change the number. $0 “to test”. Commit USD/JPY |
| 1:20–1:50 | **Unpaid draft**: still unpublished; payout not this pass | Open bank / tax / ID. Announce a URL |
| 1:50–2:00 | Local GO = **NO**. Still unpublished. **STOP** | Publish even if files + $39 look green |

---

## 0. Hard stop (read before opening Gumroad)

- [ ] This pass is a **GO check**. Default is **do not publish**.
- [ ] CU does **not** open Gumroad from this card. Parent only.
- [ ] Do not click **Publish**, **Enable**, **Unpause**, or any go-live control.
- [ ] Do not type or announce a live `gumroad.com/l/...` URL. None is in git.
- [ ] Do not open Payout / Payments / bank / tax / ID upload.
- [ ] Do not buy Discover, boosts, or a custom domain.
- [ ] Do not upload a cover, thumbnail, or buyer zip from this card.
- [ ] Do not create a product if none exists.

If a payout or identity screen appears: close it. Local note
`payout_screen_appeared`. Stop. GO stays **NO**.

Public entry (desk, not a product URL): https://gumroad.com/
Help (product editor): https://gumroad.com/help/article/149-adding-a-product

---

## 1. Find the existing unpublished SKU (do not create)

- [ ] Logged in as MAIN Google (queue already `done-draft`).
- [ ] Open the **products** list (live menu label is the source of truth).
- [ ] Locate **one** unpublished digital product that matches SKU-0 shape
      (starter intake: form → table → notify).
- [ ] Confirm unpublished / draft / not buyable. That is the **unpaid draft**.
- [ ] If several drafts: do not guess. Local note `several_drafts`. Stop. GO = **NO**.
- [ ] If already published: **do not unpublish from an agent**. Local note
      `already_published`. Stop. A human decides later. GO = **NO**.
- [ ] If no matching draft: local note `sku0_live_draft_missing`. Stop.
      Do **not** click **New product**. GO = **NO**.

Permalink: keep local as `{{GUMROAD_PERMALINK_SKU0}}`. Do not paste a real
`gumroad.com/l/...` into git.

Name shape (from polish pack, look only — do not rename here):
`n8n Starter Intake Pack — form to table, human notify` (EN) /
`n8n 受付スターター — フォームから表へ、通知は人` (JA).

---

## 2. Files — Content tab (look; 0:20–0:50)

Help: product **Content** tab holds the downloadable files.
https://gumroad.com/help/article/149-adding-a-product

This JOBS pack does **not** author or attach the buyer zip. Expected *shape*:

- intake form → table → notify
- secrets out of the zip
- send stays human
- stubs inactive (`active: false` / Inactive)

Look / require before any later human Publish (still not this card):

- [ ] Content tab opened. Nothing uploaded from this pass.
- [ ] **Files attached** (look-target for this GO card). If **no files**:
      ship-blocker. Local note `content_files_missing`. GO stays **NO**.
- [ ] Files look like a **buyer** zip/stubs, not operator files
      (`LISTING-*.md`, `FAQ-*.md`, `DRAFT_ONLY.md`, `PRICING.md`,
      `CHECKLIST.md`, `OPERATOR-CARD.md`, `GO.md`, pack README, `STATUS.md`,
      KYC slips).
- [ ] No credential files with filled secrets, `.env`, key JSON, or tax PDFs.
- [ ] No n8n workflow left `active: true`. If you cannot tell without
      downloading, do not download secrets into an agent workspace. A human
      opens the zip locally. Local note `files_need_human_open`.
- [ ] SKU-1 / SKU-2 / SKU-3 stubs are **not** attached to SKU-0.
- [ ] Versions: leave off (one digital SKU).

Files attached **does not** mean Publish. Cover / thumbnail may still be empty
(warning on [#74](https://github.com/rimone0511/autopilot-log/pull/74); not an
upload excuse here).

---

## 3. Price $39 (look; 0:50–1:20)

Help: a product may be free or up to USD 5,000. A `+` after a minimum is
pay-what-you-want. Do not freeze a fee % in git.

Look-target for this GO card: **$39** already on the draft (polish rule:
keep $39 if set). See [#74 `PRICING.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/gumroad-sku0-listing-polish-56b2/earn-jobs-gumroad-sku0-listing-polish-20260916/PRICING.md).

- [ ] Draft shows **$39** USD with PWYW **off**. **Leave it.** Do not “optimize”.
- [ ] If empty / token / other number: do not invent a new fee in git.
      Local note `price_not_39`. GO stays **NO**. Do not type a filled
      `{{PRICE}}` into this repo.
- [ ] Price is **not** $0. Do not publish at $0 to test checkout.
- [ ] Pay-what-you-want (`+`) is **off**.
- [ ] Compare-at / strikethrough empty (no fake discount).
- [ ] Max purchase count empty (no fake scarcity).
- [ ] No extra paid versions (one digital SKU).
- [ ] No second checkout currency invented. JPY, if any, is display copy only.

$39 on an **unpaid** draft is still not a live sale.

---

## 4. Unpaid draft (look; 1:20–1:50)

**Unpaid draft** on this card means all of:

1. Product is still **unpublished** / not buyable.
2. No payout method is set up **from this pass** (and this pass must not set one).
3. No live sale is treated as having happened. Do not invent GMV.

Getting paid is a **separate human** path. Help (read only; do not set up):
https://gumroad.com/help/article/13-getting-paid

- [ ] Status still unpublished / draft / not buyable.
- [ ] Do **not** open Payout / Payments / bank / tax / ID to “confirm unpaid”.
      Unpaid is the desk default until a later human pack owns payout.
- [ ] If a payout screen appears anyway: close it. Local note
      `payout_screen_appeared`. GO = **NO**.
- [ ] Discover / profile visibility **not** turned on from this pass.
- [ ] Custom permalink not treated as live. No X / note / BOOTH / profile
      “now on sale” post.
- [ ] Do not buy Discover, boosts, or a custom domain.

Publishing a $39 product with no payout is still **NO** on this card.
Setting up payout so it *could* be paid is also **NO** on this card.

---

## 5. Verdict — then STOP (1:50–2:00)

Copy the local block in [GO.md](GO.md). Do not commit filled values.

- [ ] Three looks recorded locally: files / $39 / unpaid draft.
- [ ] **GO = NO** written. This card has no YES line.
- [ ] Product status still unpublished / draft.
- [ ] Payout settings were not opened, or were closed without saving.
- [ ] **STOP.** Next CU is **not** Gumroad. Desk stays `draft_saved`.

A later human Publish is allowed only after a **separate** pack says so, every
ship-blocker is green, **and** a human (not an agent) owns the click. This
folder is not that pack.

---

## Out of scope (never this card)

- Click Publish / Enable / Unpause (including “checklist is green”)
- New product / duplicate SKU-0
- Re-paste listing / FAQ (use [PR#74](https://github.com/rimone0511/autopilot-log/pull/74))
- Title / price / icons-only look (use [PR#63](https://github.com/rimone0511/autopilot-log/pull/63))
- Full QA including empty-cover policy (use [PR#55](https://github.com/rimone0511/autopilot-log/pull/55))
- SKU-1 / SKU-2 / SKU-3 live create or publish
- Buyer-zip authoring or Content-tab upload
- Rename, reprice, upload cover/thumbnail
- Payout, Stripe KYC, PayPal bank, W-9, My Number
- Gumroad API create/enable (`draft=true` / `POST .../enable` included)

Sibling paste packs (not this GO target):

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
files_attached: yes / no / not_checked
files_look_buyer: yes / no / not_checked / files_need_human_open
price_39: yes / no / not_checked
pwyw: off / on / not_checked
unpaid_draft: yes / no / not_checked
{{GUMROAD_PERMALINK_SKU0}}:
stopped_at: unpublished | payout_screen | already_published | missing_draft | several_drafts
publish_clicked: no
GO: NO
```

---

## Official help (public)

- Adding a product: https://gumroad.com/help/article/149-adding-a-product
- Cover and thumbnail: https://gumroad.com/help/article/60-adding-a-cover-image
- Getting paid (read only; do not set up): https://gumroad.com/help/article/13-getting-paid

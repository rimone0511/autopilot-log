# CHECKLIST — unpublished SKU-0 (look-don't-ship)

Pack date: 2026-09-16  
Desk: Gumroad  
SKU: **SKU-0** — starter intake (form → table → notify)  
Mode: **DRAFT_ONLY. Look. Do not ship. Do not set up payout.**

Use this list on the **already unpublished** digital product, if one exists in the
logged-in Gumroad products list. Tick boxes on a **local** copy. Do not commit a
filled live title, price, file name that contains a secret, or a `gumroad.com/l/...`
URL.

If no unpublished product is on the products list, stop. Record that in
[GAPS.md](GAPS.md). Do **not** click **New product** from this pack.

SKU-0 pack files are **not in this repo**. There is no listing paste to copy from.
Compare the live draft against the in-repo shape only: *starter intake — form →
table → notify*, unpublished. See [README.md](README.md).

---

## 0. Hard stop (read before opening Gumroad)

- [ ] This pass is **look-don't-ship**. Unpublished stays unpublished.
- [ ] Do not click **Publish**, **Enable**, **Unpause**, or any go-live control.
- [ ] Do not type or announce a live `gumroad.com/l/...` URL. None is in git.
- [ ] Do not open Payout / Payments / bank / tax / ID upload. Not this pack.
- [ ] Do not buy Discover, boosts, or a custom domain.
- [ ] Do not attach a buyer zip, cover, or thumbnail from an agent session.
- [ ] Do not create a second Gumroad account.
- [ ] MAIN Google only (`{{GOOGLE_ACCOUNT_EMAIL}}`). Queue already `done-draft`.

If a payout or identity screen appears, close it. Leave a row in [GAPS.md](GAPS.md)
(`payout_screen_appeared`) and stop.

---

## 1. Find the existing unpublished SKU (do not create)

Public entry (desk, not a product URL): https://gumroad.com/

Help (product editor): https://gumroad.com/help/article/149-adding-a-product

- [ ] Logged in as MAIN Google (already `done-draft` on the 2026-09-16 queue).
- [ ] Open the **products** list (live menu label is the source of truth).
- [ ] Locate **one** unpublished digital product that matches SKU-0 shape
      (starter intake: form → table → notify). If several drafts exist, do not
      guess — list them as gaps and stop.
- [ ] Confirm the row / editor shows **unpublished** / draft / not buyable.
- [ ] If the product is already published: **do not unpublish from an agent**.
      Record `already_published` in [GAPS.md](GAPS.md) and stop. A human decides.
- [ ] If no matching draft exists: record `sku0_live_draft_missing` and stop.
      Do not create one from this checklist.

Permalink: keep local as `{{GUMROAD_PERMALINK_SKU0}}`. Do not paste a real
`gumroad.com/l/...` into git.

---

## 2. Title / name

Look at the product **name** field. Do not rename unless a later human pack
supplies listing paste (none exists for SKU-0 in this repo).

- [ ] Name is filled (not blank).
- [ ] Name describes starter intake (form → table → notify), not SKU-1 classifier,
      SKU-2 approval gate, or SKU-3 sheet sync.
- [ ] Name is not keyword-stuffed (`n8n AI agent xAI Grok official partner`).
- [ ] Name does not claim n8n / Gumroad / lab partnership.
- [ ] Name does not say “on sale”, “live”, or include a public product URL.
- [ ] Character count noted locally (Gumroad live limit is the form; do not invent
      a ceiling in git).

Write the **observed** name only on a local note. In [GAPS.md](GAPS.md) use
`present` / `blank` / `mismatch` — not the live string, unless it is already
public and non-secret (still prefer not to commit a title that might ship).

---

## 3. Price

Help: a product may be free or up to USD 5,000. A `+` after a minimum is
pay-what-you-want. Do not freeze a fee % in git.

- [ ] Price box is not treated as a live market decision in this pass.
- [ ] If a number is already on the draft, **leave it**. Do not “fix” it to $0
      to test checkout. Do not publish at $0.
- [ ] Pay-what-you-want (`+`) is **off** unless a later human pack says otherwise.
- [ ] Compare-at / strikethrough is empty (no fake discount).
- [ ] Max purchase count is empty (no fake scarcity).
- [ ] Versions / extra paid tiers: none expected for this SKU (one digital download).
- [ ] No second checkout currency invented. JPY, if any, is display copy only.

In-repo price token (pack missing): `{{PRICE_USD_SKU0}}`. Do not commit a filled
USD or JPY amount.

---

## 4. Icons — cover and thumbnail

Help: https://gumroad.com/help/article/60-adding-a-cover-image

Covers advertise the product (PNG, JPEG, MOV, GIF, or a YouTube/Vimeo link). Up
to 8 covers. Not a PDF. Image covers must stay under the live size limit (help:
50 MB after processing). Thumbnails are separate; if used, help says at least
600 × 600 px. They show in the customer library, Discover, and the profile.

- [ ] Cover: **look only**. Do not upload from this pack.
- [ ] Thumbnail: **look only**. Do not upload from this pack.
- [ ] If covers / thumbnail are empty: that is an allowed gap. SKU-1 listing
      paste says skip cover until original images exist. Record `cover_missing`
      / `thumbnail_missing` in [GAPS.md](GAPS.md). Do not fill with the n8n logo
      or any partner mark.
- [ ] If a cover **is** present: confirm it is original (or clearly licensed),
      not an n8n / Gumroad / lab logo used as a partner badge.
- [ ] Filename has no secret (no email, invoice, ID). Help also warns against
      `# $ _ + & ; : %` in cover filenames — note a bad name in GAPS; do not
      rename from an agent session.
- [ ] Do not embed a private Drive / Sheets URL as a cover.

---

## 5. Files — Content tab

Help: product **Content** tab holds the downloadable files (and optional folders).
https://gumroad.com/help/article/149-adding-a-product

SKU-0 buyer zip is **not in this repo**. Expected *shape* (from SKU-1’s description
of the predecessor), not a file list to invent:

- intake form → table → notify
- secrets out of the zip
- send stays human

Look:

- [ ] Content tab opened. Nothing uploaded from this pass.
- [ ] If **no files**: record `content_files_missing`. That is a ship-blocker
      for a later human, not a reason to publish or to attach stubs now.
- [ ] If files **are** present, check they look like a **buyer** zip/stubs, not
      operator files (`LISTING-*.md`, `DRAFT_ONLY.md`, `PRICING.md`, pack README,
      KYC slips).
- [ ] No credential files with filled secrets, `.env`, key JSON, or tax PDFs.
- [ ] No n8n workflow left `active: true` if JSON stubs are attached (inactive
      only). If you cannot tell without downloading, record `files_need_human_open`
      and do not download secrets into the agent workspace.
- [ ] Folders: optional. Do not restructure from this pack.
- [ ] Versions: leave off (one digital SKU).

Do not attach SKU-1 / SKU-2 / SKU-3 stubs to SKU-0.

---

## 6. Confirm still unpublished (end of look)

- [ ] Product status still unpublished / draft.
- [ ] Custom permalink not treated as live. No X / note / BOOTH / profile “now
      on sale” post.
- [ ] Discover / profile visibility not turned on from this pass (live labels
      are the source of truth; do not invent the control name).
- [ ] Payout settings were **not** opened, or were closed without saving.
- [ ] Gaps copied into [GAPS.md](GAPS.md) (template only in git; live strings
      stay local if they include a URL or price).
- [ ] **STOP.**

---

## 7. Out of scope (never this pack)

- New product / duplicate SKU-0
- SKU-1 / SKU-2 / SKU-3 live create or publish
- Buyer-zip authoring (that is a future SKU-0 pack, currently missing)
- n8n hosting, partner applications, Zapier/Make badges
- Payout, Stripe KYC, PayPal bank, W-9, My Number
- Gumroad API create/enable (`draft=true` / `POST .../enable` included)

---

## Official help used

- Adding a product: https://gumroad.com/help/article/149-adding-a-product
- Cover and thumbnail: https://gumroad.com/help/article/60-adding-a-cover-image
- Getting paid (do not set up): https://gumroad.com/help/article/13-getting-paid

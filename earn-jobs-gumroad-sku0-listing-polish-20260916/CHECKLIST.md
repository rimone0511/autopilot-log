# CHECKLIST — before Publish (SKU-0) — still DRAFT_ONLY

Pack date: 2026-09-16
Phase: JOBS
Desk: Gumroad
SKU: **SKU-0** — starter intake (form → table → notify)
Mode: **DRAFT_ONLY. This list is the gate before a later human Publish. This pack does not publish.**

Tick boxes on a **local** copy. Do not commit a filled live title, a filled
`{{PRICE}}`, a file name that contains a secret, or a `gumroad.com/l/...` URL.

If no unpublished product is on the products list, stop. Do **not** click
**New product** from this pack.

Paste sources: [LISTING-EN.md](LISTING-EN.md), [LISTING-JA.md](LISTING-JA.md),
[FAQ-EN.md](FAQ-EN.md), [FAQ-JA.md](FAQ-JA.md), [PRICING.md](PRICING.md).

---

## 0. Hard stop (read before opening Gumroad)

- [ ] This pass may **paste** into an unpublished draft. It may **not** Publish.
- [ ] Do not click **Publish**, **Enable**, **Unpause**, or any go-live control.
- [ ] Do not type or announce a live `gumroad.com/l/...` URL. None is in git.
- [ ] Do not open Payout / Payments / bank / tax / ID upload. Not this pack.
- [ ] Do not buy Discover, boosts, or a custom domain.
- [ ] Do not attach a buyer zip, cover, or thumbnail from an agent session.
- [ ] Do not create a second Gumroad account.
- [ ] MAIN Google only (`{{GOOGLE_ACCOUNT_EMAIL}}`). Queue already `done-draft`.

If a payout or identity screen appears, close it. Stop. See [DRAFT_ONLY.md](DRAFT_ONLY.md).

A later human Publish is allowed only after **every ship-blocker below is green**.
Green on this list is **not** permission for an agent to click Publish.

---

## 1. Find the existing unpublished SKU (do not create)

Public entry (desk, not a product URL): https://gumroad.com/

Help (product editor): https://gumroad.com/help/article/149-adding-a-product

- [ ] Logged in as MAIN Google (already `done-draft` on the 2026-09-16 queue).
- [ ] Open the **products** list (live menu label is the source of truth).
- [ ] Locate **one** unpublished digital product that matches SKU-0 shape
      (starter intake: form → table → notify). If several drafts exist, do not
      guess — stop and pick with a human.
- [ ] Confirm the row / editor shows **unpublished** / draft / not buyable.
- [ ] If the product is already published: **do not unpublish from an agent**.
      Stop. A human decides.
- [ ] If no matching draft exists: stop. Do not create one from this checklist.

Permalink: keep local as `{{GUMROAD_PERMALINK_SKU0}}`. Do not paste a real
`gumroad.com/l/...` into git.

---

## 2. Name / summary / description / FAQ

- [ ] Name pasted from [LISTING-EN.md](LISTING-EN.md) and/or [LISTING-JA.md](LISTING-JA.md)
      (EN 53 characters / JA 27 字 — re-count if you edit).
- [ ] Name describes starter intake (form → table → notify), not SKU-1 / SKU-2 / SKU-3.
- [ ] Name is not keyword-stuffed and does not claim partnership.
- [ ] Name does not say “on sale”, “live”, or include a public product URL.
- [ ] CTA is a built-in buy/download control (suggested: **I want this!**). Not Donate.
- [ ] Summary pasted (EN 95 characters / JA 45 字 — re-count if you edit).
- [ ] Description pasted. Buyer-facing. No “unpublished draft” sentence in the box.
- [ ] FAQ pasted from [FAQ-EN.md](FAQ-EN.md) and/or [FAQ-JA.md](FAQ-JA.md) at the
      end of the description (no separate FAQ field on the standard form).
- [ ] Affiliation sentence present (independent seller; not n8n / Gumroad / AI-lab partner).
- [ ] Additional details match listing section 5 (or left empty on purpose).
- [ ] Tags, if shown: n8n / automation / workflow / intake — no fake partner tags.

---

## 3. Price (keep $39 or `{{PRICE}}`)

Help: a product may be free or up to USD 5,000. A `+` after a minimum is
pay-what-you-want. Do not freeze a fee % in git.

- [ ] If the draft already shows **$39** USD with PWYW **off**: **keep it**.
- [ ] If the price box is empty: type a local number from `{{PRICE}}`. Do not commit it.
- [ ] Price is **not** $0. Do not publish at $0 to test checkout.
- [ ] Pay-what-you-want (`+`) is **off** unless a later human pack says otherwise.
- [ ] Compare-at / strikethrough is empty (no fake discount).
- [ ] Max purchase count is empty (no fake scarcity).
- [ ] Versions / extra paid tiers: none (one digital download).
- [ ] No second checkout currency invented. JPY, if any, is `{{PRICE_JPY_DISPLAY}}` copy only.

See [PRICING.md](PRICING.md).

---

## 4. Cover / thumbnail (do not upload from this pack)

Help: https://gumroad.com/help/article/60-adding-a-cover-image

- [ ] Cover: original or clearly licensed, **or** still empty.
- [ ] Thumbnail: original or clearly licensed, **or** still empty.
- [ ] Empty cover / thumbnail: **warning**, not an agent-upload excuse. A human
      decides whether empty art blocks Publish. Do not fill with the n8n logo
      or any partner mark.
- [ ] If present: not an n8n / Gumroad / lab logo used as a partner badge.
- [ ] Filename has no secret (no email, invoice, ID). Help also warns against
      `# $ _ + & ; : %` in cover filenames.
- [ ] Do not embed a private Drive / Sheets URL as a cover.

---

## 5. Content tab — **ship-blocker until files exist**

Help: product **Content** tab holds the downloadable files.
https://gumroad.com/help/article/149-adding-a-product

This JOBS pack does **not** author the buyer zip. Expected *shape*:

- intake form → table → notify
- secrets out of the zip
- send stays human
- stubs inactive (`active: false` / Inactive)

Look / require before any later Publish:

- [ ] Content tab opened. Nothing uploaded from this agent pass.
- [ ] **Ship-blocker:** buyer files are attached (README + placeholder credentials
      + inactive intake/table/notify stubs). If **no files**: do not Publish.
      Record locally; a separate pack authors the zip.
- [ ] Files look like a **buyer** zip/stubs, not operator files (`LISTING-*.md`,
      `FAQ-*.md`, `DRAFT_ONLY.md`, `PRICING.md`, `CHECKLIST.md`, pack README,
      `STATUS.md`, KYC slips).
- [ ] No credential files with filled secrets, `.env`, key JSON, or tax PDFs.
- [ ] No n8n workflow left `active: true`. If you cannot tell without downloading,
      do not download secrets into an agent workspace. A human opens the zip locally.
- [ ] SKU-1 / SKU-2 / SKU-3 stubs are **not** attached to SKU-0.
- [ ] Versions: leave off (one digital SKU).

---

## 6. Refund / Discover / permalink (human fields)

- [ ] Refund policy field: filled by a human locally, or left as Gumroad default
      on purpose. Do not invent “30-day no questions” in git.
- [ ] Discover / profile visibility **not** turned on from this pass.
- [ ] Custom permalink not treated as live. No X / note / BOOTH / profile “now on sale” post.
- [ ] Integrations (Circle / Discord): off unless a human later owns that community.

---

## 7. Confirm still unpublished (end of pass)

- [ ] Product status still unpublished / draft / not buyable.
- [ ] Payout settings were **not** opened, or were closed without saving.
- [ ] Ship-blockers reviewed: Content files, not $0, not already published, not a partner-logo cover.
- [ ] **STOP.** Do not click Publish from this pack.

---

## 8. Out of scope (never this pack)

- New product / duplicate SKU-0
- SKU-1 / SKU-2 / SKU-3 live create or publish
- Buyer-zip authoring (separate pack)
- n8n hosting, partner applications, Zapier/Make badges
- Payout, Stripe KYC, PayPal bank, W-9, My Number
- Gumroad API create/enable (`draft=true` / `POST .../enable` included)
- Agent click of **Publish** / **Enable** even if this checklist is all green

---

## Official help used

- Adding a product: https://gumroad.com/help/article/149-adding-a-product
- Cover and thumbnail: https://gumroad.com/help/article/60-adding-a-cover-image
- Getting paid (do not set up): https://gumroad.com/help/article/13-getting-paid

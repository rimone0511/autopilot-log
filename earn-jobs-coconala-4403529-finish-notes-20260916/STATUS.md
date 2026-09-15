# STATUS — Coconala service 4403529 (unpublished draft)

Snapshot: **2026-09-16**  
Folder: `earn-jobs-coconala-4403529-finish-notes-20260916/`  
State: **DRAFT_ONLY**  
Source: operator-supplied live draft fields + public GET. **No Coconala login. No 公開する. No 見積もり送信.**

Forbidden in this file: passwords, API keys, OTP, KYC, emails, customer bodies, cover binaries.

---

## Verdict

| Item | Status |
|---|---|
| This finish-note pack | **ready · draft** (markdown only) |
| Live CU / seller login from this agent | **not run** |
| Listing public | **no** |
| HUMAN-GO `coconala_publish_listing` | **false** |
| Ready to click 公開する | **no** (`image_missing` + GO closed) |

Hint for the desk box: **`unpublished` + `image_missing`**. Not `publish_ready_unpublished`. Not `already_published`.

---

## Recorded live draft (operator)

Seller-dashboard service id **4403529**. Treat as an unpublished draft id, not a shop URL to share.

| Field | Observed | Note |
|---|---|---|
| Visibility | **unpublished** | Guest GET 404. Do not post the URL as if live |
| Kind | 通常サービス (assumed from #79 `01`; live form wins) | Do not switch to 電話 / ビデオチャット |
| Title field (canonical) | `n8n自動化と手順書を作ります` (15) | UI may display doubled ます — [TITLE-FIX.md](TITLE-FIX.md) |
| FAQ count | **6** | Do not pad to 7 from this note |
| FAQ 6 | **fixed (スクレイピング)** | Keep scraping / browser-bot as **out of scope**. Do not revert slot 6 to a revisions-only answer if that drops the scraping line |
| Price (form) | **10000** | Unpublished draft observation. Not a market fact. Paste packs still use `{{PRICE_YEN}}` |
| 見積もり・カスタマイズ | **ON** | 受付する ≠ 見積もりを送る |
| Images | **`image_missing`** | Cover not attached. GO-blocker ([PR#90](https://github.com/rimone0511/autopilot-log/pull/90) news 1372: ≥1 image at 公開) |
| 下書き保存 | assumed already saved | This agent did not click save |
| 公開する clicked | **no** (this record) | Leave that way |

Success line for this pass (secret-free):

```
desk: Coconala
pack: earn-jobs-coconala-4403529-finish-notes-20260916/
listing_id_in_git: 4403529
listing: unpublished
public_get: 404
first_gig_source: PR79-01-same-family
fields: operator-recorded
title_canonical: n8n自動化と手順書を作ります
title_ui_double_masu: possible — fix on edit
faq: 6
faq_6: scraping-fixed
price_form_yen_observed: 10000
estimate_accept: on
estimate_sent: no
images: image_missing
cover_attached: no
publish_clicked: no
kyc_opened: no
human_go_coconala_publish_listing: false
cu_this_agent: not-run
next: attach-cover-then-human-go
```

---

## Price observation (not a paste instruction)

`10000` was already on the unpublished form. This pack does **not** retune it.

Sibling [#91](https://github.com/rimone0511/autopilot-log/pull/91) 01 bands are **DRAFT SUGGESTIONS, not 相場**. Floor snapshot there for 業務自動化・効率化支援 was 3000 (re-read live help before any later edit). `10000` clears that snapshot floor. Do not invent a new yen in git.

---

## FAQ 6 (スクレイピング) — already fixed

Do not copy sibling FAQ fences into this folder.

Intent of the live slot-6 fix: buyer-facing text must say this offer does **not** do スクレイピング / ブラウザ自動操作 / いいね・フォロー・閲覧代行. Official API + webhook only.

If the form is reopened:

- Keep FAQ 6 as the scraping / browser-bot refusal (or an equivalent that still names スクレイピング).
- [#79](https://github.com/rimone0511/autopilot-log/pull/79) `01` Q6 was 修正と追加作業. Do not paste that older Q6 over the fix.
- [#87](https://github.com/rimone0511/autopilot-log/pull/87) names スクレイピング in Q4 and in サービス内容. That is the policy; this listing’s live FAQ **6** is the slot that was corrected.

---

## Public GET (this authoring session)

| URL | HTTP | Note |
|---|---|---|
| https://coconala.com/services/4403529 | **404** | Guest. Matches unpublished. Do not treat as a shop page |
| https://coconala.com/pages/guide_sell | 200 | 出品ガイド (image step + 公開). Not a login |

**POST / login / CU: none.**

---

## Complement (do not copy bodies)

| PR | Relation |
|---|---|
| [#79](https://github.com/rimone0511/autopilot-log/pull/79) | Listing `01` title + estimate ON. Same family |
| [#87](https://github.com/rimone0511/autopilot-log/pull/87) | First-gig paste / ます auto-append / scraping in body+Q4 |
| [#90](https://github.com/rimone0511/autopilot-log/pull/90) | Publish-ready checklist. `images_missing` is a GO-blocker |
| [#91](https://github.com/rimone0511/autopilot-log/pull/91) | Local `{{PRICE_YEN}}` card. Not a second listing |
| [#81](https://github.com/rimone0511/autopilot-log/pull/81) | Inquiry replies. Do not send from this pack |

Do not dual-list #79 `02` / `03` from this finish note.

---

## Next

See [OPERATOR-NEXT.md](OPERATOR-NEXT.md). [HUMAN-GO.md](HUMAN-GO.md) stays **false**.

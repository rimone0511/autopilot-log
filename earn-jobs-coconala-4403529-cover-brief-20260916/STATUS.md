# STATUS — Coconala 4403529 cover brief

Snapshot: **2026-09-16** (~06:35 JST patrol + this pack)  
Folder: `earn-jobs-coconala-4403529-cover-brief-20260916/`  
Desk: 仕事窓口  
State: **DRAFT_ONLY**  
Source: operator / sibling finish notes + public news. **No Coconala login. No live CU. No 公開する.**

Forbidden in this file: passwords, API keys, OTP, KYC, emails, customer bodies, cover binaries.

---

## Verdict

| Item | Status |
|---|---|
| This cover-brief pack | **ready · draft** (markdown + SVG mock) |
| Live CU / seller login from this agent | **not run** |
| Listing public | **no** |
| Cover binary produced / uploaded | **no** (brief only) |
| HUMAN-GO `coconala_publish_listing` | **false** |
| Ready to click 公開する | **no** (`image_missing` + GO closed) |

Hint for the desk box: **`unpublished` + `image_missing`**. Cover pack delivered. Upload is a **later** human/CU under [PASTE-CHECKLIST.md](PASTE-CHECKLIST.md). Not `publish_ready_unpublished`. Not `already_published`.

---

## Recorded live draft (operator / sibling)

Seller-dashboard service id **4403529**. Treat as an unpublished draft id, not a shop URL to share.

| Field | Observed | Note |
|---|---|---|
| Visibility | **unpublished** | Guest GET 404 on sibling [#103](https://github.com/rimone0511/autopilot-log/pull/103). Do not post the URL as if live |
| Kind | 通常サービス (first-gig family) | Do not switch to 電話 / ビデオチャット |
| Title field (canonical) | `n8n自動化と手順書を作ります` | Overlay titles in COVER-BRIEF are **image-only** |
| FAQ | **done** | 6 pairs; slot 6 スクレイピング out of scope. Do not rewrite here |
| Images | **`image_missing`** | This pack’s gap. news 1372: ≥1 image at 公開 |
| 見積もり・カスタマイズ | ON（受付する） | ≠ 見積もりを送る |
| 公開する clicked | **no** | Leave that way |

Success line for this authoring pass (secret-free):

```
desk: Coconala
owner: 仕事窓口
pack: earn-jobs-coconala-4403529-cover-brief-20260916/
listing_id_in_git: 4403529
listing: unpublished
patrol: 2026-09-16~06:35JST
first_gig_source: PR79-01-same-family
faq: done
images: image_missing
cover_brief: ready
cover_overlay_recommended: n8n受付と手順書
cover_attached: no
publish_clicked: no
estimate_sent: no
kyc_opened: no
wave_bd_register: no
human_go_coconala_publish_listing: false
cu_this_agent: not-run
next: human-or-later-CU-upload-then-stop
```

---

## Gate (fail closed)

Mirrors Autopilot Log posting-gate: a saved draft is not permission to go live.

```
coconala_jobs_gate:
  pack: earn-jobs-coconala-4403529-cover-brief-20260916
  listing_id: 4403529
  draft_only: true
  coconala_publish_listing: false
  coconala_send_estimate: false
  coconala_resume_accepting: false
  coconala_blog_embed: false
  coconala_sns_announce: false
  any_payout_kyc_upload: false
  wave_bd_register: false
```

If this block is missing or half-filled, treat **every row as `false`**.

Do not infer GO from: FAQ done, cover brief merged, `image_missing` later cleared, JOBS patrol time, or sibling checklists.

**This authoring agent never flips a row to `true` and never clicks 公開する.**

---

## Complement (do not copy bodies)

| PR | Relation |
|---|---|
| [#103](https://github.com/rimone0511/autopilot-log/pull/103) | Finish notes. Next = attach cover. This pack **is** that brief |
| [#79](https://github.com/rimone0511/autopilot-log/pull/79) | Listing `01` title + 受付する. Same family |
| [#87](https://github.com/rimone0511/autopilot-log/pull/87) | First-gig paste / ます / scraping |
| [#90](https://github.com/rimone0511/autopilot-log/pull/90) | Publish-ready checklist. Missing image = GO-blocker |
| [#91](https://github.com/rimone0511/autopilot-log/pull/91) | Price token card. Not a second listing |

Do not dual-list #79 `02` / `03` from this cover pack.

---

## Next

1. Human makes/export PNG from [COVER-BRIEF.md](COVER-BRIEF.md) / [cover-mock.svg](cover-mock.svg).
2. Later CU or human follows [PASTE-CHECKLIST.md](PASTE-CHECKLIST.md).
3. **下書きで保存する. STOP.**
4. 祐太 only: later GO + 公開する — not this agent.

Valid next outcomes:

- `image_missing` → `cover_attached_unpublished`, GO still false
- later, **human** `already_published` — not this agent

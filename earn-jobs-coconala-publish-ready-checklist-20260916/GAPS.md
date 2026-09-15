# GAPS — Coconala publish-ready look/fill (template)

Pack date: 2026-09-16  
Mode: **DRAFT_ONLY.** Fill a **local** copy.  
Do not commit live サービス URL, filled yen, emails, or image filenames that contain secrets.

Operator: leave rows `unchecked` until a human/CU actually opened the draft.

---

## How to fill

Use only: `present` / `blank` / `mismatch` / `missing` / `blocked` / `n/a` / `not-run`.  
Do not paste the live title string unless it is already public **and** non-secret. Prefer `present` + which first-gig file it matches (`PR79-01`).

---

## Profile (`draft_saved`)

| Item | Observed |
|---|---|
| Existing member (MAIN Google) | `not-run` |
| Profile public toggle moved this pass | `not-run` (must stay no) |
| Second account created | `not-run` (must stay no) |

---

## Listing draft

| Item | Observed |
|---|---|
| Unpublished 通常サービス exists | `not-run` |
| Matches first-gig file | `not-run` (`PR79-01` expected) |
| Multiple drafts (ambiguous) | `not-run` |
| Already 公開中 | `not-run` |
| Save control | `not-run` (`下書き` / `no-save-path` / `公開-only`) |

---

## Fields / images / price / FAQ

| Item | Observed |
|---|---|
| タイトル ≤ 25, ます止め | `not-run` |
| キャッチ ≤ 30 | `not-run` |
| サービス内容 ≤ 1000, from PR#79 not estimate packs | `not-run` |
| カテゴリ nearest automation node | `not-run` |
| お願い / 見積もりお願い | `not-run` |
| Images | `not-run` (`images_missing` is a GO-blocker) |
| Price vs live category minimum | `not-run` (`rate_empty` if ledger blank) |
| FAQ count (target 6 from 01) | `not-run` |
| Partner-logo / 景表法 risk | `not-run` |

---

## Ship-blockers for HUMAN-GO (still do not click 公開する)

Write `none` or a short token list (`images_missing`, `rate_empty`, `faq_trimmed`, …).

```
ship_blockers: not-run
```

---

## Stop lights seen

| Screen | Opened? | Action |
|---|---|---|
| 公開する confirm | `not-run` | cancel |
| 本人確認 / 口座 | `not-run` | close; slip PR#43 |
| 見積もり送信 | `not-run` | do not send |

---

## Notes (no secrets)

```
date_jst:
operator:
outcome: not-run
```

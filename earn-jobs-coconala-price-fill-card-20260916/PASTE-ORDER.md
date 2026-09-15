# PASTE-ORDER — which of the 3 listings to paste first

Pack date: 2026-09-16  
Desk: Coconala  
Listings: PR#79 three 通常サービス DRAFTS  
Mode: **DRAFT_ONLY**

**Paste 01 first. Stop after 下書き保存.**  
Do not start with 02 or 03. Do not paste all three as one GO.

---

## Map

| Order | #79 file | Offer | Category (public tree; live dropdown wins) | Why this slot |
|---|---|---|---|---|
| **1 — FIRST** | `01-n8n-automation-listing.md` | n8n自動化。公式 API のみ。公開スイッチは人 | IT相談・システム開発 → 業務自動化・効率化支援 → その他（業務自動化・効率化） | Flagship JOBS offer. Same parent as 02, so **one** floor re-read covers the first sitting. Concrete deliverable (JSON + 手順書) is the easiest form to sanity-check. Matches n8n packs on other desks without copying those prices |
| 2 — after 01 is 下書き | `02-inquiry-classify-listing.md` | 問い合わせ分類。未確定。自動返信なし | **Same parent** as 01 | Different offer (not a duplicate SKU). Reuse the 01 floor check. Do not paste if 01 is still open unsaved |
| 3 — last | `03-ai-ops-accompany-listing.md` | AI運用伴走。検品リストと型。代行運用ではない | IT相談・システム開発 → ITサポート・コンサル相談 → ITコンサル相談 | **Different mid-category.** Re-read a **different** floor. Do not put this in AIエージェント開発 |

Ids from #79 (do not invent a fourth):

- `JP-JOBS-COCONALA-01`
- `JP-JOBS-COCONALA-02`
- `JP-JOBS-COCONALA-03`

---

## One-listing rule

Each sitting is **one** listing.

```
sitting_1: 01 n8n  → local {{PRICE_YEN}} → 下書きで保存する → STOP
sitting_2: 02 分類  → only if 01 is already 下書き
sitting_3: 03 伴走  → only if 01 and 02 are already 下書き (or 02 skipped on purpose)
```

Skip 02 or 03 rather than rush. Skipping is allowed. Publishing is not.

If the live form cannot save as 下書き: **do not 公開する to “keep the work”.** Close. Local note `draft_save_failed`.

---

## Do not

- Paste 02 or 03 **first** “because the floor looks cheaper”
- Paste 01 and 02 as the same service twice (duplicate SKU)
- Put 03 in AIエージェント開発 / AIチャットボット / 画像生成
- Open 見積もり送信 from this card
- Treat “three files exist” as “three must go live today”

---

## Operator tick (local copy only)

```
date_jst:
paste_first: 01
01_draft_saved: yes / no / not_started
02_draft_saved: yes / no / skipped / not_started
03_draft_saved: yes / no / skipped / not_started
publish_clicked: no
```

Do not commit a filled live service URL next to these ticks.

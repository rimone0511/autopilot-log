# COVER-BRIEF — サービス画像 1枚目（n8n受付）

Listing: Coconala **4403529** (unpublished)  
Desk: 仕事窓口  
Asset: **出品サービス画像**（検索サムネ / サービスページ先頭）。プロフィールヘッダー（1280×420）ではない。  
Listing title (do **not** change from this pack): `n8n自動化と手順書を作ります`  
Theme to match: **n8n受付** — フォームの行を表へ足して人に知らせる。公式 API のみ。公開スイッチは人。

This file is a make-spec. [cover-mock.svg](cover-mock.svg) is a layout mock only. **Do not commit the upload binary.** Live uploader wins over any px below.

---

## 1. Size (conservative · live form wins)

Official / mag / news used by siblings: 公開時はサービス画像 **1枚以上**（news 1372）。1枚目が検索結果の顔。

| Spec | Use this | Why |
|---|---|---|
| Canvas | **1220 × 1240 px** | Help-quoted max for some IT/デザイン系 PC ページ。他カテでも「大きめキャンバス」として安全 |
| Safe zone | **1220 × 1016 px** 中央（上下 約 112 px はトリム想定） | 一覧サムネは **6:5**。タイトル・バッジはここだけ |
| Thumb mental model | 正方形に近いクロップもあり得る | 重要文字はさらに内側 80 px |
| Format | **PNG**（文字多め）または JPEG | アニメ GIF 不可。WebP はフォームが拒むことがある |
| File weight | **200 KB〜2 MB** 目安 | 上限通説 100 MB。重いほどスマホで潰れる |
| Color | sRGB, 72–144 dpi 相当でよい | 印刷用 300 dpi は不要 |
| Filename | `coconala-4403529-n8n-uketsuke-cover.png` | メール・請求番号・本名を入れない |

If the live uploader prints a size, **follow the uploader**. Do not invent a second canvas “because a blog said 610×507.”

Do **not** make the 1280×420 プロフィールカバー in this pass. That is a different slot.

```
1220
┌──────────────────────────────────────────┐  ↑ trim risk (~112)
│                                          │
│   SAFE 1220 × 1016                       │  タイトル・受付フロー・バッジ
│   （ここ以外に字を置かない）               │
│                                          │
└──────────────────────────────────────────┘  ↓ trim risk (~112)
                              1240 tall
```

---

## 2. Style

仕事窓口の看板。落ち着いた業務デスク。稼げる系のネオン、ストックの握手、AI美女は使わない。

| Axis | Do | Don't |
|---|---|---|
| Tone | 受付窓口。短い。信頼 | 広告バナー、限定、ランキング |
| Palette | インク `#16324F` / 紙 `#F3F6F8` / 一点アクセント `#1F6B5C` | 赤の「必見!!」、虹グラデ |
| Type | ゴシック。タイトル 64–88 px 相当。字間広め | 細明朝の長文、英語だけのヒーロー |
| Language | **日本語**が主。`n8n` と `API` だけ欧文 | 英キャッチを全面に |
| Scene | 抽象ノード（角丸箱）+ 手順書チップ | 公式 n8n UI の生スクショ（鍵が見える） |
| People | 人は「人へ通知」のラベルだけ | 顔写真、有名人、生成リアル顔 |
| Brand | テキストの単語 `n8n` のみ | n8n / ココナラ / lab / xAI の公式ロゴ |

Visual sentence (one glance):

> 受付（フォーム）→ n8n → 表 → 人へ知らせる。公開は人が止める。手順書がある。

---

## 3. Japanese title options (overlay only · matching n8n受付)

These are **on-image** lines. They must stay inside the safe zone. They are **not** a new サービスタイトル.

Do **not** paste these into the listing title field. Canonical listing title stays `n8n自動化と手順書を作ります`（[#103](https://github.com/rimone0511/autopilot-log/pull/103) TITLE-FIX）。ますの二重付与もこのパックでは触らない。

字数は Python `len()`（UTF-8 文字。上限は画像上の可読性。25字ルールは **出品タイトル欄** 用）。

### 3.1 Recommended stack

| Role | Copy | 字 |
|---|---|---|
| **Title (pick 1)** | `n8n受付と手順書` | 9 |
| **Sub** | `公開スイッチは人です` | 10 |
| **Badge A** | `公式APIのみ` | 7 |
| **Badge B** | `スクレイピングなし` | 9 |

This stack names **受付** (patrol theme), keeps **手順書** (live listing), and repeats the two policy lines already in サービス内容.

### 3.2 Title candidates (choose one)

| # | Overlay | 字 | Use when |
|---|---|---|---|
| **A** | `n8n受付と手順書` | 9 | **Default.** Short. Matches n8n受付 + listing 手順書 |
| B | `受付をn8nにします` | 10 | Want ます-tone on the image without touching the listing field |
| C | `公式APIで受付をつなぐ` | 12 | Stress 公式API first (buyer already knows n8n) |
| D | `フォーム受付を1本にする` | 12 | Stress 1本 / フォーム（#79 向いている例） |
| E | `受付→通知。公開は人` | 10 | Most “窓口”. Weakest n8n word — add a small `n8n` chip |
| F | `n8n自動化と手順書` | 10 | Closest to listing title. Weaker 受付。A を優先 |

Do not keyword-stuff: `n8n AI エージェント 公式パートナー 代行`. Do not put `¥` or `10000` on the image.

### 3.3 Sub / chip candidates (0–2)

| Copy | 字 | Pair with |
|---|---|---|
| `公開スイッチは人です` | 10 | A–D, F |
| `公式APIのみ。公開は人` | 12 | D, E |
| `手順書つき。公式APIのみ` | 13 | B, E |
| `スクレイピングなし` | 9 | Any, as a small chip — not the hero |

Max on-image text: **title + one sub + two chips**. More will die on mobile thumb.

---

## 4. Must-have visual elements

All of these must be readable **inside the 1220×1016 safe zone** after a square-ish crop.

1. **受付フロー（必須）** — four nodes, left to right or top to bottom:
   - `フォーム`
   - `n8n`（テキスト。公式ノードアイコンをトレースしない）
   - `表`
   - `人へ通知`
   - Arrows between them. One extra node `公開は人` as a gate / pause is allowed.
2. **手順書 cue（必須）** — chip or small doc card labeled `手順書`. Shows the listing’s second deliverable.
3. **公式API-only cue（必須）** — badge `公式APIのみ` or title option C. No browser-window “クリック自動化” drawing.
4. **Human publish gate（必須）** — `公開は人` / `公開スイッチは人です`. A hand-off, not a rocket.
5. **Japanese hero title（必須）** — one line from §3.2. High contrast on a solid or paper panel (not on a busy photo).
6. **Original canvas（必須）** — own boxes / own screenshot with secrets cropped. Not another seller’s thumb.

Optional (nice): a faint lined “手順書” card behind the flow. Keep opacity low so type stays first.

---

## 5. Avoid — policy / 景品表示 / 知財

画像・動画内の文言も審査対象（ココナラ 景品表示法ヘルプ）。下は **載せない**。

| Risk | Examples to keep off the art |
|---|---|
| 断定・誇大 | 絶対、必ず、稼げる、高収入、時短90%、成功率、失敗なし |
| 根拠なし実績 | 「○件導入」「全員満足」「レビュー★5」の捏造 |
| 最上級・比較 | 日本一、業界最安、他社より、ココナラ公式おすすめ |
| 提携の誤認 | n8n / Coconala / Google / xAI の **ロゴ**、認定バッジ、Partner 帯 |
| 他者の権利 | 他人の出品サムネ、商用不可素材、有名人、無断 UI ブランドキット |
| 秘密 | API key、メール、顧客名、トークン、請求書、本人確認 |
| 範囲外の絵 | ブラウザ自動クリック、スクレイピング、いいね・フォロー、無人SNS投稿 |
| 決済・誘導 | LINE / Zoom / 振込直 / 月額サイト外 |
| 価格トリック | 二重価格、期間も数量も無い「今だけ」 |
| 顔・KYC | 自撮り、マイナ、口座画面 |
| タイトル改変 | 画像で「公式n8n代行します」と書いて出品タイトルと食い違う |

Allowed word: **n8n** as plain text (the tool this offer uses). That is already in the listing title. It is **not** a logo license.

Secrets crop rule (if a real canvas screenshot is used):

- Blur or paint over connection values, emails, webhook URLs with tokens, customer rows
- Prefer a dummy flow named `受付サンプル` with `example.com` only
- Filename and EXIF: strip GPS / author email before upload

---

## 6. How to produce (no live CU here)

Pick one:

1. **Vector first (preferred):** open [cover-mock.svg](cover-mock.svg) in a local editor, swap title if not using A, export PNG 1220×1240.
2. **Canva / Figma:** custom size 1220×1240. Recreate the four nodes. Do not start from a “Coconala売れ筋” template that already has another seller’s face.
3. **Own n8n canvas:** dummy 受付 flow, secrets cropped, then lay a paper panel + title A on top so the thumb still reads when the screenshot is tiny.

Export checklist:

- [ ] 1220×1240 (or live-uploader size)
- [ ] Title + flow inside 1220×1016
- [ ] No logo files
- [ ] No yen
- [ ] Contrast: title vs ground is obvious at 200 px wide
- [ ] Binary stays **local**. Not this git repo

Then go to [PASTE-CHECKLIST.md](PASTE-CHECKLIST.md). **STOP before 公開する.**

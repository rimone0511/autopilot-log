# ALT-TEXT — 日本語候補（4403529 カバー）

Listing: Coconala **4403529** (unpublished)  
Desk: 仕事窓口  
For: サービス画像 1枚目。フォームに「代替テキスト / 画像の説明」が **無い** ときは、手元のファイルメモと [PASTE-CHECKLIST.md](PASTE-CHECKLIST.md) の記録欄だけに使う。

ルール: 見えるものを言う。成果・件数・提携を言わない。秘密を書かない。出品タイトル欄には貼らない。

Recommended overlay stack ([COVER-BRIEF.md](COVER-BRIEF.md) §3.1): タイトル `n8n受付と手順書` / サブ `公開スイッチは人です`.

字数は Python `len()`。通説の alt は 80–120 字で足りる。画面カウンタがあればそれを正とする。

---

## 1. Recommended (default)

**A1 — 短い（検索サムネ向け）** 40字

```
n8n受付の流れと手順書。フォームから表へつなぎ、人へ通知する図。公式APIのみ
```

**A2 — 標準（説明欄があるとき）** 70字

```
フォーム・n8n・表・人へ通知の4つの箱と、公開スイッチは人ですという表示。n8n受付と手順書。公式APIのみで、スクレイピングはありません
```

**A3 — 手順書を先に** 42字

```
n8n受付と手順書の案内図。受付フローの横に手順書。公開は人が止める。公式APIのみ
```

---

## 2. Alternates (if you picked another overlay title)

Use the row that matches the **actual** on-image title.

| Overlay | Alt | 字 |
|---|---|---|
| B `受付をn8nにします` | `受付をn8nにしますと書いた図。フォームから表、人へ通知。公式APIのみ。手順書つき` | 42 |
| C `公式APIで受付をつなぐ` | `公式APIで受付をつなぐ図。n8nの箱と手順書。公開スイッチは人。スクレイピングなし` | 42 |
| D `フォーム受付を1本にする` | `フォーム受付を1本にする図。n8nと表と人へ通知。手順書つき。公式APIのみ` | 38 |
| E `受付→通知。公開は人` | `受付から通知、公開は人、と書いた図。n8nの箱と手順書。公式APIのみ` | 35 |
| F `n8n自動化と手順書` | `n8n自動化と手順書の図。受付フロー（フォーム・表・人へ通知）。公式APIのみ` | 39 |

---

## 3. Do not use

| Bad alt | Why |
|---|---|
| `n8n公式パートナーが作る受付自動化。成功率100%` | 提携の誤認 + 景品表示 |
| `必ず時短できます。高収入` | 断定・誇大 |
| `お客様の山田商事の実フロー` | 顧客名 / 秘密 |
| `https://n8n.io の公式ロゴ` | ロゴを使っていない（使うな）のにロゴと書く |
| `DRAFT 4403529 unpublished` | 買い手向けに下書きを晒す |
| `出品者メールアドレスのキャンバス` | メール / 個人情報 |

Empty alt is worse than A1 if the form has a required description. If the form has **no** alt field: skip. Do not invent a hidden HTML attribute in git.

---

## 4. After paste

- [ ] Alt matches the **exported** image (title A vs B…)
- [ ] No yen, no email, no customer name
- [ ] Listing title field still `n8n自動化と手順書を作ります`
- [ ] Still unpublished

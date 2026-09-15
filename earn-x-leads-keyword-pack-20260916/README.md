> **DRAFT_ONLY.** このフォルダは X 検索の下書きパックです。このエージェントは X API を呼びません。投稿しません。DM しません。秘密は書きません。

# X リード用キーワードパック（AIエージェント外注・JP+EN）

日付ラベル: **2026-09-16**。件数・GMV・「何件取れた」は書いていません（この PR では検索を実行していません）。

| ファイル | 役割 |
|---|---|
| [`KEYWORDS.md`](KEYWORDS.md) | JP / EN の語群。意図動詞 × 技術名詞 × 除外 |
| [`RUBRIC.md`](RUBRIC.md) | 1投稿の仕分け（`keep_queue` / `park` / `skip`）。fail-closed |
| [`SAMPLE-QUERIES.md`](SAMPLE-QUERIES.md) | x.com 検索欄へ人が貼るクエリ。API 形も参考のみ |

## この机の売り（兄弟パックと揃える）

日本の個人（ユタラボ / Autopilot Log）。人が止まれる自動化。

- n8n / Make / Zapier + 手順書
- 公式 API だけの投稿道具（YouTube は無人、TikTok は既定が受信箱。ブラウザ操作はしない）
- Claude Code / Codex などの依頼票・検品・回帰
- GAS / 表計算の仕組み化
- 検査できる MCP 配線。未確認の効果%は書かない

## 人がやること / この PR がやらないこと

**人がやること:** Latest タブにクエリを貼る。[`RUBRIC.md`](RUBRIC.md) で1件ずつ。残すなら秘密なしログ。返信文は別パック。送るのは人。

**やらないこと:** X API、投稿、いいね/フォロー自動化、スクレイピング、一斉 DM、鍵の保存、件数の捏造、マージ前の draft 解除。

## 検証

Markdown のみ。既存の投稿ゲート試験は変更していません。

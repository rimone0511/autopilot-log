> **DRAFT_ONLY.** 下の文字列は人が x.com の検索欄へ貼る。  
> **このエージェントは実行しない。** X API・投稿・DM・いいね自動化はしない。ヒット件数は未測定。

# SAMPLE-QUERIES — 人が貼る検索文（JP + EN）

語の由来は [`KEYWORDS.md`](KEYWORDS.md)。ヒットの仕分けは [`RUBRIC.md`](RUBRIC.md)。

`{{SINCE}}` を実行日の 7 日前（`YYYY-MM-DD`）に置き換える。未置換のまま API に投げない（このエージェントは投げない）。

---

## 0. 貼り方（WEB）

1. [x.com/search](https://x.com/search) を開く（人がログインしているブラウザ。このクラウドエージェントのブラウザではログインしない）。
2. 下の **WEB** 行を検索欄に貼る。`{{SINCE}}` を実日付にする。
3. **Latest**（最新）を選ぶ。Top は宣伝が上に来る。
4. 上から [`RUBRIC.md`](RUBRIC.md) の3値。ログは秘密なし1行。
5. 1クエリで長く見るより、表のローテを短く回す。

Latest の URL 形（参考。手で開いてよい）:

```text
https://x.com/search?q={{URLENCODED_QUERY}}&src=typed_query&f=live
```

この PR に完成 URL は置かない（日付とエンコードがすぐ腐る）。

### WEB と API 形の違い（実行はしない）

| | WEB（人が貼る） | API 形（参考。**呼ばない**） |
|---|---|---|
| リポスト除外 | `-filter:retweets` | `-is:retweet` |
| リプライ除外 | `-filter:replies` | `-is:reply` |
| 言語 | `lang:en` / `lang:ja` | 同じ |
| 日付 | `since:{{SINCE}}` | 同じ。recent はおおむね 7 日 |
| いいね下限 | **付けない** | `min_likes` も付けない |
| 長さ | 長すぎると欄が切る | recent **512** 字が目安。下の `chars` はスペース込み |

API 形は「後で人が公式検索を使うときの写し」であり、鍵・Bearer・コンソール操作の手順ではない。

---

## 1. EN — WEB（初手）

### Q-EN-01 — フリーランスを探している × エージェント

WEB:

```
("looking for a freelancer" OR "need a freelancer" OR "anyone know someone" OR "does anyone know a") ("AI agent" OR "Claude Code" OR MCP OR agentic) lang:en -filter:replies -filter:retweets since:{{SINCE}} -"open to work" -"hire me" -"I can build"
```

API 形（**実行しない**）:

```
("looking for a freelancer" OR "need a freelancer" OR "anyone know someone" OR "does anyone know a") ("AI agent" OR "Claude Code" OR MCP OR agentic) lang:en -is:reply -is:retweet since:{{SINCE}} -"open to work" -"hire me" -"I can build"
```

### Q-EN-02 — フリーランス × n8n / Make / Zapier

WEB:

```
("looking for a freelancer" OR "need a freelancer" OR "need someone to" OR "paid gig") (n8n OR "make.com" OR Zapier OR "workflow automation") lang:en -filter:replies -filter:retweets since:{{SINCE}} -"open to work" -"hire me" -"I can build"
```

API 形（**実行しない**）:

```
("looking for a freelancer" OR "need a freelancer" OR "need someone to" OR "paid gig") (n8n OR "make.com" OR Zapier OR "workflow automation") lang:en -is:reply -is:retweet since:{{SINCE}} -"open to work" -"hire me" -"I can build"
```

### Q-EN-03 — 紹介・推薦 × 狭いスタック

WEB:

```
("can anyone recommend" OR "who's good at" OR "who is good with" OR "any recs for") (n8n OR "Claude Code" OR "AI agent" OR MCP) lang:en -filter:replies -filter:retweets since:{{SINCE}} -"open to work" -"for hire"
```

API 形（**実行しない**）:

```
("can anyone recommend" OR "who's good at" OR "who is good with" OR "any recs for") (n8n OR "Claude Code" OR "AI agent" OR MCP) lang:en -is:reply -is:retweet since:{{SINCE}} -"open to work" -"for hire"
```

### Q-EN-04 — need someone to × 実装・配線

WEB:

```
"need someone to" (n8n OR "Claude Code" OR "AI agent" OR MCP OR Zapier OR "apps script") lang:en -filter:replies -filter:retweets since:{{SINCE}} -"open to work" -"hire me" -airdrop
```

API 形（**実行しない**）:

```
"need someone to" (n8n OR "Claude Code" OR "AI agent" OR MCP OR Zapier OR "apps script") lang:en -is:reply -is:retweet since:{{SINCE}} -"open to work" -"hire me" -airdrop
```

### Q-EN-05 — looking to hire × 業務委託寄り（求人は rubric で切る）

WEB:

```
("looking to hire" OR "contractor needed" OR "seeking a contractor" OR "project-based") ("AI agent" OR n8n OR "Claude Code" OR MCP) lang:en -filter:replies -filter:retweets since:{{SINCE}} -internship -"apply now" -"open to work"
```

API 形（**実行しない**）:

```
("looking to hire" OR "contractor needed" OR "seeking a contractor" OR "project-based") ("AI agent" OR n8n OR "Claude Code" OR MCP) lang:en -is:reply -is:retweet since:{{SINCE}} -internship -"apply now" -"open to work"
```

### Q-EN-06 — 痛み（高い iPaaS / 手作業）× 助け

WEB:

```
("need help with" OR "looking for help" OR "will pay") (n8n OR Zapier OR "make.com" OR "google sheets") lang:en -filter:replies -filter:retweets since:{{SINCE}} -"open to work" -"I can build" -"book a call"
```

API 形（**実行しない**）:

```
("need help with" OR "looking for help" OR "will pay") (n8n OR Zapier OR "make.com" OR "google sheets") lang:en -is:reply -is:retweet since:{{SINCE}} -"open to work" -"I can build" -"book a call"
```

---

## 2. JA — WEB（初手）

日本語句は `"..."` 固定。`lang:ja` を付ける。

### Q-JP-01 — 外注 × エージェント / Claude Code / MCP

WEB:

```
("外注" OR "外注先" OR "外注したい" OR "作ってほしい" OR "作ってくれる人") (AIエージェント OR "Claude Code" OR MCP OR Cursor) lang:ja -filter:replies -filter:retweets since:{{SINCE}} -"仕事ください" -"案件募集中"
```

API 形（**実行しない**）:

```
("外注" OR "外注先" OR "外注したい" OR "作ってほしい" OR "作ってくれる人") (AIエージェント OR "Claude Code" OR MCP OR Cursor) lang:ja -is:reply -is:retweet since:{{SINCE}} -"仕事ください" -"案件募集中"
```

### Q-JP-02 — 外注 × n8n / Make / Zapier

WEB:

```
("外注" OR "作ってほしい" OR "構築してほしい" OR "手伝ってほしい") (n8n OR Zapier OR Make OR ワークフロー) lang:ja -filter:replies -filter:retweets since:{{SINCE}} -"仕事ください" -"案件募集中"
```

API 形（**実行しない**）:

```
("外注" OR "作ってほしい" OR "構築してほしい" OR "手伝ってほしい") (n8n OR Zapier OR Make OR ワークフロー) lang:ja -is:reply -is:retweet since:{{SINCE}} -"仕事ください" -"案件募集中"
```

### Q-JP-03 — 詳しい人 / できる方 × 狭いスタック

WEB:

```
("詳しい人いませんか" OR "できる方いませんか" OR "得意な人" OR "フリーランス探して") (n8n OR "Claude Code" OR AIエージェント OR GAS) lang:ja -filter:replies -filter:retweets since:{{SINCE}} -"仕事ください"
```

API 形（**実行しない**）:

```
("詳しい人いませんか" OR "できる方いませんか" OR "得意な人" OR "フリーランス探して") (n8n OR "Claude Code" OR AIエージェント OR GAS) lang:ja -is:reply -is:retweet since:{{SINCE}} -"仕事ください"
```

### Q-JP-04 — 依頼したい / 発注 × 生成AI自動化

WEB:

```
("依頼したい" OR "発注したい" OR "見積もって") ("生成AI" OR n8n OR AIエージェント OR GAS) (自動化 OR ワークフロー OR 検品) lang:ja -filter:replies -filter:retweets since:{{SINCE}} -"仕事ください" -"案件募集中"
```

API 形（**実行しない**）:

```
("依頼したい" OR "発注したい" OR "見積もって") ("生成AI" OR n8n OR AIエージェント OR GAS) (自動化 OR ワークフロー OR 検品) lang:ja -is:reply -is:retweet since:{{SINCE}} -"仕事ください" -"案件募集中"
```

### Q-JP-05 — 業務委託 × 自動化（求人は rubric）

WEB:

```
"業務委託" (n8n OR "Claude Code" OR AIエージェント OR "生成AI" OR GAS) lang:ja -filter:replies -filter:retweets since:{{SINCE}} -正社員 -新卒 -インターン -"仕事ください"
```

API 形（**実行しない**）:

```
"業務委託" (n8n OR "Claude Code" OR AIエージェント OR "生成AI" OR GAS) lang:ja -is:reply -is:retweet since:{{SINCE}} -正社員 -新卒 -インターン -"仕事ください"
```

### Q-JP-06 — 検品 / 依頼票（JP-P05 と同じ核）

WEB:

```
("検品" OR "依頼票" OR "手順書") ("Claude Code" OR Cursor OR Codex OR AIエージェント) lang:ja -filter:replies -filter:retweets since:{{SINCE}} -"仕事ください"
```

API 形（**実行しない**）:

```
("検品" OR "依頼票" OR "手順書") ("Claude Code" OR Cursor OR Codex OR AIエージェント) lang:ja -is:reply -is:retweet since:{{SINCE}} -"仕事ください"
```

---

## 3. 監視だけ（keep に数えない）

意図語が無い。タイムラインの温度を見るときだけ。ヒットを `keep_queue` にしない。本文に §2 の Buyer が出て初めて rubric を通す。

### Q-WATCH-EN — 技術のみ（実行任意。リード初手にしない）

WEB:

```
("AI agent" OR n8n OR "Claude Code" OR MCP) lang:en -filter:replies -filter:retweets since:{{SINCE}}
```

### Q-WATCH-JA

WEB:

```
(AIエージェント OR n8n OR "Claude Code") lang:ja -filter:replies -filter:retweets since:{{SINCE}}
```

---

## 4. 日次ローテ（人が手で。自動化しない）

1周の目安。時間は書かない（タイムゾーンと ADHD 負荷のため「本数」だけ）。

| 順 | クエリ | メモ |
|---|---|---|
| 1 | Q-JP-01 | JP 外注 × エージェント |
| 2 | Q-JP-02 | JP 外注 × iPaaS |
| 3 | Q-EN-01 | EN フリーランス × エージェント |
| 4 | Q-EN-02 | EN フリーランス × iPaaS |
| 5 | Q-JP-03 または Q-JP-06 | 紹介 or 検品 |
| 6 | Q-EN-03 または Q-EN-04 | 紹介 or need someone |
| 任意 | Q-JP-05 / Q-EN-05 | 求人ノイズが増えたら止める |
| しない | Q-WATCH-* | 初手に使わない |

同じクエリを短時間に何周もして「件数が出るまで」やらない。未測定のまま次へ。

---

## 5. 文字数（`{{SINCE}}` を `2026-09-09` に置いたときの WEB 本文）

測定は Python `len()`。`{{SINCE}}` を `2026-09-09`（10字）に置いた WEB / API 本文。実日付が同じ桁なら差は出ない。API recent の 512 を超えない。最大は Q-EN-01 WEB の 248。

| ID | WEB chars | API chars | 512 以下 |
|---|---|---|---|
| Q-EN-01 | 248 | 237 | yes |
| Q-EN-02 | 241 | 230 | yes |
| Q-EN-03 | 213 | 202 | yes |
| Q-EN-04 | 182 | 171 | yes |
| Q-EN-05 | 230 | 219 | yes |
| Q-EN-06 | 207 | 196 | yes |
| Q-JP-01 | 173 | 162 | yes |
| Q-JP-02 | 155 | 144 | yes |
| Q-JP-03 | 163 | 152 | yes |
| Q-JP-04 | 165 | 154 | yes |
| Q-JP-05 | 142 | 131 | yes |
| Q-JP-06 | 139 | 128 | yes |
| Q-WATCH-EN | 101 | — | yes |
| Q-WATCH-JA | 92 | — | yes |

---

## 6. やってはいけないクエリ（書いているのは禁止例）

- `n8n` だけ、日付なし（宣伝タイムライン）
- `"DM me" AI agent`（売り手が埋める）
- `#hiring AI`（求人板）
- `from:{{HANDLE}}` で他人の顧客を漁る手順
- `min_faves:50` / `min_likes:50`（伸びる宣伝だけ残る）
- 言語横断の巨大 OR（512 超えとノイズ）

---

## 7. このエージェントの宣言

- X 名前空間の検索・投稿・DM ツールは **使っていない**
- Bearer / cookie / パスワードは受け取らない・書かない
- 下のクエリをクラウドから叩いて結果を PR に貼っていない

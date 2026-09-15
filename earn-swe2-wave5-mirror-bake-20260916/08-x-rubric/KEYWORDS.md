> **DRAFT_ONLY.** No X API from the authoring agent. No posting. No DMs. No secrets.  
> 語を足しても「実行した」「何件ヒットした」とは書かない。ヒット数は未測定。

# KEYWORDS — AI-agent freelance leads (JP + EN)

パック日付: **2026-09-16**。検索は人が [x.com/search](https://x.com/search) の **Latest** に貼る。クエリの組み立ては [`SAMPLE-QUERIES.md`](SAMPLE-QUERIES.md)。仕分けは [`RUBRIC.md`](RUBRIC.md)。

1クエリは **意図（人が頼みたい）× 技術（この机が受ける）× 除外（売り手・求人板・詐欺）**。言語は混ぜない。`lang:ja` と `lang:en` を同じ箱に入れない。

プレースホルダ: `{{SINCE}}` = `YYYY-MM-DD`（目安は直近7日。API の recent 窓と同じ長さ）。`{{UNTIL}}` は任意。

---

## 0. この机が拾う仕事 / 拾わない仕事

### Keep の核（語を選ぶ理由）

| 箱 | EN の例 | JP の例 |
|---|---|---|
| iPaaS + 手順書 | n8n, Make, Zapier, "workflow automation" | n8n、Make、Zapier、ワークフロー、自動化 |
| エージェント実装の依頼票・検品 | "Claude Code", Cursor, Codex, MCP, "AI agent" | Claude Code、Cursor、Codex、MCP、AIエージェント、検品 |
| 公式 API 投稿 | YouTube API, TikTok API（**inbox / gate**。無人 TikTok とは言わない） | YouTube API、TikTok（受信箱。ブラウザ自動は範囲外） |
| 表計算 | GAS, Apps Script, spreadsheet | GAS、スプレッドシート、仕組み化 |
| 社内 LLM（人が見る） | RAG, "internal GPT", "operator docs" | 社内GPT、RAG、手順書、検収 |

### 語にしない / ヒットしても skip 側へ倒す題材

いいね・フォロー・再生の自動化、スクレイピング、公式 API が無い操作、暗号資産ボット、成人向け、ビザ付き正社員のみ、共同創業エクイティのみ、同じサービスを売っている投稿、一斉「DM me for AI agents」。

---

## 1. Pack EN-INTENT — 買い手の言い方

**高シグナル（優先して OR する）**

| 語 / 句 | なぜ |
|---|---|
| `"looking for a freelancer"` | 外注が本文に出る |
| `"need a freelancer"` | 同上 |
| `"looking to hire"` | 雇用寄りのことがある。本文が業務委託なら keep、正社員応募リンクなら skip |
| `"need someone to"` | 具体動詞が続くとき強い |
| `"anyone know someone"` / `"does anyone know a"` | 紹介依頼。本人が発注者のことが多い |
| `"paid gig"` / `"paid project"` / `"will pay"` | 有償。詐欺文も多いので本文を読む |
| `"contractor needed"` / `"seeking a contractor"` | 業務委託寄り |
| `"short-term contract"` / `"project-based"` | 期間仕事 |
| `"who's good at"` / `"who is good with"` | 紹介。売り手の自問自答と区別する |
| `"can anyone recommend"` / `"any recs for"` | 推薦依頼 |
| `"budget for"` + 技術語 | 予算の話。金額はログに写さない |

**中シグナル（単独では弱い。技術語と必ず組む）**

`hiring`, `"looking for help"`, `"need help with"`, `"trying to find"`, `"open to contractors"`, `"retainer"`, `"side project help"`（趣味の無償と混ざる）, `DM` + 技術語（売り手も使う）

**使わない（供給側・宣伝）**

`"open to work"`, `"hire me"`, `"I can build your"`, `"book a call"`, `"slots open"`, `"taking clients"`, `"for hire"`, `"DM me for rates"`（自分の営業）

---

## 2. Pack EN-STACK — 技術名詞（この机）

**A. エージェント / 実装補助（高フィット）**

`"AI agent"`, `agentic`, `"Claude Code"`, `Codex`, `"Cursor agent"`, `MCP`, `"model context protocol"`, `LangGraph`, `LangChain`, `CrewAI`, `"operator docs"`, `"eval"`, `regression`（検品文脈）

**B. 自動化（高フィット）**

`n8n`, `"make.com"`, `Zapier`, `"zapier"`, `"workflow automation"`, `"apps script"`, `GAS`, `"google sheets"` + `automat`

**C. 公式投稿 API（条件付き）**

`"youtube api"`, `"content posting api"` — 本文が「公式 API・鍵は依頼者」なら keep。「アカウント代行ログイン」「ブラウザで投稿」なら skip。

**D. 弱め・ノイズ多め（OR しすぎない）**

`"custom gpt"`, `ChatGPT`, `Claude`（単体）, `"gen ai"`, `LLM`, `RAG`, `"internal chatbot"`

`ChatGPT` だけは情報商材と授業宣伝が多い。必ず意図語と組む。

**E. クエリに入れない（この机の外）**

`scraping`, `selenium`, `puppeteer`（本文が公式 API 拒否のとき skip 判定用には本文で見る）, `"engagement bot"`, `"auto like"`, `airdrop`, `nft`, `"solana bot"`, `"pump fun"`, `"onlyfans"`

---

## 3. Pack JP-INTENT — 買い手の言い方

日本語は形態素が切れないので **短い句を `"..."` で固定** する。単語1つ（例: `募集`）は求人板になる。

**高シグナル**

| 句 | メモ |
|---|---|
| `"外注"` / `"外注先"` / `"外注したい"` | 発注 |
| `"業務委託"` | 正社員求人と併記されることがある。本文確認 |
| `"作ってほしい"` / `"作ってくれる人"` / `"構築してほしい"` | 依頼 |
| `"手伝ってほしい"` / `"手伝ってくれる人"` | 弱いこともある。技術語必須 |
| `"詳しい人いませんか"` / `"得意な人"` / `"できる方いませんか"` | 紹介 |
| `"依頼したい"` / `"発注したい"` | 発注 |
| `"見積もり"` / `"見積もって"` | 有償の入口。金額はログに写さない |
| `"相談に乗って"` / `"相談乗ってくれる"` | 営業マンも使う。技術が具体なら park〜keep |
| `"フリーランス探して"` / `"フリーランス募集"` | 「募集」は求人寄り。リモート業務委託か見る |
| `"誰か"` + 技術名 | 例はクエリ側で組む |

**中シグナル**

`困っている`, `手が回らない`, `属人化`, `仕組み化したい`, `自動化したい`, `内製できない`, `リソース不足`

**使わない（供給側）**

`"仕事ください"`, `"案件募集中"`（売り手）, `"始めました"` + サービス名, `"DMください"` だけの自己紹介, `"オープンワーク"` 系の転職だけ

---

## 4. Pack JP-STACK — 技術名詞（この机）

**A. 高フィット**

`AIエージェント`, `"AI エージェント"`, `n8n`, `Make`, `Zapier`, `"Claude Code"`, `Cursor`, `Codex`, `MCP`, `GAS`, `ワークフロー`, `"生成AI"` + 自動化, `検品`, `依頼票`, `手順書`, `社内GPT`, `RAG`

**B. 公式 API**

`YouTube API`, `TikTok` + `API` — 本文が公式・審査・受信箱なら keep。スクショ自動投稿・非公式ツールなら skip。

**C. 弱め**

`ChatGPT`, `GPTs`, `Dify`, `Chatbot`, `LLM`, `プロンプト`（プロンプト販売が多い）

**D. クエリに入れない**

`いいねボット`, `フォロワー購入`, `自動いいね`, `スクレイピング代行`, `口座`, `本人確認代行`

---

## 5. Pack NEGATIVE — どの言語でも引く

スペース区切りの `-語`。やりすぎると本命も消える。**常時セット**と **ノイズが増えたら足すセット** を分ける。

### 常時（WEB / API どちらも）

EN:

```text
-"open to work" -"hire me" -"I can build" -"book a call" -airdrop -nft -"onlyfans"
```

JP（ASCII と日本語を混ぜてよい）:

```text
-"仕事ください" -"案件募集中" -エアドロ -NFT
```

### ノイズが増えたら足す

```text
-"full time" -"full-time" -internship -"apply now" -greenhouse.io -lever.co
-"taking clients" -"slots open" -"for hire"
-求人 -正社員 -新卒 -インターン
```

`hiring` 自体は引かない（買い手が使う）。本文が Lever / Greenhouse / 「Apply」なら [`RUBRIC.md`](RUBRIC.md) で skip。

`min_likes` / `min_faves` は **使わない**。伸びている投稿は宣伝か釣りが多い。未返信の短い依頼の方が keep 向き。

---

## 6. 組み合わせ規則

1. **言語を分けたクエリにする。** JP 意図 ∪ EN 技術の1箱は可（日本の投稿が `n8n` と書く）。EN 意図 ∪ 日本語意図の巨大 OR はしない（512字とノイズ）。
2. **意図なし技術だけ**（例: `n8n lang:en`）はタイムライン監視用。リード抽出の初手にしない。
3. **技術なし意図だけ**（例: `"need a freelancer" lang:en`）は職種が飛びすぎる。必ずスタックを1つ以上。
4. OR グループは **意図 ≤ 4、技術 ≤ 5** を目安。超えるならクエリを分割（[`SAMPLE-QUERIES.md`](SAMPLE-QUERIES.md) の日次ローテ）。
5. リポストとリプライを外す（WEB: `-filter:retweets -filter:replies` / API 形: `-is:retweet -is:reply`）。例外: 長いスレの2番目が発注条件のときだけ、元投稿 ID を人が開く。
6. `since:{{SINCE}}` を付ける。このパックはヒット件数を持っていないので、日付でfreshにする。
7. 公式アカウント `from:` はリード探索に使わない（製品発表になる）。競合調査は別メモ。

---

## 7. ハッシュタグ（補助。主クエリにしない）

入れるなら1つ。タグだけの投稿は売り手が多い。

| 使ってよい（技術と組む） | 使わない |
|---|---|
| `#n8n` `#buildinpublic`（依頼文が混ざる。仕分け必須） | `#fiverr` `#upwork` 単体（ギグ宣伝） |
| `#生成AI`（JP 意図と組む） | `#nft` `#crypto` `#airdrop` |
| | `#hiring` 単体（求人板） |

---

## 8. 日次で回すパック（名前だけ。本文クエリは SAMPLE）

| ID | 言語 | 意図パック | 技術パック | いつ使う |
|---|---|---|---|---|
| P1 | EN | 高シグナル紹介・外注 | A エージェント | 初手 |
| P2 | EN | 高シグナル | B iPaaS | 初手 |
| P3 | EN | `"need someone to"` 系 | A+B 短く | 午前の2本目 |
| P4 | JP | 外注・作ってほしい | A+B | 初手 |
| P5 | JP | 詳しい人いませんか | n8n / Claude Code / GAS | 初手 |
| P6 | JP | 業務委託 | 生成AI + 自動化（狭く） | 求人ノイズを rubric で切る |
| P7 | EN/JP | 使わない | 技術のみ | 監視。keep に昇格させない |

P7 のヒットを keep に数えない。意図が本文にあって初めて [`RUBRIC.md`](RUBRIC.md) を通す。

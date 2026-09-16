# MAIN ChatGPT 6.0 Pro 向け 設計書作成依頼（貼り付け用）

- 受付ID（提案）: `AI-CACHE-PARENT-SUBAGENT-20260916-FABLE51`
- 案件ID: `AI-CACHE-PARENT-SUBAGENT-20260916` / 入力版: `GROK-CACHE-CONTEXT-20260916-R3` / 軍議: `FABLE-GUNGI-20260916.md`
- 状態: **Pro 未送信**（本ファイルは貼り付け原稿。送信・受付・返答の記録は別途 STATUS.md へ）
- 作成: Fable 5.1（軍議主席）、2026-09-16 UTC
- 秘密情報: なし（認証は type/有無のみ。鍵・トークン・メール・UUID は含まない）
- 送信前チェック: (1) PR #126 と本軍議ブランチが GitHub 上で読めること、(2) 下記「Pro が自ら取得すべき資料」の URL が生きていること、(3) 貼り付け後に受付IDを Pro が復唱すること

---

## ここから貼り付け（本文）

---

# 設計書作成依頼: Fable 親／Astra・Sol・Terra・Luna 子 のキャッシュ・文脈・休止設計

受付ID: **AI-CACHE-PARENT-SUBAGENT-20260916-FABLE51**
案件ID: AI-CACHE-PARENT-SUBAGENT-20260916
入力版: GROK-CACHE-CONTEXT-20260916-R3（設計候補）＋ FABLE51 軍議（方向裁定）
あなたの役割: **MAIN（ChatGPT 6.0 Pro）として、この案件の「設計書」を書く。** 軍議記録と R3 候補は入力であり、設計書ではない。あなたの出力が設計書になる。
納品先: `rimone0511/autopilot-log` `ops/policy/ai-cache-parent-subagent-20260916/DESIGN-FABLE51.md`（保存は担当者が行う。あなたは本文を書く）

## 0. 最初にやること（R5 接続確認・読了台帳）

1. `rimone0511/codex-general` 既定ブランチの `PRO_CONTEXT.md`（R5: 案件再開・意味ある変化時に GitHub 接続と未読差分を自分で確認し、読んでいない資料を読んだ扱いにしない）を読む。
2. 同リポジトリの `pro-chat/events/AI-CACHE-PARENT-SUBAGENT-20260916/`（v1 discussion / v2 keepalive-fork / R3 proposal の3イベント）と `pro-chat/artifacts/AI-CACHE-PARENT-SUBAGENT-20260916/grok-cache-context-brief-r3.md`、関連 `pro-chat/events/GROK-FABLE-SUPERVISOR-ORCH-20260915/` を読む。
3. `rimone0511/autopilot-log` PR #126（ブランチ `cursor/ai-cache-parent-r3-20260916`）の `ops/policy/ai-cache-parent-subagent-20260916/` 配下: `BRIEF-R3-full.md`, `DESIGN-CANDIDATE-R3.md`, `INVENTORY.md`, `DOCS-CHECK-20260916.md`, `STATUS.md`、および軍議ブランチ `cursor/ai-cache-gungi-fable51-2daf` の `FABLE-GUNGI-20260916.md` を読む。
4. 設計書の冒頭に **読了台帳** を置く: 読めた資料／読めなかった資料（理由）を列挙する。**読めなかったものを読んだ扱いにしない。** 本依頼文に要約された内容は、原本を読めなかった場合「依頼文経由の要約」とラベルする。

注記: 軍議（Fable 5.1, Cursor cloud agent）からは `codex-general` に到達できなかった（404）。本依頼文中の PRO_CONTEXT／イベントの記述は R3 成果物の要約経由である。あなたは自分の接続で原本を確認すること。

## 1. 絶対規則

- **候補・設計のみ。** 設定を適用しない。常駐処理・デーモン・定期監視を有効化しない。GitHub へ「適用済み」と書かない（保存≠適用）。
- **Claude はサブスクリプション経路のみ。** API 従量・usage credits・自動追加購入・新規契約・API key 発行を提案手段に含めない。「1h TTL 試験のために一時的に API key」も不可。
- **Codex は既存 ChatGPT 認証（`auth_mode=chatgpt`）のみ。** 新規 OpenAI API key 不可。
- **4分離を維持**: すべての主張を **本人希望 / AI提案 / 公開仕様 / 実機未確認** のいずれかに置く。ラベル: `OBSERVED`（実機で読んだ）/ `FROM_PUBLIC_DOC`（2026-09-16 取得の公式Docs）/ `UNVERIFIED` / `本人希望` / `AI提案`。
- **API 単価の 0.025×（Fable 5.1 キャッシュ読み）を Max 等サブスク枠の倍率として扱わない。** 「1M÷40=25K」「読み 0.025× 対 1h 書き 2× の単価比 80×」は価格の話であり、実コンテキストや全作業消費ではない。節約%は**計測値のみ**。未計測なら「未計測」と書く。
- **1M ダミー会話での効果証明を禁止。** 小さな隔離試験のみ。
- **読んでいない資料を読んだ扱いにしない。** 版差があるため、Docs は 2026-09-16 取得内容として引用し、導入先で再照合と書く。
- **本人へ経緯の再説明・伝言・GitHub 転記・技術操作を戻さない。** 本人へ見せるのは「本人が決める部分」の一画面要約のみ。
- 秘密（鍵・トークン・メール・UUID）を書かない。認証は type/有無のみ。

## 2. 本人希望（変えない。順序・条件を付けるのは AI提案側）

- Fable 5.1 を長い文脈を持つ**親・監督**に、Astra／Sol／Terra／Luna を**範囲の明確な子**にする方向を検討中。全案件での固定採用は未決定。
- 本人報告: Codex のコンテキスト設定を約 270K → 約 870K へ拡大した。報告だけで設定キー・対象モデル・適用範囲を確定しない（→ 実機では `model_context_window = 872000` を PC ユーザー設定に OBSERVED。整合するが「有効に効いているか」は UNVERIFIED）。
- 子の自動圧縮を約 **200K** で発動させたい。親は作業中に必要な文脈を保持。**長い休止へ入る前に、温かいキャッシュを使って圧縮**したい。
- **本人が離席時間や圧縮指示を管理する運用にはしない。**
- 休止前処理の候補値 **40分**。200K・40分・親の長文脈化はいずれも**検証候補**であり、最安保証や導入済みの事実ではない。
- Claude サブスクのみ。Codex 既存認証のみ。

## 3. 実機インベントリ（2026-09-16 ~00:00–00:15 UTC、読み取りのみ、秘密なし）

| 項目 | Cursor box | 登録PC（DESKTOP-EVCBN4H） | ラベル |
|---|---|---|---|
| Claude Code 版 | **2.1.270** | **2.1.260**（≥2.1.248: 個別 `experimental.cacheTtl` 可。≥2.1.251: resume 時 SessionStart 診断可） | OBSERVED |
| `~/.claude/settings.json` | **不在** | 存在（~7.6KB） | OBSERVED |
| `~/.claude/agents/` | **不在** | **不在** → カスタムエージェント定義は現在ゼロ | OBSERVED |
| Claude 既定モデル／effort | 設定ファイルなし（セッション既定 UNVERIFIED） | `model = "opus[1m]"`, `effortLevel = "high"`; modelSettings: opus-5 high / **fable-5-1 high** / sonnet-5 medium | OBSERVED（PC） |
| Claude モデル候補キャッシュ | `claude-fable-5-1[1m]` あり | 同 | OBSERVED |
| `promptCacheTtl` / `subagentPromptCacheTtl` | 未設定 | **未設定（既定適用）** | OBSERVED |
| Claude 認証 type | OAuth（claude.ai サブスク）、`ANTHROPIC_API_KEY` env なし、`billingType=stripe_subscription`、**extra usage は org 無効** | 同パターン | OBSERVED（type/真偽のみ） |
| Codex CLI 版 | **0.154.0** | **PATH 未解決 → UNVERIFIED**（box の models_cache は client_version 0.154.0） | OBSERVED / UNVERIFIED |
| `~/.codex/config.toml` | 存在。`[projects."…"].trust_level="trusted"` のみ（モデル／圧縮キーなし） | 存在（~77KB）。`model = "gpt-5.6-luna"`, `model_reasoning_effort = "low"`, **`model_context_window = 872000`**, **`model_auto_compact_token_limit` 不在**, `default_subagent_model = "gpt-5.6-sol"`, `default_subagent_reasoning_effort = "high"` | OBSERVED |
| Codex 認証 type | `auth_mode = chatgpt`、`OPENAI_API_KEY` なし、tokens オブジェクト存在 | 同 | OBSERVED（type/有無のみ） |
| Codex カタログ（box models_cache） | `gpt-6-astra`, `gpt-reserve`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5.5`, `gpt-5.3-codex-spark`, `codex-auto-review`。5.6+/astra: `context_window=272000`, **`max_context_window=872000`**; gpt-5.5: 272000/272000; spark: 128000 | — | OBSERVED |
| 案件ログ `autopilot-log` | これらの ID の案件ログとしては未発見（repo には `codex-home/skills/codex-autopilot` のみ） | — | OBSERVED（不在） |

設定優先順位（FROM_PUBLIC_DOC）:
- Claude Code: Managed → CLI `--settings`/flags → `.claude/settings.local.json` → `.claude/settings.json` → `~/.claude/settings.json`。env はキーごとに対。`/status` で出所確認、`claude doctor` で拒否確認。
- Codex: `~/.codex/config.toml` + 信頼済みプロジェクト `.codex/config.toml` + プロファイル。プロジェクト側は provider/auth/telemetry を上書きできない。

## 4. 公開仕様（2026-09-16 取得。10 URL すべて取得成功。導入先で再照合）

**Claude Code**（`code.claude.com/docs/en/prompt-caching`, `sub-agents`, `settings`, `context-window`, `hooks`, `scheduled-tasks`）
- キャッシュは厳密な先頭一致。無効化: モデル切替（自動フォールバック含む）、effort 変更（**Fable 5.1 + サブスク/API key 経路は例外で保持**）、fast mode 初回、MCP ツール定義変化、`/compact`、多数画像、CC 版更新。保持: ファイル編集、CLAUDE.md 途中編集（clear/compact/restart まで未反映）、権限モード、skills、`/recap`、rewind、**サブエージェント起動**。
- **TTL バケット**: 主会話 と「それ以外」（サブエージェント・ワークフロー・チームメイト・フォーク・圧縮補助・タイトル）。サブスク枠内: 主会話 **1h**／それ以外 **5m**。usage credits／API key／cloud: 両方 **5m**。
- 上書き（v2.1.242+）: `promptCacheTtl` / `CLAUDE_CODE_PROMPT_CACHE_TTL`、`subagentPromptCacheTtl` / `CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL`（`5m`|`1h`）。個別（v2.1.248+）: エージェント frontmatter `experimental: { cacheTtl: 5m|1h }`（`experimental` 配下のマップ。usage credits 下では 1h 無視）。優先: FORCE_5M → env → setting → experimental.cacheTtl → ENABLE_1H → 既定。
- サブエージェント初回は親キャッシュを**読まない**。フォークは読める（作成時点のコピー）。TTL 書込みの確認は `usage.cache_creation.ephemeral_1h_input_tokens` vs `ephemeral_5m_input_tokens`。
- サブエージェント: 自前コンテキスト・system prompt・ツール、親へ要約を返す。モデル順: 呼出 → frontmatter → `CLAUDE_CODE_SUBAGENT_MODEL` → 親。ネスト既定3、同時既定20。自動圧縮はサブエージェントにも適用、`CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` 有効。
- 圧縮時に CLAUDE.md／自動メモリ／プランをディスクから再読込、直近最大5ファイル再読、skills は上限付きで再注入。Fable／Sonnet 5／Opus 4.6+ は plan により 1M（`[1m]`）。
- Hooks: SessionStart/End、UserPromptSubmit、Pre/PostToolUse、SubagentStart/Stop、**PreCompact/PostCompact**、Stop、Notification（**`idle_prompt` matcher あり**）等。hook はコマンド／HTTP／MCP／prompt／agent を実行。**「40分後」と記録する hook だけではアイドルのモデルは起きない。** SessionStart（resume）は `prompt_cache_likely_expired`、`seconds_since_last_response`、`estimated_cache_write_usd` を含み得る（v2.1.251+）。
- `/loop`・CronCreate/List/Delete は**セッションスコープ**（開いたセッション必須、`--resume` で復元あり・自走 `/loop` は復元されない）。最短1分、繰返しは7日失効、ジッター。代替: Cloud Routines（最短1h）、Desktop scheduled tasks（開いたセッション不要）、GitHub Actions。`CLAUDE_CODE_DISABLE_CRON=1` で無効。

**Anthropic API**（`platform.claude.com/docs/en/build-with-claude/prompt-caching`）
- 既定 TTL 5分、任意 `ttl: "1h"`。寿命は書込み／読込み**リクエスト開始**から（ストリーミングが TTL を食う）。ヒットで更新。
- Fable 5.1 価格: 基本入力 $10/MTok、キャッシュ読み **$0.25（0.025×）**、5分書き 1.25×、1h 書き 2×、出力 $50。最小キャッシュ可能プレフィックス 512 tokens。（Fable 5（5.1 以前）は読み 0.1×。Opus 5 読み $0.50、Sonnet 5 読み $0.20。）**→ すべて API 価格。サブスク枠の倍率ではない。**

**OpenAI**（`developers.openai.com/api/docs/guides/prompt-caching`, `compaction`, `codex/config-reference`）
- GPT-5.6+: `prompt_cache_options.ttl` は **`30m` のみ**（既定）。書き 1.25×、読み 0.1×、最小 1024 可視トークン。旧モデルは `prompt_cache_retention` `in_memory`／`24h`。Agents API 同挙動。**「セッション維持はヒット保証ではない。」** 圧縮／ツール／effort／verbosity 変更で先頭が崩れる。
- サーバー側圧縮: `context_management` の `compact_threshold`（例 200_000）、`/responses/compact`。圧縮アイテムは**不透明**（人が読めない）。
- Codex 設定: `model_auto_compact_token_limit`（数値）、`model_auto_compact_token_limit_scope`（`total` 既定 | `body_after_prefix`）、`model_context_window`、`default_subagent_model`、`default_subagent_reasoning_effort`。hooks に PreCompact/PostCompact 名あり。

**Cursor（参考、cache-facts）**: プロバイダのキャッシュのみ。Cursor は温め直しをしない（staff）。Anthropic ~5m スライディング、GPT-5.6+ 30m。

## 5. 軍議（Fable 5.1）の裁定 — 設計書はこれを起点にし、異論があれば根拠付きで書く

### 5.1 目的の置き直し（AI提案）
本案件の目的はキャッシュ最適化ではない。**「Fable 親を一日単位で走らせ続け、子を使いながら、本人が離席・圧縮を管理せず、サブスク枠あたりの成果を最大化する」**。TTL・200K・40分は手段。キャッシュヒット率は計測項目であって目的ではない。

### 5.2 評価軸（設計書は案をこの軸で比較する）
- E1 手離れ（必須）／E2 文脈無欠損（必須。BRIEF §9 の10項目: 目標・最新本人決定・禁止・未回答・未承認操作・未回収子結果・現在ファイル版・重要根拠・失敗と未検証・次の一手）／E3 枠あたり成果（`/usage` 等の**観測できる**指標。API $ は補助）／E4 非割り込み（必須）／E5 局所性・戻し／E6 証拠品質（必須。ラベル・計測値のみ）／E7 認可遵守（必須）／E8 予測失敗の被害（離席予測が外れて圧縮したときの損失）。

### 5.3 最大のレバーは「親に入る情報量」
Astra/Sol/Terra/Luna は全て OpenAI カタログのモデル（OBSERVED）＝別ベンダー。**親 Fable とキャッシュを一切共有しない。** Claude 組み込み子も初回は親キャッシュを読まない。よって親の消費は「子から親へ返す差分の短さ」と「親履歴の圧縮タイミング」で決まる。R3 §D（差分報告）を**第一層**へ昇格。

### 5.4 40分温圧縮の価値を読み替える
API 単価（読み 0.025×）で成立する「節約」はサブスク枠では UNVERIFIED。読み替え: **「製品の自動圧縮が作業中の悪いタイミングで発火する前に、安全な区切りで、引継ぎ保存済みの状態で、一度だけ圧縮する」= 圧縮タイミングの制御。** 温かさはおまけ。これにより Test 0 の結果（枠が cached を区別するか）に設計が依存しない。本人希望「温かいうちに圧縮」は否定せず、ゲート付きで実現する。

### 5.5 判定は外・実行は中・引継ぎは常時
- アイドル判定をモデル呼び出し（cron で「暇なら圧縮せよ」）で行うと、それ自体が空打ち延命と同じコスト（**F2**）。判定は hook が書いたタイムスタンプを OS 側の**通常スケジューラー**（新デーモンではない）が読む。モデル呼び出しは圧縮の**一回**だけ。
- 引継ぎファイルは作業中に常時更新（追加プロセス不要）。圧縮・失効・スリープ・枠到達のどれでも「引継ぎから戻れる」を基線にする。

### 5.6 親の起動形態が第一の決定事項
対話TUI／`claude -p --resume <id>` を回すハーネス／Agent SDK・app-server／Desktop のどれか **UNVERIFIED**。TUI なら外部から同一セッションへ圧縮を確実に起こす経路は現時点で見当たらず **P4（遅延判断）** が基線。ハーネスなら P-A（ハーネス自発）が最有力。

### 5.7 `~/.claude/agents/` 不在
個別 `experimental.cacheTtl` の差分は、**まずどの子をカスタムエージェントとして定義するか**を決めないと置き場がない（**F17**）。

## 6. 01方向案「外で判定・中で一回・常時引継ぎ」（AI提案。R3 の最小差分 A〜D は捨てずに順序・前提・ゲートを付ける）

### T0 前提表（設計書の最初の成果物）
(1) 親の起動形態を1行で確定（不明なら確認手順＋形態別分岐）。
(2) 子 spawn 経路表: (a) Claude 組み込みサブエージェント（5m 既定・個別1h可・初回継承なし）／(b) Claude フォーク（作成時点コピー）／(c) 別プロセス `claude` 主会話（**1h**）／(d) 別プロセス `codex`（OpenAI 30m・親と非共有・圧縮アイテム不透明）／(e) Codex 内部サブエージェント（既定 sol/high。閾値継承 UNVERIFIED）。子ロールごとに1行。空欄は UNVERIFIED＋確認手順。

### T1 無条件層（設定変更なし）
- **D 差分報告規約**: 子へ渡す＝目標／完成条件／変更禁止／認可範囲／資料参照先＋版／未解決点。親へ返す＝**変更時のみ**、固定テンプレ `完了／残り／詰まり／親に必要な判断／成果・証拠の参照先＋版`。巨大ログ・Codex 圧縮アイテム・全文成果は正本ファイルへ、親は参照先のみ。軽微報告は**既存**キュー・重複防止で機械集約（新台帳を作らない）。親増分（子1件あたり）を測る。
- **H 常時引継ぎ**: 親は意味ある区切りごとに引継ぎファイル（§9 の10項目）を更新。PreCompact hook で鮮度確認。圧縮後の再読込は製品仕様（CLAUDE.md／プラン／直近ファイル再読）に乗せる（CLAUDE.md から引継ぎを参照させる案を検討）。
- **I 子の隔離**: Codex 子は別プロセス＋子だけが読む設定層。ユーザー全域の `model_context_window = 872000` は触らない。Claude 1h 候補の子は**先にカスタムエージェント定義として切り出す**。

### T2 条件付き層（子側設定。適用は別認可。R3 §A/§B）
- **A Claude 子 個別 1h**: 5分以上空いて同じ履歴へ戻る子のみ、agent frontmatter に `experimental: { cacheTtl: "1h" }`。短い子は 5m。前提: (a) 経路であること／定義ファイル存在／env・`subagentPromptCacheTtl` が上書きしていない。検証: `ephemeral_1h_input_tokens` 立つ＋ >5m <1h 再訪で `cache_read`。**一律 `subagentPromptCacheTtl: "1h"` は不採用。**
- **B Codex 子 200K total**: 子スコープ層にのみ `model_auto_compact_token_limit = 200000` / `model_auto_compact_token_limit_scope = "total"`（`total` は既定＝意図の明示）。窓は 872000 のまま。**270000 へ戻さない。** 大きな原資料の同時比較が本質の仕事は例外。検証: 圧縮の**開始と完了**＋前後アクティブ文脈量。まず低い仮閾値で機構確認→200K 近辺で1回。閾値を下げるほど得と考えない。

### T3 二重ゲート層（親の休止前一回圧縮。本人希望の実現層）
ゲート全成立で有効化。1つでも不成立なら P4 基線のまま。
- **G1 経路**: 起動形態に対応する「同一親セッションへ実モデル呼び出し／正式圧縮を起こす経路」が試験セッションで1回実証。
- **G2 外判定**: A・B の判定が hook タイムスタンプ＋OS 通常スケジューラーで行われ、**非アイドル時にモデル呼び出しゼロ**を実証。
- **G3 一回性**: 発火1回で止まり、圧縮後に再発火・延命ループなし。活動再開で予約が取り消される。
- **G4 温度確認**: 発火時に A を再計算。失効推定なら**圧縮しない**（冷たい圧縮を温かいと偽装しない）→ P4。
- **G5 サイズ閾値**: 親コンテキストが縮める価値のある規模を超えている（数値候補を設計書で）。小さければ省略。

**P4 基線（遅延判断）**: 休止中は無操作。再開時に SessionStart（resume）の `prompt_cache_likely_expired` / `seconds_since_last_response` を読み、失効前なら続行、失効後は「続ける（冷たい再書込み1回）」か「引継ぎから新セッション」かを**規則で**決める（本人に選ばせない）。規則候補（休止 X 時間超・親サイズ Y 超）を設計書で定める。

**時計（BRIEF §8 の A/B を観測源まで落とす）**:
- A（最終キャッシュ接触）: 本来「最後にプレフィックスを読み書きしたリクエストの**開始**時刻」。観測可能な近似は **Stop hook 時刻（最終応答終了）**。真の A より**遅い**ので「温かい」側に楽観的。最終ターン所要 < 余裕（60−40=20分）を前提にし、長い最終ターンは G4 で保守的に扱う。**推定と明示。**
- B（実活動）: UserPromptSubmit／認可済み作業の意味ある進捗。空の延命通知・キュー登録・子の活動だけでは B を更新しない。
- 発火条件: `now − A_est ≥ 40分` ∧ B 新規なし ∧ 親が推論中・ツール中・圧縮中でない ∧ G4 ∧ G5。
- **40分は導出値**（TTL 60分 − 最終ターン所要 − スケジューラーのジッター − 圧縮所要の余裕）。固定値として書かない。

**状態別処理**（BRIEF §8）: 作業中（割り込まない）→ 子待ち（機械集約→意味ある確認→親だけ圧縮して待つ案と比較。無限延命しない）→ 休止可能（G1–G5→引継ぎ保存→一回圧縮）→ 圧縮後（休止。再圧縮・延命なし。本人再開／認可済み結果で復帰）→ 失効・不明（偽装しない。P4）。設計書は**状態遷移図**にする。

### 経路候補（G1 の材料。すべて UNVERIFIED）
| 経路 | 仕組み | 致命点 |
|---|---|---|
| P-A ハーネス自発 | `claude -p --resume <id>` を回すハーネスが外判定成立時に圧縮ターンを1回発行 | 親が TUI なら不可。ハーネス存在 UNVERIFIED |
| P-B セッション内 Cron/`/loop` | 親がターン末に A+40分の発火を予約 | 発火＝モデル呼び出し。非アイドル発火は **F2**。予約更新が親トークンを食う。one-shot 可否・取消可否 UNVERIFIED。7日失効・ジッター |
| P-C `idle_prompt` hook → OS one-shot → `claude --resume -p` | hook が A/B を書き、OS の一回実行タイマー（Windows タスクスケジューラ once／`systemd-run --on-active` 等）が期限に外判定→再開して圧縮 | 対話セッション開放中の `--resume` は**競合／フォーク**の恐れ。`-p` でスラッシュコマンド可否 UNVERIFIED。再開が同一プレフィックスを温かく読むかも UNVERIFIED |
| P-D Desktop scheduled task | 開いたセッション不要 | ほぼ確実に**別セッション**＝親の圧縮にならない。候補外 |
| P-E Cloud Routines | 最短1h | 40分に届かない。org/課金要確認。候補外 |
| P4 遅延判断 | 休止中無操作、再開時に規則判断 | 温かい圧縮は得られない。冷たい再書込み1回、または引継ぎ再開の情報損失 |

裁定: **P4 を必ず実装**。P-A（ハーネスがあれば）→ P-C → P-B の順で G1〜G3 を実証。P-D/P-E は同一セッション圧縮の手段に数えない。

## 7. 失敗モード（設計書は各項に対策と試験番号を付ける）

F1 予測失敗（40分で圧縮→45分で本人復帰。詳細消失＋要約コスト）／F2 偽装延命（cron 定期プロンプトで判定）／F3 別セッション（スケジューラーが新セッションを起こす）／F4 再開競合（対話開放中の `--resume`）／F5 圧縮中の子結果・本人入力（消失／二重反映。既存キュー＋重複防止で一度だけ反映）／F6 枠到達（5時間／週間。extra usage は org 無効→親停止→TTL 失効→冷たい復帰。無限再試行しない）／F7 一律 TTL（圧縮補助・タイトルにも 2× 書き）／F8 Codex 圧縮スラッシング（200K total で繰返し・未完了）／F9 優先順位で無言の 5m（env/setting が個別を上書き）／F10 版差（PC 2.1.260／box 2.1.270）／F11 コールドスタート（親モデル切替。effort 変更は Fable 5.1 サブスクで保持＝FACT、要確認）／F12 換算誤用（0.025× を枠倍率）／F13 スリープ・通信断（A 失効済みなのに温かい扱い→G4）／F14 引継ぎ陳腐化（PreCompact で鮮度確認・区切り更新の規約化）／F15 不透明データ流入（Codex 圧縮アイテム・巨大ログを親へ）／F16 子の初回コールド（組み込み子は親キャッシュを読まない→子へ渡す情報最小化）／F17 定義不在（カスタムエージェントがないのに個別 TTL）。

## 8. 不採用・却下（理由付きで設計書に残す）

cron/`/loop` による「暇なら圧縮」判定（F2）／Desktop scheduled task を親圧縮に数える（F3）／40分を固定値で書く／キャッシュヒット率を目的関数にする／API $ 換算でサブスク節約を断定／一律 `subagentPromptCacheTtl: "1h"`／`model_context_window = 270000` へ戻す／LLM（Luna 等）を時計にする／40分ごとの一文字送信／1M ダミー／新デーモン・常駐監視・新台帳・時計専用 LLM／Claude を API key・usage credits へ切替／Codex に新規 API key／役割名「子」だから 5m と決める／「子を圧縮したから親も軽くなる」／同モデル通常子を親のフォークと呼ぶ／読んでいない資料を読んだ扱い（R5）。

## 9. 隔離試験計画（Fable 版。1M ダミー禁止。設計書は合否基準・停止条件・記録項目を確定する）

| # | 名称 | 目的 | 規模 | 合格 | 停止 |
|---|---|---|---|---|---|
| T0 | 枠感度 | サブスク枠が cached/uncached 入力を区別するか | 安定プレフィックス 15–30K tokens を (i) cold (ii) 直後 warm (iii) 6–10分後 (iv) 65分後 に各1回。`/usage` の%差・`cache_creation` 内訳 | 差の有無を**明記**。断定しない | 4回で終了。粒度不足なら「計測不能」で終了し、設計は温かさ依存を外す |
| T1 | 設定読込（乾式） | 試験子が実際に読む agent ファイル／Codex 層、版、認証 type | 0〜1 呼び出し | 読込元特定 | — |
| T2 | Claude 個別 TTL | `experimental.cacheTtl: "1h"` 有／無の双子、8–15分空けて2ターン | 小プレフィックス | 有: `ephemeral_1h` 書込み＋2ターン目 `cache_read`。無: `ephemeral_5m`＋再書込み | 証拠が出たら終了 |
| T3 | Codex 圧縮 | 200K/total で圧縮**開始と完了**、前後サイズ | 低い仮閾値で機構確認→200K 近辺で1回 | 完了ログ＋前後サイズ | 1回完了で終了。未完了は F8 記録 |
| T4 | 外判定（G2） | hook（UserPromptSubmit／Stop／idle_prompt）が A/B を書き、OS one-shot が期限に判定。**非アイドル時にモデル呼び出しゼロ** | 試験セッション | 非アイドル時の API 呼び出し記録なし | — |
| T5 | 経路（G1/G3/G4） | 選んだ経路で**試験親**に一回圧縮。セッションID一致、再発火なし、A 失効時は圧縮しない | 試験セッション1回 | 同一セッションで PreCompact/PostCompact が1回だけ | 2回目が起きたら即停止 |
| T6 | 差分報告 | 子が短文テンプレのみ返し、親増分を測る | 子1〜2件 | 親増分が規約内 | — |
| T7 | 引継ぎ再開（P4） | 引継ぎファイルから新セッションで復帰、§9 の10項目が揃う | 1回 | 10項目照合 | — |
| T8 | 安全 | 圧縮中の子結果到着／スリープ／枠到達模擬 | 各1回 | フェイルセーフ停止、無限再試行なし | — |
| 記録 | — | 全項目に FACT/UNVERIFIED、版、認証 type。節約%は計測値のみ | — | — | — |

## 10. 設計書に含める章（この順で。省略不可。各章末に「本章の UNVERIFIED」を列挙）

0. 受付ID復唱／読了台帳（読めた・読めなかった・依頼文経由）
1. 目的と評価軸（§5.1–5.2 を採用または修正。修正なら根拠）
2. 前提表 T0: 親の起動形態（確定または確認手順＋形態別分岐）／子 spawn 経路表（ロールごと）
3. 主張の分離台帳: 本人希望／AI提案／公開仕様（URL＋取得日）／実機未確認
4. 設計本体: T1（D・H・I）／T2（A・B の最小差分: ファイルパス・キー・YAML/TOML 本文・前提・検証）／T3（G1–G5・P4 規則・A/B の観測源・発火条件・40分の導出式・状態遷移図）
5. 経路の試験順（P-A → P-C → P-B）と各経路の合否基準
6. 引継ぎファイル: 置き場・形式（§9 の10項目）・更新契機・PreCompact 鮮度確認・圧縮後再読込への乗せ方
7. 差分報告テンプレ（固定文）と既存キュー・重複防止への接続（新設なし）
8. 隔離試験計画（§9 を確定。合否・停止・記録）
9. 失敗モード F1–F17: 対策と対応試験番号
10. 不採用案と理由
11. 戻し表（変更ごとに1操作。R3 の表を継承・更新）
12. 追加認可が必要な操作（R3 の表を継承・更新。現認可で可能な範囲も明記）
13. 本人向け一画面要約（平易。本人が決める部分のみ。技術操作・伝言を戻さない）
14. UNVERIFIED 総覧と、次に確認すべき順序

## 11. 設計書の書式

- 日本語。表を多用。各主張にラベル（`OBSERVED` / `FROM_PUBLIC_DOC` / `UNVERIFIED` / `本人希望` / `AI提案`）。
- 数値は出所を付ける（例: 872000 = PC `~/.codex/config.toml` OBSERVED）。
- 「節約 N%」「N倍安い」は計測値がない限り書かない。API 単価の比較を書く場合は「API 価格表上」と明記し、サブスク枠への適用は UNVERIFIED と併記。
- 設定差分はコピーできる本文（YAML/TOML）とファイルパス、前提版、検証方法、戻し方をセットで。
- 「保存」「相手による検知」「読解」「設定適用」「動作検証」を別々の状態として記録する（R5）。
- 秘密を書かない。
- 冒頭に受付ID `AI-CACHE-PARENT-SUBAGENT-20260916-FABLE51` を復唱。

## 12. あなたが答えるべき問い（設計書の中で明示的に回答）

1. 親の起動形態は何か。不明なら確認手順と形態別の分岐。
2. 子ロール（Astra／Sol／Terra／Luna／Claude 子）ごとの spawn 経路。空欄は UNVERIFIED＋確認手順。
3. Test 0 の設計。計測不能な場合の設計上の扱い。
4. G1–G5 の合否基準と試験手順。P4 の規則（X・Y）。
5. 引継ぎファイルの置き場・形式・更新契機・圧縮後再読込への乗せ方。
6. D のテンプレ固定文と機械集約の既存経路。
7. Codex 子の設定層（プロファイル／信頼済みプロジェクト）と読込確認。Codex 内部サブエージェントへの継承可否。
8. Claude 子の 1h 対象の具体名（存在しないなら「まず定義」）。
9. F5／F6／F13 のフェイルセーフ。
10. 戻し表・追加認可表。
11. 本人向け一画面。
12. 軍議の裁定に**異論**があれば、どの評価軸でどう優劣が変わるかを根拠付きで。

## 13. 出力の終わり方

- 設計書本文の末尾に「本設計書は候補であり未適用。適用・隔離試験の実施は別認可。」を明記。
- 本人への伝言・再説明・GitHub 転記依頼を書かない。
- 読めなかった資料があれば、末尾ではなく冒頭の読了台帳に書く。

---

## 貼り付けここまで

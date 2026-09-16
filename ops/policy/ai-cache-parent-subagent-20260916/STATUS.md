# AI-CACHE-PARENT-SUBAGENT-20260916 STATUS

- 版: GROK-CACHE-CONTEXT-20260916-R3 → **FABLE51 軍議完了**
- 状態: **軍議完了（方向裁定）・Pro 未送信**。設計書は未作成（MAIN 6.0 Pro が `PRO-PROMPT-MAIN60-AI-CACHE.md` を受けて書く）。採用済み／全案件適用／常駐有効化はしない。設定未適用。
- 認可: 理解・記録・現状確認・設計・隔離検証準備まで。Claudeサブスクのみ。Codex既存認証のみ。API従量・usage credits・自動課金禁止。
- 入口: rimone0511/codex-general `PRO_CONTEXT.md` を R3 パスで `gh api` 取得・読了（R5接続確認方針）。**軍議パス（Cursor cloud agent）からは codex-general に到達不能（404）→ 軍議は R3 要約経由。Pro は自ら接続確認する。**
- 関連: GROK-FABLE-SUPERVISOR-ORCH-20260915（ローカル `ops/policy/fable-supervisor-orch-20260915` + GitHub event）

## 成果物

### R3 パス（2026-09-16 ~09:15 JST、PR #126 `cursor/ai-cache-parent-r3-20260916`）

| File | Role |
|---|---|
| `INVENTORY.md` | Box + PC 版／モデル／Effort／認証type／設定パス・優先順位（秘密なし）。FACT/OBSERVED/FROM_PUBLIC_DOC/UNVERIFIED |
| `DOCS-CHECK-20260916.md` | 指定10 URL取得サマリ（全OK） |
| `DESIGN-CANDIDATE-R3.md` | 本人希望/AI提案/公開仕様/実機未確認分離 + 最小差分候補 + 不採用 + 隔離試験 + 戻し + 追加認可 |
| `BRIEF-R3-full.md` | 既存引継ぎ（入力） |
| `STATUS.md` | 本ファイル |

### FABLE51 軍議パス（2026-09-16 ~00:10–00:40 UTC = ~09:10–09:40 JST、ブランチ `cursor/ai-cache-gungi-fable51-2daf`）

| File | Role |
|---|---|
| `FABLE-GUNGI-20260916.md` | 軍議記録: 目的の置き直し・評価軸 E1–E8・01方向案「外で判定・中で一回・常時引継ぎ」（T0 前提表／T1 無条件／T2 子設定／T3 二重ゲート＋P4 基線）・経路候補比較・失敗モード F1–F17・却下罠・Pro への問い・隔離試験 T0–T8。**設計書ではない。** |
| `PRO-PROMPT-MAIN60-AI-CACHE.md` | MAIN ChatGPT 6.0 Pro 向け貼り付け用依頼文（受付ID提案 `AI-CACHE-PARENT-SUBAGENT-20260916-FABLE51`）。インベントリ事実・公開仕様・裁定・失敗モード・試験計画・設計書の章構成を内包。**未送信。** |

## 進捗メモ

### 2026-09-16 朝（事前）
- BRIEF-R3-full.md 保存済
- PRO_CONTEXT / cache-facts 接続方針

### 2026-09-16 ~09:15 JST（本実行）
- 公式Docs 10本 fetch → DOCS-CHECK
- Box: Claude **2.1.270**, Codex **0.154.0**, Claude OAuth subscription, Codex `auth_mode=chatgpt`（API keyなし）
- PC `DESKTOP-EVCBN4H`: Claude **2.1.260**, settings `model=opus[1m]` effort high, TTL overrides unset; Codex config `model=gpt-5.6-luna`, **`model_context_window=872000`**, auto-compact limit **未設定**, default subagent sol/high; `codex` PATH未解決でPC版UNVERIFIED
- GitHub events 接続:
  - `pro-chat/events/AI-CACHE-PARENT-SUBAGENT-20260916/` ×3（discussion v1, keepalive-fork v2, proposal R3）
  - `pro-chat/artifacts/AI-CACHE-PARENT-SUBAGENT-20260916/grok-cache-context-brief-r3.md`
  - `pro-chat/events/GROK-FABLE-SUPERVISOR-ORCH-20260915/20260916T001200+0900_artifact-design-v1.json`
- `autopilot-log` 案件ログは未発見（skills/codex-autopilot のみ）
- **設定変更・常駐・課金操作なし**

### 2026-09-16 ~00:10–00:40 UTC（FABLE51 軍議・Fable 5.1）
- 入力読了: uploads 5本（PR #126 と同一内容を確認）＋ `BRIEF-R3-full.md`（PR #126 ブランチから取得）＋ PR #126 本文
- 到達不能: `rimone0511/codex-general`（404）→ PRO_CONTEXT／イベント本文は読了扱いにしない
- 裁定要点:
  - 目的を「キャッシュ最適化」から「親 Fable の一日連続運用・本人手離れ・枠あたり成果」へ置き直し
  - 最大レバーは子側 TTL ではなく **親に入る情報量**（差分報告 D を第一層へ）。Astra/Sol/Terra/Luna は OpenAI 側＝親とキャッシュ非共有
  - 40分温圧縮の価値を「節約」→「圧縮タイミングの制御（温かさはおまけ）」に読み替え。サブスク枠での 0.025× 相当は UNVERIFIED のまま
  - **判定は外・実行は中・引継ぎは常時**。cron 定期プロンプトでの判定は偽装延命（F2）として却下
  - **親の起動形態（TUI／`-p --resume` ハーネス／SDK／Desktop）が設計書の第一決定**。TUI なら P4（遅延判断）基線
  - `~/.claude/agents/` 両ホスト不在 → 個別 TTL 差分は「子の定義」から
- Pro 依頼文 `PRO-PROMPT-MAIN60-AI-CACHE.md` 作成（受付ID提案 FABLE51）。**送信していない。**
- **設定変更・常駐・課金操作・API鍵発行なし**

## 次（別認可後）

1. **Pro 送信**: `PRO-PROMPT-MAIN60-AI-CACHE.md` 本文を MAIN ChatGPT 6.0 Pro へ貼り付け → 設計書 `DESIGN-FABLE51.md` を受領・保存（保存≠適用）
2. 設計書受領後、T0 前提表（親の起動形態・子 spawn 経路）を実機で埋める
3. 隔離試験 T0–T8（軍議 §9 / DESIGN §Isolated test plan）— 1Mダミー禁止
4. 採用時のみ最小差分を子スコープに適用
5. 親40分（T3）は G1–G5 全成立が条件。不成立なら P4 基線のまま

## Blockers

- **親 Fable の起動形態が未確認**（軍議で最上位ブロッカーに格上げ。TUI か ハーネス かで T3 の実現可否が変わる）
- 親セッションへ確実に compact を起こせる経路が未実証（P-A / P-C / P-B いずれも UNVERIFIED）
- サブスク枠が cached/uncached 入力を区別するか未計測（T0。粒度不足の可能性あり）
- 子ごとの spawn 経路（in-process subagent vs 別メイン会話 vs 別 codex プロセス）未分類
- カスタムエージェント定義が存在しない（`~/.claude/agents/` 不在）
- PC Codex CLI version / PATH
- 実キャッシュヒット計測未実施
- codex-general への接続は Pro 側で要確認（軍議パスは 404）

# 原典（骨格用）

秘密・トークン・Drive ファイル ID・金庫パスは書かない。  
リポジトリに並列キャップ APPLY 原文は無かった。以下は照合できた題名と日付。

## この窓の直接源

- HANDS 指示 2026-09-16（初回）: APPLY-WINDOW 骨格。max Cursor Grok / SWE-2 / CU=1 / refill-on-empty。当時は `{{PRO_NUMBER}}` 待ち
- HANDS 指示 2026-09-16（回収）: Pro **PARALLEL-CAP-PERF** を回収。適応設計へ置換。全文は貼らない
- 回収内容の範囲（題名だけ。数値の max は含まない）:
  - ~10/~10 = `LEGACY_UNVERIFIED` 移行境界のみ。証明済み maxima ではない
  - CU = 1 always
  - GREEN: time ratio <= 1.10 + quality pass + no RL/stall/resource/acceptance degrade → trial +1 してよい
  - YELLOW: stop growth。RED: lower affected resource cap。HARD: close affected op
  - shared cross-model caps。one reconcile function。no wait-only Pro workers。no duplicate fake parallelism
  - 最適数はライブ観測まで UNKNOWN
- 未回収（隣接）: GROK-FOUNDATION-COST（MAIN 6 Pro 再送中）。この窓の数字の代用にしない

## 兄弟下書き（同じリポジトリ、未マージ）

- `ops-bake-orch-cli-20260916/` — ORCH 振り分け順 / CU mutex=1 / SWE-2 prefer / Effort は観測 / Head ON / Hands~0。並行**数**は焼いていない

## 本人決定・共有記憶（Notion。題名と日付だけ）

- 外部AI運用｜SWE-2優先と役割分担（2026-09-13、本人）
- AI運用｜費用を抑えて品質を保つ（2026-09-13）
- 引継ぎ｜会話統合と設定・記憶連携（2026-09-13）
- 実装契約｜Sol Highへの引継ぎ（2026-09-13）
- 確定要件｜キャッシュ・文脈・費用管理 v2.0（CLI-CACHE-CONTEXT-20260913 v2.0）
- Pro総点検｜会話統合・共有記憶 rev2（INTEGRATED-GOAL-AUDIT-20260913）— G1 は 15 並行を証明しない
- 今日の看板｜一目でわかる（2026-09-15: MAIN Pro 枠 0%）

## 使わなかったもの

- 引継ぎ文面の「10〜15担当まで並行」— CLI 整備の話であり、この窓の Grok/SWE-2 キャップではない。数字としても焼かない
- Codex 並列バッチ mutex の旧 RED 試験ログ（CU mutex=1 の実装仕様ではない）
- 料金・TTL・並行数の推定。固定 10/10 max の復元
- Drive 上の `parallel-capture-regression` フォルダ群（別案件。ID は書かない）
- GROK-FOUNDATION-COST の想像復元

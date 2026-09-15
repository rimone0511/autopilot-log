# 原典（observer スタブ用）

秘密・トークン・Drive ファイル ID・金庫パスは書かない。  
リポジトリに並列キャップの本番 observer は無かった。以下は照合できた題名と日付。

## このスタブの直接源

- HANDS 指示 2026-09-16: `ops-parallel-cap-observer-stub-20260916/` を作り、PARALLEL-CAP-PERF の薄い規則（台帳状態、GREEN/YELLOW/RED/HARD、CU=1、LEGACY_UNVERIFIED~10）を擬似コードと Markdown だけに残す。本番未適用。最適 N は UNKNOWN。秘密なし
- 案件名 **PARALLEL-CAP-PERF**（並列キャップの薄い規則。MAIN Pro 再送系。看板は MAIN Pro 枠 残り 0%。このスタブは Pro 全文を想像復元しない）

## 兄弟下書き（同じリポジトリ、未マージ）

- `ops-parallel-cap-bake-skeleton-20260916/` — APPLY-WINDOW の骨格。max Grok / SWE-2 / CU / refill-on-empty は `{{PRO_NUMBER_*}}`。ソフト暫定 GO は ~10+~10（Pro まで）。数字は焼いていない
- `ops-bake-orch-cli-20260916/` — ORCH 振り分け順 / CU mutex=1 / SWE-2 prefer / Effort は観測 / Head ON / Hands~0。並行**数**は焼いていない

## 本人決定・共有記憶（Notion。題名と日付だけ）

- 外部AI運用｜SWE-2優先と役割分担（2026-09-13、本人）
- AI運用｜費用を抑えて品質を保つ（2026-09-13）
- 引継ぎ｜会話統合と設定・記憶連携（2026-09-13）
- 実装契約｜Sol Highへの引継ぎ（2026-09-13）
- 確定要件｜キャッシュ・文脈・費用管理 v2.0（CLI-CACHE-CONTEXT-20260913 v2.0）— 新しい司令塔・監視専用モデル・管理だけの台帳や常駐サービスを既定にしない
- Pro総点検｜会話統合・共有記憶 rev2（INTEGRATED-GOAL-AUDIT-20260913）— G1 は 15 並行を証明しない。新しい監視台帳・人数埋めの並列処理は作らない
- 今日の看板｜一目でわかる（2026-09-15: MAIN Pro 枠 0%）

## 使わなかったもの

- 引継ぎ文面の「10〜15担当まで並行」— CLI 整備の話。このスタブの Grok/SWE-2 キャップでも最適 N でもない
- Codex 並列バッチ mutex の旧 RED 試験ログ（CU mutex=1 の実装仕様ではない）
- 料金・TTL・最適 N の推定、負荷試験の数字
- Drive 上の `parallel-capture-regression` フォルダ群（別案件。ID は書かない）
- 未回収 Pro 本文の想像復元
- 兄弟 APPLY-WINDOW の `{{PRO_NUMBER_*}}` を観測値へ写すこと

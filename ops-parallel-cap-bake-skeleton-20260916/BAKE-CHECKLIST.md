# BAKE-CHECKLIST（並列キャップ）

状態: **PARALLEL-CAP-PERF 回収済み。** 窓のトークン置換は適応設計まで完了。本番 APPLY は未。  
固定 10/10 を max にして完了扱いにしない。

焼き込み先は本番の憲法・CLI・Bot ではなく、まず [APPLY-WINDOW.md](APPLY-WINDOW.md)。本番 APPLY は別作業。

---

## A. 入力が揃うまで

- [x] Pro 案件 **PARALLEL-CAP-PERF** の本文を回収した（再送中・枠 0% のまま想像しない）
- [x] 回答の版・日付・座席を SOURCES に題名だけ足した（秘密・全文は貼らない）
- [x] ソフト暫定 GO（~10/~10）を最終値と読み替えなかった → `{{LEGACY_UNVERIFIED}}`（移行境界のみ）
- [x] 兄弟 `ops-bake-orch-cli-20260916/` の CU mutex=1 と食い違わない → CU = 1 always

## B. トークン置換（APPLY-WINDOW のみ）

`{{PRO_NUMBER_*}}` は使わない。固定人数で埋めない。

- [x] max Cursor Grok ← `{{UNKNOWN}}`（shared。~10 は `{{LEGACY_UNVERIFIED}}` のみ）
- [x] max SWE-2 ← `{{UNKNOWN}}`（shared。~10 は `{{LEGACY_UNVERIFIED}}` のみ）
- [x] CU ← **1 always**（上げない。Pro と兄弟ロックが一致）
- [x] refill-on-empty ← `{{ADAPTIVE}}`（固定 N は無し。GREEN の trial +1 / reconcile 1 本）
- [x] 本文に `{{PRO_NUMBER}}` が残っていない
- [x] ~10 や 15 を「近いから」で max に代入していない

## C. 窓の自己点検（置換後）

- [x] Grok / SWE-2 は shared cap + `{{UNKNOWN}}`。ORCH の振り分け順は触っていない
- [x] CU が 1 のまま（Pro: always。本人上書きで上げていない）
- [x] refill-on-empty が CU mutex=1 を破らない（+1 は shared モデル枠の GREEN trial のみ）
- [x] Effort の未観測を 0 にしていない（最適数は `{{UNKNOWN}}`）
- [x] 料金・TTL・キュー長など、Pro が書いていない列を足していない

未観測のまま残すもの（チェックしない = まだライブが無い）:

- [ ] ライブ観測で最適数が `{{UNKNOWN}}` から外れた（観測ログが正。今は無し）
- [ ] GREEN / YELLOW / RED / HARD を実測で一度でも踏んだ（今は無し）

## D. まだやらない（この骨格 PR の外）

未チェック = 実行していない（正しい）。

- [ ] （しない）憲法・CLI COMMON・スキル本体への本番パッチ
- [ ] （しない）GrokBOT desired-state の書き換え
- [ ] （しない）Computer Use 起動、並列 CU 試験
- [ ] （しない）公開・課金・解約・秘密の転記

## E. 完了の定義

窓の置換: A / B / 既知の C は付いた。  
本番完了ではない。ライブ観測が着くまで最適数は `{{UNKNOWN}}`。  
看板へ「焼き込み済み」と書かない。

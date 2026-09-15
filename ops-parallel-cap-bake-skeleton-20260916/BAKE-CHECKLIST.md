# BAKE-CHECKLIST（並列キャップ）

状態: **全部未完**。Pro `PARALLEL-CAP-PERF` 未着。  
このファイルのチェックを先に付けない。数字の想像で完了にしない。

焼き込み先は本番の憲法・CLI・Bot ではなく、まず [APPLY-WINDOW.md](APPLY-WINDOW.md) のトークン置換。本番 APPLY は別作業。

---

## A. 入力が揃うまで（今ここ）

- [ ] Pro 案件 **PARALLEL-CAP-PERF** の本文を回収した（再送中・枠 0% のまま想像しない）
- [ ] 回答の版・日付・座席を SOURCES に題名だけ足した（秘密・全文は貼らない）
- [ ] ソフト暫定 GO（~10+~10）を最終値と読み替えなかった
- [ ] 兄弟 `ops-bake-orch-cli-20260916/` の CU mutex=1 と食い違わない

## B. トークン置換（APPLY-WINDOW のみ）

残っていたら未完。0 埋めしない。無い項目は「Pro 文面に無し」と書き、数字を作らない。

- [ ] `{{PRO_NUMBER_GROK_MAX}}` ← max Cursor Grok
- [ ] `{{PRO_NUMBER_SWE2_MAX}}` ← max SWE-2
- [ ] `{{PRO_NUMBER_CU}}` ← CU。兄弟ロックは 1。上げる値なら **停止**して本人確認
- [ ] `{{PRO_NUMBER_REFILL_ON_EMPTY}}` ← refill-on-empty（個数。方針文が数字を伴うときだけ）
- [ ] 本文に裸の `{{PRO_NUMBER}}` が残っていない
- [ ] ~10 や 15 を「近いから」で代入していない

置換後もこのチェックリストの A/B が全部付くまで、C に進まない。

## C. 窓の自己点検（置換後）

- [ ] Grok 上限と SWE-2 上限が、ORCH の振り分け順（SWE-2 第一候補、Grok は難所）と矛盾しない
- [ ] CU が 1 のまま、または Pro が明示した値で本人が上書き承認した
- [ ] refill-on-empty が CU mutex=1 を破らない
- [ ] Effort の未観測を 0 にしていない
- [ ] 料金・TTL・キュー長など、Pro が書いていない列を足していない

## D. まだやらない（この骨格 PR の外）

- [ ] （しない）憲法・CLI COMMON・スキル本体への本番パッチ
- [ ] （しない）GrokBOT desired-state の書き換え
- [ ] （しない）Computer Use 起動、並列 CU 試験
- [ ] （しない）公開・課金・解約・秘密の転記

## E. 完了の定義

完了 = A と B が付き、C が矛盾なし、D をやっていない。  
完了前に「焼き込み済み」と看板へ書かない。

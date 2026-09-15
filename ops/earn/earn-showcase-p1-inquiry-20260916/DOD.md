# Definition of Done（P1のみ）

範囲外: P2週報、P3故障停止、サイト登録、提案送信、他机のPR。

| # | 条件 | 確認 |
|---|---|---|
| 1 | 対象はこのフォルダだけ | [x] `ops/earn/earn-showcase-p1-inquiry-20260916/` |
| 2 | 合成問い合わせが約20件。実PIIなし | [x] `fixtures/inquiries.csv` / `.json` |
| 3 | 入力検査がある | [x] `p1_inquiry/validate.py` |
| 4 | 重複判定がある（連絡先・類似・同一 `inquiry_id`） | [x] `p1_inquiry/duplicates.py`。同一IDは全行 `needs_human` |
| 5 | 確認待ち一覧が出る | [x] `output/needs_human.csv` と `hold_queue.csv` |
| 6 | 曖昧は `needs_human`（閉じて止める） | [x] 判定表と `--check` |
| 7 | 秘密なしで動く / Importできる | [x] Python標準ライブラリ。n8nは認証空 |
| 8 | 送信・公開・Applyなし | [x] `sent=0` `published=0` 下書きは SAMPLE |
| 9 | 日本語READMEが入力→出力を書く | [x] `README.md` |
| 10 | FACTSカード。偽KPIなし | [x] `FACTS.md` |
| 11 | 画面3枚（プレースホルダまたはワイヤ） | [x] `screens/01-03` と `output/report.html` |
| 12 | この見本のDraft PRだけ | [x] 他机・P2/P3なし |
| 13 | 別担当が再現できる | [x] `python3 run.py --check`（temp生成・output非破壊）と `python3 tests/test_p1.py` |

## 実行コマンド

```bash
cd ops/earn/earn-showcase-p1-inquiry-20260916
python3 tests/test_p1.py
python3 run.py --check
```

両方 0 終了なら、この見本のDoDは満たす。

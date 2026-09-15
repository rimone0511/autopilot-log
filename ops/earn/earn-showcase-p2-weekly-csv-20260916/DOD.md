# P2 DoD — CSV週報（根拠付き）

チケット: `EARN-SHOWCASE-P2-20260916`  
検証はコマンド結果で行う。口頭の「動いた」は合格にしない。

## Must（このPRで緑にする）

- [x] 成果物が `ops/earn/earn-showcase-p2-weekly-csv-20260916/` のみ（P1/P3フォルダを作っていない）
- [x] 合成CSVがある。実顧客名・実メール・鍵が無い
- [x] ジェネレータ `src/weekly_report.py` が追加依存なしで動く
- [x] 見本出力（Markdown と CSV）があり、要約の各行に `row_id` と CSV `#Ln` リンクがある
- [x] 除外行は確定合計に混ざらない（衝突ID・週外・0件・不正値）
- [x] `FACTS.md` が「合成 / 自主制作 / 売上主張なし」を近接表示する
- [x] README が日本語で再現手順を持つ
- [x] n8n JSON は `active: false`。送信ノードなし
- [x] 販売者の実売上・時短・精度を数字で主張していない

コマンド:

```bash
cd ops/earn/earn-showcase-p2-weekly-csv-20260916
python3 src/weekly_report.py --check
python3 tests/test_lineage.py
python3 src/weekly_report.py --trace ROW-W37-007
python3 -c "import json,pathlib; p=pathlib.Path('n8n/p2-weekly-csv-evidence.inactive.json'); d=json.loads(p.read_text()); assert d['active'] is False"
```

合格の数字（このfixture・この週）:

| 項目 | 値 |
|---|---|
| input rows | 29 |
| fulfilled | 14 |
| cancelled | 2 |
| hold | 2 |
| exception | 11 |
| 確定・合成円 (L03) | 9600 |
| lineage_errors | 0 |
| `--trace ROW-W37-007` | L01, L02, L03, L07, L10 |

## SWE-2 が別環境で印を付ける項

- [ ] 空の作業領域で README のコマンドだけを使い、同じ `out/` が再生成される
- [ ] `weekly-2026-W37.md` のリンクを1つ開き、CSVの該当行と指標が一致する
- [ ] 入力を1行壊して再実行し、その行が L03 から消えて L15 に出る
- [ ] n8n を Import しても Active にしない（任意。正本は Python）

## 合格に使わない（Should / 対象外）

動画、独自ロゴ、日英フル、P1、P3、Gumroad公開、提案送信、実n8nホスティング、CIへの本テスト追加。

## 失敗の定義

次のいずれかがあれば未達:

- 要約行の根拠 ID が入力に無い、または入力の該当行が根拠から欠けている
- 除外理由の行が L03 の合成円に含まれている
- 出力から「合成」「売上の証拠ではない」が消えている
- 秘密らしき文字列（鍵、Bearer、webhook path）が git に入っている
- n8n JSON が `active: true`、または送信コネクタがある

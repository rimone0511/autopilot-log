> **DRAFT_ONLY。公開しない。応募しない。送信しない。n8n を Active にしない。**  
> 合成データ。販売者の売上・顧客実績・時短率を主張しない。秘密を置かない。

# P2 見せもの — CSV週報（根拠が入力行へ戻る）

チケット: `EARN-SHOWCASE-P2-20260916`  
本人GO: Pro寄り（見本P2を提案より先に作る）  
対象週の見本: **2026-W37**（JST、2026-09-07 00:00 以上 〜 2026-09-14 00:00 未満）  
店舗名: **ハーバー文具（合成）** — 実在しない

問い合わせ整理（P1）と故障停止（P3）はこのフォルダに含めない。

## 何を見せるか

1種類の入力CSVから、週次の要約表を出す。**要約の各行は、使った入力の `row_id` と CSV 行リンクを必ず持つ。** 壊れた行・週の外・ID衝突は確定合計に入れず、除外明細へ出す。

売るものは n8n という名前ではなく、「数字の隣に根拠がある週報」である。n8n JSON は inactive の見本で、再現の正本は Python である。

## 含まないもの

- 実売上、実顧客名、実シートID、鍵、webhook、本番メール
- 自動送信、Slack/Gmail コネクタ、公開、応募
- 時短○%、精度○%、n8n Partner などのバッジ
- P1（問い合わせ整理）と P3（二重登録・故障カタログ）

## フォルダ

| パス | 役割 |
|---|---|
| [fixtures/inbound-ops-synthetic-w37.csv](fixtures/inbound-ops-synthetic-w37.csv) | 合成29行（確定・キャンセル・確認待ち・除外） |
| [fixtures/columns.md](fixtures/columns.md) | 列定義 |
| [src/weekly_report.py](src/weekly_report.py) | 正本ジェネレータ |
| [n8n/p2-weekly-csv-evidence.inactive.json](n8n/p2-weekly-csv-evidence.inactive.json) | 取り込み用。`active: false` |
| [n8n/code-weekly-evidence.js](n8n/code-weekly-evidence.js) | 上記 JSON の Code ノード正本 |
| [out/weekly-2026-W37.md](out/weekly-2026-W37.md) | 見本週報（Markdown） |
| [out/weekly-2026-W37-summary.csv](out/weekly-2026-W37-summary.csv) | 要約CSV |
| [out/weekly-2026-W37-evidence.csv](out/weekly-2026-W37-evidence.csv) | 要約行×入力行の対応 |
| [out/weekly-2026-W37-exceptions.csv](out/weekly-2026-W37-exceptions.csv) | 除外行 |
| [out/weekly-2026-W37-RUN.json](out/weekly-2026-W37-RUN.json) | 実行記録（入力ハッシュ） |
| [FACTS.md](FACTS.md) | 言ってよい事実だけ |
| [DOD.md](DOD.md) | 完了条件（コマンドで検証） |
| [DRAFT_ONLY.md](DRAFT_ONLY.md) | 公開・送信ゲート |

## 実行手順（別担当の再現はここだけ見れば足りる）

Python 3.9+。追加パッケージなし。リポジトリルートから:

```bash
python3 ops/earn/earn-showcase-p2-weekly-csv-20260916/src/weekly_report.py \
  --input ops/earn/earn-showcase-p2-weekly-csv-20260916/fixtures/inbound-ops-synthetic-w37.csv \
  --out-dir ops/earn/earn-showcase-p2-weekly-csv-20260916/out \
  --week 2026-W37 \
  --generated-at 2026-09-16T12:00:00+09:00 \
  --check
```

パックディレクトリから:

```bash
cd ops/earn/earn-showcase-p2-weekly-csv-20260916
python3 src/weekly_report.py --check
python3 tests/test_lineage.py
python3 src/weekly_report.py --trace ROW-W37-007
```

期待する標準出力の要点:

- `counts fulfilled=14 cancelled=2 hold=2 exception=11 input=29`
- `lineage_errors=0`
- `--trace ROW-W37-007` が `L01` `L03` `L07` `L10` を含む

`git diff -- ops/earn/earn-showcase-p2-weekly-csv-20260916/out` が空なら、コミット済み見本と再生成が一致している。

### n8n（任意・動かさなくてよい）

1. n8n で Import from File → `n8n/p2-weekly-csv-evidence.inactive.json`
2. Active のままにしない（JSON は `active: false`）
3. 私有コピーでのみ `{{P2_FIXTURE_PATH}}` をローカルCSVへ置換する
4. 最後のノードは NoOp。「送信」ノードを足さない
5. 見本の数字合わせは Python 側で行う（n8n は形状の見本）

公式の import 手順: https://docs.n8n.io/build/manage-workflows/export-and-import/

## 根拠の読み方

Markdown の根拠列は GitHub の行リンクである。例:

`[ROW-W37-007](../fixtures/inbound-ops-synthetic-w37.csv#L8)`

- `ROW-W37-007` が入力の安定ID
- `#L8` が同じファイルの8行目

`out/weekly-2026-W37-evidence.csv` は「要約行ID × 入力行」の正規化表。どちらか片方でも欠ければ DoD 失敗。

見本の確定・合成金額 **9,600円** は架空店舗の計算結果である。販売者の売上ではない。

## 入力の内訳（合成29行）

| 分類 | 行数 | 確定合計へ |
|---|---:|---|
| fulfilled（週内・妥当） | 14 | 入れる |
| cancelled | 2 | 入れない（L11/L12） |
| hold | 2 | 入れない（L13/L14） |
| exception（0件、週外、欠落、負数、不明値、ID衝突） | 11 | 入れない（L15） |

ID `ROW-W37-DUP` は2行ある。衝突した ID は **両方除外** する。

## ゲート

[DRAFT_ONLY.md](DRAFT_ONLY.md) の値はすべて false。この PR から公開・応募・送信・n8n 有効化をしない。

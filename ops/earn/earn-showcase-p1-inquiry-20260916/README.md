# 問い合わせ受付見本 P1（合成）

チケット: `EARN-SHOWCASE-P1-20260916`  
対象フォルダだけが範囲です。P2/P3・サイト登録・他机のPRは含みません。

人が止める前提の、**問い合わせ受付 → 入力検査 → 重複判定 → 確認待ち一覧** です。  
n8n は実装候補の輸出ファイルです。検証済みの実行手段は下の Python/CLI です。

**合成データ / 自主制作。実顧客・実PII・実績KPIはありません。送信しません。公開しません。**

## 入力 → 出力

```
fixtures/inquiries.csv  （または inquiries.json）
        │
        ▼
 python3 run.py
        │
        ├─ output/needs_human.csv        閉じて止める一覧
        ├─ output/ready_for_review.csv   形は通ったが、人が見るまで返信しない
        ├─ output/hold_queue.csv         上の2つをまとめた確認待ち
        ├─ output/records.json           全件の判定
        ├─ output/reply_drafts.SAMPLE.json  下書き見本（送らない）
        ├─ output/summary.json           このfixtureの件数だけ
        └─ output/report.html            画面3枚ぶんのワイヤ
```

入力1種類（問い合わせ行）→ 出力1種類（確認待ちキュー）。  
自動返信・自動公開・サイト登録・課金・通知はありません。

## 動かし方（秘密情報なし）

Python 3.9+。追加パッケージは不要です。

```bash
cd ops/earn/earn-showcase-p1-inquiry-20260916
python3 run.py
python3 run.py --check
python3 tests/test_p1.py
```

JSON入力も同じ結果になります。

```bash
python3 run.py --input fixtures/inquiries.json --out output
```

`--check` は `fixtures/expected/queues.json` とキューが一致するか見ます。  
ネットワーク、APIキー、ログインは使いません。

## 判定（曖昧なら人へ倒す）

| 状態 | キュー | 意味 |
|---|---|---|
| 必須が欠ける / 形式が壊れている | `needs_human` | 通さない |
| 未来日付・未知チャネル・リスク語 | `needs_human` | 通さない |
| 同じメール / 同じ電話 / 本文がほぼ同一 | `needs_human` | 重複として止める |
| 氏名+会社は同じだが連絡先が違う | `needs_human` | 同一人物か判断しない |
| 本文が似ているが連絡先が違う | `needs_human` | 類似として止める |
| 上記以外で一意 | `ready_for_review` | 整理済み。**それでも送信しない** |

基準時刻は `2026-09-16T12:00:00+00:00`（見本の固定時計）。  
20件の内訳は `fixtures/expected/decision_table.md`。

返信下書きは `ready_for_review` にだけテンプレートを付けます。  
ファイル名も本文も **SAMPLE / 合成下書き** です。送信フラグは常に `not_sent`。

## n8n（任意）

`n8n/inquiry_intake_p1.json` を Import できます。認証情報は空です。  
Manual Trigger → 合成20件を読む → 同じ理由コードで分ける、という流れです。  
バージョン差で Code ノードが動かないときは Python を正とします。

## 画面見本

- `screens/01_input.txt`
- `screens/02_validation.txt`
- `screens/03_hold_list.txt`

実行後の `output/report.html` が同じ3画面のHTML版です。

## 事実

`FACTS.md` を先に読んでください。時短率・売上・顧客数は書いていません。  
完成条件は `DOD.md`。

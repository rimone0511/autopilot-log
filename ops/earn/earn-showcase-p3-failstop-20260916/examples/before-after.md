# Before / after — 合成台帳

自主制作の見本。実在の登録ではない。

## Before

シード: [before-ledger.json](before-ledger.json)

| record_id | 表示名 | メール | 由来 |
|---|---|---|---|
| cust-1001 | 依頼者A | client-a@example.invalid | seed-001 |
| cust-1002 | 依頼者B | client-b@example.invalid | seed-002 |

2 行。ここに無い顧客はまだ台帳にいない。

## 何が起きたか（12 イベント）

入力は [../fixtures/events.jsonl](../fixtures/events.jsonl)。

1. 依頼者C を書く → 成功（evt-01）
2. 依頼者A の二重登録を止める
3. メール欠落を止める
4. 依頼者B の ID 衝突を止める
5. 依頼者C の再送を止める
6. 依頼者D を人待ちにする
7. D が timeout → **書かない**
8. 依頼者E を人待ちにする
9. E を人が approve → 書く
10. 依頼者F を人待ちにする
11. F を人が reject → 書かない
12. 空の名前を止める

## After

ランナー出力: [after-ledger.json](after-ledger.json) / [after-needs-human.json](after-needs-human.json)

### 台帳（4 行）

| record_id | 表示名 | 書いたイベント | 備考 |
|---|---|---|---|
| cust-1001 | 依頼者A | seed-001 | 変化なし |
| cust-1002 | 依頼者B | seed-002 | 変化なし |
| cust-1003 | 依頼者C | evt-01 | 新規 |
| cust-1005 | 依頼者E | evt-09 | 人の approve のあと |

### 書いていない（意図どおり）

| record_id | 表示名 | 理由 |
|---|---|---|
| cust-1004 | 依頼者D | `timeout_not_approve` |
| cust-1006 | 依頼者F | `rejected` |
| cust-1090 | 依頼者X | `invalid_payload`（メール欠落） |
| cust-1091 | （空） | `invalid_payload`（名前欠落） |

### needs_human（7 件）

| event_id | reason |
|---|---|
| evt-02 | `duplicate_registration` |
| evt-03 | `invalid_payload` |
| evt-04 | `id_collision` |
| evt-05 | `duplicate_registration` |
| evt-07 | `timeout_not_approve` |
| evt-11 | `rejected` |
| evt-12 | `invalid_payload` |

**読み方:** After の行数は「成功した登録数」ではない。止まって人に渡した行が、成功件数の横に並んでいる。

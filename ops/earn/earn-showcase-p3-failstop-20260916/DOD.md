# Definition of Done — P3 失敗停止 / 二重登録ガード

チケット: `EARN-SHOWCASE-P3-20260916`  
検品の正本: `python3 runner/failstop.py`（n8n は分岐見本）

Must だけ。動画・ロゴ・公開 repo・P1/P2 は合否に使わない。

## Must

- [x] 成果物が `ops/earn/earn-showcase-p3-failstop-20260916/` だけにあり、P1/P2 を含まない
- [x] 合成 fixture（台帳シード + イベントログ）がある
- [x] ランナーがある（依存パッケージなし）
- [x] n8n JSON がある。`active: false`。認証ノードなし。Webhook なし（Manual Trigger）
- [x] before / after 例がある
- [x] FACTS card がある。実績・時短・売上を書いていない
- [x] README が日本語で、含むもの / 含まないもの / 手順を書く
- [x] 二重登録の書き込みが止まり、`needs_human` になる
- [x] 不正（必須欠落）の書き込みが止まり、`needs_human` になる
- [x] ID 衝突の書き込みが止まり、`needs_human` になる
- [x] `decision=timeout` は台帳に書かない（timeout ≠ approve）
- [x] `decision` 欠落 / 不明も承認にしない
- [x] `event_id` 欠落 / 重複、`occurred_at` 欠落 / タイムゾーンなしは書かない
- [x] actor 無しの `approve` は書かない（認証ではない。合成ログ上の欄）
- [x] 秘密（鍵、実メール、webhook 実体、シート ID）が成果物に無い
- [x] 別担当が README だけで import 不要のローカル再現ができる

## 再現コマンド（別担当）

作業ディレクトリは **このフォルダ**:

```bash
cd ops/earn/earn-showcase-p3-failstop-20260916
python3 runner/failstop.py \
  --ledger fixtures/ledger-seed.json \
  --events fixtures/events.jsonl \
  --out-dir /tmp/p3-failstop-out
python3 tests/test_failstop.py
```

期待する summary（同梱サンプル。性能主張ではない）:

| 項目 | 値 |
|---|---|
| 台帳 after | `cust-1001`, `cust-1002`, `cust-1003`, `cust-1005` |
| 書いたイベント | `evt-01`, `evt-09` |
| 依頼者D (`cust-1004`) | **無い**（timeout） |
| `needs_human` | 7 件（二重 2 / 不正 2 / 衝突 1 / timeout 1 / reject 1） |

## 独立検品（SWE-2）

- [ ] 空の作業領域で上の 2 コマンドが exit 0
- [ ] `/tmp/p3-failstop-out/after-needs-human.json` に `timeout_not_approve` があり、`after-ledger.json` に `cust-1004` が無い
- [ ] actor 無し approve、event_id / 時刻欠落、重複 event_id が全て非書き込み（`tests/test_failstop.py` の probe）
- [ ] n8n JSON を開いて `active` が false、Credential 欄が空、Webhook ノードが無い
- [ ] FACTS に無い数字を README が言っていない
- [ ] このパックから送信・公開・Activate していない

## この DoD で見ないもの

動画、カバー画像、P1/P2、Gumroad ZIP、公開、応募、実 n8n ホスト、SLA。

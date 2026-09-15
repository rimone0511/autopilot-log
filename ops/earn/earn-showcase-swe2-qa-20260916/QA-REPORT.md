# EARN showcase SWE-2 QA

- チケット: `EARN-SHOWCASE-SWE2-QA-20260916`
- 役割: 独立 empty-env QA（SOL review § SWE-2 へ渡す最小追加 QA）
- 日付: 2026-09-15 UTC（見本時計 2026-09-16）
- Runtime: Python 3.12.3 / Linux 6.12.94+
- Lock: QA only。**publish / apply / send / register / merge / n8n Activate は実施していない**
- この PR の成果物: 本報告のみ。P1/P2/P3 のコードは触っていない

判定の意味:

- `PASS`: README/DOD の正常系と SOL 追加 probe を、公開 CLI の許容入力で破らなかった
- `FAIL`: 中心主張（受付キー、根拠の出典、監査 envelope）を公開 runner で破れた
- 期待される非ゼロ（`--check` 拒否、未知 timezone、欠落 input）は FAIL に数えない

## 固定した head

SOL が CONDITIONAL/FAIL とした head ではなく、**修正後 head** を detached worktree で検品した。

| Pack | PR | branch | QA head | SOL が見た head | 対象 |
|---|---:|---|---|---|---|
| P1 | #115 | `cursor/earn-showcase-p1-inquiry-04e1` | `541bb18a964931ff38e3d5ab44bbd28eb6919b4d` | `07bedd55218efbdfd88ea1b81a2096e88cca5187` | `ops/earn/earn-showcase-p1-inquiry-20260916/` |
| P2 | #117 + #120 | `cursor/earn-showcase-p2-weekly-csv-be1d`（#120 マージ後。`cursor/earn-p2-provenance-timezone-134b` と同一 SHA） | `14b818c7a0e51ba3fabfe76a9cdc326e743333d5` | `1dd4a0208afee58dca0d053fcdffa95f625a70de` | `ops/earn/earn-showcase-p2-weekly-csv-20260916/` |
| P3 | #116 | `cursor/earn-showcase-p3-failstop-ee4f` | `0a822e017a8e7d642e4fe21ccd96d56b3249880e` | `324bece6496bd26310fb3bbe90d5a8cc90b16fa5` | `ops/earn/earn-showcase-p3-failstop-20260916/` |

作業領域: `/tmp/earn-qa/p1` `/tmp/earn-qa/p2` `/tmp/earn-qa/p3`（各 pack 専用 worktree）。追加パッケージなし。ネットワークなし。

## 総括

| Pack | 判定 | 記載コマンド | SOL 追加 probe | 提案準備（FACTS 限定） |
|---|---|---|---|---|
| P1 | **PASS** | 全て exit 0 | 重複 `inquiry_id` 全行 hold / CSV=JSON / `--check` 後 git clean | **開始可** |
| P2 | **PASS** | 全て exit 0 | 一時カスタム入力の source/link/hash 一致 / `--timezone UTC` が実計算 | **開始可** |
| P3 | **PASS** | 全て exit 0 | actorless approve / event ID・時刻欠落 / 重複 event ID が非書き込み | **開始可** |
| 共通 | **PASS** | — | n8n `active=false`、送信ノードなし、認証オブジェクトなし、fixture は合成 | — |

**提案準備は FACTS の範囲に限り開始してよい。** 実績・売上・時短・精度・認証済み本番運用・「n8n 導入済み」は不可。publish / apply / send / register / merge / Activate は別 GO まで不可。

---

## P1 — inquiry intake（#115 / `541bb18`）

**PASS**

SOL の Must gap（同一 `inquiry_id` を両方 ready にする / `--check` が tracked output を汚す）は、この head では再現しなかった。

### 記載コマンド（README / DOD）

作業ディレクトリ: `ops/earn/earn-showcase-p1-inquiry-20260916`

| # | コマンド | exit | 要点 |
|---|---|---:|---|
| 1 | `python3 run.py` | 0 | `input_count=20` `ready_for_review=6` `needs_human=14` `sent=0` `published=0` `secrets_used=0` `synthetic=true` `generated_at_utc=2026-09-16T12:00:00+00:00` |
| 2 | `python3 run.py --check` | 0 | `CHECK OK: committed outputs match temp regeneration; queues match fixtures/expected/queues.json` |
| 3 | `python3 tests/test_p1.py` | 0 | `Ran 22 tests in 0.027s` / `OK` |
| 4 | `python3 run.py --input fixtures/inquiries.json --out /tmp/earn-qa/p1-json-out` | 0 | JSON 入力も同じ件数 |

`git status --porcelain`（worktree ルート）:

| 時点 | 出力 |
|---|---|
| 実行前 | 空 |
| `run.py` 後 | 空（`generated_at_utc` は見本時計。tracked `output/` は書き換え後も一致） |
| `--check` 後 | 空（`--check` は temp 比較。committed `output/` 非破壊） |

ready IDs: `INQ-S0-001, 002, 004, 016, 017, 019`  
hold IDs: `INQ-S0-003, 005, 006, 007, 008, 009, 010, 011, 012, 013, 014, 015, 018, 020`

### SOL 追加 probe

**1. 同一 `inquiry_id` の全行が hold（CSV と JSON）**

公開 CLI に、同じ `inquiry_id=DUP-ID`・別メール・別本文の妥当な 2 行を渡した。

```bash
python3 run.py --input /tmp/earn-qa/probes/p1-dup/dup.csv --out /tmp/earn-qa/probes/p1-dup/out-csv
# exit 0
python3 run.py --input /tmp/earn-qa/probes/p1-dup/dup.json --out /tmp/earn-qa/probes/p1-dup/out-json
# exit 0
```

| 経路 | ready | needs_human | reason_text |
|---|---:|---|---|
| CSV | 0 | `DUP-ID`, `DUP-ID` | 両行 `DUPLICATE_INQUIRY_ID` |
| JSON | 0 | `DUP-ID`, `DUP-ID` | 両行 `DUPLICATE_INQUIRY_ID` |

SOL 当時の actual（両方 `ready_for_review` / `VALID_UNIQUE`）は破れていない。  
任意入力の summary は `dataset=external-input-not-asserted` `synthetic=false` `secrets_used=null`。事実化していない。

**2. CSV / JSON 一致（同梱 fixture）**

```bash
python3 run.py --input fixtures/inquiries.csv --out /tmp/earn-qa/probes/p1-csv-fixture   # exit 0
python3 run.py --input fixtures/inquiries.json --out /tmp/earn-qa/probes/p1-json-fixture # exit 0
```

ready IDs・hold IDs・全行 `reasons` が一致。

**3. 再生成後 git clean（`--check`）**

`--check` は temp へ再生成して committed `output/` 全体を比較する。worktree は dirty にならない。  
同梱外入力は拒否される（期待される非ゼロ）:

```bash
python3 run.py --check --input /tmp/earn-qa/probes/p1-dup/dup.csv
# exit 1
# stderr: CHECK FAILED: --check accepts only bundled showcase fixtures
```

### 残メモ（FAIL ではない）

- 秘密スキャンは禁止パターンの不在であり、秘密ゼロの完全証明ではない
- 提案では bundled fixture 限定と書く。任意 `--input` の件数を KPI にしない

---

## P2 — traceable weekly CSV（#117/#120 / `14b818c`）

**PASS**

SOL の中心ブロッカー（`--input` が別ファイルでも既定 fixture を根拠表示 / `--timezone` を無視して JST 固定）は、この head では再現しなかった。

### 記載コマンド（README / DOD）

作業ディレクトリ: `ops/earn/earn-showcase-p2-weekly-csv-20260916`

| # | コマンド | exit | 要点 |
|---|---|---:|---|
| 1 | `python3 src/weekly_report.py --check` | 0 | `counts fulfilled=14 cancelled=2 hold=2 exception=11 input=29` `lineage_errors=0` |
| 2 | `python3 tests/test_lineage.py` | 0 | `Ran 16 tests in 0.019s` / `OK` |
| 3 | `python3 src/weekly_report.py --trace ROW-W37-007` | 0 | `L01` `L02` `L03` `L07` `L10` |
| 4 | `python3 -c "import json,pathlib; p=pathlib.Path('n8n/p2-weekly-csv-evidence.inactive.json'); d=json.loads(p.read_text()); assert d['active'] is False"` | 0 | `active=false` |

`git status --porcelain` は実行前後とも空。  
`git diff -- ops/earn/earn-showcase-p2-weekly-csv-20260916/out` も空。

Markdown の L03 先頭リンク `../fixtures/inbound-ops-synthetic-w37.csv#L2` を開くと CSV 2 行目は  
`ROW-W37-001,2026-09-07T09:12:00+09:00,store,NB-A5,2,480,fulfilled,合成・店頭`。指標と一致。

### SOL 追加 probe

**1. temporary custom input の source / link / hash 一致**

```bash
cp fixtures/inbound-ops-synthetic-w37.csv /tmp/earn-qa/probes/p2-custom/customer-input.csv
python3 src/weekly_report.py \
  --input /tmp/earn-qa/probes/p2-custom/customer-input.csv \
  --out-dir /tmp/earn-qa/probes/p2-custom/out \
  --week 2026-W37 \
  --generated-at 2026-09-16T12:00:00+09:00
# exit 0
```

| 面 | 観測 |
|---|---|
| 実ファイル SHA-256 | `8c9638a9bebb8e8d96c26e08968e303fa0ba78658750cd887aa5c31d614ba96b`（fixture と同バイト） |
| RUN.json `input` | `customer-input.csv`（既定名なし） |
| RUN.json `input_sha256` | 上と同じ |
| Markdown | `入力: customer-input.csv` / 同じ hash / `../customer-input.csv#L2` |
| evidence / summary / exceptions | `customer-input.csv#L…`。既定 fixture 名なし |
| 親ディレクトリ漏えい | `/tmp/earn-qa/probes/p2-custom` は出力に出ない |

SOL 当時の actual（Markdown/RUN/evidence が `fixtures/inbound-ops-synthetic-w37.csv` のまま）は破れていない。

SWE-2 DOD「1行壊す」も原 fixture を汚さず一時コピーで実施:

```bash
python3 src/weekly_report.py \
  --input /tmp/earn-qa/probes/p2-broken/broken-copy.csv \
  --out-dir /tmp/earn-qa/probes/p2-broken/out \
  --week 2026-W37 \
  --generated-at 2026-09-16T12:00:00+09:00
# exit 0
# counts fulfilled=13 cancelled=2 hold=2 exception=12 input=29
```

- `ROW-W37-001` は L03 から消え、L15 に出る（`negative_qty`、合成円 8640）
- 出典は `broken-copy.csv` / `../broken-copy.csv#L2`。hash は fixture と異なる
- 原 fixture は未変更

**2. timezone option の実計算**

```bash
python3 src/weekly_report.py \
  --input fixtures/inbound-ops-synthetic-w37.csv \
  --out-dir /tmp/earn-qa/probes/p2-utc/out-fixture \
  --week 2026-W37 \
  --timezone UTC \
  --generated-at 2026-09-16T12:00:00+09:00
# exit 0
```

| | JST（committed） | `--timezone UTC` |
|---|---|---|
| 記録 timezone | `Asia/Tokyo` | `UTC` |
| week_start | `2026-09-07T00:00:00+09:00` | `2026-09-07T00:00:00+00:00` |
| week_end_exclusive | `2026-09-14T00:00:00+09:00` | `2026-09-14T00:00:00+00:00` |
| Markdown | `（ISO、Asia/Tokyo）` | `（ISO、UTC）` |

同梱 29 行の件数は UTC でも 14/2/2/11 のまま（境界に乗らない）。**件数一致だけでは timezone 無視を否定できない**ので、境界 CSV で実分類を見た。

```text
ROW-TZ-JST-ONLY  occurred_at=2026-09-07T00:30:00+09:00
ROW-TZ-BOTH      occurred_at=2026-09-08T12:00:00+09:00
```

```bash
python3 src/weekly_report.py --input .../tz-boundary.csv --out-dir .../out-jst --timezone Asia/Tokyo ...
# exit 0 / fulfilled=2 exception=0 / week_start=+09:00 / input=tz-boundary.csv
python3 src/weekly_report.py --input .../tz-boundary.csv --out-dir .../out-utc --timezone UTC ...
# exit 0 / fulfilled=1 exception=1 / week_start=+00:00 / input=tz-boundary.csv
```

`ROW-TZ-JST-ONLY` は JST で fulfilled、UTC で `out_of_week`。既定 fixture 名は出ない。

期待される fail-closed:

```bash
python3 src/weekly_report.py --input fixtures/inbound-ops-synthetic-w37.csv --timezone Not/AZone ...
# exit 2 / stderr: unknown timezone: Not/AZone
python3 src/weekly_report.py --input /tmp/earn-qa/probes/p2-custom/no-such.csv ...
# exit 2 / stderr: input not found: .../no-such.csv
```

存在しない `--input` は既定 fixture に落ちない。

### 残メモ（FAIL ではない）

- `--input` が任意ファイルでも RUN.json の `synthetic=true` は定数。提案では bundled fixture（またはそれが合成だと分かる入力）に限定する
- n8n Code stub の `SOURCE_REL` は形状見本。根拠の正本は Python
- n8n の Read Binary File は inactive。私有コピーでパスを差し替える設計。Activate / 実ファイル接続はしない

---

## P3 — fail-stop（#116 / `0a822e0`）

**PASS**

SOL の中心ブロッカー（actor 無し approve、event ID/時刻無し write が `written=true`）は、この head では再現しなかった。

### 記載コマンド（README / DOD）

作業ディレクトリ: `ops/earn/earn-showcase-p3-failstop-20260916`

| # | コマンド | exit | 要点 |
|---|---|---:|---|
| 1 | `python3 runner/failstop.py --ledger fixtures/ledger-seed.json --events fixtures/events.jsonl --out-dir /tmp/p3-failstop-out` | 0 | 下表 |
| 2 | `python3 tests/test_failstop.py` | 0 | `Ran 25 tests in 0.009s` / `OK` |

| 項目 | 値 |
|---|---|
| 台帳 after | `cust-1001`, `cust-1002`, `cust-1003`, `cust-1005`（4） |
| written events | `evt-01`, `evt-09` |
| needs_human | 7（二重 2 / 不正 2 / 衝突 1 / timeout 1 / reject 1） |
| `timeout_not_approve` | あり（`evt-07`） |
| `cust-1004` | **無い** |
| `timeout_is_approve` | false |

`git status --porcelain` は実行前後とも空（出力は `/tmp`）。

### SOL 追加 probe（公開 CLI + 一時 JSONL）

いずれも seed ledger + 合成 probe 行。`written=true` になってはいけない。

**1. actorless approve**

```bash
python3 runner/failstop.py \
  --ledger fixtures/ledger-seed.json \
  --events /tmp/earn-qa/probes/p3-actorless.jsonl \
  --out-dir /tmp/earn-qa/probes/p3-actorless-out
# exit 0
```

- hold（`cust-3101`）のあと `decision=approve` で `actor` 無し
- `written_event_ids=[]` `ledger_count_after=2`（seed のみ）
- `probe-approve` → `needs_human` / `missing_actor` / `written=false`
- `cust-3101` は台帳に無い

**2. missing event ID / time**

```bash
python3 runner/failstop.py --ledger ... --events /tmp/earn-qa/probes/p3-missing-id.jsonl --out-dir ...
# exit 0 / written=[] / reason=missing_event_id / event_id=null / cust-3201 無し

python3 runner/failstop.py --ledger ... --events /tmp/earn-qa/probes/p3-missing-time.jsonl --out-dir ...
# exit 0 / written=[] / reason=missing_occurred_at / event_id=probe-notime / cust-3202 無し

python3 runner/failstop.py --ledger ... --events /tmp/earn-qa/probes/p3-missing-both.jsonl --out-dir ...
# exit 0 / written=[] / reason=missing_event_id / event_id=null / cust-3209 無し
```

**3. duplicate event ID**

```bash
python3 runner/failstop.py --ledger ... --events /tmp/earn-qa/probes/p3-dup-eid.jsonl --out-dir ...
# exit 0
```

- 同一 `event_id=dup-id`、別 record / 別 idempotency key
- 1 件目 `cust-3301` は書く（初出）
- 2 件目 `cust-3302` は `needs_human` / `duplicate_event_id` / `written=false`
- 台帳の `source_event_id=dup-id` は 1 行だけ

SOL の「再利用できる」は破れていない。初出の write は監査可能な 1 件として残る。

### 残メモ（FAIL ではない）

- actor 欄の必須は本人認証ではない。提案では「合成ログ上で actor を要求する」までに限定する
- `synthetic=true` は任意 ledger/events でも定数。bundled fixture 外で使わない
- n8n は Manual Trigger。Webhook 無し。Activate しない

---

## 共通 — n8n / 合成 / 秘密らしき値

JSON を読んだだけ。Import / Activate / 送信はしていない。

| Pack | `active` | ノード type | credentials オブジェクト | 送信 / webhook |
|---|---|---|---|---|
| P1 | `false` | stickyNote, manualTrigger, code×2 | ノードに無し。`meta.description` に "No credentials" の文言のみ。`meta.templateCredsSetupCompleted=true` はテンプレ印 | httpRequest / send 無し |
| P2 | `false` | stickyNote, manualTrigger, readBinaryFile, spreadsheetFile, code, **noOp** | ノードに無し。"No credentials" は注記 | gmail / slack / webhook / telegram 無し |
| P3 | `false` | stickyNote, manualTrigger, code, switch, noOp×4 | ファイルに `credentials` キー無し | webhook / emailSend / gmail / slack 無し。注記に "Do NOT add a Webhook" |

禁止パターン（`sk-` / `xoxb-` / `AIza` / `BEGIN PRIVATE` / `aws_secret` / `ghp_` 等）は各 pack の成果物にヒットしなかった。  
`@gmail.com` / Slack hook URL は fixture に無い（P3 テストが「含めないこと」を断言しているだけ）。  
P1 fixture は `example.com` / 架空番号。P3 は `@example.invalid`。これは秘密不存在の完全証明ではない。

---

## 提案ゲート

| 問 | 答 |
|---|---|
| 現状の修正後 head で、FACTS 限定の提案準備を始めてよいか | **よい**（3 パックとも PASS） |
| 実績・売上・時短・精度・認証済み本番・n8n 稼働を書いてよいか | **不可** |
| publish / apply / send / register / merge / n8n Activate | **不可**（別 GO） |
| 提案に使ってよい範囲 | 合成 fixture、人手確認前提、自動送信なし、根拠付き週報（合成円）、合成ログ上の guard simulation |

SOL の「追加 QA が緑なら FACTS 限定で提案準備可」を満たす。

---

## 人間コーディネータ向け 10 行 verdict

1. 総合判定は GO（FACTS 限定）。修正後 3 head は正常系と SOL 追加 probe が緑。
2. P1 #115 `541bb18` は同一 `inquiry_id` の全行を `needs_human`（`DUPLICATE_INQUIRY_ID`）。CSV/JSON 一致。
3. P1 の `--check` は temp 比較で committed `output/` を汚さず、再生成後 git clean。
4. P2 #117/#120 `14b818c` は一時 `customer-input.csv` の source / `#Ln` / SHA-256 が実ファイルと一致する。
5. P2 の `--timezone UTC` は `week_start=+00:00` を記録し、境界行の分類が JST と異なる。
6. P3 #116 `0a822e0` は actorless approve・event ID/時刻欠落・event ID 再利用が全て非書き込み。
7. P3 同梱 12 件は timeout ≠ approve。`cust-1004` は台帳に無い。25 テスト OK。
8. 三者とも n8n は `active=false`、送信ノードなし、認証オブジェクトなし。fixture は合成。
9. 提案準備は FACTS 範囲に限り開始可。実績・売上・時短・精度・認証済み本番運用は不可。
10. publish / apply / send / register / merge / n8n Activate は別 GO まで不可。

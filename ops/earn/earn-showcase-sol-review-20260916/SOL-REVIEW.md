# EARN showcase SOL review

- 相談ID: `EARN-SHOWCASE-SOL-REVIEW-20260916 / v1`
- Review: Cursor SOL
- Reviewed work: Cursor Grok
- Review date: 2026-09-15 UTC
- Runtime: Python 3.12.3 / Linux
- Lock: review only。publish / apply / send / register / merge は実施していない

## 対象と固定点

| Pack | PR | reviewed head | 対象 |
|---|---:|---|---|
| P1 | #115 | `07bedd55218efbdfd88ea1b81a2096e88cca5187` | `ops/earn/earn-showcase-p1-inquiry-20260916/` |
| P2 | #117 | `1dd4a0208afee58dca0d053fcdffa95f625a70de` | `ops/earn/earn-showcase-p2-weekly-csv-20260916/` |
| P3 | #116 | `324bece6496bd26310fb3bbe90d5a8cc90b16fa5` | `ops/earn/earn-showcase-p3-failstop-20260916/` |

README / DOD / FACTS / runner / tests と n8n stub を読んだ。判定は次の意味で使う。

- `PASS`: 記載 Must と主張範囲にブロッカーを確認しなかった。
- `CONDITIONAL`: 同梱 fixture の正常系は再現するが、提案前に直すべき Must gap がある。
- `FAIL`: 中心となる安全性・根拠性の主張を、公開 runner の許容入力で破れる。

## 総括

| Pack | 判定 | 記載コマンド | 中心ブロッカー | 現状のまま SWE-2 QA 後に提案開始 |
|---|---|---|---|---|
| P1 | **CONDITIONAL** | 全て exit 0 | 同一 `inquiry_id` 2件を両方 `ready_for_review` にする | **NO** |
| P2 | **FAIL** | 全て exit 0 | `--input` が別ファイルでも既定 fixture を根拠として表示する | **NO** |
| P3 | **FAIL** | 全て exit 0 | actor・event ID・時刻が無くても書き込める | **NO** |

「現状のまま」は、各 DOD に書かれた正常系コマンドだけを SWE-2 が再実行する場合を指す。下記の最小修正と追加ケースを含む SWE-2 QA が緑になれば、FACTS の範囲に限定した提案準備は開始可。実績、売上、時短、精度、認証済み本番運用の主張は不可。

## P1 — inquiry intake

### 判定

**CONDITIONAL**

同梱20件について、入力検査、重複・曖昧判定、`needs_human`、送信なしの出力は再現した。一方、受付の安定キーである `inquiry_id` の重複を検査しないため、「曖昧なら人へ倒す」「重複判定がある」を一般化して提案に使うには不足する。

### 実行結果

PR head の worktree で README / DOD の順に実行した。

```text
python3 run.py                         exit 0
python3 run.py --check                 exit 0 / CHECK OK
python3 tests/test_p1.py               exit 0 / 13 tests OK
result                                 input=20, ready=6, needs_human=14
git status after regeneration          output/summary.json modified
```

変更は `generated_at_utc` の実行時刻だけだった。キュー結果は CSV / JSON 間で一致する。

追加の fail-closed probe:

```text
input: 同じ inquiry_id="DUP-ID"、別メール・別本文の妥当な2件
actual:
  DUP-ID -> ready_for_review / VALID_UNIQUE
  DUP-ID -> ready_for_review / VALID_UNIQUE
```

n8n JSON は `active: false`、Manual Trigger + Code nodes のみで、`credentials` フィールドと送信ノードは無かった。

### Must gaps

1. `inquiry_id` の空値は止めるが、バッチ内重複を止めない。同じキーの2レコードを人手確認へ倒さず、出力・下書きにも同一受付番号が重複する。
2. DOD #13 の「再現」はキュー比較に限られる。`--check` 自体が tracked output を書き換え、`generated_at_utc` が非決定なので、コミット済み成果物の完全再生成は clean にならない。

### Honesty / secrets risk

- bundled fixture と reviewed tree に、使用中の鍵・token・credential に見える値は確認しなかった。パターンスキャンの一致はテスト内の禁止文字列だけだった。ただしこれは秘密不存在の完全な証明ではない。
- `synthetic=true`、`secrets_used=0`、`sent=0` は入力内容の検査結果ではなく定数である。`--input` に任意ファイルを渡せるため、実データを渡すと「合成」「秘密0」の表示が不正確になり得る。提案では bundled fixture 限定と明記する必要がある。
- HTML は入力文字列を escape しており、同梱 fixture で HTML 注入は確認しなかった。

### Reproducibility

- bundled fixture の判定件数・理由コード・キューは高速かつネットワークなしで再現した。
- 出力全体は byte-for-byte 再現ではない。テストも committed output 全体の一致を検査しない。
- n8n と Python の同値性は自動比較されておらず、Python が正本という限定は README と整合する。

### Minimal fix list

1. 入力全体で `inquiry_id` を数え、重複IDに属する全行を `needs_human`（例: `DUPLICATE_INQUIRY_ID`）にする。
2. CSV / JSON 双方に重複IDテストを追加する。
3. showcase の `generated_at` を CLI で固定可能にし、`--check` は一時ディレクトリへ生成して committed output 全体を比較する。あるいは実行時刻を tracked output から外す。
4. 任意入力を残すなら、`synthetic` / `secrets_used` を無条件で事実化しない。最小案は showcase fixture 以外を `--check` で拒否する。

### Proposal gate

現行 SWE-2 項目だけの合格後は **開始不可**。上記 1–3 と重複ID probe、clean regeneration を SWE-2 が確認した後は、合成fixture・人手確認前提・自動送信なしという FACTS 範囲に限り **開始可**。

## P2 — traceable weekly CSV

### 判定

**FAIL**

同梱 fixture の週報は決定的に再生成され、根拠表も閉じている。しかし公開 CLI の `--input` は任意ファイルを受ける一方、Markdown、CSV evidence、RUN.json の入力名とリンクを既定 fixture に固定する。別入力の結果が既定 fixture に由来したように表示されるため、中心価値の「数字の隣に正しい根拠がある」を破る。

### 実行結果

```text
python3 src/weekly_report.py --check              exit 0
counts                                             fulfilled=14, cancelled=2,
                                                   hold=2, exception=11, input=29
lineage_errors                                     0
python3 tests/test_lineage.py                      exit 0 / 12 tests OK
python3 src/weekly_report.py --trace ROW-W37-007   exit 0
trace                                              L01,L02,L03,L07,L10
n8n active assertion                              pass
git status after regeneration                     clean
```

別入力 probe:

```text
actual input          /tmp/.../customer-input.csv
Markdown input        fixtures/inbound-ops-synthetic-w37.csv
RUN.json input        fixtures/inbound-ops-synthetic-w37.csv
evidence links        ../fixtures/inbound-ops-synthetic-w37.csv#Ln
```

timezone probe:

```text
requested             UTC
reported              Asia/Tokyo
week_start            2026-09-07T00:00:00+09:00
```

n8n JSON は `active: false`、credential なし、最後は NoOp で、送信 connector は無かった。

### Must gaps

1. `SOURCE_REL` が定数のため、`--input` が別ファイルでも出力が既定 fixture を根拠として記録する。SHA-256 は実入力だが、人が開く根拠リンクと RUN metadata が一致しない。
2. `--timezone` を公開しているが、値に関係なく JST で集計し `Asia/Tokyo` と記録する。CLI が受理した条件と実計算条件が一致しない。
3. 現行 lineage test は既定 fixture だけを使うため、1 と 2 を検出しない。

### Honesty / secrets risk

- reviewed tree の鍵・token・credential に見える実値は確認しなかった。パターンスキャンの一致は scanner 自身の regex だけだった。
- 金額は Markdown / FACTS / RUN の近くで合成と明記され、9,600円を販売者売上にしていない。この点は適切。
- 別入力時の誤った出典表示は、秘密漏えいよりも provenance の虚偽リスクである。逆に実パスをそのまま出す修正は私有パス漏えいを起こし得るため、安全な相対参照か入力制限が必要。
- n8n の Read Binary File stub は inactive だが、私有コピーでパスを差し替える設計である。PR内で Active 化・実ファイル接続をしてはいけない。

### Reproducibility

- bundled fixture は生成後も git clean で、committed output 5ファイルをテストが byte-for-byte 比較する。3パック中で最も強い。
- 行数、合成円、衝突ID両側除外、L01–L15 の根拠閉包は再現した。
- 再現性は既定 fixture / JST に限る。公開 options 全体には成立しない。

### Minimal fix list

1. 最小の安全案は `--input` を bundled fixture に制限する。任意入力を残すなら、実入力から漏えいのない source label と evidence target を生成し、Markdown / summary / evidence / RUN の全てで同じ出典を使う。
2. `--timezone` を正しく `ZoneInfo` へ渡して出力にも記録するか、option を削除して JST 固定を明示する。
3. temporary custom input と UTC 指定の regression tests を追加し、表示 source、SHA-256、集計境界の一致を検査する。
4. SWE-2 の「1行壊す」は原 fixture を汚さず一時コピーで行い、そのコピーを根拠として表示することまで確認する。

### Proposal gate

現行 SWE-2 項目だけの合格後は **開始不可**。出典固定問題と timezone option を修正または削除し、別入力 regression を含む SWE-2 QA が緑になった後は、合成週報・根拠付き・本番実績なしという FACTS 範囲に限り **開始可**。

## P3 — fail-stop

### 判定

**FAIL**

同梱12イベントでは二重・不正・衝突・timeout・reject を止める。しかし runner は `approve` の actor を要求せず、write event の `event_id` と `occurred_at` も要求しない。監査キーと時刻が欠落した書き込みを成功扱いできるため、「人が approve」「確認できる台帳」「壊れる側に倒す」を runner の一般的挙動としては主張できない。

### 実行結果

```text
python3 runner/failstop.py ... --out-dir /tmp/p3-failstop-out   exit 0
ledger after                                                     4
written events                                                   evt-01, evt-09
needs_human                                                      7
timeout_not_approve                                              present
cust-1004                                                        absent
python3 tests/test_failstop.py                                   exit 0 / 21 tests OK
git status                                                       clean
```

追加の fail-closed probes:

```text
actor 無し human_decision + approve       written=true
event_id 無し・occurred_at 無し write      written=true, source_event_id=null
```

n8n JSON は `active: false`、credential なし、外向き送信 node なし。ただし unauthenticated webhook trigger の stub を含む。

### Must gaps

1. `decision=approve` だけで書き込み、`actor` の存在すら検査しない。「人が approve」は同梱 fixture の説明にしかならず、runner の制御では保証されない。
2. write event の `event_id`、`occurred_at` を必須検査しない。欠落したイベントが `written` となり、監査行の `source_event_id` / `written_at` が欠落または代替値になる。
3. event ID の一意性を管理しない。同じ event ID を異なる idempotency key / record ID で再利用できる。
4. Python と n8n stub の双方に同じ欠落があり、現行21テストは検出しない。

### Honesty / secrets risk

- reviewed tree の鍵・token・credential、実メール、実 Slack hook は確認しなかった。fixture のメールは `example.invalid`。
- `synthetic=true` は任意の ledger / events に対して定数である。実入力に差し替えると出力表示が不正確になるため、bundled fixture 外で使わない。
- n8n webhook は inactive かつ placeholder path だが認証が無い。誤って Activate すると未認証 ingress になる設計なので、showcase のまま提案先環境へ import / Activate させない。
- actor 文字列を必須化しても本人認証にはならない。「認証済み承認」とは主張せず、「合成ログ上で actor 欄を要求する」までに限定すべき。

### Reproducibility

- bundled fixture の件数・reason sequence・台帳IDは再現した。ネットワークと追加依存は不要。
- committed examples test は after ledger の ID 列と needs_human の reason 列を比較するが、全 after files の byte-for-byte 一致までは検査しない。
- `/tmp` 出力を使う標準手順は tracked tree を汚さず、同梱ケースの再実行には適切。

### Minimal fix list

1. 全イベントで非空・一意な `event_id` と妥当な timezone 付き `occurred_at` を必須化し、欠落・再利用・形式不正を `needs_human` にする。
2. `approve` では非空 actor を必須化する。認証機構が無いことは README / FACTS に明記したままにする。
3. actorless approve、missing envelope、duplicate event ID の unit tests を追加する。
4. n8n mirror に同じ検査を入れる。より安全な最小案は webhook を Manual Trigger に替え、外部 ingress の形状見本は文書だけにする。

### Proposal gate

現行 SWE-2 項目だけの合格後は **開始不可**。event envelope と actor の fail-closed 修正、3つの追加 probe、inactive / no-credential 確認を SWE-2 が通した後は、「合成ログ上の guard simulation」であることを明記する場合に限り **開始可**。本番承認、認証、SLA、完全な重複防止は主張不可。

## SWE-2 へ渡す最小追加 QA

| Pack | 追加で必須の確認 |
|---|---|
| P1 | 同一 `inquiry_id` の全行が hold、CSV/JSON一致、再生成後 git clean |
| P2 | temporary custom input の source/link/hash 一致、timezone 指定の実計算一致 |
| P3 | actorless approve、missing event ID/time、duplicate event ID が全て非書き込み |
| 共通 | n8n `active=false`、credential / send node なし、fixture が合成のみ |

## 人間コーディネータ向け10行 verdict
1. 総合判定は HOLD、現状の3パックから提案は開始しない。
2. P1は正常系13テスト成功だが、重複 inquiry_id を通すため CONDITIONAL。
3. P1は固定時刻または一時生成比較を入れ、再生成後 git clean を必須にする。
4. P2は正常系12テスト成功かつ既定fixtureは決定的だが、別入力の根拠を誤表示するため FAIL。
5. P2は input provenance と timezone option を修正または削除する。
6. P3は正常系21テスト成功だが、actorless approve と監査情報欠落の書き込みを許すため FAIL。
7. P3は event ID・時刻・actor を fail-closed で検査し、event ID 再利用も止める。
8. 三者とも reviewed tree に実秘密や送信nodeは見つからず、n8n は inactive だった。
9. 修正後の SWE-2 は正常系だけでなく、本報告の追加 probe を必ず実行する。
10. 追加 QA が緑なら FACTS 限定で提案準備可、publish・apply・send・register は別GOまで不可。

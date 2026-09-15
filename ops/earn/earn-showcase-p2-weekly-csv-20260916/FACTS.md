> **Operator fact table. 提案文や画面にこのファイルごと貼らない。**  
> No secrets. No live rates. No real buyer names.

# Pack facts — P2 CSV週報（根拠付き）

ここに無い数字・実績は作らない。見本の 9,600円 は下の「合成店舗」の計算結果だけである。

## Seller（公開してよい）

| key | value in this repo |
|---|---|
| display_name | `{{DISPLAY_NAME}}` — 推奨 Yuta Ishida / 石田祐太 |
| location | Japan（US/EU を装わない） |
| timezone | `{{TIMEZONE}}` 例: `JST` |
| languages | Japanese and English (async) |
| public_site | https://yutalab.dev/ |
| public_github | https://github.com/rimone0511 |
| public_tool | https://github.com/rimone0511/autopilot-log |

ログインメール、電話、本名の別表記、私有パスは書かない。

## この見本が証明すること

| 言ってよい | 言ってはいけない |
|---|---|
| 1つのCSVから週報を出し、要約行から入力行（row_id と `#Ln`）へ戻れる。`--input` の表示出典と hash はそのファイル | 顧客の本番データで動かした。別入力なのに既定 fixture 由来と表示する |
| 壊れた行・週外・ID衝突を確定合計に混ぜない | 精度○%、二重登録を「防ぐ」 |
| 合成の確定件数 14 / 合成円 9,600（2026-W37、このfixture） | 販売者や顧客の売上・GMV |
| Python 3.9+ と標準ライブラリで再現できる。`--timezone` は週境界に使われ、記録と一致する | n8n Partner / Expert |
| n8n JSON は inactive の形状見本 | このPRで n8n 実機を常時稼働させた |
| 自主制作のサンプルである | 納品済み・時短○時間 |

## 合成店舗（フィクション）

| key | value |
|---|---|
| label | ハーバー文具（合成） |
| week | 2026-W37 |
| SKU | NB-A5 / PEN-BK / CLIP-20 |
| channels | store / web / phone / wholesale |
| 確定・合成円 | 9600（L03。根拠行のみ） |

実在の店舗・注文・依頼者に置き換えない。git に実名を足さない。

## 関連（本文はコピーしない）

P1 問い合わせ整理、P3 故障停止、Gumroad SKU、提案文パックは別チケット。このフォルダは P2 だけ。

## Explicit non-facts

- 販売者の年商、顧客数、成約率、時短、精度
- 「本番 Sheets に接続済み」
- 「タイムアウトしたら確定」
- Autopilot Log が TikTok を無人投稿する（既定は受信箱アップロード）
- このPRが公開・応募・送信した

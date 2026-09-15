# ACTIVITY-GATE — Wave D late (D11–D20) (2026-09-16)

対象: オペレーター指定の **Wave D D11–D20**。  
観測: **2026-09-16 JST**（公開 GET / 公式ヘルプのみ）。ログインしていない。登録していない。有料プランを開いていない。

このフォルダは **活動ゲートの記録** だけ。貼り付けパックでも、アカウント作成でもない。

Wave D は QUEUE どおり **合格するまで登録しない**。この観測の **keep（pass）は 0**。全部 SKIP または閉じた机。**下書きのみ。公開しない。** 今回は登録していない。

## PR#1 QUEUE との関係

親キュー `earn-register-expand-20260916/QUEUE.md`（[PR#1](https://github.com/rimone0511/autopilot-log/pull/1)）の Wave D 表は **D1–D8 だけ**。

- **D-late 行は QUEUE に無い。** 作らない。
- Wave C の LATE（Zapier / Make / n8n / Toptal = C-L1–C-L4）は **Wave C のまま**。ここでは再ゲートしない。
- D1–D8 は兄弟フォルダ `earn-activity-gate-waveD-20260916/`（PR#13）側。ここでは繰り返さない。

D11–D20 はオペレーター指定の残り Fit-Med。QUEUE に無かった机なので、合格しても Wave A には上げない（今回は合格 0）。

## 机（このフォルダの範囲）

1. D11 Comet
2. D12 Replit Bounties
3. D13 Superpeer
4. D14 We Work Remotely
5. D15 Remote OK
6. D16 Himalayas
7. D17 ココナラテック
8. D18 Findy Freelance
9. D19 PRONI アイミツ
10. D20 比較ビズ（公式は `biz.ne.jp`。`hikaku-biz.com` は別の会計ブログ）

## ラベル

| ラベル | 意味 |
|---|---|
| `pass` | 公開ページに生きている机と、新しさの手がかりがある。Wave C 末尾 Med として下書き登録の検討可。**この観測では 0** |
| `fail-closed` | 公式が閉鎖・移転・スタンドアロン終了、または売り手用の自前机が閉じている |
| `fail-aggregator` | 自前の仕事机が無く、求人ボード／他社案件の束ねだけ |
| `fail-thin` | 公開の個人スキル販売カタログではない（企業向け一括見積・有料掲載など）。本線と噛み合わない |
| `skip-agent` | 机は生きているが、登録面談／専属エージェント紹介が前提。MAIN Google の下書きキューでは代行しない |
| `needs_check` | 公開面が読めない／日付が無い。推測で pass にも thin にもしない。**この観測では 0**（読めないページは他証拠で判定できた） |

件数・GMV・「稼げる額」は **作らない**。画面に出ている見出しと日付だけ書く。マーケ数字は活動証明に使わない。

## keep vs skip（要約）

詳細は [SUMMARY.md](SUMMARY.md)。

- **keep:** なし
- **skip:** D11–D20 すべて（閉じた机 3 / 寄せ集め 3 / 面接エージェント 2 / 企業見積比較 2）

## この観測でやらなかったこと

- ブラウザ登録、MAIN Google ログイン、OAuth 完走
- KYC・口座・Stripe/PayPal 接続・マイナンバー
- 有料会員・優先掲載・審査スキップの購入
- 応募・出品公開・CV 送信・パートナー掲載申込
- 秘密（メール実値、トークン、署名付きURLの鍵）の保存

## ファイル

- [SUMMARY.md](SUMMARY.md) — **keep vs skip**
- [QUEUE.md](QUEUE.md) — QUEUE-ready（全部 skip。昇格なし）
- [ACTIVITY-GATE.md](ACTIVITY-GATE.md) — 10机の一覧と短文
- [records/](records/) — チェックリスト 1机1枚
- [SKIP.md](SKIP.md) — 切った机
- [METHOD.md](METHOD.md) — 公開 GET の方法と HTTP 要約。秘密なし

次の手（人がやる）: この10机は登録しない。Wave A/B の `next` / `week-2` と、別フォルダの Wave D `pass` だけを下書き対象にする。

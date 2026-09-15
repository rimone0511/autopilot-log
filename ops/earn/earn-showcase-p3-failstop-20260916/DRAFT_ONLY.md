# DRAFT_ONLY — このパックから外に出さない

チケット: `EARN-SHOWCASE-P3-20260916`  
パック: `ops/earn/earn-showcase-p3-failstop-20260916/`  
状態: **下書き。公開しない。応募しない。送信しない。**

このフォルダは見せもの P3（失敗停止 / 二重登録ガード）の自主制作見本です。
エージェントも運用者も、このパックだけを根拠に次を行いません。

| 行為 | このパックからの許可 |
|---|---|
| マーケット出品の公開 | `false` |
| 提案・応募・メール送信 | `false` |
| n8n ワークフローの Activate | `false` |
| 本番台帳 / CRM / Sheets への書き込み | `false` |
| 認証情報の接続 | `false` |
| 登録追加 | `false` |
| この PR の Ready / merge | `false`（本人レビューまで draft） |

タイムアウトを承認として扱わない。欠落した判定も承認ではない。

後から公開・応募する場合は、**このフォルダの外**で本人 GO を取る。
GO が出るまで、下の箱はすべて `false` のまま。

- [ ] `publish`
- [ ] `send`
- [ ] `activate_n8n`
- [ ] `attach_live_credential`
- [ ] `merge`

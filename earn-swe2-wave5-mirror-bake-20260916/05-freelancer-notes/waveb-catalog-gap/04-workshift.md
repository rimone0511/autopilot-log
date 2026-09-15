# Catalog-gap — Workshift（ワークシフト）

日付（観測）: 2026-09-15 UTC  
机: Workshift  
QUEUE: **載っていない**（Wave B カタログ欠け）。**Workship ではない**  
このフォルダの判定: **needs_check**  
ログインしたか: no  
登録したか: no

## 名前の衝突（先に読む）

| 机 | 公式（QUEUE / パック） | この NOTES |
|---|---|---|
| **Workship**（ワークシップ） | QUEUE B2 https://goworkship.com/ （JP パックあり。activity-gate `pass`） | 対象外。開いたのは区別用のみ |
| **Workshift**（ワークシフト） | QUEUE に無い | 対象。海外フリーランスマッチングのコピー |

CU が Workship のパックを Workshift に貼らないこと。

## 開いた公開 URL（候補）

| 何 | URL | この環境 |
|---|---|---|
| サービスサイト | https://workshift-sol.com/ | HTTP 200。title「クラウドソーシングで海外進出支援「ワークシフト」Workshift」 |
| 会社サイト | https://workshift-sol.co.jp/ | HTTP 200。ワークシフト・ソリューションズ株式会社 |
| 案件検索 | https://workshift-sol.com/jobs/search | HTTP 200。**HTML に案件の日付文字列は無い**（シェル／JS）。新しさは未読 |
| メール登録開始（検索で出たパス） | https://workshift-sol.com/registration/mail_start | ブラウザ UA の GET は 200。別 UA では CloudFront **403**。登録面の中身は未読 |
| フリーランス検索 | https://workshift-sol.com/users/search | HTTP 200。title「フリーランスを検索する」 |

手数料ページの公式 URL は **未確認。捏造しない。**

会社ページのマーケ人数・「Likes」は活動証明に使わない。

## 公開コピーから分かること（中の案件は見ていない）

- 自前のクラウドソーシング机、という会社説明（寄せ集め専用とは、この GET だけでは決めない）
- 依頼は日本企業、働き手は海外在住が多い、というコピーあり。**日本在住の売り手本線と噛むかは未確認**
- フルタイム来日の「Workshift Navi」と、オンラインの Workshift を混同しない（英語説明ページが区別している。CU は来日求人に逃げない）

## 手数料

**書かない。** 円・% の数字を HTML から拾って料金表にしない。ライブのヘルプ／フッターを人が開く。

## CU の前に確認すること

- [ ] 今開いているのが Workshift であって Workship でない
- [ ] フリーランス登録（仕事を受けたい）であり、クライアント登録ではない
- [ ] Google があるか。メール開始 URL が WAF で潰れていないか（UA / IP で 403 になりうる）
- [ ] 公開 `jobs/search` をブラウザで描画し、**案件カードの日付**が1件以上読めるか。読めなければ `needs_check` のまま
- [ ] 日本語のリモート案件があるか。海外オフショア発注者だけ／現地労働だけなら本線外を人が書く
- [ ] KYC・パスポートアップロードが登録直後に出ないか
- [ ] 有料会員・入札課金・ウォレット最低残高が必須か。必須なら止める。額は invent しない
- [ ] 利用規約に自動応募・スクレイプ禁止があれば、CU は検索だけして応募しない
- [ ] QUEUE に足すなら ACTIVITY-GATE 合格が先。カタログ欠けのまま直列に挿さない

次: 人が案件カードの日付と人材側入口を見てから。この PR では登録しない。

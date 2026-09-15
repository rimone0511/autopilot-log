# Wave B catalog-gap live-check NOTES

観測: **2026-09-15 UTC** 公開 GET のみ。ログインなし。登録なし。フォーム送信なし。有料なし。  
判定（このフォルダ）: 4机とも **`needs_check`**。合格にしない。手数料額を書かない。QUEUE に無い机を QUEUE へ足さない。

「catalog-gap」= 売り手／人材の **貼るパックが無い**、または QUEUE に載っていない机。CU はここの確認リストを人が埋めるまで **登録しない**。

兄弟の JP Wave B activity-gate は活動の目視用。あちらで Skill Shift が `pass` でも、**カタログ欠け（パック・手数料・Google・KYC・人材側入口）は未確認のまま**なので、ここは `needs_check` のままにする。

## Summary

| # | 机 | QUEUE? | このフォルダの Gate | 公開 GET で開いた候補（捏造ではない。CU は再オープン） | 手数料 |
|---|---|---|---|---|---|
| 1 | AI CrowdWorks | Wave B15 | **needs_check** | `https://ai.crowdworks.jp/` ；ニュース `https://crowdworks.co.jp/news/akdv13x1sf/` ；登録面候補 `https://crowdworks.jp/aicw/register/new_email`（JS 無しだと本文が出ない） | **書かない**。ライブ画面を読む |
| 2 | Skill Shift | Wave B16 | **needs_check** | QUEUE の `https://skillshift.jp/` は **DNS 失敗**。開いた公式 `https://www.skill-shift.com/` ；公開 `GET /api/jobs` | **書かない** |
| 3 | DMM 生成AI人材バンク | **QUEUE に無い** | **needs_check** | 人材フォーム候補 `https://algoage.co.jp/jinzaibanktouroku` ；運営案内 `https://dmm-businessai.com/about-us/` | **書かない**（FAQ の支援費用は依頼者向けに読める。人材手数料と混ぜない） |
| 4 | Workshift | **QUEUE に無い** | **needs_check** | サービス `https://workshift-sol.com/` ；会社 `https://workshift-sol.co.jp/` ；案件検索 `https://workshift-sol.com/jobs/search`（HTML に日付無し） | **書かない** |

**Workshift ≠ Workship.** Workship は QUEUE B2 `https://goworkship.com/`（別机。パックあり）。混ぜない。

`fail` / `SKIP thin` / `blocked_paid_plan`: この NOTES では **付けない**（見えないものを薄いにしない。手数料も見ていない）。

## CU の前に共通で見ること

各机のファイルのチェックリストを、**人が公式画面で**埋める。エージェントは登録しない。

1. 売り手／人材側か。依頼者・企業コンソールなら閉じる。
2. Google が公式ボタンであるか。無ければ MAIN Google のメール経路か。新しい SNS アカウントを作らない。
3. KYC（免許・マイナンバー・顔写真・keycode・住民票・口座）が出たらアップロードせず停止。
4. 有料会員・優先掲載・審査スキップ・ウォレット入金が必須なら `blocked_paid_plan` にして止める。**額を推測して書かない。**
5. 公開案件または自前の仕事机の **日付表示** が1画面あるか。マーケの「○万人」は使わない。
6. 本線（公式API自動化／手順書／リモートのスキル販売）と机が噛むか。現地だけ・寄せ集めだけなら SKIP 候補を人が書く。
7. パック本文がまだ無い。この NOTES はパックの代わりではない。

## ファイル

- [01-ai-crowdworks.md](01-ai-crowdworks.md)
- [02-skill-shift.md](02-skill-shift.md)
- [03-dmm-seiseiai-jinzaibank.md](03-dmm-seiseiai-jinzaibank.md)
- [04-workshift.md](04-workshift.md)

## この観測でやらなかったこと

- ブラウザ登録、MAIN Google ログイン、OAuth 完走
- フォーム送信（DMM 人材バンクの会員登録を含む）
- KYC・口座・Stripe
- 手数料表の転記（ライブが正）
- 応募・出品公開
- 秘密の保存

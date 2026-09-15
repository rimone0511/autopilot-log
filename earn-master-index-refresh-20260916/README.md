# earn-ops MASTER INDEX refresh — 2026-09-16

案件: PR#1–#32 のフォルダ地図（register / handoff / activity / proposal / ops）  
版: 2026-09-16 GO refresh（索引日。観測は 2026-09-15〜16）  
枝: `earn-master-index-refresh-20260916/`

**下書きのみ。秘密なし。登録しない。公開しない。パック本文は複製しない。**

本フォルダは **地図の更新** だけ。貼る文・ゲート証拠・ランブック本文は兄弟PRにある。

## このフォルダ

| ファイル | 中身 |
|---|---|
| [INDEX.md](INDEX.md) | 全パック表（pack / path / desk(s) / CU vs prep / status / PR#） |

## いまの CU ポインタ（この refresh の正）

**live box 進捗（発明しない）。** [PR#24 REGISTER-BOARD](https://github.com/rimone0511/autopilot-log/pull/24) の「CW next」行は、この観測で上書きする。QUEUE の `next` ラベルより新しい。

| 机 | CU hint | 意味 |
|---|---|---|
| Fiverr（CU-02） | `blocked_skip` **hold** | このパスでは開かない。ギグ/FAQパックは unpublished のまま |
| ランサーズ Lancers（CU-03） | `blocked_skip` **captcha** | このパスでは開かない。handoff パックは置いたまま |
| クラウドワークス CrowdWorks（CU-04） | `blocked_skip` **403** | live box で signup/homepage が **403 Forbidden**。再試行しない。signup しない |
| **Upwork（CU-05）** | **next CU**（in progress） | #16 handoff。Catalog は Submit しない。0 Connects。KYC で止める |
| LinkedIn Services（CU-06） | after Upwork | #16 の次。Service Page draft。Jobs/feed は対象外 |

Wave B/C/D の CU 登録は、Wave A の `pending` が `draft` か parked `blocked_skip` になるまで開かない。

## 兄弟の索引と役割分担

| 索引 | 役割 | 出典 |
|---|---|---|
| **この MASTER INDEX refresh** | フォルダ単位。register / handoff / activity / proposal / ops と **PR#1–#32** | [PR#35](https://github.com/rimone0511/autopilot-log/pull/35) |
| [PR#14 MASTER INDEX](https://github.com/rimone0511/autopilot-log/pull/14) | 同じ地図の初版（#1–#13 を読んだ時点。この refresh が後継） | `earn-register-pack-master-index-20260916/` |
| [PR#24 REGISTER-BOARD](https://github.com/rimone0511/autopilot-log/pull/24) | 机単位の CU hint（#1–#22 のフォルダ名まで。本文は複製しない） | `earn-register-progress-board-20260916/` |
| [PR#8 CU serial INDEX](https://github.com/rimone0511/autopilot-log/pull/8) | 机単位の貼る順 CU-01–CU-28 と期待ファイル | `earn-register-pack-index-20260916/INDEX.md` |
| [PR#3 JP-WEEK2-INDEX](https://github.com/rimone0511/autopilot-log/pull/3) | JP Week2 の局所直列（CU-11–CU-18） | `earn-register-packs-jp-20260916/JP-WEEK2-INDEX.md` |
| [PR#1 QUEUE](https://github.com/rimone0511/autopilot-log/pull/1) | 波（A/B/C/D）と登録作業の状態ラベル | `earn-register-expand-20260916/QUEUE.md` |

衝突したら: **いま開く机** はこの refresh の CU ポインタ（Fiverr/Lancers/CW skip → **Upwork** in progress → LinkedIn Services）。PR#24 の CW-next は古い。波と `done-draft` は QUEUE。CU番号は PR#8。フォルダがどのPRにあるかは **この表**。

## やらないこと

- パック本文のコピー
- アカウント作成、KYCアップロード、出品公開
- 秘密・実メール・実電話・身分証のコミット
- 案件数・GMV・「稼げる額」の創作
- Fiverr hold / Lancers captcha / CrowdWorks 403 の再試行

# earn-ops MASTER INDEX refresh — 2026-09-16

観測日: 2026-09-15〜16（公開ページ。ブラウザ登録はしていない）  
索引日: 2026-09-16  
スナップショット: **2026-09-15 UTC** 時点の `rimone0511/autopilot-log` 開いているPR **#1–#32**  
状態: **DRAFT-ONLY**（このPRは地図だけ。パック本文はコピーしない）  
禁止: 秘密の記入、ブラウザ登録、公開、KYC完了、有料プラン加入

これは earn-ops の **フォルダ単位マスター索引の更新**。  
register / handoff / activity-gate / proposal / listing / ops を1枚で辿る。

初版は [PR#14](https://github.com/rimone0511/autopilot-log/pull/14)（#1–#13）。机単位の貼る順（CU-01–CU-28）は複製しない。それは [PR#8](https://github.com/rimone0511/autopilot-log/pull/8)。机単位の CU hint は [PR#24](https://github.com/rimone0511/autopilot-log/pull/24)（#1–#22 まで）。

認証: MAIN Google のみ。KYC が出たら朝の本人へ。エージェントは進めない。

---

## いまの CU ポインタ

QUEUE の Fiverr `next` より、REGISTER-BOARD の skip が新しい。**次に開く CU は CrowdWorks。**

| 机 | CU serial | CU hint | パック（本文は開かない。パスだけ） | 次の動作 |
|---|---|---|---|---|
| Fiverr | CU-02 | `blocked_skip` **hold** | #6 #15（listing）。`earn-packs/fiverr/` は未作成 | パーク。再試行しない。signup しない。Gig/FAQ は unpublished |
| ランサーズ Lancers | CU-03 | `blocked_skip` **captcha** | #17 handoff | パーク。captcha を回さない。signup しない |
| **クラウドワークス CrowdWorks** | **CU-04** | **next CU**（`pending`） | #17 handoff。#32 は field map（prep。playbook ではない） | **このパスの最初の `pending`。** seller 下書きのみ。応募しない。KYC で止める |

直列（ランブック #7。本文は複製しない）: Fiverr → Lancers → **CrowdWorks** → Upwork → LinkedIn Services → TimeTicket → Contra → Craudia → Freelancer.com → Wave B **gate `pass` only**。  
Fiverr と Lancers は parked skip。Wave B/C/D の CU 登録は Wave A `pending` が終わるまで開かない。

---

## 列の読み方

| 列 | 意味 |
|---|---|
| Pack | フォルダの役割名。本文の題名ではない |
| Path | マージ後のリポジトリ相対。未マージなら出典PRの枝にある |
| Desk(s) | そのパックが扱う机。QUEUE の波番号は参考 |
| CU vs prep | **CU** = computer-use 直列で開く／貼るもの。**prep** = ゲート・索引・朝の本人・HANDS提案・ops・スキャン。prep を CU ブラウザで登録してはいけない |
| Status | パックファイルの有無とPR状態。**登録済みではない** |
| PR# | 2026-09-15 UTC 時点で確認した GitHub PR。無ければ `—` |

### Status 記号

| 記号 | 意味 |
|---|---|
| `ready · open` | 兄弟PRにファイルがある。PRは下書き解除済み |
| `ready · draft` | 兄弟PRにファイルがある。PRは draft |
| `unknown · no PR` | 机または置き場は QUEUE / ランブックにあるが、パックファイルがどの枝にも無い |
| `blocked_skip` | CU はこの机をこのパスで開かない（パックが `ready` でも） |
| `next CU` | このパスで次に開く机（CrowdWorks） |

`ready` は「登録済み」ではない。QUEUE の `done-draft` / `next` / `week-2` / `gate` / `late` は登録作業のラベルで、別物。

パス列のリンクは **出典PRの枝**（未マージ）を指す。`master` にはまだ無い。

---

## MASTER 表（フォルダ）— PR#1–#32

上から「先に読む順」。CU直列の机順ではない。種別は register / handoff / activity / proposal / ops（listing は CU 貼り付けなので register の隣に置く）。

| Pack | Path | Desk(s) | CU vs prep | Status | PR# |
|---|---|---|---|---|---|
| Register QUEUE (expand) | [`earn-register-expand-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-register-expand-20260916-b673/earn-register-expand-20260916) | Wave A–D の全机（順の正本）。Coconala / Gumroad は QUEUE 上 `done-draft` | CU | ready · open | [#1](https://github.com/rimone0511/autopilot-log/pull/1) |
| Week-2 GLOBAL register packs | [`earn-register-packs-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-register-packs-week2-a398/earn-register-packs-20260916) | Guru.com, PeoplePerHour (Hourlies/Offers), Malt.com, Workana | CU | ready · open | [#2](https://github.com/rimone0511/autopilot-log/pull/2) |
| Week-2 GLOBAL activity-gate (nested) | [`earn-register-packs-20260916/ACTIVITY-GATE-week2-global.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-register-packs-week2-a398/earn-register-packs-20260916/ACTIVITY-GATE-week2-global.md) | 同上4机 | prep | ready · open · Guru `pass` / Malt `pass`（下書き） / PPH `blocked_paid_plan` / Workana jobs `needs_check` | [#2](https://github.com/rimone0511/autopilot-log/pull/2) |
| JP Week2 register packs | [`earn-register-packs-jp-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/jp-earn-register-packs-8df7/earn-register-packs-jp-20260916) | Workship, 複業クラウド, SOKUDAN, CrowdLinks, Anycrew, MENTA, ストアカ, Shufti（CU-11–CU-18。在庫01–08ではない） | CU | ready · draft | [#3](https://github.com/rimone0511/autopilot-log/pull/3) |
| KYC morning handoff | [`earn-kyc-morning-checklist-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-kyc-morning-checklist-9baf/earn-kyc-morning-checklist-20260916) | Wave A（LinkedIn Services / Gumroad は対象外）。Wave B は画面が出たときだけ | prep | ready · draft | [#4](https://github.com/rimone0511/autopilot-log/pull/4) |
| EN HANDS proposal + invite (Wave 1) | [`earn-en-proposal-drafts-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-en-proposal-drafts-b102/earn-en-proposal-drafts-20260916) | Upwork, Fiverr, Contra | prep | ready · draft · DO NOT SEND | [#5](https://github.com/rimone0511/autopilot-log/pull/5) |
| Fiverr n8n Gig listing paste | [`earn-fiverr-gig-draft-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-fiverr-gig-draft-91ed/earn-fiverr-gig-draft-20260916) | Fiverr（CU-02。ギグは Draft のまま） | CU | ready · draft · unpublished · CU `blocked_skip` hold | [#6](https://github.com/rimone0511/autopilot-log/pull/6) |
| CU serial runbook | [`earn-cu-runbook-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-cu-serial-runbook-2e17/earn-cu-runbook-20260916) | Wave A 残り（Fiverr→…→Freelancer.com）→ Wave B の gate `pass` のみ | CU | ready · draft · いまの skip は BOARD が上 | [#7](https://github.com/rimone0511/autopilot-log/pull/7) |
| CU serial register-pack INDEX | [`earn-register-pack-index-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-register-pack-index-45e2/earn-register-pack-index-20260916) | CU-01–CU-28（机単位の期待パス） | prep | ready · draft | [#8](https://github.com/rimone0511/autopilot-log/pull/8) |
| ops-bake ORCH / CLI / GrokBOT Head | [`ops-bake-orch-cli-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/ops-bake-orch-cli-20260916-ad2e/ops-bake-orch-cli-20260916) | マーケット机ではない（運用焼き込み。本番未適用） | prep | ready · draft · 本番未適用 | [#9](https://github.com/rimone0511/autopilot-log/pull/9) |
| Upwork Project Catalog listing paste | [`earn-upwork-catalog-draft-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-upwork-catalog-draft-0e79/earn-upwork-catalog-draft-20260916) | Upwork（CU-05。Catalog は Submit しない） | CU | ready · draft · unpublished | [#10](https://github.com/rimone0511/autopilot-log/pull/10) |
| JP HANDS proposal + estimate (Wave 1) | [`earn-jp-proposal-drafts-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/jp-proposal-drafts-c1d1/earn-jp-proposal-drafts-20260916) | CrowdWorks, Lancers, Coconala | prep | ready · draft · DO NOT SEND | [#11](https://github.com/rimone0511/autopilot-log/pull/11) |
| JP Wave B activity-gate | [`earn-activity-gate-waveB-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-activity-gate-waveb-jp-fced/earn-activity-gate-waveB-20260916) | SOKUDAN, Workship, 複業クラウド, CrowdLinks, Anycrew, MENTA, ストアカ, Skill Shift, AI CrowdWorks, ITプロパートナーズ, YOUTRUST, Offers, Shufti | prep | ready · draft · pass 5 / needs_check 8 / SKIP thin 0 | [#12](https://github.com/rimone0511/autopilot-log/pull/12) |
| Wave D Fit-Med activity-gate | [`earn-activity-gate-waveD-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-activity-gate-waved-b552/earn-activity-gate-waveD-20260916) | SKIMA, Payhip, Ko-fi, Dribbble Services, Fastwork, Truelancer, Twine, ワークシフト, ママワークス, 99designs, シュフティ, Wellfound | prep | ready · draft · pass 9 / needs_check 1 / SKIP 2 | [#13](https://github.com/rimone0511/autopilot-log/pull/13) |
| MASTER INDEX (first cut) | [`earn-register-pack-master-index-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-register-pack-master-index-9290/earn-register-pack-master-index-20260916) | #1–#13 の地図。この refresh が後継 | prep | ready · draft · superseded by this folder for #15–#32 | [#14](https://github.com/rimone0511/autopilot-log/pull/14) |
| Fiverr Requirements + FAQ polish | [`earn-fiverr-requirements-faq-polish-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-fiverr-req-faq-polish-7daf/earn-fiverr-requirements-faq-polish-20260916) | Fiverr（unpublished n8n Gig の Requirements/FAQ） | CU | ready · draft · unpublished · CU `blocked_skip` hold | [#15](https://github.com/rimone0511/autopilot-log/pull/15) |
| CU handoff Upwork + LinkedIn Services | [`earn-upwork-linkedin-cu-handoff-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-upwork-linkedin-cu-handoff-a525/earn-upwork-linkedin-cu-handoff-20260916) | Upwork (CU-05), LinkedIn Services (CU-06) | CU | ready · draft | [#16](https://github.com/rimone0511/autopilot-log/pull/16) |
| CU handoff Lancers + CrowdWorks | [`earn-lancers-cw-cu-handoff-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-lancers-cw-cu-handoff-a8a0/earn-lancers-cw-cu-handoff-20260916) | Lancers (CU-03) `blocked_skip` captcha; **CrowdWorks (CU-04) next CU** | CU | ready · draft · Lancers skip / CW next | [#17](https://github.com/rimone0511/autopilot-log/pull/17) |
| CU handoff TimeTicket + Contra + Craudia | [`earn-timeticket-contra-craudia-handoff-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-tt-contra-craudia-handoff-37db/earn-timeticket-contra-craudia-handoff-20260916) | TimeTicket (CU-07), Contra (CU-08), クラウディア (CU-09) | CU | ready · draft | [#18](https://github.com/rimone0511/autopilot-log/pull/18) |
| Freelancer.com profile + Wave B catalog-gap notes | [`earn-freelancer-waveb-gap-notes-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-freelancer-waveb-gap-notes-40b7/earn-freelancer-waveb-gap-notes-20260916) | Freelancer.com (CU-10); notes: AI CrowdWorks, Skill Shift（DMM生成AI人材バンク / Workshift は QUEUE 外） | CU（profile） / prep（gap notes） | ready · draft · no bids | [#19](https://github.com/rimone0511/autopilot-log/pull/19) |
| Wave D late activity-gate (D11–D20) | [`earn-activity-gate-wave-d-late-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-activity-gate-wave-d-late-4f33/earn-activity-gate-wave-d-late-20260916) | Comet, Replit Bounties, Superpeer, We Work Remotely, Remote OK, Himalayas, ココナラテック, Findy Freelance, PRONI アイミツ, 比較ビズ | prep | ready · draft · keep 0 / skip 10 | [#20](https://github.com/rimone0511/autopilot-log/pull/20) |
| Wave B ALIVE CU-ready profile sample | [`earn-waveb-alive-handoff-sample-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-waveb-alive-handoff-a6eb/earn-waveb-alive-handoff-sample-20260916) | SOKUDAN, Anycrew, 複業クラウド, MENTA, ストアカ | CU | ready · draft · Wave A のあと | [#21](https://github.com/rimone0511/autopilot-log/pull/21) |
| Wave D-early activity-gate (D01–D10) | [`earn-activity-gate-wave-d-early-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-activity-gate-wave-d-early-3a00/earn-activity-gate-wave-d-early-20260916) | Shufti, カイコク, note, Braintrust, Twine, Fastwork, Twago, 99freelas, Gulp, Xing Projects | prep | ready · draft · keep_queue 6 / skip_log 2 / needs_check 2 | [#22](https://github.com/rimone0511/autopilot-log/pull/22) |
| ops-bake PARALLEL-CAP APPLY-WINDOW | [`ops-parallel-cap-bake-skeleton-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/ops-parallel-cap-bake-skeleton-31df/ops-parallel-cap-bake-skeleton-20260916) | マーケット机ではない（並行キャップ。本番未適用。CU mutex=1） | prep | ready · draft · 本番未適用 | [#23](https://github.com/rimone0511/autopilot-log/pull/23) |
| REGISTER-BOARD (Wave A–D CU status) | [`earn-register-progress-board-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-register-progress-board-5458/earn-register-progress-board-20260916) | Wave A–D の机（フォルダ名のみ。#1–#22）。**Fiverr/Lancers skip · CW next** の正本 | prep | ready · draft | [#24](https://github.com/rimone0511/autopilot-log/pull/24) |
| World gigs scan wave2 | [`earn-world-gigs-scan-wave2-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-world-gigs-scan-wave2-d86f/earn-world-gigs-scan-wave2-20260916) | JP+EN ボードの AI-agent/automation パターン地図（30）。登録ではない | prep | ready · draft | [#25](https://github.com/rimone0511/autopilot-log/pull/25) |
| ops GROK-HEAD-THIN-HANDS bake skeleton | [`ops-grok-head-thin-hands-bake-skeleton-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/ops-grok-head-thin-hands-skeleton-1bcc/ops-grok-head-thin-hands-bake-skeleton-20260916) | マーケット机ではない（Pro 未着。本番未適用） | prep | ready · draft · 本番未適用 | [#26](https://github.com/rimone0511/autopilot-log/pull/26) |
| X keyword pack + triage rubric | [`earn-x-leads-keyword-pack-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-x-leads-keyword-pack-8ee4/earn-x-leads-keyword-pack-20260916) | X（Twitter）公開 Latest 用。APIなし。投稿・DMなし | prep | ready · draft · 検索未実行 | [#27](https://github.com/rimone0511/autopilot-log/pull/27) |
| JP Wave 2 proposal DRAFTs | [`earn-jp-proposal-wave2-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-jp-proposal-wave2-097d/earn-jp-proposal-wave2-20260916) | CrowdWorks, Lancers, Coconala（n8n / 分類 / AI運用 / 日英文） | prep | ready · draft · DO NOT SEND | [#28](https://github.com/rimone0511/autopilot-log/pull/28) |
| Wave B GLOBAL CU handoff | [`earn-waveb-global-handoff-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-waveb-global-handoff-e27c/earn-waveb-global-handoff-20260916) | Guru.com, Malt.com, Workana, Freelancermap, PeoplePerHour（PPH は有料 Basic を買わない） | CU | ready · draft · Wave A のあと | [#29](https://github.com/rimone0511/autopilot-log/pull/29) |
| Wave B batch2 CU-ready profiles | [`earn-waveb-cu-handoff-batch2-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-waveb-cu-handoff-batch2-87d0/earn-waveb-cu-handoff-batch2-20260916) | Workship, CrowdLinks, ITプロパートナーズ, Offers, YOUTRUST | CU | ready · draft · Wave A のあと | [#30](https://github.com/rimone0511/autopilot-log/pull/30) |
| EN Wave 2 proposal DRAFTs | [`earn-en-proposal-wave2-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-en-proposal-wave2-7659/earn-en-proposal-wave2-20260916) | Upwork, Fiverr, Contra（n8n / lead classify / AI ops / JP-EN） | prep | ready · draft · DO NOT SEND | [#31](https://github.com/rimone0511/autopilot-log/pull/31) |
| CrowdWorks + Upwork field maps | [`earn-cw-upwork-fieldmap-livecheck-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-cw-upwork-fieldmap-livecheck-ce1d/earn-cw-upwork-fieldmap-livecheck-20260916) | CrowdWorks worker signup; Upwork freelancer profile（公開ヘルプ。ログイン後フォームは対象外） | prep | ready · draft · CU playbook ではない | [#32](https://github.com/rimone0511/autopilot-log/pull/32) |
| MASTER INDEX refresh (this pack) | [`earn-master-index-refresh-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-master-index-refresh-127d/earn-master-index-refresh-20260916) | 上の全パックを束ねる。机の貼る順は持たない | prep | ready · draft | this PR |

QUEUE 内の [`ACTIVITY-GATE.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-register-expand-20260916-b673/earn-register-expand-20260916/ACTIVITY-GATE.md) は **目視チェックリストの型**（件数を作らない）。結果表ではない。結果は PR#2 入れ子、PR#12、PR#13、PR#20、PR#22。

この契約は **#1–#32**。#33 以降が開いていても、この表には足さない。

---

## 開いているPR（#1–#32）

`gh pr list --state open` で読んだ。マージ済み・クローズは 0。#1 と #2 だけ draft 解除済み。

| PR# | Draft? | Title | Branch | Folder |
|---|---|---|---|---|
| [#1](https://github.com/rimone0511/autopilot-log/pull/1) | open | earn-ops: expanded marketplace registration queue (2026-09-16) | `cursor/earn-register-expand-20260916-b673` | `earn-register-expand-20260916/` |
| [#2](https://github.com/rimone0511/autopilot-log/pull/2) | open | Week-2 GLOBAL earn-ops draft packs (Guru, PPH Hourlies, Malt, Workana) | `cursor/earn-register-packs-week2-a398` | `earn-register-packs-20260916/` |
| [#3](https://github.com/rimone0511/autopilot-log/pull/3) | draft | earn-ops: JP Week2 marketplace paste packs (CU-11–CU-18, draft) | `cursor/jp-earn-register-packs-8df7` | `earn-register-packs-jp-20260916/` |
| [#4](https://github.com/rimone0511/autopilot-log/pull/4) | draft | earn-ops: 朝の本人確認1枚（2026-09-16） | `cursor/earn-kyc-morning-checklist-9baf` | `earn-kyc-morning-checklist-20260916/` |
| [#5](https://github.com/rimone0511/autopilot-log/pull/5) | draft | earn-ops: EN HANDS proposal + invite drafts (Upwork/Fiverr/Contra) | `cursor/earn-en-proposal-drafts-b102` | `earn-en-proposal-drafts-20260916/` |
| [#6](https://github.com/rimone0511/autopilot-log/pull/6) | draft | earn-ops: Fiverr n8n Gig DRAFT pack (unpublished, 2026-09-16) | `cursor/earn-fiverr-gig-draft-91ed` | `earn-fiverr-gig-draft-20260916/` |
| [#7](https://github.com/rimone0511/autopilot-log/pull/7) | draft | earn-ops: thick CU serial runbook (Wave A remaining → Wave B passes) | `cursor/earn-cu-serial-runbook-2e17` | `earn-cu-runbook-20260916/` |
| [#8](https://github.com/rimone0511/autopilot-log/pull/8) | draft | earn-ops: merge register-pack INDEX (CU serial, 2026-09-16) | `cursor/earn-register-pack-index-45e2` | `earn-register-pack-index-20260916/` |
| [#9](https://github.com/rimone0511/autopilot-log/pull/9) | draft | ops-bake: draft APPLY docs for ORCH, CLI COMMON, and GrokBOT Head | `cursor/ops-bake-orch-cli-20260916-ad2e` | `ops-bake-orch-cli-20260916/` |
| [#10](https://github.com/rimone0511/autopilot-log/pull/10) | draft | earn-ops: Upwork Project Catalog draft (3 tiers, EN 800) | `cursor/earn-upwork-catalog-draft-0e79` | `earn-upwork-catalog-draft-20260916/` |
| [#11](https://github.com/rimone0511/autopilot-log/pull/11) | draft | earn-ops: JP marketplace proposal DRAFT pack (CW/Lancers/Coconala) | `cursor/jp-proposal-drafts-c1d1` | `earn-jp-proposal-drafts-20260916/` |
| [#12](https://github.com/rimone0511/autopilot-log/pull/12) | draft | earn-ops: JP Wave B activity-gate results (2026-09-16) | `cursor/earn-activity-gate-waveb-jp-fced` | `earn-activity-gate-waveB-20260916/` |
| [#13](https://github.com/rimone0511/autopilot-log/pull/13) | draft | earn-ops: Wave D Fit-Med activity-gate (2026-09-16) | `cursor/earn-activity-gate-waved-b552` | `earn-activity-gate-waveD-20260916/` |
| [#14](https://github.com/rimone0511/autopilot-log/pull/14) | draft | earn-ops: MASTER INDEX linking register/handoff/activity-gate packs (2026-09-16) | `cursor/earn-register-pack-master-index-9290` | `earn-register-pack-master-index-20260916/` |
| [#15](https://github.com/rimone0511/autopilot-log/pull/15) | draft | earn-ops: Fiverr Requirements + FAQ polish (unpublished n8n, 2026-09-16) | `cursor/earn-fiverr-req-faq-polish-7daf` | `earn-fiverr-requirements-faq-polish-20260916/` |
| [#16](https://github.com/rimone0511/autopilot-log/pull/16) | draft | earn-ops: CU handoff DRAFT packs (Upwork + LinkedIn Services) | `cursor/earn-upwork-linkedin-cu-handoff-a525` | `earn-upwork-linkedin-cu-handoff-20260916/` |
| [#17](https://github.com/rimone0511/autopilot-log/pull/17) | draft | earn-ops: thick CU handoff for Lancers + CrowdWorks (after Fiverr) | `cursor/earn-lancers-cw-cu-handoff-a8a0` | `earn-lancers-cw-cu-handoff-20260916/` |
| [#18](https://github.com/rimone0511/autopilot-log/pull/18) | draft | earn-ops: CU-07/08/09 handoff DRAFT (TimeTicket, Contra, Craudia) | `cursor/earn-tt-contra-craudia-handoff-37db` | `earn-timeticket-contra-craudia-handoff-20260916/` |
| [#19](https://github.com/rimone0511/autopilot-log/pull/19) | draft | earn-ops: Freelancer.com profile DRAFT + Wave B catalog-gap notes | `cursor/earn-freelancer-waveb-gap-notes-40b7` | `earn-freelancer-waveb-gap-notes-20260916/` |
| [#20](https://github.com/rimone0511/autopilot-log/pull/20) | draft | earn-ops: Wave D late activity-gate (D11–D20, 2026-09-16) | `cursor/earn-activity-gate-wave-d-late-4f33` | `earn-activity-gate-wave-d-late-20260916/` |
| [#21](https://github.com/rimone0511/autopilot-log/pull/21) | draft | earn-ops: Wave B ALIVE CU-ready DRAFT profile packs (5 desks) | `cursor/earn-waveb-alive-handoff-a6eb` | `earn-waveb-alive-handoff-sample-20260916/` |
| [#22](https://github.com/rimone0511/autopilot-log/pull/22) | draft | earn-ops: Wave D-early activity-gate (D01–D10, 2026-09-16) | `cursor/earn-activity-gate-wave-d-early-3a00` | `earn-activity-gate-wave-d-early-20260916/` |
| [#23](https://github.com/rimone0511/autopilot-log/pull/23) | draft | ops-bake: skeleton APPLY-WINDOW for parallel caps (awaiting PARALLEL-CAP-PERF) | `cursor/ops-parallel-cap-bake-skeleton-31df` | `ops-parallel-cap-bake-skeleton-20260916/` |
| [#24](https://github.com/rimone0511/autopilot-log/pull/24) | draft | earn-ops: Wave A–D REGISTER-BOARD (CU status, 2026-09-16) | `cursor/earn-register-progress-board-5458` | `earn-register-progress-board-20260916/` |
| [#25](https://github.com/rimone0511/autopilot-log/pull/25) | draft | earn-ops: world gigs scan wave2 (30 AI-agent/automation patterns) | `cursor/earn-world-gigs-scan-wave2-d86f` | `earn-world-gigs-scan-wave2-20260916/` |
| [#26](https://github.com/rimone0511/autopilot-log/pull/26) | draft | ops: GROK-HEAD-THIN-HANDS bake skeleton (awaiting Pro) | `cursor/ops-grok-head-thin-hands-skeleton-1bcc` | `ops-grok-head-thin-hands-bake-skeleton-20260916/` |
| [#27](https://github.com/rimone0511/autopilot-log/pull/27) | draft | earn-ops: X keyword pack + triage rubric for AI-agent freelance leads (JP+EN) | `cursor/earn-x-leads-keyword-pack-8ee4` | `earn-x-leads-keyword-pack-20260916/` |
| [#28](https://github.com/rimone0511/autopilot-log/pull/28) | draft | earn-ops: JP Wave 2 proposal DRAFT pack (n8n / 分類 / AI運用 / 日英文) | `cursor/earn-jp-proposal-wave2-097d` | `earn-jp-proposal-wave2-20260916/` |
| [#29](https://github.com/rimone0511/autopilot-log/pull/29) | draft | earn-ops: Wave B GLOBAL CU handoff DRAFT (Guru, Malt, Workana, Freelancermap, PPH) | `cursor/earn-waveb-global-handoff-e27c` | `earn-waveb-global-handoff-20260916/` |
| [#30](https://github.com/rimone0511/autopilot-log/pull/30) | draft | earn-ops: Wave B batch2 CU-ready DRAFT profile packs (5 desks) | `cursor/earn-waveb-cu-handoff-batch2-87d0` | `earn-waveb-cu-handoff-batch2-20260916/` |
| [#31](https://github.com/rimone0511/autopilot-log/pull/31) | draft | earn-ops: Wave 2 EN proposal DRAFTs (n8n / lead classify / AI ops / JP-EN) | `cursor/earn-en-proposal-wave2-7659` | `earn-en-proposal-wave2-20260916/` |
| [#32](https://github.com/rimone0511/autopilot-log/pull/32) | draft | earn-ops: CrowdWorks + Upwork field maps (public help, DRAFT) | `cursor/earn-cw-upwork-fieldmap-livecheck-ce1d` | `earn-cw-upwork-fieldmap-livecheck-20260916/` |

`master` には earn-ops フォルダはまだ無い（YouTube/TikTok CLI のみ）。

種別の束ね（本文は開かない）:

| 種別 | PR# |
|---|---|
| register（QUEUE / ペーストパック / ボード / 索引） | #1 #2 #3 #8 #14 #24 · this |
| handoff（CU 手渡し） | #4（朝の本人） #16 #17 #18 #19 #21 #29 #30 |
| activity-gate | #2（入れ子） #12 #13 #20 #22 |
| proposal（送らない） | #5 #11 #28 #31 |
| listing paste（unpublished） | #6 #10 #15 |
| field map（prep） | #32 |
| ops / scan | #7 #9 #23 #25 #26 #27 |

---

## Activity-gate 結果の束ね（prep。登録ではない）

件数・GMVは作っていない。ラベルは各ゲートPRの本文どおり。

| Gate pack | PR# | pass / keep | needs_check / block | SKIP / fail |
|---|---|---|---|---|
| Week-2 GLOBAL | #2 | Guru; Malt（英語下書き） | PPH `blocked_paid_plan`（有料 Basic は買わない）。Workana の jobs 一覧 | — |
| JP Wave B | #12 | SOKUDAN, Workship, Skill Shift, ITプロパートナーズ, Offers | 複業クラウド, CrowdLinks, Anycrew, MENTA, ストアカ, AI CrowdWorks, YOUTRUST, Shufti | thin 0 / fail 0 |
| Wave D Fit-Med | #13 | SKIMA, Payhip, Ko-fi, Dribbble Services, Fastwork, Truelancer, Twine, ワークシフト, ママワークス | シュフティ（SPA空。薄いとは決めない） | 99designs `fail-thin`; Wellfound `fail-aggregator` |
| Wave D-early D01–D10 | #22 | keep_queue: note, Braintrust, Twine, Fastwork, 99freelas, Gulp | Shufti, カイコク | Twago `dead`; Xing Projects `dead` |
| Wave D late D11–D20 | #20 | keep 0 | — | 10机すべて skip（closed / aggregator / agent / thin） |

CU ランブック（#7）は Wave B を **gate `pass` の机だけ** に進める。`needs_check` はクリック時の目視。Wave D の `pass` も A/B より後ろ。D-late は CU で開かない。

Shufti は JP パックが `ready`（CU-18 / PR#3）でも、QUEUE と両ゲートで **登録前 `gate`**。

---

## 期待パスの更新（PR#8 の `unknown` から）

PR#8 は QUEUE 置き場 `earn-packs/<desk-slug>/` を期待する。そのパスは **まだ無い**。handoff / listing が別フォルダで `ready` になった机だけ下に書く。本文は複製しない。

### Wave A（Top10 + Gumroad）

| Pack | Path（QUEUE 期待） | 別フォルダで ready | Desk(s) | CU vs prep | Status | PR# |
|---|---|---|---|---|---|---|
| Top10 paste (missing) | `earn-packs/coconala/` | — | ココナラ（CU-01, QUEUE `done-draft`） | CU | unknown · no PR · BOARD `draft` | — |
| Top10 paste (missing) | `earn-packs/fiverr/` | listing #6 #15 | Fiverr（CU-02） | CU | unknown · no PR（登録プロフィール）。listing `ready`。CU `blocked_skip` hold | #6 #15 |
| Top10 paste (missing) | `earn-packs/lancers/` | handoff #17 | ランサーズ（CU-03） | CU | unknown · no PR（`earn-packs/`）。handoff `ready`。CU `blocked_skip` captcha | #17 |
| Top10 paste (missing) | `earn-packs/crowdworks/` | handoff #17 · field map #32 | **クラウドワークス（CU-04）next CU** | CU | unknown · no PR（`earn-packs/`）。handoff `ready` · **next CU** | #17 #32 |
| Top10 paste (missing) | `earn-packs/upwork/` | catalog #10 · handoff #16 · field map #32 | Upwork（CU-05） | CU | unknown · no PR（登録プロフィールの QUEUE パス）。別フォルダ `ready` | #10 #16 #32 |
| Top10 paste (missing) | `earn-packs/linkedin-services/` | handoff #16 | LinkedIn Services（CU-06）。Jobsボードは SKIP | CU | unknown · no PR（`earn-packs/`）。handoff `ready` | #16 |
| Top10 paste (missing) | `earn-packs/timeticket/` | handoff #18 | TimeTicket（CU-07） | CU | unknown · no PR（`earn-packs/`）。handoff `ready` | #18 |
| Top10 paste (missing) | `earn-packs/contra/` | handoff #18 | Contra（CU-08） | CU | unknown · no PR（`earn-packs/`）。handoff `ready` | #18 |
| Top10 paste (missing) | `earn-packs/craudia/` | handoff #18 | クラウディア（CU-09） | CU | unknown · no PR（`earn-packs/`）。handoff `ready` | #18 |
| Top10 paste (missing) | `earn-packs/freelancer-com/` | profile #19 | Freelancer.com（CU-10） | CU | unknown · no PR（`earn-packs/`）。profile `ready` | #19 |
| Top10 paste (missing) | `earn-packs/gumroad/` | — | Gumroad（A+, QUEUE `done-draft`。CU-11 をずらさない） | CU | unknown · no PR · BOARD `draft` | — |

Fiverr / Upwork は **出品文** があっても、QUEUE が想定する `earn-packs/<desk>/` は未作成。無いときはランブックの generic field map。あるときは live form を正とする。#32 は公開ヘルプのラベル地図であり、ログイン後フォームの正本ではない。

### Week2 残り（QUEUE B12–B17 = CU-23–CU-28）

| Pack | Path（QUEUE 期待） | 別フォルダで ready | Desk(s) | CU vs prep | Status | PR# |
|---|---|---|---|---|---|---|
| Week2-rest paste (missing) | `earn-packs/freelancermap/` | GLOBAL handoff #29 | Freelancermap（CU-23） | CU | unknown · no PR（`earn-packs/`）。handoff `ready` | #29 |
| Week2-rest paste (missing) | `earn-packs/youtrust/` | batch2 #30 | YOUTRUST（CU-24）。gate `needs_check` | CU | unknown · no PR（`earn-packs/`）。handoff `ready` | #30 |
| Week2-rest paste (missing) | `earn-packs/offers/` | batch2 #30 | Offers（CU-25）。gate `pass` | CU | unknown · no PR（`earn-packs/`）。handoff `ready` | #30 |
| Week2-rest paste (missing) | `earn-packs/ai-crowdworks/` | gap notes #19 | AI CrowdWorks（CU-26）。gate `needs_check` | CU | unknown · no PR。notes only | #19 |
| Week2-rest paste (missing) | `earn-packs/skill-shift/` | gap notes #19 | Skill Shift（CU-27）。gate `pass`（公式は skill-shift.com） | CU | unknown · no PR。notes only | #19 |
| Week2-rest paste (missing) | `earn-packs/itpropartners/` | batch2 #30 | ITプロパートナーズ（CU-28）。gate `pass` | CU | unknown · no PR（`earn-packs/`）。handoff `ready` | #30 |

JP Week2 の薄いパックは #3 のまま。厚い handoff は #21（5机）と #30（別5机）。GLOBAL 薄いパックは #2、厚い handoff は #29（Freelancermap を含む）。

### この索引にパック行を足さないもの

順だけ QUEUE にあり、パックPRも（ゲート結果以外）無い。CU番号は振らない（PR#8 と同じ）。

- **Wave C Fit High 残り**: ビザスク, クラウドテック, レバテック, note, BOOTH, Kwork, Codementor, Braintrust（note / Braintrust は #22 で keep_queue。波の正は C）
- **LATE**: Zapier / Make / n8n パートナー, Toptal（朝の本人。エージェントは申請しない）
- **SKIP**: PR#1 `SKIP.md` と、#13 の 99designs / Wellfound、#22 の Twago / Xing Projects、#20 の D11–D20

Wave D の `pass` 机にもペーストパックPRはまだ無い（ゲートだけ）。CU は A/B の後ろ。

---

## 使い方

1. **どのフォルダ／PRか** はこの表。
2. **どの机を何番で貼るか** は [PR#8](https://github.com/rimone0511/autopilot-log/pull/8)。波と `done-draft` は [PR#1 QUEUE](https://github.com/rimone0511/autopilot-log/pull/1)。
3. **いま開く CU** は CrowdWorks（#17 の `02-crowdworks.md`）。Fiverr は `blocked_skip` hold。Lancers は `blocked_skip` captcha。#32 はラベル地図だけ（playbook にしない）。
4. MAIN Google。別アカウントを増やさない。
5. 活動ゲートが `needs_check` / `gate` の机は、公開一覧の日付を目視するまで登録しない。
6. KYC・有料プラン・出品公開で止める。提案文（#5 / #11 / #28 / #31）は **送らない**。
7. 値はプレースホルダのまま。実メール・パスワード・身分証はリポジトリに書かない。

## このPRでやらないこと

- パック本文の複製
- アカウント作成、本人確認、出品公開、提案送信
- 秘密・実メール・実電話のコミット
- 案件数・GMV・「稼げる額」の創作
- 兄弟PRのマージや draft 解除
- Fiverr hold / Lancers captcha の再試行

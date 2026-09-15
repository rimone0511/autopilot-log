# earn-register MASTER INDEX — 2026-09-16

観測日: 2026-09-15〜16（公開ページ。ブラウザ登録はしていない）  
索引日: 2026-09-16  
スナップショット: **2026-09-15 UTC** 時点の `rimone0511/autopilot-log` 開いているPR（#1–#13）と、その枝のフォルダ  
状態: **DRAFT-ONLY**（このPRは地図だけ。パック本文はコピーしない）  
禁止: 秘密の記入、ブラウザ登録、公開、KYC完了、有料プラン加入

これは earn-ops の **フォルダ単位マスター索引**。  
register / handoff / activity-gate / listing / ops と、同日に開いているPRを1枚で辿る。

机単位の貼る順（CU-01–CU-28）は複製しない。それは [PR#8](https://github.com/rimone0511/autopilot-log/pull/8) `earn-register-pack-index-20260916/INDEX.md`。

認証: MAIN Google のみ。KYC が出たら朝の本人へ。エージェントは進めない。

---

## 列の読み方

| 列 | 意味 |
|---|---|
| Pack name | フォルダの役割名。本文の題名ではない |
| Path | マージ後のリポジトリ相対。未マージなら出典PRの枝にある |
| Desk(s) | そのパックが扱う机。QUEUE の波番号は参考 |
| CU vs prep | **CU** = computer-use 直列で開く／貼るもの。**prep** = ゲート・索引・朝の本人・HANDS提案・ops。prep を CU ブラウザで登録してはいけない |
| Status | パックファイルの有無とPR状態。登録済みではない |
| PR | 2026-09-15 UTC 時点で確認した GitHub PR。無ければ `—` |

### Status 記号

| 記号 | 意味 |
|---|---|
| `ready · open` | 兄弟PRにファイルがある。PRは下書き解除済み |
| `ready · draft` | 兄弟PRにファイルがある。PRは draft |
| `unknown · no PR` | 机または置き場は QUEUE / ランブックにあるが、パックファイルがどの枝にも無い |
| `this PR · draft` | この MASTER INDEX 自身 |

`ready` は「登録済み」ではない。QUEUE の `done-draft` / `next` / `week-2` / `gate` / `late` は登録作業の状態で、別物。

パス列のリンクは **出典PRの枝**（未マージ）を指す。`master` にはまだ無い。

---

## MASTER 表（フォルダ）

上から「先に読む順」。CU直列の机順ではない。

| Pack name | Path | Desk(s) | CU vs prep | Status | PR |
|---|---|---|---|---|---|
| Register QUEUE (expand) | [`earn-register-expand-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-register-expand-20260916-b673/earn-register-expand-20260916) | Wave A–D の全机（順の正本）。Coconala / Gumroad は QUEUE 上 `done-draft` | CU | ready · open | [#1](https://github.com/rimone0511/autopilot-log/pull/1) |
| Week-2 GLOBAL register packs | [`earn-register-packs-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-register-packs-week2-a398/earn-register-packs-20260916) | Guru.com, PeoplePerHour (Hourlies/Offers), Malt.com, Workana | CU | ready · open | [#2](https://github.com/rimone0511/autopilot-log/pull/2) |
| Week-2 GLOBAL activity-gate (nested) | [`earn-register-packs-20260916/ACTIVITY-GATE-week2-global.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-register-packs-week2-a398/earn-register-packs-20260916/ACTIVITY-GATE-week2-global.md) | 同上4机 | prep | ready · open · Guru `pass` / Malt `pass`（下書き） / PPH `blocked_paid_plan` / Workana jobs `needs_check` | [#2](https://github.com/rimone0511/autopilot-log/pull/2) |
| JP Week2 register packs | [`earn-register-packs-jp-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/jp-earn-register-packs-8df7/earn-register-packs-jp-20260916) | Workship, 複業クラウド, SOKUDAN, CrowdLinks, Anycrew, MENTA, ストアカ, Shufti（CU-11–CU-18。在庫01–08ではない） | CU | ready · draft | [#3](https://github.com/rimone0511/autopilot-log/pull/3) |
| KYC morning handoff | [`earn-kyc-morning-checklist-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-kyc-morning-checklist-9baf/earn-kyc-morning-checklist-20260916) | Wave A（LinkedIn Services / Gumroad は対象外）。Wave B は画面が出たときだけ | prep | ready · draft | [#4](https://github.com/rimone0511/autopilot-log/pull/4) |
| EN HANDS proposal + invite | [`earn-en-proposal-drafts-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-en-proposal-drafts-b102/earn-en-proposal-drafts-20260916) | Upwork, Fiverr, Contra | prep | ready · draft · DO NOT SEND | [#5](https://github.com/rimone0511/autopilot-log/pull/5) |
| Fiverr n8n Gig listing paste | [`earn-fiverr-gig-draft-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-fiverr-gig-draft-91ed/earn-fiverr-gig-draft-20260916) | Fiverr（CU-02。ギグは Draft のまま） | CU | ready · draft · unpublished | [#6](https://github.com/rimone0511/autopilot-log/pull/6) |
| CU serial runbook | [`earn-cu-runbook-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-cu-serial-runbook-2e17/earn-cu-runbook-20260916) | Wave A 残り（Fiverr→…→Freelancer.com）→ Wave B の gate `pass` のみ | CU | ready · draft | [#7](https://github.com/rimone0511/autopilot-log/pull/7) |
| CU serial register-pack INDEX | [`earn-register-pack-index-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-register-pack-index-45e2/earn-register-pack-index-20260916) | CU-01–CU-28（机単位の期待パス） | prep | ready · draft | [#8](https://github.com/rimone0511/autopilot-log/pull/8) |
| ops-bake ORCH / CLI / GrokBOT Head | [`ops-bake-orch-cli-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/ops-bake-orch-cli-20260916-ad2e/ops-bake-orch-cli-20260916) | マーケット机ではない（運用焼き込み。本番未適用） | prep | ready · draft · 本番未適用 | [#9](https://github.com/rimone0511/autopilot-log/pull/9) |
| Upwork Project Catalog listing paste | [`earn-upwork-catalog-draft-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-upwork-catalog-draft-0e79/earn-upwork-catalog-draft-20260916) | Upwork（CU-05。Catalog は Submit しない） | CU | ready · draft · unpublished | [#10](https://github.com/rimone0511/autopilot-log/pull/10) |
| JP HANDS proposal + estimate | [`earn-jp-proposal-drafts-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/jp-proposal-drafts-c1d1/earn-jp-proposal-drafts-20260916) | CrowdWorks, Lancers, Coconala | prep | ready · draft · DO NOT SEND | [#11](https://github.com/rimone0511/autopilot-log/pull/11) |
| JP Wave B activity-gate | [`earn-activity-gate-waveB-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-activity-gate-waveb-jp-fced/earn-activity-gate-waveB-20260916) | SOKUDAN, Workship, 複業クラウド, CrowdLinks, Anycrew, MENTA, ストアカ, Skill Shift, AI CrowdWorks, ITプロパートナーズ, YOUTRUST, Offers, Shufti | prep | ready · draft · pass 5 / needs_check 8 / SKIP thin 0 | [#12](https://github.com/rimone0511/autopilot-log/pull/12) |
| Wave D Fit-Med activity-gate | [`earn-activity-gate-waveD-20260916/`](https://github.com/rimone0511/autopilot-log/tree/cursor/earn-activity-gate-waved-b552/earn-activity-gate-waveD-20260916) | SKIMA, Payhip, Ko-fi, Dribbble Services, Fastwork, Truelancer, Twine, ワークシフト, ママワークス, 99designs, シュフティ, Wellfound | prep | ready · draft · pass 9 / needs_check 1 / SKIP 2 | [#13](https://github.com/rimone0511/autopilot-log/pull/13) |
| MASTER INDEX (this pack) | [`earn-register-pack-master-index-20260916/`](INDEX.md) | 上の全パックを束ねる。机の貼る順は持たない | prep | this PR · draft | this PR |

QUEUE 内の [`ACTIVITY-GATE.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-register-expand-20260916-b673/earn-register-expand-20260916/ACTIVITY-GATE.md) は **目視チェックリストの型**（件数を作らない）。結果表ではない。結果は PR#2 入れ子、PR#12、PR#13。

---

## 開いているPR（2026-09-15 UTC）

`gh pr list --state open` の13件。マージ済み・クローズは 0。この MASTER INDEX のPRは作成時点で14件目になる。

| PR | Draft? | Title | Branch | Folder |
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

`master` には earn-ops フォルダはまだ無い（YouTube/TikTok CLI のみ）。

---

## Activity-gate 結果の束ね（prep。登録ではない）

件数・GMVは作っていない。ラベルは各ゲートPRの本文どおり。

| Gate pack | PR | pass | needs_check / block | SKIP / fail |
|---|---|---|---|---|
| Week-2 GLOBAL | #2 | Guru; Malt（英語下書き） | PPH `blocked_paid_plan`（有料 Basic は買わない）。Workana の jobs 一覧 | — |
| JP Wave B | #12 | SOKUDAN, Workship, Skill Shift, ITプロパートナーズ, Offers | 複業クラウド, CrowdLinks, Anycrew, MENTA, ストアカ, AI CrowdWorks, YOUTRUST, Shufti | thin 0 / fail 0 |
| Wave D Fit-Med | #13 | SKIMA, Payhip, Ko-fi, Dribbble Services, Fastwork, Truelancer, Twine, ワークシフト, ママワークス | シュフティ（SPA空。薄いとは決めない。JP Wave B と同じ） | 99designs `fail-thin`; Wellfound `fail-aggregator` |

CU ランブック（#7）は Wave B を **gate `pass` の机だけ** に進める。`needs_check` はクリック時の目視。Wave D の `pass` も A/B より後ろ。

Shufti は JP パックが `ready`（CU-18 / PR#3）でも、QUEUE と両ゲートで **登録前 `gate`**。

---

## 期待パスだがパックPRが無いもの（`unknown · no PR`）

PR#8 と同じ契約。QUEUE の置き場は `earn-packs/<desk-slug>/`。中のファイル名は未定なのでフォルダだけ書く。  
ランブックの `earn-register-packs-top10-20260916/` もプレースホルダで、枝には無い。

### Top10 + Gumroad（Wave A）

| Pack name | Path | Desk(s) | CU vs prep | Status | PR |
|---|---|---|---|---|---|
| Top10 paste (missing) | `earn-packs/coconala/` | ココナラ（CU-01, QUEUE `done-draft`） | CU | unknown · no PR | — |
| Top10 paste (missing) | `earn-packs/fiverr/` | Fiverr（CU-02, QUEUE `next`）。ギグ本文は #6 が別フォルダで `ready` | CU | unknown · no PR（登録プロフィールパック） | — |
| Top10 paste (missing) | `earn-packs/lancers/` | ランサーズ（CU-03） | CU | unknown · no PR | — |
| Top10 paste (missing) | `earn-packs/crowdworks/` | クラウドワークス（CU-04） | CU | unknown · no PR | — |
| Top10 paste (missing) | `earn-packs/upwork/` | Upwork（CU-05）。Catalog 本文は #10 が別フォルダで `ready` | CU | unknown · no PR（登録プロフィールパック） | — |
| Top10 paste (missing) | `earn-packs/linkedin-services/` | LinkedIn Services（CU-06）。Jobsボードは SKIP | CU | unknown · no PR | — |
| Top10 paste (missing) | `earn-packs/timeticket/` | TimeTicket（CU-07） | CU | unknown · no PR | — |
| Top10 paste (missing) | `earn-packs/contra/` | Contra（CU-08） | CU | unknown · no PR | — |
| Top10 paste (missing) | `earn-packs/craudia/` | クラウディア（CU-09） | CU | unknown · no PR | — |
| Top10 paste (missing) | `earn-packs/freelancer-com/` | Freelancer.com（CU-10） | CU | unknown · no PR | — |
| Top10 paste (missing) | `earn-packs/gumroad/` | Gumroad（A+, QUEUE `done-draft`。CU-11 をずらさない） | CU | unknown · no PR | — |

Fiverr / Upwork は **出品文**（#6 / #10）があっても、QUEUE が想定する `earn-packs/<desk>/` 登録パックは未作成。無いときはランブックの generic field map。あるときは live form を正とする。

### Week2 残り（QUEUE B12–B17 = CU-23–CU-28）

JP 8机 + GLOBAL 4机のあと。ゲート記録（#12）は一部ある。ペーストパックは無い。

| Pack name | Path | Desk(s) | CU vs prep | Status | PR |
|---|---|---|---|---|---|
| Week2-rest paste (missing) | `earn-packs/freelancermap/` | Freelancermap（CU-23） | CU | unknown · no PR | — |
| Week2-rest paste (missing) | `earn-packs/youtrust/` | YOUTRUST（CU-24）。gate `needs_check` | CU | unknown · no PR | — |
| Week2-rest paste (missing) | `earn-packs/offers/` | Offers（CU-25）。gate `pass` | CU | unknown · no PR | — |
| Week2-rest paste (missing) | `earn-packs/ai-crowdworks/` | AI CrowdWorks（CU-26）。gate `needs_check` | CU | unknown · no PR | — |
| Week2-rest paste (missing) | `earn-packs/skill-shift/` | Skill Shift（CU-27）。gate `pass`（公式は skill-shift.com） | CU | unknown · no PR | — |
| Week2-rest paste (missing) | `earn-packs/itpropartners/` | ITプロパートナーズ（CU-28）。gate `pass` | CU | unknown · no PR | — |

### この索引にパック行を足さないもの

順だけ QUEUE にあり、パックPRもゲート結果フォルダも無い。CU番号は振らない（PR#8 と同じ）。

- **Wave C Fit High 残り**: ビザスク, クラウドテック, レバテック, note, BOOTH, Kwork, Codementor, Braintrust
- **LATE**: Zapier / Make / n8n パートナー, Toptal（朝の本人。エージェントは申請しない）
- **SKIP**: PR#1 `SKIP.md`（閉鎖・本人専用・寄せ集め・現地労働・薄い机）と PR#13 で切った 99designs / Wellfound

Wave D の `pass` 9机にもペーストパックPRはまだ無い（ゲートだけ）。

---

## 使い方

1. **どのフォルダ／PRか** はこの表。
2. **どの机を何番で貼るか** は [PR#8](https://github.com/rimone0511/autopilot-log/pull/8)。Wave と `next` は [PR#1 QUEUE](https://github.com/rimone0511/autopilot-log/pull/1)。
3. Wave A の最初の `next`（いまは Fiverr）を1つだけ開く。パックが `unknown` なら QUEUE + ランブック。ギグ本文だけ #6 を使う。
4. MAIN Google。別アカウントを増やさない。
5. 活動ゲートが `needs_check` / `gate` の机は、公開一覧の日付を目視するまで登録しない。
6. KYC・有料プラン・出品公開で止める。提案文（#5 / #11）は **送らない**。
7. 値はプレースホルダのまま。実メール・パスワード・身分証はリポジトリに書かない。

## このPRでやらないこと

- パック本文の複製
- アカウント作成、本人確認、出品公開、提案送信
- 秘密・実メール・実電話のコミット
- 案件数・GMV・「稼げる額」の創作
- 兄弟PRのマージや draft 解除

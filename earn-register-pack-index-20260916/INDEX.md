# earn-register pack INDEX — 2026-09-16

観測日: 2026-09-15（公開ページ。ブラウザ登録はしていない）  
索引日: 2026-09-16  
状態: **DRAFT-ONLY**（このPRは索引だけ。パック本文はコピーしない）  
禁止: 秘密の記入、ブラウザ登録、公開、KYC完了、有料プラン加入

これは earn-ops の **貼る順（CU直列）** と、Top10 / Week2 JP / Week2 GLOBAL で **あるはずのファイル** の合併索引。  
パック本文は兄弟PRにある。このフォルダに実値・本人確認・出品文の完成形は置かない。

## 状態記号（この索引の Pack 列だけ）

| 記号 | 意味 |
|---|---|
| `ready` | ペーストパック（または作業順ドキュメント）が兄弟PRのパスに存在する。中身をこのPRへ複製していない |
| `unknown` | 机はキューにあるが、パックファイルがリポジトリ／既存PRに見当たらない。プレースホルダ |

`ready` は「登録済み」ではない。QUEUE の `done-draft` / `next` / `week-2` は登録作業の状態。Pack 列とは別物。

認証: MAIN Google のみ。KYC が出たら朝の本人へ。エージェントは進めない。

---

## CU直列（貼る順。在庫ファイル名の番号ではない）

上から 1 机。`unknown` の行はパックを書いてから貼る。`ready` でも公開・KYC・有料化はしない。

| CU直列 | Wave | 机 | 期待ファイル | Pack | QUEUE | 出典 |
|---|---|---|---|---|---|---|
| CU-01 | Top10 A1 | ココナラ Coconala | `earn-packs/coconala/` | `unknown` | `done-draft` | [PR#1](https://github.com/rimone0511/autopilot-log/pull/1) QUEUE。パックPRなし |
| CU-02 | Top10 A2 | Fiverr | `earn-packs/fiverr/` | `unknown` | `next` | PR#1 QUEUE（置き場の例もここ） |
| CU-03 | Top10 A3 | ランサーズ Lancers | `earn-packs/lancers/` | `unknown` | `next` | PR#1 QUEUE |
| CU-04 | Top10 A4 | クラウドワークス CrowdWorks | `earn-packs/crowdworks/` | `unknown` | `next` | PR#1 QUEUE |
| CU-05 | Top10 A5 | Upwork | `earn-packs/upwork/` | `unknown` | `next` | PR#1 QUEUE |
| CU-06 | Top10 A6 | LinkedIn Services | `earn-packs/linkedin-services/` | `unknown` | `next` | PR#1 QUEUE。Jobsボードは SKIP |
| CU-07 | Top10 A7 | TimeTicket | `earn-packs/timeticket/` | `unknown` | `next` | PR#1 QUEUE |
| CU-08 | Top10 A8 | Contra | `earn-packs/contra/` | `unknown` | `next` | PR#1 QUEUE |
| CU-09 | Top10 A9 | クラウディア Craudia | `earn-packs/craudia/` | `unknown` | `next` | PR#1 QUEUE |
| CU-10 | Top10 A10 | Freelancer.com | `earn-packs/freelancer-com/` | `unknown` | `next` | PR#1 QUEUE |
| A+ | Top10 | Gumroad | `earn-packs/gumroad/` | `unknown` | `done-draft` | PR#1 QUEUE。A+ であり **CU-11 は Workship のまま** |
| CU-11 | Week2 JP | Workship | `earn-register-packs-jp-20260916/02-workship.md` | `ready` | `week-2` | [PR#3](https://github.com/rimone0511/autopilot-log/pull/3) |
| CU-12 | Week2 JP | 複業クラウド | `earn-register-packs-jp-20260916/03-fukugyo-cloud.md` | `ready` | `week-2` | PR#3 |
| CU-13 | Week2 JP | SOKUDAN | `earn-register-packs-jp-20260916/01-sokudan.md` | `ready` | `week-2` | PR#3（在庫01 ≠ 直列13） |
| CU-14 | Week2 JP | CrowdLinks | `earn-register-packs-jp-20260916/04-crowdlinks.md` | `ready` | `week-2` | PR#3 |
| CU-15 | Week2 JP | Anycrew | `earn-register-packs-jp-20260916/05-anycrew.md` | `ready` | `week-2` | PR#3。人材側 |
| CU-16 | Week2 JP | MENTA | `earn-register-packs-jp-20260916/06-menta.md` | `ready` | `week-2` | PR#3 |
| CU-17 | Week2 JP | ストアカ | `earn-register-packs-jp-20260916/07-street-academy.md` | `ready` | `week-2` | PR#3 |
| CU-18 | Week2 JP | Shufti | `earn-register-packs-jp-20260916/08-shufti.md` | `ready` | `gate`（Wave D） | PR#3 Optional Med。QUEUE は登録前ゲート |
| CU-19 | Week2 GLOBAL | Guru.com | `earn-register-packs-20260916/01-guru-com-seller-profile-draft.md` | `ready` | `week-2` | [PR#2](https://github.com/rimone0511/autopilot-log/pull/2) |
| CU-20 | Week2 GLOBAL | PeoplePerHour (Hourlies/Offers) | `earn-register-packs-20260916/02-peopleperhour-hourlies-draft.md` | `ready` | `week-2` | PR#2。有料 Basic は買わない |
| CU-21 | Week2 GLOBAL | Malt.com (EU) | `earn-register-packs-20260916/03-malt-com-eu-draft.md` | `ready` | `week-2` | PR#2 |
| CU-22 | Week2 GLOBAL | Workana | `earn-register-packs-20260916/04-workana-draft.md` | `ready` | `week-2` | PR#2 |
| CU-23 | Week2 rest | Freelancermap | `earn-packs/freelancermap/` | `unknown` | `week-2` | PR#1 QUEUE B12 |
| CU-24 | Week2 rest | YOUTRUST | `earn-packs/youtrust/` | `unknown` | `week-2` | PR#1 QUEUE B13 |
| CU-25 | Week2 rest | Offers | `earn-packs/offers/` | `unknown` | `week-2` | PR#1 QUEUE B14 |
| CU-26 | Week2 rest | AI CrowdWorks | `earn-packs/ai-crowdworks/` | `unknown` | `week-2` | PR#1 QUEUE B15。売り手入口を先に目視 |
| CU-27 | Week2 rest | Skill Shift | `earn-packs/skill-shift/` | `unknown` | `week-2` | PR#1 QUEUE B16 |
| CU-28 | Week2 rest | ITプロパートナーズ | `earn-packs/itpropartners/` | `unknown` | `week-2` | PR#1 QUEUE B17 |

Wave A の `next`（CU-02→CU-10）が全部 `done-draft` になるまで Week2 は触らない（PR#3 INDEX と同じ）。  
CU-18 Shufti はパックが `ready` でも、QUEUE Wave D の ACTIVITY-GATE を通すまで登録しない。

---

## 期待ファイル在庫（Top10 + Week2 + GLOBAL）

パスはマージ後のリポジトリ相対。未マージの `ready` は出典PRの枝にある。

### 1. Top10 + Gumroad — 期待パック（すべて `unknown`）

Top10 のペーストパックPRは 2026-09-16 時点で無い。QUEUE の置き場契約は `earn-packs/<desk-slug>/`。中のファイル名は未定なのでフォルダだけを期待パスにする。

| 期待パス | 机 | Pack |
|---|---|---|
| `earn-packs/coconala/` | ココナラ | `unknown` |
| `earn-packs/fiverr/` | Fiverr | `unknown` |
| `earn-packs/lancers/` | ランサーズ | `unknown` |
| `earn-packs/crowdworks/` | クラウドワークス | `unknown` |
| `earn-packs/upwork/` | Upwork | `unknown` |
| `earn-packs/linkedin-services/` | LinkedIn Services | `unknown` |
| `earn-packs/timeticket/` | TimeTicket | `unknown` |
| `earn-packs/contra/` | Contra | `unknown` |
| `earn-packs/craudia/` | クラウディア | `unknown` |
| `earn-packs/freelancer-com/` | Freelancer.com | `unknown` |
| `earn-packs/gumroad/` | Gumroad | `unknown` |

QUEUE 本体（順だけ。パックではない）:

| 期待パス | Pack | 出典 |
|---|---|---|
| `earn-register-expand-20260916/QUEUE.md` | `ready` | [PR#1](https://github.com/rimone0511/autopilot-log/pull/1) |
| `earn-register-expand-20260916/SKIP.md` | `ready` | PR#1 |
| `earn-register-expand-20260916/ACTIVITY-GATE.md` | `ready` | PR#1 |

### 2. Week2 JP — 期待パック（在庫 01–08 + INDEX）

貼る順は上の CU-11–CU-18。ファイル名の 01–08 は在庫順。

| 期待パス | 机 | Pack | 出典 |
|---|---|---|---|
| `earn-register-packs-jp-20260916/JP-WEEK2-INDEX.md` | （JP直列の局所索引） | `ready` | [PR#3](https://github.com/rimone0511/autopilot-log/pull/3) |
| `earn-register-packs-jp-20260916/01-sokudan.md` | SOKUDAN | `ready` | PR#3 |
| `earn-register-packs-jp-20260916/02-workship.md` | Workship | `ready` | PR#3 |
| `earn-register-packs-jp-20260916/03-fukugyo-cloud.md` | 複業クラウド | `ready` | PR#3 |
| `earn-register-packs-jp-20260916/04-crowdlinks.md` | CrowdLinks | `ready` | PR#3 |
| `earn-register-packs-jp-20260916/05-anycrew.md` | Anycrew | `ready` | PR#3 |
| `earn-register-packs-jp-20260916/06-menta.md` | MENTA | `ready` | PR#3 |
| `earn-register-packs-jp-20260916/07-street-academy.md` | ストアカ | `ready` | PR#3 |
| `earn-register-packs-jp-20260916/08-shufti.md` | Shufti | `ready` | PR#3 |

### 3. Week2 GLOBAL — 期待パック（PR#2 のパスを正とする）

Guru / PeoplePerHour / Malt / Workana。ファイル名は PR#2 のまま。リネームしない。

| 期待パス | 机 | Pack | 出典 |
|---|---|---|---|
| `earn-register-packs-20260916/01-guru-com-seller-profile-draft.md` | Guru.com seller/profile | `ready` | [PR#2](https://github.com/rimone0511/autopilot-log/pull/2) |
| `earn-register-packs-20260916/02-peopleperhour-hourlies-draft.md` | PeoplePerHour Offers (legacy Hourlies) | `ready` | PR#2 |
| `earn-register-packs-20260916/03-malt-com-eu-draft.md` | Malt.com EU | `ready` | PR#2 |
| `earn-register-packs-20260916/04-workana-draft.md` | Workana freelancer/talent | `ready` | PR#2 |
| `earn-register-packs-20260916/ACTIVITY-GATE-week2-global.md` | GLOBAL ゲート要約 | `ready` | PR#2 |
| `earn-register-packs-20260916/README.md` | 共有プレースホルダと禁止事項 | `ready` | PR#2 |

GLOBAL の **クリック順**（ゲート文書。CU直列とは別）: Guru → Malt → Workana → PPH（有料壁を最後）。  
**CU直列** は QUEUE B8–B11 と PR#2 ファイル番号に合わせ、CU-19 Guru → CU-20 PPH → CU-21 Malt → CU-22 Workana。

### 4. Week2 残り — 期待パック（すべて `unknown`）

JP 8机 + GLOBAL 4机のあと。QUEUE Wave B の B12–B17。

| 期待パス | 机 | Pack |
|---|---|---|
| `earn-packs/freelancermap/` | Freelancermap | `unknown` |
| `earn-packs/youtrust/` | YOUTRUST | `unknown` |
| `earn-packs/offers/` | Offers | `unknown` |
| `earn-packs/ai-crowdworks/` | AI CrowdWorks | `unknown` |
| `earn-packs/skill-shift/` | Skill Shift | `unknown` |
| `earn-packs/itpropartners/` | ITプロパートナーズ | `unknown` |

---

## CU番号の付け方

1. **CU-01–CU-10** = QUEUE Wave A の A1–A10（Top10）。Gumroad は A+ で、CU-11 以降をずらさない。
2. **CU-11–CU-18** = [PR#3 `JP-WEEK2-INDEX.md`](https://github.com/rimone0511/autopilot-log/blob/cursor/jp-earn-register-packs-8df7/earn-register-packs-jp-20260916/JP-WEEK2-INDEX.md) の直列（Workship 起算）。QUEUE の B1=SOKUDAN 順ではない。
3. **CU-19–CU-22** = QUEUE B8–B11 = PR#2 の `01`–`04`（Guru → PPH → Malt → Workana）。
4. **CU-23–CU-28** = QUEUE B12–B17。パック未作成なので Pack=`unknown`。

このファイルを合併後の CU 正本にする。衝突したら QUEUE の波と PR#3 直列をこの表で読み替える。

---

## この索引に含めないもの

- **Wave C** Fit High 残り（ビザスク、クラウドテック、レバテック、note、BOOTH、Kwork、Codementor、Braintrust）と LATE パートナー（Zapier / Make / n8n / Toptal）— パック未作成。順は PR#1 `QUEUE.md`。
- **Wave D** Fit Med（ママワークス、Twine、99designs、Truelancer、Fastwork、Dribbble、Wellfound）。Shufti だけ JP Week2 パックがある（CU-18）。他はゲート前に登録しない。
- **SKIP**（Bizseek、サグー、Mercor/Outlier/DataAnnotation、寄せ集め、現地労働、薄い机）— PR#1 `SKIP.md`。CU を振らない。

---

## 使い方

1. Wave A の最初の `next`（いまは Fiverr = CU-02）を1つだけ開く。パックが `unknown` なら QUEUE の手順だけで下書きし、後でパックを足す。
2. MAIN Google。別アカウントを増やさない。
3. 人材／売り手側か確認。企業コンソールなら閉じる。
4. KYC・有料プラン・出品公開で止める。
5. 値はプレースホルダのまま。実メール・パスワード・身分証はリポジトリに書かない。
6. Week2 JP は CU-11 から。GLOBAL は CU-19 から（PR#2 パス）。

## このPRでやらないこと

- パック本文の複製
- アカウント作成、本人確認、出品公開
- 秘密・実メール・実電話のコミット
- 案件数・GMV・「稼げる額」の創作

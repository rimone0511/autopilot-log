# ACTIVITY-GATE — JP Wave B desks

観測日: **2026-09-16 JST**  
方法: 公開 URL の GET。ログインなし。登録なし。有料なし。  
フォルダ: `earn-activity-gate-waveB-20260916/`

QUEUE の売り手入口と、今回実際に開いた公開 URL が違う場合は **開いた URL を正** とし、QUEUE 側はメモする。

---

## Summary

| # | 机 | 公式（QUEUE） | 活動の目視 | Google | 無料の売り手入口 | Gate |
|---|---|---|---|---|---|---|
| B1 | SOKUDAN | https://sokudan.work/ | トップに案件カード。リモート可・一部不可が混在。一覧 `/top/projects` はフィルタ無しだと「案件が見つかりませんでした」 | 登録面に `/users/auth/google?category=signup` | 登録面「無料新規登録」 | **pass** |
| B2 | Workship | https://goworkship.com/ | `/portal/search` に案件カード。画面見出し `全238件中 1-20件`（マーケ合計ではなく、その画面のページ見出し） | 登録は SNS。Google アイコンは **needs_check** | `/signup` タイトル「フリーランス登録をする」 | **pass** |
| B3 | 複業クラウド | talent https://talent.aw-anotherworks.com/ | 個別 `/projects/{id}` のタイトルは求人。本文は SPA。日付は会社情報寄りで **案件の新しさは不明** | 公開 HTML ではボタン未確認 | 人材ドメイン 200。企業コンソールは使わない | **needs_check** |
| B4 | CrowdLinks | https://crowdlinks.jp/ | 個別 `/projects/{id}` に案件タイトル。一覧・本文はログイン誘導。ヘルプ FAQ 更新 **2026/8/1** | 登録 SPA。クリック時確認 | ワーカー新規登録 URL 200 | **needs_check** |
| B5 | Anycrew | 人材 https://www.any-crew.com/ | 人材アプリ https://app.any-crew.com/ は生きている。`/offers` は SPA 空。案件カードは未読 | アプリに「Googleでログイン」 | 「FacebookかGoogleのアカウントで利用登録」。Facebook は新規作成しない | **needs_check** |
| B6 | MENTA | https://menta.work/ | トップは Chrome UA で 200。`/plan` と登録はこの環境で AWS WAF **202** | 登録面が WAF。パック記載の OAuth は未確認 | メンター導線は公式にあるが、カタログ日付は未読 | **needs_check** |
| B7 | ストアカ | https://www.street-academy.com/ | トップは WAF。ヘルプは Cloudflare 403。講師面 `/teach` は登録フォーム | OAuth の Google は公式ヘルプ上見当たらない（既存パックどおり） | `/teach`「無料ではじめられる」 | **needs_check** |
| B16 | Skill Shift | QUEUE `https://skillshift.jp/` は **接続失敗** | 公式は https://www.skill-shift.com/ 。公開 jobs API の `created_at` が **2026-09-11〜14**。オンライン／リモート中心の行あり | 未確認 | 個人ユーザー登録は公式サイト。有料壁は見ていない | **pass**（URL は QUEUE を公式ドメインに読み替え） |
| B15 | AI CrowdWorks | 入口は公式から辿る | 事前登録 LP は終了コピー。正式リリース記事 **2026-08-20**。公開仕事詳細は「読み込み中」。トップは依頼者向け | 登録は **メール**（https://crowdworks.jp/aicw/register/new_email）。Google 未確認 | 無料会員登録の画面あり。事前登録フォームは閉じている | **needs_check** |
| B17 | ITプロパートナーズ | https://itpropartners.com/ | 公開案件カード。例: 最終更新日 **2026/09/08**、フルリモートの行あり | `/register` 初面は職種選択。Google ボタンなし | `/register` 200。初面に有料壁なし | **pass** |
| B13 | YOUTRUST | https://youtrust.jp/ | ヘルプは「ジョブは全ユーザーに公開」。`/api/recruitment_posts` は未ログイン **401**。カード日付は未読 | ホーム HTML に Google 文字列あり。登録完走はしていない | サインアップ URL は LP へリダイレクト | **needs_check** |
| B14 | Offers | https://offers.jp/ | トップは転職寄りのコピー。**Jobs** https://offers.jp/jobs/engineer/side-job に業務委託カード。更新日 **2026-09-10**、フルリモート | LP に「Googleで登録する」 | 無料登録コピーあり。有料壁は見ていない | **pass**（転職だけではない。Jobs の業務委託を先に見る） |
| D1/CU-18 | Shufti | https://www.shufti.jp/ → アプリ https://app.shufti.jp/ | `/jobs/search` は SPA 空。ヘルプ「本人確認を行う」に **20260912** 系の更新。案件カードは未読 | パックは Google。この HTML ではボタン未描画 | `/signup` 200 | **needs_check**（本線一致は弱い。見えないので SKIP thin にしない） |

`fail`（閉鎖）: **0**  
`SKIP thin`: **0**（カタログが読めない机を薄いと決めない）  
`blocked_paid_plan`: **0**（公開面では課金必須を見ていない。有料化画面が出たら止める）

---

## 机ごとの証拠（短文）

マーケの「○万人／○件」は活動証明に使わない。以下は **この観測で画面または公式 HTML に出たもの**。

### SOKUDAN — pass

- トップ https://sokudan.work/ に案件見出しが並ぶ。例: 「【基本リモ】名古屋大学発AIスタートアップで業務設計から実装を担うFDE募集」「【週2～】Claude×Figma MCPでデザインを効率化するデザイナー」「【フルリモ／週10h〜】TikTok Shop立ち上げ・運用ディレクター募集」。リモート可と常駐が混在。
- ブログ日付 **2026.06.19**（導入事例）。カード自体の「○時間前」は未確認。
- `/top/projects` はフィルタ無しで「案件が見つかりませんでした」。トップカードを活動の根拠にする。一覧は人がフィルタして再確認。
- 登録 https://sokudan.work/signup/pro 「無料新規登録」。Google パスあり。
- 個別ページ例は「この案件は募集終了」もある。終了カードだけを机全体の死としない。

### Workship — pass

- https://goworkship.com/portal/search に案件カード。例: 「不動産業務の改善・AI自動化エンジニア募集」「LLM活用｜業務効率化・設計レビュー・テスト品質改善エンジニア募集」。リモート／副業 OK のフィルタがある。
- 画面見出し `全238件中 1-20件` は **そのページの表示**。GMV ではない。
- トップに `2026/09/07` などの日付文字列あり（ニュース／更新系。カードの投稿時刻ではない）。
- `/signup` 生きている。Google ラベルは人がアイコンを見る。

### 複業クラウド — needs_check

- https://talent.aw-anotherworks.com/ 200。企業向け https://cl.aw-anotherworks.com/ も公開。人材側だけ。
- 個別例: https://talent.aw-anotherworks.com/projects/91374 タイトル「法人SNS運用ディレクター募集」。本文はローダー。HTML 内の 2024/2025 は会社情報に見える。
- 公開一覧の「新着日付」は未読。合格にしない。

### CrowdLinks — needs_check

- ワーカー新規登録 https://crowdlinks.jp/worker/signup/ 200（シェル）。一覧 https://crowdlinks.jp/worker/projects/ はタイトルのみ。
- 個別例: https://crowdlinks.jp/projects/vjPMBUvY7cd04K457KSC タイトル「【フルリモート】フロントエンド兼コーダー募集！」。本文は稼働時間の入力誘導（ログイン側）。
- HTML 内の `20260915` は **AWS 署名の日時**であり、案件の公開日ではない。使わない。
- ヘルプ https://help.crowdlinks.jp/ ユーザー向け FAQ 更新 **2026/8/1 13:50**。机はメンテされている。カードの新しさはクリック時。

### Anycrew — needs_check

- https://app.any-crew.com/ 「FacebookかGoogleのアカウントで利用登録」「Googleでログイン」。企業 https://biz.any-crew.com/ は使わない。
- https://app.any-crew.com/offers は React シェルのみ。案件名は未読。

### MENTA — needs_check

- トップは UA 次第で 200。`/plan`・登録・OAuth はこの環境で WAF 202。
- カタログ日付が取れないので pass にしない。死滅証拠でもない。

### ストアカ — needs_check

- `/teach` タイトル「ストアカ講師/主催団体登録フォーム」。コピー「無料ではじめられる」「ストアカが集金を代行」。
- トップ WAF、support.street-academy.com は 403。講座ページは 405。講座の開催日は未読。
- Google OAuth は既存ヘルプどおり未確認。メール（MAIN Google のメール）は人がやる。

### Skill Shift — pass

- QUEUE の `https://skillshift.jp/` は接続失敗。公式は **https://www.skill-shift.com/**。
- 公開 `GET https://www.skill-shift.com/api/jobs`（サイトの求人検索が使うもの）。先頭行の `created_at`: **2026-09-14, 2026-09-13, 2026-09-12, 2026-09-11**。`is_recruiting: true`。
- 例（見出しのみ）: 「AI活用で業務効率化！業務棚卸しから始めるAIアドバイザー」（`side_job_style`: オンライン想定）、「【建設業×SNS】窓・ドアの魅力を届ける集客パートナー」（リモート基本）。対面ミックスの行もある。**全部が現地労働ではない**。
- API の pagination.total は書かない（活動証明に使わない）。
- 現場のみと分かった行は応募しない。机全体は SKIP しない。

### AI CrowdWorks — needs_check

- ニュース https://crowdworks.co.jp/news/akdv13x1sf/ : 正式リリース **2026年8月20日**。事前登録は終了。
- 人材登録の公開面: https://crowdworks.jp/aicw/register/new_email 「カンタン無料会員登録」。クラウドワークス ID または **メール**。Google ボタンは見ていない。
- トップ https://ai.crowdworks.jp/ は依頼者向け。「現在募集中の仕事」は仕事例のカテゴリ（Claude Code 利用支援など）で、日付付きの公開ボードではない。
- 仕事詳細例は「読み込み中」。売り手入口は開いているが、公開案件の新しさは不明。QUEUE どおり登録前に人が入口を辿る。

### ITプロパートナーズ — pass

- トップと https://itpropartners.com/job/sale-4 に業務委託カード。例: 最終更新日 **2026/09/08**「コーポレートIT／社内情報システム」（基本リモート一部出社）、**2026/09/05**「M&A事業部…アポ獲得」（フルリモート）。
- 登録 https://itpropartners.com/register 初面は職種選択。Google なし。エージェント型。面談が本人確認に乗ったら停止。
- `/signup` `/entry` は 404。入口は `/register`。

### YOUTRUST — needs_check

- https://youtrust.jp/ 200。ヘルプ: ジョブは全ユーザーに公開、Web は「ジョブ」メニュー。
- https://youtrust.jp/api/recruitment_posts は未ログイン 401。カードと日付は未読。
- SNS 実名連携を求められたら記録。KYC なら停止。

### Offers — pass

- トップは「AI時代のハイクラスエンジニア**転職**」。QUEUE の「転職導線だけなら再判定」は、Jobs を見て判定する。
- https://offers.jp/jobs/engineer/side-job に業務委託カード。例: 「【フルリモート】AI×FDE｜…」更新日 **2026-09-10**、雇用形態 業務委託、ラベル「今週活動あり・積極採用中」。
- LP に「Googleで登録する」。GitHub 連携は任意。有料ブースは買わない。

### Shufti — needs_check

- https://app.shufti.jp/signup ・ `/jobs/search` は SPA。カード未読。
- ヘルプ「本人確認を行う」は 200。KYC 画面は出さない。
- 製品コピーは在宅タスク寄り。本線（自動化の売り手）とは弱い。**カードを見ていないので SKIP thin にしない**。入力・モニターばかりなら人が SKIP thin。

---

## 認証・停止（全机共通）

1. MAIN Google のみ。別アカウントを作らない。
2. パスポート／免許／マイナンバー／顔写真／口座が出たら **アップロードせず停止**。
3. 有料会員・優先掲載・審査スキップは買わない。
4. プロフィール公開・出品公開・応募はしない。
5. 公開一覧が読めなければ `needs_check` のまま。数字を埋めない。

## オペレーター順（このゲートのあと）

1. **pass かつ パックがある机**（Workship → 複業クラウドは check 残り → SOKUDAN）— 下書きのみ
2. **pass でパックが薄い机** — ITプロパートナーズ、Offers Jobs、Skill Shift（公式ドメイン）
3. **needs_check** — 人が公開一覧の日付を1画面見てから。AI CrowdWorks はメール登録面まで見て、案件ボードが無ければプロフィール下書き可否だけ判断
4. Shufti は Optional Med。本線と違うカードなら SKIP thin を人が書く

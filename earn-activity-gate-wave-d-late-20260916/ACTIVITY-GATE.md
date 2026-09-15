# ACTIVITY-GATE — Wave D late desks (D11–D20)

観測日: **2026-09-16 JST**  
方法: 公開 URL の GET。ログインなし。登録なし。有料なし。  
フォルダ: `earn-activity-gate-wave-d-late-20260916/`

QUEUE の売り手入口と、今回実際に開いた公開 URL が違う場合は **開いた URL を正** とし、QUEUE 側はメモする。親 QUEUE には D11–D20 行が無い。

数値を作らない。公式が出していない件数・GMV・成約率・「月収」を書かない。`unknown` は不合格（登録しない）。

---

## Summary

| # | 机 | 公式（開いた URL） | 活動の目視 | Google | 無料の売り手入口 | Gate |
|---|---|---|---|---|---|---|
| D11 | Comet | https://www.comet.co/ | LP は 2026-09-15 公開。ミッションカードはプレースホルダ。`app.comet.co` は個人スペース閉鎖 | 未確認 | ダッシュボード閉鎖。Contact の CV 項目は送信していない | **fail-closed** |
| D12 | Replit Bounties | https://replit.com/bounties → Contra | Bounties 面は無い。Contra の Replit Experts ページ | Contra 側。完走していない | Bounties 入口は 301。Contra は Wave A | **fail-closed** |
| D13 | Superpeer | https://superpeer.com/ → Skillshare | スタンドアロン sunset **2024-12-31**（公式ヘルプ） | 未確認（Skillshare トップはこのIPで 403） | Superpeer 登録面は無い | **fail-closed** |
| D14 | We Work Remotely | https://weworkremotely.com/ | 求人ボード。「Latest post about 6 hours ago」。このIP curl は 403 | 未確認 | Post a job（雇用側）。売り手ギグなし | **fail-aggregator** |
| D15 | Remote OK | https://remoteok.com/ | 求人ボード。og:updated_time **2026-09-03**。カード相対時刻は未描画 | 未確認 | Post a Job（雇用側） | **fail-aggregator** |
| D16 | Himalayas | https://himalayas.app/ | Remote Job Board。`/jobs` はこのIPで 403 | 求職 Sign up with Google（未クリック） | Post a job（雇用側） | **fail-aggregator** |
| D17 | ココナラテック | https://tech.coconala.com/job-postings | NEW カード（PMO / PdM 等）。日付文字列は未確認 | このHTMLではボタン未確認 | LP `/#Registration`。その後 **登録面談** | **skip-agent** |
| D18 | Findy Freelance | https://freelance.findy-code.io/ | トップの案件例。カード日付は未確認。脚注 2026-01〜03 はアンケート期間 | 「Googleで登録し案件を探す」（未クリック） | トップの新規登録。その後 **審査＋面談** | **skip-agent** |
| D19 | PRONI アイミツ | https://imitsu.jp/ | 発注カテゴリと一括見積。受注は企業掲載 | 未確認 | `partner.imitsu.jp`（受注企業）。広告掲載料の FAQ | **fail-thin** |
| D20 | 比較ビズ | https://www.biz.ne.jp/ | 公開の見積依頼。記事例 **2026年09月11日** | 未確認 | `/seller/` 掲載・資料請求（企業・専門家） | **fail-thin** |

`pass`: **0**  
`needs_check`: **0**  
`fail-local` / `fail-identity` / `blocked_paid_plan`: **0**（有料掲載は thin 側で切った。料金表の送信はしていない）

---

## 机ごとの証拠（短文）

マーケの「○万人／○件」は活動証明に使わない。以下は **この観測で画面または公式 HTML に出たもの**。

### Comet — fail-closed

- https://www.comet.co/ : 「cabinet de conseil」「consultants indépendants」。Webflow Last Published **Tue Sep 15 2026**（サイトの公開日時であり、ミッション日ではない）。
- https://www.comet.co/fr ほか旧パスは 404「Notre ancien site a fermé ses portes」。
- https://www.comet.co/freelance → `/consultant`。「Nos dernières missions」の本文は Dementors / Hogwarts 風プレースホルダ。実案件名として使わない。
- https://app.comet.co/ : 「votre espace personnel est clôturé」。ミッション検索の自前机は閉じている。
- Contact に「Déposer votre CV」。送信していない。ヘルプデスクは 402。

### Replit Bounties — fail-closed

- https://replit.com/bounties と `/site/bounties` は **301** で https://contra.com/replit 。
- 到着ページ題「Hire Replit Experts for Your Web Project」。Bounties ボードは開かない。
- Contra は親 QUEUE Wave A。このゲートから登録しない。

### Superpeer — fail-closed

- https://superpeer.com/ は **301** で Skillshare。このIPの Skillshare トップは Cloudflare 403。
- https://help.skillshare.com/hc/en-us/articles/32235980292877-Sunsetting-Superpeer-as-a-Standalone-Site-December-2024 : スタンドアロン Superpeer を **December 31, 2024** までに sunset。以後の 1-on-1 / デジタル商品は Skillshare 側。
- Skillshare `/teach` は講師応募面。別机。完走していない。キューに足さない。

### We Work Remotely — fail-aggregator

- コピー「job board for remote jobs」。雇用側 Post a job。
- Jobs 面（Web 取得）: 「DevOps and Sysadmin Jobs Latest post about **6 hours ago**」。求人カード例: Senior DevOps Engineer（Lemon.io）。
- このIPの curl は CF 403。ギグ／サービス出品面は見ていない（求人ボードとして判定）。

### Remote OK — fail-aggregator

- https://remoteok.com/ : Remote Jobs、Post a Job、JSON/API フィード案内。
- `/remote-freelance-jobs` はトップと同じ机に戻る。別の freelance カタログは開かない。
- `og:updated_time` **2026-09-03T19:12:26+00:00**。個別カードの「○ hours ago」はこの HTML に無い。
- 「14,800,000+」はマーケ。使わない。

### Himalayas — fail-aggregator

- タイトル「Remote Job Board and Free AI Job Search Tools」。求職マッチ・履歴書 AI。Post a job。
- 「Sign up with Google」（求職。未クリック）。
- `/jobs` はこのIPで CF 403。トップの「Linear / Vercel」例はマーケ枠に見えるので、案件の新しさには使わない。

### ココナラテック — skip-agent

- https://tech.coconala.com/job-postings : 一覧。カードに **NEW**。例: 「【PMO】大手通信会社向けSalesforce導入プロジェクト」「【PdM】プロダクトライフサイクルマネジメント」。
- コピー「Web公開可能な『一部案件のみ』」。一覧の件数見出しはマーケ。使わない。
- 流れ: 会員登録 → **登録面談** → 専属エージェントが紹介 → 企業面談。`/signup` は 404。入口は `/#Registration`。
- 公開カードがあるので closed / thin にしない。面談代行はしない。

### Findy Freelance — skip-agent

- https://freelance.findy-code.io/ : 「ハイスキル向けフリーランスエンジニアエージェント」。案件例（週3~5日/フルリモート/TypeScript,Next.js 等）。
- 「Googleで登録し案件を探す」「GitHubで登録」。クリックしていない。
- 流れ: ヒアリング。**審査制**。案内可能と判断した人だけ面談・案件紹介。
- 脚注 ※1–3 の「2026年1月〜3月」はアンケート／集計期間。カード日付ではない。
- 公開案件例があるので closed / thin にしない。面談代行はしない。

### PRONI アイミツ — fail-thin

- https://imitsu.jp/ : 2023年9月1日よりアイミツから改名。発注者「一括見積もり」。カテゴリ（Web制作、AI、システム開発 等）。
- FAQ: 受注企業から **広告掲載料**。発注者は無料。
- 受注入口 https://partner.imitsu.jp/ タイトル「パートナー向け（受注企業）サイト」。本文は SPA で空。フォームは送っていない。
- 個人の出品カタログではない。

### 比較ビズ — fail-thin

- 公式は https://www.biz.ne.jp/ 。`hikaku-biz.com` は会計ソフト記事サイト（表示 2024-11-29）で **別物**。
- トップに見積依頼カード。`/subject/` に公開依頼例（HP制作、税理士、生成AIチャットボット、運送 等）。「ヒアリング済」ラベルあり。
- `/seller/` : 企業・専門家の掲載。資料請求フォーム（未送信）。発注者無料・受注者広告費のコピー。
- 記事日付の例 **2026年09月11日**。個人ギグカタログではない。

---

## 認証・停止（全机共通）

1. MAIN Google のみ。別アカウントを作らない。Google が無ければ MAIN Google のメール。
2. パスポート／免許／マイナンバー／顔写真／口座が出たら **アップロードせず停止**。
3. CV 送信・登録面談・掲載申込・資料請求はしない。
4. 有料会員・優先掲載・審査スキップは買わない。
5. プロフィール公開・出品公開・応募はしない。
6. 公開一覧が読めなければ `needs_check` のまま。数字を埋めない。

## オペレーター順（このゲートのあと）

1. **keep / pass:** なし
2. **SKIP closed:** Comet、Replit Bounties、Superpeer
3. **SKIP aggregator:** We Work Remotely、Remote OK、Himalayas
4. **SKIP agent:** ココナラテック、Findy Freelance
5. **SKIP thin:** PRONI アイミツ、比較ビズ

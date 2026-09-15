# SUMMARY — keep vs skip (Wave D late D11–D20)

観測: 2026-09-16 JST  
状態: **DRAFT_ONLY**。登録していない。公開していない。数字は作っていない。

親 QUEUE（PR#1）に D11–D20 行も D-late 行も無い。Wave C LATE（Zapier / Make / n8n / Toptal）は **この表に足さない**。

## keep（QUEUE 昇格・下書き検討）

**0 机。**

`pass` が無いので、Wave C 末尾 Med への昇格はしない。

## skip（QUEUE に戻さない）

| # | 机 | 判定 | なぜ切るか（見たものだけ） |
|---|---|---|---|
| D11 | Comet | `fail-closed` | `app.comet.co` 「espace personnel est clôturé」。旧 `/fr/freelance` は 404「Notre ancien site a fermé」。公開ミッションカードはプレースホルダ文。LP はコンサル案内 |
| D12 | Replit Bounties | `fail-closed` | `replit.com/bounties` が `contra.com/replit` へ 301。Bounties 机は閉じている。Contra は Wave A（ここでは登録しない） |
| D13 | Superpeer | `fail-closed` | `superpeer.com` が `skillshare.com` へ 301。Skillshare ヘルプ: スタンドアロン Superpeer を **2024-12-31** までに sunset |
| D14 | We Work Remotely | `fail-aggregator` | リモート求人ボード。「Post a job」。Jobs 面に「Latest post about 6 hours ago」。ギグ出品面は無い |
| D15 | Remote OK | `fail-aggregator` | リモート求人ボード。「Post a Job」。`/remote-freelance-jobs` はトップへ戻る。og:updated_time **2026-09-03**（ページ更新。カードの投稿時刻ではない） |
| D16 | Himalayas | `fail-aggregator` | トップが Remote Job Board。求職「Sign up with Google」。`/jobs` はこのIPで CF 403。売り手カタログは無い |
| D17 | ココナラテック | `skip-agent` | `/job-postings` に NEW カード。流れは会員登録 → **登録面談** → 専属エージェント紹介。代行しない |
| D18 | Findy Freelance | `skip-agent` | トップに案件例と「Googleで登録」。流れはヒアリング → **審査制** → 面談・案件紹介。代行しない |
| D19 | PRONI アイミツ | `fail-thin` | 発注者向け一括見積。受注は「貴社を掲載」「広告掲載料」。個人のスキル販売カタログではない |
| D20 | 比較ビズ | `fail-thin` | 公式 `https://www.biz.ne.jp/`。公開の見積依頼あり。受注は企業・専門家の **掲載／資料請求**。`hikaku-biz.com` は会計ブログで机が違う |

## needs_check

**0 机。**

読めなかった URL（WWR のこのIP 403、Himalayas `/jobs` 403、Skillshare トップ 403、アイミツ partner LP の SPA）は、別の公開ページで判定が付いた。推測で pass にしていない。

## この観測のあと

1. この10机は登録しない。
2. 閉じた机の後継（Contra / Skillshare 1-on-1）を **新規机として足さない**。ACTIVITY-GATE を通すのは本人 GO のあと。
3. 面接エージェント机は朝の本人以外は触らない（親 SKIP の Midworks / テクフリと同じクラス）。

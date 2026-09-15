# B10 — Anycrew

日付（JST）: 2026-09-16  
机: Anycrew（エニィクルー）  
This folder id: **B10** · QUEUE: **B5** · CU serial: **CU-15**  
公開ページを見たか: yes  
ログインしたか: no  
公開したか: no

## Schema

| Field | Value |
|---|---|
| **URL** | Talent app https://app.any-crew.com/ · marketing https://www.any-crew.com/ · offers (SPA) https://app.any-crew.com/offers · signup shell https://id.any-crew.com/signup · **do not use** https://biz.any-crew.com/ |
| **observed activity evidence** | **Job cards unread.** `/offers` is a 429-byte React shell (`<div id="root">` only). No offer titles, no posted dates. Company **news** lists media mentions through **2026-08-31**. **Blog** https://blog.any-crew.com/ 新着 **2026.08.26**. App HTML Last-Modified **Tue, 15 Sep 2026**. Alive ≠ dated catalog. Do not use news/blog as job-board freshness |
| **signup notes** | App HTML: 「会員登録 (無料)」「FacebookかGoogleのアカウントで利用登録」「Googleでログイン」. Facebook = do not create a new account. `id.any-crew.com/signup` is SPA-empty in this GET. Terms 第5条: 利用者は基本無料。求人事業者の有料プランは **employer** — talent % is not on that page. App FAQ: 「仕事を受けるフリーランス・副業人材の方には一切費用はかかりません。」 Talent % number: **not on this HTML → do not invent** |
| **CU tip** | **Do not open this desk this pass.** Gate is `needs_check`. If a human later sees one dated `/offers` card: talent app only; PREFER_GOOGLE; profile 検索結果 = **非公開**; no 応募. Agent-mediated jobs that require 職務経歴書 → stop. Employer console → close. KYC/ID → stop |
| **gate label** | `needs_check` |

## Checklist (PR#1 template)

1 生きている: yes（ブランド一致。閉鎖文なし）  
2 寄せ集めではない: yes（自前マッチング。外部求人ボードへ飛ばす一覧ではない）  
3 現地だけではない: unknown（コピーは「大半はフルリモート」。カード未読）  
4 本人専用ではない: yes  
5 活動の目視: unknown（案件カードなし。ニュース/ブログ日付は机の宣伝）  
6 KYC: 出ていない  
7 本線: yes（業務委託マッチング。人材側）

判定: **needs_check**（推測で `pass` にしない。`SKIP thin` にしない）  
QUEUE: Wave B のまま。昇格しない。  
Google: **PREFER_GOOGLE**（公開 HTML ラベル）  
有料: 人材「一切費用はかかりません」（FAQ）。事業者有料プランは触らない  
SKIP thin: no

## Do not

- GraphQL POST to `base.any-crew.com/graphql` (SPA needs CSRF)
- Complete Google / Facebook OAuth from this pack
- Copy CSRF tokens
- Treat 「案件が豊富」 copy as a count

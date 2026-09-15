# B11 — MENTA

日付（JST）: 2026-09-16  
机: MENTA  
This folder id: **B11** · QUEUE: **B6** · CU serial: **CU-16**  
公開ページを見たか: yes  
ログインしたか: no  
公開したか: no

## Schema

| Field | Value |
|---|---|
| **URL** | https://menta.work/ · catalog https://menta.work/plan · register https://menta.work/index.php/register/choose · mentor pitch https://menta.work/about_mentor · 特商法 https://menta.work/tokutei |
| **observed activity evidence** | Public plan catalog HTTP 200. Named cards, e.g. 「【未経験・初心者OK】Web制作 x AI 副業案件獲得コース（全24回）」 (`/index.php/plan/5485`). **NEW** labels on cards, e.g. 「【1ヶ月で完成！】未経験◎現役Webデザイナーと作るStudioWebサイト制作伴奏」. Filter UI includes 「最終ログイン30日以内」 and sort link 「新着」 (`/index.php/plan?order=2`) — **that sort URL was AWS WAF 202 in this GET; not used as proof**. No ISO `created_at` on the default listing. Catalog count on the page is **not** recorded here (not activity proof). Home marketing 「約7,400名」「8万人」 ignored |
| **signup notes** | Register choose 200: 「メールアドレスで登録する」「**Googleアカウントで登録する**」 plus X / Facebook / Apple / Lancers. Use **PREFER_GOOGLE** only. Do not complete OAuth from this pack. Mentor fee **cited**: 特商法 = 報酬の **20％（税別）**（利用15％＋決済5％）+ 振込都度 **300円**. Help 2022-08-31: **22%**（20%+消費税10%）+ 300円. Which figure the live form uses = click-time. Do not invent a third %. Stripe 本人確認 is for payout — **STOP** (help 3025561) |
| **CU tip** | After Wave A only. Google on `/register/choose`. Paste profile / 自己紹介. **Do not submit a plan** (出品). Do not open 本人確認 / Stripe / 口座. If WAF 202 on a filtered URL, park or use `/plan` with no query. Plan publish = not this GO |
| **gate label** | `pass` |

## Checklist (PR#1 template)

1 生きている: yes  
2 寄せ集めではない: yes  
3 現地だけではない: yes（オンラインメンター。チャット / ビデオ通話フィルタ）  
4 本人専用ではない: yes  
5 活動の目視: yes（公開プランカード + **NEW** = 新着カード。カレンダー日付は未読）  
6 KYC: 出ていない。出金の Stripe は STOP  
7 本線: yes（教える / 相談。デジタル）

判定: **pass**（下書き登録の検討可。公開・プラン提出はしない）  
QUEUE: Wave B。Wave A のあと  
Google: **PREFER_GOOGLE**  
有料: メンター手数料は特商法・ヘルプに数字あり（上）。有料プラン購入はしない  
SKIP thin: no

## Do not

- Follow `/oauth/google` to completion
- Use homepage contract-count marketing as activity proof
- Write a plan price into git

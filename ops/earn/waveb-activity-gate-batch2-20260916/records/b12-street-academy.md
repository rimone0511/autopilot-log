# B12 — ストアカ（Street Academy）

日付（JST）: 2026-09-16  
机: ストアカ  
This folder id: **B12** · QUEUE: **B7** · CU serial: **CU-17**  
公開ページを見たか: yes（www は UA 次第で WAF 405 → 再GETで 200）  
ログインしたか: no  
公開したか: no

## Schema

| Field | Value |
|---|---|
| **URL** | https://www.street-academy.com/ · teacher https://www.street-academy.com/teach · register https://www.street-academy.com/register · fee https://www.street-academy.com/fee · catalog https://www.street-academy.com/online/all · lecturer media https://teach.street-academy.com/ （登録フォームではない） |
| **observed activity evidence** | `/online/all` HTTP 200 (second UA). Class cards with session times on this listing, e.g. 「伝わる話し方が身に付くコミュニケーション練習会…」 session **9月18日(金) 10:00** オンライン; 「【60分で完成⏰】スキマ時間でパン作り…」 **9月16日(水) 10:00** オンライン; 「話し方1on1…」 **9月16日(水) 21:20** オンライン. Date-filter JSON includes `{"date":"2026-09-16"}` and later days. Sort links: 新着順 / 開催日順. Individual `/myclass/{id}` not opened (prior GET had WAF 405 on detail). Category totals on the nav are **not** activity proof. Lecturer media article date **2026.06.18** is extra alive-signal, not the catalog |
| **signup notes** | `/register` 200: **LINEで登録する** / **Facebookで登録する** / submit **メールアドレスで登録** (`user[email]` + password). Google on this page is Tag Manager / site-verification only → **NOT_OFFERED_OAUTH**. Use MAIN Google **mailbox** on the email path. Do not create LINE/Facebook for this desk. `/teach`: 「無料ではじめられる」「ストアカが集金を代行」. 「先生として活動いただくためには、本人確認書類の提出をお願いしています」→ **STOP** at that screen. Fee **cited** from `/fee` (not the Cloudflare-blocked help): 登録・掲載・月額 **0円**. 自己集客 **10%**. ストアカ送客 **30%**（対面 **20%**）. 2回目以降 **10%**. 別途消費税. Help https://support.street-academy.com/hc/ja/articles/200700579 was **403** here — `/fee` is the citation |
| **CU tip** | After Wave A only. If www is WAF 405, human browser or park. Email register with `{{EMAIL}}`. Password local only. LINE/Facebook only if email path is dead. Teacher profile (name / photo / public URL / bio) **draft**. **Do not create or submit a class.** ID-with-face → stop. Do not paste fee % unless `/fee` is re-opened at click time |
| **gate label** | `pass` |

## Checklist (PR#1 template)

1 生きている: yes（WAF は死滅ではない。200 の再GETでフォームと講座一覧）  
2 寄せ集めではない: yes  
3 現地だけではない: yes（オンライン講座カード。対面カテゴリは応募しない）  
4 本人専用ではない: yes  
5 活動の目視: yes（公開講座カード + 開催時刻。フィルタに 2026-09-16）  
6 KYC: 出ていない。顔写真付き証明書は STOP  
7 本線: yes（オンラインで教える）

判定: **pass**（講師プロフィール下書きの検討可。講座公開はしない）  
QUEUE: Wave B。Wave A のあと  
Google: **NOT_OFFERED_OAUTH** → MAIN Google メール  
有料: `/fee` に率あり（上）。初期費用 0円コピーあり。有料サポートは買わない  
SKIP thin: no

## Do not

- Commit `authenticity_token` from the register form
- Use 「209 万人」「37,014」 as activity proof
- Open a class for 掲載審査

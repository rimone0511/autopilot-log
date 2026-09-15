> **DRAFT_ONLY.** Evidence from this public GET only. No signup. No secrets.
> Unread course dates → **`needs_check`**. Do not guess `pass`.
> Help 403 does **not** by itself flip a readable catalog to `needs_check`.

# GATE — B12 ストアカ（Street Academy）

日付（JST）: **2026-09-16**  
机: ストアカ  
This folder id: **B12** · QUEUE: **B7** · CU serial: **CU-17**  
公開ページを見たか: **yes** (www **200** this GET; sibling GETs sometimes WAF 405)  
ログインしたか: **no**  
公開したか: **no**  
Forms: **not submitted**

## Schema

| Field | Value |
|---|---|
| **URL** | https://www.street-academy.com/ · teacher signup https://www.street-academy.com/teach · register https://www.street-academy.com/register · fee https://www.street-academy.com/fee · catalog https://www.street-academy.com/online/all · lecturer media https://teach.street-academy.com/ （登録フォームではない） |
| **observed activity evidence** | **Course dates read this GET → not `needs_check`.** `/online/all` HTTP 200. Class cards with session times, e.g. 「伝わる話し方が身に付くコミュニケーション練習会…」 **9月18日(金) 10:00** オンライン; 「【60分で完成⏰】スキマ時間でパン作り…」 **9月16日(水) 10:00**; 「話し方1on1…」 **9月16日(水) 21:20** オンライン. Date-filter JSON includes `{"date":"2026-09-16"}` and later days (also 2026-09-17…30, 2026-10-02…). Sort links: 新着順 / 開催日順. Home `/` also showed **9月16日** session labels. Category totals on the nav are **not** activity proof. Lecturer media PickUp **2026.06.18** is extra alive-signal, not the catalog |
| **signup notes (`/teach`)** | `/teach` 200 title「ストアカ講師/主催団体登録フォーム」。Copy: 「無料ではじめられる」「受講料の集金や入金確認はすべてストアカが代行します」. Flow on page: まずは先生としてアカウント登録 ※1 → 掲載審査・募集開始. 「※1 先生として活動いただくためには、本人確認書類の提出をお願いしています」→ **STOP** at that screen. 「※登録時に審査はありません」. Logged-in CTA: **LINEでログイン** / **Facebookでログイン** (`/auth/line`, `/auth/facebook` — **not followed**). Also: 「新規登録はこちら（無料）」; page HTML includes **メールアドレスで登録** and `user[email]`. **Google signup control: none** (GTM / site-verification only) → **NOT_OFFERED_OAUTH**. Use MAIN Google **mailbox** on the email path. Do not create LINE/Facebook for this desk |
| **signup notes (`/register`)** | `/register` 200「無料登録」. Visible: **LINEで登録する** / **Facebookで登録する** / email field `user[email]` + password + submit **メールアドレスで登録**. **not submitted.** Google button = GTM only |
| **WAF / 403 (this GET)** | **Top `/`:** 200, no AWS WAF body. **www `/help`:** 404 (not 403). **www `/top`:** 404. **www `/faq`:** 403 Cloudflare「Just a moment...」. **support.street-academy.com/hc/ja** and fee-help article **200700579:** 403 Cloudflare, help body unread. WAF on a later click ≠ dead |
| **gate label** | **`pass`** (catalog session dates readable). See rule below |

## Course-date unread → `needs_check`

| Catalog observation | Gate |
|---|---|
| Session / 開催日 **unread** (WAF, empty SPA, 403/405 on listing, or cards with no date) | **`needs_check`** — do **not** guess `pass`. Do not use marketing counts, help 403, or media-blog dates as a substitute |
| Session dates **read** on a public listing (this GET: `/online/all` **9月16日(水)** + JSON **2026-09-16**) | **`pass`** — draft-only later. No class publish |

[PR#12](https://github.com/rimone0511/autopilot-log/pull/12) first JP Wave B GET: `/teach` yes; top WAF; help 403; 講座 URL 405; **活動の目視 unknown** → **`needs_check`**. That is the unread-date rule applied. This folder does not rewrite PR#12.

Help / Cloudflare **403** with a **readable** catalog stays **`pass`**. Missing help text → fee cite from `/fee` only, or `needs_check` on the **help article**, not on the desk gate.

## Checklist (PR#1 template)

1 生きている: **yes**（WAF は死滅ではない。This GET: フォームと講座一覧 200）  
2 寄せ集めではない: **yes**  
3 現地だけではない: **yes**（オンライン講座カード。対面カテゴリは応募しない）  
4 本人専用ではない: **yes**  
5 活動の目視: **yes**（公開講座カード + 開催時刻。フィルタに 2026-09-16）  
6 KYC: 出ていない。顔写真付き証明書は STOP  
7 本線: **yes**（オンラインで教える）

判定: **`pass`**（講師プロフィール下書きは **後続 human GO の検討可**。講座公開はしない。**Early CU this folder = NO-GO / defer** — [CU-NOTE.md](CU-NOTE.md)）  
QUEUE: Wave B。**REGISTER-CU-CUT** — do not play from this pack  
Google: **NOT_OFFERED_OAUTH** → MAIN Google メール  
有料: `/fee` に率あり（[CU-NOTE.md](CU-NOTE.md)）。初期費用 0円コピーあり。有料サポートは買わない  
SKIP thin: **no**

## Do not

- Commit `authenticity_token` from `/teach` or `/register`
- Follow `/auth/line` or `/auth/facebook` from this pack
- Use 「209 万人」「37,014」 as activity proof
- Open 掲載審査 / create a class because the gate is `pass`
- Treat www `/help` 404 as the Zendesk help (help lives on `support.street-academy.com`, 403 here)

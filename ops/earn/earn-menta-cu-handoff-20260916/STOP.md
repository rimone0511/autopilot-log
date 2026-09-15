# STOP — MENTA (B11)

Mode: **DRAFT_ONLY**  
Pack: `ops/earn/earn-menta-cu-handoff-20260916/`  
Date: 2026-09-16

**This file is a stop list.** It does not tell anyone how to pass Stripe Identity, which ID to use, which bank to pick, how to 提出, or how to price a plan.

Three families of stop, all in-scope for this desk:

1. **Publish / 出品:** official help says **提出** sends the mentor plan to ops, then **一般に公開**. This pack does **not** 提出.
2. **Paid:** do not buy boosts, do not type a 金額, do not start a priced 月契約 (auto-renew), do not contract a plan as a mentee “to test.”
3. **KYC / money:** Stripe 本人確認, 口座, 出金. CU does **not** upload. Morning operator owns any later ID work.

CU does not complete KYC. CU does not 提出.

This is a **mentor listing**, not gig escrow. Do not “応募” as a workaround and do not paste a Coconala price to “just publish.”

---

## Allowed (non-publish, non-paid, non-KYC)

- [ ] MAIN Google signup or login (`Googleアカウントで登録する`), or the same MAIN email if Google is missing
- [ ] Email verification via **parent Gmail** (do not paste codes into git)
- [ ] Wait out an AWS WAF challenge once (`holdDurationMs` 1800 / 2500) then park if it still fails
- [ ] メンタープラン編集: タイトル / できること / 自己紹介 / 公開URL
- [ ] Optional **one** プラン行 with **empty 金額** (skip the row if 金額 is required)
- [ ] ステータス **表示しない** if the control is visible
- [ ] Optional face photo that is **not** an ID
- [ ] Save / 更新 **only if it is not 提出**

---

## Hard stop — do not open or complete

Publish / 出品:

- [ ] **提出** / 提出する / メンタープランを提出
- [ ] ステータス **相談できます**（契約が可能な状態）
- [ ] ステータス **今、忙しいです** as a way to “soft publish” (help: 表示はされる)
- [ ] 公開 / 出品中になる操作
- [ ] 運営への修正再提出

Paid:

- [ ] Any 金額 on a 月契約 or 単発 row
- [ ] Copying Coconala / Gumroad / Fiverr / ストアカ / help「平均契約価格帯1.4万円」into 金額
- [ ] Buying featured / boost / 有料プラン
- [ ] 運営と一緒に企画 inquiry
- [ ] Contracting someone else’s plan as a mentee to test
- [ ] Inventing a third 手数料％

Identity / payout:

- [ ] 設定 → **本人確認ページ** (Stripe)
- [ ] Government photo ID, selfie, liveness
- [ ] マイナンバー / 番号面
- [ ] 口座情報
- [ ] 出金申請 / 売上履歴からの振込
- [ ] Bank, PayPal, or any payout vendor

Wrong desk / WAF abuse:

- [ ] Lancers アカウントで登録する
- [ ] Workana (QUEUE B11) / Skill Shift (local B06) / ストアカ by mistake
- [ ] POST login through a WAF challenge page
- [ ] Saving WAF keys, cookies, or `gokuProps` into git

If a phone-SMS step appears: it is **not** an instruction to start ID. If **draft save** is impossible without SMS, only a number the **user** already placed in chat may be used, then stop. If the same step asks for ID, selfie, or a paid ID vendor, treat it as KYC and **stop**.

---

## Why we stop here (cite, not a procedure)

Publish:

- 「メンタープランが完成したらメンタープランを提出しましょう。新規メンターは運営チームが…確認します。確認後問題がなければ、一般に公開されます。」  
  https://intercom.help/mentajp/ja/articles/3025349
- 「確認後、問題がなければメンタープランが公開され、メンターとしての活動がはじまります。」提出ボタンは編集ページ最下部。提出は必須・**費用はかからない** — 無料提出 ≠ このパックの GO。  
  https://intercom.help/mentajp/ja/articles/5252569
- ステータス「相談できます」= 表示され **契約が可能**。「表示しない」= 表示されず契約不可。  
  https://intercom.help/mentajp/ja/articles/3751409
- Help は公開プランを **出品中** と呼ぶ。  
  https://intercom.help/mentajp/ja/articles/3025564

Paid / fees (cite only; do not type into the form):

- 手数料22％（20％+消費税10％）+ 出金都度 300円（help 2022-08-31）  
  https://intercom.help/mentajp/ja/articles/3025582
- 特商法 20％税別（利用15％+決済5％）+ 振込都度 300円 — sibling GET on https://menta.work/tokutei ; **this GET WAF unread**. Re-read in a browser before any later priced GO (not this pass). Do **not** invent a third ％.

KYC / money:

- 「メンターへのお支払いには本人確認が必要」「Stripe を利用」  
  https://intercom.help/mentajp/ja/articles/3025561
- 出金: 売上 1,000円超かつ入金日より30日。**事前に本人確認・口座情報の登録が必要**。都度 300円。  
  https://intercom.help/mentajp/ja/articles/3025575

Do not follow those articles’ fill steps in this pack. Do not quote their field lists into a CU prompt as “next clicks.”

---

## If 提出 is pressed by mistake

1. Do **not** set 相談できます. Do not message mentees. Do not start Stripe “to finish listing.”
2. Record only: date, desk `MENTA`, `submit_stop`. No session-token URLs.
3. Leave whatever unpublished draft already existed.
4. Morning user decides whether to ask ops to keep it unpublished. This pack has **no** withdraw how-to.

`submit_stop` is a valid desk outcome. It is not “keep going.”

## If a KYC screen appears

1. Close the dialog. Do not choose a file. Do not continue into Stripe.
2. Leave whatever unpublished draft already saved.
3. Record only: date, desk `MENTA`, screen type (`stripe_identity` / `bank` / `photo_id` / `selfie` / other). No document data.
4. Set outcome `kyc_wait`. Morning user decides.
5. Do not 提出 as a workaround. Do not buy anything to skip identity.

`kyc_wait` is a valid desk outcome. It is not failure.

Do not store screenshots that show ID, face, full account email, OTP, bank digits, or WAF challenge internals.

## If WAF never clears

1. Park. Outcome `waf_challenge` or `hold_failed`.
2. Do not create a new mailbox. Do not script retries.
3. Morning user retries in a normal browser.

## Morning memo (no secrets)

```
date:
desk: MENTA
ids: B11 / QUEUE-B6 / CU-16
screen:
saved_draft: yes/no/unknown
draft_plan: none | unpublished | skipped
submit: no | accidental
publish: no
kyc_shown: yes/no
upload: none
paid_plan: no
bank: no
waf: passed | parked | unseen
next: morning-user | park | next-desk
```

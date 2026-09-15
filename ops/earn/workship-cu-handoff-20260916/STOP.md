# STOP — Workship (B02)

Mode: **DRAFT_ONLY**  
Pack: `ops/earn/workship-cu-handoff-20260916/`  
Date: 2026-09-16

**This file is a stop list.** It does not tell anyone how to pass identity checks, which ID to use, which bank to pick, or how to エントリー.

Two families of stop, both in-scope for this desk:

1. **Apply:** official help says **「気になる！」= エントリー完了** and opens a メッセージルーム. This pack does **not** apply.
2. **KYC / money:** 契約署名, 前払い本人確認, 振込先口座, マイナンバー. CU does **not** upload. Morning operator owns any later ID work.

CU does not complete KYC. CU does not press 気になる.

---

## Allowed (non-apply, non-KYC)

- [ ] MAIN Google signup or login (`SNSで登録` / `SNSでログイン` Google icon), or the same MAIN email if Google is missing
- [ ] Email verification via **parent Gmail** (do not paste codes into git)
- [ ] プロフィールを編集: 自己紹介 / やってみたいこと / 職歴 / スキル / 公開URL
- [ ] Save with **更新する** / **追加する**
- [ ] 公開範囲 → 鍵 / 非公開 if the control is visible
- [ ] Optional face photo that is **not** an ID

---

## Hard stop — do not open or complete

Apply / message (official flow STEP3+):

- [ ] **気になる！** (help: 押すとエントリー完了)
- [ ] **エントリー**
- [ ] スカウトに返信する / メッセージルームで営業
- [ ] 成約報告
- [ ] エージェント「提案希望」

Identity / payout:

- [ ] 契約管理 → **署名をする** (機密保持契約 / 準委任契約 / 個別契約)
- [ ] Government photo ID, 印鑑証明, selfie, liveness
- [ ] 前払いオプション / 「本人確認手続き」
- [ ] マイナンバー / 番号面
- [ ] 振込先口座 (報酬 / お祝い金)
- [ ] 帳票ドキュメントの振込先（別設定でも今は開けない）
- [ ] Bank, PayPal, or any payout vendor

Wrong desk / paid:

- [ ] ENTERPRISE / 採用担当者ログイン
- [ ] Workshift (`workshift-sol.com`)
- [ ] Paid boosters / 優先掲載 bought to skip identity
- [ ] Inventing prepaid 手数料％ to “just pay it”

If a phone-SMS step appears: it is **not** an instruction to start ID. If **draft save** is impossible without SMS, only a number the **user** already placed in chat may be used, then stop. If the same step asks for ID, selfie, or a paid ID vendor, treat it as KYC and **stop**.

---

## Why we stop here (cite, not a procedure)

Apply:

- 「各募集にある『気になる！』ボタンを押すと、エントリー完了です。エントリーすると、企業とのメッセージルームが自動的に作成されます。」  
  https://goworkship.com/help/how_to/72
- エントリー後のメッセージ / 面談: https://goworkship.com/help/how_to/77
- Official flow STEP3 = 募集にエントリーする: https://goworkship.com/flow

KYC / money:

- 新規登録 help: ログイン後「契約管理」→ 契約書はドラフト → **署名をする**  
  https://goworkship.com/help/how_to/44
- 三者間 機密保持契約 / 準委任契約 / 個別契約:  
  https://goworkship.com/help/agreement/105
- 「前払いオプションを利用するには、本人確認が必要です」  
  https://goworkship.com/help/agreement/95  
  手数料は「手数料・利用規約を確認の上」。**％はコピーしない。申請しない。**
- 振込先口座 / 初月お祝い金:  
  https://goworkship.com/help/agreement/118  
  https://goworkship.com/help/agreement/100
- 対象: 日本国内の住民票 + 本人名義の国内口座（資格の引用。**口座フォームは今は開かない**）  
  https://goworkship.com/help/about_workship/71

Do not follow those articles’ fill steps in this pack. Do not quote their field lists into a CU prompt as “next clicks.”

---

## If 気になる / エントリー is pressed by mistake

1. Do **not** send a first message. Do not 成約報告.
2. Record only: date, desk `Workship`, `apply_stop`, listing title if visible **without** pasting a tracking URL that includes a session token.
3. Leave profile draft as-is.
4. Morning user decides whether to withdraw / ignore. This pack has no withdraw how-to.

`apply_stop` is a valid desk outcome. It is not “keep going.”

## If a KYC screen appears

1. Close the dialog. Do not choose a file. Do not continue into the vendor.
2. Leave whatever unpublished draft already saved.
3. Record only: date, desk `Workship`, screen type (`contract_sign` / `prepaid_id` / `bank` / `my_number` / `photo_id` / `selfie` / other). No document data.
4. Set outcome `kyc_wait`. Morning user decides.
5. Do not 気になる as a workaround. Do not buy anything to skip identity.

`kyc_wait` is a valid desk outcome. It is not failure.

Do not store screenshots that show ID, face, full account email, OTP, or bank digits.

## Morning memo (no secrets)

```
date:
desk: Workship
screen:
saved_draft: yes/no/unknown
kininaru: no | accidental
entry: no | accidental
kyc_shown: yes/no
upload: none
prepaid: no
bank: no
next: morning-user | park | next-desk
```

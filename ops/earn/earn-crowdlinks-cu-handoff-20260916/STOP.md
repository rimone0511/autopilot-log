# STOP — CrowdLinks / クラウドリンクス (B04)

Mode: **DRAFT_ONLY**  
Pack: `ops/earn/earn-crowdlinks-cu-handoff-20260916/`  
Date: 2026-09-16

**This file is a stop list.** It does not tell anyone how to pass identity checks, which ID to use, which bank to pick, how to pass SMS, or how to 応募.

Three families of stop, all in-scope for this desk:

1. **Apply:** 応募フォームへ / 話を聞きたい / スカウト返信 / マッチング報告. This pack does **not** apply.
2. **KYC / money / paid:** 追加書類, 有料会員審査, 身分証, 口座, マイナンバー. CU does **not** upload. Morning operator owns any later ID work.
3. **Phone:** アカウント設定の電話番号 is documented. It is **not** an instruction to start SMS. If draft save is impossible without SMS, only a number the **user** already placed in chat may be used, then stop. If the same step asks for ID, selfie, or a paid ID vendor, treat it as KYC and **stop**.

CU does not complete KYC. CU does not 応募. CU does not start phone verification to “be thorough.”

---

## Allowed (non-apply, non-KYC)

- [ ] MAIN Google signup or login (`Googleで登録する` / `Googleでログイン`), or the same MAIN email if Google is missing
- [ ] Email verification via **parent Gmail** (do not paste codes into git)
- [ ] プロフィール: キャリアの概要 / 課題解決できること / 経歴・実績 1件 / スキルタグ / 公開URL
- [ ] Save with live **保存する**
- [ ] 公開範囲 → **クラウドリンクス内で公開** (not 一般公開)
- [ ] Optional 企業ブロック (names off git)
- [ ] Optional face photo that is **not** an ID

---

## Hard stop — do not open or complete

Apply / message:

- [ ] **応募フォームへ**
- [ ] **話を聞きたい**
- [ ] スカウトに返信する / メッセージで営業
- [ ] マッチング報告 / 「報告する」
- [ ] 案件応募ガイドラインに沿った応募そのもの

Identity / payout / paid:

- [ ] 有料会員化 / 有料プラン申込
- [ ] TOS 第3条4 / 第4条の **追加の書類等の提出**
- [ ] Government photo ID, マイナンバー, selfie, liveness
- [ ] 口座 / 振込先 / PayPal / その他の支払いベンダー
- [ ] 企業との直接契約で身分証を求められたとき（FAQ: 契約は企業と直接 — still STOP）
- [ ] Inventing 手数料％ or 有料会員の円 to “just pay it”

Phone:

- [ ] アカウント設定 → 連絡先の電話番号（下書き保存が止まらないなら触らない）
- [ ] SMS / 認証コード入力（user-chat wait only if draft save is blocked **and** no ID screen）
- [ ] Phone as a stand-in for KYC

Wrong desk / visibility:

- [ ] `/client/` 契約企業
- [ ] CrowdWorks.jp
- [ ] Facebook 新規
- [ ] プロフィール **一般公開**
- [ ] Second CrowdLinks account

If a phone-SMS step appears: it is **not** an instruction to start ID. If **draft save** is impossible without SMS, only a number the **user** already placed in chat may be used, then stop. If the same step asks for ID, selfie, or a paid ID vendor, treat it as KYC and **stop**.

---

## Why we stop here (cite, not a procedure)

Apply:

- 「プロフィールにご経歴やスキルを記載した上で、応募したいプロジェクトのページの右下にある『応募フォームへ』より応募ができます。」  
  https://help.crowdlinks.jp/0029649d31534622a6d95ffe53df18dd
- Older FAQ slug still says 「話を聞きたい」:  
  https://help.crowdlinks.jp/faq-worker
- 案件応募ガイドライン（応募時の TOS 再掲。**応募手順としては使わない**）:  
  https://help.crowdlinks.jp/entry_guidelines
- スカウト = 企業からのメッセージ。FAQ は返信を勧める。このパックでは返信しない。

KYC / money / paid:

- 無料会員でも「審査において必要な場合、追加の書類等の提出を求めることができる」  
  https://crowdlinks.jp/terms 第3条4
- 有料会員は申込・審査・追加書類・利用料。**金額はこのGETの TOS / FAQ に無い → 作らない・買わない**  
  https://crowdlinks.jp/terms 第4条
- 「マッチングした企業様とユーザーが直接契約」「掲載報酬額から手数料は引かれない」  
  https://help.crowdlinks.jp/0029649d31534622a6d95ffe53df18dd  
  Direct contract **is not** permission to upload ID from this pack.

Phone:

- 電話番号はアカウント設定の「連絡先」から変更できる、とだけ書いてある。登録必須とは書いていない。  
  https://help.crowdlinks.jp/change-mail-tel

Real-name / 副業 (stop if the human has not cleared this):

- 本名必須ではないが推奨  
  https://help.crowdlinks.jp/0029649d31534622a6d95ffe53df18dd
- 「自己の所属する組織体の規則に反した行為をしていないこと」  
  TOS 第3条2(9) · 応募ガイドライン同文
- 公開範囲 3種 + 企業ブロック  
  FAQ · https://help.crowdlinks.jp/corporate_block

Do not follow those articles’ fill steps in this pack. Do not quote their field lists into a CU prompt as “next clicks.”

---

## If 応募 / 話を聞きたい is pressed by mistake

1. Do **not** send a first message. Do not マッチング報告.
2. Record only: date, desk `CrowdLinks`, `apply_stop`, listing title if visible **without** pasting a tracking URL that includes a session token.
3. Leave profile draft as-is.
4. Morning user decides whether to withdraw / ignore. This pack has no withdraw how-to.

`apply_stop` is a valid desk outcome. It is not “keep going.”

## If a KYC screen appears

1. Close the dialog. Do not choose a file. Do not continue into the vendor.
2. Leave whatever unpublished draft already saved.
3. Record only: date, desk `CrowdLinks`, screen type (`extra_docs` / `paid_review` / `bank` / `my_number` / `photo_id` / `selfie` / `phone_kyc` / other). No document data.
4. Set outcome `kyc_wait`. Morning user decides.
5. Do not 応募 as a workaround. Do not buy 有料会員 to skip identity.

`kyc_wait` is a valid desk outcome. It is not failure.

## If a phone / SMS screen appears

1. If profile **draft save already works**, close. Do not add a number.
2. If save is blocked: wait for a number the user already placed in chat. Enter once. Do not store it in git / STATUS.
3. If the screen asks for photo ID, liveness, or a paid vendor: **KYC STOP** (`phone_kyc`).
4. Outcome `sms_wait_user` or `kyc_wait`. Not “retry until it works.”

Do not store screenshots that show ID, face, full account email, OTP, phone, or bank digits.

## Morning memo (no secrets)

```
date:
desk: CrowdLinks
screen:
saved_draft: yes/no/unknown
entry: no | accidental
hanashi: no | accidental
kyc_shown: yes/no
phone_sms: no | sms_wait_user | phone_kyc
upload: none
paid: no
bank: no
visibility: crowdlinks-internal | unknown
next: morning-user | park | next-desk
```

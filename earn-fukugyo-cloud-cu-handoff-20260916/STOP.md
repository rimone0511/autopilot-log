# STOP — 複業クラウド (B03) KYC / phone / SMS / apply

Mode: **DRAFT_ONLY**  
Pack: `earn-fukugyo-cloud-cu-handoff-20260916/`  
Date: 2026-09-16

**This file is a stop list.** It does not tell anyone how to pass identity checks, which ID to use, which bank to pick, or how to エントリー.

Three families of stop, all in-scope for this desk:

1. **Apply:** TOS 第2.1条3 is 応募. Public JS has **キニナル / キニナル済**. This pack does **not** apply and does **not** キニナル.
2. **KYC / money:** 身分証, 自撮り, 口座, マイナンバー. Public TOS + company privacy GET had **no** those strings. If the **live** wizard shows them — close. CU does **not** upload. Morning operator owns any later ID work.
3. **Phone / SMS:** not observed on public signup JS as a required field. If it appears, it is **not** an instruction to start ID. Draft-save block only → user-chat number → stop. ID on the same step → KYC STOP.

CU does not complete KYC. CU does not press エントリー. CU does not press キニナル.

---

## Allowed (non-apply, non-KYC)

- [ ] MAIN Google signup or login (`外部サービスでサインイン` → `Googleでサインイン`), or the same MAIN email if Google is missing
- [ ] Email verification via **parent Gmail** (do not paste codes into git)
- [ ] Talent プロフィール: 自己紹介 / 職種 / スキル / 公開URL / optional face photo that is **not** an ID
- [ ] Save **下書き** / live save control
- [ ] 公開トグル → 非公開 if the control is visible
- [ ] Optional 非表示企業 from ledger (names stay off git)

---

## Hard stop — do not open or complete

Apply / message (TOS 第2.1条3–5):

- [ ] **エントリー** / **応募する** / この求人に応募
- [ ] **キニナル** / **キニナル済** (public JS like-control. App Store: compare. 2022 article: easy entry. **Either way, do not press**)
- [ ] スカウトに返信する / オファーに返信 / メッセージで営業
- [ ] **ソリューション** を投稿する / 公開する
- [ ] 複業転職スカウトを「今すぐ転職」に振り切る

Identity / payout (stop-at-KYC notes only — **no how-to**):

- [ ] 本人確認 / eKYC / 本人確認書類のアップロード
- [ ] Government photo ID, 印鑑証明, selfie, liveness
- [ ] マイナンバー / 番号面
- [ ] 振込先口座 / PayPal / その他の出金
- [ ] カードを「確認のため」入れる
- [ ] 源泉・税務番号の代理入力

Phone / SMS checklist:

- [ ] Phone number on signup **when draft save still works without it** → skip
- [ ] Phone / SMS **only if draft save is blocked** → number the **user** already placed in chat → then **stop**. Outcome `sms_wait_user`
- [ ] Do not guess a number. Do not pull a number from git. Do not type OTP digits into git / STATUS
- [ ] If the phone step shows ID, selfie, liveness, or 「本人確認へ」→ treat as **KYC** and **stop** (`kyc_wait`). Do not use SMS as a workaround for identity
- [ ] Account-recovery SMS is not this pass

Wrong desk / paid:

- [ ] `cl.aw-anotherworks.com` 無料デモ / 人材データベース / サービス資料
- [ ] 事業者プラン / TOS 第3.2条 利用料金
- [ ] Inventing a worker 手数料％ to “just pay it”

Captcha (see PLAYBOOK skip rules):

- [ ] Image / tile puzzle — do not click tiles → `blocked_skip`
- [ ] Press-hold / checkbox that fails after `holdDurationMs` 1800 + retry 2500 → `blocked_skip`
- [ ] Captcha bypass / lockout retries

---

## Why we stop here (cite, not a procedure)

Apply:

- TOS 第2.1条3: 登録タレントは求人に**応募すること等**により登録事業者を探索できる.  
  https://cl.aw-anotherworks.com/user_tos
- TOS 第2.1条4: メッセージは応募に必要な範囲. **迷惑となる営業行為**は禁止（利用停止・登録取消しあり）.
- TOS 第3.1条2: 登録事業者はタレントの**エントリー**を受け付ける — worker clicking エントリー is matching, not this pack.
- Public JS: `text:u?"キニナル済":"キニナル"` (like-pink control). Do not press.

KYC / money / phone — **observed absence, live still wins**:

- TOS GET (this session): **0** hits for 本人確認 / マイナンバー / SMS / 口座.
- Company privacy https://anotherworks.co.jp/user_privacy GET 200: **0** hits for 本人確認 / マイナンバー / 電話番号 / SMS / 口座. (The word Google in that HTML was a webfont name, not SSO.)
- `cl.aw-anotherworks.com/user_privacy` **404** this GET — do not invent a KYC article there.
- Signup/login public chunks: メール / パスワード / Google·Facebook·Apple. **No** 電話番号 / SMS / 本人確認 strings in the signup-specific chunk `2ft1bogak3uo6.js`.
- Shared Firebase chunk includes `RECAPTCHA_NOT_ENABLED` error codes — that is **SDK text**, not proof the live `/sign_up` paints captcha. If captcha **does** paint: PLAYBOOK skip rules.

Do not follow a later KYC wizard’s fill steps in this pack. Do not quote field lists into a CU prompt as “next clicks.” Note **screen type only**.

---

## If エントリー / キニナル is pressed by mistake

1. Do **not** send a first message. Do not 成約. Do not add ソリューション.
2. Record only: date, desk `複業クラウド`, `apply_stop`, listing title if visible **without** pasting a tracking URL that includes a session token.
3. Leave profile draft as-is.
4. Morning user decides whether to withdraw / ignore. This pack has no withdraw how-to.

`apply_stop` is a valid desk outcome. It is not “keep going.”

## If a KYC screen appears

1. Close the dialog. Do not choose a file. Do not continue into the vendor. Do not enable the camera for identity.
2. Leave whatever unpublished draft already saved.
3. Record only: date, desk `複業クラウド`, screen type (`photo_id` / `selfie` / `liveness` / `bank` / `my_number` / `ekyc` / other). No document data.
4. Set outcome `kyc_wait`. Morning user decides.
5. Do not エントリー as a workaround. Do not buy a company plan to skip identity.

`kyc_wait` is a valid desk outcome. It is not failure.

Do not store screenshots that show ID, face, full account email, OTP, or bank digits.

## If phone / SMS appears

| Situation | Action |
|---|---|
| Optional; draft saves without it | Skip |
| Required for **draft save** | User-chat number only. `sms_wait_user`. Stop after the code lands in the user’s device. Do not log the code |
| User away | Park. Do not invent a number |
| Same step asks for ID / selfie | **KYC STOP**. `kyc_wait` |

## Morning memo (no secrets)

```
date:
desk: 複業クラウド
screen:
saved_draft: yes/no/unknown
entry: no | accidental
kininaru: no | accidental
kyc_shown: yes/no
kyc_type:
phone_sms: skipped | sms_wait_user | skipped_optional
upload: none
bank: no
skip: none | blocked_skip
next: morning-user | park | next-desk
```

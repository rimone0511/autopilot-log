# STOP before KYC — TimeTicket host + Contra Independent

Mode: **DRAFT_ONLY**  
Pack date: 2026-09-16

本人確認・Persona・口座は **販売・出金・Discover 完成** のゲートとして公式が書く。このパックは出金も発行完了もしない。だから書類を上げる理由は無い。

ライブフォームが **下書きプロフィールを保存できない** と身分証を要求したら **stop**。机名と画面種類だけ朝の本人へ。アップロードしない。

CU は KYC を完了しない。朝の本人は兄弟 `earn-kyc-morning-checklist-20260916/`（あれば）。

---

## Allowed for this pack

- [ ] MAIN Google signup / login、または TimeTicket で Google が無いときの **同じ MAIN Gmail** メール登録
- [ ] Email verification via **parent Gmail MCP**（コードを git に貼らない）
- [ ] SMS only if draft save is blocked, and only with a number the **user** placed in chat
- [ ] TimeTicket **ホスト** プロフィール下書き。非公開トグルがあればオフ（規約第8条: 未設定だと公開）
- [ ] TimeTicket **通常チケット** を **メッセージ** だけで下書き保存できるときだけ。発行完了はしない
- [ ] Contra **Share work / Independent**、**Free**、one-liner、400 字以内の About、公開 URL
- [ ] Contra Discoverable **off**（トグルがあれば）

---

## Hard stop — do NOT

Identity and tax (KYC):

- [ ] TimeTicket [identifications/edit](https://www.timeticket.jp/users/identifications/edit)
- [ ] Upload government photo ID（免許・パスポート・在留・特別永住者証明書等）
- [ ] マイナンバーカード **裏面（個人番号）** / 通知カード / 住民票のマイナ記載
- [ ] Type a national ID number, My Number, tax ID, W-8, SSN, EIN
- [ ] Selfie / liveness for ID matching
- [ ] Contra Wallet → **Add account** / **Add an account**
- [ ] Persona redirect（政府ID・顔・支払い口座）
- [ ] Stripe Identity / Airwallex で別国口座
- [ ] Expert verification that demands government ID
- [ ] Send ID photos to Support

Payments and paid plans:

- [ ] TimeTicket [payouts/new](https://www.timeticket.jp/payouts/new) / 振込口座
- [ ] Contra bank / PayPal / crypto payout
- [ ] **Buy Contra Pro / Max**（Discover や手数料のためでも不可）
- [ ] Add a credit card “to verify you”

Publish and commerce:

- [ ] TimeTicket「発行して予約可能日時の登録へ」「チケット発行手続きを完了する」
- [ ] 電話相談チケットの発行
- [ ] 予約可能日時の公開カレンダー埋め
- [ ] Contra feed への Work **Publish**
- [ ] Contra opportunity apply / invoice / payment link（応募文は兄弟 EN pack。ここでは送らない）
- [ ] プロフィールを「公開する」トグルが明示的にあるときの公開

Phone:

- [ ] Phone SMS for **account recovery** is not the same as ID upload. If onboarding blocks even a **draft** without SMS, the user may complete SMS on a device they control, then stop. If the phone step asks for ID, selfie, or a paid ID vendor, treat it as KYC and **stop**.

---

## Official stop text (do not treat as a GO)

### TimeTicket

- 本人確認資料の提出: 提出画面は `https://www.timeticket.jp/users/identifications/edit`。  
  https://help.timeticket.jp/articles/19398  
  免許は **表面**（国際免許不可）。パスポートは日本国の顔写真ページ。マイナは **裏面提出お控え**。住民票はマイナ記載なし・本籍等は隠す。
- 提出画面 = **STOP**。販売に確認が要ると画面が言っても **回避せず停止**。朝の本人が上げる。エージェントはファイルを選ばない。
- 出金は口座登録が先（ヘルプ 19376）。出金しないので口座もやらない。

### Contra

- Onboarding Independent: Discoverable 完成の最後が **Verify identity & set up your wallet**。  
  https://help.contra.com/en/articles/9322381-onboarding-and-completing-your-profile  
  このパックは Discover 完成チェックを埋めない。wallet の手前で止める。
- How to Verify Your Identity（2026-03-27）: Wallet → Add account → **発行国**（居住国ではない）→ Persona。  
  https://help.contra.com/en/articles/9322955-how-to-verify-your-identity-on-contra
- Your Contra Wallet（2026-03-13）: “Add an account” → 発行国 → パートナーサイトで ID。  
  https://help.contra.com/en/articles/9322950-your-contra-wallet
- Persona / Add account = **STOP**。Pro を買って Discover を先に進める代替もしない。

---

## If KYC appears

1. Close the upload dialog. Do not choose a file.
2. Leave the profile in whatever unpublished state already saved.
3. Record only: date, desk, screen type (`photo_id` / `my_number_reverse` / `selfie` / `address` / `bank` / `persona` / `wallet_add_account` / other).
4. Morning operator decides. This pack is complete as unpublished paste.
5. Continue to the **next** desk only if KYC is not a hard lock on the whole browser session.

Do not store screenshots that show ID, face, or full account email in the repo.

`kyc_wait` is a valid desk outcome. It is not failure.

## 朝メモの型（秘密なし）

```
date:
desk: TimeTicket | Contra
screen:
saved_draft: yes/no/unknown
kyc_shown: yes/no
upload: none
pro_upgrade: no
ticket_issued: no
next: morning-user | park | next-desk
```

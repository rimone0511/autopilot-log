# STOP before KYC — Skill Shift / SOKUDAN / MENTA / Anycrew / ストアカ

Mode: **DRAFT_ONLY**  
Pack date: 2026-09-16

本人確認・Stripe・口座・eKYC は **出金や出品のゲート** として公式が書く机がある。このパックは出金も公開もしない。だから書類を上げる理由は無い。

ライブフォームが **下書きプロフィールを保存できない** と身分証を要求したら **stop**。机名と画面種類だけ朝の本人へ。アップロードしない。

CU は KYC を完了しない。朝の本人は兄弟 `earn-kyc-morning-checklist-20260916/`（あれば）。

---

## Allowed for this pack

- [ ] MAIN Google signup / login、または Google OAuth が無い机での **同じ MAIN Gmail** メール登録
- [ ] Email verification / 仮登録マジックリンク via **parent Gmail MCP**（コードを git に貼らない）
- [ ] SMS only if draft save is blocked, and only with a number the **user** placed in chat
- [ ] 個人 / 人材 / メンター / 先生（企業・発注者コンソールは閉じる）
- [ ] Profile fields from the desk cards, saved as draft / 非公開 if a control exists
- [ ] MENTA: プロフィール保存まで。プランは作っても **公開しない**（作らない方がよい）
- [ ] ストアカ: 生徒〜先生プロフィール（名前・顔写真・公開 URL・自己紹介）。講座公開しない

---

## Hard stop — do NOT

Identity and tax (KYC):

- [ ] 本人確認申請 / 本人確認ページ / オンライン本人確認 / eKYC / Stripe Identity
- [ ] Upload government photo ID（免許・パスポート・在留・住民基本台帳カード等）
- [ ] マイナンバーカード（表面・チップ・JPKI）または通知カード
- [ ] Type a national ID number, My Number, tax ID, インボイス登録番号
- [ ] Selfie / liveness for ID matching
- [ ] 住民票・住所証明のアップロード
- [ ] Skill Shift 規約の「本人確認サービス」に乗る資料提出
- [ ] SOKUDAN 規約第4条の「審査に必要な書類」
- [ ] ストアカの顔写真付き公的証明書 + 顔撮影
- [ ] Send ID photos to Support

Payments and paid plans:

- [ ] 口座 / 振込先 / bank / PayPay / 出金申請
- [ ] Buy featured listings or paid membership
- [ ] Add a credit card “to verify you”

Publish and commerce:

- [ ] 案件への応募 / 提案送信 / スカウト承諾で契約
- [ ] MENTA プラン公開（出品）
- [ ] ストアカ講座の公開申請
- [ ] プロフィールを「公開する」トグルが明示的にあるときの公開

Phone:

- [ ] Phone SMS for **account recovery** is not the same as ID upload. If onboarding blocks even a **draft** without SMS, the user may complete SMS on a device they control, then stop. If the phone step asks for ID, selfie, or a paid ID vendor, treat it as KYC and **stop**.

---

## Official stop text (do not treat as a GO)

### Skill Shift

- 利用規約 第7条6: 会員が「本人確認サービス」の提供を受ける場合、虚偽・偽造等の資料を提出しない。  
  https://www.skill-shift.com/terms-of-service  
  **資料提出画面 = STOP。** このパックは本人確認サービスを申し込まない。
- 同 第3条1: 個人会員登録は **本人が行う**。代理登録しない（CU は人が目の前にいる直列に限る。この authoring エージェントは登録しない）。
- 個人情報の開示請求に伴う本人確認書類（プライバシー文面）も上げない。

### SOKUDAN

- 利用規約 第4条: 会員登録申請の審査に **必要な書類の提出を求めることがあり**、提出しない場合は登録を拒否できる。  
  https://sokudan.work/pages/terms  
  書類提出 UI = STOP。拒否されても ID を上げて通さない。
- 第14条 期中審査: 必要書類の提供を求めることがある。同じく STOP。

### Anycrew

- 公開 FAQ（人材アプリ）: 通常は Web プロフィールのみ。エージェント仲介の一部案件は応募時に面談・職務経歴書。  
  https://app.any-crew.com/  
  職務経歴書が **必須** と出たら後回し（任意ならスキップ）。身分証が乗ったら KYC STOP。
- 規約第3条: 登録には外部 SNS。身分証アップロード条は公開規約に見当たらない → 画面が出たら STOP（`needs_check` ではなく、出た瞬間に止める）。

### MENTA

- 公式ヘルプ「本人確認をする」（2021-03-18）: メンターへの支払いには本人確認。設定 → **本人確認ページ**。Stripe 利用。  
  https://intercom.help/mentajp/ja/articles/3025561  
- メンター案内: 出金は売上 1,000円超かつ入金から 30日、**事前に本人確認・口座情報**。  
  https://menta.work/about_mentor  
  出金しないので両方やらない。

### ストアカ

- 公式ヘルプ「会員登録の方法（パソコンサイト）」: 講座ページ作成の前にプロフィール、**本人確認の提出**、先生ページ。マンツーマン前提の個人先生は確認書類が必要。  
  https://support.street-academy.com/hc/ja/articles/360011723660
- 公式ヘルプ「オンライン本人確認について」: 免許・パスポート・マイナンバーカード等 + **本人の顔写真撮影**（eKYC）。  
  https://support.street-academy.com/hc/ja/articles/4409755419673  
  提出画面 = STOP。Blue バッジ取得後必須、と書いてあってもこのパックではやらない。

---

## If KYC appears

1. Close the upload dialog. Do not choose a file.
2. Leave the profile in whatever unpublished state already saved.
3. Record only: date, desk, screen type (`photo_id` / `my_number` / `selfie` / `address` / `bank` / `stripe_identity` / `ekyc` / `review_docs` / other).
4. Morning operator decides. This pack is complete as unpublished paste.
5. Continue to the **next** desk only if KYC is not a hard lock on the whole browser session.

Do not store screenshots that show ID, face, or full account email in the repo.

`kyc_wait` is a valid desk outcome. It is not failure.

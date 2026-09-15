# STOP before KYC — 複業クラウド / Anycrew / ストアカ

Mode: **DRAFT_ONLY**  
Pack date: 2026-09-16

本人確認・口座・eKYC は出金や出品のゲートとして公式が書く机がある。このパックは出金も公開もしない。だから書類を上げる理由は無い。

ライブフォームが **下書きプロフィールを保存できない** と身分証を要求したら **stop**。机名と画面種類だけ朝の本人へ。アップロードしない。

CU は KYC を完了しない。朝の本人は兄弟 `earn-kyc-morning-checklist-20260916/`（あれば）。

---

## Allowed for this pack

- [ ] MAIN Google signup / login、または Google OAuth が無い机での **同じ MAIN Gmail** メール登録
- [ ] Email verification via **parent Gmail MCP**（コードを git に貼らない）
- [ ] SMS only if draft save is blocked, and only with a number the **user** placed in chat
- [ ] 人材 / 先生（企業・発注者コンソールは閉じる）
- [ ] Profile fields from the desk cards, saved as draft / 非公開 if a control exists
- [ ] ストアカ: 生徒〜先生プロフィール（名前・顔写真・公開 URL・自己紹介）。講座公開しない

## Hard stop — do NOT

Identity and tax (KYC):

- [ ] 本人確認申請 / オンライン本人確認 / eKYC
- [ ] Upload government photo ID（免許・パスポート・在留・住民基本台帳カード等）
- [ ] マイナンバーカード（表面・チップ・JPKI）または通知カード
- [ ] Type a national ID number, My Number, tax ID, インボイス登録番号
- [ ] Selfie / liveness for ID matching
- [ ] 住民票・住所証明のアップロード
- [ ] 複業クラウド TOS 第1.3条7 の「当社から要求された資料」
- [ ] ストアカの顔写真付き公的証明書 + 顔撮影
- [ ] Send ID photos to Support

Payments and paid plans:

- [ ] 口座 / 振込先 / bank / 出金申請
- [ ] Buy featured listings or paid membership
- [ ] Add a credit card “to verify you”

Publish and commerce:

- [ ] 案件への応募 / 提案送信 / スカウト承諾で契約
- [ ] ストアカ講座の公開申請
- [ ] プロフィールを「公開する」トグルが明示的にあるときの公開
- [ ] Anycrew 検索結果の「公開」

---

## Official stop text (do not treat as a GO)

### 複業クラウド

- 利用規約 第2.1条1: 登録タレントは本サービスを **無料で利用**できる。  
  https://cl.aw-anotherworks.com/user_tos  
- 同 第1.3条7: 登録情報の変更時に当社が **資料の提出を求める**ことがある。提出 UI = **STOP**。
- 同 第2.1条2: 当社が定めるプロフィール項目は **登録事業者に公開**される、と書く。追加の「公開する」トグルがあれば押さない。応募しない。
- 企業コンソール `cl.aw-anotherworks.com` のデモ・資料請求は閉じる。人材は `talent.aw-anotherworks.com` だけ。

### Anycrew

- 公開 FAQ（人材アプリ）: 通常は Web プロフィールのみ。エージェント仲介の一部案件は応募時に面談・職務経歴書。  
  https://app.any-crew.com/  
  職務経歴書が **必須** と出たら後回し。身分証が乗ったら KYC STOP。
- 規約第3条: 登録には外部 SNS。身分証アップロード条は公開規約に見当たらない → 画面が出たら STOP。
- `biz.any-crew.com` は閉じる。

### ストアカ

- `/teach` 公開面: 「先生として活動いただくためには、本人確認書類の提出をお願いしています」。提出画面 = STOP。
- `/register` 公開面: 「マンツーマンの講座は、本人確認も必須」。このパックは講座を作らない。
- 公式ヘルプ「オンライン本人確認について」URL は公開。**この環境の GET は Cloudflare 403** → 本文 **needs_check**。読めなくても eKYC 画面が出たら上げない。  
  https://support.street-academy.com/hc/ja/articles/4409755419673

---

## If KYC appears

1. Close the upload dialog. Do not choose a file.
2. Leave the profile in whatever unpublished state already saved.
3. Record only: date, desk, screen type (`photo_id` / `my_number` / `selfie` / `address` / `bank` / `ekyc` / `review_docs` / other).
4. Morning operator decides. This pack is complete as unpublished paste.
5. Continue to the **next** desk only if KYC is not a hard lock on the whole browser session.

Do not store screenshots that show ID, face, or full account email in the repo.

`kyc_wait` is a valid desk outcome. It is not failure.

# STOP before KYC — クラウディア worker（書類 + 自撮り）

Mode: **DRAFT_ONLY**  
Pack date: 2026-09-16

本人確認は公式が **出金・取引の信頼** のゲートとして書く（FAQ 103 / 93）。このパックは出金も応募もしない。だから書類も自撮りも上げる理由は無い。

ライブフォームが **下書きプロフィールを保存できない** と身分証・自撮りを要求したら **stop**。机名と画面種類だけ朝の本人へ。アップロードしない。

CU は KYC を完了しない。朝の本人は兄弟 `earn-kyc-morning-checklist-20260916/`（あれば）。

---

## Allowed for this pack

- [ ] MAIN Google signup / login、または同じ MAIN Gmail のメール仮登録（i2iID）
- [ ] Email verification via **parent Gmail MCP**（コードを git に貼らない）
- [ ] SMS / 電話認証 only if draft save is blocked, and only with a number the **user** placed in chat
- [ ] ワーカー **プロフィール** 下書き（FAQ 92 プロフィール編集）。公開トグルがあればオフ
- [ ] プロフィールの得意種別・スキル欄（実務があるものだけ）
- [ ] 公開ポートフォリオ URL（yutalab / GitHub）。mailto にしない

---

## Hard stop — do NOT

Identity (KYC) — **朝の本人確認 + 自撮り**:

- [ ] マイページ設定メニュー → **本人確認**（FAQ 93）
- [ ] https://www.craudia.com/mypage/setting/person （FAQ 156。未ログイン GET はトップ。**上げない**）
- [ ] Upload government photo ID（免許・マイナンバーカード・パスポート・在留・特別永住者証明書）
- [ ] **自撮り顔写真データ**（FAQ 93 必須と明記。エージェントは撮らない・選ばない）
- [ ] マイナンバーカードの個人番号面を強調して撮る・番号をタイプする
- [ ] Type a national ID number, My Number, tax ID
- [ ] 海外在住の追加証明（領事館の在留証明・公共料金領収書）。今のオペレーター想定外 → 止める
- [ ] Send ID photos or a selfie to Support

Payments:

- [ ] マイページ＞入出金管理＞振込依頼（FAQ 110）
- [ ] 口座登録・Craudia 口座からの出金
- [ ] クレジットカードを「確認のため」入れる
- [ ] Craudia PRO の有料マッチング登録

Publish and commerce:

- [ ] 参加申請（FAQ 89）
- [ ] 「納品する」から仕事開始
- [ ] スキルを出品する / スキル **公開**（FAQ 175 / 出品ガイド ステップ8）
- [ ] 見積もり提案を送る
- [ ] プロフィールを「公開する」トグルが明示的にあるときの公開

Phone:

- [ ] Phone SMS / 電話認証 for **account recovery** is not the same as ID upload. If onboarding blocks even a **draft** without it, the user may complete it on a device they control, then stop. If the phone step asks for ID, selfie, or 本人確認へ誘導（FAQ 156）, treat it as KYC and **stop**.

---

## Official stop text (do not treat as a GO)

### クラウディア

- 登録そのものに本人確認は **必須ではない**。  
  https://www.craudia.com/app/faq/contents/103  
  「会員登録時は連絡の取れるPCメールアドレスがあれば問題ございません。ただし、貯まった報酬をCraudia口座から出金される場合は、『本人確認』が必要となります。」
- 提出方法: ログイン後、マイページ設定メニューの「本人確認」。  
  https://www.craudia.com/app/faq/contents/93  
  日本の公的機関が発行した有効期限内の顔付き書類いずれか1つ + **自撮り顔写真データ（必須）**。目安: 提出後 **3営業日程度**。完了するとプロフィールに本人確認済みアイコン。
- 電話認証ができないときの案内も本人確認 URL を出す。  
  https://www.craudia.com/app/faq/contents/156  
  それでも **このパックでは上げない**。回避のために自撮りしない。
- 出金は振込依頼（FAQ 110）。出金しないので口座もやらない。振込手数料 300円（FAQ 39）は **cited, unused**。

提出画面 = **STOP**。バッジのために今すぐ出す代替もしない。朝の本人が上げる。エージェントはファイルを選ばない。カメラ権限を KYC に渡さない。

---

## If KYC appears

1. Close the upload dialog. Do not choose a file. Do not take a selfie.
2. Leave the profile in whatever unpublished state already saved.
3. Record only: date, desk, screen type (`photo_id` / `my_number` / `selfie` / `address` / `bank` / `person_confirm` / other).
4. Morning operator decides. This pack is complete as unpublished paste.
5. There is no next desk in this folder.

Do not store screenshots that show ID, face, or full account email in the repo.

`kyc_wait` is a valid desk outcome. It is not failure.

## 朝メモの型（秘密なし）

```
date:
desk: Craudia
screen: マイページ設定 → 本人確認
saved_draft: yes/no/unknown
kyc_shown: yes/no
selfie_required_by_faq93: yes
upload: none
pro_upgrade: no
apply: no
skill_listing: no
next: morning-user | park
```

エージェントが書いてよいログ（秘密なし）:

```
desk: Craudia
screen: マイページ設定 → 本人確認
action: STOP no upload
morning: user
docs_hint: 顔付き公的書類 + 自撮り（FAQ 93）
when: 出金の前。登録完了には不要（FAQ 103）
```

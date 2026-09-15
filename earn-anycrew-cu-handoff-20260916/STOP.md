# STOP — Anycrew（B10）no apply / no publish / KYC / phone

> **DRAFT_ONLY.** **REGISTER-CU-CUT.** No secrets. **No apply. No publish.**  
> Anycrew is **not** next live CU. Jobs-first. This file is a stop list, not a how-to for KYC, SMS, payments, or sending proposals.  
> This authoring agent did not sign up, apply, publish, or upload ID.

CU 手順: [PLAYBOOK.md](PLAYBOOK.md)  
Paste: [FIELD-MAP.md](FIELD-MAP.md)

---

## Primary stop: do not apply / do not publish

Anycrew `/offers` は activity-gate の枠（案件 SPA が生きていること）であり、**応募キューではない。**

押さない:

- 応募する / この案件に応募 / 応募を確定
- 気になる / 検討中から応募
- スカウトに返信 / メッセージを送る
- 検索結果の **公開**（FAQ: 「非公開」「公開」）

確認画面に入ったら戻る。送信しない。`apply: no` `publish: no` のまま [STATUS.md](STATUS.md) を書く。

同じ停止:

| Live wording / wall (examples) | Action |
|---|---|
| 応募する / この求人に応募 / 応募を確定 | Close. `apply_wall` |
| 「応募にはプロフィール公開が必要」 | Do not flip public just to apply. Park |
| エージェント仲介で職務経歴書が必須 | Stop. 応募しないので通常出ない |
| 面談を申し込む / 日程を確定 | Stop. Morning user |
| 求人を掲載する / 法人向け | Close. `biz.any-crew.com` |

JOBS フェーズの他机ドラフト（Coconala / Contra / Freelancer bids など）も **この Anycrew 机からは送らない。**

Offers.jp の「登録して求人に応募する」はこの机の話ではない。取り違えない。

---

## STOP-at-phone

登録 JS（この GET）に「電話番号」「SMS」は無かった。プライバシーは **応募・契約時** に電話番号を収集項目として書く。

ライブが電話・SMS を出したら:

- 実番号を git / 成功ログ / チャットに貼らない。
- 下書き保存が電話なしで通るなら空で進む。
- 下書きが止まる → `sms_wait_user` / `phone_wall`。ユーザーチャット。CU は番号を推測しない。
- 電話 OTP を親 Gmail 経路で取らない（SMS は朝の本人）。
- 応募のために電話を埋めて突破しない。

フィールド手順（キャリア選択、SMS 再送の裏技）は書かない。

---

## STOP-at-KYC

公開プライバシーの利用目的に「登録の受付、**本人確認**」とある。書類ウィザードはこの GET では出ていない。

ライブが書類・自撮り・マイナンバーを出したら:

- 画面の **種類だけ** メモして閉じる（例: 顔付き身分証、自撮り）。フィールド手順は書かない。
- アップロードしない。朝の本人。
- `kyc_wait`。このパスは終わる。

口座・出金・e-sign も同じ。代理入力しない。

---

## Also stop

### Money / paid

規約（この GET）:

- 第5条 利用者は **基本的に無料**
- 求人事業者の有料プランは **employer** — 触らない
- アプリ FAQ: 人材側は「一切費用はかかりません」
- **人材％は FAQ / 規約に数字なし → 作らない**

止め: 有料プラン、カード入力、口座、第三者記事のマージン％を埋める。

### Employer / hire side

- https://biz.any-crew.com/ と `/login` は採用側。人材ではない。
- ID JS の **法人向けログイン** を選ばない。

### OAuth / extra identities

- MAIN Google 以外の新規 Google / 新規メールを作らない
- Facebook をこの机のためだけに作らない（「Facebookで登録する」は STOP）
- Gmail / Drive / Contacts の過剰スコープは拒否 → `oauth_overreach`
- Google OAuth の **POST をこの authoring から送らない**（GET は 404。完走は後続 CU + 人）

### Secrets / CSRF

OTP・パスワード・電話・`authenticity_token`・セッション Cookie を git や成功ログに書かない。OTP は親 Gmail。CU は `mail.google.com` を開かない。

### GraphQL / SPA scrape

`base.any-crew.com/graphql` へ POST して `/offers` カードを埋めない。CSRF が要る。activity は人が 1 画面見たときだけ。

---

## Allowed before stop

ここまでやってよい（人が GO した CU のとき）:

1. https://app.any-crew.com/ または https://id.any-crew.com/signup?auth_entry_source=front
2. MAIN **Googleで登録する / Googleでログイン**（または同じ MAIN メール）
3. プロフィール・スキル・公開 URL を [FIELD-MAP.md](FIELD-MAP.md) から貼る
4. 検索結果 **非公開**
5. **下書き保存**
6. `/offers` シェルを目視する（応募しない。カードが空なら `needs_check` のまま）

ここで終わる。次の机へ進む指示がこのフォルダにあっても、**応募してから進むことはない。**

---

## If a wall appears

| Wall | STATUS token | Next |
|---|---|---|
| Apply required to save profile | `apply_wall` | Stop. Do not apply. Tell the morning user |
| Public profile required to apply | `apply_wall` | Do not flip 公開 |
| KYC / selfie / My Number | `kyc_wait` | Close wizard. No upload |
| Phone / SMS OTP | `sms_wait_user` / `phone_wall` | User chat. Do not guess. Do not log the number |
| Gmail OTP | parent Gmail | CU does not open Gmail |
| `/offers` still empty | `needs_check_offers` | Do not invent dates. Do not GraphQL POST |
| Paid plan / card | `card_wall` | Close |
| No draft-save control | `no_draft_path` | Park |
| Hold / captcha fail | `hold_failed` | Park after one retry with `holdDurationMs` 2500 |
| Google missing on live page | park (email-only is `needs_check`) | Still no new identity / no Facebook |

Do not invent a workaround that includes 応募、公開、電話突破、または身分証アップロード。

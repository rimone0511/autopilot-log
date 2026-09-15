# STOP — Offers（B19）no apply

> **DRAFT_ONLY.** No secrets. **No apply.** **REGISTER-CU-CUT.**  
> Default: do **not** treat Offers as next live CU. Prefer JOBS.  
> This file is a stop list. It is not a how-to for KYC, payments, or sending proposals.  
> This authoring agent did not sign up, apply, or upload ID.

CU 手順: [PLAYBOOK.md](PLAYBOOK.md)  
Paste: [FIELD-MAP.md](FIELD-MAP.md)

---

## Primary stop: do not apply

Offers Jobs は activity-gate の根拠（業務委託カードが生きていること）であり、**応募キューではない。**

この GET で繰り返し出る CTA:

- 「**登録して求人に応募する**」（`/jobs/engineer/side-job` ほか）

押さない。確認画面に入ったら戻る。送信しない。`apply: no` のまま [STATUS.md](STATUS.md) を書く。

同じ停止:

| Live wording / wall (examples) | Action |
|---|---|
| 応募する / この求人に応募 / 応募を確定 | Close. `apply_wall` |
| 気になる / 検討中リストから応募 | Close. Not a substitute apply |
| スカウトに返信 / メッセージを送る | Do not send this pass |
| カジュアル面談を申し込む / 日程を確定 | Stop. Morning user |
| ヘッドハント面談のカレンダー確定 | Stop |
| 職務経歴書を「応募のため」必須アップロード | Stop. Profile draft に不要なら後回し |
| 「応募にはプロフィール公開が必要」 | Do not flip public just to apply. Park |

JOBS フェーズの他机ドラフト（Coconala / Contra / Freelancer bids など）も **この Offers 机からは送らない。**

---

## Also stop (not apply, still out of scope)

### Identity / KYC

公開プライバシーポリシー GET に「本人確認」文字列は無かった。ライブが書類・自撮り・マイナンバーを出したら:

- 画面の **種類だけ** メモして閉じる（例: 顔付き身分証、自撮り）。フィールド手順は書かない。
- アップロードしない。朝の本人。
- `kyc_wait`。このパスは終わる。

### Money / paid

規約（この GET）:

- 第11条 システム利用料 = **クライアント** が払う
- 第12条 マッチング成功報酬 = **クライアント** が「当社が指定する手数料」を払う
- **％は規約に数字なし → 作らない。** 第三者記事の「ワーカー無料・マージンなし」を手数料欄に固定しない

止め:

- 有料ブース / 優先掲載
- カード入力
- 口座・出金
- 成功報酬のユーザー負担を発明して埋める

### Client / hire side

- https://offers.jp/client と `/client/login` は採用側。ワーカーではない。
- ワークスペースをクライアントに切り替えない。

### OAuth / extra identities

- MAIN Google 以外の新規 Google / 新規メールを作らない
- この机のためだけに X / LinkedIn アカウントを作らない
- GitHub は公開リポジトリと一致するときだけ（任意）
- Gmail / Drive / Contacts の過剰スコープは拒否 → `oauth_overreach`

### Secrets

OTP・パスワード・電話・CSRF・セッション Cookie を git や成功ログに書かない。OTP は親 Gmail。CU は `mail.google.com` を開かない。

---

## Allowed before stop

ここまでやってよい（人が GO した CU のとき）:

1. `/worker/signup` または `/worker/login`
2. MAIN **Google で登録する / ログインする**（または同じ MAIN メール）
3. プロフィール・スキル・公開 URL を [FIELD-MAP.md](FIELD-MAP.md) から貼る
4. **下書き保存**
5. Jobs 見出しを目視する（応募しない）

ここで終わる。次の机へ進む指示がこのフォルダにあっても、**応募してから進むことはない。**

---

## If a wall appears

| Wall | STATUS token | Next |
|---|---|---|
| Apply required to save profile | `apply_wall` | Stop. Do not apply. Tell the morning user |
| KYC / selfie / My Number | `kyc_wait` | Close wizard. No upload |
| SMS OTP | `sms_wait_user` | User chat. Do not guess |
| Gmail OTP | parent Gmail | CU does not open Gmail |
| Paid booth / card | `card_wall` | Close |
| No draft-save control | `no_draft_path` | Park |
| Hold / captcha fail | `hold_failed` | Park after one retry with `holdDurationMs` 2500 |
| Google missing on live page | email fallback same MAIN | Still no new identity |

Do not invent a workaround that includes 応募.

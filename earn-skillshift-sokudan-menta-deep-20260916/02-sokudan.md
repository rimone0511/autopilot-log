# B1 / CU-13 — SOKUDAN（ソクダン）CU desk

Desk: SOKUDAN  
CU serial: **CU-13**（INDEX）。この deep pack では 2 番目  
Checked: 2026-09-16（公開 signup/login HTML、トップ FAQ、規約）  
Mode: **DRAFT ONLY**  
Language: **日本語**  
Google: **PREFER_GOOGLE**  
OTP: 認証メール → **Gmail parent**. SMS → **user chat**  
activity_gate: **pass**（PR#12）  
Operator: CAMELORS株式会社（規約）

---

## 0. How far to go (then stop)

1. https://sokudan.work/signup/pro — **フリーランス・副業の方向け**。企業の方は閉じる。
2. 「Google で登録」。Facebook「推奨」は使わない。
3. プロフィール・スキル・公開 URL。下書き保存。
4. **応募しない。** スカウト返信しない。
5. 審査書類 UI = STOP。
6. Success line. Then Anycrew.

Timebox: 15–25 minutes.

---

## 1. URLs

### Confirmed

| What | URL |
|---|---|
| Home | https://sokudan.work/ |
| 人材 無料新規登録 | https://sokudan.work/signup/pro |
| Login | https://sokudan.work/login |
| Google signup（登録 HTML） | `/users/auth/google?category=signup&usage_type_id=1` |
| Google login | `/users/auth/google?category=login` |
| 利用規約 | https://sokudan.work/pages/terms |
| プライバシー | https://sokudan.work/pages/policy （`/pages/privacy` は 2026-09-16 に 404） |
| FAQ（トップ内アコーディオン） | ホーム。Notion 転送の `/pages/faq` よりトップ HTML を正とする場合あり |

### Guess only

```
{{URL_GUESS_SOKUDAN_PROFILE_EDIT}}
```

他プロバイダ（登録 HTML 2026-09-16）: Facebook / LinkedIn / X(Twitter) / GitHub / メール。  
**Google を選ぶ。** GitHub は公開リポジトリと一致するときだけ次点。新しい SNS を作らない。

Internet Explorer 不可、と登録面に書いてある。現行ブラウザを使う。

---

## 2. Google MAIN notes (this desk)

1. Land on https://sokudan.work/signup/pro
2. Click the Google icon（`alt="Google で登録"`）。「Facebook で無料登録 / 推奨」は無視。
3. Picker: `rimone0511@gmail.com` only.
4. Consent: basic profile/email. Deny Gmail-read-all.
5. Already registered: **ログイン** https://sokudan.work/login → Google でログイン。
6. フォールバック: 「メールで無料登録」。メール = MAIN Gmail。パスワードはローカル。
7. 認証メール: parent Gmail。再送 1 回まで。
8. Hold: `holdDurationMs: 1800`.

規約第4条: 代理人による会員登録は認められない。CU 直列は本人が同席する前提。この markdown の著者は登録しない。

---

## 3. Profile paste fields (JP)

登録直後の必須ラベルはログイン壁の向こう。公開情報 + 人材登録面の範囲。ライブを正とする。

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | Google | 必須 | PREFER_GOOGLE |
| メール | `{{EMAIL}}` | Googleから来る | |
| 氏名 | `{{LEGAL_NAME_KANJI}}` | 高 | 公開名が分かれるなら表示は `{{DISPLAY_NAME}}` |
| 生年月 | `{{BIRTH_YEAR}}` / `{{BIRTH_MONTH}}` | 高 | 日が無ければ空 |
| 居住地 | `{{PREFECTURE}}` `{{CITY}}` | 高 | 番地は KYC 手前なら空でよい |
| 電話番号 | `{{PHONE}}` | 高 | SMS なら user chat |
| 職種 | エンジニア / 自動化 / 業務改善の最寄り | 高 | 「AI」だけにしない |
| 所有スキル | n8n, 業務自動化, Python, YouTube Data API, TikTok Content Posting API, Claude Code | 高 | 未経験を経験と書かない。スキルに `xAI` / `Grok` を詰め込まない |
| 経験年数 | `{{YEARS_AUTOMATION_PUBLIC}}` | 高 | 未確認なら空 |
| 職務経歴 | 下記 800 字を短縮 | 高 | 規約に AI 作成支援あり。人が検品してから保存 |
| 職務経歴書ファイル | 任意。ローカル PDF | 任意〜高 | リポジトリに置かない。必須と言われたら後回し |
| ポートフォリオ | `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}` | 高 | |
| 稼働条件 | リモート可。週次は要相談 | 高 | 数字の創作禁止 |
| SNS | `{{GITHUB_URL}}` | 任意 | |
| 現所属の非公開 | 画面に「同じ会社名は互いに見えない」FAQ あり | 任意 | 就業規則は人が確認。社名を git に書かない |
| 招待コード | `{{INVITE_CODE}}` | 任意 | 空でよい |
| 応募 | やらない | STOP | |

トップ FAQ: 「同じ会社名を登録しているユーザーは、互いに登録情報が閲覧できない」。所属企業名の扱いだけ人が決める。

### キャッチ

```
AI業務自動化と手順書。公式APIのみ。ブラウザ自動操作なし
```

### JA bio 200

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIによる業務自動化の手順・つまずき・確認できた結果を、むずかしい言葉を避けて公開しています。公式APIだけを使う動画アップロード道具も公開中です。ブラウザ自動操作はしません。人が検品できる形で、繰り返し作業を自動化します。リモート可。未確認の数字は書きません。公開は人が決めます。秘密は貼りません。根拠を残す方針です。
```

### JA bio 800

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AIを使って毎日の作業を自動化する手順、つまずいた点、確認できた結果を、むずかしい言葉を避けて公開しています。売り物は「動いたように見える自動化」ではなく、人が検品できる仕組みです。公開している実録と道具を、業務委託の成果物の根拠にします。提供できること：（1）繰り返し作業の自動化設計。目的・範囲・合格条件・停止条件を先に切り、実装後に回帰確認まで残します。（2）Claude CodeやCodexなど、AIに実装を任せるときの指示の書き方、検品、失敗時の切り分け。（3）YouTubeとTikTokへの公式API投稿の仕組みづくり。ブラウザ自動操作とスクレイピングは対象外です。（4）鍵の扱い、公開事故、トークン期限など、自動化が止まりやすい箇所の点検。公開している道具の例：Autopilot Log（https://github.com/rimone0511/autopilot-log）。YouTube Data API v3 と TikTok Content Posting API のみを使い、投稿の門番は壊れても非公開側に倒れます。受けないこと：いいねやフォローの自動化、権利のない投稿代行、本人確認書類・口座・マイナンバーの代理入力、未確認のままの公開。進め方はテキスト中心です。根拠と反証を残し、公開スイッチは依頼者または本人の手に置きます。リモート可。週次の稼働時間は案件ごとに相談します。未確認の件数や年数は書きません。確認できた公開物だけを貼ります。秘密はチャットに出さず、本人の安全な入力経路だけを使います。日本語でのやり取りを標準にします。英語の一次資料は必要なら要約して渡します。契約前に範囲外を一文で確定します。納期は着手前に合意します。作業の記録を残す。
```

規約第7条の AI 機能で自己紹介を自動生成できる、とある。使うなら **保存前に人が直す**。件数を足させない。

---

## 4. Fees — official public pages only

| Claim | Status | Source | Quote / note |
|---|---|---|---|
| 人材側の利用は無料 | **cited** | トップ FAQ「サービスを利用するのに、費用はかかりますか？」 https://sokudan.work/ | 「すべて無料でご利用いただけます。採用担当者としてご利用する場合は、こちらからお問い合わせください。」 |
| 登録面の「無料新規登録」 | **cited** | https://sokudan.work/signup/pro | 見出し「無料新規登録」／「メールで無料登録」 |
| 仲介マージン％ | **needs_check** | 規約第10条 https://sokudan.work/pages/terms | 「本サービス利用料」「委託料に含まれる当社の手数料の料率」とあるが **％は未記載**。メタ description の「仲介手数料ゼロ」はマーケ。FAQ の「すべて無料」以外の％を創作しない |
| 2020 プレスの「仲介手数料ゼロ」 | **do not cite as current fee** | ニュース 2020-02-13 | 古い告知。料率表の代わりにしない |

Do not type CrowdWorks/Lancers % onto this desk.

---

## 5. Explicit do-not

- 案件応募
- 審査書類・身分証・口座
- Facebook 推奨ボタン
- 発注者機能の申込（規約に発注機能の追加規定あり）
- マーケ「92% リモート」を自己紹介にコピーして実績のように見せる

---

## 6. Success before Anycrew

| Outcome | Meaning |
|---|---|
| `done-draft` | Google 人材。自己紹介保存。応募なし |
| `already_member_draft` | 既存。未公開のまま |
| `kyc_wait` | 第4条書類。閉じた |

```
desk: SOKUDAN
pack: earn-skillshift-sokudan-menta-deep-20260916/02-sokudan.md
auth: google-main | email-same-mailbox | already_member | blocked
otp: gmail-parent | sms-chat | none
kyc: none | wait-morning + type
draft_profile: yes/no
publish: no
apply: no
next: Anycrew
```

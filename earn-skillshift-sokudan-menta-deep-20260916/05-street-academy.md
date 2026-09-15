# B7 / CU-17 — ストアカ（Street Academy）講師 CU desk

Desk: ストアカ  
CU serial: **CU-17**  
Checked: 2026-09-16（www は WAF 405。公式ヘルプ URL は公開。ヘルプ本文 GET は 403。teach.street-academy.com は 200）  
Mode: **DRAFT ONLY** — プロフィールまで。**講座公開しない。eKYC しない**  
Language: **日本語**  
Google: **NOT_OFFERED_OAUTH** → メール = MAIN Gmail  
OTP: 認証メール → **Gmail parent**  
activity_gate: **needs_check**

アプリは先生機能なし、と既存ヘルプ。**ブラウザで登録**（人がやる / CU 直列）。

---

## 0. How far to go (then stop)

1. Human: www が WAF ならブラウザで Human Verification。開けなければ park。死滅とはしない。
2. 新規登録 → **メールアドレスで登録**。LINE / Facebook は使わない。
3. 生徒アカウントのあと、先生プロフィール（名前・顔写真・公開 URL・自己紹介）。
4. 本人確認（顔写真付き公的証明書 + 顔撮影）画面 = STOP。
5. 講座作成ウィザードに入っても **公開申請しない**。下書きが無いならプロフィールのみ。
6. Success line. End of this pack.

Timebox: 15–25 minutes.

---

## 1. URLs

### Confirmed

| What | URL | This env |
|---|---|---|
| Home | https://www.street-academy.com/ | 405 WAF |
| Register | https://www.street-academy.com/register | 405 WAF |
| Teach | https://www.street-academy.com/teach | 405 WAF |
| 講師メディア | https://teach.street-academy.com/ | 200 |
| 会員登録の方法（PC） | https://support.street-academy.com/hc/ja/articles/360011723660 | 公式 URL。GET 403 |
| 手数料 | https://support.street-academy.com/hc/ja/articles/200700579 | 公式 URL。GET 403 |
| オンライン本人確認 | https://support.street-academy.com/hc/ja/articles/4409755419673 | 公式 URL |
| 本人確認書類を提出する | https://support.street-academy.com/hc/ja/articles/201574119 | 公式 URL |

### Guess only

```
{{URL_GUESS_STOREKA_PROFILE}}
{{URL_GUESS_STOREKA_LESSON_NEW}}
```

---

## 2. Google MAIN notes (this desk)

公式ヘルプ「会員登録の方法（パソコンサイト）」:

> 登録は、**LINE・Facebook・メールアドレス**より選択してください。  
> メールアドレスで登録する場合は、登録したいメールアドレスと設定したいパスワードを入力して［メールアドレスで登録］。

Google OAuth は案内に無い。

方針:

1. ［新規登録］→ **メールアドレスで登録**
2. メール = `{{EMAIL}}`（MAIN Gmail）
3. パスワード = ローカル台帳。git に書かない
4. LINE / Facebook は、メール経路が死んでいるときだけ。新規 Facebook/LINE をこの仕事のためだけに作らない
5. 認証メール: parent Gmail。リンクを同じプロファイルで開く。再送 1 回
6. アプリ登録は先生マイページが無い、とヘルプ系。PC ブラウザ
7. Hold / WAF: `holdDurationMs: 1800` / retry `2500`

---

## 3. Profile paste fields (JP)

公式ヘルプ（PC 登録）: ご本人が特定できる顔写真と、登録名と顔が確認できる SNS または HP。その後に本人確認・先生ページ・講座。  
**このパックはプロフィール更新まで。** 本人確認画面は開いたら閉じる。

| 画面の項目（公開ヘルプベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | メールアドレスで登録 | 必須 | NOT_OFFERED_OAUTH |
| メール | `{{EMAIL}}` | 必須 | |
| パスワード | ローカルのみ | 必須 | |
| 名前 | 生徒表示 `{{DISPLAY_NAME}}` / 先生は実名 `{{LEGAL_NAME_KANJI}}` | 必須 | |
| 性別 | `{{GENDER_FORM_VALUE}}` | 生徒登録で出る | 未設定可なら空 |
| 地域 | `{{PREFECTURE}}` | 生徒登録で出る | |
| 興味カテゴリ | ビジネス / IT・プログラミングの最寄り | 任意 | |
| 先生: 顔写真 | `{{PHOTO_LOCAL_PATH}}` 本人が特定できる顔 | 必須に近い | 身分証の写真をアイコンにしない。コミット禁止 |
| 先生: SNSまたはHP | `{{PORTFOLIO_URL}}` | 必須に近い | 顔が確認できる公開ページ |
| 自己紹介 | 下記 200 / 800 | 高 | |
| 電話番号確認 | スキップ可なら skip | 任意 | OTP なら user chat |
| 本人確認書類 / eKYC | やらない | STOP | |
| 講座ページ | やらない / 下書きのみ | 出品 STOP | |
| 自己集客 URL の発行 | KYC 前でも「見るだけ」可 | 任意 | 講座公開はしない |

### JA bio 200（講師向け）

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AI自動化の手順を初心者向け日本語で公開しています。公式APIの動画投稿も扱います。ブラウザ自動操作は教えません。最初の1回を、人が確認できる形で安全に動かすところまで伴走します。公開スイッチは受講者本人が持ちます。未確認の数字は書きません。リモート可。宿題は小さく先に切ります。秘密は貼りません。必ず根拠だけ教えます。
```

### JA bio 800（講師向け）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AI自動化の手順を初心者向けの日本語で公開しています。教える範囲は、道具の入れ方から「最初の1回を安全に動かす」までです。専門用語は後回しにし、つまずきやすい場所を先に書きます。教えられること：（1）Claude Code / Codex のはじめ方と、対象ファイル・完成条件・禁止事項を入れた指示の書き方。（2）毎日の作業を自動化してよいかの見分け。秘密・公開・課金が絡む仕事は外す判断。（3）公式APIだけを使う動画投稿の考え方。ブラウザ自動操作やスクレイピングは教えません。（4）動いたあとの検品。仕様、境界値、秘密情報、権限、再現性の順に見ます。公開している教材の土台：ユタラボの実録記事と、Autopilot Log（https://github.com/rimone0511/autopilot-log）。投稿の門番は壊れても非公開側に倒れる設計です。受けないこと：代行ログイン、本人確認の代理、権利のない投稿、未確認の公開、いいね自動化。進め方はチャットまたは非同期テキストです。宿題は小さく切り、合格条件を先に合意します。公開スイッチは受講者本人が持ちます。未確認の受講者数や収益は書きません。公開記事と公開リポジトリを教材の根拠にします。秘密はチャットへ貼らず、本人の画面で入力してもらいます。レッスンはオンライン想定です。録画の外部公開はしません。課題の提出物に秘密を含めないよう、提出前チェックを宿題にします。料金と回数はプラン欄で別途示し、プロフィール本文では約束しません。初回は環境確認から始め、いきなり本番公開へ進みません。止める条件も先に書きます。画面共有なしでも進められます。質問はテキストで残します。未確認の効果は言いません。料金はプラン欄だけに書きます。
```

---

## 4. Fees — official public pages only

公式ヘルプ本文は **この環境では Cloudflare 403**。数字は公式記事 URL の公開スニペットに出たものだけ残し、**貼る直前に人が公式を再読**する。再読できないなら料率を価格欄に使わない。

| Claim | Status | Source | Quote / note |
|---|---|---|---|
| 自己集客 10% / ストアカ送客 30%（対面講座 20%） | **cited from official URL snippets; live GET needs_check** | https://support.street-academy.com/hc/ja/articles/200700579 | 公式 Q「ストアカの手数料・利用料はいくらですか？」: 初めての提供は自己集客 10%（自己集客 URL 経由に限る）、ストアカ送客 30%（対面開催の講座は 20%）。自己集客 URL をストアカ内やストアカユーザーへ送って送客手数料を避けることは公式が禁止 |
| リピーター 10% | **cited from same official article snippets; live GET needs_check** | 同上 | ご自身で集客した場合は新規・リピーター共に 10%、という Q&A が公式記事スニペットに出る。**再読必須** |
| 全サービスへの料率展開（2022-07） | **cited URL** | https://support.street-academy.com/hc/ja/articles/7110479391129 | 講座以外（依頼・月額）にも自己集客/送客/リピーターを導入、と告知。現行表は 200700579 を正とする |
| www 上の「無料ではじめられる」 | **needs_check** | `/teach` は this env 405 | 初期費用ゼロのコピーは WAF で未取得。手数料表の代わりにしない |

運用メモ（KYC 前でも URL 発行だけ見るのは可。講座公開は本人判断）:

- ユタラボからの流入は **自己集客 URL** 前提。ストアカ内 SEO 流入は送客側
- プロフィールに「手数料 10%」と書いて集客する必要はない（誤解のもと）

---

## 5. KYC stop (this desk)

公式「オンライン本人確認について」:

- 対象: 先生ユーザー、主催団体（法人以外）の管理者
- 有効期限内のいずれか 1 点の撮影: 免許 / パスポート（日本国政府発行） / 住民基本台帳 / マイナンバーカード / 在留カード / 運転経歴証明書 / 特別永住者証明書 **+ 本人の顔写真（撮影）**
- ウェブカメラまたはスマホカメラの eKYC

**どれも上げない。** Blue バッジ後に必須、と書いてあってもこのパックではやらない。

講座 3 回までに本人確認、という第三者解説は公式として使わない。公式ヘルプの提出画面だけを STOP 条件にする。

---

## 6. Explicit do-not

- LINE / Facebook 新規身分
- eKYC / 身分証 / 口座
- 講座公開申請
- ストアカ内で自己集客 URL を回して 10% を狙う（公式禁止）
- 受講料の創作

---

## 7. Success (end of pack)

```
desk: Storeka
pack: earn-skillshift-sokudan-menta-deep-20260916/05-street-academy.md
auth: email-same-mailbox | already_member | blocked | waf_park
otp: gmail-parent | sms-chat | none | otp_missing
kyc: none | wait-morning + ekyc
draft_profile: yes/no
draft_lesson: skipped | saved-unpublished | none
publish: no
next: stop (pack complete)
```

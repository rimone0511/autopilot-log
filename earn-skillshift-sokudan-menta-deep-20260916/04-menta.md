# B6 / CU-16 — MENTA（メンター）CU desk

Desk: MENTA  
CU serial: **CU-16**  
Checked: 2026-09-16（register/choose、特商法、about_mentor、Intercom ヘルプ）  
Mode: **DRAFT ONLY** — プロフィール保存まで。**プラン公開しない**  
Language: **日本語**  
Google: **PREFER_GOOGLE**  
OTP: Google 経路なら通常なし。メール経路は使わない  
activity_gate: **needs_check**（プラン一覧が環境により WAF。登録面は 200）  
Operator: 特商法ページどおり（ランサーズ株式会社 — 特商法を再読）

---

## 0. How far to go (then stop)

1. Human: トップまたは登録面が開くこと。プランカード日付が WAF なら needs_check のまま進めてよいが、**プランは公開しない**。
2. https://menta.work/index.php/register/choose → **Googleアカウントで登録する**。
3. メンター寄りのプロフィール（自己紹介）。受講者だけの箱に閉じない。
4. プラン名・料金は **空のまま**。出品しない。
5. 設定 → 本人確認ページ = STOP。口座 = STOP。
6. Success line. Then ストアカ.

Timebox: 15–25 minutes.

---

## 1. URLs

### Confirmed

| What | URL |
|---|---|
| Home | https://menta.work/ |
| 登録経路 | https://menta.work/index.php/register/choose |
| Google OAuth | https://menta.work/index.php/oauth/google |
| メンター案内 | https://menta.work/about_mentor |
| 特商法 | https://menta.work/tokutei |
| 本人確認ヘルプ | https://intercom.help/mentajp/ja/articles/3025561 |
| 手数料ヘルプ | https://intercom.help/mentajp/ja/articles/3025582 |

### Guess only

```
{{URL_GUESS_MENTA_PROFILE}}
{{URL_GUESS_MENTA_PLAN_NEW}}   # 触らない / 公開しない
```

登録面の他ボタン（2026-09-16）: メール / X / Facebook / Apple / Lancers。**使わない。**

---

## 2. Google MAIN notes (this desk)

1. https://menta.work/index.php/register/choose
2. 「Googleアカウントで登録する」（クラス `m-button__text google`）。
3. Picker: `rimone0511@gmail.com` only.
4. Consent: basic. Deny Gmail-read-all.
5. 既登録ならログイン。Lancers アカウントで登録する、は使わない（別身分になる）。
6. 環境によって登録面が WAF。Hold `1800` / retry `2500`。失敗なら park（`hold_failed`）。ゲート needs_check のまま。

プラン提出は KYC ではないが **公開＝出品**。このパックの完了はプロフィール保存。プラン提出は本人の別判断。エージェントは出品しない。

---

## 3. Profile paste fields (JP)

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | Google | 必須 | |
| ユーザー名 | `{{DISPLAY_NAME}}` または英数制限に合わせる | 高 | 変更可否はライブヘルプ。空ならユーザーに一度聞く |
| アイコン | `{{PHOTO_LOCAL_PATH}}` | 任意 | 身分証禁止 |
| 自己紹介 | 下記 200 / 800 | 必須に近い | メンター案内が詳細記入を促す |
| 経歴・実績 | 公開記事と公開リポジトリのみ | 高 | 受講者数を作らない |
| 教えられること | Claude Code, Codex, 自動化の始め方, 公式API投稿, 検品 | 高 | ブラウザ自動操作は教えないと明記 |
| 教え方 | テキスト中心、宿題を小さく切る、公開スイッチは受講者 | 高 | |
| プラン名 | 空 | STOP | |
| プラン料金 | 空 | STOP | 円額を創作しない |
| Stripe 本人確認 | やらない | STOP | |
| 口座 | やらない | STOP | |

### JA bio 200（メンター向け）

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AI自動化の手順を初心者向け日本語で公開しています。公式APIの動画投稿も扱います。ブラウザ自動操作は教えません。最初の1回を、人が確認できる形で安全に動かすところまで伴走します。公開スイッチは受講者本人が持ちます。未確認の数字は書きません。リモート可。宿題は小さく先に切ります。秘密は貼りません。必ず根拠だけ教えます。
```

### JA bio 800（メンター向け）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AI自動化の手順を初心者向けの日本語で公開しています。教える範囲は、道具の入れ方から「最初の1回を安全に動かす」までです。専門用語は後回しにし、つまずきやすい場所を先に書きます。教えられること：（1）Claude Code / Codex のはじめ方と、対象ファイル・完成条件・禁止事項を入れた指示の書き方。（2）毎日の作業を自動化してよいかの見分け。秘密・公開・課金が絡む仕事は外す判断。（3）公式APIだけを使う動画投稿の考え方。ブラウザ自動操作やスクレイピングは教えません。（4）動いたあとの検品。仕様、境界値、秘密情報、権限、再現性の順に見ます。公開している教材の土台：ユタラボの実録記事と、Autopilot Log（https://github.com/rimone0511/autopilot-log）。投稿の門番は壊れても非公開側に倒れる設計です。受けないこと：代行ログイン、本人確認の代理、権利のない投稿、未確認の公開、いいね自動化。進め方はチャットまたは非同期テキストです。宿題は小さく切り、合格条件を先に合意します。公開スイッチは受講者本人が持ちます。未確認の受講者数や収益は書きません。公開記事と公開リポジトリを教材の根拠にします。秘密はチャットへ貼らず、本人の画面で入力してもらいます。レッスンはオンライン想定です。録画の外部公開はしません。課題の提出物に秘密を含めないよう、提出前チェックを宿題にします。料金と回数はプラン欄で別途示し、プロフィール本文では約束しません。初回は環境確認から始め、いきなり本番公開へ進みません。止める条件も先に書きます。画面共有なしでも進められます。質問はテキストで残します。未確認の効果は言いません。料金はプラン欄だけに書きます。
```

プロフィール本文に手数料％や「稼げる額」を書かない。料金はプラン欄だけ、かつこのパックではプラン欄を空にする。

---

## 4. Fees — official public pages only

二つの公式表現がある。**両方 cited。プロフィールに数字を貼らない。** 価格を付けるとき人が特商法とヘルプを再読する。

| Claim | Status | Source | Quote / note |
|---|---|---|---|
| メンター手数料 20%税別（利用15%+決済5%） | **cited** | 特商法 https://menta.work/tokutei | 「メンターには、メンティーからメンターへ支払われる報酬の20％（税別）の手数料（利用手数料15％＋決済手数料5％）が発生します。」メンティー側 10%税別も同ページ |
| 振込都度 300円 | **cited** | 特商法 同ページ | 「当社からメンターに対して振込みが発生する都度、300円の振込手数料が発生します。」 |
| 運用案内 22%（20%+消費税10%） | **cited** | ヘルプ 2022-08-31 https://intercom.help/mentajp/ja/articles/3025582 | 「手数料22%（手数料20% + 消費税10%）」例: 10,000円プラン → 手数料 2,200円、報酬 7,800円。出金1回あたり振込 300円 |
| メンター案内の 20%+消費税 | **cited** | https://menta.work/about_mentor | 「利用手数料は売上の15%、決済手数料は5%の合計20%+消費税」「出金時に都度300円」 |
| 出金条件 | **cited**（KYC 理由。GO ではない） | about_mentor | 売上 1,000円超かつ入金日から30日。事前に本人確認・口座 |

旧料率（2022-06-13 以前の月額）はヘルプに階段がある。新規プランには使わない。

Do not invent a third percentage to “reconcile” 20%税別 vs 22%込。

---

## 5. Explicit do-not

- プラン公開
- Stripe 本人確認
- 口座・出金
- メール / X / Apple / Lancers 登録
- 受講者数・収益の創作
- 有料ブースト

---

## 6. Success before ストアカ

```
desk: MENTA
pack: earn-skillshift-sokudan-menta-deep-20260916/04-menta.md
auth: google-main | already_member | blocked
otp: none | gmail-parent | otp_missing
kyc: none | wait-morning + stripe_identity
draft_profile: yes/no
draft_plan: none | saved-unpublished | skipped
publish: no
next: Storeka
```

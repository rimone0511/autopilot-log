> DRAFT_ONLY paste pack. NO secrets. NO browser signup from this PR. NO publish.
> CU-ready field map for a later human/CU session. Agent that wrote this pack did not create an account.
> `thin_site_skip: false` unless public evidence shows the product is dead.
> Stop at KYC: do not upload ID, My Number, bank, Stripe identity, or e-sign identity contracts.

# CU-16 PACK — MENTA（メンター登録）

| キー | 値 |
|---|---|
| sample_inventory | 04 |
| cu_serial | CU-16 |
| activity_gate | **needs_check**（カタログ日付未読。登録面は環境により WAF） |
| self_serve | **yes**（公開「無料登録」+ メンター募集。プラン公開は別） |
| cu_ready | **true** |
| official | https://menta.work/ |
| register | https://menta.work/index.php/register/choose |
| google_oauth | https://menta.work/index.php/oauth/google |
| mentor | https://menta.work/about_mentor |
| kyc_help | https://intercom.help/mentajp/ja/articles/3025561 |
| fee_help | https://intercom.help/mentajp/ja/articles/3025582 |
| tokutei | https://menta.work/tokutei |
| google_signup_preference | **PREFER_GOOGLE** |
| fee_public | 特商法: メンター手数料は報酬の **20％税別**（利用15％+決済5％）。振込都度 **300円**。運用ヘルプは **22%（20%+消費税10%）** と併記。**貼る直前に公式を再読。プラン料金は書かない** |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP**（Stripe本人確認の直前） |
| draft | true |
| observed | 2026-09-16 公開 GET |

## needs_check

1. **活動** — トップ 200。プランカタログの開催日・新着は未読。活動ゲートは登録面 WAF の記録あり
2. **登録面** — この環境の `register/choose` は 200 で Google OAuth リンクあり。WAF が出たら park
3. **手数料の見え方** — 特商法20％税別 vs ヘルプ22%（税込換算）。**どちらの数字を画面が使うかはクリック時**。創作しない
4. トップの「約7,400名」「8万人」はマーケ。活動証明に使わない

完了条件は **プロフィール保存まで**。プラン提出は出品。エージェントは出品しない。

## CU handoff（この机）

やってよい（下書きのみ・後続CU）:

1. https://menta.work/index.php/register/choose 「Googleアカウントで登録する」
2. 他経路（メール / X / Facebook / Apple / Lancers）は使わない
3. 自己紹介・教えられることを貼る。**プラン名・料金は空。提出しない**
4. 設定 → 本人確認ページは開いたら閉じる

## Field map（プレースホルダ）

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| 登録経路 | Google | 必須 | |
| ユーザー名 | `{{DISPLAY_NAME}}` または英数制限に合わせる | 高 | |
| アイコン | `{{PHOTO_LOCAL_PATH}}` | 任意 | |
| 自己紹介 | 下記 200 / 800 | 必須に近い | |
| 経歴・実績 | 公開記事と公開リポジトリのみ | 高 | 受講者数を作らない |
| 教えられること | Claude Code, Codex, 自動化の始め方, 公式API投稿, 検品 | 高 | |
| 教え方 | テキスト中心、宿題を小さく切る、公開スイッチは受講者 | 高 | |
| プラン名 | このパックでは空。出品しない | STOP | |
| プラン料金 | 空 | STOP | |
| Stripe本人確認 | やらない | STOP | |
| 口座 | やらない | STOP | |

共通プレースホルダは [INDEX.md](INDEX.md)。

## JA bio 200（200字）

```
石田祐太。個人サイト「ユタラボ」（https://yutalab.dev/）で、AI自動化の手順を初心者向け日本語で公開しています。公式APIの動画投稿も扱います。ブラウザ自動操作は教えません。最初の1回を、人が確認できる形で安全に動かすところまで伴走します。公開スイッチは受講者本人が持ちます。未確認の数字は書きません。リモート可。宿題は小さく先に切ります。秘密は貼りません。必ず根拠だけ教えます。
```

## JA bio 800（800字）

```
石田祐太（Yuta Ishida）です。個人サイト「ユタラボ」（https://yutalab.dev/）で、AI自動化の手順を初心者向けの日本語で公開しています。教える範囲は、道具の入れ方から「最初の1回を安全に動かす」までです。専門用語は後回しにし、つまずきやすい場所を先に書きます。教えられること：（1）Claude Code / Codex のはじめ方と、対象ファイル・完成条件・禁止事項を入れた指示の書き方。（2）毎日の作業を自動化してよいかの見分け。秘密・公開・課金が絡む仕事は外す判断。（3）公式APIだけを使う動画投稿の考え方。ブラウザ自動操作やスクレイピングは教えません。（4）動いたあとの検品。仕様、境界値、秘密情報、権限、再現性の順に見ます。公開している教材の土台：ユタラボの実録記事と、Autopilot Log（https://github.com/rimone0511/autopilot-log）。投稿の門番は壊れても非公開側に倒れる設計です。受けないこと：代行ログイン、本人確認の代理、権利のない投稿、未確認の公開、いいね自動化。進め方はチャットまたは非同期テキストです。宿題は小さく切り、合格条件を先に合意します。公開スイッチは受講者本人が持ちます。未確認の受講者数や収益は書きません。公開記事と公開リポジトリを教材の根拠にします。秘密はチャットへ貼らず、本人の画面で入力してもらいます。レッスンはオンライン想定です。録画の外部公開はしません。課題の提出物に秘密を含めないよう、提出前チェックを宿題にします。料金と回数はプラン欄で別途示し、プロフィール本文では約束しません。初回は環境確認から始め、いきなり本番公開へ進みません。止める条件も先に書きます。画面共有なしでも進められます。質問はテキストで残します。未確認の効果は言いません。料金はプラン欄だけに書きます。
```

## STOP-AT-KYC

ここまでやってよい: Google登録、プロフィール、自己紹介。

ここで止める:

- 設定 → 本人確認ページ（Stripe）
- 銀行口座
- 出金申請
- プラン公開（出品）

公式ヘルプ: メンターへの支払いに本人確認が必要。登録パックはプロフィールで終わり。

## thin_site_skip

false。2026-09-16 に公式トップ・特商法・register/choose が 200。運営はランサーズ株式会社（特商法）。WAF は死滅証拠ではない。

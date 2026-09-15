> DRAFT-ONLY paste pack. NO secrets. NO browser signup. NO publish.
> Human paste only. Agent does not create accounts.
> `thin_site_skip: false` unless public evidence shows the product is dead.
> Stop at KYC: do not upload ID, My Number, bank, Stripe identity, or e-sign identity contracts.

# CU-23 PACK — Freelancermap

| キー | 値 |
|---|---|
| cu_serial | CU-23（QUEUE B12） |
| inventory | 01 |
| activity_gate | **pass**（この観測。PR#12 の JP 表には無い GLOBAL 机） |
| official | https://www.freelancermap.com/ |
| signup | https://www.freelancermap.com/registration |
| login | https://www.freelancermap.com/login |
| projects | https://www.freelancermap.com/projects |
| pricing | https://www.freelancermap.com/pricing/freelancer |
| help | https://www.freelancermap.com/help.html |
| terms | https://www.freelancermap.com/term-and-conditions.html |
| privacy | https://www.freelancermap.com/data-privacy.html |
| google_signup_preference | **NOT_OFFERED_OAUTH** |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP** |
| draft | true |
| observed | 2026-09-16 JST 公開 GET |
| language | English profile OK. Operator is in Japan. Do not invent a DE/EU address. |

## Google signup preference

公開の登録面（`/registration`）とログイン面（`/login`）に **Google / LinkedIn OAuth ボタンは見当たらない**。HTML 内の Google 文字列は conversion / Tag Manager だけ。

経路: メール（`{{EMAIL}}` = MAIN Google のメール）+ `{{PASSWORD_DO_NOT_STORE}}`。パスワードはリポジトリに書かない。

使わない: この仕事のためだけの新規 SNS。Premium（公開ヘルプ: 年払い換算 €13.99/月から）を買わない。Basic は 0,00 €。

## Signup steps (draft — do not run from this PR)

1. Open https://www.freelancermap.com/registration （`/register` と `/signup` は 2026-09-16 に 404）
2. Account type: **Freelancer / Agency**（Project provider は発注者。閉じる）
3. Continue。以降の項目はライブフォームを正とする（公開初面は種別ラジオのみ）
4. Stay on **Basic**（無料。公開料金表: 月 10 件の応募）。Upgrade / Premium は閉じる
5. Fill profile from the field map. Keep visibility hidden / unpublished if the UI offers it
6. STOP. Do not click profile verification. Do not apply to projects. Do not buy extra applications

## Field map（プレースホルダ）

| 画面の項目（公開情報ベース） | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| Account type | Freelancer / Agency | 必須 | 発注者を選ばない |
| Email | `{{EMAIL}}` | 必須 | MAIN Google メール |
| Password | `{{PASSWORD_DO_NOT_STORE}}` | メール経路 | コミット禁止 |
| Full name | `{{FULL_LEGAL_NAME}}` | 高 | KYC 時に一致する名前。今は身分証を出さない |
| Display / screen name | `{{DISPLAY_NAME}}` | 高 | |
| Country / city | `{{COUNTRY}}` / `{{CITY}}` | 高 | Japan でよい。偽の EU 所在は作らない |
| Tagline | 下記 Short bio | 高 | English |
| Profile / about | 下記 Long bio | 高 | |
| Skills | n8n, AI automation, API integration, technical documentation, Python, YouTube Data API, TikTok Content Posting API | 高 | 未経験を経験と書かない |
| Hourly / daily | `{{HOURLY_RATE_EUR}}` / `{{DAILY_RATE_EUR}}` | 任意〜高 | 未確認なら空 |
| Portfolio | `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}` | 任意 | |
| Availability | Remote; weekdays `{{TIMEZONE}}`; async-first | 高 | 数字の創作禁止 |
| Membership | Basic (free) | 必須 | 10 applications / month。買い足さない |

共通プレースホルダは [INDEX.md](INDEX.md)。

## EN bios (AI automation / n8n / docs seller)

### Short

```
n8n and AI automation with operator docs -- workflows you can rerun without me.
```

### Long

```
I help small teams stop copy-pasting between tools.

I build n8n workflows and light AI steps (classify, summarize, draft) that connect the tools you already use: forms, sheets, CRMs, inboxes, and internal APIs. Then I write the docs a non-engineer can follow: what the workflow does, what to do when it fails, and which values are secrets vs. safe to edit.

Typical deliverables:
- One production n8n workflow with retries and a failure alert
- A short SOP or README for the operator
- A change log so the next edit is not guesswork

Public work: Autopilot Log (https://github.com/rimone0511/autopilot-log) -- YouTube Data API v3 and TikTok Content Posting API only. Fail-closed posting gate. No browser automation.

I work in English, async, in {{TIMEZONE}}. Location: {{CITY}}, {{COUNTRY}}.

I will not:
- Automate engagement (likes, follows, fake views)
- Bypass a platform that has no official API
- Publish content on your behalf without your posting gate
- Take payment or files off freelancermap

If you need a scoped first pack -- one workflow plus docs -- start from a message on this profile after a later human publish decision. This draft does not apply to projects.
```

## STOP-AT-KYC

ここまでやってよい: 無料 Basic のアカウント作成、プロフィール下書き、スキル。

ここで止める:

- 公開ヘルプの **profile verification**（身分確認。信頼バッジ。有料割引の記述あり → 有料も買わない）
- 免許・パスポート・住所証明のアップロード
- Premium / 応募枠の追加購入
- 案件への Apply / メッセージ送信
- プロフィールを検索に出す（人が後で決める）

## DE/EU 偏り

QUEUE どおり記録する。案件タイトル例（公開 `/projects` JSON）: `EU-based freelance developer C# and VBS`、SAP / Supply Chain。日本のオペレーターでも English プロフィールは可。所在は Japan のまま。

## thin_site_skip

false。2026-09-16 に homepage 200、`/registration` 200、`/projects` 200。埋め込みプロジェクトの `created` 例: **2026-09-15T19:36:50+02:00**、**2026-09-15T18:24:49+02:00**。マーケ件数は使わない。

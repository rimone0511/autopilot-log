> DRAFT-ONLY paste pack. NO secrets. NO publish. NO KYC upload.
> Human / CU paste only. Live form wins.
> `thin_site_skip: false`
> Stop at KYC: Wallet → Add account → Persona. Morning user.
> Stay **Free** until a paying client exists. Do not buy Contra Pro.

# CU-08 PACK — Contra（Independent page）

| キー | 値 |
|---|---|
| cu_serial | CU-08（QUEUE **A8**） |
| role | **Independent / Share work**。Hire 側に入らない |
| official | https://contra.com/ |
| independents | https://contra.com/how-it-works/independents |
| pricing | https://contra.com/pricing |
| onboarding | https://help.contra.com/en/articles/9322381-onboarding-and-completing-your-profile |
| identity | https://help.contra.com/en/articles/9322955-how-to-verify-your-identity-on-contra |
| paid_projects | https://help.contra.com/en/articles/9322763-paid-projects |
| terms | https://contra.com/policies/terms |
| google_signup_preference | **PREFER_GOOGLE** |
| thin_site_skip | **false** |
| stop_at_kyc | **STOP** |
| plan | **Free** until a client. No Pro / Max |
| draft | true |

## Google / signup preference

優先: **Continue with Google** as `{{GOOGLE_ACCOUNT_EMAIL}}`（MAIN のみ）。

フォールバック: 同じ MAIN メール。OTP は親 Gmail。

使わない: 新規 SNS、Hire creative talent、Agency として別人格。

## CU 手順（Independent page, Free）

公式オンボーディング（2026-01-27 更新）:

1. https://contra.com/ — sign up。
2. **What brings you to Contra?** → **Share work**（Independent）。Hire は選ばない。
3. プロフィール写真: `{{PHOTO_LOCAL_PATH}}`（ローカル。git に置かない）。無ければスキップ可ならスキップ。
4. One-liner: 下記。
5. Create account: **Free**。**Contra Pro を契約しない**（公式: sign up for Pro *or* proceed with a free account）。Pricing は Pro `$29 / month` または `$199 / year` を出す。このパックは買わない。クライアントが付くまで Free。
6. Topics: 自動化・API・documentation に近い公式トピックだけ。無いものは作らない。
7. プロフィールを埋める（cover、公開リポジトリのリンク、rate プレースホルダ、social = ポートフォリオ / GitHub）。
8. Discoverable / public トグルがあれば **off**。公式はプロフィール完成（identity 含む）で Discoverable になると書く。この GO は Discover 完了チェックを埋めない。
9. **Verify identity & set up your wallet は開かない。** Persona に入ったら閉じて朝メモ。
10. 案件応募・invoice・payment link はしない（応募文は sibling `earn-en-proposal-drafts-20260916/`）。

Feed に Work を **投稿** するのは公開に近い。プロフィールに公開 URL を足すだけにする。4 pieces of work が必須で投稿しか無いなら、公開 GitHub / yutalab を case study 下書きまでにして **Publish to feed はしない**。詰まればプロフィール途中で完了。

## Field map（プレースホルダ）

| 画面の項目 | 貼る値 | 必須見込み | メモ |
|---|---|---|---|
| Workspace | **Share work** | 必須 | Independent page |
| Google | `{{GOOGLE_ACCOUNT_EMAIL}}` | 必須 | PREFER_GOOGLE |
| Plan | **Free** / skip Pro | 必須 | 「Free until client」 |
| Display name | `{{DISPLAY_NAME}}` | 必須 | 推奨: `Yuta Ishida` |
| Photo | `{{PHOTO_LOCAL_PATH}}` | 高 | |
| One-liner | 下記 | 必須 | |
| Location | Japan / `{{PREFECTURE}}` 相当 | 高 | 番地なし |
| Topics | Automation, APIs, documentation, 画面の最寄り | 高 | |
| Cover | 公開サイトのスクショ（秘密なし）またはスキップ | 任意 | ID 写真不可 |
| Work samples | 公開 URL のみ。feed 投稿しない | 任意〜高 | `{{PORTFOLIO_URL}}`, `{{GITHUB_REPO_AUTOPILOT}}` |
| Hourly rate | `{{HOURLY_USD}}` | 完成チェック用 | **git に実額を書かない**。空で保存できるなら空 |
| Social | `{{PORTFOLIO_URL}}` と `{{GITHUB_URL}}` | 高 | LinkedIn を新規投稿しない。既存 URL なら可 |
| Discoverable | **off** | 必須（あれば） | |
| Wallet / Add account | やらない | STOP | Persona。発行国は居住国ではない |
| Expert verification | やらない | STOP | |
| Apply to opportunity | やらない | STOP | このフォルダの外 |

## Paste — One-liner

公式例の型: 何をするか + 誰向け。連絡先なし。

```
Japan-based independent: n8n and official-API automation plus operator docs a non-engineer can follow
```

## Paste — Independent about (EN)

```
I am {{DISPLAY_NAME}} (Yuta Ishida), a Japan-based independent. I help small teams replace copy-paste with an n8n or official-API workflow plus docs a non-engineer can follow.

Public notes: {{PORTFOLIO_URL}}
API-only upload tool with a fail-closed posting gate: {{GITHUB_REPO_AUTOPILOT}}

I do not scrape, fake engagement, or move a Contra-originated project off Contra for payment. Async text in {{TIMEZONE}}. English OK.

I will not invent traffic or earnings here. Scope and stop conditions come first.
```

`{{TIMEZONE}}` はローカル台帳（例: `JST`）。git に住所を足さない。

## Paste — work sample titles (if the form needs one line)

| Sample | URL | Title line |
|---|---|---|
| 1 | `{{PORTFOLIO_URL}}` | Operator-facing notes on AI automation (Japanese, public) |
| 2 | `{{GITHUB_REPO_AUTOPILOT}}` | Autopilot Log — YouTube Data API v3 + TikTok Content Posting API, fail-closed gate |

Do not upload private videos, client files, or ID.

## Fees（発明しない）

- 登録: 公式 pricing / independents — **Join / profile is free**。
- Independent 向けに Contra は **commission-free** と書く。同時に Free プランでは **client payment fees** と processing が pricing / Paid projects に出る。
- Paid projects ヘルプ（2026-05-12）の Non-Pro 表（例: プロジェクト規模ごとの $2 … $29）は **支払いが発生したとき** の公式表。このパックは請求しないので表を転記して「今払う額」にしない。現行は https://contra.com/pricing と Paid projects を開いて確認する。
- **Pro を買って手数料を下げる操作はしない。** クライアントが付くまで Free。

## STOP-AT-KYC

ここまでやってよい: Google、Share work、Free、one-liner、topics、公開 URL、Discoverable off。

ここで止める:

- Wallet → **Add account**
- Persona（政府ID、顔、支払い口座）
- 税番号・W-8 相当を git やチャットに書くこと
- 銀行 / PayPal / crypto payout
- Contra Pro / Max のカード入力

公式: wallet には identity verification が必要。第三者は Persona。ID の国は **発行国**（居住国ではない）。別国の銀行は Airwallex とヘルプが書く — どちらも今はやらない。

## thin_site_skip

false。2026-09-15 に contra.com/pricing、Independent 向け how-it-works、onboarding / identity / paid-projects ヘルプが生存。

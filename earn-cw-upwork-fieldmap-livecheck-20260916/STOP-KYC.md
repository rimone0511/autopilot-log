> Hard stop. DRAFT_ONLY field maps do not continue past these screens. No files, no camera, no bank numbers.

# STOP — identity, tax, payout

## CrowdWorks

Open a KYC/payout screen **only** far enough to confirm the label, then close it. Do not submit.

| Label / flow (official names) | Why stop | Cite |
|---|---|---|
| 本人確認 / 本人確認書類提出 | 利用規約 第8条: 弊社所定の本人確認. Blog: マイナンバーカード可; 個人番号記載面・通知カードは対象外 | https://crowdworks.jp/pages/agreement · https://blog.crowdworks.jp/archives/5685/ · https://crowdworks-help.zendesk.com/hc/ja/articles/5006077943838 |
| デジタル認証アプリ / マイナアプリ | Blog 2026-07-14: マイナンバーカード + デジタル認証アプリ. 取得するのは氏名・住所・生年月日。マイナンバーは提供されない、と公式は書くが **this pack still does not start the app** | https://blog.crowdworks.jp/archives/6465/ |
| 振込先口座 / ゆうちょ銀行 / 個人口座 | 出金・振込手数料の公式案内。利用規約 第17条5項: 日本国内の銀行等口座 | https://crowdworks.jp/pages/guides/employee/fee · https://crowdworks.jp/pages/agreement |
| 適格請求書 / インボイス登録番号 | 利用規約 第5条 情報提供義務（適格請求書発行事業者） | https://crowdworks.jp/pages/agreement |
| クレジットカード情報 | 個人情報保護方針の取得項目に含まれる。クライアント決済側。ワーカー下書きでは触らない | https://crowdworks.jp/pages/privacy_policy |

Help index (do not walk the upload UI): 本人確認・各種手続き  
https://crowdworks-help.zendesk.com/hc/ja/sections/4987979705374

## Upwork

| Label / flow | Why stop | Cite |
|---|---|---|
| Identity verification / government ID / Visual (video or phone photo) / SMS code | Help: government-issued photo ID; 7-day window after notify; freelancers may pay 35 Connects for a badge — **do not buy Connects, do not upload ID** | https://support.upwork.com/hc/en-us/articles/360001176427-How-to-verify-your-identity-as-a-freelancer · https://support.upwork.com/hc/en-us/articles/34397755511955-Identity-verification-Frequently-asked-questions · https://support.upwork.com/hc/en-us/articles/360000563227-How-to-verify-your-identity-with-a-government-ID |
| Tax information | Help: country/residence change requires matching tax info | https://support.upwork.com/hc/en-us/articles/34397755511955-Identity-verification-Frequently-asked-questions |
| Withdrawal method / payout | Names on ID, withdrawal, and tax must match. Do not add a payout method in this pack | https://support.upwork.com/hc/en-us/articles/360001176427-How-to-verify-your-identity-as-a-freelancer |
| Phone number (verification SMS/call) | Listed as an identity-verification type | same ID article |
| Profile submit if it opens ID / vetting | Saving in-progress is OK. Submit-as-vetting is STOP | Profile essentials + ID articles above |

Park codes (secret-free): `kyc_wait` · `sms_wait_user` · `id_flow_on_photo_picker`.

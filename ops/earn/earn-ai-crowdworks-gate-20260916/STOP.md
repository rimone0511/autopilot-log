# STOP — B05 AI CrowdWorks

**DRAFT_ONLY.** This list is a stop fence, not a how-to for vendor KYC.

This authoring agent already stopped (no signup). A later human GO still stops at the same lines.

## Do not, from this folder

- Treat CU as **GO**. One-pager is **NO-GO**. Skip profile draft until the board is readable in a browser.
- Submit https://crowdworks.jp/aicw/register/new_email (email or CrowdWorks ID).
- Start Google / Yahoo / Facebook OAuth. Direct `/aicw/auth/google` is **404** this GET; do not hunt alternate auth URLs.
- Loop `/aicw/login` (login JS imports WAF protection).
- Use `/aicw/register/enable_aicw` to convert an existing CrowdWorks account from an agent.
- Hunt https://ai.crowdworks.jp/lp/pre-registration/ (301 to home). The 2026.5.14 news form is **closed**.
- Click **興味がある** / 応募 / スカウト返信. List copy: member-gated 案内.
- Open client paths: **仕事を依頼する**, 無料相談, https://crowdworks.jp/aicw/consult, Jicoo `…/cw_ai_bpo/e/aicwtop`, 仕事依頼フォーム.
- Call the public 無料相談 phone on the LP. Client desk.
- Upload 本人確認 / 身分証 / マイナンバー / 口座 (`/identification_request_top`, `/bank_account/new` exist on main CrowdWorks JS — **not opened**).
- Pay, boost, or buy membership.
- Copy main CrowdWorks **5–20%** (or any third-party %) onto this desk.
- Write marketing「10,000名」or sitemap-style counts as activity.
- Paste PR#34 JA bios into git again.
- Mix this desk with QUEUE **B5 Anycrew**, **A4 crowdworks.jp**, or **B04 CrowdLinks**.

## Allowed later (human GO only, after dated cards)

1. Email `{{EMAIL}}` or existing CW ID. MAIN mailbox. Free copy only.
2. Profile **draft**. Unpublished.
3. Close the tab.

## Placeholders (empty of secrets)

`{{EMAIL}}` `{{LEGAL_NAME_KANJI}}` `{{DISPLAY_NAME}}` `{{PORTFOLIO_URL}}` `{{GITHUB_REPO_AUTOPILOT}}`

Do not fill 希望単価 from teaser yen or category examples.

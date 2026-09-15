# STATUS — Coconala price-fill card (2026-09-16)

Snapshot: **2026-09-16** (pack authoring; live fill **not** run from this agent)  
Folder: `earn-jobs-coconala-price-fill-card-20260916/`  
State: **DRAFT_ONLY**  
After: listing DRAFTS [#79](https://github.com/rimone0511/autopilot-log/pull/79)

Forbidden here: secrets, live emails, OTP, KYC files, filled `{{PRICE_YEN}}`, invented `coconala.com/services/…`, GMV, “will earn ¥…”, competitor 相場 presented as fact.

---

## What this pack is

A **local** operator card to:

- map **paste first = 01 n8n自動化**
- offer `{{PRICE_YEN}}` **DRAFT SUGGESTION** bands (not market facts)
- save as 下書き
- wait for **human GO** before 公開する

It does not replace #79’s サービス内容.

---

## Inventory

| Item | State |
|---|---|
| #79 three listing files | Sibling DRAFT PR. Source of title/body/FAQ. Yen still tokens there |
| This card | Pack ready in git |
| Live category floor | Operator re-reads help + form. Snapshot in PRICE-BANDS is **not** frozen |
| Local `{{PRICE_YEN}}` | **Not filled from this agent** |
| 01 / 02 / 03 下書き on site | **Not claimed.** This agent did not log in |
| 公開する | **no** |
| 見積もり送信 | **no** |

---

## Paste-first (committed map)

```
paste_first: 01
then: 02 (same parent category; different offer)
last: 03 (different mid-category; re-read floor)
publish: human GO only
```

---

## Auth / KYC (secret-free)

```
auth: MAIN Google
second_account: no
coconala_login_from_this_agent: no
filled_yen_committed: no
publish: no
estimate_sent: no
payout_kyc: not this pack
boost_or_pro: no
```

---

## This PR does not

- Log into Coconala
- Click 公開する
- Send an estimate
- Commit a filled yen amount
- Scrape other listings for “the market”
- Rewrite #79 buyer-facing fences
- Touch `autopilot_log/` Python or posting-gate tests beyond running them unchanged

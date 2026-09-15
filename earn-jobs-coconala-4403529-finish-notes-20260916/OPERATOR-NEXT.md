# OPERATOR-NEXT — cover, then human GO

Listing: Coconala **4403529**  
Now: unpublished · FAQ 6 ok · estimate ON · **`image_missing`**  
This pack: **DRAFT_ONLY.** [HUMAN-GO.md](HUMAN-GO.md) is **false**.

Order matters. Do not click **公開する** to “finish the cover step.”

---

## 1. Attach cover (this is the remaining listing gap)

Public mag / news: 公開時は画像が要ることがある ([PR#90](https://github.com/rimone0511/autopilot-log/pull/90) cites news 1372). Missing image = **GO-blocker**.

Use **one original** cover that shows **what the service is** (n8n flow + 手順書), secrets cropped.

Allowed:

- Own canvas screenshot (credentials / emails / tokens cropped)
- Own 手順書 screenshot (no customer names)

Forbidden:

- n8n / Coconala / lab / xAI / Google logos as affiliation
- Another seller’s listing image
- ID / selfie / bank / invoice
- Filenames with emails or invoice numbers
- Commit the binary to this git repo

If the uploader shows a size, follow the live uploader. Do not invent px in git.

After upload: **下書きで保存する.** Confirm still unpublished. Then the image row can move off `image_missing`.

Optional while the editor is open: [TITLE-FIX.md](TITLE-FIX.md) if the heading shows ますます.

---

## 2. Do not send work from this draft

見積もり is **ON** (受付する). That is a checkbox, not a send.

- Do not 見積もりを送る / 提案する
- Do not トーク営業
- Do not LINE / Zoom / メール直

Inquiry paste lives in [#81](https://github.com/rimone0511/autopilot-log/pull/81) and stays unsent from this pack.

---

## 3. Human GO for 公開 (祐太 only, after cover)

Only after:

1. Cover attached, secrets cropped
2. Displayed title is `n8n自動化と手順書を作ります` (one ます)
3. FAQ 6 still names スクレイピング as out of scope
4. Price / estimate still as intended on the **live** form
5. Re-read https://coconala.com/pages/guide_sell and https://coconala.com/pages/guide_rule
6. Re-read category minimum-price help
7. [HUMAN-GO.md](HUMAN-GO.md) `coconala_publish_listing` is **`true` in the copy 祐太 is acting on**
8. 祐太 clicks **公開する** on the live page

This authoring agent never flips GO and never clicks 公開する.

If GO stays false: **stop after cover + 下書き保存.** That is a complete next action.

---

## Stop lights

| Screen | Action |
|---|---|
| 公開する confirm | Cancel unless step 3 is fully true |
| 本人確認 / 口座 / インボイス | Close. Slip [#43](https://github.com/rimone0511/autopilot-log/pull/43) |
| 見積もり送信 | Do not send |
| Captcha / hold | `blocked_skip`. No second account |

---

## Done when (this finish note)

Valid next outcomes:

- `image_missing` → cover attached, still unpublished, GO false
- later, **human** `already_published` — not this agent

Not done: 「エージェントが公開した」「見積もり送った」「口座登録した」.

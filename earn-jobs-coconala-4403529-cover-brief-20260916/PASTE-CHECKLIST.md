# PASTE-CHECKLIST — upload cover, then STOP

Listing: Coconala **4403529**  
Seller URL: `https://coconala.com/mypage/services/4403529`  
Desk: 仕事窓口  
Pack: `earn-jobs-coconala-4403529-cover-brief-20260916/`  
Mode: **DRAFT_ONLY.** This authoring agent does **not** drive live CU.

Goal of the **next** human or CU session: attach **one** original サービス画像 → **下書きで保存する** → confirm still unpublished → **STOP**.

Not a goal: 公開する / 見積もり送信 / KYC / Wave B/D register / 二件目の出品.

Tick on a **local** copy. Do not paste secrets back into git.

---

## 0. Hard stop (read first)

- [ ] Role = **出品者**. 仕事を依頼する側に入らない。
- [ ] MAIN Google only. Second Coconala = STOP.
- [ ] **公開する** を押さない。確認ダイアログもキャンセル。
- [ ] 見積もりを送らない。トーク営業しない。
- [ ] 本人確認・口座・インボイスが出たら **閉じる**。
- [ ] Wave B/D の新規登録を始めない。
- [ ] 出品タイトルをこのチェックリストで書き換えない（ますますだけは sibling TITLE-FIX）。
- [ ] カバー二値をこのリポジトリにコミットしない。

If the next required click publishes: **park** `no_draft_path`. Do not work around.

---

## 1. Preflight (local, no Coconala yet)

- [ ] Cover file exists locally from [COVER-BRIEF.md](COVER-BRIEF.md) (1220×1240 or live size).
- [ ] Safe-zone check: title + 受付フロー + バッジが中央 1220×1016 に入っている。
- [ ] Secrets cropped. No partner logos. No yen. No face / ID.
- [ ] Filename has no email or invoice number.
- [ ] Alt candidate picked from [ALT-TEXT.md](ALT-TEXT.md) (A1 default).
- [ ] Viewport desktop. One marketplace profile. Do not also live in Gmail in that profile.

---

## 2. Open the existing draft (do not create another)

1. MAIN Google → existing Coconala.
2. Open **exactly**: `https://coconala.com/mypage/services/4403529`  
   Fallback: 出品サービス管理 → 下書き **4403529** だけ。
3. Confirm it is **下書き / unpublished**. If the row is already **公開中**: write `already_published` locally and **stop**. Do not unpublish from an agent.
4. Confirm it is the n8n first-gig family (`n8n自動化と手順書を作ります`). If it is a different offer: **stop**. Do not upload this cover onto `02` / `03`.
5. Do **not** click 新規出品.

---

## 3. Upload サービス画像 1枚目

Guide_sell の「画像」ステップ。1枚目が検索結果。

- [ ] Find サービス画像 / イメージ画像 (live label wins).
- [ ] Upload the **one** local PNG/JPEG to **slot 1**.
- [ ] If the form asks 代替テキスト: paste [ALT-TEXT.md](ALT-TEXT.md) **A1** (or the row that matches the overlay).
- [ ] Preview: 受付フローとタイトルが切れていない。秘密が見えていない。
- [ ] Do not fill slots 2–10 this pass (no keyword spam).
- [ ] 動画 URL は空のまま。
- [ ] If the uploader rejects the file: resize / convert PNG↔JPEG locally. Do not grab a random web image.

Forbidden uploads: n8n 公式ロゴ、他セラーのサムネ、KYC、口座、顧客実データ。

---

## 4. Save 下書き — then STOP

- [ ] Click **下書きで保存する** (live label wins).
- [ ] If a dialog says the service will become **公開**: **Cancel**. That click is 公開する.
- [ ] If there is **no** 下書き保存 and only 公開する: leave the image in the form if it stays, **do not press 公開する**. Park `listing_draft_no_save_path`.
- [ ] Status still 下書き / 非公開 / 受付休止. Not 公開中 / 受付中.
- [ ] Guest must still fail: do not open / announce `coconala.com/services/4403529` as a shop.
- [ ] **STOP.** Close the tab. Do not “ついでに” FAQ・価格・公開。

Optional only if the heading shows `作りますます`: sibling [#103](https://github.com/rimone0511/autopilot-log/pull/103) TITLE-FIX, then 下書き保存 again. Still no 公開.

---

## 5. Stop lights

| Screen | Action |
|---|---|
| 公開する / この内容で公開する | **Cancel.** End of job |
| 本人確認 / 口座 / インボイス | Close. Not this pack |
| 見積もりを送る / 提案する | Do not send |
| 新規会員 / 別アカウント | STOP |
| Captcha / hold | `blocked_skip`. No second account |
| Wave B/D 登録ウィザード | Close. Wrong fanout |

---

## 6. Paste-ready CU prompt (later agent only)

This authoring agent must **not** run the block. Paste into a **future** computer-use agent that is allowed to log in.

```
Follow earn-jobs-coconala-4403529-cover-brief-20260916/ exactly.

THIS session (JOBS, DRAFT_ONLY):
  1) MAIN Google login to the existing Coconala. No second account.
  2) Open https://coconala.com/mypage/services/4403529
     (出品サービス管理 → draft 4403529). Live menu wins.
  3) Confirm unpublished 通常サービス. If 公開中: stop, already_published.
  4) Upload ONE local original cover to サービス画像 slot 1
     (from COVER-BRIEF.md; secrets cropped; no partner logos).
  5) If alt field exists: ALT-TEXT.md A1.
  6) 下書きで保存する. Confirm still unpublished.
  7) STOP. Close.

NEVER click 公開する / 出品する / 受付開始 / 見積もりを送る.
If the next required click publishes: park no_draft_path.
KYC / 口座 / インボイス: close. No uploads.
No Wave B/D register. No new listing. Do not retitle
(unless heading shows 作りますます — then TITLE-FIX from PR 103 only).
Do not open Gmail in the CU browser. OTP: parent channel, one resend max.

Success: cover_attached, listing unpublished, publish_clicked: no.
Write a secret-free session line. Do not commit the binary.
```

---

## 7. Success / park keys (secret-free)

Valid: `cover_attached_unpublished` | `image_missing` | `listing_draft_no_save_path` | `already_published` | `blocked_skip` | `kyc_wait` | `wrong_listing`.

Not success: 「公開した」「見積もり送った」「口座登録した」。

```
desk: Coconala
pack: earn-jobs-coconala-4403529-cover-brief-20260916/
listing_id_in_git: 4403529
listing: unpublished
images: cover_attached | image_missing | needs_human
alt: A1 | none-no-field | not-run
save: 下書き | no-save-path | not-run
publish_clicked: no
estimate_sent: no
kyc_opened: no
wave_bd_register: no
cu_this_authoring_agent: not-run
human_go_coconala_publish_listing: false
next: stop
```

---

## 8. Out of scope

- This markdown’s authoring agent logging in
- Flipping GO / clicking 公開する
- Wave B/D
- #79 `02` / `03` as a second live draft this sitting
- Python posting-gate edits
- Committing PNG/JPEG

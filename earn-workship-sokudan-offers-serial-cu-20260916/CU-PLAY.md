# CU-PLAY — Wave B pass ∩ PREFER_GOOGLE

Audience: computer-use serial agent. One human operator.  
Mode: **`DRAFT_ONLY`**. Timebox: **15–25 minutes per desk**.  
The agent that wrote the markdown did **not** create accounts. You may type in a browser under these rules.

Serial for **this folder only**:

```
Workship (CU-11) → SOKUDAN (CU-13) → Offers (CU-25)
```

Do not continue into Skill Shift, ITプロパートナーズ, CrowdLinks, YOUTRUST, or Wave A / C / D from here.

Paste source of truth: [POINTERS.md](POINTERS.md). Read [00-google-otp-hold.md](00-google-otp-hold.md) once. Read [STOP-KYC.md](STOP-KYC.md) once. Live form wins.

---

## 0. One-screen GO / NO-GO

| Switch | Value | If you cannot keep it |
|---|---|---|
| Account | MAIN Google `{{GOOGLE_ACCOUNT_EMAIL}}` only | STOP. No second identity. |
| Publish | `DRAFT_ONLY` | STOP. Do not toggle public / 応募 / エントリー. |
| KYC | Stop. Morning user. No uploads | Hand off. Do not continue **that** desk. Next desk is allowed after park. |
| Fees / rates | Placeholders only | Park rather than invent 円 or %. |
| Email OTP | Parent Gmail MCP | Do not open `mail.google.com` in the CU profile. |
| SMS OTP | User chat | Wait. Do not guess. |
| Press & Hold | `holdDurationMs` required | Do not fake a hold with click+sleep. |
| Secrets | Never in git / this log / screenshots | Redact. No CSRF copy-paste into the repo. |
| Signup from authoring PR | Already **no** | You are the later CU. Still no publish. |

Viewport: desktop **≥ 1280px**. Do not switch to a phone emulator mid-desk unless the site dead-ends on desktop (record it).

---

## 1. Preflight

1. One browser profile. MAIN Google picker only. Do not also open Gmail in that profile.
2. Hold: `holdDurationMs` 1800, one retry 2500. Missing schema → `tool_missing_holdDurationMs`.
3. File pickers for ID = close without a file.
4. Thick paste files (other PRs / same checkout if merged):

   | Desk | Thick file |
   |---|---|
   | Workship | `earn-waveb-cu-handoff-batch2-20260916/01-workship.md` |
   | SOKUDAN | `earn-skillshift-sokudan-menta-deep-20260916/02-sokudan.md` |
   | Offers | `earn-waveb-cu-handoff-batch2-20260916/04-offers.md` |

   If those paths are not in **this** checkout, open the blob links in [POINTERS.md](POINTERS.md). Do not invent a third bio.

You will **not**: scrape listings to apply, like, follow, message clients, open Gmail in CU, buy paid plans, or operate Autopilot Log posting.

---

## 2. MAIN Google login play (all three desks)

1. Land on the **worker / 人材 / フリーランス** signup URL in the desk card.
2. Click **Google で登録** / Google icon. Workship: confirm the icon **says Google** before click. If it does not, email fallback = same MAIN mailbox.
3. Pick **only** MAIN. If the picker shows another user, do not continue.
4. Consent: basic profile/email. Deny Gmail-read-all.
5. Already registered: **ログイン** with the same Google. Do not duplicate.
6. If you land on 企業 / client: leave. Switch to worker. If you cannot without KYC → KYC stop.

OTP: mail → parent. SMS → user chat.

---

## 3. Desk 1 — Workship (CU-11)

| | |
|---|---|
| Role | フリーランス登録。**Not** `enterprise.goworkship.com` |
| Entry | https://goworkship.com/signup |
| Help | https://goworkship.com/help/how_to/44 |
| Google | **PREFER_GOOGLE** (SNS / FirebaseUI — label at click-time) |
| Draft artifact | プロフィール・自己紹介 **下書き保存**。エントリー 0 |
| KYC stop | 前払い本人確認、契約署名の身分証、口座 |
| Do not | お祝い金フロー、成約報告、スカウト返信 |

### Steps

1. Close enterprise marketing if it hijacks the tab. Stay on `goworkship.com/signup`.
2. SNS **Google**. Fallback: メール = `{{EMAIL}}`. reCAPTCHA は人が解く。確認 URL 24時間。
3. Paste from thick PR#30 field map + JA bio 200/800. `{{YEARS_AUTOMATION_PUBLIC}}` empty if unknown. `{{HOURLY_YEN_DRAFT}}` empty or 「要相談」.
4. 招待コード empty. 顔写真 = local path only; do not commit.
5. Save profile. **Do not** エントリー.

Done codes: `done-draft` | `already_member_draft` | `kyc_wait` | `sms_wait_user` | `otp_missing` | `no_draft_path` | `hold_failed` | `oauth_overreach`.

Then: SOKUDAN.

---

## 4. Desk 2 — SOKUDAN (CU-13)

| | |
|---|---|
| Role | フリーランス・副業（`/signup/pro`）。**Not** 採用担当 / 企業 |
| Entry | https://sokudan.work/signup/pro |
| Terms | https://sokudan.work/pages/terms |
| Google | **PREFER_GOOGLE**. Ignore Facebook「推奨」 |
| Draft artifact | プロフィール・スキル・公開 URL 保存。応募 0 |
| KYC stop | 第4条 審査書類 |
| Do not | 発注者機能、マーケ「92%」を自己紹介に貼る |

### Steps

1. 「Google で登録」。Internet Explorer 不可 — use a current desktop browser.
2. Paste from thick PR#33. 規約の AI 自己紹介生成を使うなら **保存前に人が直す**。件数を足させない。
3. 職務経歴書ファイルはローカル PDF。リポジトリに置かない。必須と言われたら後回し（KYC でなければ）。
4. 応募しない。スカウト返信しない。

Then: Offers.

---

## 5. Desk 3 — Offers (CU-25)

| | |
|---|---|
| Role | **ワーカー**. Not `/client/` |
| Entry | https://offers.jp/worker/signup （`/signup` is **404**) |
| Jobs (look, don't apply) | https://offers.jp/jobs/engineer/side-job |
| Google | **PREFER_GOOGLE** 「Googleで登録する」 |
| Draft artifact | ワーカープロフィール下書き。応募 0 |
| KYC stop | 面談 ID、出金、本人確認書類 |
| Do not | 有料ブース、年収診断の必須送信が詰まったら park、カード時給を希望単価にコピー |

### Steps

1. 「Google で登録する」。GitHub 連携は公開リポジトリと一致するときだけ任意のあと。
2. Paste from thick PR#30. 業務委託意欲は画面の最寄り。転職意欲を盛らない。
3. Jobs を見ても **「登録して求人に応募する」を押さない**。
4. Save draft. Stop.

---

## 6. Session log (secret-free)

Fill [SESSION-LOG.md](SESSION-LOG.md). No OTP, no ID crops, no passwords, no CSRF.

After each desk:

```
desk: Workship | SOKUDAN | Offers
pack: earn-workship-sokudan-offers-serial-cu-20260916/<file>
auth: google-main | email-same-mailbox | already_member | blocked
otp: gmail-parent | sms-chat | none | otp_missing | sms_wait_user
kyc: none | wait-morning + type
draft_profile: yes/no
publish: no
apply: no
holdDurationMs_used: <e.g. 1800 or none>
next: SOKUDAN | Offers | stop
```

Valid outcomes: `done-draft` | `already_member_draft` | `kyc_wait` | `sms_wait_user` | `no_draft_path` | `otp_missing` | `hold_failed` | `card_wall` | `oauth_overreach`.

Not success: “応募した”, “公開した”, “本人確認済み”.

---

## 7. Prompt stub (future CU agent)

```
Follow earn-workship-sokudan-offers-serial-cu-20260916/CU-PLAY.md exactly.
Serial: Workship → SOKUDAN → Offers (Wave B pass ∩ PREFER_GOOGLE only).
MAIN Google only. DRAFT_ONLY profile save. Stop KYC. No apply.
Paste bios from thick sibling packs (POINTERS.md). Do not invent fees or a third bio.
Gmail OTP: parent Gmail MCP. Do not open Gmail in the CU browser.
SMS OTP: wait in user chat.
Press & Hold: holdDurationMs 1800, one retry 2500.
Do not sign up from the markdown-authoring PR's rules as a license to publish.
Do not open enterprise / client consoles.
Do not copy secrets into git or the session log.
```

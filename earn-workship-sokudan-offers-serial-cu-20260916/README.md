> **MAIN Google only.** Same mailbox as QUEUE / CU runbook. Placeholder `{{EMAIL}}` / `{{GOOGLE_ACCOUNT_EMAIL}}`. No second account. No `+desk@`. No Facebook / Apple / LINE / X / LinkedIn created just for this GO.
> **DRAFT_ONLY.** Profile save only. No publish, 応募, エントリー, スカウト返信, 成約報告, 公開トグル.
> **STOP-KYC.** No ID, My Number, selfie-with-ID, bank, 印鑑証明. See [STOP-KYC.md](STOP-KYC.md).
> **No secrets.** No passwords, OTP digits, phone digits, CSRF tokens, cookies, or ID images in git or session logs.
> **No invented fees.** Cite official public pages only. Missing % → `needs_check`. Marketing totals / 「○万人」are not activity proof.
> **No publish. No signup from this PR.** The agent that wrote these files did **public GET only**. It did not create accounts.

# Wave B pass serial CU-PLAY — Workship → SOKUDAN → Offers (2026-09-16)

状態: **DRAFT_ONLY** / `cu_ready` はパックと直列手順があること。**登録済みではない。**

このフォルダは Computer Use（CU）へ渡す **3机直列**。対象は JP Wave B のうち activity-gate **`pass` かつ `PREFER_GOOGLE`** の机だけ。

| この直列の順 | INDEX CU | 机 | gate (PR#12) | Google |
|---|---|---|---|---|
| 1 | CU-11 | Workship | **pass** | **PREFER_GOOGLE**（SNSアイコン。静的HTMLに Google ラベルなし → 貼る人が目視） |
| 2 | CU-13 | SOKUDAN | **pass** | **PREFER_GOOGLE**（`/users/auth/google?category=signup`） |
| 3 | CU-25 | Offers | **pass** | **PREFER_GOOGLE**（`/oauth/worker_signup/google`） |

同じ Wave B **pass** でもこの直列に **入れない**:

- Skill Shift（CU-27）— `NOT_OFFERED_OAUTH`。厚いパックは PR#33
- ITプロパートナーズ（CU-28）— `NOT_OFFERED_OAUTH` / エージェント面談。パックは PR#30

QUEUE の B1=SOKUDAN 順でもない。本番 Week2 の INDEX は **CU-11 Workship 起算**（PR#8）。このフォルダはそのうち Google 優先の pass 3机だけを、その番号順で切った **CU-PLAY**。

観測: 2026-09-16 公開 GET。ログイン Cookie なし。詳細は [METHOD.md](METHOD.md)。貼る順は [INDEX.md](INDEX.md)。手順は [CU-PLAY.md](CU-PLAY.md)。ポインタ表は [POINTERS.md](POINTERS.md)。

## 方針（固定）

1. 1机ずつ。人材／売り手入口だけ。企業コンソール（`enterprise.goworkship.com` / SOKUDAN 採用担当 / Offers `/client/`）なら閉じる。
2. **MAIN Google のみ。** ピッカーは QUEUE と同じアドレス。別アカウント禁止。
3. プロフィール・自己紹介は **下書き保存**。公開・応募・スカウト返信はしない。
4. 自己紹介 200/800 と Field map の本文は **先パックを正** とする。このフォルダへ秘密も長文バイオも複製しない。
5. Gmail OTP は親（Gmail MCP）。CU ブラウザで Gmail を開かない。
6. SMS が要る画面はユーザーチャット待ち。不在なら park して次の机へ。
7. KYC が出たらアップロードせず停止。朝の本人へ机名と画面の種類だけ。
8. 手数料％が公式ページに無いなら空 / `needs_check`。第三者ブログのマージンを貼らない。
9. Press & Hold がある画面は `holdDurationMs`（目安 1800、再試行 2500）。スキーマに無ければセッション停止。
10. ライブフォームのラベルがパックと違うときは **画面を正**。

## プレースホルダ（実値はローカル台帳。git に書かない）

共通の長い一覧は複製しない。先パック [PR#30 README](https://github.com/rimone0511/autopilot-log/blob/cursor/earn-waveb-cu-handoff-batch2-87d0/earn-waveb-cu-handoff-batch2-20260916/README.md) を正とする。この直列で使う最小セット:

- `{{GOOGLE_ACCOUNT_EMAIL}}` / `{{EMAIL}}` — MAIN Google（同じ値）
- `{{LEGAL_NAME_KANJI}}` / `{{DISPLAY_NAME}}` — 表示の推奨は先パックどおり `石田祐太`
- `{{PHONE}}` — SMS なら park。数字をログに残さない
- `{{PREFECTURE}}` `{{CITY}}` `{{BIRTH_YEAR}}` `{{BIRTH_MONTH}}` `{{BIRTH_DAY}}`
- `{{PORTFOLIO_URL}}` 公開してよい: `https://yutalab.dev/`
- `{{GITHUB_URL}}` 公開してよい: `https://github.com/rimone0511`
- `{{GITHUB_REPO_AUTOPILOT}}` `https://github.com/rimone0511/autopilot-log`
- `{{YEARS_AUTOMATION_PUBLIC}}` / `{{HOURLY_YEN_DRAFT}}` — 未確認なら空
- `{{INVITE_CODE}}` — 空でよい
- `{{PASSWORD_DO_NOT_STORE}}` — メール経路のみ。git / チャット禁止

## この PR でやらないこと

- アカウント作成、OAuth 完走、OTP 入力
- 本人確認アップロード
- 出品・応募・公開・有料プラン
- 秘密・実メール・実電話・CSRF・Cookie のコミット
- 案件数・GMV・「稼げる額」・未確認マージン％の創作
- Skill Shift / ITプロパートナーズ / Wave A / Wave C–D の直列
- Python 投稿ゲート試験の変更

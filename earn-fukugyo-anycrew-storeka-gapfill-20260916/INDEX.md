# INDEX — このフォルダの貼る順

状態: **DRAFT_ONLY**  
本番 Week2 直列は兄弟 INDEX（CU-11 Workship から）。ここはギャップ埋め 3 机だけ。

## このフォルダ内

人が公開一覧を 1 画面見られる机から。`needs_check` は見えてから。

1. [03-street-academy.md](03-street-academy.md) — CU-17。この GET では `/online/all` に開催日あり。**講座は作らない。公開しない。** 個別 `myclass` が WAF なら park。
2. [01-fukugyo-cloud.md](01-fukugyo-cloud.md) — CU-12。案件日付は未読。人が 1 件開いてから。
3. [02-anycrew.md](02-anycrew.md) — CU-15。`/offers` は SPA 空。人が 1 画面見てから。

共通: [STOP-KYC.md](STOP-KYC.md) / [CU-PROMPT.md](CU-PROMPT.md) / [METHOD.md](METHOD.md)

## Shared placeholders

Replace locally. Never commit filled values.

```
{{LEGAL_NAME_KANJI}}
{{LEGAL_NAME_KANA}}
{{DISPLAY_NAME}}
{{EMAIL}}
{{GOOGLE_ACCOUNT_EMAIL}}
{{PASSWORD_DO_NOT_STORE}}
{{PHONE}}
{{PREFECTURE}}
{{CITY}}
{{POSTAL_CODE}}
{{BIRTH_YEAR}}
{{BIRTH_MONTH}}
{{BIRTH_DAY}}
{{PHOTO_LOCAL_PATH}}
{{PORTFOLIO_URL}}
{{GITHUB_URL}}
{{GITHUB_REPO_AUTOPILOT}}
{{GENDER_FORM_VALUE}}
{{BLOCK_COMPANY_NAMES}}
{{INVITE_CODE}}
```

Suggested public URLs（すでに公開。机に打ってよい）:

- Site: `https://yutalab.dev/`
- GitHub: `https://github.com/rimone0511`
- Tooling example: `https://github.com/rimone0511/autopilot-log`

Public defaults（CU チャットに出してよい）:

| Token | Public default |
|---|---|
| `{{GOOGLE_ACCOUNT_EMAIL}}` / `{{EMAIL}}` | `rimone0511@gmail.com`（ログイン識別。受信箱の中身は秘密） |
| `{{DISPLAY_NAME}}` | `石田祐太` / `Yuta Ishida` |
| `{{PORTFOLIO_URL}}` | `https://yutalab.dev/` |
| `{{GITHUB_URL}}` | `https://github.com/rimone0511` |
| `{{GITHUB_REPO_AUTOPILOT}}` | `https://github.com/rimone0511/autopilot-log` |

Do not type a real phone, ID number, or tax ID into git.

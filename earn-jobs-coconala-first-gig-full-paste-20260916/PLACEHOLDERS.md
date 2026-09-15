# Yen and other placeholders — never commit filled values

Replace locally. Empty is safer than an invented number.

## Money (`{{YEN}}` family)

Do **not** invent a yen amount. Category marketing tables on `/categories/230` are vendor copy, not a price we set.

| Token | Where it goes | If the live form requires a number |
|---|---|---|
| `{{YEN}}` | generic alias — do not type this literal into a money field | same as the matching tier/option token |
| `{{TIER_BASIC_YEN}}` | ベーシック / プラン1 | `rate_required` |
| `{{TIER_STANDARD_YEN}}` | スタンダード / プラン2 / single サービス価格 | `rate_required` |
| `{{TIER_PREMIUM_YEN}}` | プレミアム / プラン3 | `rate_required` |
| `{{OPTION_FAST_YEN}}` | 急ぎ納品 | skip the option row |
| `{{OPTION_EXTRA_API_YEN}}` | 公式API接続 +1 | skip the option row |
| `{{OPTION_SOP_YEN}}` | 手順をSOPに厚くする | skip the option row |
| `{{OPTION_REVISION_YEN}}` | 修正 +1 | skip the option row |

If the form has **one** サービス価格 only, use `{{TIER_STANDARD_YEN}}` for that cell. Do not copy a competitor’s 20,000円.

## Identity / contact (login only; never git-fill)

```
{{GOOGLE_ACCOUNT_EMAIL}}
{{EMAIL}}
{{FULL_LEGAL_NAME}}
{{LEGAL_NAME_KANJI}}
{{LEGAL_NAME_KANA}}
{{DISPLAY_NAME}}
{{PHONE_E164}}
{{PASSWORD_DO_NOT_STORE}}
{{PROFILE_PHOTO_LOCAL_PATH}}
```

## Public defaults (safe to type on Coconala)

| Token | Public default |
|---|---|
| `{{GOOGLE_ACCOUNT_EMAIL}}` / `{{EMAIL}}` | `rimone0511@gmail.com` (login identity; inbox contents stay secret) |
| `{{DISPLAY_NAME}}` | `石田祐太` / `Yuta Ishida` |
| `{{COUNTRY}}` | `Japan` |
| `{{TIMEZONE}}` | `Asia/Tokyo` |
| `{{PORTFOLIO_URL}}` / `{{WEBSITE_URL}}` | `https://yutalab.dev/` |
| `{{GITHUB_URL}}` | `https://github.com/rimone0511` |
| `{{GITHUB_REPO_AUTOPILOT}}` | `https://github.com/rimone0511/autopilot-log` |

## Delivery days (not money — paste these numbers)

| Token meaning | Value |
|---|---|
| ベーシック 予想お届け日数 | `5` |
| スタンダード 予想お届け日数 | `7` |
| プレミアム 予想お届け日数 | `10` |
| single-price form 予想お届け日数 | `7` |

If the live form uses 要相談 instead of a number, check 要相談 **and** still write 7 in サービス内容 if a number field is hidden.

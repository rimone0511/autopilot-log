# 判定表（合成20件）

基準時刻 `as_of` = 2026-09-16T12:00:00+00:00。曖昧はすべて `needs_human`。

| ID | ねらい | 期待キュー | 主な理由 |
|---|---|---|---|
| INQ-S0-001 | きれいなフォーム | ready_for_review | VALID_UNIQUE |
| INQ-S0-002 | きれいなメール | ready_for_review | VALID_UNIQUE |
| INQ-S0-003 | 001のメール再送 | needs_human | EXACT_EMAIL_DUPLICATE |
| INQ-S0-004 | 電話メモ（メールなし） | ready_for_review | VALID_UNIQUE |
| INQ-S0-005 | 004と同じ電話 | needs_human | EXACT_PHONE_DUPLICATE |
| INQ-S0-006 | 連絡先なし | needs_human | MISSING_CONTACT |
| INQ-S0-007 | メール形式不正 | needs_human | INVALID_EMAIL |
| INQ-S0-008 | 本文空 | needs_human | MISSING_BODY |
| INQ-S0-009 | 未来日付 | needs_human | FUTURE_RECEIVED_AT |
| INQ-S0-010 | 返金 | needs_human | RISK_KEYWORD |
| INQ-S0-011 | 本文が挨拶だけ | needs_human | UNCLEAR_INTENT / BODY_TOO_SHORT |
| INQ-S0-012 | 弁護士 | needs_human | RISK_KEYWORD |
| INQ-S0-013 | 未知チャネル fax | needs_human | UNKNOWN_CHANNEL |
| INQ-S0-014 | 名前なし | needs_human | MISSING_NAME |
| INQ-S0-015 | 002に近い本文・別人連絡先 | needs_human | AMBIGUOUS_SIMILARITY |
| INQ-S0-016 | きれいなチャット | ready_for_review | VALID_UNIQUE |
| INQ-S0-017 | きれいな資料請求 | ready_for_review | VALID_UNIQUE |
| INQ-S0-018 | 017と同じ氏名+会社・別連絡先 | needs_human | AMBIGUOUS_IDENTITY |
| INQ-S0-019 | 電話のみ・別件 | ready_for_review | VALID_UNIQUE |
| INQ-S0-020 | 001の続き | needs_human | EXACT_EMAIL_DUPLICATE |

`ready_for_review` も送信しない。人が見てから動く。

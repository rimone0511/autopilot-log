# Mail ops

Cross-agent **mail-sort current location**. Not the Windows ledger canonical.

| Path | Role |
|---|---|
| [`shared-progress.json`](./shared-progress.json) | Shared progress box (grok-bot / claude-code / Codex / Cursor Grok / Devin). |
| `mail-ledger-reference` | **Read-only** ledger snapshot. Do not write. Do not treat as settlement. Windows ledger remains canonical. |
| [`RULE-v1.md`](../policy/mail-shared-progress-20260916/RULE-v1.md) | Policy (when to update, de-dupe, prohibitions). |

## Must

1. **Read before any sort** (ad-hoc skill or scheduled digest).
2. **Write after** (`last_run`, `reported_open_items`, `processed_message_ids` — cap 200 newest).
3. **Unchanged fingerprint → do not re-ask the user** in いま動くこと / 本人判断. Put 変化なし in result only.
4. **報告済み ≠ 決着.** This file is report state, not ledger close.
5. **No secrets** (passwords, OTP, full card numbers, address bodies).

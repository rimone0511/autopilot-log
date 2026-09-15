> **DRAFT_ONLY.** Bookmark reuse notes for a human. This agent does not call the X API. It does not list, add, or remove bookmarks. It does not post, like, follow, or DM. No secrets.

# X bookmark reuse notes — AI-agent earn leads (keep vs junk)

Date label: **2026-09-16**. This folder is a **form**, not a scan. It does not contain live bookmark rows, hit counts, or GMV.

Sort policy is the sibling pack [earn-ops PR #27](https://github.com/rimone0511/autopilot-log/pull/27) (`keep_queue` / `park` / `skip`). This pack turns that policy into **reuse notes** for posts a person already bookmarked: **keep** (still a lead this desk might answer) vs **junk** (do not reuse as outreach).

| File | Role |
|---|---|
| [`RUBRIC.md`](RUBRIC.md) | Fail-closed keep vs junk. Maps PR #27 gates. Bookmark-specific stale / filled / duplicate rules |
| [`TEMPLATE.md`](TEMPLATE.md) | One blank note + two fictional filled examples. Copy per bookmark. No full post text |

## This desk (same as PR #27)

Japan solo (YutaLab / Autopilot Log). Automation a person can stop.

- n8n / Make / Zapier + runbooks
- Official posting APIs only (YouTube unattended; TikTok default = inbox. No browser posting)
- Claude Code / Codex tickets, inspect, regression
- GAS / spreadsheet ops
- MCP wiring that can be checked. No unverified “% lift”

## What a person does / what this PR does not

**Person:** open **their own** X bookmarks UI (already logged in). For each visible post, fill one [`TEMPLATE.md`](TEMPLATE.md) block using [`RUBRIC.md`](RUBRIC.md). Keep notes in a private scratch file if they hold permalinks; git only gets redacted 1-liners.

**This PR does not:** X API (including bookmark list / folder / unbookmark), unbookmark instructions, posting, bulk DM, scraping, Bearer/cookies, inventing rows, lifting draft, marketplace send, KYC upload.

Junk in a note **does not** mean “delete the bookmark.” The bookmark stays until a person later taps it by hand, if they want. This pack never says to bulk-unbookmark.

## Verification

Markdown only. Existing posting-gate tests are unchanged. This authoring agent did not call any tool in the X namespace.

# DOCS-CHECK — fetch date 2026-09-16

All URLs fetched via WebFetch on 2026-09-16. Quotes are paraphrased summaries of content actually returned; not invented. Status: **OK** unless noted.

---

## 1. https://code.claude.com/docs/en/prompt-caching — **OK**

**Summary (fetched):**
- Claude Code manages prompt caching; exact prefix match; layers: system → project context → conversation.
- Invalidates: model switch, effort change (except Fable 5.1 + API key/subscription path), fast mode first enable, MCP tool defs in prefix, plugins (MCP case), deny whole tools (when not deferred), `/compact`, many images, CC upgrade.
- Keeps cache: file edits, CLAUDE.md mid-session (but not applied until clear/compact/restart), permission mode, skills, `/recap`, rewind, **spawning a subagent**.
- **TTL buckets:** Main conversation vs “everything else” (subagents, workflows, teammates, forks, compaction, titles).
  - Subscription within plan usage: main **1h**; everything else **5m** (except some server-controlled helpers).
  - Usage credits / API key / cloud: both buckets default **5m**.
- Overrides (v2.1.242+): `promptCacheTtl` / `CLAUDE_CODE_PROMPT_CACHE_TTL`; `subagentPromptCacheTtl` / `CLAUDE_CODE_SUBAGENT_PROMPT_CACHE_TTL` (`5m`|`1h` only).
- Per-subagent `experimental.cacheTtl` in frontmatter (v2.1.248+); ignored `1h` while on usage credits.
- Precedence: FORCE_5M → env → setting → experimental.cacheTtl (subagent) → ENABLE_1H → default.
- Subagent first request does **not** read parent cache; fork can.
- Verify TTL writes via `usage.cache_creation` (`ephemeral_1h_input_tokens` vs `ephemeral_5m_input_tokens`).

---

## 2. https://code.claude.com/docs/en/sub-agents — **OK**

**Summary (fetched):**
- Subagents = own context, system prompt, tools; return summary to parent.
- Frontmatter includes `experimental.cacheTtl: 5m|1h` (map under `experimental`, not top-level).
- Model order: invocation → frontmatter → `CLAUDE_CODE_SUBAGENT_MODEL` → parent.
- Nested depth default 3; concurrent limit default 20.
- Auto-compaction applies to subagents; `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` applies.
- Fork inherits parent prefix/cache; non-fork starts fresh.

---

## 3. https://code.claude.com/docs/en/settings — **OK**

**Summary (fetched):**
- Files: `~/.claude/settings.json` (user), `.claude/settings.json` (shared), `.claude/settings.local.json` (local), managed.
- Precedence (high→low): Managed → CLI `--settings`/flags → local → project → user.
- Lists merge; some keys session-start only (`model` mid-session via `/model`).
- Confirm with `/status` Setting sources; `claude doctor` for rejects.

---

## 4. https://code.claude.com/docs/en/context-window — **OK**

**Summary (fetched):**
- Interactive timeline of what fills context; subagent keeps large reads out of parent.
- Compaction reloads CLAUDE.md / auto memory / plan from disk; re-reads up to 5 recent files; skills re-injected with caps.
- Fable / Sonnet 5 / Opus 4.6+ support **1M** context where plan allows (`[1m]` variants; Sonnet 5 has 1M without `[1m]` picker in some cases).
- `/autocompact`, `/compact`, `/clear`, delegate to subagents.

---

## 5. https://code.claude.com/docs/en/hooks — **OK** (large page; key bits)

**Summary (fetched):**
- Lifecycle hooks: SessionStart/End, UserPromptSubmit, Pre/PostToolUse, SubagentStart/Stop, **PreCompact / PostCompact**, Stop, Notification (`idle_prompt` matcher exists), etc.
- Hooks run commands/HTTP/MCP/prompt/agent; can block some events.
- **Important for idle design:** a hook that only *records* “40 minutes later” does not by itself wake an idle model. PreCompact fires before compaction once compaction is triggered.
- SessionStart on resume may include `prompt_cache_likely_expired`, `seconds_since_last_response`, `estimated_cache_write_usd` (v2.1.251+) — useful for clock A diagnostics.

---

## 6. https://code.claude.com/docs/en/scheduled-tasks — **OK**

**Summary (fetched):**
- `/loop` and CronCreate/List/Delete: **session-scoped**; need open session; restored on `--resume` with exceptions (self-paced `/loop` not restored).
- Min interval 1 minute; 7-day expiry for recurring; jitter.
- Alternatives: Cloud Routines (min 1h), Desktop scheduled tasks (machine on, no open session required), GitHub Actions.
- Disable: `CLAUDE_CODE_DISABLE_CRON=1`.
- **Implication:** parent idle ~40min candidate needs a scheduler that can actually invoke compact on the **same** parent session (or Desktop/Routines path), not blank keepalive text alone.

---

## 7. https://platform.claude.com/docs/en/build-with-claude/prompt-caching — **OK**

**Summary (fetched):**
- Default TTL 5m; optional `ttl: "1h"`; lifetime from **start** of write/read request (streaming eats TTL).
- Pricing: Fable 5.1 cache read **$0.25/MTok** (0.025× of $10 base); 5m write 1.25×; 1h write 2×.
- Min cacheable prefix 512 for Fable 5.1 / Opus 5 / etc. (platform-dependent table).
- Exact prefix; tools→system→messages hierarchy.

---

## 8. https://developers.openai.com/api/docs/guides/prompt-caching — **OK**

**Summary (fetched):**
- GPT-5.6+: `prompt_cache_options.ttl` only supported value **`30m`** (default); write 1.25×, read 0.1×; min 1024 visible tokens.
- Earlier models: `prompt_cache_retention` `in_memory` / `24h`.
- Agents API same caching behavior; session ≠ guaranteed hit.
- Compaction / tool / effort / verbosity changes can break prefix.

---

## 9. https://developers.openai.com/api/docs/guides/compaction — **OK**

**Summary (fetched):**
- Server-side: `context_management` with `compact_threshold` on Responses create; emits opaque compaction item.
- Standalone `/responses/compact` for explicit control.
- Examples use thresholds like `200_000`.
- Compaction item not human-interpretable; do not prune compact endpoint output.

---

## 10. https://developers.openai.com/codex/config-reference — **OK**

**Summary (fetched):**
- `model_auto_compact_token_limit` (number): threshold for automatic history compaction.
- `model_auto_compact_token_limit_scope`: `total` (default) | `body_after_prefix`.
- `model_context_window` (number): tokens available to active model.
- Agents: `default_subagent_model`, `default_subagent_reasoning_effort`.
- Hooks feature optional; PreCompact/PostCompact named in hooks schema.

---

## Fetch failures

None of the 10 requested URLs returned 404/blocked on this pass. All **OK**.

*(BRIEF also listed monitoring-usage, Fable overview, app-server — not in the required write list; not fetched for this file.)*

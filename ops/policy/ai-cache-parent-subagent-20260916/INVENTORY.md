# INVENTORY — AI-CACHE-PARENT-SUBAGENT-20260916 / R3

**Collected:** 2026-09-16 ~00:00–00:15 UTC (= 2026-09-16 ~09:00–09:15 JST)  
**Scope:** Read-only. No settings applied. No secrets/values.  
**Hosts:** Cursor box (`/home/box`) + registered PC `DESKTOP-EVCBN4H` (connected).

Labels: **OBSERVED** = read on this pass · **FROM_PUBLIC_DOC** = official docs fetched 2026-09-16 · **UNVERIFIED** = not confirmed on this pass / status says read elsewhere.

---

## 1. Claude Code

| Fact | Box | User PC (`DESKTOP-EVCBN4H`) | Label |
|---|---|---|---|
| CLI version | `2.1.270 (Claude Code)` | `2.1.260 (Claude Code)` (`claude.exe` ProductVersion 2.1.260.0) | OBSERVED |
| Binary path | `/home/box/.local/bin/claude` | `%USERPROFILE%\.local\bin\claude.exe` | OBSERVED |
| `~/.claude/settings.json` | **Absent** | **Present** (~7.6 KB) | OBSERVED |
| `~/.claude/settings.local.json` | Absent | Absent | OBSERVED |
| `~/.claude.json` | Present (runtime/state) | Present (large) | OBSERVED |
| `~/.claude/agents/` | Absent | Absent | OBSERVED |
| Auth *type* | OAuth / Claude.ai subscription path (`claudeAiOauth` present; `ANTHROPIC_API_KEY` env **false**; `billingType=stripe_subscription`; `hasExtraUsageEnabled=false`; `cachedExtraUsageDisabledReason=org_level_disabled`) | Same pattern: OAuth present; API key env not checked via dump; `billingType=stripe_subscription`; `hasExtraUsageEnabled=false`; extra usage org-disabled | OBSERVED (booleans/types only; no secret values) |
| Default model (settings) | No user `settings.json` → session defaults **UNVERIFIED** | `model = "opus[1m]"` | OBSERVED (PC) / UNVERIFIED (box session default) |
| Effort | Not in box settings file | `effortLevel = "high"`; `modelSettings`: opus-5 high, fable-5-1 high, sonnet-5 medium | OBSERVED (PC) |
| Model IDs visible (cache, no secrets) | `additionalModelOptionsCache` includes `claude-fable-5-1[1m]` | Same Fable `[1m]` option cached | OBSERVED |
| `promptCacheTtl` / `subagentPromptCacheTtl` | Not set in files (no settings.json) | **undefined** in settings.json (defaults apply) | OBSERVED |
| TTL defaults if unset | Subscription within plan: main **1h**; subagents/"everything else" **5m**. Overrides: settings/env/`experimental.cacheTtl` (v2.1.242+ / v2.1.248+) | same | FROM_PUBLIC_DOC |

### Claude settings precedence (findable)

From docs (settings page, fetched 2026-09-16):

1. Managed  
2. CLI `--settings` / flags  
3. Project local `.claude/settings.local.json`  
4. Shared project `.claude/settings.json`  
5. User `~/.claude/settings.json`  

Env vars are **not** a single stack level; paired per-key.  
**Label:** FROM_PUBLIC_DOC

Paths on box: `/home/box/.claude/`, `/home/box/.claude.json`  
Paths on PC: `%USERPROFILE%\.claude\`, `%USERPROFILE%\.claude.json`  
**Label:** OBSERVED

---

## 2. Codex

| Fact | Box | User PC | Label |
|---|---|---|---|
| CLI version | `codex-cli 0.154.0` | `codex` **not in PATH** this pass; version on PC **UNVERIFIED** (models_cache on box says client_version 0.154.0) | OBSERVED / UNVERIFIED |
| Binary | `/home/box/.local/bin/codex` | Not resolved via `Get-Command` | OBSERVED |
| `~/.codex/config.toml` | Present; **only** `[projects."…"].trust_level = "trusted"` entries (no model / compact keys) | Present (~77 KB); includes model + context keys (below) | OBSERVED |
| Auth *type* | `auth_mode = chatgpt`; `OPENAI_API_KEY` **null/absent**; `tokens` object **present** (OAuth-style ChatGPT login) | Same: `auth_mode=chatgpt`; API key absent; tokens present | OBSERVED (type/presence only) |
| Active model (config) | Not set in config.toml | `model = "gpt-5.6-luna"`; `model_reasoning_effort = "low"` | OBSERVED (PC) |
| Context window override | Not set | `model_context_window = 872000` | OBSERVED (PC) — aligns with user report ~870K |
| Auto-compact threshold | Not set | **`model_auto_compact_token_limit` not present** in scanned lines | OBSERVED (absent) |
| Subagent defaults | Not set | `default_subagent_model = "gpt-5.6-sol"`; `default_subagent_reasoning_effort = "high"` | OBSERVED (PC) |
| Catalog model IDs (box `models_cache.json`) | `gpt-6-astra`, `gpt-reserve`, `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5.5`, `gpt-5.3-codex-spark`, `codex-auto-review` | — | OBSERVED |
| Catalog windows (box cache) | Most 5.6+/astra: `context_window=272000`, `max_context_window=872000`; gpt-5.5: 272000/272000; spark: 128000 | — | OBSERVED |

### Codex config precedence (docs)

User `~/.codex/config.toml` + trusted project `.codex/config.toml`; profiles `$CODEX_HOME/profile-name.config.toml`. Project-scoped cannot override provider/auth/telemetry keys.  
**Label:** FROM_PUBLIC_DOC (`https://developers.openai.com/codex/config-reference`)

Relevant keys for this case (docs):  
`model_auto_compact_token_limit`, `model_auto_compact_token_limit_scope` (`total` \| `body_after_prefix`), `model_context_window`.  
**Label:** FROM_PUBLIC_DOC

---

## 3. Related assets found (no invent)

| Asset | Location | Label |
|---|---|---|
| BRIEF R3 | `…/ai-cache-parent-subagent-20260916/BRIEF-R3-full.md` | OBSERVED |
| cache-facts | `…/fable-supervisor-orch-20260915/research/cache-facts.md` | OBSERVED |
| PRO_CONTEXT.md | `rimone0511/codex-general` default branch (fetched via `gh api`, 2026-09-16) — R5 connection-check policy | OBSERVED |
| Case events (GitHub) | `pro-chat/events/AI-CACHE-PARENT-SUBAGENT-20260916/` (3 events) + artifact brief | OBSERVED |
| Related orch case | `pro-chat/events/GROK-FABLE-SUPERVISOR-ORCH-20260915/` + local `ops/policy/fable-supervisor-orch-20260915/` | OBSERVED |
| `autopilot-log` named path | **Not found** as a case log for these IDs; repo has `codex-home/skills/codex-autopilot` (unrelated skill) | OBSERVED (absence) |

### GitHub event index (links only; bodies summarized in DESIGN / STATUS)

- `pro-chat/events/AI-CACHE-PARENT-SUBAGENT-20260916/20260916T075553+0900_discussion-cache-parent-subagent-v1.json`
- `pro-chat/events/AI-CACHE-PARENT-SUBAGENT-20260916/20260916T081100+0900_discussion-cache-keepalive-fork-v2.json`
- `pro-chat/events/AI-CACHE-PARENT-SUBAGENT-20260916/20260916T083815+0900_proposal-cache-context-grok-r3.json`
- `pro-chat/artifacts/AI-CACHE-PARENT-SUBAGENT-20260916/grok-cache-context-brief-r3.md`
- `pro-chat/events/GROK-FABLE-SUPERVISOR-ORCH-20260915/20260916T001200+0900_artifact-design-v1.json`

---

## 4. Gaps / blockers for inventory

1. PC Codex CLI version not on PATH this pass → **UNVERIFIED**.  
2. Box Claude has no `settings.json` → effort/model for interactive sessions on box **UNVERIFIED**.  
3. Whether a given “child” is in-process subagent (5m bucket) vs separate Claude Code main process (may get 1h) is **role-dependent** — must inspect spawn path per worker (**UNVERIFIED** per worker).  
4. No live cache hit telemetry (`/usage`, `cache_creation` breakdown) collected this pass — **UNVERIFIED**.  
5. Subscription quota burn under 1h writes vs 5m — not measured; API price ratios ≠ Max plan (**FROM_PUBLIC_DOC** caveat).

---

## 5. Safety note

No API keys, tokens, emails, UUIDs, or credential values recorded above. Auth reported as type/boolean presence only.

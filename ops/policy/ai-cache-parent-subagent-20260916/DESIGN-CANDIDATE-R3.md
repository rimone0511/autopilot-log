# DESIGN-CANDIDATE-R3 — AI-CACHE-PARENT-SUBAGENT-20260916

**Edition:** GROK-CACHE-CONTEXT-20260916-R3  
**Status:** **CANDIDATE ONLY** — not adopted, not applied globally, no standing processes enabled.  
**Auth constraints:** Claude = subscription path only (no usage credits / API spend / auto top-up). Codex = existing ChatGPT auth only.

Sources used this pass:
- Local: `BRIEF-R3-full.md`, `fable-supervisor-orch-20260915/research/cache-facts.md`
- GitHub: `rimone0511/codex-general` `PRO_CONTEXT.md` (R5) + case events (fetched)
- Inventory: `INVENTORY.md` (box + PC)
- Docs: `DOCS-CHECK-20260916.md`

---

## Separation of claims

### 本人希望 (owner intent)

- Explore Fable 5.1 as long-context **parent/supervisor**; Astra/Sol/Terra/Luna as scoped **children** — **not** fixed for all jobs.
- Codex context reported expanded ~270K → ~870K; do not treat report alone as verified key/scope.
- Want child auto-compact ~**200K**; parent keeps needed context; before long idle, compact while cache still warm.
- Do **not** make the user manage leave time / compact by hand.
- Candidate idle preprocessing ≈ **40 minutes**.
- Claude subscription only; no paid API / usage credits / auto top-up.
- Codex stay on existing auth.

### AI提案 (this R3 candidate — not deployed)

See §Minimal diffs below. Prefer per-agent Claude `experimental.cacheTtl: "1h"` for long-gap kids; keep 5m for short kids; avoid blanket `subagentPromptCacheTtl`. Codex child trial: `model_auto_compact_token_limit = 200000` + `scope = "total"`; do **not** force `model_context_window = 270000`. Parent idle: ~40min via real scheduler that can invoke compact — no blank keepalive; clocks A vs B; child→parent short deltas.

### 公開仕様 (from docs fetched 2026-09-16)

- Claude Code TTL buckets; subagent default 5m; per-agent `experimental.cacheTtl` / bucket overrides; Fable 5.1 API cache read 0.025×; 1h write 2×.
- OpenAI GPT-5.6+ prompt cache min **30m**; Codex keys for auto-compact + context window.
- `/loop`/cron session-scoped; Desktop/Routines for durable schedules; PreCompact/PostCompact hooks exist but do not alone wake idle sessions.

### 実機未確認 (this pass)

- Live cache hit ratios / `ephemeral_1h` vs `5m` writes on PC Claude children.
- Whether each “child” is in-process subagent vs separate Claude main process.
- Codex PC CLI version (not on PATH); whether any profile already sets auto-compact.
- That a Desktop/`/loop`/Cron path can invoke **compact on the exact parent Fable session** after ~40m idle.
- Subscription quota equivalence of API 0.025× (not claimed).
- End-to-end 200K compact completion (not just config accept).

---

## Observed baseline (PC, critical)

| Item | Value | Label |
|---|---|---|
| Claude Code | 2.1.260 (≥ 2.1.248 → per-agent cacheTtl available) | OBSERVED |
| Claude model/effort | `opus[1m]`, effort high; Fable 5.1 effort high in modelSettings | OBSERVED |
| Claude TTL overrides | unset → defaults | OBSERVED |
| Claude auth | subscription OAuth; extra usage org-disabled | OBSERVED |
| Codex model | `gpt-5.6-luna`, effort low | OBSERVED |
| Codex `model_context_window` | **872000** | OBSERVED |
| Codex auto-compact limit | **not set** | OBSERVED |
| Codex default subagent | `gpt-5.6-sol` / effort high | OBSERVED |
| Codex auth | chatgpt tokens; no API key | OBSERVED |
| Box Claude | 2.1.270; no settings.json | OBSERVED |
| Box Codex | 0.154.0; trust-only config | OBSERVED |

---

## Recommended MINIMAL diffs (candidates only)

### A. Claude child TTL — prefer per-agent

**Do (candidate):** For workers that routinely idle **>5m** then resume same history (long tests, external waits), add only to those agent markdown files:

```yaml
experimental:
  cacheTtl: "1h"
```

**Keep:** Short / bursty kids on default **5m** (lower write premium when gaps never exceed 5m).

**Do not yet:** Blanket `subagentPromptCacheTtl: "1h"` (or env) — docs say that bucket covers subagents **and** other non-main requests (workflows, teammates, forks, compaction helpers, titles). Wider blast radius.

**Preconditions:** Claude ≥ 2.1.248 (PC 2.1.260 OK); stay within subscription included usage (1h ignored under usage credits — PC has extra usage disabled).  
**Verify:** On a long-gap child request, inspect `usage.cache_creation.ephemeral_1h_input_tokens` vs `ephemeral_5m_*`, then a same-prefix hit after >5m and <1h.

### B. Codex child compact — 200K total trial

**Do (candidate):** In the **child-scoped** config layer that only those Codex child sessions load (profile / trusted project / agent `config_file` — pick one existing mechanism; do not change user-global unless isolated):

```toml
model_auto_compact_token_limit = 200000
model_auto_compact_token_limit_scope = "total"
```

**Do not:** Force `model_context_window = 270000`. PC already has **872000**; shrinking window globally would fight the owner’s expansion report and catalog `max_context_window`.

**Compare later:** remove mistaken window overrides vs keep window + only lower compact threshold.

**Verify:** Compact **starts and completes**; measure active context before/after — not “config accepted.”

### C. Parent Fable idle — ~40min candidate

**Clocks (must distinguish):**
- **A — last cache touch:** start time of last parent request that read/wrote the reusable prefix (docs: TTL from request **start**).
- **B — real activity:** last user input / meaningful work / authorized progress.  
  Blank keepalive, queue enqueue, child activity alone ≠ update A or B incorrectly.

**Do (candidate):** Use a **real scheduler** that can trigger an actual model call or formal `/compact` (or product compact) on the **same parent session**:
- Prefer existing Desktop scheduled task / session Cron/`/loop` **only if** confirmed to fire while parent session exists and can run compact once.
- On “休止可能”: A ≥ ~40m, no B activity, safe boundary, cache still warm → save handoff → **one** compact → mark idle; **no** keepalive loop after.

**Do not:** Blank “A” / one-character pings every 40m (still burns long cached input on each parent call).  
**Do not:** Rely on hook text “after 40m” without an invoker.  
**Do not:** Treat `/goal`/`/loop` as sole insurance without verifying fire conditions.

### D. Child → parent short delta reports

Child receives: goal, done criteria, forbid list, auth scope, material refs+versions, open questions — **not** full parent history.

Parent receives **only on change**, short:

`done / remaining / blockers / decisions needed / artifact refs+versions`

No giant child logs / opaque compact blobs into Fable. Aggregate trivial updates mechanically when possible.

---

## Rejected options (+ why)

| Option | Why rejected (candidate stage) |
|---|---|
| Blanket `subagentPromptCacheTtl: "1h"` | Affects entire non-main bucket; write premium on short jobs; harder to revert selectively |
| Force all Claude kids to 1h | Short kids pay 2× writes for unused TTL |
| Force `model_context_window = 270000` | Contradicts OBSERVED 872000; hurts large-source compare jobs |
| 40m blank keepalive / single-char ping | Updates A at cost of full prefix cache read; not “free”; BRIEF rejects |
| LLM-as-clock (Luna timer) | Prefer ordinary scheduler; wastes model; unreliable |
| Assume role name “child” ⇒ 5m TTL | External Claude process may be its own **main** conversation (1h on subscription) |
| Treat API 0.025× as Max-plan 40× | Quota mechanics undocumented as exact ratio |
| 1M dummy burn to “prove” cache | Forbidden by BRIEF; use small isolated tests |
| Auto-enable standing monitors / new daemons | Outside authorization |
| Switch Claude to API key / usage credits for 1h tests | Violates subscription-only |
| Mint new OpenAI API key for Codex | Violates existing-auth-only |

---

## Isolated test plan (no 1M dummy burn)

1. **Config load check (dry):** Confirm which agent file / Codex profile a trial child actually reads; record version + auth type.  
2. **Claude TTL micro-test:** One custom agent with `experimental.cacheTtl: "1h"` vs twin without; two turns with gap ~8–15m on a **small** stable prefix; compare `ephemeral_1h` vs `5m` write fields and second-turn `cache_read`. Stop after evidence — no marathon.  
3. **Codex compact micro-test:** Isolated project/profile with `200000`/`total`; drive context with **modest** repeated tool output until compact fires; confirm completion + before/after sizes. Optionally first prove mechanism with a **lower temporary** threshold, then retest near 200K once.  
4. **Parent idle path dry-run:** Document which scheduler can call compact on a **test** parent session; fire once; confirm no second fire; confirm blank ping not used.  
5. **Delta report check:** Child returns only the short template; parent context growth measured.  
6. **Safety cases:** concurrent child result during compact; sleep/offline; rate-limit — expect fail-safe stop, no infinite retry.  
7. **Record:** FACT vs UNVERIFIED; never claim savings % without measurements.

---

## Revert path

| Change | Revert |
|---|---|
| Per-agent `experimental.cacheTtl` | Delete the `experimental` map from those agent files; restart or wait for agent reload |
| Trial Codex compact keys | Remove the two keys from the **same** child-scoped file; leave global 872000 untouched |
| Scheduler / one-shot compact job | Disable/delete that task only; do not leave `/loop` running |
| Any accidental global TTL | Restore previous settings.json / unset env; confirm with `/status` + a probe request’s cache_creation fields |

No global “apply all” switch was recommended; revert stays file-local.

---

## Ops that need EXTRA auth

| Op | Why extra |
|---|---|
| Enabling usage credits / API key on Claude | Spend path; forbidden without new owner auth |
| Cloud Routines / org managed settings | May need org admin / billing |
| Changing PC user-global Codex `model_context_window` or default model for all projects | Cross-case impact — needs explicit adopt |
| Turning on standing Desktop always-on agent / new daemon | Standing process |
| Publishing customer-facing or paid actions | Outside internal design auth |
| GitHub write of adopted settings as “live” | Separate from design candidate; R5 says save≠apply |

**Allowed under current auth:** read inventory, design docs, isolated non-spend probes on subscription/ChatGPT paths, prepare patches for later approval.

---

## Linkage to PRO_CONTEXT R5 / prior cases

- **R5:** On case resume / meaningful change, verify GitHub connection + unread diffs yourself; backfill gaps; don’t invent unread docs; don’t ping user to re-explain. This inventory+design pass fetched PRO_CONTEXT + listed events — **detected**; parent **recognized/held** for Claude/Codex remains their own duty.
- **Prior discussions (v1/v2):** Corrected by R3 — TTL≠role name; no keepalive-only optimization; prefer selective 1h; 200K total trial; 40m warm compact candidate.
- **GROK-FABLE-SUPERVISOR-ORCH-20260915:** Local research `cache-facts.md` + GitHub artifact-design-v1 connected; orchestration “bake-in” not executed here.

---

## One-screen owner summary (non-technical)

候補だけです。今は設定を変えていません。  
子Claudeは「待ちが長い子だけ1時間キャッシュ」、短い子は5分のままがおすすめです。Codex子は窓を切らず、圧縮の開始を約20万トークンにする試験。親は約40分あいたら本物のタイマーで一度だけ要約圧縮（空打ち延長はしない）。効果は小さな試験で確認してから、別途許可で入れる想定です。

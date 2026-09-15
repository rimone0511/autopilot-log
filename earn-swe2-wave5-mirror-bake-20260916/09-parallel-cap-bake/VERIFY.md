> DRAFT / not production-applied. Fixed 10/10 is **not** the bake.

# Verify notes — adaptive PARALLEL-CAP-PERF window

Mirror-bake: 2026-09-16. Pro case **PARALLEL-CAP-PERF**: sibling HANDS recovered (full text not pasted here).

## Token audit (this tree)

| Knob | Must be | Found in APPLY-WINDOW |
|---|---|---|
| shared cap (Grok × SWE-2) | `{{UNKNOWN}}` until live observation | yes |
| max Cursor Grok | `{{UNKNOWN}}` (follows shared) | yes |
| max SWE-2 | `{{UNKNOWN}}` (follows shared) | yes |
| old ~10/~10 | `{{LEGACY_UNVERIFIED}}` migration boundary only | yes |
| CU | **1 always** | yes |
| refill-on-empty | `{{ADAPTIVE}}` (no fixed N) | yes |
| `{{PRO_NUMBER}}` leftovers | **0** | none in APPLY-WINDOW |

Do **not** write 10 or 15 into the max column because they are “nearby.” G1 does not prove 15 concurrent.

## Adaptive lanes (Pro; do not invent step sizes)

| Lane | Allowed |
|---|---|
| **GREEN** | time ratio **<= 1.10** AND quality pass AND no RL/stall/resource/acceptance regression → may **trial +1** on **shared** cap. **Not** on CU |
| **YELLOW** | stop growth |
| **RED** | lower the **affected** resource cap. **Width not in Pro → do not invent** |
| **HARD** | close the affected op |

Also locked: shared cross-model caps, **one** reconcile function, no wait-only Pro workers, no fake parallelism (idle/wait double-count).

## LIVE_DEVIN_NEEDED

**No.** Do not start Computer Use to “test 10 agents.” CU mutex stays 1.

**LIVE_OBSERVATION_NEEDED** (ops, later): first GREEN/YELLOW/RED/HARD measurement. Until then optimal N stays `{{UNKNOWN}}`. Unobserved ≠ 0 and ≠ 10.

## Still not this PR

Constitution / CLI COMMON / GrokBOT desired-state patches. Sibling ORCH file is a **boundary** copy so routing order (SWE-2 first, Grok for hard spots) is not redefined here.

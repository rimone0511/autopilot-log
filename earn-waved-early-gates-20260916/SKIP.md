# SKIP — Wave D-early sample (`dead` only)

Stamp: 2026-09-16 JST  
`thin`: **0**. `dead`: **1**.

Same treatment as parent QUEUE skip: do not return to the register line unless the operator writes an explicit GO for a **different** product.

## dead

### D07 Twago

```
日付: 2026-09-16 JST
机: Twago
URL: https://www.twago.com/  →  https://www.talent-pool.com/
見たもの: HTTP 301 Location talent-pool.com. Title "Talent-Pool.com | Talent is family". Copy "We are a complete Talent Pool solution" / "fully integrated white-label talent pool solution" / "Official Fieldglass Partner". /jobs も同じ LP。https://www.twago.de/ は 404 Not Found (nginx)。公開フリーランス仕事ボードなし。
gate_result: dead
CU: skip
action: skip_log。QUEUE に戻さない。企業コンソールに入らない。
```

Not SKIP-thin: D02 カイコク (signup/LP live, dates unread — `needs_check`).

Not in this SKIP file: D05 Twine / D06 Fastwork (already `alive` elsewhere, not dead).

# SKIP — Wave D-early sample (`dead` only)

Stamp: 2026-09-16 JST  
`thin`: **0**. `dead`: **2**.

Same treatment as parent QUEUE skip: do not return to the register line unless the operator writes an explicit GO for a **different** product.

## dead

### D07 Twago

```
日付: 2026-09-16 JST
机: Twago
URL: https://www.twago.com/  →  https://www.talent-pool.com/
見たもの: HTTP 301 Location talent-pool.com. Title "Talent-Pool.com | Talent is family". Copy "We are a complete Talent Pool solution" + white-label + Official Fieldglass Partner. /jobs on twago.com follows the same 301. https://www.twago.de/ → 404 Not Found. No public freelancer signup / job board on the opened pages.
SKIP理由: dead — public freelance marketplace replaced by an enterprise Talent Pool product
```

Do not sign up. Do not bookmark as a seller desk. Do not open the Talent-Pool customer console.

### D10 Xing Projects

```
日付: 2026-09-16 JST
机: Xing Projects
URL: https://www.xing.com/projects
見たもの: HTTP 404. Title "404 - Not Found | XING". Body "We couldn't find this page." Button "Browse jobs" → xing.com. https://www.xing.com/en title "Find the right job for you. Or get found!" / "XING - The jobs network". Keyword search /jobs/search?keywords=freelance 301s into the jobs UI. That is not the Projects marketplace.
SKIP理由: dead — dedicated Projects URL is 404. Do not treat the jobs network as this desk
```

Do not create an XING job-seeker profile **because of this SKIP**. Jobs boards stay aggregator/jobs class (same family as Wellfound / LinkedIn Jobs).

## thin

None this GET. カイコク is `needs_check`, not thin: the LP and register URL are live; only listing dates are missing.

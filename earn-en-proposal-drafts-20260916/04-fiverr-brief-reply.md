# 04 — Fiverr Brief / inbound request reply

| | |
|---|---|
| Desk | Fiverr |
| Type | Brief / inbound request (official UI) |
| Mode | DRAFT_ONLY, HANDS paste |
| When | Fiverr showed **you** this Brief or request in the seller UI |
| When not | Scraped “buyer request” lists. Messaging buyers who did not request you. Gig page copy (other pack) |

Use Fiverr’s Brief flow: create an offer, ask questions, or mark not interested. Declining a brief does not ding you in the help article ([Briefs](https://help.fiverr.com/hc/en-us/articles/4415608857745-Personalized-offers-Briefs-for-freelancers)). If it is not a fit, decline instead of sending a generic offer.

The introduction you attach to a brief offer should describe relevant work. Do not paste contact details.

## Send gate

- [ ] I opened this Brief/request inside Fiverr (not a Chrome extension list)
- [ ] `{{ONE_SPECIFIC_DETAIL}}` is a phrase from **this** brief
- [ ] I will not send substantially the same paragraph to a stack of briefs in one sitting without rewriting the detail line
- [ ] No off-platform pay or messenger
- [ ] I submit in the Brief UI myself

## Paste (introduction on the brief offer / question step)

```
I read your brief: {{ONE_SPECIFIC_DETAIL}}.

Fit: I design, build, and document automations (n8n or official APIs) that an operator can rerun without me. Public notes: {{PORTFOLIO_URL}}. Example of API-only posting with a fail-closed gate: {{GITHUB_REPO_AUTOPILOT}}.

Out of scope: scraping without an official API, engagement automation, or publishing that skips your own approve step.

If we proceed I will put in the offer:
- {{DELIVERABLE_1}}
- Operator SOP
- Delivery {{DELIVERY_DAYS}} days after requirements are complete

One check before you accept: {{QUESTION_1}}

If that is wrong, tell me here — or decline and I will mark not interested so you are not waiting.
```

## If Fiverr only gives “Not interested” / “Ask questions” / “Create offer”

- Wrong stack or engagement-farm brief → **Not interested** (optionally paste snippet 08 block B in Ask questions if a box exists; otherwise just decline)
- Missing facts → **Ask questions** with `{{QUESTION_1}}` and `{{QUESTION_2}}`
- Clear fit → questions first if needed, then custom offer (snippet 05)

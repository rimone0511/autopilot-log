# 05 — Fiverr custom offer description

| | |
|---|---|
| Desk | Fiverr |
| Type | Custom offer body |
| Mode | DRAFT_ONLY, HANDS paste |
| When | Same inbox or Brief thread, after you have enough answers |
| When not | First message in a cold thread. Unsolicited offers to users who did not contact you |

Send from the inbox / Brief **Create an offer** UI ([help](https://help.fiverr.com/hc/en-us/articles/360010559198-Creating-and-managing-custom-offers)). Price, delivery time, revisions, and Gig selection are **form fields**. Help lists custom offers between **$5 and $20,000 USD** and delivery **1–90 days** — re-read the live article if the form disagrees.

Put `{{FIXED_PRICE_USD}}` in the price field. Repeat it in the description only if it **matches the field**. Do not write a second conflicting price.

Trust the on-screen character counter. Keep this shorter than a blog post.

## Send gate

- [ ] This offer is attached to an existing buyer thread or Brief
- [ ] Deliverables match what they asked, including `{{ONE_SPECIFIC_DETAIL}}`
- [ ] Price in the text = price in the form, or the text has no price
- [ ] No email / phone / external invoice link
- [ ] I click Send offer myself
- [ ] I am not stacking five nearly identical offers to five buyers from a script

## Paste

```
Custom offer for: {{ONE_SPECIFIC_DETAIL}}

Included:
1. Map the current steps and the stop conditions
2. Build the workflow on {{STACK_OR_TOOL}} (official API or documented connector only)
3. Hand over a short operator SOP and a change note (what to edit, what is a secret)

Not included: extra tools, extra channels, likes/follows/views, browser scraping, or posting that bypasses your approve step. New scope = a new offer.

Revisions: {{REVISION_COUNT}}, limited to the deliverables above.
Delivery: {{DELIVERY_DAYS}} days after you complete the order requirements on Fiverr.
```

## Optional last line if the form has no separate milestone UI

```
Suggested split if you want milestones: (1) map + stop conditions (2) working workflow + failure alert (3) SOP. I will mirror that split in Fiverr’s milestone fields when the category allows it.
```

Only use that line when you will actually fill matching milestone fields. Do not promise five milestones if the form caps at five and you have not counted.

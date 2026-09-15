# 03 — Fiverr inbound inbox reply

| | |
|---|---|
| Desk | Fiverr |
| Type | Buyer message reply |
| Mode | DRAFT_ONLY, HANDS paste |
| When | A buyer already opened a conversation on your Gig |
| When not | Cold DM to a random user (forbidden). Briefs (use 04). Sending the custom offer itself (use 05 after they answer) |

Fiverr forbids using bots/scripts to send mass messages, and forbids DMs whose point is promoting your Gigs to people who did not ask ([Community Standards](https://help.fiverr.com/hc/en-us/articles/32242973123985-Our-Community-Standards)). This snippet is **only** for a thread the buyer started.

Keep the first reply short. Ask what you need for a custom offer. Do not dump the full offer in chat if you are about to send the official offer object.

## Send gate

- [ ] This is an existing inbox thread started by the buyer
- [ ] `{{ONE_SPECIFIC_DETAIL}}` is from **their** message or Gig request, not a leftover
- [ ] No email / phone / WhatsApp
- [ ] I am not attaching an off-Fiverr invoice
- [ ] I click send myself (native quick-response insert is OK if I edit it first)

## Paste

```
Thanks for writing about {{ONE_SPECIFIC_DETAIL}} on "{{GIG_TITLE}}".

I can scope this as an automation plus an operator note (what it does, what to do when it fails). I only use official APIs or documented connectors — no browser bots, no likes/follows/views.

To send an accurate custom offer in this inbox I need:
1. {{QUESTION_1}}
2. {{QUESTION_2}}

Please keep the order on Fiverr. I will put price, delivery days, and revisions in the offer form after you answer.
```

## If they only said “hi” / “are you available?”

Still require one real detail. If they will not give one, do not send a priced offer yet. You may use snippet 08 block A.

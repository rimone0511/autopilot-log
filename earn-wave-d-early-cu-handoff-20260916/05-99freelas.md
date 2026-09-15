> DRAFT_ONLY paste pack. NO secrets. NO marketplace login from this authoring PR. NO publish.
> Role: Eu quero Trabalhar. 0 propostas. No Premium.
> Termos: no contact/links in profile; no off-platform pay; do not discuss commission in the proposal text.
> Do not copy OAuth client IDs from page JS into git.

# PACK — 99freelas — this-folder play 5

| Key | Value |
|---|---|
| inventory | 05 |
| cu_serial | **unindexed** |
| queue | D-early gate add (not original QUEUE D1–D8 row; PR#22 keep) |
| activity_gate | **alive** (PR#22: `/projects` public headings e.g. Laravel 12 / IA logística) |
| self_serve | yes (Cadastre-se / É grátis) |
| cu_ready | true (pack exists. **not registered**) |
| official | https://www.99freelas.com.br/ |
| projects | https://www.99freelas.com.br/projects |
| register | https://www.99freelas.com.br/register |
| register_freelancer | https://www.99freelas.com.br/register/freelancer → **403** Cloudflare this IP |
| how | https://www.99freelas.com.br/como-funciona |
| terms | https://www.99freelas.com.br/termos |
| google_signup_preference | **PREFER_GOOGLE** (public JS has `registerFreelancer` Google OAuth URL; confirm button after Trabalhar) |
| worker_fee_public | How-it-works: cadastro grátis. **“taxa de 5% a 20% (R$ 10,00 no mínimo)”** on the freelancer offer, paid by the contractor, on the final value. Premium **R$ 54,90 a R$ 89,90 por mês** — do not buy. Extra “Turbinar” from **R$ 19,90** — do not buy |
| paid | **NO** |
| stop_at_kyc | **STOP** |
| draft | true |
| observed | 2026-09-16 public GET |

UI language: **pt-BR**. Operator does not fake native Portuguese. English bio is OK unless the form requires PT — then paste the EN text and note `needs_check` for PT rewrite by a human. Do not machine-invent a native-PT bio in git.

Homepage marketing totals (projetos concluídos, freelancers cadastrados, pago aos freelancers) are **not** activity proof.

## needs_check

- Google button after “Eu quero Trabalhar” → Continuar (`/register/freelancer` 403 this IP).
- `Publicado:` timestamps empty in static `/projects` HTML. Do not invent recency counts.
- Whether profile can stay incomplete / not listed.

## CU handoff

1. Open https://www.99freelas.com.br/register (not `/register/freelancer` first if it challenges).
2. **Eu quero Trabalhar** (not Contratar).
3. **Google** as `{{GOOGLE_ACCOUNT_EMAIL}}`. Fallback: email `{{EMAIL}}`. Do not create Facebook/LinkedIn for this desk.
4. Email confirm via parent Gmail MCP.
5. Profile: skills, EN About, honest `{{COUNTRY}}`. **No email, phone, WhatsApp, or URLs in profile/portfolio** (Termos).
6. **Keep Premium closed.**
7. **0 propostas.** No chat pitches.
8. STOP at payout / government ID / bank.

Cloudflare: `holdDurationMs` 1800, retry 2500. Do not store Ray IDs.

## Field map (placeholders)

### Account

| UI field | Paste | Notes |
|---|---|---|
| Intent | Trabalhar / Freelancer | Not client. |
| Google | `{{GOOGLE_ACCOUNT_EMAIL}}` | Preferred. |
| Email | `{{EMAIL}}` | MAIN mailbox. |
| Password | `{{PASSWORD_DO_NOT_STORE}}` | Email path. |
| Name | `{{FULL_LEGAL_NAME}}` | |
| Country | `{{COUNTRY}}` | Honest JP OK. Do not fake BR. |

### Worker profile

| UI field | Paste | Notes |
|---|---|---|
| Photo | `{{PROFILE_PHOTO_LOCAL_PATH}}` | Face. Not ID. |
| Title / headline | Short bio | English unless PT required. |
| About | Long bio | **No contact data** (Termos). |
| Skills | `n8n, automação, API, documentação, SOP, Python, integração` + English twins | Live picker. |
| Hourly / value | `{{HOURLY_RATE_USD}}` | Empty → `rate_required`. Do not invent BRL. |
| Portfolio links | **omit** | Termos forbid contact/links on profile. Website only if a dedicated non-contact field exists **and** Termos still allow — default skip. |
| Premium | off | Do not subscribe. |

## EN bios

### Short

```
n8n automation + operator docs. I stay on 99Freelas for chat, files, and payment.
```

### Long

```
I build n8n workflows and short operator manuals so a teammate can rerun the job.

Typical first project: one process (form → sheet → CRM or inbox), retries, a failure alert, and a numbered SOP. I work in English from {{CITY}}, {{COUNTRY}} ({{TIMEZONE}}). I can add Japanese operator notes if you ask in the 99Freelas thread. I am not a native Portuguese speaker -- written PT is limited and honest.

I will not:
- Share phone, email, or off-platform pay (Termos)
- Automate likes, follows, or fake traffic
- Scrape a product that has no official API

Quote inside 99Freelas only. I already include platform rules in the quote; I do not discuss commission percentages in the proposal text.
```

## STOP

Do NOT: Premium, Turbinar, propostas, contact-in-profile, off-platform pay, payout KYC, invent “N projetos/dia”, copy OAuth secrets from HTML.

Allowed: Google/email Trabalhar signup, draft profile without links.

## Activity note

PR#22 **alive**. This GET: `/projects` 200, `/register` 200, `/register/freelancer` 403, `/como-funciona` fee copy, `/termos` 200. `thin_site_skip: false` (WAF ≠ dead).

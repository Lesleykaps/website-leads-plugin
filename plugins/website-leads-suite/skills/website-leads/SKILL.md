---
name: website-leads
description: Research publicly advertised businesses that may need a new or improved website, verify the evidence, deduplicate results, and export an auditable Excel report. Use for prospect research only; never contact prospects.
---

# Website Leads

Produce evidence-backed, research-only website-improvement leads. Do not send, schedule, draft for delivery, or otherwise initiate contact. Do not treat a public contact as marketing consent.

## Start each run

Resolve: geography, requested qualified-lead target, sectors to include/exclude, output folder, and the persistence mode. If unspecified, ask for geography and target; use a conservative target of 15 only if the user asks to proceed without one. Use the portable defaults in [configuration.md](references/configuration.md). Read [qualification.md](references/qualification.md), [evidence-and-scoring.md](references/evidence-and-scoring.md), and [output-schema.md](references/output-schema.md) before production research.

Choose one persistence mode before qualification:

- `none`: within-run matching only. Clearly label the report as having no historical deduplication.
- `local`: use an installer-selected, private JSONL registry; run the helper before and immediately before export.
- `remote`: use only a configured, authenticated MCP/backend that implements [persistence-and-backend.md](references/persistence-and-backend.md). Obtain confirmation before its first write in a run.

Never silently depend on a repository, a local drive path, personal account, country-specific phone rule, or unavailable browser tool. Country is a configuration value; preserve a number as advertised unless a configured regional normalizer and evidence support its normalisation.

## Research workflow

1. Build a varied search matrix. Use at least four industries where the market supports it; keep a single industry below 30% unless the user asks for a focused sector. Bound the run to the configured candidate and page limits.
2. Make one candidate queue. Capture only public business identity, public business contacts, business-specific activity evidence, and source URLs. Social, directory, and marketplace pages can discover a business but do not automatically prove it lacks a site.
3. Dedupe the queue with `scripts/dedupe.py`; do not auto-accept a strong fuzzy match. Record within-run, historical, and unresolved matches separately.
4. Verify current activity and each claimed website condition using the rules below. For existing-site claims, inspect desktop and mobile and retain screenshots when the host allows it. A timeout, anti-bot page, or browser failure is inconclusive, not a defect.
5. Reconcile current official domains. If a plausible working replacement site exists or ownership is uncertain, move the candidate to `Review Needed`.
6. Score each accepted lead independently across all six components; do not reuse default scores or status templates. For 10+ assessed candidates, run the anomaly audit if 80% share a status or exact total.
7. Run `scripts/validate_leads.py` before creating the report. Move failing candidates to `Review Needed`; never override a failed gate. Build the four-sheet XLSX specified in [output-schema.md] and ZIP the workbook with retained evidence.
8. Immediately before export, rerun dedupe. In `local` or confirmed `remote` mode, append only validated qualified leads after the final gate. Return the XLSX, evidence ZIP, count qualified, counts by dedupe type, and `Review Needed` count.

## Non-negotiable safeguards

- Collect only public business contact details. No personal-data inference, gated-data scraping, access-control bypass, or intrusive security testing.
- Require a public business email or phone. Email eligibility requires a syntactically valid, non-obfuscated email plus a verbatim business-specific evidence excerpt and observation date. Phone-only does not imply WhatsApp capability.
- A qualifying lead needs business-specific identity, current-activity, contact, and website-condition evidence. Do not reuse a source URL as required primary/contact evidence across separate qualified leads.
- Do not qualify `No Website` from one missing link: record a branded search query, two independent business-specific sources on different hosts, and the plausible domains checked. Browser evidence alone cannot prove absence.
- Existing-site claims require screenshots and reproducible visitor-visible evidence. Mobile-unresponsive claims additionally require a human-readable impact note. Put low-confidence or unresolved work in `Review Needed`.
- Never lower the evidence threshold to meet a target. If bounded searching is exhausted, document the shortfall and stop.

## User-facing actions

Offer these actions without performing outreach: `Run research`, `Audit supplied businesses`, `Review evidence`, `Export report`, `Configure persistence`, and `Delete local research data`. See [examples.md](references/examples.md) for wording and expected outputs.


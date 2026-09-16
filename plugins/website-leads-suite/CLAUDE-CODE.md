# Claude Code installation

Website Leads Suite is compatible with Claude Code as a skills-only plugin. It includes evidence-backed research, review-ready outreach drafting, and approval-gated delivery instructions.

## Install from the Cipher Technologies marketplace

In Claude Code, run:

```text
/plugin marketplace add Lesleykaps/website-leads-suite
/plugin install website-leads-suite@cipher-technologies
```

Then invoke the skill as:

```text
/website-leads-suite:website-leads Find 10 verified website-improvement opportunities in Harare and export an XLSX report.
/website-leads-suite:craft-website-outreach Create a review workbook from this approved research report.
```

For command-line installation, use:

```text
claude plugin marketplace add Lesleykaps/website-leads-suite
claude plugin install website-leads-suite@cipher-technologies
```

## Scope and safeguards

- Research and drafting never send. Delivery requires an explicitly approved row plus a user-authorized email provider.
- It uses public business contact details only.
- Browser checks, screenshots, Excel creation, and historical deduplication depend on the capabilities and configuration available in the user's Claude Code environment.
- Use local persistence unless a user has deliberately configured an authenticated backend. No credentials or personal sender identity are included in the plugin.

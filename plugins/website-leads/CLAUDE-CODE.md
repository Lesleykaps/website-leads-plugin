# Claude Code installation

Website Leads is compatible with Claude Code as a skills-only plugin. It uses the same research-only policy, evidence standards, local deduplication helper, and output schema as the Codex edition.

## Install from the Cipher Technologies marketplace

In Claude Code, run:

```text
/plugin marketplace add Lesleykaps/website-leads-plugin
/plugin install website-leads@cipher-technologies
```

Then invoke the skill as:

```text
/website-leads:website-leads Find 10 verified website-improvement opportunities in Harare and export an XLSX report.
```

For command-line installation, use:

```text
claude plugin marketplace add Lesleykaps/website-leads-plugin
claude plugin install website-leads@cipher-technologies
```

## Scope and safeguards

- This is research only: it never sends messages, emails, or outreach.
- It uses public business contact details only.
- Browser checks, screenshots, Excel creation, and historical deduplication depend on the capabilities and configuration available in the user's Claude Code environment.
- Use local persistence unless a user has deliberately configured an authenticated backend.

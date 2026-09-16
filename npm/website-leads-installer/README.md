# Website Leads npm installer

This package installs the Website Leads plugin from the Cipher Technologies GitHub marketplace. It is an installer only: it does not collect data, run research, contact businesses, or transmit research records.

## Use after publication

For Codex:

```text
npx @cipher-technologies/website-leads codex
```

For Claude Code:

```text
npx @cipher-technologies/website-leads claude
```

Add `--yes` only for a non-interactive, deliberately approved installation.

## What the installer changes

For the selected host, it adds the public Cipher Technologies marketplace if needed and installs the `website-leads` plugin. The host may retain the marketplace if the plugin is later removed; this is normal marketplace behavior.

## Prerequisites

- Node.js 18 or later.
- Codex CLI/Desktop for the `codex` target, or Claude Code for the `claude` target.
- GitHub access to the public Website Leads repository.

## Publishing

This package is published manually by a Cipher Technologies npm organization owner. It is intentionally not published by CI and does not run installation actions during `npm install`.

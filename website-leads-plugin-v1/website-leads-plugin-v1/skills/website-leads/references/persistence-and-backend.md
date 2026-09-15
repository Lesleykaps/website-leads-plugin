# Persistence and optional backend contract

Skills alone cannot provide reliable cross-user historical deduplication, account-scoped storage, or managed browser execution. V1 therefore includes no MCP configuration and works locally or with no history. A future remote implementation should expose only these authenticated, least-privilege operations:

| Operation | Input | Output | Write? |
|---|---|---|---|
| `registry.check` | candidate identities, workspace scope | exact/fuzzy matches and reasons | No |
| `registry.append_validated` | validated lead records, run ID, idempotency key | accepted IDs/conflicts | Yes, explicit consent |
| `registry.delete_scope` | workspace scope, confirmation | deletion receipt | Yes, explicit consent |
| `research.capture` | approved URL, viewport, run ID | screenshot/evidence metadata | Optional, consented |

Scope all data by authenticated tenant/user; never use a global public lead registry. Enforce idempotency, optimistic concurrency, append-only audit events, data minimisation, retention/deletion policy, request and per-host limits, URL allow/deny controls, and validation of every untrusted URL/content field. Return structured errors such as `AUTH_REQUIRED`, `CONSENT_REQUIRED`, `RATE_LIMITED`, `CONFLICT`, `INVALID_INPUT`, and `SERVICE_UNAVAILABLE`. The skill must preserve its local checkpoint and continue only with a safe fallback; otherwise it stops without claiming historical dedupe.

Do not add `mcp.json` until an HTTPS service, authentication design, published privacy/terms URLs, threat model, test environment, and review evidence exist.

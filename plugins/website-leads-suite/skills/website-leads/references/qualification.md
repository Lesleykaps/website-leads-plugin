# Qualification rules

Accept a lead only when it is an active business; identity and location are corroborated by an official presence or two credible public sources; it has a public business email or phone; the website issue has observable evidence; and dedupe does not block it. Current activity evidence should normally be within 18 months and business-specific.

Primary statuses: `No Website`, `Broken Website`, `Mobile Unresponsive`, `Outdated Website`, `Insecure Website`, and `Poor Conversion Website`. Use one primary status and record secondary issues.

- **No Website:** no current official site after a branded search and two different-host, business-specific sources that identify the active business and do not reveal an owned domain. Record the query, URLs, source types, and rejected plausible domains.
- **Broken Website:** two fresh attempts plus independent browser/HTTP evidence show a visitor-visible DNS, TLS, connection, material server, unrelated redirect, or unavailable critical journey failure. Never use one timeout.
- **Mobile Unresponsive:** screenshot evidence shows material overflow, clipping, unreadable content, unusable navigation, or an unusable form; document the actual impact. Styling preference, small text alone, and a missing viewport tag do not qualify.
- **Outdated Website:** several visible maintenance signals, such as stale business information and broken key content. An old look or copyright year alone is insufficient.
- **Insecure Website:** ordinary use displays a browser warning/broken HTTPS or a sensitive submission path lacks appropriate transport security. Do not scan or exploit.
- **Poor Conversion Website:** a working site materially obstructs the business's likely enquiry, booking, or sale journey. Tie the observation to visible business context.

For all existing-site statuses, check plausible replacement domains. A working attributable replacement domain or uncertain attribution is `Review Needed`.


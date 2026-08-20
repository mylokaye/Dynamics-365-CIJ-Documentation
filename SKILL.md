---
name: d365-customer-insights-forms
description: Build, embed, customize, and troubleshoot Dynamics 365 Customer Insights - Journeys marketing forms. Use when creating a form, identifying Designer elements, applying CSS or JavaScript customizations, handling submission behavior, embedding forms in web or React applications, or validating Customer Insights form API guidance.
---

# D365 Customer Insights Forms

Help users make safe, maintainable changes to Customer Insights - Journeys marketing forms. Use the focused references below for implementation work.

## Choose the reference

- For the HTML hierarchy, section/container layout, reusable block shapes, or structural review, read [references/form-structure.md](references/form-structure.md).
- For form settings, field constraints, lookup privacy, consent, publishing, or validation, read [references/form-management.md](references/form-management.md).
- For Designer metadata, containers, protected elements, and style-setting attributes, read [references/custom-attributes.md](references/custom-attributes.md).
- For custom fonts, fallback stacks, and typography testing, read [references/custom-fonts.md](references/custom-fonts.md).
- For HTML Designer blocks or locked elements, read [references/designer-elements.md](references/designer-elements.md).
- For standard embeds, lifecycle events, dynamic rendering, React, or lookup fields, read [references/embed-and-client-api.md](references/embed-and-client-api.md).
- For confirmation messages, submission icons, redirects, and CSS, read [references/styling-and-submission-feedback.md](references/styling-and-submission-feedback.md).
- For custom scripts and progressive disclosure, read [references/custom-javascript.md](references/custom-javascript.md).

## Workflow

1. Determine the hosting model: hosted-as-script, dynamic JavaScript rendering, React, or iframe. Do not propose the JavaScript API for iframe-hosted forms.
2. Prefer form settings and standard Designer options before editing HTML, CSS, or JavaScript. Use the built-in post-submission action for standard thank-you and redirect behavior.
3. Preserve Designer-managed content inside `data-editorblocktype` elements. Make custom behavior event-driven and attach listeners with `addEventListener`.
4. Use the published form embed code for environment-specific URLs and identifiers; do not invent service URLs, organization IDs, form IDs, or regions.
5. For platform behavior that could have changed, consult the Microsoft Learn MCP before giving a definitive answer. Distinguish documented behavior from a custom workaround.
6. Provide a minimal, scoped snippet and a test plan. Include cache-bypass testing where a published form may be served from a CDN.

## Guardrails

- Avoid inline event attributes because the form editor can sanitize them.
- Do not place secrets, API keys, or customer data in client-side code.
- Confirm selectors and behavior against the published form; custom CSS classes are implementation details and can change.
- When source notes disagree about event names or payload properties, prefer current Microsoft Learn documentation and say what was verified.

---
name: d365-customer-insights-forms
description: Create, convert, embed, customize, and validate Dynamics 365 Customer Insights - Journeys marketing forms. Use for new native forms, migrations of existing HTML forms, Form Capture integrations, published-form troubleshooting, or client-side extensions.
---

# D365 Customer Insights forms

Build forms that Customer Insights - Journeys can validate, publish, and process. A local HTML render is not proof of platform compatibility.

## Choose the supported path

Read [references/build-or-convert.md](references/build-or-convert.md) before creating or converting a form.

- **New native form:** Create a blank form in Customer Insights - Journeys and use its form editor. This is the default for new work.
- **Rebuild an existing form as native:** Use a blank form from the target environment, recreate the layout, and add mapped fields, unmapped fields, consent, reCAPTCHA, and Submit through the form editor. Choose this when Customer Insights should own rendering and submission.
- **Form Capture:** Keep the existing site's form and integrate the generated capture script. Use this only when the existing form has complex logic or must also submit to another system. Read [references/form-capture.md](references/form-capture.md).
- **Standard embed:** If the site only needs to display a Customer Insights form, create the native form and use the exact embed snippet from **Publish**. Do not convert the host page's form.

Do not mix the native loader API and Form Capture API. Do not propose the JavaScript loader API for an iframe-hosted form.

## Establish the environment contract

Before generating deployable code, establish:

1. form type and target audience: Contact, Lead, Lead & Contact, or event registration;
2. duplicate-record strategy and every field required by its matching rule;
3. mapped versus unmapped questions and the actual logical names available to that audience;
4. compliance profile, purposes, topics, channels, and opt-in behavior;
5. hosting model and exact allowed external-hosting domain when applicable;
6. a same-environment native form export, embed snippet, or Form Capture snippet.

Do not invent form IDs, organization IDs, API or CDN hosts, field mappings, generated control IDs, template IDs, compliance IDs, purpose IDs, or topic IDs. If the target-environment artifact is unavailable, produce a clearly labeled candidate or migration plan—not a deployment-ready or compatible form.

## Native create workflow

1. In Customer Insights - Journeys, create a form under **Channels** > **Forms**, choose a blank form or a target-environment template, confirm the audience, and set the duplicate-record strategy.
2. Add mapped fields from the selected audience in the form editor. Add questions that must not update Contact or Lead as supported unmapped fields. Do not turn arbitrary hand-authored inputs into mapped fields by guessing `data-*` metadata.
3. Add and configure consent in the form editor. Add reCAPTCHA to every publicly accessible form. Add a Submit button.
4. Use Theme and form settings first. Use the HTML editor only for requirements the supported settings cannot meet. Start code work from the current form's stored HTML or a same-environment seed form and preserve generated mappings and metadata.
5. Run the local preflight checker when HTML is available. Resolve `scripts/validate_form.py` relative to this `SKILL.md`; for example, from the skill directory:

   ```bash
   python3 scripts/validate_form.py path/to/form.html --mode native
   ```

6. In Customer Insights, run **Check content**, resolve blocking errors and relevant warnings, then publish using the generated standalone or JavaScript option.
7. Verify a published submission, not only rendering. Confirm the submission reaches **Success**, the intended Contact or Lead is created or updated according to the matching rule, and consent records are correct when consent is present.

## Conversion workflow

Inventory the existing form before editing: fields, field types, names, validation, hidden values, consent, CAPTCHA, submission endpoint, redirects, analytics, accessibility, and any non-Dynamics destination.

- Prefer a **native rebuild** when the form can be represented in the Customer Insights editor. Preserve the visual design, but replace existing controls with mapped or unmapped blocks added by the form editor.
- Prefer **Form Capture** when the original DOM, business logic, or other submission destinations must remain. Start from the generated capture snippet, complete its mappings, and wait for its submission promise before redirecting.
- Preserve the original server submission only when the requirement explicitly calls for dual submission, and test both destinations independently.

Never paste environment-specific consent markup from the repository examples into a real form. Configure consent in the target form editor; Form Capture ignores consent-definition changes made only in its code snippet.

## Compatibility evidence

Report the strongest level actually verified:

- **Candidate:** HTML or an integration plan exists, but target-environment values are missing.
- **Locally checked:** the preflight checker and relevant local browser/accessibility checks pass.
- **Platform accepted:** the target form saves and **Check content** passes in Customer Insights.
- **Published:** the current version renders through the intended standalone or embed route; external domains are allowed for form hosting.
- **End-to-end verified:** a unique test submission succeeds and the expected record, submitted values, and consent state are confirmed.

Do not describe a form as working or Customer Insights-compatible below **Platform accepted**. Do not describe submission behavior as verified below **End-to-end verified**.

## Coding and security rules

- Use the published embed or capture code for environment-specific endpoints and identifiers.
- Treat prefill tokens, hidden fields, unmapped fields, capture mappings, and submitted values as untrusted input. Never place secrets or authorization decisions in them.
- Add JavaScript with `addEventListener`; the form editor sanitizes inline event attributes. Use the documented lifecycle events for loader-hosted forms.
- Prefer the built-in post-submission action. If custom success handling is necessary, account for the documented `Success`/`successful` inconsistency and verify the actual event payload.
- Scope CSS to the form. Preserve generated field blocks, consent blocks, validation attributes, and inline layout metadata unless a target-environment test proves an override is safe.
- A domain only needs to be added to allowed domains and enabled for external form hosting; completing email-domain authentication is a separate concern.
- Use `#d365mkt-nocache` only for testing a newly published standalone version. Do not distribute cache-bypass URLs.
- For current platform behavior, search Microsoft Learn MCP first and fetch the relevant full page. Distinguish Microsoft-documented behavior, repository fixture conventions, and custom workarounds.

## Focused references

- [Build or convert](references/build-or-convert.md): routing, field mapping, required artifacts, and acceptance tests.
- [Form Capture](references/form-capture.md): generated-script workflow and dual-submit boundaries.
- [Form structure](references/form-structure.md): native HTML hierarchy, Designer blocks, and published geometry.
- [Form management](references/form-management.md): audience, matching, validation, consent, and publishing.
- [Embed and client API](references/embed-and-client-api.md): standard embeds, lifecycle events, dynamic rendering, React, and lookups.
- [Custom attributes](references/custom-attributes.md): Designer containers, elements, and style settings.
- [Form prefill and submitted values](references/form-prefill-and-submitted-values.md): prefill, unmapped fields, and downstream values.
- [Form security and operations](references/form-security-and-operations.md): reCAPTCHA, privacy, throttling, and public-hosting boundaries.
- [Custom JavaScript](references/custom-javascript.md), [custom fonts](references/custom-fonts.md), [Designer elements](references/designer-elements.md), and [styling and submission feedback](references/styling-and-submission-feedback.md): load only when the request needs them.

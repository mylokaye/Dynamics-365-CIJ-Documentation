# Dynamics 365 - Customer Insights Forms Skill

> **Release status: Alpha / locally validated**
>
> This project is experimental and not a substitute for validation in a target Customer Insights environment. Dynamics 365 markup, CSS classes, JavaScript APIs, and Designer behavior may change.

This repository contains a Codex skill for creating, converting, embedding, customizing, validating, and troubleshooting Dynamics 365 Customer Insights - Journeys forms.

The skill combines:

- Focused guidance for Designer elements, form embedding, client-side events, custom JavaScript, submission feedback, and styling.
- Current Microsoft Learn documentation retrieved through the Microsoft Learn MCP.
- Archival Lead and Contact form exports used to study generated structure. They contain non-reusable placeholder and environment-specific consent values and are not deployment templates.
- An experimental visual design system that preserves Dynamics-managed form structure.

## Current scope

The Alpha currently helps an agent:

- Recognize and preserve Designer-managed HTML and `data-*` attributes.
- Choose between a native form, native rebuild, standard embed, and Form Capture integration.
- Create a native form from a target-environment blank form and convert an existing form without inventing mappings or identifiers.
- Understand the published D365 layout-width contract, including generated inline `width` and `flex-basis` values on sections and containers.
- Preserve the section, container, column, and field spacing represented by the repository fixtures without treating those values as universal platform requirements.
- Derive required fields from the selected matching rule, target table, and business requirement.
- Work with script-hosted forms, dynamic rendering, React embedding, and lookup fields.
- Add scoped CSS and event-driven JavaScript without relying on inline event attributes.
- Work with form prefill, unmapped fields, and submitted values without treating CRM setup as form code.
- Apply public-form bot protection and account for service-protection throttling.
- Customize validation, submission feedback, redirects, consent controls, and common form fields.
- Apply custom fonts, including the project's Manrope choice, with system and generic fallbacks.
- Check changing platform behavior against official Microsoft Learn documentation.
- Run a dependency-free local preflight for native source or Form Capture pages and report platform acceptance separately from local checks.

The core agent instructions are in [`SKILL.md`](SKILL.md). Detailed material is loaded from `references/` only when relevant.

## Repository structure

```text
.
├── CHANGELOG.md
├── SKILL.md
├── test.html
├── agents/
│   └── openai.yaml
├── scripts/
│   └── validate_form.py
├── tests/
│   └── test_validate_form.py
├── references/
│   ├── build-or-convert.md
│   ├── custom-attributes.md
│   ├── custom-fonts.md
│   ├── custom-javascript.md
│   ├── designer-elements.md
│   ├── embed-and-client-api.md
│   ├── form-management.md
│   ├── form-capture.md
│   ├── form-prefill-and-submitted-values.md
│   ├── form-security-and-operations.md
│   ├── form-structure.md
│   └── styling-and-submission-feedback.md
└── examples/
    ├── contact/
    │   └── default.html
    ├── design-system/
    │   └── customer-insights-form.css
    └── lead/
        ├── default.html
        ├── minimal.html
        └── brand.html
```

## Example variants

| Variant | Purpose | Status |
| --- | --- | --- |
| `default.html` | Archival Dynamics export and structural baseline | Available for Lead and Contact; not reusable as-is |
| `minimal.html` | Styling removed while preserving the archival structure and metadata | Lead only; reference use; not reusable as-is |
| `brand.html` | Archival Lead export with an additional visual-only brand override | Lead only; experimental; not reusable as-is |

The branded form is based on the archival Dynamics default export, not the minimal form. It is a visual experiment, not a production template. Dynamics' own stylesheet and inline layout values remain authoritative; the brand stylesheet should change visual presentation without taking ownership of sections, columns, widths, or flex layout. The design-system CSS uses the project's Manrope font choice and applies it to the branded form.

The archival exports contain values such as `undefined` consent fields, example topic/purpose identifiers, generated IDs, and older HIP CAPTCHA styles. Never copy these values into a target form. Add consent and current reCAPTCHA through that environment's form editor.

The root [`test.html`](test.html) is a basic standalone smoke test. Its outer card budgets for the `600px` inner width used by the Dynamics layout, so it can be used to verify the width budget without treating a local preview as proof that a published form fits.

## Known issues and limitations

- The design system is an early prototype and has only received limited testing with the included Lead form.
- The Contact minimal and branded variants have not been created.
- Adding, removing, reordering, or resizing fields has not been tested across all Designer layouts and field types.
- Dynamics can rewrite HTML, CSS, and inline layout values when a form is saved.
- The Designer canvas adds editor-specific styles and overlays, so it may differ from the published form.
- Published Dynamics output can materialize `data-container-width` as fixed inline widths and flex bases. A padded `600px` `border-box` wrapper therefore has less content width than the generated layout and can visibly overflow unless the outer width budget accounts for padding and borders.
- The repository fixtures use a white background and one observed spacing pattern: zero-padded sections, `10px` field/content container padding, `16px` section gaps, `1rem` two-column gaps, and `0.45rem` label/control gaps. These are not universal Microsoft requirements.
- Published, standalone, externally embedded, React, and iframe scenarios have not all been verified.
- Keyboard navigation, screen readers, high-contrast mode, browser zoom, native validation, mobile layouts, and reduced-motion behavior need a full accessibility review.
- Success, error, loading, redirect, consent, and server-validation states need broader testing.
- Microsoft documentation currently contains inconsistent naming for the post-submit success property. Verify the current API before relying on it.
- Example forms contain placeholder consent values, generated IDs, topic identifiers, and environment-specific data. They are intentionally excluded from deployment validation.
- The local checker cannot validate Dataverse metadata, consent configuration, matching rules, domain allow-list state, platform sanitization, or submission processing. There are no automated end-to-end Dynamics tests.

## Development principles

1. Preserve all Dynamics-generated metadata, field attributes, IDs, validation, consent configuration, and Designer `div` structures unless a task explicitly requires changing them.
2. Keep original default exports unchanged as comparison baselines.
3. Apply branded styles after the Dynamics stylesheet and avoid overriding structural layout rules.
4. Treat custom Dynamics CSS selectors and generated inline layout widths as implementation details that require published-form testing.
5. Derive the audience, mappings, required fields, consent identifiers, form IDs, and service URLs from the target environment; repository fixture values are not portable.
6. Verify current platform behavior through the Microsoft Learn MCP before presenting it as definitive.
7. Test changes in a non-production form and check both the Designer and the published result, including computed widths, horizontal overflow, submission state, target record, and consent records.
8. Remove customer data, organization URLs, form IDs, tracking identifiers, and private asset URLs from shared examples.

## Planned work

- Complete Lead form validation in the Designer and published form.
- Create Contact minimal and branded variants.
- Test all supported field and consent types.
- Test field addition, removal, reordering, and column-width changes.
- Verify responsive behavior and accessibility.
- Test success, failure, validation, and redirect states.
- Forward-test the skill with realistic form-building and troubleshooting requests.

## Official sources

- [Microsoft Learn MCP Server](https://learn.microsoft.com/en-us/training/support/mcp)
- [Create Customer Insights - Journeys forms](https://learn.microsoft.com/dynamics365/customer-insights/journeys/real-time-marketing-form-create)
- [Deploy pages that contain Customer Insights - Journeys forms](https://learn.microsoft.com/dynamics365/customer-insights/journeys/real-time-marketing-deploy-pages)
- [Capture existing forms](https://learn.microsoft.com/dynamics365/customer-insights/journeys/real-time-marketing-form-capture)
- [Extend Customer Insights - Journeys forms using code](https://learn.microsoft.com/dynamics365/customer-insights/journeys/developer/realtime-marketing-form-client-side-extensibility)
- [Use custom attributes to enable designer features](https://learn.microsoft.com/dynamics365/customer-insights/journeys/custom-template-attributes)
- [Use custom fonts in Customer Insights - Journeys](https://learn.microsoft.com/dynamics365/customer-insights/journeys/use-custom-fonts)
- [Manage Customer Insights - Journeys forms](https://learn.microsoft.com/dynamics365/customer-insights/journeys/real-time-marketing-manage-forms)
- [Prefill values for forms and event registration](https://learn.microsoft.com/dynamics365/customer-insights/journeys/real-time-marketing-form-prefill)
- [Create unmapped fields for marketing forms](https://learn.microsoft.com/dynamics365/customer-insights/journeys/real-time-marketing-forms-custom-fields)
- [Use submitted values from forms](https://learn.microsoft.com/dynamics365/customer-insights/journeys/real-time-marketing-form-submitted-values)
- [Forms security and privacy](https://learn.microsoft.com/dynamics365/customer-insights/journeys/real-time-marketing-form-security-privacy)
- [Troubleshoot Customer Insights - Journeys forms](https://learn.microsoft.com/dynamics365/customer-insights/journeys/real-time-marketing-troubleshooting-forms)
- [Authenticate domains and enable external form hosting](https://learn.microsoft.com/dynamics365/customer-insights/journeys/domain-authentication)

## Version

- Repository version: `1.0.1`
- Release stage: **Alpha / locally validated**
- Stability: **Unstable; breaking changes expected**

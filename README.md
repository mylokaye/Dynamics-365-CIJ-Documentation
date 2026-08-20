# Dynamics 365 - Customer Insights Forms Skill

> **Release status: Alpha / pre-development**
>
> This project is experimental, incomplete, and not ready for production use. It contains known issues and unverified behavior. Dynamics 365 markup, CSS classes, JavaScript APIs, and Designer behavior may change.

This repository contains a Codex skill for building, embedding, customizing, and troubleshooting Dynamics 365 Customer Insights - Journeys forms.

The skill combines:

- Focused guidance for Designer elements, form embedding, client-side events, custom JavaScript, submission feedback, and styling.
- Current Microsoft Learn documentation retrieved through the Microsoft Learn MCP.
- Sanitized Lead and Contact form examples exported from Dynamics 365.
- An experimental visual design system that preserves Dynamics-managed form structure.

## Current scope

The Alpha currently helps an agent:

- Recognize and preserve Designer-managed HTML and `data-*` attributes.
- Work with script-hosted forms, dynamic rendering, React embedding, and lookup fields.
- Add scoped CSS and event-driven JavaScript without relying on inline event attributes.
- Customize validation, submission feedback, redirects, consent controls, and common form fields.
- Embed the required Manrope font in a form with system and generic fallbacks.
- Check changing platform behavior against official Microsoft Learn documentation.

The core agent instructions are in [`SKILL.md`](SKILL.md). Detailed material is loaded from `references/` only when relevant.

## Repository structure

```text
.
├── CHANGELOG.md
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── custom-attributes.md
│   ├── custom-fonts.md
│   ├── custom-javascript.md
│   ├── designer-elements.md
│   ├── embed-and-client-api.md
│   ├── form-management.md
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
| `default.html` | Untouched Dynamics export and structural baseline | Available for Lead and Contact |
| `minimal.html` | Styling removed while preserving form structure and metadata | Lead only; reference use |
| `brand.html` | Dynamics default form with an additional visual-only brand override | Lead only; experimental |

The branded form must be based on the Dynamics default export, not the minimal form. Dynamics' own stylesheet and inline layout values remain authoritative; the brand stylesheet should change visual presentation without taking ownership of sections, columns, widths, or flex layout. The design-system CSS embeds the required Manrope font and applies it to the branded form.

## Known issues and limitations

- The design system is an early prototype and has only received limited testing with the included Lead form.
- The Contact minimal and branded variants have not been created.
- Adding, removing, reordering, or resizing fields has not been tested across all Designer layouts and field types.
- Dynamics can rewrite HTML, CSS, and inline layout values when a form is saved.
- The Designer canvas adds editor-specific styles and overlays, so it may differ from the published form.
- Published, standalone, externally embedded, React, and iframe scenarios have not all been verified.
- Keyboard navigation, screen readers, high-contrast mode, browser zoom, native validation, mobile layouts, and reduced-motion behavior need a full accessibility review.
- Success, error, loading, redirect, consent, and server-validation states need broader testing.
- Microsoft documentation currently contains inconsistent naming for the post-submit success property. Verify the current API before relying on it.
- Example forms may contain placeholder consent values, generated IDs, topic identifiers, or environment-specific data. Review and replace these before any real deployment.
- There are no automated structural regression tests or end-to-end Dynamics tests yet.

## Development principles

1. Preserve all Dynamics-generated metadata, field attributes, IDs, validation, consent configuration, and Designer `div` structures unless a task explicitly requires changing them.
2. Keep original default exports unchanged as comparison baselines.
3. Apply branded styles after the Dynamics stylesheet and avoid overriding structural layout rules.
4. Treat custom Dynamics CSS selectors as implementation details that require published-form testing.
5. Verify current platform behavior through the Microsoft Learn MCP before presenting it as definitive.
6. Test changes in a non-production form and check both the Designer and the published result.
7. Remove customer data, organization URLs, form IDs, tracking identifiers, and private asset URLs from shared examples.

## Planned work

- Complete Lead form validation in the Designer and published form.
- Create Contact minimal and branded variants.
- Test all supported field and consent types.
- Test field addition, removal, reordering, and column-width changes.
- Verify responsive behavior and accessibility.
- Test success, failure, validation, and redirect states.
- Add repeatable checks that prove branded examples preserve the default form structure.
- Forward-test the skill with realistic form-building and troubleshooting requests.

## Official sources

- [Microsoft Learn MCP Server](https://learn.microsoft.com/en-us/training/support/mcp)
- [Extend Customer Insights - Journeys forms using code](https://learn.microsoft.com/dynamics365/customer-insights/journeys/developer/realtime-marketing-form-client-side-extensibility)
- [Use custom attributes to enable designer features](https://learn.microsoft.com/dynamics365/customer-insights/journeys/custom-template-attributes)
- [Use custom fonts in Customer Insights - Journeys](https://learn.microsoft.com/dynamics365/customer-insights/journeys/use-custom-fonts)
- [Manage Customer Insights - Journeys forms](https://learn.microsoft.com/dynamics365/customer-insights/journeys/real-time-marketing-manage-forms)

## Version

- Repository version: `1.0.0`
- Release stage: **Alpha / pre-development**
- Stability: **Unstable; breaking changes expected**

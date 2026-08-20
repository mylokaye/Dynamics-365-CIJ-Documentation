---
name: d365-customer-insights-forms
description: Build, embed, customize, and troubleshoot Dynamics 365 Customer Insights - Journeys marketing forms. Use when creating a form, identifying Designer elements, applying CSS or JavaScript customizations, handling submission behavior, embedding forms in web or React applications, or validating Customer Insights form API guidance.
---

# D365 Customer Insights Forms

Help users make safe, maintainable changes to Customer Insights - Journeys marketing forms. Use the focused references below for implementation work.

## Choose the reference

- For the HTML hierarchy, section/container layout, reusable block shapes, or structural review, read [references/form-structure.md](references/form-structure.md).
- For form settings, field constraints, lookup privacy, consent, publishing, or validation, read [references/form-management.md](references/form-management.md).
- For form prefill, unmapped fields, or using submitted values in downstream form-triggered behavior, read [references/form-prefill-and-submitted-values.md](references/form-prefill-and-submitted-values.md).
- For public-form CAPTCHA, security boundaries, tracking privacy, throttling, or service limits, read [references/form-security-and-operations.md](references/form-security-and-operations.md).
- For Designer metadata, containers, protected elements, and style-setting attributes, read [references/custom-attributes.md](references/custom-attributes.md).
- For custom fonts, fallback stacks, and typography testing, read [references/custom-fonts.md](references/custom-fonts.md).
- For HTML Designer blocks or locked elements, read [references/designer-elements.md](references/designer-elements.md).
- For standard embeds, lifecycle events, dynamic rendering, React, or lookup fields, read [references/embed-and-client-api.md](references/embed-and-client-api.md).
- For confirmation messages, submission icons, redirects, and CSS, read [references/styling-and-submission-feedback.md](references/styling-and-submission-feedback.md).
- For custom scripts and progressive disclosure, read [references/custom-javascript.md](references/custom-javascript.md).

## Required generated document shell

Every generated HTML form must include the following Dynamics 365 Customer Insights - Journeys document shell before the form body. Preserve the doctype, template identifier, author link, title, referrer policy, and Designer settings exactly as shown. Do not omit these elements for minimal, standalone, or test forms.

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html data-template-id="4c65bec8-4b46-ed11-bba2-000d3a8d107a">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://go.microsoft.com/fwlink/?linkid=2224838" data-comment="Form extensibility documentation" rel="author">
    <title>Marketing Form</title>
    <meta name="referrer" content="never">
    <meta type="xrm/designer/setting" name="type" value="marketing-designer-content-editor-document">
    <meta type="xrm/designer/setting" name="layout-editable" value="marketing-designer-layout-editable">
    <meta type="xrm/designer/setting" name="layout-max-width" value="600px" datatype="text" label="Layout max width">
  </head>
```

The closing `</head>`, the form markup, and the document closing tags must follow this shell. Do not substitute a different template ID or Designer metadata unless the user supplies an environment-specific published export that requires it.

## D365 published layout width contract

Treat `data-layout-maxwidth="600px"` as the inner content width owned by the Dynamics form layout. It is not the total width of a custom card or wrapper around the form.

Published Designer output can add fixed inline widths and flex bases to containers, for example:

```html
<div data-container="true" data-container-width="50" style="width: 300px; flex: 0 0 300px;"></div>
<div data-container="true" data-container-width="100" style="width: 600px; flex: 0 0 600px;"></div>
```

These generated values are structural layout values. Preserve them in a published export and do not assume that `data-container-width` alone applies the corresponding CSS in a standalone page. A section can expand beyond its parent when fixed-width child containers combine with the default `min-width: auto` behavior.

When adding a custom outer card, calculate the width budget explicitly:

```text
outer border-box width = D365 content width + left/right padding + left/right borders
```

For example, a `600px` outer element using `box-sizing: border-box`, `40px` left and right padding, and `1px` borders leaves only `518px` for the form content. A published Dynamics section or container still sized to `600px` will then overflow by `82px`. Keep the D365 layout as the width owner, or make the outer wrapper wide enough to contain the full generated layout.

Do not treat a standalone local render as proof that a published form fits. Verify the published result after Dynamics applies its generated inline styles.

## Required spacing and field defaults

Use these spacing patterns consistently for generated forms. Keep container widths derived from the published `data-layout-maxwidth`; do not hard-code example values such as `280px`, `580px`, or `600px` when the layout width changes.

- Sections use `display: flex`, `flex: 1 0 0%`, `margin: 0`, and `padding: 0`, with no visible border. Preserve the generated border declarations when present, but keep the effective border style set to `none`.
- Standard field and content containers use `padding: 10px`, `flex-direction: column`, `min-width: 5px`, `float: left`, and word wrapping (`word-wrap: break-word` and `word-break: break-word`). Full-width field containers also use the `10px` padding.
- The form-fields layout uses `gap: 16px` between sections.
- A two-column row uses `gap: 1rem` between its columns.
- Field blocks use `gap: 0.45rem` between the label and control.
- Use a white page/form background (`background: #fff`); do not emit an empty or invalid background value.
- Keep submit-button wrappers centered and preserve any generated no-padding submit-container exception when it is part of the published export.

For basic contact or lead forms, last name (`lastname`) and email (`emailaddress1`) are required fields. Mark both the Designer block and native control as required with `data-required="required"` and `required="required"`. Do not silently make either field optional.

## Workflow

1. Start every generated HTML form with the required document shell above, then determine the hosting model: hosted-as-script, dynamic JavaScript rendering, React, or iframe. Do not propose the JavaScript API for iframe-hosted forms.
2. Prefer form settings and standard Designer options before editing HTML, CSS, or JavaScript. Use the built-in post-submission action for standard thank-you and redirect behavior.
3. Preserve Designer-managed content inside `data-editorblocktype` elements. Make custom behavior event-driven and attach listeners with `addEventListener`.
4. Use the published form embed code for environment-specific URLs and identifiers; do not invent service URLs, organization IDs, form IDs, or regions.
5. Treat prefill tokens, hidden fields, unmapped fields, and submitted values as untrusted form data. Never place secrets or authorization decisions in them.
6. For platform behavior that could have changed, consult the Microsoft Learn MCP before giving a definitive answer. Distinguish documented behavior from a custom workaround.
7. Provide a minimal, scoped snippet and a test plan. Include cache-bypass testing where a published form may be served from a CDN.
8. For custom wrappers, cards, or responsive overrides, verify the published geometry in Chrome: compare the computed widths of the layout, every section and container, and each field/button; confirm that no child right edge exceeds its intended parent and that the document has no unintended horizontal overflow.

## Guardrails

- Before returning generated HTML, verify that the required document shell is present, including the XHTML doctype, `data-template-id`, author link, title, referrer setting, and all three `xrm/designer/setting` metadata elements.
- Do not give a custom outer wrapper a total width equal to the D365 content width when the wrapper also adds padding or borders; account for the full width budget.
- Do not override generated container `width`, `flex-basis`, or section sizing merely to make a local preview fit. Confirm the published form's computed geometry and document any intentional structural override.
- Before returning a basic contact or lead form, confirm that the last-name and email field blocks and their native controls are both marked required.
- Avoid inline event attributes because the form editor can sanitize them.
- Do not place secrets, API keys, or customer data in client-side code.
- Confirm selectors and behavior against the published form; custom CSS classes are implementation details and can change.
- When source notes disagree about event names or payload properties, prefer current Microsoft Learn documentation and say what was verified.

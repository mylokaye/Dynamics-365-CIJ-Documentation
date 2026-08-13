# Custom JavaScript

## Add scripts safely

Use the form HTML editor only when a Designer option cannot meet the need: open the form editor and select the **HTML** (`</>`) control in the top toolbar. Place custom JavaScript in the HTML `<body>`; scripts placed in other sections can be removed when the form is saved. The editor can wrap scripts in `safe-script` during edit mode and sanitizes inline event attributes such as `onclick` and `onchange`.

Attach behavior with `addEventListener` instead:

```js
document.addEventListener("DOMContentLoaded", () => {
  const button = document.querySelector(".submit-button");
  button?.addEventListener("click", () => {
    // Add narrowly scoped behavior.
  });
});
```

## Event-name discrepancy

One source names `d365mkt-formload`, `d365mkt-beforeformsubmit`, `d365mkt-afterformsubmit`, and `d365mkt-formerror`. The dedicated client-API guidance names a different lifecycle set, including `d365mkt-afterformload`, `d365mkt-formsubmit`, and `d365mkt-afterformsubmit`.

Do not assume that these names are interchangeable. Before writing an event handler, verify its current availability and payload through Microsoft Learn MCP; then use the documented name consistently.

## Progressive field display

Use a rendered-form lifecycle event when the field belongs to a script-hosted marketing form; `DOMContentLoaded` alone may be too early. Scope selectors to the form and handle missing elements gracefully.

```js
document.addEventListener("d365mkt-afterformload", (event) => {
  const form = event.target.querySelector("form");
  const company = form?.querySelector('[name="company"]');
  const employeeCount = form?.querySelector(".employee-count-field");
  if (!company || !employeeCount) return;

  employeeCount.hidden = !company.value;
  company.addEventListener("change", () => {
    employeeCount.hidden = !company.value;
  });
});
```

Test all changes in a non-production form first, including validation errors, inaccessible-JavaScript fallback, keyboard interaction, and mobile rendering. Use Microsoft Learn MCP for current troubleshooting and form-capture guidance.

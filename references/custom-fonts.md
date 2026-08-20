# Custom fonts

Use this reference when embedding the required Manrope font in a Customer Insights - Journeys form. The form loads Manrope in its own HTML, falls back to the system UI font, and then falls back to a generic sans-serif font. The font rules apply to the form and its controls.

For current product behavior, verify the [Microsoft Learn guidance on custom fonts](https://learn.microsoft.com/en-us/dynamics365/customer-insights/journeys/use-custom-fonts).

## Embed Manrope in the form

Add the font import at the beginning of the form's existing `<style>` block. Keep it before the other CSS rules. If the form editor removes external font imports, use an approved self-hosted font URL or the platform-supported font configuration instead.

```css
@import url("https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700&display=swap");
```

Loading a Google-hosted font sends a request to Google from the visitor's browser. Confirm that this is acceptable for the form's privacy, security, licensing, and availability requirements before publishing. If it is not, self-host the required Manrope font using an approved source; do not substitute a different primary font.

## Apply the font to the complete form

Place these rules after the Dynamics stylesheet and any generated form styles. The form root establishes the stack; descendants, pseudo-elements, and native controls inherit the font family.

```css
form.marketingForm {
  font-family: "Manrope", system-ui, sans-serif !important;
}

form.marketingForm *,
form.marketingForm *::before,
form.marketingForm *::after {
  font-family: inherit !important;
}
```

The fallback order is:

1. `Manrope`, when the embedded font loads.
2. `system-ui`, using the visitor's operating-system interface font.
3. `sans-serif`, as the generic browser fallback.

Do not replace the generated form layout selectors or use broad global selectors such as `*` outside `.marketingForm`.

## Reuse and testing rules

- Keep the `@import` at the top of the existing `<style>` block; do not create a competing stylesheet or duplicate the import.
- Keep Manrope as the primary font when self-hosting; only the system and generic fonts may act as fallbacks.
- Preserve the Dynamics stylesheet and generated inline layout values. Typography changes should not change section or container sizing unexpectedly.
- Test labels, inputs, select menus, buttons, validation messages, consent text, focus indicators, zoom, and narrow mobile widths.
- Confirm the form remains legible when Manrope is unavailable and that the system and generic fallbacks have sufficient contrast and readable metrics.

# Styling Forms

## Using the Theme Panel

The form designer includes a **Theme panel** to control visual appearance without writing code:

1. Open your form in the editor
2. Click the **Styles** or **Theme** tab
3. Adjust settings: fonts, colors, spacing, borders, buttons

## Adding Custom CSS

For more control beyond the theme panel:

1. Click the **HTML** button (`</>`) in the form editor
2. Locate the `<style>` section
3. Add your custom CSS
4. Click **Save**

### Custom CSS Example

```css
.form-field input {
    border: 2px solid #e0e0e0;
    border-radius: 8px;
    padding: 12px;
}

.submit-button {
    background: #0078d4;
    color: white;
    padding: 14px 28px;
    border-radius: 6px;
}
```

## Related Resources

- [Advanced Customization](advanced-customization.md)
- [Customize Submission Images](../how-to/customize-submission-images.md)

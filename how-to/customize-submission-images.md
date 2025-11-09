# Customize Form Submission Images

## Overview

Form submissions display a generic green checkmark icon that cannot be changed through standard settings.

## Implementation

Customize or hide the submission icon by adding CSS code to your form's HTML.

## Option 1: Hide the Icon Completely

```css
div[data-cached-form-url] .onFormSubmittedFeedbackIcon {
  display: none;
}
```

## Option 2: Replace with Your Own Image

### Step 1: Adjust Message Positioning

```css
div[data-cached-form-url] .onFormSubmittedFeedback .onFormSubmittedFeedbackMessage {
  padding: 10em 1em 0em 1em;
  color: #000;
  font-size: 14px;
}
```

### Step 2: Add Custom Image

```css
div[data-cached-form-url] .onFormSubmittedFeedback .onFormSubmittedFeedbackInternalContainer {
  padding: 30px 0px 30px 1px;
  background: url(YOUR-IMAGE-URL-HERE) no-repeat;
  margin: auto;
  background-position: center;
}
```

## How to Add the CSS

1. Edit your marketing form
2. Click **HTML** (`</>`) in the top right
3. Find the `<style>` section
4. Paste your CSS code inside it
5. Save and publish

## Bonus: Redirect After Confirmation

Show a message AND then redirect:

```javascript
<script>
document.addEventListener("d365mkt-afterformsubmit", function(event) {
  setTimeout(function() {
    window.location.href = "/thank-you"; 
  }, 5000); // 5 seconds
});
</script>
```

Place this JavaScript below your form embed script on your website.

## Tips

- Keep images under 200KB
- Use 64x64px to 128x128px for icons
- PNG with transparency looks professional
- Test with [`#d365mkt-nocache`](../guides/editing-forms.md#using-the-cache-bypass-parameter) first to bypass CDN caching

## Related Resources

- [Styling Forms](../guides/styling-forms.md)
- [Advanced Customization](../guides/advanced-customization.md)

# Frequently Asked Questions (FAQ)

## General Questions

### What is form capture?

Form capture connects existing HTML forms to D365 without rebuilding them in the form editor.

See the [Form Capture guide](../guides/form-capture.md) for detailed setup instructions and use cases.

### Do D365 Forms use cookies?

No. Forms use a [journey-id](technical-reference.md#journey-id) instead of cookies to identify known users.

See [Overview - Privacy & Cookies](../getting-started/overview.md#privacy--cookies) for details.

### How secure are Forms in Dynamics 365?

Forms include domain authentication, bot protection (CAPTCHA), rate limiting, and data encryption.

See [Overview - Security Features](../getting-started/overview.md#security-features) for complete details.

## Publishing & Caching

### Why aren't my form changes showing up?

Forms are cached on a [CDN](technical-reference.md#cdn-caching). Changes take up to 10 minutes to propagate.

**Quick testing**: Append [`#d365mkt-nocache`](../guides/editing-forms.md#using-the-cache-bypass-parameter) to your form URL (don't share publicly).

### How do I unpublish a form?

1. Open the form
2. Click **Stop**
3. Status changes to **Draft**

## Technical Issues

### Why is my form not accepting submissions?

Check:
1. Domain authentication
2. Form is published
3. Rate limiting (2,000 requests/minute)
4. Required fields are mapped
5. No CORS errors in console

### Why is my data not syncing to CRM?

Common causes:
1. Field mapping errors
2. Entity permissions
3. Duplicate detection rules
4. Data type mismatches

### Why am I getting CORS errors?

Your domain isn't enabled for external form hosting.

**Solution**: Go to **Settings > Domain Authentication** and add your domain. See [Domain Authentication](technical-reference.md#domain-authentication) for details.

### How do I enable Form Capture?

1. **Settings > Feature switches**
2. Navigate to **Forms**
3. Toggle on **Form capture**
4. Requires version 1.1.35355+

## Styling & Customization

### Why won't my custom CSS apply?

Common issues:
1. Inline styles override theme
2. Cache (wait 10 minutes)
3. CSS specificity too low
4. Syntax errors

### Can I use JavaScript in forms?

Yes! Add custom JavaScript in the HTML editor. Use `addEventListener` instead of inline event attributes.

### How do I hide the submission checkmark?

```css
div[data-cached-form-url] .onFormSubmittedFeedbackIcon {
  display: none;
}
```

See [Customize Submission Images](../how-to/customize-submission-images.md)

## Performance & Limits

### What are the form submission rate limits?

- 2,000 requests per minute per organization
- Translates to 100-500 valid submissions per minute

See [Rate Limiting](technical-reference.md#rate-limiting) for more details.

### How many fields should a form have?

**Best practice**: 5-7 fields maximum for optimal completion rates.

## Related Resources

- [Troubleshooting Guide](troubleshooting.md)
- [Form Capture Setup](../guides/form-capture.md)
- [Advanced Customization](../guides/advanced-customization.md)

# Dynamics 365 Customer Insights Forms - Overview

## What Are Forms?

Forms in Dynamics 365 Customer Insights – Journeys let you capture customer information directly from your website, events, or campaigns and sync it automatically into your database. 

They're powerful because they turn every interaction into usable data for segmentation, personalization, and automated follow-up across your customer journeys.

## Security Features

Keeping your marketing and event forms secure is a key priority in Customer Insights – Journeys. Here's how it protects your data and forms:

**Approved domains only**: Forms and captured submissions only work on domains that you've added to the "allowed" list for external hosting.

**Default setup**: If you're using Microsoft's built-in hosting domain, it's already approved by default.

**Bot protection**: To stop spam or fake submissions, add a CAPTCHA to your form. You can use the built-in CAPTCHA option or connect a third-party service for better user experience.

**Traffic control**: To protect against DDoS attacks (too many requests at once), the system limits traffic to 2,000 requests per minute per organization.

## Privacy & Cookies

Marketing and event registration forms don't use any cookies. Form visit and form submit interactions use a [journey-id](../reference/technical-reference.md#journey-id) to get details about known users.

## Best Practices

### Performance Optimization

- Keep forms short (5-7 fields maximum)
- Use conditional logic to show/hide fields
- Enable progressive profiling
- Minimize required fields

### Compliance Considerations

- Include clear consent checkboxes
- Link to privacy policies
- Use preference centers for opt-out management
- Maintain audit trails of consent

### Data Quality

- Use dropdown lists for standardized data
- Implement proper validation patterns
- Set clear error messages
- Use placeholder text for guidance

## Related Resources

- [Creating Your First Form](creating-your-first-form.md)
- [Editing Forms](../guides/editing-forms.md)
- [FAQ](../reference/faq.md)

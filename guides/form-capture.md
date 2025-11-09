# Form Capture

## Overview

Form capture connects existing HTML forms to D365 without rebuilding them in the form editor.

**When to use:**
- Your form sends data to multiple systems
- Your form has complex custom logic
- You want to keep your existing form design
- You're gradually migrating to D365

## Prerequisites

- Solution version 1.1.35355 or higher
- [Domain authentication](../reference/technical-reference.md#domain-authentication) must be enabled for external form hosting
- Form capture feature enabled in settings

## Enabling Form Capture

1. Navigate to **Settings > Feature switches**
2. Go to the **Forms** section
3. Toggle on **Form capture**

## How Form Capture Works

The process involves:
1. Creating a form in the Customer Insights - Journeys form editor
2. Publishing the form to obtain a capture script
3. Embedding the script into your web page
4. Mapping form fields to Dynamics 365 attributes
5. Viewing submissions in Customer Insights

## Setting Up Form Capture

### Step 1: Create the Form in D365

1. Go to **Customer Insights - Journeys > Channels > Forms**
2. Click **New**
3. Name the form
4. Choose the target audience (Contact, Lead, etc.)
5. Add all fields you want to map
6. Add a Submit button
7. Click **Publish** and copy the capture code

### Step 2: Field Mapping

Map your HTML form fields to D365 attributes:

```javascript
fieldMapping: {
    'firstname': 'firstname',
    'lastname': 'lastname',
    'email': 'emailaddress1',
    'phone': 'telephone1',
    'company': 'companyname'
}
```

### Mapping OptionSet Fields

```javascript
fieldMapping: {
    'industry': {
        attribute: 'industrycode',
        valueMap: {
            'tech': 1,
            'finance': 2,
            'healthcare': 3
        }
    }
}
```

## Domain Authentication

Your domain must be enabled for external form hosting in **Settings > Domain Authentication**.

See [Domain Authentication glossary entry](../reference/technical-reference.md#domain-authentication) for detailed setup instructions.

## Related Resources

- [Troubleshooting Guide](../reference/troubleshooting.md)
- [FAQ](../reference/faq.md)

# Technical Reference

## Overview

This technical documentation provides in-depth details on how Dynamics 365 Customer Insights forms work, including requirements, structure, and implementation details.

### Complete Form Example

[View Complete Example](https://pattens-tech.github.io/dynamics-365-forms/templates/contact-form.html)

---

## Table of Contents

1. [Glossary](#glossary)
   - [CDN Caching](#cdn-caching)
   - [Domain Authentication](#domain-authentication)
   - [Form Capture](#form-capture)
   - [Journey ID](#journey-id)
   - [Rate Limiting](#rate-limiting)
   - [Logical Name](#logical-name)
   - [Target Audience](#target-audience)
2. [Form Element Types](#form-element-types)
3. [Default Form Fields](#default-form-fields)
4. [Form Structure Requirements](#form-structure-requirements)
   - [Header Structure](#header-structure)
   - [Body Structure (Form)](#body-structure-form)
   - [Body Structure (Thank You Modal)](#body-structure-thank-you-modal)
5. [Advanced Styling with Tailwind CSS](#advanced-styling-with-tailwind-css)
   - [Typography Guidelines](#typography-guidelines)
   - [Color System](#color-system)
   - [Spacing Conventions](#spacing-conventions)
   - [Layout Standards](#layout-standards)
6. [Accessibility Requirements](#accessibility-requirements)
   - [Core Principles](#core-principles)
   - [Accessibility Checklist](#accessibility-checklist)

---

## Glossary

### CDN Caching
**Content Delivery Network (CDN) Caching** refers to how D365 forms are distributed globally for fast loading. When you publish or edit a form, changes are cached across Microsoft's CDN servers worldwide. This means:
- Changes take **up to 10 minutes** to propagate globally
- Forms load faster for end users
- You can bypass caching for testing using `#d365mkt-nocache` parameter

**Learn more**: [Editing Forms - Testing Changes Safely](../guides/editing-forms.md#testing-changes-safely)

### Domain Authentication
**Domain Authentication** is the process of authorizing specific domains to host and submit D365 forms. For security, forms only work on pre-approved domains.

**Setup location**: Settings > Domain Authentication

**Requirements**:
- Add your domain to the allowed list
- Complete DNS verification
- Allow 24 hours for propagation

**Note**: Microsoft's built-in hosting domain is pre-approved by default.

**Learn more**: [Troubleshooting - CORS Errors](troubleshooting.md#cors-errors)

### Form Capture
**Form Capture** allows you to connect existing HTML forms (not built in D365) to Dynamics 365 Customer Insights. Instead of rebuilding your form, you add a capture script that maps your form fields to D365 attributes.

**Use cases**:
- Existing forms with complex custom logic
- Forms that send data to multiple systems
- Gradual migration to D365

**Requirements**: Solution version 1.1.35355 or higher

**Learn more**: [Form Capture Guide](../guides/form-capture.md)

### Journey ID
**Journey ID** is a unique identifier used to track form interactions and link them to specific customer journeys in D365. Forms use this ID instead of cookies to:
- Identify known users
- Track form visits and submissions
- Connect form data to customer journey analytics

**Privacy note**: No cookies are used; journey-id is passed as a parameter.

### Rate Limiting
**Rate Limiting** is a security measure that restricts the number of form requests to prevent abuse and DDoS attacks.

**Current limits**:
- **2,000 requests per minute** per organization
- Translates to approximately 100-500 valid submissions per minute

**When exceeded**: Additional requests are temporarily blocked. Consider implementing client-side throttling for high-traffic forms.

**Learn more**: [Troubleshooting - Rate Limit Exceeded](troubleshooting.md#form-not-accepting-submissions)

### Logical Name
**Logical Name** is the internal database field name in Dynamics 365 (e.g., `emailaddress1` for the email field, `firstname` for first name). When mapping form fields, you must use the exact logical name, which is case-sensitive.

**Finding logical names**: Settings > Customizations > Entities > Fields

**Common logical names**:
- Email: `emailaddress1`
- Phone: `telephone1` or `mobilephone`
- Company: `companyname`

### Target Audience
**Target Audience** refers to the D365 entity (e.g., Contact, Lead) that form submissions will create or update. This is specified using the `data-targetaudience` attribute in form HTML.

**Common values**:
- `contact` - For contact records
- `lead` - For lead records

---

## Form Element Types

### Required Form Elements

| Element | `data-editorblocktype` | Purpose |
|---------|----------------------|---------|
| Email field | `Field-email` | Email input |
| Text fields | `Field-firstname`, `Field-lastname` | Text inputs |
| Checkbox | `Field-checkbox` | Checkbox field |
| Submit button | `SubmitButtonBlock` | Form submission (required) |

### Optional Form Elements

| Element | `data-editorblocktype` | Purpose |
|---------|----------------------|---------|
| Custom field | `Field-{name}` | Any CRM field (use logical name) |
| Subscription list | `SubscriptionListBlock` | Subscription options |
| Captcha | `CaptchaBlock` | Captcha verification |
| Reset button | `ResetButtonBlock` | Form reset |
| Forward to friend | `ForwardToFriendBlock` | Forward functionality |

---

## Default Form Fields

### Contacts & Leads

These may differ depending on your D365 customizations:

| Field | Logical name |
|-------|--------------|
| Contact / First Name | firstname |
| Contact / Last Name | lastname |
| Contact / Email | emailaddress1 |
| Lead / First Name | firstname |
| Lead / Last Name | lastname |
| Lead / Email | emailaddress1 |
| Lead / Mobile phone | mobilephone |
| Lead / Company name | companyname |

### Field Properties

Each form field supports:

| Property | Description | Example |
|----------|-------------|---------|
| Placeholder | Text shown when field is empty | "Enter your email" |
| Default Value | Pre-filled value | "newsletter@example.com" |
| Required | Makes field mandatory | true/false |
| Validation | Input validation rule | Custom RegExp |
| Hidden | Hide field from view | true/false |

---

## Form Structure Requirements

Both header and body structures are required for forms to function:

```
├─→ Entire file
│   ├─→ Header (Dynamics 365 tags)
│   ├─→ Header (Style, Fonts)
│   ├─→ Body (Form)
│   └─→ Body (Thank you modal)
```

### Header Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
         <!-- Required: Dynamics 365 -->
         <meta type="xrm/designer/setting" name="type" value="marketing-designer-content-editor-document">
         <meta type="xrm/designer/setting" name="layout-editable" value="marketing-designer-layout-editable">
         <meta type="xrm/designer/setting" name="additional-fonts" datatype="font" value="<Inter>">

         <!-- Required: HTML document setup -->
         <meta charset="UTF-8">
         <meta name="viewport" content="width=device-width, initial-scale=1.0">
       
        <!-- Required: Tailwind CSS -->
        <script src="https://cdn.tailwindcss.com"></script>

        <!-- Google Fonts: Roboto -->
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
        
        <!-- Required: Tailwind Configuration -->
        <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        brand: {
                            DEFAULT: /* @brand-color */ '#0078d4' /* @brand-color */
                        }
                    },
                    fontFamily: {
                        roboto: ['Roboto', 'sans-serif']
                    }
                }
            }
        }
 </script>
</head>
```

### Body Structure (Form)

```html
<body>
  <form class="marketingForm">
    <div data-layout="true" data-layout-version="v2" class="max-w-lg mx-auto p-6 bg-white shadow-lg rounded-2xl">
  

      <!-- Form intro -->

      <div data-editorblocktype="Text" class="mb-2">
        <h1 class="text-3xl font-bold text-center text-sky-900 mb-2">Contact us</h1>
      </div>
      <div data-editorblocktype="Text" class="mb-6">
        <p class="text-center text-gray-600 mb-6">We'd love to hear from you</p>
      </div>

      <!-- Form fields-->
      <div class="mb-4" data-editorblocktype="TextFormField" data-targetaudience="contact" data-targetproperty="firstname" data-prefill="false" data-required="required">
        <label for="firstname" class="block text-gray-800 text-sm font-medium mb-2">First Name</label>
        <input id="firstname" type="text" name="firstname" placeholder="First Name" maxlength="50" required class="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-400">
      </div>
      <div class="mb-4" data-editorblocktype="TextFormField" data-targetaudience="contact" data-targetproperty="lastname" data-required="required" data-prefill="false">
        <label for="lastname" class="block text-gray-800 text-sm font-medium mb-2">Last Name</label>
        <input id="lastname" type="text" name="lastname" placeholder="Last Name" maxlength="50" required class="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-400">
      </div>
      <div class="mb-4" data-editorblocktype="TextFormField" data-targetaudience="contact" data-targetproperty="emailaddress1" data-prefill="false" data-required="required">
        <label for="emailaddress1" class="block text-gray-800 text-sm font-medium mb-2">Email</label>
        <input id="emailaddress1" type="email" name="emailaddress1" placeholder="Email" required class="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-400">
      </div>
      <div class="mb-4" data-editorblocktype="TextAreaFormField" data-targetaudience="contact" data-targetproperty="description" data-prefill="false" data-required="required">
        <label for="description" class="block text-gray-800 text-sm font-medium mb-2">Description</label>
        <textarea id="description" name="description" placeholder="Description" maxlength="2000" required class="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-400 h-32"></textarea>
      </div>
      <hr class="my-6 border-gray-200">

      <div data-editorblocktype="Text" class="mb-2">
        <h2 class="text-xl font-semibold text-gray-800 mb-2 text-left">Newsletter</h2>
      </div>
      <div data-editorblocktype="Text" class="mb-2">
        <p class="text-gray-600 text-left mb-2">We will send you news, webinars, marketing emails. You can opt out at any time.</p>
      </div>
      <div class="flex items-start mb-4" data-editorblocktype="Topic" data-required="false">
        <input type="checkbox" id="consentTopicCheckbox" name="msdynmkt_topicid;channels;optinwhenchecked" value="b5cfd151-c1ac-f011-bbd3-7c1e522e1eab;Email;true" class="h-4 w-4 text-sky-600 border-gray-300 rounded focus:ring-sky-500">
        <label for="consentTopicCheckbox" class="ml-2 text-sm text-gray-700">Send me the newsletter</label>
      </div>

      <div class="text-center mt-6" data-editorblocktype="SubmitButton">
        <button type="submit" class="bg-sky-700 hover:bg-sky-800 text-white font-semibold py-3 px-6 rounded-lg shadow-md transition-all">Send message</button>
      </div>

      <div data-editorblocktype="Text">
        <p class="text-xs text-gray-400 mt-4 text-center">By selecting Send message, I agree to the Terms of Service and acknowledge the Privacy policy.</p>
      </div>
    </div>
  </form>
```

### Body Structure (Thank You Modal)

```html
    <!-- Thank You Modal -->
    <div id="thankYouModal" class="fixed inset-0 bg-black bg-opacity-50 hidden items-center justify-center">
      <div class="bg-white rounded-2xl p-8 shadow-xl text-center max-w-sm">
        <div class="mx-auto mb-4 w-16 h-16 flex items-center justify-center rounded-full bg-green-100 text-green-600 text-3xl">✓</div>
        <h2 class="text-2xl font-bold text-gray-800 mb-2">Thank you!</h2>
        <p class="text-gray-600 mb-4">We've received your message and will get back to you soon.</p>
        <button type="button" class="bg-sky-700 text-white px-6 py-2 rounded-lg hover:bg-sky-800 transition" onclick="closeThankYouModal()">Close</button>
      </div>
    </div>

  <script>
    function closeThankYouModal() {
      document.getElementById('thankYouModal').classList.add('hidden');
    }
  </script>
</body>
</html>
```

---

## Advanced Styling with Tailwind CSS

Using Tailwind CSS enables faster forms due to external hosting.

### Typography Guidelines

- Use `font-roboto` for consistent font family
- Headers: `font-medium` (500 weight)
- Body: `font-normal` (400 weight)

### Color System

- Brand color: `text-brand` or `bg-brand`
- Background: `bg-gray-50` for form background
- Text: `text-gray-900` for primary text
- Secondary text: `text-gray-500`

### Spacing Conventions

- Container padding: `p-8`
- Between fields: `mb-4`
- Section spacing: `mb-8`

### Layout Standards

- Container width: `max-w-3xl`
- Center alignment: `mx-auto`
- Responsive padding: `px-4 sm:px-6 lg:px-8`

---

## Accessibility Requirements

All forms should include proper accessibility features:

### Core Principles

- **Label every field clearly**: Use `<label>` elements linked to inputs via `for` and `id` attributes
- **Keyboard navigation**: Ensure all interactive elements are reachable via Tab/Shift+Tab
- **ARIA roles**: Use appropriate attributes (`aria-required`, `aria-label`, `aria-describedby`)
- **Error messages**: Make visible to screen readers (`aria-live="polite"`)
- **Contrast and focus**: Sufficient color contrast and clear focus indicators
- **Group related fields**: Use `<fieldset>` and `<legend>` for groups
- **Accessible buttons**: Use `<button>` or `<input type="submit">` with clear labels

### Example: Required Field with Error Handling

```html
<div class="mb-4"
     data-editorblocktype="TextFormField"
     data-targetaudience="contact"
     data-targetproperty="firstname"
     data-required="required">
  <label for="firstname" class="block text-gray-800 text-sm font-medium mb-2">
    First Name <span aria-label="required" class="text-red-600">*</span>
  </label>
  <input
    id="firstname"
    type="text"
    name="firstname"
    placeholder="First Name"
    aria-required="true"
    aria-describedby="firstname-error"
    maxlength="50"
    required
    class="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-400">
  <span id="firstname-error" class="hidden text-red-600 text-sm mt-1" role="alert" aria-live="polite"></span>
</div>
```

### Example: Checkbox Group with Fieldset

```html
<fieldset class="mb-6">
  <legend class="text-xl font-semibold text-gray-800 mb-2">Newsletter Preferences</legend>
  <p class="text-gray-600 mb-4">Select the topics you're interested in:</p>

  <div class="flex items-start mb-3">
    <input
      type="checkbox"
      id="topic-marketing"
      name="msdynmkt_topicid;channels;optinwhenchecked"
      value="topic-id-1;Email;true"
      class="h-4 w-4 text-sky-600 border-gray-300 rounded focus:ring-sky-500"
      aria-describedby="topic-marketing-desc">
    <label for="topic-marketing" class="ml-2 text-sm text-gray-700">
      Marketing Updates
      <span id="topic-marketing-desc" class="block text-xs text-gray-500">
        Latest product news and promotions
      </span>
    </label>
  </div>

  <div class="flex items-start mb-3">
    <input
      type="checkbox"
      id="topic-events"
      name="msdynmkt_topicid;channels;optinwhenchecked"
      value="topic-id-2;Email;true"
      class="h-4 w-4 text-sky-600 border-gray-300 rounded focus:ring-sky-500"
      aria-describedby="topic-events-desc">
    <label for="topic-events" class="ml-2 text-sm text-gray-700">
      Event Invitations
      <span id="topic-events-desc" class="block text-xs text-gray-500">
        Webinars, conferences, and networking events
      </span>
    </label>
  </div>
</fieldset>
```

### Accessibility Checklist

- [ ] All form fields have associated `<label>` elements
- [ ] Required fields marked with `aria-required="true"`
- [ ] Form completable using keyboard only
- [ ] Visible focus indicators on all interactive elements
- [ ] Error messages use `role="alert"` and `aria-live="polite"`
- [ ] Color contrast meets WCAG 2.1 AA (4.5:1 for normal text)
- [ ] Related controls grouped with `<fieldset>` and `<legend>`
- [ ] Clear, accessible error feedback

---

## Credits

Documentation rewritten from: [Microsoft Learn - Custom Template Attributes](https://learn.microsoft.com/en-gb/dynamics365/customer-insights/journeys/custom-template-attributes?WT.mc_id=DX-MVP-5003395)

# How to Create Forms in D365 Customer Insights

## Overview

Learn how to effectively create, customize, and deploy forms in D365 Customer Insights to capture customer data and manage preferences across your marketing campaigns.


## How to Create Your First Form

Adding Form Fields

The form editor in D365 Customer Insights uses a drag-and-drop interface. Here's how to add fields:

From the toolbox panel, drag field elements onto your canvas
Click each field to configure:
Field mapping: Link to the correct entity attribute
Display name: Set user-friendly labels
Validation rules: Make fields required or set specific formats
Default values: Pre-populate where appropriate
Essential Fields to Include

For marketing forms, typically include:

First Name and Last Name
Email Address (always required)
Company Name
Phone Number
Marketing preferences checkboxes
How to Style Your Forms

Using the Style Editor

##Customize your form appearance to match your brand:

Click the Styles tab in the form editor

Adjust:
Font family and sizes
Color schemes for fields, buttons, and text
Spacing and padding
Border styles and radius

```css
/* Add custom CSS in the Style Editor */
.form-container {
    max-width: 600px;
    margin: 0 auto;
}
.submit-button {
    background-color: #0078d4;
    color: white;
    padding: 12px 24px;
}
```
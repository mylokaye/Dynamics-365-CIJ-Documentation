# Setup Form Capture in Dynamics 365 Customer Insights

## Overview

Form capture allows you to capture submissions from existing forms that weren't created using the Customer Insights - Journeys form editor. 

This feature is recommended if your existing form also sends submissions to systems other than Dynamics 365 or if it contains complex logic that can't be easily recreated in the form editor.



## How Form Capture Works

The form capture feature is disabled by default. Enable it by navigating to: Settings > Feature switches > Forms and toggle on the Form capture option. Form capture mimics submission of a standard Customer Insights - Journeys form. 

The process involves:

Creating a form in the Customer Insights - Journeys form editor
Publishing the form to obtain a capture script
Embedding the script into your web page with the existing form
Mapping form fields to Dynamics 365 entity attributes
Viewing submissions and analytics in Customer Insights - Journeys

---

## Creating a Form Capture Setup

Go to Customer Insights - Journeys > Channels > Forms
Select New on the command bar
Name the form and choose the target audience (important for field mapping)
Add all fields you want to map to your existing form fields
Add consent elements (Purpose or Topic) if needed
Add a Submit button (required for validation)
Click Publish and copy the form capture code snippet

The domain where your existing form is hosted must be enabled for external form hosting.

FAQ:

What is form capture? 
Form capture lets you capture submissions from existing forms and map them to Dynamics 365 without using the native form editor.

When should I use Form Capture? 
Use it when your form sends data to multiple systems or has complex logic that's hard to recreate in the form editor.

How do I map OptionSet and lookup fields? 
Define value mapping arrays that connect your form values to Dynamics 365 options. For lookups, set a default value or map specific field values to record IDs.

Why am I getting CORS errors? 

Your domain isn't enabled for external form hosting. Configure domain authentication to allow cross-origin submissions.
How do I enable Form Capture?

Go to Settings > Feature switches > Forms and toggle on Form capture. You need solution version 1.1.35355 or higher.

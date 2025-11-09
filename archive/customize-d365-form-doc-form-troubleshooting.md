# Troubleshooting Forms in Dynamics 365 Customer Insights

## Overview

Learn how to troubleshoot forms in Customer Insights.




## Save time by creating Custom Form Templates


Save time by creating reusable templates:
Navigate to Templates in the left navigation

Click New template > Form
Design your template with:
Standard fields and layout
Pre-configured styling
Default audience settings
Consent configurations
Save and name your template
Access it when creating new forms

---

## FAQ


Why is my form is not accepting submissions?
Check these settings in D365 Customer Insights:
Verify domain is authenticated
Confirm form is published
Check the 2,000 requests/minute limit hasn't been exceeded

Why is my Data Not Syncing to CRM?
Ensure:
Field mappings are correct
Entity permissions are properly configured
No duplicate detection rules are blocking submissions
Check data type compatibility


Why is the CAPTCHA Not Working?

Verify CAPTCHA is enabled in form settings
Check that scripts are loading correctly
Test in different browsers
Consider implementing a third-party CAPTCHA service


Why am I getting CORS errors? 

Your domain isn't enabled for external form hosting. Configure domain authentication to allow cross-origin submissions.
How do I enable Form Capture?

Go to Settings > Feature switches > Forms and toggle on Form capture. You need solution version 1.1.35355 or higher.

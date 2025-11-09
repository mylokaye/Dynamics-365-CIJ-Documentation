# Edit and Customise Forms in Customer Insights - Journeys

## Edit forms in Dynamics 365

1. Navigate to your form and click Edit in the command bar.
2. Make your changes in the form designer.
3. Click Save to publish changes immediately.
• Because the form is cached on a CDN, changes may take up to 10 minutes to reflect on the live page.
• To see changes immediately for testing, append #d365mkt-nocache to the form URL (don’t use this URL publicly).

If you prefer, you can create a copy of a form, make changes there, and publish the new version instead.



## Unpublish a form

• To remove a form from live use, click Stop. That changes its status to Draft.
• Visitors may still see the form due to browser caching, but they won’t be able to submit it.

## Handling duplicate records & matching

• Forms have a Duplicate records setting, where you choose how submissions match to Contacts or Leads (update existing vs create new).
• You can use a custom matching rule (beyond the default) for more control.

• Recent enhancements allow a form to match against both Leads and Contacts (if enabled and version is updated).

## Advanced customisation (CSS, JavaScript, events)

• Open the HTML editor (via the </> button) to view or edit raw HTML and CSS.
• You can inject custom JavaScript into your form (in <body> section). In newer versions, if you add JS in <head>, the system will automatically relocate it into <body>. It uses a <safe-script> wrapper during edit mode for security.
• Inline event attributes like onClick or onChange are sanitized; instead, use addEventListener in your script.
• Use the form’s JavaScript API to trigger or react to events such as formLoad or formSubmit.

## Styling, themes & look and feel

• In the form designer you have a Theme panel to control colors, fonts, input styles, buttons, spacing, etc.
• If styling changes don’t “take,” it might be because an element was added with inline styles—remove and re-add it so it inherits your theme.
• You can override or extend styles via custom CSS in the HTML source.

## Publishing & cache behavior

• Once a form is published, it’s pushed to a global content delivery network (CDN) for fast delivery.
• Because of caching, edits can take up to 10 minutes to propagate.
• Using #d365mkt-nocache lets you bypass the CDN cache for testing, but should not be shared externally.

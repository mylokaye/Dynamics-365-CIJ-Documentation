# Editing Forms

## How to Edit a Published Form

1. Navigate to your form in **Channels > Forms**
2. Click **Edit** in the command bar
3. Make your changes in the form designer
4. Click **Save** to publish changes immediately

### Important Notes on Caching

- Because the form is cached on a CDN, changes may take up to 10 minutes to reflect on the live page
- To see changes immediately for testing, use the Dynamics 365 Form Debugger: https://pattens.tech/dynamics-365-form-debugger
- Alternatively, append `#d365mkt-nocache` to your form URL to bypass the cache during testing (remove before sharing publicly)

## Testing Changes Safely

### Using the Cache Bypass Parameter

Add `#d365mkt-nocache` to the end of your form URL:

```
https://your-domain.com/contact-form#d365mkt-nocache
```

**Important**: Remove this parameter before sharing the URL publicly, as it bypasses the CDN and impacts performance.

### Preview Mode

Before publishing changes:

1. Click **Preview** in the form editor to see how changes will appear
2. Test all form fields and validation rules
3. Verify submission behavior
4. Check mobile responsiveness

<a href="https://microsoftedge.microsoft.com/addons/detail/dynamics-365-form-debugge/ceoaoafhphcpdokfdfkiilmndbepbbec">
  <img width="300" alt="English_Get it from Microsoft Edge" src="https://github.com/user-attachments/assets/28f14c7c-a752-4fd0-9bc4-1c6da358adee" />
</a>

## Creating a Copy

If you prefer not to edit the live form directly:

1. Open the form you want to copy
2. Click **Save As** or **Copy**
3. Make changes to the new version
4. Publish when ready
5. Update your website embed code to use the new form

### When to Use Copies

- Testing major design changes
- Creating seasonal variations
- A/B testing different form layouts
- Maintaining backup versions

## Unpublishing a Form

To stop a form from accepting new submissions:

1. Navigate to **Channels > Forms**
2. Select the form you want to unpublish
3. Click **Stop** in the command bar
4. The form status changes to **Draft**

**Note**: Unpublished forms will show an error message to users who try to access them. Consider updating your website to remove the form embed code.

## Managing Form Versions

### Version Control Best Practices

- **Naming conventions**: Use descriptive names like "Contact Form v2 - Mobile Optimized"
- **Documentation**: Add notes in the form description about what changed
- **Archiving**: Keep old versions for rollback purposes
- **Testing**: Always test in a non-production environment first

### Tracking Changes

D365 automatically tracks:
- Last modified date
- Last modified by
- Publication status
- Form performance metrics

View this information in the form properties panel.

## Handling Duplicate Records

When editing forms, you may encounter duplicate detection:

### Duplicate Detection Scenarios

1. **Email already exists**: If a contact with the same email submits the form
2. **Name match**: If first name, last name, and company match an existing record
3. **Custom rules**: Based on your organization's duplicate detection settings

### Managing Duplicates

**Option 1: Update Existing Records**
- Configure form to update matching records instead of creating new ones

**Option 2: Allow Duplicates**
- Disable duplicate detection for specific forms (not recommended)

**Option 3: Merge Later**
- Review and merge duplicates manually in D365

### Configuration

1. Go to **Settings > Data Management > Duplicate Detection Rules**
2. Review rules that apply to your target entity (Contact, Lead, etc.)
3. Adjust rules or create entity-specific exceptions

## Common Editing Tasks

### Adding New Fields

1. Click **Add field** in the toolbox
2. Select field type (text, dropdown, checkbox, etc.)
3. Map to D365 attribute
4. Configure validation rules
5. Save and publish

### Removing Fields

1. Select the field in the form designer
2. Press **Delete** or click the trash icon
3. Confirm removal
4. Save and publish

**Warning**: Removing fields doesn't delete historical data, but submissions after the change won't include that field.

### Changing Field Order

1. Drag and drop fields to reorder
2. Save changes
3. Wait for CDN cache to update (up to 10 minutes)

### Modifying Validation Rules

1. Click on the field to edit
2. Go to **Properties** panel
3. Update **Required**, **Pattern**, or **Custom validation**
4. Save and test thoroughly

## Related Resources

- [Creating Your First Form](../getting-started/creating-your-first-form.md)
- [Styling Forms](styling-forms.md)
- [Troubleshooting Guide](../reference/troubleshooting.md)

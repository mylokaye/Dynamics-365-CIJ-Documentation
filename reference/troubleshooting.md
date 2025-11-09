# Troubleshooting Guide

## Quick Diagnostic Checklist

Before diving into specific issues:

- [ ] Is the form published (not Draft)?
- [ ] Is the domain authenticated?
- [ ] Within rate limits (2,000 requests/minute)?
- [ ] Waited 10 minutes for CDN cache?
- [ ] Any errors in browser console (F12)?
- [ ] All required fields mapped?

## Form Not Accepting Submissions

### Possible Causes & Solutions

#### 1. Form Not Published
**Check**: Verify status is "Live" not "Draft"
**Solution**: Click Publish

#### 2. Domain Not Authenticated
**Check**: Settings > Domain Authentication
**Solution**: Add domain, complete DNS verification

#### 3. Rate Limit Exceeded
**Check**: Monitor requests in form insights
**Solution**: Implement client-side throttling

#### 4. Required Fields Missing
**Check**: Browser console for validation errors
**Solution**: Ensure all required fields present

## Data Not Syncing to CRM

### Possible Causes & Solutions

#### 1. Incorrect Field Mapping
**Check**: Field names match D365 attributes exactly

**Solution**: 
```javascript
// Correct
'email': 'emailaddress1'  // ✅

// Incorrect  
'email': 'email'  // ❌
```

#### 2. Data Type Mismatch
**Check**: Source and destination types match
**Solution**: Text to Text, Number to Number, etc.

#### 3. Duplicate Detection Rules
**Check**: Duplicate detection settings
**Solution**: Review and adjust matching criteria

## CORS Errors

### Symptom
"Cross-Origin Request Blocked" in browser console

### Solution

1. Go to **Settings > Domain Authentication**
2. Add your domain
3. Complete DNS verification
4. Allow 24 hours for propagation

## Styling Issues

### CSS Not Applying

**Causes:**
1. Cache not cleared (wait 10 minutes)
2. Inline styles override
3. CSS specificity too low

**Solution**: Use `#d365mkt-nocache` for testing

## Form Capture Problems

### Submissions Not Captured

**Causes:**
1. Feature not enabled
2. Version too old (need 1.1.35355+)
3. Field mapping errors

**Solution**: Enable in Settings > Feature switches > Forms

## Technical Implementation Issues

### Modal Doesn't Close

**Problem**: Thank you modal doesn't close when clicking Close button.

**Solution**: Ensure the JavaScript function is included:

```html
<script>
  function closeThankYouModal() {
    document.getElementById('thankYouModal').classList.add('hidden');
  }
</script>
```

### Form Doesn't Submit to D365

**Causes**:

1. **Incorrect target audience/properties**
   - Verify `data-targetaudience` is `contact` or `lead`
   - Check `data-targetproperty` matches exact logical names (case-sensitive)

2. **Missing D365 meta tags**
   ```html
   <meta type="xrm/designer/setting" name="type" value="marketing-designer-content-editor-document">
   <meta type="xrm/designer/setting" name="layout-editable" value="marketing-designer-layout-editable">
   ```

3. **Form not published**
   - Status must be "Live" not "Draft"

### Styling Broken

**Causes**:

1. **Tailwind not loading**
   ```html
   <script src="https://cdn.tailwindcss.com"></script>
   ```

2. **Configuration errors**: Check JavaScript syntax in config block

### Custom Fields Not Mapping

**Solution**:

1. Find logical name in D365: Settings > Customizations > Entities > Fields
2. Use exact name in `data-targetproperty`

**Common logical names**:
- Email: `emailaddress1`
- Phone: `telephone1` or `mobilephone`
- Company: `companyname`

### Validation Errors Not Showing

**Solution**: Add JavaScript error handling:

```html
<script>
  document.querySelector('form').addEventListener('submit', function(e) {
    const email = document.getElementById('email');
    const error = document.getElementById('email-error');

    if (!email.validity.valid) {
      error.classList.remove('hidden');
      e.preventDefault();
    } else {
      error.classList.add('hidden');
    }
  });
</script>
```

### Newsletter Consent Not Tracking

**Solution**: Use correct format:

```html
<input
  type="checkbox"
  name="msdynmkt_topicid;channels;optinwhenchecked"
  value="YOUR-TOPIC-ID;Email;true">
```

Find topic ID: Marketing > Subscription centers > Topics

## Getting Help

### Browser Console
Press F12 > Console tab > Look for red errors

### Contact Support
Provide: Form URL, browser version, console logs, steps to reproduce

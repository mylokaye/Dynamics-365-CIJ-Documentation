# Advanced Customization

## Accessing the HTML Editor

1. Open your form in the editor
2. Click the **HTML** button (`</>`) in the top toolbar
3. View or edit raw HTML, CSS, and JavaScript

## Adding Custom JavaScript

You can inject custom JavaScript into your form. The system uses a `<safe-script>` wrapper during edit mode for security.

### Important Security Note

Inline event attributes like `onClick` or `onChange` are sanitized. Instead, use `addEventListener`:

```javascript
<script>
document.addEventListener('DOMContentLoaded', function() {
    const button = document.querySelector('.submit-button');
    button.addEventListener('click', function(e) {
        console.log('Button clicked');
    });
});
</script>
```

## Form JavaScript API

The form provides built-in events:

### formLoad Event

```javascript
document.addEventListener('d365mkt-formload', function(event) {
    console.log('Form loaded:', event);
});
```

### formSubmit Event

```javascript
document.addEventListener('d365mkt-beforeformsubmit', function(event) {
    console.log('Form is being submitted');
});

document.addEventListener('d365mkt-afterformsubmit', function(event) {
    console.log('Form submitted successfully');
});
```

### formError Event

```javascript
document.addEventListener('d365mkt-formerror', function(event) {
    console.error('Form error:', event.detail);
});
```

## Advanced Use Cases

### Progressive Field Display

```javascript
document.addEventListener('DOMContentLoaded', function() {
    const companyField = document.querySelector('[name="company"]');
    const employeeCountField = document.querySelector('.employee-count-field');
    
    employeeCountField.style.display = 'none';
    
    companyField.addEventListener('change', function() {
        if (this.value) {
            employeeCountField.style.display = 'block';
        }
    });
});
```

## Related Resources

- [Troubleshooting Guide](../reference/troubleshooting.md)
- [Form Capture](form-capture.md)

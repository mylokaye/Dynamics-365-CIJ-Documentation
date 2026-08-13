# Designer elements

## Identify a Designer-managed element

Each time an element is added through the **Designer** tab, the editor creates opening and closing `div` tags for it and generates the HTML required by that element's **Properties** settings.

Designer elements have a `data-editorblocktype` attribute. Its value identifies the element type:

```html
<div data-editorblocktype="Text">
  <!-- Do not edit Designer-managed content here. -->
</div>
```

## Element inventory

| Design element | Element category | `data-editorblocktype` value | Additional detail |
| --- | --- | --- | --- |
| Text | Common design element | `Text` | |
| Image | Common design element | `Image` | |
| Divider | Common design element | `Divider` | |
| Button | Common design element | `Button` | |
| Content block | Common design element | `Content` | Also has `data-block-datatype="text"` or `data-block-datatype="image"`. |
| Marketing page | Email | `Marketing Page` | |
| Event | Email | `Event` | |
| Survey | Email | `Survey` | |
| Form | Form | `FormBlock` | |
| Field | Form content | `Field-<field-name>` | Example: `Field-email`. |
| Subscription list | Form content | `SubscriptionListBlock` | |
| Forward to a friend | Form content | `ForwardToFriendBlock` | |
| Do-not-email or Remember-me | Form content | `Field-checkbox` | Both create checkboxes; distinguish them through their internal settings. |
| Submit button | Form content | `SubmitButtonBlock` | |
| Reset button | Form content | `ResetButtonBlock` | |
| CAPTCHA | Form content | `CaptchaBlock` | |

## Editing rule

Avoid editing content between a Designer element's opening and closing `div` tags in the HTML tab. The result can be unpredictable and the Designer may overwrite the changes. Use the **Designer** tab to manage the element's content and properties.

## Lock an element

Add `data-protected="true"` to the opening Designer element to lock its content and properties in Designer view.

```html
<div data-editorblocktype="Divider" data-protected="true">
  ...
</div>
```

# Embed and client API

## Standard form hosting

Use the embed code generated from the form's **Publish** options. It supplies the right form ID, organization ID, loader host, and geographic region for the environment. Do not hand-author those values.

The JavaScript API applies to forms hosted as a script, not iframe-hosted forms.

A standard placeholder uses the form ID, form API URL, and cached-form URL from that generated code. Load `FormLoader.bundle.js` using the generated loader host and geographic region. The loader recognizes the placeholders after `DOMContentLoaded`.

## Lifecycle events

Attach listeners using `document.addEventListener`. The available guidance identifies these events:

| Event | Use |
| --- | --- |
| `d365mkt-beforeformload` | Placeholder recognized, before content fetch |
| `d365mkt-formrender` | Content fetched, before injection |
| `d365mkt-afterformload` | Form injected into the placeholder |
| `d365mkt-formsubmit` | Submission; cancelable for validation |
| `d365mkt-afterformsubmit` | Submission completed; inspect the result |

Use current Microsoft Learn MCP documentation to confirm exact event payload property names before relying on them in production.

The source describes a `payload` object on `d365mkt-formsubmit`, and a Boolean success result plus the submitted `payload` on `d365mkt-afterformsubmit`. It uses both `success` and `successful` in different places, so verify the current property name.

```js
document.addEventListener("d365mkt-formsubmit", (event) => {
  // Validate the rendered form, then call event.preventDefault() to stop submission.
});
```

## Dynamic and React hosts

- For dynamically inserted content, use `d365mktforms.createForm(formId, formApiBaseUrl, formUrl)` after the loader is available, then append the returned `div` to the intended container.
- In React, use the loader's `d365mktforms.FormPlaceholder` component. Its matching properties are `formId`, `formApiBaseUrl`, and `formUrl`.
- Event-registration forms require the appropriate readable event ID in addition to normal form details: `data-readable-event-id` with `createForm`, or `readableEventId` with `FormPlaceholder`.

## Form behavior configuration

Set `window.d365mkt` before loading the form loader to configure supported behavior. The available guidance records `hideProgressBar: true` for suppressing the loading progress bar.

Use `data-preventsubmissionui="true"` on the form placeholder to suppress the default submission feedback UI and provide your own.

## Lookup fields

After `d365mkt-afterformload`, obtain the rendered form and use `d365mktforms.fillLookupFromSearch(form, fieldLogicalName, searchTerm)` only when its supported signature has been verified for the current platform. Handle both successful and rejected promises.

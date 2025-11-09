# How to Customize Form Submission Images in Dynamics 365 Marketing

## The Problem

When someone submits a Real-time Marketing Form in Dynamics 365 Marketing (Customer Insights - Journeys), you have two options:

1. Redirect them to another page
2. Show a confirmation message (default)

The message option works fine, but it displays a generic green checkmark icon that you can't change through the normal settings.

## The Solution

You can customize or hide this icon by adding CSS code to your form's HTML.

---

## Option 1: Hide the Icon Completely

Add this CSS to remove the checkmark without replacing it:

```css
div[data-cached-form-url] .onFormSubmittedFeedback {
  display: flex;
  align-items: center;
  justify-content: center;
  background: #fff;
  margin: 0 auto;
}

div[data-cached-form-url] .onFormSubmittedFeedbackIcon {
  display: none;
  margin-left: auto;
  margin-right: auto;
  height: 64px;
  size: 64px;
}
```

**What this does:** The icon simply won't appear. Only your confirmation message shows.

---

## Option 2: Replace with Your Own Image

### Step 1: Adjust the Message Positioning

This ensures your text sits properly with the new image:

```css
div[data-cached-form-url] .onFormSubmittedFeedback .onFormSubmittedFeedbackMessage {
  padding: 10em 1em 0em 1em;
  color: #000;
  font-size: 14px;
  line-height: 20px;
  font-family: Segoe UI;
  margin-left: auto;
  margin-right: auto;
}
```

### Step 2: Add Your Custom Image

Replace the checkmark with your own image:

```css
div[data-cached-form-url] .onFormSubmittedFeedback .onFormSubmittedFeedbackInternalContainer {
  padding: 30px 0px 30px 1px;
  background: url(YOUR-IMAGE-URL-HERE) no-repeat;
  margin: auto;
  background-position: center;
}
```

**Image URL options:**
- Use a relative path if the image is on your website: `/wp-content/uploads/image.jpg`
- Use a full URL from D365's Asset Library: `https://assets-gbr.mkt.dynamics.com/...`
- Works with static images (JPG, PNG) or animated GIFs

### Step 3: Upload Images to Asset Library (Optional)

If you don't have website access:

1. Go to Asset Library in D365 Marketing
2. Upload your image
3. Copy the image URL
4. Paste it into the CSS code above

---

## How to Add the CSS

1. Edit your marketing form
2. Click **HTML** (top right)
3. Find the `<style>` section
4. Paste your CSS code inside it
5. Save

Done! Your custom image (or no image) will now appear when forms are submitted.

---

## Bonus: Redirect After Showing the Confirmation

Want to show a thank you message AND then redirect to another page? You can do both!

### How It Works

1. User submits form
2. Thank you message displays (with your custom image)
3. After a few seconds, they're automatically redirected

### The Code

Add this JavaScript directly **below** your form embed script on your website:

```javascript
<script>
document.addEventListener("d365mkt-afterformsubmit", function(event) {
  setTimeout(function() {
    window.location.href = "/blog"; // Replace with your URL
  }, 10000); // Time in milliseconds (10000 = 10 seconds)
});
</script>
```

### Customize It

**Change the redirect URL:**
- Replace `/blog` with your destination page
- Example: `/thank-you`, `https://yoursite.com/success`, etc.

**Adjust the timing:**
- `10000` = 10 seconds
- `5000` = 5 seconds  
- `3000` = 3 seconds
- Change to whatever works best for your users


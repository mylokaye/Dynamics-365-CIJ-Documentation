# Changelog

All material changes to the D365 Customer Insights - Journeys Forms skill should be recorded here. Keep entries concise and describe changes that affect how the skill is discovered, used, or maintained.

## [Unreleased]

Add material changes here before the next version is released.

## [1.0.1] - 2026-08-20

### Added

- Added form-prefill, unmapped-field, and submitted-value guidance focused on generated form markup and form integrations, excluding CRM schema and role setup.
- Added public-form security and operations guidance covering reCAPTCHA, HIP captcha removal, client-side security boundaries, tracking privacy, service-protection limits, and `429` throttling.
- Added Dynamics form-editor instructions for uploading custom fonts and applying them through Theme text styles.

### Changed

- Updated README scope and official-source links for the new references.
- Clarified that Manrope is a project font choice rather than a universal Dynamics platform requirement, while retaining the existing fallback and testing guidance.

## [1.0.0] - 2026-08-20

Initial v1 baseline for the Dynamics 365 Customer Insights - Journeys Forms skill.

### Added

- Focused references for form structure, form management, Designer attributes, custom fonts, Designer elements, embedding, JavaScript, and submission feedback.
- Sanitized Lead and Contact form examples plus an experimental design-system stylesheet.
- Required Manrope font guidance with system and generic fallbacks.

### Changed

- Scoped the Designer element inventory to form-relevant blocks and added Consent and Topic blocks.
- Added routing for all references from `SKILL.md` and renamed generic references to `form-management.md` and `form-structure.md`.
- Updated the branded example and design-system stylesheet to use Manrope.
- Added guidance to preserve generated form metadata, structure, validation, consent settings, and environment-specific values.

### Notes

- Release stage remains Alpha / pre-development; platform behavior, APIs, generated markup, and selectors may change.
- The original default form exports remain comparison baselines.

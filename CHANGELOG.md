# Changelog

All notable changes to this documentation will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [1.1.0] - 2025-10-27

### Changed - Structure & Consistency Improvements

#### Style & Formatting
- Removed all emojis from README.md for more professional tone
- Standardized "Related Resources" section naming across all documentation files
- Improved heading consistency throughout documentation

#### Content Organization
- Moved "Common Technical Issues" section from `technical-reference.md` to `troubleshooting.md` (90+ lines)
- Better separation of concerns: technical reference now focuses on structure/implementation, troubleshooting focuses on problem-solving
- Reduced technical-reference.md from 422 lines to 331 lines for better readability

#### Navigation Improvements
- Added "Related Resources" section to `getting-started/overview.md`
- Standardized all navigation sections to use "Related Resources" instead of mixed "Next Steps" and "Related Guides"
- Enhanced cross-referencing between related documents

### Added - Content Enhancements

#### Editing Forms Guide
- Significantly expanded `guides/editing-forms.md` from 24 lines to 148 lines
- Added "Testing Changes Safely" section with cache bypass parameter usage
- Added "Unpublishing a Form" workflow
- Added "Managing Form Versions" with version control best practices
- Added "Handling Duplicate Records" with three management strategies
- Added "Common Editing Tasks" reference (adding/removing/reordering fields, modifying validation)

#### Glossary & Technical Reference
- Added comprehensive glossary section to `technical-reference.md`
- Defined 7 key technical terms with explanations and cross-references:
  - CDN Caching
  - Domain Authentication
  - Form Capture
  - Journey ID
  - Rate Limiting
  - Logical Name
  - Target Audience
- Added Table of Contents to `technical-reference.md` for easier navigation
- Improved structure and organization of 330+ line technical document

#### Cross-References
- Added hyperlinks from technical terms throughout documentation to glossary
- Linked journey-id references in `overview.md` to glossary
- Linked domain authentication references in `form-capture.md` to glossary
- Linked cache bypass parameter references to detailed explanation
- Linked CDN, domain authentication, and rate limiting in FAQ to glossary
- Added links to Key Concepts section in README.md

#### Conciseness & Clarity
- Tightened wordy introduction in `creating-your-first-form.md` (reduced from 25 to 9 words)
- Consolidated redundant sections in `form-capture.md` overview
- Removed duplicate content from FAQ, replaced with links to full guides:
  - Form capture explanation now links to Form Capture guide
  - Cookie/privacy question now links to Overview
  - Security features now links to Overview
- Improved heading professionalism in `customize-submission-images.md`:
  - "The Problem" → "Overview"
  - "The Solution" → "Implementation"

### Fixed
- Improved documentation structure for easier maintenance
- Enhanced navigation with consistent cross-references
- Better discoverability of related content
- Reduced redundancy between FAQ and detailed guides
- More professional and concise tone throughout

---

## [1.0.0] - 2025-10-27

### Added - Initial Release

#### Documentation Structure
- Created organized documentation structure with four main sections:
  - Getting Started (beginner-friendly tutorials)
  - Guides (comprehensive how-to guides)
  - How-To (task-specific solutions)
  - Reference (FAQs, troubleshooting, and technical documentation)

#### Getting Started
- **Overview** - Introduction to D365 forms, security features, and best practices
- **Creating Your First Form** - Step-by-step guide for beginners

#### Guides
- **Editing Forms** - Complete guide to editing, unpublishing, and managing duplicates
- **Styling Forms** - Theme customization, CSS, and responsive design
- **Advanced Customization** - JavaScript integration, event handling, and custom scripts
- **Form Capture** - External form integration with field mapping examples

#### How-To Articles
- **Customize Submission Images** - Hide or replace default checkmark icon
- **Create Form Templates** - Build reusable templates for consistency

#### Reference
- **FAQ** - 30+ frequently asked questions with detailed answers
- **Troubleshooting** - Comprehensive troubleshooting guide with solutions
- **Technical Reference** - In-depth form structure, element types, field properties, and implementation details

#### Content Improvements
- Consolidated scattered FAQs from original docs
- Added code examples for JavaScript and CSS
- Included mobile responsiveness guidelines
- Added security and compliance best practices
- Created quick reference tables and checklists

---

## Document Migration Notes

### Original Files Reorganized

| Original File | New Location | Notes |
|--------------|--------------|-------|
| `customize-d365-form-doc-overview.md` | `getting-started/overview.md` | Enhanced with additional context |
| `customize-d365-form-doc-create.md` | `getting-started/creating-your-first-form.md` | Expanded with step-by-step instructions |
| `customize-d365-form-doc-edit.md` | `guides/editing-forms.md` | Split styling into separate guide |
| `customize-d365-form-doc-edit.md` (styling section) | `guides/styling-forms.md` | New dedicated styling guide |
| `customize-d365-form-doc-edit.md` (JS section) | `guides/advanced-customization.md` | Expanded with examples |
| `customize-d365-form-doc-form-capture.md` | `guides/form-capture.md` | Enhanced with detailed examples |
| `customize-d365-form-doc-submission-images.md` | `how-to/customize-submission-images.md` | Reformatted for clarity |
| `customize-d365-form-doc-form-troubleshooting.md` | `reference/troubleshooting.md` | Significantly expanded |
| `Technical.md` | `reference/technical-reference.md` | Reorganized with improved structure and formatting |
| FAQs from multiple files | `reference/faq.md` | Consolidated all FAQs |

---

## Future Considerations

### Potential Additions
- Video tutorials and screenshots
- Advanced multi-step form examples
- Integration with Power Automate flows
- A/B testing form variations
- Advanced analytics and reporting
- Accessibility (WCAG) compliance guide
- Multi-language form setup
- Progressive profiling strategies

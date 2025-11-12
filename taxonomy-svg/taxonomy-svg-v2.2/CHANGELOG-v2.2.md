# Changelog

All notable changes to the Taxonomy SVG Generator skill will be documented in this file.

## [2.2.0] - 2025-11-12

### Added
- Enhanced typography with larger, more readable font sizes
- Improved spacing between card items for better readability
- Wider canvas display (2500px) for modern screens
- Better visual hierarchy with optimized font size relationships

### Changed
- Category description font size: 12px → 16px (+33%)
- Card title font size: 13px → 14px (+8%)
- Card item font size: 11px → 12px (+9%)
- Footer font size: 10px → 16px (+60%)
- Category description position: y=50 → y=60 (+10px spacing)
- First card item offset: dy=0 → dy=10
- Card item spacing: dy=17 → dy=25 (+47%)
- Canvas width attribute: 2000px → 2500px (viewBox stays 2000px)

### Fixed
- Footer text: "...the kind" → "...the middle"

### Technical
- Added typography constants for easy customization
- Added spacing constants for consistent layout
- Enhanced output messaging with size and font information
- Improved code documentation and comments

## [2.1.0] - 2025-11-10

### Added
- Automatic date stamping in footer
- Custom attribution footer with personalized message
- Proper date formatting with day names and commas

### Changed
- Footer now displays current generation date
- Footer includes attribution: "Crafted by Varada with help from intelligence"

## [2.0.0] - 2025-11-08

### Added
- 4-level hierarchy support (H1 → H2 → H3 → H4 → H5)
- Nested card structure for subcategories
- Auto-sizing based on number of subcategories
- Category descriptions below titles
- Backward compatibility with dash bullets

### Changed
- Major restructure from 3-level to 4-level system
- H4 now represents subcategory cards
- H5 now represents items within cards
- Improved visual hierarchy and organization

### Technical
- Complete rewrite of category and card generation
- New auto-width calculation for categories
- Enhanced positioning algorithm

## [1.0.0] - 2025-11-01

### Added
- Initial release with basic 3-level structure
- Trunk-and-branch arrow routing
- Color-coded categories (4 color gradient system)
- Endpoint dots on arrows
- Smart spacing and clearances
- Auto-layout with 3 categories per row
- Professional gradients and shadows
- SVG generation from markdown

### Features
- H2 categories with colored gradient backgrounds
- H3 cards inside categories
- Dash-bullet items in cards
- Orthogonal arrow routing with 10px clearances
- Automatic row wrapping

---

## Version Numbering

This project follows [Semantic Versioning](https://semver.org/):
- MAJOR version for incompatible API changes
- MINOR version for backwards-compatible functionality additions
- PATCH version for backwards-compatible bug fixes

## Upgrade Notes

### From v2.1 to v2.2
- **100% backward compatible**
- No markdown syntax changes required
- All existing markdown files work without modification
- Typography and spacing improvements are automatic
- Consider limiting cards to 6-8 items for optimal spacing

### From v2.0 to v2.1
- **100% backward compatible**
- Footer automatically includes date and attribution
- No action required for existing markdown files

### From v1.0 to v2.0
- **Breaking change in markdown structure**
- Must convert 3-level to 4-level:
  - Change `#### Title` to `#### Title` (cards)
  - Change `- Item` to `##### Item` (items)
- See migration guide in SKILL.md

---

**For detailed documentation, see SKILL.md**

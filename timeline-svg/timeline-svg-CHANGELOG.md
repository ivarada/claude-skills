# Changelog

> EDITS PENDING

All notable changes to the Timeline SVG Generator project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [5.1] - 2025-11-13

### Added
- **Automatic header** displaying timeline date range
  - Format: "Timeline - {START_YEAR} - {END_YEAR}"
  - Centered at top in 24px bold font
  - Professional styling in dark gray (#1f2937)
- **Automatic footer** with generation metadata
  - Current date in format: "Wednesday, Nov 14, 2025"
  - Custom attribution text with configurable link
  - Clickable LinkedIn link in attribution
  - Styled in light gray (#9ca3af) with 16px font
- Professional spacing for header (60px) and footer (80px)

### Changed
- Enhanced visual presentation with automatic title and attribution
- Improved spacing between timeline content and canvas edges

### Technical
- Header positioned at y=60 from top
- Footer positioned at y=(canvas_height - 80) from top
- SVG link element added for clickable attribution

## [5.0] - 2025-10-15

### Added
- Enhanced typography with larger, more readable fonts
  - Year labels increased to 18px (previously 16px)
  - Event text increased to 14px (previously 12px)
- Distinctive dotted line pattern for events
  - Stroke dasharray: 1px dot, 12px gap
  - Rounded line caps for smooth appearance
- Improved visual hierarchy with color coding
  - Green years for emphasis on time periods
  - Light gray months for subtle structure
  - Black events for high contrast readability

### Changed
- Thicker axis line (3px, previously 2px) for better visibility
- Thicker month tick marks (2px, previously 1.5px)
- Event tick marks standardized at 1.5px
- Enhanced spacing between elements for clarity

### Improved
- Overall readability and professional appearance
- Better visual separation between timeline elements
- More prominent year markers

## [4.0] - 2025-09-01

### Added
- **Mixed text styling** for events
  - Bold formatting for event titles/dates
  - Regular weight for main descriptions
  - Italic formatting for supplementary notes
- Three-part event format support
  - `title`: Event identifier (bold)
  - `description`: Main content (regular)
  - `notes`: Additional context (italic, optional)
- Extended event tick marks to 120px (previously 100px)

### Changed
- Event display format: "Title (bold) - Description (regular) - Notes (italic)"
- Improved text hierarchy and readability
- Better visual distinction between event components

## [3.0] - 2025-07-15

### Added
- Color-coded timeline elements
  - Green for years (growth and progress)
  - Light gray for months (subtle structure)
  - Black for events and axis (high contrast)
- Enhanced color scheme for better visual hierarchy

### Changed
- Single-line event format with improved spacing
- Standardized color palette across all elements
- Updated font sizes for consistency

### Improved
- Visual clarity through strategic use of color
- Professional appearance with cohesive design
- Better differentiation between timeline components

## [2.0] - 2025-05-20

### Added
- YAML configuration file support
- Customizable tick spacing and lengths
- Configurable SVG canvas width
- Support for arbitrary date ranges

### Changed
- Moved from hardcoded values to YAML configuration
- More flexible event positioning
- Improved file naming convention

### Improved
- Easier customization without code changes
- Better documentation of configuration options

## [1.0] - 2025-03-10

### Added
- Initial release of Timeline SVG Generator
- Basic vertical timeline layout
- Year and month tick marks
- Simple event markers
- SVG output format
- Python script for generation

### Features
- Automatic spacing calculation
- Dynamic viewport sizing
- Embedded CSS styling
- Font-based text rendering

---

## Version Comparison

| Feature | v1.0 | v2.0 | v3.0 | v4.0 | v5.0 | v5.1 |
|---------|------|------|------|------|------|------|
| Basic timeline | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| YAML config | ❌ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Color coding | ❌ | ❌ | ✅ | ✅ | ✅ | ✅ |
| Mixed text styling | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| Enhanced typography | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| Dotted event lines | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ |
| Auto header/footer | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |

## Upgrade Notes

### Upgrading to v5.1
- No breaking changes
- Existing YAML files work without modification
- Timeline title and footer are added automatically
- To customize attribution, edit the footer text in `generate_timeline.py`

### Upgrading to v5.0
- No breaking changes
- Existing YAML files work without modification
- Visual appearance is enhanced automatically
- Existing timelines will look more professional when regenerated

### Upgrading to v4.0
- Event format changed to support three parts (title, description, notes)
- Old single-text events still work but display only in regular weight
- To take advantage of mixed styling, update events to use new three-part format

### Upgrading to v3.0
- No breaking changes
- Colors applied automatically to existing timelines
- Regenerate existing timelines to get color-coded elements

### Upgrading to v2.0
- Configuration moved to YAML file (breaking change)
- Migrate hardcoded values to `timeline.yaml`
- See documentation for YAML structure

## Future Plans

### Planned Features
- [ ] Horizontal timeline orientation option
- [ ] Custom color schemes
- [ ] Interactive HTML output with hover effects
- [ ] Export to PNG/PDF formats
- [ ] Multiple timeline tracks
- [ ] Timezone support for events
- [ ] Recurring events support
- [ ] Date range events (spans)

### Under Consideration
- [ ] GUI configuration tool
- [ ] Web-based timeline editor
- [ ] Template library
- [ ] Animation support
- [ ] Collaborative timeline editing

## Support

For bug reports and feature requests, please open an issue on the [GitHub repository](https://github.com/yourusername/timeline-svg/issues).

---

**Maintained by**: Varada ([@ivarada](https://www.linkedin.com/in/ivarada/))

**License**: MIT

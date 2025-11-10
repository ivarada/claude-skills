# Changelog - Taxonomy SVG Generator

All notable changes to the Taxonomy SVG Generator skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-11-10

### Added
- **4-Level Hierarchy Support**: Complete redesign to support H3 categories → H4 subcategories → H5 items structure
- **Nested Card Layout**: Subcategories now render as white cards nested within colored category boxes
- **Auto-Sizing**: Category boxes automatically size based on the number of subcategories
- **Enhanced Visual Hierarchy**: Clear distinction between categories, subcategories, and items
- **Improved Documentation**: Comprehensive SKILL.md with examples and best practices
- **Migration Guide**: Instructions for converting from 3-level to 4-level structure
- **Optional Metadata**: Support for `row=N` and `height=XXX` parameters in category headers
- **Smart Layout**: Automatic 3-column grid with intelligent wrapping

### Changed
- **Markdown Structure**: Changed from H2/H3 categories to H3/H4/H5 hierarchy
- **Item Syntax**: Items now use `#####` (H5) instead of bullet points (`-`)
- **Box Sizing**: Dynamic width calculation based on subcategory count
- **Card Spacing**: Improved 10px gaps between nested cards
- **Visual Design**: Enhanced shadows, gradients, and professional polish

### Improved
- **Arrow Routing**: More precise trunk-and-branch connections
- **Text Layout**: Better text wrapping and spacing in cards
- **Color System**: Maintains original blue/purple/green/red gradient cycle
- **Spacing System**: Consistent 10px clearance between all elements
- **Documentation**: Extensive examples and troubleshooting guides

### Technical
- **Output Format**: SVG 1.1 compatible, self-contained
- **Dependencies**: Zero external dependencies (stdlib only)
- **Performance**: Efficient layout calculation for large taxonomies
- **Compatibility**: Python 3.6+ required

## [1.0.0] - 2024-09-15

### Added
- Initial release of Taxonomy SVG Generator
- 3-level hierarchy support (H2 categories, H3 cards, bullet points)
- Trunk-and-branch arrow routing system
- Color-coded category boxes with gradients
- Central question box with radiating arrows
- Auto-layout with 3 categories per row
- Professional design with shadows and polish
- Pure Python implementation (no dependencies)
- SVG 1.1 output format

### Features
- Automatic color cycling (blue, purple, green, red)
- Smart spacing with 10px clearances
- Endpoint dots on arrows (3.5px radius)
- Configurable canvas size (2000px width)
- Support for category descriptions
- Flexible card sizing

---

## Version Comparison

### v2.0.0 vs v1.0.0

**Structure Changes:**
- v1.0: H2 → H3 → bullets
- v2.0: H3 → H4 → H5

**Visual Changes:**
- v1.0: Flat card layout within categories
- v2.0: Nested card structure with improved hierarchy

**Migration:**
Replace `- Item` with `##### Item` throughout your markdown files.

---

## Upgrade Guide

### From v1.0 to v2.0

1. **Update Markdown Files**:
   ```markdown
   # Before (v1.0)
   ## CATEGORY
   ### Card Title
   - Item 1
   - Item 2
   
   # After (v2.0)
   ### CATEGORY
   #### Card Title
   ##### Item 1
   ##### Item 2
   ```

2. **Run Migration Script** (if you have many files):
   ```bash
   # Simple sed command for bulk conversion
   sed -i 's/^## /### /g' your-file.md
   sed -i 's/^### /#### /g' your-file.md
   sed -i 's/^- /##### /g' your-file.md
   ```

3. **Regenerate SVGs**:
   ```bash
   python scripts/generate_svg.py your-updated-file.md
   ```

---

## Future Roadmap

### Planned for v2.1.0
- [ ] Export to PNG/PDF formats
- [ ] Interactive SVG with hover effects
- [ ] Custom color scheme support
- [ ] Template system for common taxonomies
- [ ] CLI with more options

### Planned for v3.0.0
- [ ] 5-level hierarchy support
- [ ] Alternative layout styles (circular, radial)
- [ ] Animation support
- [ ] Web-based editor
- [ ] Collaborative editing features

---

## Known Issues

### v2.0.0
- Very long item text (>40 characters) may overflow cards
- Maximum recommended: 5 subcategories per category
- Canvas width is fixed at 2000px
- No built-in text wrapping for extremely long category names

**Workarounds**: See SKILL.md troubleshooting section

---

## Support

For issues, questions, or feature requests:
- GitHub Issues: [Report a bug](https://github.com/yourusername/claude-skills/issues)
- Documentation: See SKILL.md for detailed usage
- Examples: Check the examples/ directory

---

## Contributors

Thank you to everyone who has contributed to this project!

- Initial design and implementation
- Community feedback and testing
- Documentation improvements
- Bug reports and fixes

---

[2.0.0]: https://github.com/yourusername/claude-skills/releases/tag/taxonomy-svg-v2.0.0
[1.0.0]: https://github.com/yourusername/claude-skills/releases/tag/taxonomy-svg-v1.0.0

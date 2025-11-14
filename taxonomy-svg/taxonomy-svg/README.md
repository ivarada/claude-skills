# Taxonomy SVG Generator v2.2

Convert structured markdown hierarchies into professional SVG taxonomy diagrams with nested card support, trunk-and-branch arrow routing, and color-coded categories.

## Version 2.2 - Revised Typography Edition

### What's New in v2.2

**Enhanced Typography:**
- Category descriptions: 12px → 16px (+33% larger)
- Card titles: 13px → 14px (+8% larger)
- Card items: 11px → 12px (+9% larger)
- Footer: 10px → 16px (+60% larger)

**Improved Spacing:**
- Category description position: y=50 → y=60 (more breathing room)
- First card item: dy=0 → dy=10 (consistent spacing)
- Card item spacing: dy=17 → dy=25 (+47% more space)

**Display Enhancement:**
- Canvas width: 2000px → 2500px (better on modern displays)
- ViewBox remains 2000px (maintains coordinate system)

**Content Fix:**
- Footer text corrected: "...the kind" → "...the middle"

### Features

✅ 4-level hierarchy (H1 → H2 → H3 → H4 → H5)
✅ Nested card structure with subcategories
✅ Trunk-and-branch arrow routing
✅ Color-coded categories (blue, purple, green, red)
✅ Professional gradients and shadows
✅ Auto-layout with 3 categories per row
✅ Smart spacing and alignment
✅ Automatic date stamping
✅ Custom footer attribution

### Quick Start

1. Create a markdown file following the structure in `SKILL.md`
2. Run: `python scripts/generate_svg.py your-file.md`
3. Output: `ai-taxonomy-from-md.svg` in same directory

### Markdown Structure

```markdown
# Taxonomy Title
## Central Question?
### CATEGORY NAME
Description text
#### Subcategory Name
##### Item one
##### Item two
```

### Example Output

- Beautifully styled SVG diagrams
- Professional color gradients
- Clear visual hierarchy
- Scalable to any size
- Self-contained (no external dependencies)

### Requirements

- Python 3.6 or higher
- No external packages required (uses only stdlib)

### Documentation

See `SKILL.md` for:
- Complete usage guide
- Markdown structure details
- Design specifications
- Best practices
- Troubleshooting
- Examples

### Version History

- **v2.2** (Nov 2025) - Revised typography and spacing
- **v2.1** (Nov 2025) - Footer attribution
- **v2.0** (Nov 2025) - 4-level nested structure
- **v1.0** (Nov 2025) - Initial release

### License

This skill is provided as-is for creating taxonomy visualizations.

---

**Crafted with attention to detail for clear, professional diagrams.**

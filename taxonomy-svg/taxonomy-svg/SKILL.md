---
name: taxonomy-svg
description: Convert structured markdown hierarchies into professional SVG taxonomy diagrams with nested card support, trunk-and-branch arrow routing, and color-coded categories.
---

# Taxonomy SVG Generator Skill (4-Level Enhanced)

## Overview

This skill converts structured markdown hierarchies into professional SVG taxonomy diagrams with **4-level nested card support**, trunk-and-branch arrow routing, and color-coded categories.

## What This Skill Does

Transforms markdown outlines into beautiful visual taxonomy diagrams featuring:

✅ **4-Level Hierarchy** - Categories with nested subcategory cards
✅ **Trunk-and-Branch Routing** - Clean orthogonal arrow flow
✅ **Color-Coded Categories** - Auto-cycling through blue, purple, green, red
✅ **Endpoint Dots** - Visual termination markers on arrows
✅ **Smart Spacing** - 10px clearance between lines and boxes
✅ **Auto-Layout** - 3 categories per row with automatic wrapping
✅ **Professional Design** - Gradients, shadows, and polish

## Markdown Structure

### 4-Level Hierarchy

```markdown
# Taxonomy Title                    (H1 - Main title)
## Central Question?                (H2 - Central box text)
### CATEGORY NAME                   (H3 - Colored category box)
Description text for category
#### Subcategory Name               (H4 - White nested card)
##### Item one                      (H5 - Bullet point)
##### Item two                      (H5 - Bullet point)
#### Another Subcategory            (H4 - Another nested card)
##### Item three                    (H5 - Bullet point)
```

### Visual Result

```
┌─────────────────────────────────────────┐
│  CATEGORY NAME (colored gradient)       │
│  Description text                       │
│                                         │
│  ┌──────────┐  ┌──────────┐           │
│  │SubCat A  │  │SubCat B  │           │
│  │• Item 1  │  │• Item X  │           │
│  │• Item 2  │  │• Item Y  │           │
│  │• Item 3  │  │• Item Z  │           │
│  └──────────┘  └──────────┘           │
└─────────────────────────────────────────┘
```

## Complete Example

```markdown
# Academic Theory Building

## WHAT MAKES A STRONG THEORY PAPER?

### FOUNDATIONAL ELEMENTS
Core components of theory

#### Conceptual Framework
##### Construct definitions
##### Relationship propositions
##### Boundary conditions
##### Underlying assumptions

#### Theoretical Contribution
##### Novel insights
##### Paradigm extension
##### Integration across domains
##### Mechanism explanation

### VALIDATION CRITERIA
Standards for theory quality

#### Theoretical Rigor
##### Logical consistency
##### Construct clarity
##### Falsifiability
##### Scope conditions

#### Empirical Support
##### Testable propositions
##### Evidence alignment
##### Replication potential
##### Generalizability

### CONTRIBUTION TYPES
Ways theories advance knowledge

#### Incremental
##### Refinement
##### Extension
##### Specification
##### Contextualization

#### Revolutionary
##### Paradigm shift
##### Fundamental reconception
##### New foundations
##### Disruptive insight
```

## Usage

### Step 1: Create Markdown File

Create a `.md` file following the structure above:
- Use H1 (#) for title
- Use H2 (##) for central question
- Use H3 (###) for category names
- Use H4 (####) for subcategory cards
- Use H5 (#####) for items in cards

### Step 2: Generate SVG

```bash
python scripts/generate_svg.py your-file.md
```

The SVG will be created as `ai-taxonomy-from-md.svg` in the same directory.

## Advanced Features

### Optional Metadata

You can add metadata to categories:

```markdown
### CATEGORY NAME | row=2 height=400
```

- `row=N` - Force category to specific row (default: auto-assigned)
- `height=XXX` - Set custom height in pixels (default: 320)

### Category Description

Add a description line right after the category:

```markdown
### CATEGORY NAME
This is the category description
```

The description appears in smaller text below the category name.

## Design Specifications

### Arrow Routing
- **Main trunk**: Single vertical line from central question
- **Horizontal branches**: One per row at 40px above boxes
- **Entry points**: 
  - Left box: Enters from left side
  - Center box: Enters from top
  - Right box: Enters from right side
- **Spacing**: 10px clearance between lines and boxes
- **Endpoint dots**: 3.5px radius circles at termination points

### Color Scheme
Categories cycle through:
1. **Blue** (#1e40af to #93c5fd gradient)
2. **Purple** (#7e22ce to #c084fc gradient)
3. **Green** (#15803d to #86efac gradient)
4. **Red** (#b91c1c to #f87171 gradient)

### Layout
- **Canvas**: 2000px wide, auto-height
- **Categories per row**: 3 (auto-wraps)
- **Category box**: Auto-width based on subcategories
- **Nested cards**: 170px × 190px each
- **Card spacing**: 10px gaps
- **Row spacing**: 60px vertical gaps

## Best Practices

### Category Level (H3)
✅ **DO:**
- Keep names concise (1-4 words)
- Use ALL CAPS for visual consistency
- Add optional description for context

❌ **DON'T:**
- Use long category names (wraps awkwardly)
- Mix capitalization styles

### Subcategory Level (H4)
✅ **DO:**
- Use 2-4 subcategories per category
- Use Title Case for subcategory names
- Balance counts across categories
- Keep titles short (2-4 words)

❌ **DON'T:**
- Exceed 5 subcategories (box gets too wide)
- Use single subcategory (looks odd)

### Item Level (H5)
✅ **DO:**
- Keep items brief (3-7 words)
- Use 3-6 items per subcategory
- Maintain parallel structure
- Use noun phrases

❌ **DON'T:**
- Write long sentences (overflows card)
- Exceed 9 items per card (too tall)
- Mix item types (inconsistent)

## Limitations

### Card Capacity
- **Per card**: Comfortably holds 8-9 items
- **Per category**: Best with 2-4 subcategories
- **Per row**: 3 categories recommended

### Text Length
- **Category names**: ~30 characters max
- **Subcategory names**: ~20 characters max
- **Items**: ~40 characters max

### Canvas Size
- **Width**: Fixed at 2000px
- **Height**: Auto-calculated
- **Maximum categories**: Unlimited (wraps to new rows)

## Troubleshooting

### Problem: Cards overlapping
**Solution**: Reduce subcategories per category or increase CARD_GAP

### Problem: Text overflow in cards
**Solution**: Shorten item text or increase CARD_H in script

### Problem: Category too narrow
**Solution**: Add more subcategories or set custom width

### Problem: Too many rows
**Solution**: Reduce total categories or increase CATEGORIES_PER_ROW

## Migration from 3-Level

If you have existing 3-level taxonomies, convert them:

**Before (3-level):**
```markdown
### CATEGORY
#### Card Title
- Item 1
- Item 2
```

**After (4-level):**
```markdown
### CATEGORY
#### Card Title
##### Item 1
##### Item 2
```

Change `- ` to `##### `!

## Technical Details

### File Structure
```
taxonomy-svg/
├── SKILL.md          (this file)
└── scripts/
    └── generate_svg.py
```

### Dependencies
- Python 3.6+
- No external packages required (uses only stdlib)

### Output Format
- SVG 1.1 compatible
- Embedded styles and gradients
- Self-contained (no external dependencies)
- Scalable to any size

## Examples

### Simple Taxonomy (3 categories, 2 subcategories each)
- **Total elements**: 3 × 2 = 6 subcategory cards
- **Rows**: 1
- **Width**: Fits perfectly on one row

### Medium Taxonomy (6 categories, 3 subcategories each)
- **Total elements**: 6 × 3 = 18 subcategory cards
- **Rows**: 2
- **Layout**: Balanced and readable

### Large Taxonomy (10 categories, 3 subcategories each)
- **Total elements**: 10 × 3 = 30 subcategory cards
- **Rows**: 4
- **Recommendation**: Consider splitting into multiple diagrams

## Pro Tips

1. **Start with structure** - Outline H3/H4 hierarchy first, fill items later
2. **Balance subcategories** - Keep similar counts across categories
3. **Group logically** - Put related items in same subcategory
4. **Test frequently** - Generate SVG often to check layout
5. **Iterate design** - Adjust groupings based on visual feedback
6. **Use descriptions** - Add context to categories when helpful
7. **Print guide** - Keep this guide handy when designing taxonomies

## Footer Attribution

Every generated SVG automatically includes a footer at the bottom with:
- **Current date** in proper format (e.g., "Monday, Nov 10, 2025")
- **Custom attribution**: "Crafted by Varada with help from intelligence (the real, artificial, and somewhere in the kind)"

The footer is:
- Positioned 30px from the bottom
- Centered on the canvas
- Styled in light gray (#9ca3af)
- Automatically updates with the generation date

## Version History

### v2.1 - Footer Attribution (Current)
- ✅ Added automatic date stamp
- ✅ Added custom attribution footer
- ✅ Proper date formatting with commas

### v2.0 - 4-Level Enhanced
- ✅ Added nested card structure (H4 subcategories, H5 items)
- ✅ Auto-sizing based on subcategory count
- ✅ Improved visual hierarchy
- ✅ Enhanced documentation

### v1.0 - Original
- Basic 3-level structure (H2 categories, H3 cards, items)
- Trunk-and-branch routing
- Color coding and spacing

## Support

For issues or questions:
1. Check this SKILL.md for guidance
2. Review the example markdown files
3. Verify markdown structure matches specification
4. Adjust layout constants if needed

## License

This skill is provided as-is for creating taxonomy visualizations.

---

**Happy Taxonomy Building!** 🎨📊

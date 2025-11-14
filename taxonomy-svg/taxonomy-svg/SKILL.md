---
name: taxonomy-svg
description: Convert structured markdown hierarchies into professional SVG taxonomy diagrams with nested card support, trunk-and-branch arrow routing, and color-coded categories.
---

# Taxonomy SVG Generator Skill (4-Level Enhanced)
## Version 2.2 - Revised Typography Edition

## Overview

This skill converts structured markdown hierarchies into professional SVG taxonomy diagrams with **4-level nested card support**, trunk-and-branch arrow routing, and color-coded categories. Version 2.2 introduces improved typography and spacing for enhanced readability.

## What This Skill Does

Transforms markdown outlines into beautiful visual taxonomy diagrams featuring:

✅ **4-Level Hierarchy** - Categories with nested subcategory cards
✅ **Trunk-and-Branch Routing** - Clean orthogonal arrow flow
✅ **Color-Coded Categories** - Auto-cycling through blue, purple, green, red
✅ **Endpoint Dots** - Visual termination markers on arrows
✅ **Smart Spacing** - 10px clearance between lines and boxes
✅ **Auto-Layout** - 3 categories per row with automatic wrapping
✅ **Professional Design** - Gradients, shadows, and polish
✅ **Enhanced Typography** - Optimized font sizes for readability (v2.2)
✅ **Improved Spacing** - Better vertical rhythm in cards (v2.2)

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
│  Description text (larger, clearer)     │
│                                         │
│  ┌──────────┐  ┌──────────┐           │
│  │SubCat A  │  │SubCat B  │           │
│  │          │  │          │           │
│  │• Item 1  │  │• Item X  │           │
│  │          │  │          │           │
│  │• Item 2  │  │• Item Y  │           │
│  │          │  │          │           │
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

The description appears in 16px font below the category name (improved in v2.2).

## Design Specifications

### Typography (v2.2 Revised)

| Element | Font Size | Notes |
|---------|-----------|-------|
| **Main Title** | 32px | Bold, centered |
| **Central Question** | 18px | Bold, gray box |
| **Category Title** | 18px | Bold, white on gradient |
| **Category Description** | **16px** | White, 90% opacity (was 12px) |
| **Card Title** | **14px** | Bold, dark gray (was 13px) |
| **Card Items** | **12px** | Medium gray (was 11px) |
| **Footer** | **16px** | Light gray (was 10px) |

### Spacing (v2.2 Revised)

| Element | Spacing | Notes |
|---------|---------|-------|
| **Category Desc Y-offset** | **60px** | From category top (was 50px) |
| **First Card Item** | **dy=10** | Initial offset (was 0) |
| **Subsequent Items** | **dy=25** | Between bullets (was 17) |
| **Cards Horizontal** | 10px | Between cards |
| **Cards from Edge** | 20px | Padding in category |

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
- **Canvas Display**: 2500px wide (v2.2: wider for better viewing)
- **Canvas ViewBox**: 2000px wide (internal coordinates)
- **Canvas Height**: Auto-calculated based on content
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
- Description will be prominent (16px font)

❌ **DON'T:**
- Use long category names (wraps awkwardly)
- Mix capitalization styles

### Subcategory Level (H4)
✅ **DO:**
- Use 2-4 subcategories per category
- Use Title Case for subcategory names
- Balance counts across categories
- Keep titles short (2-4 words)
- 14px font makes titles clear

❌ **DON'T:**
- Exceed 5 subcategories (box gets too wide)
- Use single subcategory (looks odd)

### Item Level (H5)
✅ **DO:**
- Keep items brief (3-7 words)
- Use 3-6 items per subcategory
- Maintain parallel structure
- Use noun phrases
- Enjoy the improved spacing (25px between items)

❌ **DON'T:**
- Write long sentences (overflows card)
- Exceed 8 items per card (gets too tall with new spacing)
- Mix item types (inconsistent)

## Limitations

### Card Capacity
- **Per card**: Comfortably holds 6-8 items (v2.2: reduced from 9 due to larger spacing)
- **Per category**: Best with 2-4 subcategories
- **Per row**: 3 categories recommended

### Text Length
- **Category names**: ~30 characters max
- **Subcategory names**: ~20 characters max
- **Items**: ~40 characters max

### Canvas Size
- **Display Width**: 2500px (optimized for modern displays)
- **ViewBox Width**: 2000px (internal coordinate system)
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

### Problem: Items look cramped (v2.1 and earlier)
**Solution**: Upgrade to v2.2 for improved 25px spacing

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

## What's New in v2.2

### Typography Improvements
- **Category descriptions** increased from 12px → 16px (33% larger)
- **Card titles** increased from 13px → 14px (better hierarchy)
- **Card items** increased from 11px → 12px (more legible)
- **Footer** increased from 10px → 16px (more visible)

### Spacing Improvements
- **Category description position** moved from y=50 → y=60 (more breathing room)
- **First card item offset** increased from dy=0 → dy=10 (consistent spacing)
- **Card item spacing** increased from dy=17 → dy=25 (47% more space)

### Display Improvements
- **Canvas width attribute** increased from 2000px → 2500px
- ViewBox remains 2000px (maintains coordinate system)
- Better display on high-resolution monitors

### Content Improvements
- **Footer text** corrected: "kind" → "middle"

### Result
Clearer visual hierarchy, improved readability, more professional appearance, better spacing throughout.

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
- **Items per card**: 3-6 recommended with v2.2 spacing

### Medium Taxonomy (6 categories, 3 subcategories each)
- **Total elements**: 6 × 3 = 18 subcategory cards
- **Rows**: 2
- **Layout**: Balanced and readable
- **Items per card**: 4-7 recommended with v2.2 spacing

### Large Taxonomy (10 categories, 3 subcategories each)
- **Total elements**: 10 × 3 = 30 subcategory cards
- **Rows**: 4
- **Items per card**: 3-6 recommended with v2.2 spacing
- **Recommendation**: Consider splitting into multiple diagrams

## Pro Tips

1. **Start with structure** - Outline H3/H4 hierarchy first, fill items later
2. **Balance subcategories** - Keep similar counts across categories
3. **Group logically** - Put related items in same subcategory
4. **Test frequently** - Generate SVG often to check layout
5. **Iterate design** - Adjust groupings based on visual feedback
6. **Use descriptions** - Add context to categories when helpful (now more prominent!)
7. **Print guide** - Keep this guide handy when designing taxonomies
8. **Limit items** - With v2.2 spacing, 6-8 items per card is optimal
9. **Embrace whitespace** - The improved spacing makes diagrams more readable
10. **Check on multiple displays** - The 2500px width displays well on various screens

## Footer Attribution

Every generated SVG automatically includes a footer at the bottom with:
- **Current date** in proper format (e.g., "Wednesday, Nov 12, 2025")
- **Custom attribution**: "Crafted by Varada with help from intelligence (the real, artificial, and somewhere in the middle)"

The footer is:
- Positioned 30px from the bottom
- Centered on the canvas
- Styled in light gray (#9ca3af)
- Now displayed in 16px font (v2.2: was 10px)
- Automatically updates with the generation date

## Version History

### v2.2 - Revised Typography and Spacing (Current)
- ✅ Increased category description font: 12px → 16px
- ✅ Increased card title font: 13px → 14px
- ✅ Increased card item font: 11px → 12px
- ✅ Increased footer font: 10px → 16px
- ✅ Adjusted category description position: y=50 → y=60
- ✅ Improved card item spacing: first dy=0→10, subsequent dy=17→25
- ✅ Updated canvas width attribute: 2000 → 2500 (viewBox stays 2000)
- ✅ Fixed footer text: "kind" → "middle"
- ✅ Enhanced visual hierarchy and readability

### v2.1 - Footer Attribution
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

## Comparison: v2.1 vs v2.2

| Feature | v2.1 | v2.2 | Improvement |
|---------|------|------|-------------|
| Cat Description | 12px | 16px | +33% |
| Card Title | 13px | 14px | +8% |
| Card Item | 11px | 12px | +9% |
| Footer | 10px | 16px | +60% |
| Item Spacing | 17px | 25px | +47% |
| Cat Desc Position | y=50 | y=60 | Better spacing |
| Canvas Width | 2000px | 2500px | Wider display |

## Support

For issues or questions:
1. Check this SKILL.md for guidance
2. Review the example markdown files
3. Verify markdown structure matches specification
4. Adjust layout constants if needed
5. Consider upgrading to v2.2 if using older version

## Backward Compatibility

✅ All v2.2 changes are purely presentational
✅ Existing markdown files work without modification
✅ No changes to parsing logic or structure
✅ Colors, gradients, and routing unchanged

## License

This skill is provided as-is for creating taxonomy visualizations.

---

**Happy Taxonomy Building!** 🎨📊

*Now with enhanced typography for even better readability!*

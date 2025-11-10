# Taxonomy SVG Generator

Convert structured markdown hierarchies into professional SVG taxonomy diagrams with nested card support, trunk-and-branch arrow routing, and color-coded categories.

![Version](https://img.shields.io/badge/version-2.0-blue)
![Python](https://img.shields.io/badge/python-3.6+-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

## 🎯 Features

- **4-Level Hierarchy** - Categories with nested subcategory cards
- **Trunk-and-Branch Routing** - Clean orthogonal arrow flow from central concept
- **Color-Coded Categories** - Auto-cycling through blue, purple, green, and red gradients
- **Smart Spacing** - 10px clearance between lines and boxes
- **Auto-Layout** - 3 categories per row with automatic wrapping
- **Professional Design** - Gradients, shadows, and polished visual presentation
- **No Dependencies** - Pure Python using only standard library

## 📸 Example Output

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

## 🚀 Quick Start

### Installation

No installation required! Just Python 3.6+.

```bash
git clone https://github.com/yourusername/taxonomy-svg.git
cd taxonomy-svg
```

### Basic Usage

1. Create a markdown file with your taxonomy structure:

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
```

2. Generate the SVG:

```bash
python scripts/generate_svg.py your-taxonomy.md
```

3. Open `ai-taxonomy-from-md.svg` in your browser or design tool!

## 📝 Markdown Structure

### Hierarchy Levels

```markdown
# Taxonomy Title                    (H1 - Main title)
## Central Question?                (H2 - Central box text)
### CATEGORY NAME                   (H3 - Colored category box)
Description text for category
#### Subcategory Name               (H4 - White nested card)
##### Item one                      (H5 - Bullet point)
##### Item two                      (H5 - Bullet point)
```

### Visual Result

Each category becomes a gradient-colored box containing nested subcategory cards. Arrows flow from a central question box to all categories using a trunk-and-branch routing system.

## 🎨 Design Specifications

### Color Scheme

Categories automatically cycle through four color gradients:

1. **Blue** - #1e40af to #93c5fd
2. **Purple** - #7e22ce to #c084fc
3. **Green** - #15803d to #86efac
4. **Red** - #b91c1c to #f87171

### Layout

- **Canvas Width**: 2000px (fixed)
- **Height**: Auto-calculated based on content
- **Categories per Row**: 3 (automatically wraps)
- **Nested Cards**: 170px × 190px each
- **Spacing**: 10px gaps between elements
- **Row Spacing**: 60px vertical gaps

### Arrow System

- Main trunk from central question
- Horizontal branches per row (40px above boxes)
- Three entry points:
  - Left box: Enters from left side
  - Center box: Enters from top
  - Right box: Enters from right side
- Endpoint dots (3.5px radius) at arrow terminations
- 10px clearance from all boxes

## 🔧 Advanced Features

### Optional Metadata

Control category positioning and sizing:

```markdown
### CATEGORY NAME | row=2 height=400
```

Parameters:
- `row=N` - Force category to specific row number
- `height=XXX` - Set custom height in pixels

### Category Descriptions

Add descriptive text after category names:

```markdown
### CATEGORY NAME
This description appears below the category name in smaller text
```

## 📏 Best Practices

### ✅ DO

- Keep category names concise (1-4 words, ALL CAPS)
- Use 2-4 subcategories per category
- Keep items brief (3-7 words)
- Use 3-6 items per subcategory
- Maintain parallel structure across items

### ❌ DON'T

- Use long category names (wraps awkwardly)
- Exceed 5 subcategories per category (too wide)
- Write long sentences in items (overflows cards)
- Use single subcategory per category (looks odd)
- Exceed 9 items per card (too tall)

## 📦 Use Cases

Perfect for visualizing:

- Academic frameworks and theories
- Research taxonomies
- Conceptual models
- Knowledge classification systems
- Decision frameworks
- Process categories
- Strategic planning frameworks
- Educational concept maps

## 🔄 Migration from v1.0

If you have existing 3-level taxonomies:

**Before (v1.0):**
```markdown
### CATEGORY
#### Card Title
- Item 1
- Item 2
```

**After (v2.0):**
```markdown
### CATEGORY
#### Card Title
##### Item 1
##### Item 2
```

Simply change `- ` to `##### `!

## 🛠️ Technical Details

### Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

### Output Format

- SVG 1.1 compatible
- Embedded styles and gradients
- Self-contained (no external files)
- Scalable to any size without quality loss

### File Structure

```
taxonomy-svg/
├── README.md
├── SKILL.md
├── LICENSE
└── scripts/
    └── generate_svg.py
```

## 🐛 Troubleshooting

**Problem: Cards overlapping**
- Solution: Reduce subcategories per category or increase spacing in script

**Problem: Text overflow in cards**
- Solution: Shorten item text or increase card height

**Problem: Category too narrow**
- Solution: Add more subcategories or set custom width

**Problem: Too many rows**
- Solution: Reduce total categories or split into multiple diagrams

## 📚 Examples

Check the `examples/` directory for sample markdown files and their generated SVGs:

- `simple-taxonomy.md` - Basic 3-category example
- `medium-taxonomy.md` - 6-category balanced layout
- `complex-taxonomy.md` - Full-featured example with all options

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Designed for use with Claude AI skills system
- Inspired by academic taxonomy visualization needs
- Built with feedback from research and education communities

## 📧 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/taxonomy-svg/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/taxonomy-svg/discussions)
- **Documentation**: See [SKILL.md](SKILL.md) for detailed technical documentation

## 🔗 Related Projects

- [Crossref Lookup](https://github.com/yourusername/crossref-lookup) - Academic citation tools
- [OpenLibrary Lookup](https://github.com/yourusername/openlibrary-lookup) - Book citation tools

---

**Made with ❤️ for researchers, educators, and visual thinkers**

*Star ⭐ this repository if you find it useful!*

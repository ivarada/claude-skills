# Claude Skills Collection

A curated collection of three powerful Claude AI skills for academic research, visualization, and citation management. These tools help researchers, students, and educators work more efficiently with [...]

![Python](https://img.shields.io/badge/python-3.6+-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Skills](https://img.shields.io/badge/skills-3-orange)

## 🎯 What's Inside

This repository contains three production-ready Claude skills:

### 📊 [Taxonomy SVG Generator](https://github.com/ivarada/claude-skills/tree/main/taxonomy-svg)
Convert structured markdown hierarchies into beautiful SVG taxonomy diagrams with nested cards, color-coded categories, and professional arrow routing.

**Perfect for:** Academic frameworks, research taxonomies, conceptual models, knowledge classification

### 📚 [Crossref Lookup](https://github.com/ivarada/claude-skills/tree/main/crossref-lookup)
Academic publication metadata retrieval and citation generation using the Crossref REST API. Look up DOIs, search papers, and generate citations instantly.

**Perfect for:** Literature reviews, bibliography generation, research validation, citation management

### 📖 [OpenLibrary Lookup](https://github.com/ivarada/claude-skills/tree/main/openlibrary-lookup)
Book lookup, search, and citation generation using the OpenLibrary API. Search books, look up ISBNs, and create formatted citations.

**Perfect for:** Book citations, reading lists, library cataloging, bibliography creation

## 🚀 Quick Start

### Installation

Clone the repository:

```bash
git clone https://github.com/ivarada/claude-skills.git
cd claude-skills
```

Install Python dependencies:

```bash
pip install requests --break-system-packages
```

### Using with Claude

These skills are designed to work with Claude AI's skills system:

1. **Copy to Skills Directory**: Place each skill folder in your Claude skills directory
2. **Reference in Prompts**: Claude will automatically use these skills when relevant
3. **Manual Execution**: Run scripts directly from command line for standalone use

## 📚 Skill Documentation

Each skill has its own comprehensive documentation:

- **[Taxonomy SVG README](https://github.com/ivarada/claude-skills/blob/main/taxonomy-svg/taxonomy-svg-README.md)** - Complete guide to creating visual taxonomies
- **[Crossref Lookup README](https://github.com/ivarada/claude-skills/blob/main/crossref-lookup/crossref-lookup-README.md)** - Academic citation tools documentation
- **[OpenLibrary Lookup README](https://github.com/ivarada/claude-skills/blob/main/openlibrary-lookup/openlibrary-lookup-README.md)** - Book citation tools guide

## 🎨 Use Cases

### For Researchers

```bash
# Generate citations for your paper
cd crossref-lookup
python scripts/citation_lookup.py bib.doi == 10.1038/nature12373

# Create a visual framework
cd ../taxonomy-svg
python scripts/generate_svg.py research-framework.md

# Add book citations
cd ../openlibrary-lookup
python scripts/book_lookup.py bib.isbn == 9780140328721
```

### For Students

```bash
# Build your bibliography
cd crossref-lookup
python scripts/search_by_author.py "Einstein" --rows 10

cd ../openlibrary-lookup
python scripts/search_books.py "quantum physics" --limit 10

# Organize concepts visually
cd ../taxonomy-svg
python scripts/generate_svg.py study-guide.md
```

### For Educators

```bash
# Create course taxonomies
cd taxonomy-svg
python scripts/generate_svg.py course-outline.md

# Build reading lists with citations
cd ../openlibrary-lookup
python scripts/book_lookup.py "Thinking Fast and Slow"

# Find relevant research
cd ../crossref-lookup
python scripts/search_works.py "educational psychology" --rows 20
```

## 📦 Repository Structure

```
claude-skills/
├── README.md
├── LICENSE
│
├── taxonomy-svg/
│   ├── taxonomy-svg-CHANGELOG.md
│   ├── taxonomy-svg.skill
│   ├── taxonomy-svg-README.md
│
├── crossref-lookup/
│   ├── crossref-lookup-README.md
│   ├── crossref-lookup.skill
│   ├── crossref-lookup-CHANGELOG.md
│
└── openlibrary-lookup/
    ├── openlibrary-lookup-README.md
    ├── openlibrary-lookup.skill
    ├── openlibrary-lookup-CHANGELOG.md
```

## 🔧 Requirements

### System Requirements
- Python 3.6 or higher
- Internet connection (for API-based tools)

### Python Dependencies
- `requests` library (for Crossref and OpenLibrary skills)

```bash
pip install requests --break-system-packages
```

### No Dependencies
- **Taxonomy SVG** uses only Python standard library

## 🌟 Features Comparison

| Feature | Taxonomy SVG | Crossref Lookup | OpenLibrary Lookup |
|---------|-------------|-----------------|-------------------|
| **Purpose** | Visualization | Paper Citations | Book Citations |
| **Input** | Markdown | DOI/Query | ISBN/Title |
| **Output** | SVG Diagram | Citations/JSON | Citations/JSON |
| **API Required** | No | Yes (Free) | Yes (Free) |
| **Dependencies** | None | requests | requests |
| **Use Case** | Frameworks | Research Papers | Books |

## 🎓 Workflows

### Complete Research Workflow

1. **Find Papers** (Crossref Lookup)
   ```bash
   cd crossref-lookup
   python scripts/search_works.py "your topic" --rows 20
   ```

2. **Generate Citations** (Crossref Lookup)
   ```bash
   python scripts/citation_lookup.py bib.doi == 10.1038/xxxx
   ```

3. **Find Related Books** (OpenLibrary Lookup)
   ```bash
   cd ../openlibrary-lookup
   python scripts/search_books.py "your topic" --limit 10
   ```

4. **Create Bibliography** (OpenLibrary Lookup)
   ```bash
   cd ../openlibrary-lookup
   python scripts/book_lookup.py bib.isbn == 9780140328721
   ```

5. **Visualize Framework** (Taxonomy SVG)
   ```bash
   cd ../taxonomy-svg
   python scripts/generate_svg.py my-research-framework.md
   ```

## 🐛 Troubleshooting

### Common Issues

**Problem: Import errors**
```bash
# Solution: Install dependencies
pip install requests --break-system-packages
```

**Problem: API timeouts**
- Normal during peak hours
- Scripts have automatic retry logic
- Try again in a few minutes

**Problem: Skill not recognized by Claude**
- Ensure skill folder is in correct location
- Check SKILL.md file exists
- Verify folder name matches skill name

**Problem: SVG not rendering**
- Check markdown structure matches specification
- Validate H1-H5 hierarchy
- Review example files in taxonomy-svg/

### Getting Help

1. Check individual skill README files
2. Review SKILL.md technical documentation
3. See CHANGELOG.md for known issues
4. Open an issue on GitHub: https://github.com/ivarada/claude-skills/issues

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute

1. **Bug Reports**: Found an issue? Open a GitHub issue: https://github.com/ivarada/claude-skills/issues
2. **Feature Requests**: Have an idea? Start a discussion via the Issues page
3. **Code Contributions**: Submit a pull request against this repository
4. **Documentation**: Improve guides and examples
5. **Examples**: Share your use cases and workflows

### Contribution Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Make your changes
4. Test thoroughly
5. Commit with clear messages (`git commit -m 'Add YourFeature'`)
6. Push to your branch (`git push origin feature/YourFeature`)
7. Open a Pull Request against https://github.com/ivarada/claude-skills

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/ivarada/claude-skills/blob/main/LICENSE) file for details.

### What This Means
- ✅ Commercial use allowed
- ✅ Modification allowed
- ✅ Distribution allowed
- ✅ Private use allowed
- ❌ No liability
- ❌ No warranty

## 🙏 Acknowledgments

### APIs and Services
- **Crossref** - Free academic metadata API
- **OpenLibrary** - Free book metadata from Internet Archive
- **Anthropic** - Claude AI skills system

### Community
- Research community for feedback and feature requests
- Open source contributors
- Academic institutions using these tools
- Students and educators worldwide

## 📧 Support

### Getting Help
- **Documentation**: Check individual skill READMEs in this repo
- **Issues**: https://github.com/ivarada/claude-skills/issues

### Contact
- **GitHub**: https://github.com/ivarada

## 🔗 Related Resources

### External Links
- [Claude AI Documentation](https://docs.claude.com)
- [Crossref API Docs](https://api.crossref.org)
- [OpenLibrary API Docs](https://openlibrary.org/dev/docs/api)

### Related Projects
- Citation management tools
- Academic research software
- Visualization libraries
- Bibliography generators

## 📈 Version History

See individual CHANGELOG.md files for detailed version history:
- [Taxonomy SVG Changelog](./taxonomy-svg/taxonomy-svg-CHANGELOG.md)
- [Crossref Lookup Changelog](./crossref-lookup/crossref-lookup-CHANGELOG.md)
- [OpenLibrary Lookup Changelog](./openlibrary-lookup/openlibrary-lookup-CHANGELOG.md)

---

## ⭐ Show Your Support

If you find these skills useful:

1. **Star this repository** ⭐: https://github.com/ivarada/claude-skills
2. **Share with colleagues** 📢
3. **Contribute improvements** 🔧
4. **Cite in your research** 📚
5. **Follow for updates** 👀

---

**Made with ❤️ for researchers, students, and educators worldwide**

*Empowering academic work through better tools*

### Quick Links
- [Taxonomy SVG](https://github.com/ivarada/claude-skills/tree/main/taxonomy-svg)
- [Crossref Lookup](https://github.com/ivarada/claude-skills/tree/main/crossref-lookup)
- [OpenLibrary Lookup](https://github.com/ivarada/claude-skills/tree/main/openlibrary-lookup)
- [Issues](https://github.com/ivarada/claude-skills/issues)

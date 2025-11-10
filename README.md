# Claude Skills Collection

A curated collection of three powerful Claude AI skills for academic research, visualization, and citation management. These tools help researchers, students, and educators work more efficiently with academic content.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.6+-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)
![Skills](https://img.shields.io/badge/skills-3-orange)

## 🎯 What's Inside

This repository contains three production-ready Claude skills:

### 📊 [Taxonomy SVG Generator](./taxonomy-svg)
Convert structured markdown hierarchies into beautiful SVG taxonomy diagrams with nested cards, color-coded categories, and professional arrow routing.

**Perfect for:** Academic frameworks, research taxonomies, conceptual models, knowledge classification

### 📚 [Crossref Lookup](./crossref-lookup)
Academic publication metadata retrieval and citation generation using the Crossref REST API. Look up DOIs, search papers, and generate citations instantly.

**Perfect for:** Literature reviews, bibliography generation, research validation, citation management

### 📖 [OpenLibrary Lookup](./openlibrary-lookup)
Book lookup, search, and citation generation using the OpenLibrary API. Search books, look up ISBNs, and create formatted citations.

**Perfect for:** Book citations, reading lists, library cataloging, bibliography creation

## 🚀 Quick Start

### Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/claude-skills-collection.git
cd claude-skills-collection
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

- **[Taxonomy SVG README](./taxonomy-svg/README.md)** - Complete guide to creating visual taxonomies
- **[Crossref Lookup README](./crossref-lookup/README.md)** - Academic citation tools documentation
- **[OpenLibrary Lookup README](./openlibrary-lookup/README.md)** - Book citation tools guide

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
claude-skills-collection/
├── README.md                    # This file
├── LICENSE                      # MIT License
│
├── taxonomy-svg/               # Visual taxonomy generator
│   ├── README.md
│   ├── SKILL.md
│   ├── CHANGELOG.md
│   └── scripts/
│       └── generate_svg.py
│
├── crossref-lookup/            # Academic citation tools
│   ├── README.md
│   ├── SKILL.md
│   ├── CHANGELOG.md
│   ├── scripts/
│   │   ├── citation_lookup.py
│   │   ├── doi_lookup.py
│   │   ├── search_works.py
│   │   ├── search_by_author.py
│   │   ├── generate_apa7_citation.py
│   │   ├── generate_bibtex.py
│   │   └── journal_lookup.py
│   └── references/
│       ├── api_reference.md
│       ├── response_schemas.md
│       ├── citation_formats.md
│       └── filters_guide.md
│
└── openlibrary-lookup/         # Book citation tools
    ├── README.md
    ├── SKILL.md
    ├── CHANGELOG.md
    ├── scripts/
    │   ├── book_lookup.py
    │   ├── search_books.py
    │   ├── isbn_lookup.py
    │   ├── get_author_info.py
    │   ├── generate_apa7_citation.py
    │   └── generate_bibtex.py
    └── references/
        ├── api_reference.md
        ├── response_schemas.md
        └── citation_formats.md
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
   python scripts/book_lookup.py bib.isbn == 9780140328721
   ```

5. **Visualize Framework** (Taxonomy SVG)
   ```bash
   cd ../taxonomy-svg
   python scripts/generate_svg.py my-research-framework.md
   ```

### Literature Review Workflow

1. Search papers by topic
2. Filter by date and relevance
3. Generate citations for selected papers
4. Create conceptual taxonomy of findings
5. Export complete bibliography

### Teaching Material Workflow

1. Create course taxonomy diagram
2. Build reading list with citations
3. Find supplementary papers
4. Organize all references
5. Generate student handouts

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
4. Open an issue on GitHub

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute

1. **Bug Reports**: Found an issue? Open a GitHub issue
2. **Feature Requests**: Have an idea? Start a discussion
3. **Code Contributions**: Submit a pull request
4. **Documentation**: Improve guides and examples
5. **Examples**: Share your use cases and workflows

### Contribution Process

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Make your changes
4. Test thoroughly
5. Commit with clear messages (`git commit -m 'Add YourFeature'`)
6. Push to your branch (`git push origin feature/YourFeature`)
7. Open a Pull Request

### Development Guidelines

- Follow existing code style
- Add tests for new features
- Update documentation
- Include examples
- Test with Claude AI when applicable

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### What This Means

✅ Commercial use allowed
✅ Modification allowed
✅ Distribution allowed
✅ Private use allowed
❌ No liability
❌ No warranty

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
- **Documentation**: Check individual skill READMEs
- **Issues**: [GitHub Issues](https://github.com/yourusername/claude-skills-collection/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/claude-skills-collection/discussions)

### Contact
- **Email**: your-email@example.com
- **GitHub**: [@yourusername](https://github.com/yourusername)

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

## 📊 Statistics

- **3** Production-ready skills
- **13** Python scripts
- **7** Reference guides
- **100+** Combined features
- **0** External dependencies (Taxonomy SVG)
- **Free** API access (Crossref & OpenLibrary)

## 🗺️ Roadmap

### Planned Features

**v1.1.0** (Q1 2025)
- [ ] Additional citation formats (MLA, Chicago)
- [ ] Batch processing utilities
- [ ] Web interface for all skills
- [ ] Export to reference managers

**v1.2.0** (Q2 2025)
- [ ] Enhanced search filters
- [ ] Multi-language support
- [ ] Integration with other academic APIs
- [ ] Automated testing suite

**v2.0.0** (Future)
- [ ] GUI applications
- [ ] Cloud deployment options
- [ ] Mobile companion apps
- [ ] AI-powered recommendations

### Community Requests
See our [GitHub Issues](./issues) for community-requested features.

## 📈 Version History

See individual CHANGELOG.md files for detailed version history:
- [Taxonomy SVG Changelog](./taxonomy-svg-CHANGELOG.md)
- [Crossref Lookup Changelog](./crossref-lookup-CHANGELOG.md)
- [OpenLibrary Lookup Changelog](./openlibrary-lookup-CHANGELOG.md)

---

## ⭐ Show Your Support

If you find these skills useful:

1. **Star this repository** ⭐
2. **Share with colleagues** 📢
3. **Contribute improvements** 🔧
4. **Cite in your research** 📚
5. **Follow for updates** 👀

---

**Made with ❤️ for researchers, students, and educators worldwide**

*Empowering academic work through better tools*

### Quick Links
• [Taxonomy SVG](./taxonomy-svg.skill)
• [Crossref Lookup](./crossref-lookup.skill)
• [OpenLibrary Lookup](./openlibrary-lookup.skill)
• [Issues](ivarada/claude-skills/issues)
• [Contribute](#contributing)

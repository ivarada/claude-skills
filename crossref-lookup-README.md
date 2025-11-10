# Crossref Lookup

Academic publication metadata retrieval and citation generation using the Crossref REST API. Look up DOIs, search papers, generate citations, and create BibTeX entries - all from the command line.

![Version](https://img.shields.io/badge/version-2.0-blue)
![Python](https://img.shields.io/badge/python-3.6+-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

## 🎯 Features

- **Unified Citation Tool** - Single command for complete citations (NEW!)
- **DOI Lookup** - Retrieve complete publication metadata
- **Publication Search** - Search Crossref's 150M+ records
- **Author Search** - Find papers by specific authors
- **APA 7 Citations** - Generate formatted academic citations
- **BibTeX Generation** - Create Zotero-compatible entries
- **Journal Information** - Look up journal details by ISSN
- **Rate Limit Friendly** - Respects API etiquette and quotas

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/yourusername/crossref-lookup.git
cd crossref-lookup
pip install requests --break-system-packages
```

### Instant Citation (NEW!)

The fastest way to get a complete citation:

```bash
# Using the convenient bib.doi format
python scripts/citation_lookup.py bib.doi == 10.1038/s41586-025-09663-y

# Or just pass the DOI directly
python scripts/citation_lookup.py 10.1038/nature12373
python scripts/citation_lookup.py https://doi.org/10.1038/nature12373
```

**Outputs:**
- ✅ Complete publication information
- ✅ APA 7th edition citation (saved to `<doi>_apa7.txt`)
- ✅ BibTeX entry (saved to `<doi>.bib`)
- ✅ JSON metadata for programmatic use

### Basic Usage Examples

```bash
# Look up a specific DOI
python scripts/doi_lookup.py 10.1038/nature12373

# Search for papers
python scripts/search_works.py "machine learning" --rows 10

# Find papers by author
python scripts/search_by_author.py "Jane Smith" --rows 20

# Generate APA citation
python scripts/generate_apa7_citation.py 10.1038/nature12373

# Generate BibTeX
python scripts/generate_bibtex.py 10.1038/nature12373

# Look up journal info
python scripts/journal_lookup.py 0028-0836
```

## 📚 Script Reference

### citation_lookup.py (Unified Tool)

**All-in-one DOI lookup with complete citation generation**

```bash
python scripts/citation_lookup.py [bib.doi ==] <doi>
```

**Features:**
- Accepts DOI with or without URL prefix
- Supports `bib.doi == <doi>` format for convenience
- Generates both APA7 and BibTeX automatically
- Saves citations to files for easy reference
- Returns comprehensive JSON output

**Examples:**
```bash
python scripts/citation_lookup.py bib.doi == 10.1038/s41586-025-09663-y
python scripts/citation_lookup.py 10.1371/journal.pone.0161344
python scripts/citation_lookup.py https://doi.org/10.1038/nature12373
```

### doi_lookup.py

**Retrieve complete metadata for any DOI**

```bash
python scripts/doi_lookup.py <doi>
```

Returns full publication metadata including:
- Title, authors, and affiliations
- Journal name and ISSN
- Publication dates
- Volume, issue, pages
- Abstract (when available)
- References and citations
- License information

### search_works.py

**Search Crossref's 150+ million records**

```bash
python scripts/search_works.py "<query>" [--rows N] [--filter "params"]
```

**Query Tips:**
- Plain text searches across titles, abstracts, and full text
- Use filters for date ranges, publication types, etc.
- Control result count with `--rows` (default: 10)

**Examples:**
```bash
python scripts/search_works.py "climate change" --rows 20
python scripts/search_works.py "CRISPR" --filter "from-pub-date:2020"
python scripts/search_works.py "quantum computing" --filter "type:journal-article"
```

### search_by_author.py

**Find publications by author name**

```bash
python scripts/search_by_author.py "<author_name>" [--rows N]
```

**Examples:**
```bash
python scripts/search_by_author.py "Einstein" --rows 20
python scripts/search_by_author.py "Marie Curie"
```

### generate_apa7_citation.py

**Create APA 7th edition citations**

```bash
python scripts/generate_apa7_citation.py <doi>
```

**Supported Formats:**
- Journal articles
- Books and book chapters
- Conference papers
- Reports and datasets
- Preprints

**Output Example:**
```
Smith, J. A., & Johnson, M. B. (2023). Machine learning in healthcare: 
    A comprehensive review. Nature Medicine, 29(4), 1234-1245. 
    https://doi.org/10.1038/s41591-023-12345-6
```

### generate_bibtex.py

**Generate Zotero-compatible BibTeX entries**

```bash
python scripts/generate_bibtex.py <doi>
```

**Output Example:**
```bibtex
@article{smith2023machine,
  title = {Machine learning in healthcare: A comprehensive review},
  author = {Smith, John A. and Johnson, Mary B.},
  journal = {Nature Medicine},
  volume = {29},
  number = {4},
  pages = {1234--1245},
  year = {2023},
  doi = {10.1038/s41591-023-12345-6}
}
```

### journal_lookup.py

**Get journal information by ISSN**

```bash
python scripts/journal_lookup.py <issn>
```

Returns journal metadata including:
- Full journal title
- Publisher information
- Subject classifications
- ISSN (print and electronic)
- Coverage dates

## 📖 Advanced Usage

### Filtering Search Results

Use the `--filter` parameter for advanced queries:

```bash
# Papers from specific date range
python scripts/search_works.py "AI" --filter "from-pub-date:2020,until-pub-date:2023"

# Specific publication type
python scripts/search_works.py "genome" --filter "type:journal-article"

# Specific journal (by ISSN)
python scripts/search_works.py "evolution" --filter "issn:0028-0836"

# Open access only
python scripts/search_works.py "COVID-19" --filter "has-license:true"
```

### API Etiquette

The Crossref API is free but has etiquette guidelines:

✅ **DO:**
- Include your email in requests (scripts use `mailto` parameter)
- Cache responses when making multiple requests
- Use specific queries rather than broad searches
- Respect rate limits (50 requests/second free, higher for polite pool)

❌ **DON'T:**
- Make excessive requests
- Hammer the API without timeouts
- Ignore error responses
- Skip the polite pool parameters

## 🔧 Configuration

All scripts use reasonable defaults:
- **Timeout**: 15 seconds per request
- **User Agent**: Includes polite pool email
- **Rate Limiting**: Automatic retry on 429 errors
- **Error Handling**: Graceful degradation

To customize, edit the scripts directly or use environment variables.

## 📁 Reference Documentation

Comprehensive guides in the `references/` directory:

- **api_reference.md** - Complete API endpoint documentation
- **response_schemas.md** - JSON structure and field definitions
- **citation_formats.md** - Citation style guides and examples
- **filters_guide.md** - Advanced search filter parameters

## 🎓 Use Cases

Perfect for:

- **Researchers** - Quick citation generation for papers
- **Librarians** - Batch metadata retrieval
- **Developers** - Building citation tools and reference managers
- **Students** - Finding relevant papers and generating bibliographies
- **Publishers** - Validating DOIs and metadata
- **Data Scientists** - Analyzing publication trends and networks

## 🛠️ Requirements

- Python 3.6 or higher
- `requests` library

```bash
pip install requests --break-system-packages
```

## 📦 File Structure

```
crossref-lookup/
├── README.md
├── SKILL.md
├── LICENSE
├── scripts/
│   ├── citation_lookup.py      # Unified citation tool (NEW!)
│   ├── doi_lookup.py
│   ├── search_works.py
│   ├── search_by_author.py
│   ├── generate_apa7_citation.py
│   ├── generate_bibtex.py
│   └── journal_lookup.py
└── references/
    ├── api_reference.md
    ├── response_schemas.md
    ├── citation_formats.md
    └── filters_guide.md
```

## 🐛 Troubleshooting

**Problem: "DOI not found"**
- Verify the DOI is correct and exists
- Try searching for the paper first
- Check if the DOI is recently registered

**Problem: Slow responses**
- Normal for Crossref API during peak times
- Scripts use 15-second timeout
- Try again in a few minutes

**Problem: Rate limit errors**
- You're making too many requests too quickly
- Scripts handle this automatically with retry logic
- Consider caching results for repeated lookups

**Problem: Missing metadata**
- Not all DOIs have complete metadata
- Try the DOI directly at doi.org to verify
- Some fields are optional in Crossref

## 🔍 Tips & Tricks

1. **Batch Processing**: Write a shell loop to process multiple DOIs
2. **Caching**: Save JSON responses to avoid repeated API calls
3. **Search Strategies**: Start broad, then narrow with filters
4. **Citation Verification**: Always verify citations before publication
5. **API Monitoring**: Check Crossref status page if issues persist

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewScript`)
3. Commit your changes (`git commit -m 'Add new script'`)
4. Push to the branch (`git push origin feature/NewScript`)
5. Open a Pull Request

**Ideas for contributions:**
- Additional citation formats (MLA, Chicago, etc.)
- Export to reference managers (EndNote, Mendeley)
- Batch processing utilities
- Web interface
- Integration with other APIs

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Crossref** - For providing free API access to academic metadata
- **Claude AI** - Skill system integration
- **Research Community** - Feedback and feature requests

## 📧 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/crossref-lookup/issues)
- **Crossref API Docs**: [api.crossref.org](https://api.crossref.org)
- **Email**: your-email@example.com

## 🔗 Related Projects

- [Taxonomy SVG](https://github.com/yourusername/taxonomy-svg) - Visual taxonomy diagrams
- [OpenLibrary Lookup](https://github.com/yourusername/openlibrary-lookup) - Book citations

---

**Made with ❤️ for the research community**

*If this tool helps your research, consider citing Crossref in your acknowledgments!*

⭐ Star this repo if you find it useful!

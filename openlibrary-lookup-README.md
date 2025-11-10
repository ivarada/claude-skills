# OpenLibrary Lookup

Book lookup, search, and citation generation using the OpenLibrary API. Search books by title or author, look up ISBNs, generate citations, and create BibTeX entries for Zotero - all from the command line.

![Version](https://img.shields.io/badge/version-2.0-blue)
![Python](https://img.shields.io/badge/python-3.6+-green)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

## 🎯 Features

- **Unified Book Lookup** - Single command for complete citations (NEW!)
- **ISBN Lookup** - Get detailed book information instantly
- **Book Search** - Search by title, author, or subject
- **Author Information** - Find author biographies and bibliographies
- **APA 7 Citations** - Generate formatted book citations
- **BibTeX Generation** - Create Zotero-compatible entries
- **Cover Images** - Access book cover URLs in multiple sizes
- **Free API** - No authentication required

## 🚀 Quick Start

### Installation

```bash
git clone https://github.com/yourusername/openlibrary-lookup.git
cd openlibrary-lookup
pip install requests --break-system-packages
```

### Instant Citation (NEW!)

The fastest way to get a complete book citation:

```bash
# Using the convenient bib.isbn format
python scripts/book_lookup.py bib.isbn == 978-1566199094

# Or just pass the ISBN directly
python scripts/book_lookup.py 9781566199094

# Or search by title
python scripts/book_lookup.py "The Great Gatsby"
```

**Outputs:**
- ✅ Complete book information
- ✅ APA 7th edition citation (saved to `<isbn>_apa7.txt`)
- ✅ BibTeX entry (saved to `<isbn>.bib`)
- ✅ JSON metadata for programmatic use

### Basic Usage Examples

```bash
# Search for books
python scripts/search_books.py "the lord of the rings" --limit 5

# Look up by ISBN
python scripts/isbn_lookup.py 9780140328721

# Get author information
python scripts/get_author_info.py "Neil Gaiman"

# Generate APA citation
python scripts/generate_apa7_citation.py 9780140328721

# Generate BibTeX
python scripts/generate_bibtex.py 9780140328721
```

## 📚 Script Reference

### book_lookup.py (Unified Tool)

**All-in-one book lookup with complete citation generation**

```bash
python scripts/book_lookup.py [bib.isbn ==] <isbn_or_query>
```

**Features:**
- Accepts ISBN-10, ISBN-13, or book title
- Supports `bib.isbn == <isbn>` format for convenience
- Generates both APA7 and BibTeX automatically
- Saves citations to files for easy reference
- Returns comprehensive JSON output

**Examples:**
```bash
python scripts/book_lookup.py bib.isbn == 978-1566199094
python scripts/book_lookup.py 9781566199094
python scripts/book_lookup.py "Fantastic Mr Fox"
python scripts/book_lookup.py "author:Tolkien"
```

### search_books.py

**Search the OpenLibrary catalog**

```bash
python scripts/search_books.py "<query>" [--limit N]
```

**Query Formats:**
- Plain text: `"machine learning"`
- By author: `"author:tolkien"`
- By title: `"title:hobbit"`
- By subject: `"subject:science fiction"`

**Returns:**
- Title and subtitle
- Authors
- Publication year
- ISBN numbers
- Cover image URLs
- OpenLibrary IDs

**Examples:**
```bash
python scripts/search_books.py "quantum physics" --limit 10
python scripts/search_books.py "author:Neil Gaiman" --limit 20
python scripts/search_books.py "title:1984" --limit 5
python scripts/search_books.py "subject:fantasy" --limit 15
```

### isbn_lookup.py

**Get detailed book information by ISBN**

```bash
python scripts/isbn_lookup.py <isbn>
```

**Accepts:**
- ISBN-10: `0140328726`
- ISBN-13: `9780140328721`
- With hyphens: `978-0-14-032872-1`

**Returns:**
- Complete title and subtitle
- Full author list with roles
- Publisher and publication date
- Page count
- Physical dimensions
- Cover image URLs (S, M, L sizes)
- Subject classifications
- Dewey and LC classifications

**Examples:**
```bash
python scripts/isbn_lookup.py 9780140328721
python scripts/isbn_lookup.py 0140328726
python scripts/isbn_lookup.py 978-0-14-032872-1
```

### get_author_info.py

**Search for authors or get detailed author information**

```bash
python scripts/get_author_info.py <author_name_or_key>
```

**Accepts:**
- Author name: `"Neil Gaiman"` (searches for matches)
- OpenLibrary key: `OL23919A` (direct lookup)

**Returns:**
- Full name and alternate names
- Biography
- Birth and death dates
- List of published works
- Cover images for works
- OpenLibrary author key

**Examples:**
```bash
python scripts/get_author_info.py "J.K. Rowling"
python scripts/get_author_info.py "Isaac Asimov"
python scripts/get_author_info.py OL23919A
```

### generate_apa7_citation.py

**Create APA 7th edition book citations**

```bash
python scripts/generate_apa7_citation.py <isbn_or_openlibrary_id>
```

**Accepts:**
- ISBN-10 or ISBN-13
- OpenLibrary book ID (e.g., `OL7353617M`)

**Output Format:**
```
Author, A. A., & Author, B. B. (Year). Title of book: Subtitle of book. 
    Publisher Name.
```

**Examples:**
```bash
python scripts/generate_apa7_citation.py 9780140328721
python scripts/generate_apa7_citation.py OL7353617M
```

**Sample Output:**
```
Fitzgerald, F. S. (1925). The great Gatsby. Charles Scribner's Sons.
```

### generate_bibtex.py

**Generate Zotero-compatible BibTeX entries**

```bash
python scripts/generate_bibtex.py <isbn_or_openlibrary_id>
```

**Output Format:**
```bibtex
@book{fitzgerald1925great,
  title = {The Great Gatsby},
  author = {Fitzgerald, F. Scott},
  year = {1925},
  publisher = {Charles Scribner's Sons},
  isbn = {9780140328721}
}
```

**Ready for:**
- Zotero import
- LaTeX bibliographies
- Reference managers
- Academic writing tools

## 📖 Advanced Usage

### Search Strategies

**Broad Search:**
```bash
python scripts/search_books.py "artificial intelligence" --limit 50
```

**Author-Specific:**
```bash
python scripts/search_books.py "author:isaac asimov" --limit 30
```

**Subject Browse:**
```bash
python scripts/search_books.py "subject:programming python" --limit 20
```

**Title Exact Match:**
```bash
python scripts/search_books.py "title:to kill a mockingbird" --limit 5
```

### Working with Cover Images

Cover images are available in three sizes:

```python
# From search results or ISBN lookup
cover_id = "8739161"  # Example ID

# URLs for different sizes
small_cover = f"https://covers.openlibrary.org/b/id/{cover_id}-S.jpg"
medium_cover = f"https://covers.openlibrary.org/b/id/{cover_id}-M.jpg"
large_cover = f"https://covers.openlibrary.org/b/id/{cover_id}-L.jpg"
```

### Batch Processing

Process multiple ISBNs:

```bash
#!/bin/bash
for isbn in 9780140328721 9781566199094 9780451524935; do
  python scripts/generate_apa7_citation.py "$isbn"
  sleep 1  # Be nice to the API
done
```

## 🎓 Use Cases

Perfect for:

- **Students** - Quick bibliography generation for papers
- **Researchers** - Book metadata for literature reviews
- **Librarians** - Cataloging and metadata verification
- **Book Collectors** - Organizing personal libraries
- **Developers** - Building book applications and databases
- **Writers** - Research and reference management
- **Educators** - Creating reading lists and syllabi

## 🔧 Configuration

All scripts use sensible defaults:
- **Timeout**: 10 seconds per request
- **Limit**: 10 results (search), adjustable
- **Error Handling**: Graceful degradation
- **Output**: JSON format for easy parsing

## 📁 Reference Documentation

Detailed guides in the `references/` directory:

- **api_reference.md** - Complete API endpoint documentation
- **response_schemas.md** - JSON structure and field definitions
- **citation_formats.md** - APA7 and BibTeX format guides

## 🛠️ Requirements

- Python 3.6 or higher
- `requests` library

```bash
pip install requests --break-system-packages
```

## 📦 File Structure

```
openlibrary-lookup/
├── README.md
├── SKILL.md
├── LICENSE
├── scripts/
│   ├── book_lookup.py          # Unified citation tool (NEW!)
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

## 🐛 Troubleshooting

**Problem: "Book not found"**
- Verify ISBN is correct (check with/without hyphens)
- Try searching by title first
- Check if book exists on openlibrary.org

**Problem: Missing metadata**
- Not all books have complete information
- Try multiple editions (different ISBNs)
- Some fields are optional in OpenLibrary

**Problem: Slow responses**
- Normal for OpenLibrary API during peak times
- Scripts have 10-second timeout
- Try again in a few minutes

**Problem: No cover image**
- Not all books have cover images
- Try different editions
- Check covers.openlibrary.org directly

## 🔍 Tips & Tricks

1. **Multiple Editions**: Books often have many editions with different ISBNs - search by title to see all options
2. **Author Variations**: Try different name formats (first last, last first, initials)
3. **Search Operators**: Use `author:`, `title:`, and `subject:` for precise searches
4. **Batch Processing**: Write shell scripts to process reading lists
5. **Cover Images**: Download covers for visual book management
6. **Citation Management**: Import BibTeX files directly into Zotero

## 🌟 Examples

### Building a Bibliography

```bash
# Create citations for your reading list
python scripts/book_lookup.py "9780140328721"
python scripts/book_lookup.py "9781566199094"
python scripts/book_lookup.py "9780451524935"

# Combine all .bib files
cat *.bib > my_bibliography.bib
```

### Finding Books by Your Favorite Author

```bash
# Search and get detailed info
python scripts/search_books.py "author:Terry Pratchett" --limit 50

# Then look up specific editions
python scripts/isbn_lookup.py 9780060853983
```

### Creating a Formatted Bibliography

```bash
# Generate APA citations for multiple books
for isbn in 9780140328721 9781566199094 9780451524935; do
  python scripts/generate_apa7_citation.py "$isbn" >> bibliography.txt
  echo "" >> bibliography.txt
done
```

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/Enhancement`)
3. Commit your changes (`git commit -m 'Add enhancement'`)
4. Push to the branch (`git push origin feature/Enhancement`)
5. Open a Pull Request

**Ideas for contributions:**
- Additional citation formats (MLA, Chicago)
- Export to other reference managers
- GUI or web interface
- Enhanced search filters
- Multi-language support
- Book recommendation features

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **OpenLibrary** - For providing free access to book metadata
- **Internet Archive** - For supporting OpenLibrary
- **Claude AI** - Skill system integration
- **Book Lovers** - Community feedback and feature requests

## 📧 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/openlibrary-lookup/issues)
- **OpenLibrary API**: [openlibrary.org/dev/docs/api](https://openlibrary.org/dev/docs/api)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/openlibrary-lookup/discussions)

## 🔗 Related Projects

- [Crossref Lookup](https://github.com/yourusername/crossref-lookup) - Academic paper citations
- [Taxonomy SVG](https://github.com/yourusername/taxonomy-svg) - Visual taxonomy diagrams

---

**Made with ❤️ for book lovers and researchers**

*Happy reading and citing! 📚*

⭐ Star this repo if you find it useful!

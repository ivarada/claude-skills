# Changelog - OpenLibrary Lookup

All notable changes to the OpenLibrary Lookup skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Additional citation formats (MLA, Chicago, AMA)
- Export to EndNote and Mendeley formats
- Batch ISBN processing
- Web interface
- Cover image download utility
- Reading list generator

## [2.0.0] - 2024-11-10

### Added
- **🎉 Unified Book Lookup Tool** - `book_lookup.py` for complete workflow
  - Single command for ISBN/title lookup + citations
  - Generates both APA7 and BibTeX automatically
  - Saves citations to files (`<isbn>_apa7.txt` and `<isbn>.bib`)
  - Supports convenient `bib.isbn == <isbn>` format
  - Accepts ISBN-10, ISBN-13, or book title
  - Returns comprehensive JSON output
- **Enhanced Search Capabilities**
  - Title search
  - Author search with `author:` prefix
  - Subject search with `subject:` prefix
  - Configurable result limits
- **Comprehensive Reference Documentation**
  - `api_reference.md` - Complete API documentation
  - `response_schemas.md` - JSON structure examples
  - `citation_formats.md` - APA7 and BibTeX guides

### Changed
- Improved timeout handling (10 seconds)
- Better ISBN normalization (handles hyphens and formatting)
- Enhanced author name parsing
- Improved error messages and user feedback
- Updated documentation with more examples

### Fixed
- Citation formatting for books with multiple authors
- ISBN-10 to ISBN-13 conversion edge cases
- Publisher name handling for various formats
- Edition information parsing
- Cover image URL generation
- Author name formatting in citations

### Technical Improvements
- Better handling of missing metadata fields
- Improved JSON parsing for edge cases
- Enhanced search result filtering
- More robust error handling
- Better support for older book editions

## [1.5.0] - 2024-10-01

### Added
- **get_author_info.py** - Author information lookup
  - Search authors by name
  - Direct lookup by OpenLibrary author key
  - Biography and publication history
  - Birth/death dates when available
- **Edition comparison** - Multiple edition handling
- **Subject classification** - Subject and genre information
- **Physical details** - Page count, dimensions, weight
- **Cover images** - Multiple size support (S, M, L)

### Changed
- Enhanced `isbn_lookup.py` with more metadata fields
- Improved `search_books.py` result formatting
- Better handling of books without ISBNs

### Fixed
- Author name parsing for non-Western names
- Date handling for books with approximate dates
- Publisher information for self-published works

## [1.0.0] - 2024-08-15

### Added
- Initial release of OpenLibrary Lookup skill
- **isbn_lookup.py** - Core ISBN lookup functionality
  - Retrieve complete book metadata
  - Support for ISBN-10 and ISBN-13
  - JSON output with all available fields
  - Cover image URLs
- **search_books.py** - Book search
  - Title and author search
  - Subject-based search
  - Configurable result limits
  - Publication year filtering
- **generate_apa7_citation.py** - APA 7th edition citations
  - Format: Author (Year). *Title*. Publisher.
  - Support for multiple authors
  - Edition handling
  - Place of publication when available
- **generate_bibtex.py** - BibTeX generation
  - Zotero-compatible @book entries
  - Automatic citation key generation
  - Complete field mapping
  - ISBN and editor support
- **API Integration**
  - OpenLibrary Books API
  - OpenLibrary Search API
  - Cover Images API
  - Timeout handling (10 seconds)
  - Error handling for missing books

### Documentation
- Comprehensive SKILL.md with usage examples
- Script reference documentation
- Query tips and search strategies
- Best practices guide

### Dependencies
- `requests` library for HTTP operations
- Python 3.6+ required
- No other external dependencies

## [0.9.0] - 2024-07-01

### Development Preview
- Internal testing version
- Basic ISBN lookup
- Simple citation generation
- Initial API integration
- Not publicly released

---

## Version Naming

- **Major (X.0.0)**: Breaking changes, major features, API changes
- **Minor (1.X.0)**: New features, non-breaking improvements
- **Patch (1.0.X)**: Bug fixes, documentation updates, minor enhancements

## API Version Compatibility

| Skill Version | OpenLibrary API | Status |
|---------------|-----------------|---------|
| 2.0.0 | v1 (current) | ✅ Active |
| 1.5.0 | v1 | ✅ Active |
| 1.0.0 | v1 | ✅ Active |

**Note:** OpenLibrary API is stable and changes infrequently.

## Breaking Changes

### v2.0.0
- None - Fully backward compatible
- New `book_lookup.py` is additive, old scripts still work
- Enhanced functionality without breaking existing workflows

### v1.0.0
- Initial release, no breaking changes from previous versions

## Migration Guide

### To v2.0.0 from v1.x

**No migration required!** All v1.x scripts continue to work.

**Recommended**: Start using `book_lookup.py` for new workflows:

**Old workflow:**
```bash
python scripts/isbn_lookup.py 9780140328721
python scripts/generate_apa7_citation.py 9780140328721
python scripts/generate_bibtex.py 9780140328721
```

**New workflow:**
```bash
python scripts/book_lookup.py 9780140328721
# Gets everything in one command!
```

**Or use the convenient format:**
```bash
python scripts/book_lookup.py bib.isbn == 978-0-14-032872-1
```

## Known Issues

### v2.0.0
- Some very old books (pre-1900) may have incomplete metadata
- Self-published books may lack publisher information
- Some international editions have limited metadata
- Cover images not available for all books
- Search results may include multiple editions of same book

### Workarounds
- For incomplete metadata: Try alternative ISBN/edition
- For missing covers: Check OpenLibrary.org directly
- For search duplicates: Filter by publication year
- For missing publisher: Use edition notes or distributor info

## Performance Notes

### v2.0.0
- Average ISBN lookup: 0.5-1.5 seconds
- Search queries: 1-2 seconds
- Author lookup: 0.5-1 second
- Timeout: 10 seconds (configurable)
- Rate limits: Generally permissive for reasonable use

**Best Practices:**
- Cache results when making repeated lookups
- Space out requests when processing large batches
- Use specific ISBN when possible (faster than search)
- Consider rate limiting for batch operations

## Feature Comparison

| Feature | v1.0.0 | v1.5.0 | v2.0.0 |
|---------|--------|--------|--------|
| ISBN Lookup | ✅ | ✅ | ✅ |
| Book Search | ✅ | ✅ | ✅ |
| APA7 Citations | ✅ | ✅ | ✅ |
| BibTeX Generation | ✅ | ✅ | ✅ |
| Author Info | ❌ | ✅ | ✅ |
| Cover Images | ✅ | ✅ | ✅ |
| Unified Tool | ❌ | ❌ | ✅ |
| Reference Docs | Basic | Enhanced | Complete |
| File Output | ❌ | ❌ | ✅ |
| Title Search | ✅ | ✅ | ✅ |

## Dependencies History

### v2.0.0
- `requests` >= 2.25.0 (recommended)
- Python >= 3.6

### v1.0.0
- `requests` >= 2.20.0
- Python >= 3.6

## Common Use Cases

### Academic Research
- Literature review book references
- Textbook citations
- Historical source documentation
- Bibliography generation

### Library Science
- Cataloging and metadata verification
- Collection management
- ISBN validation
- Reading list creation

### Personal Use
- Book collection organization
- Reading list management
- Citation generation for personal research
- Author discovery

## Limitations and Scope

### What This Tool Does
✅ Look up book metadata by ISBN
✅ Search for books by title, author, subject
✅ Generate APA7 and BibTeX citations
✅ Retrieve author information
✅ Access cover images
✅ Export formatted citations

### What This Tool Doesn't Do
❌ Full-text book access
❌ Book recommendations
❌ Price information
❌ Availability checking
❌ Library catalog integration (use your library's API)
❌ E-book format conversion

## Acknowledgments

### Contributors
- Initial development team
- Community testers and feedback providers
- Librarians and educators
- Academic users worldwide

### Data Sources
- OpenLibrary API by Internet Archive
- ISBN metadata from publishers
- Cover images from OpenLibrary
- Author information from OpenLibrary

## Support and Resources

### Getting Help
- Check SKILL.md for detailed documentation
- Review reference documentation in `references/` directory
- Open GitHub issue for bugs or feature requests
- Join discussions for questions and sharing

### External Resources
- [OpenLibrary API Documentation](https://openlibrary.org/dev/docs/api)
- [ISBN Overview](https://www.isbn.org/)
- [APA 7th Edition Guide](https://apastyle.apa.org/)
- [BibTeX Format Specification](http://www.bibtex.org/Format/)

## Data Quality Notes

### OpenLibrary Coverage
- **Excellent**: English-language books published after 1950
- **Good**: Books published 1900-1950
- **Variable**: Self-published, regional, or rare books
- **Limited**: Pre-1900 books may have minimal metadata

### Metadata Completeness
Books typically include:
- ✅ Title, author, publication year (95%+)
- ✅ Publisher information (90%+)
- ✅ ISBN (modern books 95%+)
- ⚠️ Page count (80%+)
- ⚠️ Physical description (70%+)
- ⚠️ Cover images (60%+)
- ⚠️ Subject classifications (50%+)

## Future Roadmap

### v2.1.0 (Planned Q4 2024)
- [ ] MLA citation format
- [ ] Chicago citation format
- [ ] Batch ISBN processing script
- [ ] Reading list generator
- [ ] Enhanced search filters

### v2.2.0 (Planned Q1 2025)
- [ ] Web interface
- [ ] Cover image downloader
- [ ] Export to EndNote/Mendeley
- [ ] Integration with library catalogs
- [ ] Book availability checker

### v3.0.0 (Future)
- [ ] GUI application
- [ ] Personal library manager
- [ ] Reading recommendations
- [ ] Multi-language support
- [ ] Advanced analytics

---

**Legend:**
- `Added` - New features
- `Changed` - Changes in existing functionality
- `Deprecated` - Soon-to-be removed features
- `Removed` - Removed features
- `Fixed` - Bug fixes
- `Security` - Security improvements
- `Performance` - Performance improvements
- `Documentation` - Documentation changes

# Changelog - Crossref Lookup

All notable changes to the Crossref Lookup skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned
- Additional citation formats (MLA, Chicago, AMA)
- Export to EndNote and Mendeley formats
- Batch processing utilities
- Web interface
- Caching system for repeated lookups
- Advanced search filters UI

## [2.0.0] - 2024-11-10

### Added
- **🎉 Unified Citation Tool** - `citation_lookup.py` for complete workflow
  - Single command for DOI lookup + citations
  - Generates both APA7 and BibTeX automatically
  - Saves citations to files (`<doi>_apa7.txt` and `<doi>.bib`)
  - Supports convenient `bib.doi == <doi>` format
  - Accepts DOI with or without URL prefix
  - Returns comprehensive JSON output
- **Enhanced Error Handling** - Better timeout and retry logic
- **Comprehensive Reference Documentation**
  - `api_reference.md` - Complete API documentation
  - `response_schemas.md` - JSON structure examples
  - `citation_formats.md` - Citation format guides
  - `filters_guide.md` - Advanced search techniques

### Changed
- Increased timeout to 15 seconds for reliability
- Improved polite pool implementation with user email
- Better JSON parsing for edge cases
- Enhanced citation formatting for various publication types
- Updated documentation with more examples

### Fixed
- Citation formatting for multi-author papers (>10 authors)
- Date parsing for various date formats
- DOI normalization (handling prefixes and whitespace)
- BibTeX key generation for special characters
- Journal name handling for abbreviated titles

### Technical Improvements
- Added retry logic for rate limiting (429 errors)
- Better handling of incomplete metadata
- Improved author name parsing
- Enhanced publication type detection
- More robust URL handling

## [1.5.0] - 2024-10-01

### Added
- **journal_lookup.py** - Get journal information by ISSN
- **Author affiliation support** - Extract institutional info when available
- **License information** - Display open access status and licenses
- **Abstract retrieval** - Include abstracts in DOI lookup results
- **Reference counting** - Show citation and reference counts

### Changed
- Improved `search_works.py` with better filtering
- Enhanced `generate_bibtex.py` with more field types
- Better handling of preprints and datasets

### Fixed
- Special character encoding in BibTeX entries
- Date formatting for online-first publications
- Author name parsing for complex name formats

## [1.0.0] - 2024-08-15

### Added
- Initial release of Crossref Lookup skill
- **doi_lookup.py** - Core DOI lookup functionality
  - Retrieve complete publication metadata
  - JSON output with all available fields
  - Support for all Crossref content types
- **search_works.py** - Publication search
  - Full-text search across Crossref database
  - Filter support for dates, types, licenses
  - Configurable result count
- **search_by_author.py** - Author-based search
  - Find papers by author name
  - Returns publications with author metadata
- **generate_apa7_citation.py** - APA 7th edition citations
  - Support for journal articles
  - Book chapters
  - Conference papers
  - Reports and working papers
- **generate_bibtex.py** - BibTeX generation
  - Zotero-compatible entries
  - Automatic citation key generation
  - Complete field mapping
- **API Integration**
  - Polite pool support with mailto parameter
  - Rate limiting respect (50 req/sec)
  - Timeout handling (10 seconds)
  - Error handling and retries

### Documentation
- Comprehensive SKILL.md with usage examples
- Script reference documentation
- API best practices guide
- Query tips and tricks

### Dependencies
- `requests` library for HTTP operations
- Python 3.6+ required
- No other external dependencies

## [0.9.0] - 2024-07-01

### Development Preview
- Internal testing version
- Basic DOI lookup
- Simple citation generation
- Initial API integration
- Not publicly released

---

## Version Naming

- **Major (X.0.0)**: Breaking changes, major features, API changes
- **Minor (1.X.0)**: New features, non-breaking improvements
- **Patch (1.0.X)**: Bug fixes, documentation updates, minor enhancements

## API Version Compatibility

| Skill Version | Crossref API Version | Status |
|---------------|---------------------|---------|
| 2.0.0 | v1 (current) | ✅ Active |
| 1.5.0 | v1 | ✅ Active |
| 1.0.0 | v1 | ✅ Active |

## Breaking Changes

### v2.0.0
- None - Fully backward compatible
- New `citation_lookup.py` is additive, old scripts still work
- Enhanced functionality without breaking existing workflows

### v1.0.0
- Initial release, no breaking changes from previous versions

## Migration Guide

### To v2.0.0 from v1.x

**No migration required!** All v1.x scripts continue to work.

**Recommended**: Start using `citation_lookup.py` for new workflows:

**Old workflow:**
```bash
python scripts/doi_lookup.py 10.1038/nature12373
python scripts/generate_apa7_citation.py 10.1038/nature12373
python scripts/generate_bibtex.py 10.1038/nature12373
```

**New workflow:**
```bash
python scripts/citation_lookup.py 10.1038/nature12373
# Gets everything in one command!
```

## Known Issues

### v2.0.0
- Some very old DOIs (pre-1990) may have incomplete metadata
- Preprint metadata structure varies by provider
- Conference proceedings may lack complete venue information
- Rate limiting can occur during peak hours (automatic retry implemented)

### Workarounds
- For incomplete metadata: Try alternative DOI resolvers
- For rate limiting: Script handles automatically with retries
- For missing data: Check doi.org directly to verify availability

## Performance Notes

### v2.0.0
- Average DOI lookup: 0.5-2 seconds
- Search queries: 1-3 seconds
- Timeout: 15 seconds (configurable)
- Rate limit: 50 requests/second (free tier)
- Polite pool: Higher limits with email parameter (automatic)

## Feature Comparison

| Feature | v1.0.0 | v1.5.0 | v2.0.0 |
|---------|--------|--------|--------|
| DOI Lookup | ✅ | ✅ | ✅ |
| Publication Search | ✅ | ✅ | ✅ |
| Author Search | ✅ | ✅ | ✅ |
| APA7 Citations | ✅ | ✅ | ✅ |
| BibTeX Generation | ✅ | ✅ | ✅ |
| Journal Lookup | ❌ | ✅ | ✅ |
| Unified Tool | ❌ | ❌ | ✅ |
| Reference Docs | Basic | Enhanced | Complete |
| File Output | ❌ | ❌ | ✅ |

## Dependencies History

### v2.0.0
- `requests` >= 2.25.0 (recommended)
- Python >= 3.6

### v1.0.0
- `requests` >= 2.20.0
- Python >= 3.6

## Acknowledgments

### Contributors
- Initial development team
- Community testers and feedback providers
- Academic users worldwide

### Data Sources
- Crossref API for publication metadata
- DOI.org for resolution services
- Research community for citation standards

## Support and Resources

### Getting Help
- Check SKILL.md for detailed documentation
- Review reference documentation in `references/` directory
- Open GitHub issue for bugs or feature requests
- Join discussions for questions and sharing

### External Resources
- [Crossref API Documentation](https://api.crossref.org)
- [APA 7th Edition Guide](https://apastyle.apa.org/)
- [BibTeX Format Specification](http://www.bibtex.org/Format/)
- [DOI Handbook](https://www.doi.org/the-identifier/resources/handbook)

## Future Roadmap

### v2.1.0 (Planned Q4 2024)
- [ ] MLA citation format
- [ ] Chicago citation format
- [ ] Batch processing script
- [ ] Configuration file support
- [ ] Enhanced search filters

### v2.2.0 (Planned Q1 2025)
- [ ] Web interface
- [ ] Citation export formats (RIS, EndNote XML)
- [ ] Integration with reference managers
- [ ] Advanced analytics and reporting

### v3.0.0 (Future)
- [ ] GUI application
- [ ] Database integration
- [ ] Machine learning for citation recommendations
- [ ] Multi-language support

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

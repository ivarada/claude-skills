---
name: crossref-lookup
description: Academic publication metadata retrieval and citation generation using the Crossref REST API. Now includes unified citation_lookup.py tool supporting the convenient bib.doi format. Use this skill when users ask to look up DOIs, search for academic papers, retrieve journal article metadata, find publication information, generate citations for research papers, get author information for academic works, search by ISSN, or retrieve bibliographic data. Triggers include queries like look up DOI, search for papers by author, find article metadata, cite this paper, generate citation for DOI, search Crossref, get publication details, or bib.doi with a DOI number.
---

# Crossref Lookup Skill

This skill provides Python scripts and reference documentation for retrieving academic publication metadata using the Crossref REST API.

## Quick Start

### Unified Citation Lookup (NEW!)

Use `scripts/citation_lookup.py` for the easiest way to get both APA7 and BibTeX citations:

```bash
python scripts/citation_lookup.py bib.doi == 10.1038/s41586-025-09663-y
python scripts/citation_lookup.py bib.doi == https://doi.org/10.1038/s41586-025-09663-y
python scripts/citation_lookup.py 10.1038/nature12373
python scripts/citation_lookup.py https://doi.org/10.1038/nature12373
```

This command will:
- Look up the publication in Crossref
- Display complete publication information
- Generate APA 7th edition citation
- Generate BibTeX entry
- Save both citations to files automatically

### Look Up by DOI

Use `scripts/doi_lookup.py` to get complete metadata for a publication:

```bash
python scripts/doi_lookup.py 10.1038/nature12373
python scripts/doi_lookup.py "10.1371/journal.pone.0161344"
```

### Search Publications

Use `scripts/search_works.py` to search for academic works:

```bash
python scripts/search_works.py "machine learning" --rows 10
python scripts/search_works.py "climate change" --filter "from-pub-date:2020"
```

### Search by Author

Use `scripts/search_by_author.py` to find publications by specific authors:

```bash
python scripts/search_by_author.py "Jane Smith"
python scripts/search_by_author.py "Einstein" --rows 20
```

### Generate APA7 Citation

Use `scripts/generate_apa7_citation.py` to create citations from DOIs:

```bash
python scripts/generate_apa7_citation.py 10.1038/nature12373
```

### Generate BibTeX

Use `scripts/generate_bibtex.py` to create reference manager entries:

```bash
python scripts/generate_bibtex.py 10.1038/nature12373
```

### Get Journal Information

Use `scripts/journal_lookup.py` to retrieve journal metadata by ISSN:

```bash
python scripts/journal_lookup.py 0028-0836
python scripts/journal_lookup.py "1476-4687"
```

## Script Reference

### citation_lookup.py (UNIFIED TOOL)

**Purpose:** All-in-one DOI lookup with APA7 and BibTeX generation

**Usage:** `python scripts/citation_lookup.py [bib.doi ==] <doi>`

**Examples:**
```bash
python scripts/citation_lookup.py bib.doi == 10.1038/s41586-025-09663-y
python scripts/citation_lookup.py bib.doi == https://doi.org/10.1038/s41586-025-09663-y
python scripts/citation_lookup.py 10.1038/nature12373
python scripts/citation_lookup.py https://doi.org/10.1038/nature12373
```

**Returns:** 
- Complete publication information
- APA 7th edition citation (printed and saved to file)
- BibTeX entry (printed and saved to .bib file)
- JSON output with all data

**Files Created:**
- `<doi>_apa7.txt` - APA citation with metadata
- `<doi>.bib` - BibTeX entry ready for Zotero/LaTeX

**Special Format:** Supports `bib.doi == <doi>` format for convenience

**Accepts:** DOI with or without URL prefix (https://doi.org/)

### doi_lookup.py

**Purpose:** Retrieve complete metadata for a publication by DOI

**Usage:** `python scripts/doi_lookup.py <doi>`

**Returns:** JSON with full publication metadata including title, authors, journal, dates, references, and more

**Accepts:** Any valid DOI (with or without the "https://doi.org/" prefix)

### search_works.py

**Purpose:** Search Crossref database for publications

**Usage:** `python scripts/search_works.py "<query>" [--rows N] [--filter "filter_params"]`

**Returns:** List of matching works with key metadata

**Query Tips:**
- Plain text searches across titles, abstracts, and full text
- Use `--filter` for advanced filtering (date ranges, publication types, etc.)
- Use `--rows` to control number of results (default: 10)

### search_by_author.py

**Purpose:** Find publications by author name

**Usage:** `python scripts/search_by_author.py "<author_name>" [--rows N]`

**Returns:** Publications authored by the specified person

**Note:** Searches author fields in Crossref metadata

### generate_apa7_citation.py

**Purpose:** Generate APA 7th edition citations from DOIs

**Usage:** `python scripts/generate_apa7_citation.py <doi>`

**Returns:** Formatted APA7 citation with structured data

**Formats:** Journal articles, books, conference papers, and more

### generate_bibtex.py

**Purpose:** Generate Zotero-compatible BibTeX entries from DOIs

**Usage:** `python scripts/generate_bibtex.py <doi>`

**Returns:** Complete BibTeX entry with all available fields

**Entry Types:** @article, @book, @inproceedings, etc.

### journal_lookup.py

**Purpose:** Get journal information by ISSN

**Usage:** `python scripts/journal_lookup.py <issn>`

**Returns:** Journal title, publisher, subjects, and other metadata

**Accepts:** ISSN (print or electronic)

## Advanced Usage

For detailed API documentation and advanced features, read:
- `references/api_reference.md` - Complete Crossref API documentation
- `references/response_schemas.md` - JSON response structure examples
- `references/citation_formats.md` - Citation format guide with examples
- `references/filters_guide.md` - Advanced search filters and parameters

These references provide information about:
- All available API endpoints
- Query parameters and filters
- Rate limiting and etiquette
- Response field definitions
- Citation formatting rules
- Advanced search techniques

## Dependencies

All scripts require the `requests` library:

```bash
pip install requests --break-system-packages
```

## Best Practices

1. **Use polite pool** - Always include a `mailto` parameter in API requests for better rate limits
2. **Respect rate limits** - Free tier: 50 requests/second, Polite pool: higher limits
3. **Handle errors gracefully** - DOIs may not exist, API may be slow
4. **Use appropriate timeouts** - All scripts use 15-second timeouts for reliability
5. **Cache results** when making multiple requests for the same data
6. **Read references** for advanced filtering and search techniques
7. **Verify citations** - Always check accuracy before using in publications

## API Etiquette

The Crossref API is free but follows an etiquette policy:
- Include your email in requests (mailto parameter) for better service
- Don't make excessive requests
- Cache responses when possible
- Use specific queries rather than broad searches
- Be a good API citizen!

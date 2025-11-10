---
name: openlibrary-lookup
description: Book lookup, search, and citation generation using the OpenLibrary API. Now includes unified book_lookup.py tool supporting the convenient bib.isbn format. Use this skill when users ask to search for books, look up book information by ISBN, find books by author, get book details from OpenLibrary, search for information about authors or literary works, generate citations (APA7 format), or create BibTeX entries for Zotero. Triggers include queries like look up this book, search for books by author, find ISBN, what books has author written, get book details, generate APA citation, create BibTeX entry, cite this book, or bib.isbn with a number.
---

# OpenLibrary Lookup Skill

This skill provides Python scripts and reference documentation for looking up books and authors using the OpenLibrary API.

## Quick Start

### Unified Book Lookup (NEW!)

Use `scripts/book_lookup.py` for the easiest way to get both APA7 and BibTeX citations:

```bash
python scripts/book_lookup.py bib.isbn == 978-1566199094
python scripts/book_lookup.py 9781566199094
python scripts/book_lookup.py "The Great Gatsby"
```

This command will:
- Look up the book in OpenLibrary
- Display complete book information
- Generate APA 7th edition citation
- Generate BibTeX entry
- Save both citations to files automatically

### Search for Books

Use `scripts/search_books.py` to search by title, author, or subject:

```bash
python scripts/search_books.py "the lord of the rings" --limit 5
python scripts/search_books.py "author:tolkien" --limit 10
```

### Look Up by ISBN

Use `scripts/isbn_lookup.py` to get detailed book information:

```bash
python scripts/isbn_lookup.py 9780140328721
python scripts/isbn_lookup.py 0140328726
```

### Get Author Information

Use `scripts/get_author_info.py` to search for authors or get author details:

```bash
python scripts/get_author_info.py "Neil Gaiman"
python scripts/get_author_info.py OL23919A
```

### Generate APA7 Citation

Use `scripts/generate_apa7_citation.py` to create APA 7th edition citations:

```bash
python scripts/generate_apa7_citation.py 9780140328721
python scripts/generate_apa7_citation.py OL7353617M
```

### Generate BibTeX for Zotero

Use `scripts/generate_bibtex.py` to create Zotero-compatible BibTeX entries:

```bash
python scripts/generate_bibtex.py 9780140328721
python scripts/generate_bibtex.py OL7353617M
```

## Script Reference

### book_lookup.py (UNIFIED TOOL)

**Purpose:** All-in-one book lookup with APA7 and BibTeX generation

**Usage:** `python scripts/book_lookup.py [bib.isbn ==] <isbn_or_query>`

**Examples:**
```bash
python scripts/book_lookup.py bib.isbn == 978-1566199094
python scripts/book_lookup.py 9781566199094
python scripts/book_lookup.py "Fantastic Mr Fox"
```

**Returns:** 
- Complete book information
- APA 7th edition citation (printed and saved to file)
- BibTeX entry (printed and saved to .bib file)
- JSON output with all data

**Files Created:**
- `<isbn>_apa7.txt` - APA citation with metadata
- `<isbn>.bib` - BibTeX entry ready for Zotero/LaTeX

**Special Format:** Supports `bib.isbn == <isbn>` format for convenience

### search_books.py

**Purpose:** Search the OpenLibrary catalog

**Usage:** `python scripts/search_books.py "<query>" [--limit N]`

**Returns:** JSON with search results including title, authors, publication year, ISBN, and cover URLs

**Query Tips:**
- Plain text: searches across all fields
- `author:name`: search by author
- `title:name`: search by title
- `subject:topic`: search by subject

### isbn_lookup.py

**Purpose:** Look up a specific book edition by ISBN

**Usage:** `python scripts/isbn_lookup.py <isbn>`

**Returns:** Complete book information including title, authors, publishers, page count, and cover images

**Accepts:** ISBN-10 or ISBN-13 (with or without hyphens)

### get_author_info.py

**Purpose:** Get author information

**Usage:** `python scripts/get_author_info.py <author_name_or_key>`

**Returns:** Author details including name, biography, birth/death dates, and bibliography

**Accepts:** Author name (searches) or OpenLibrary author key (direct lookup)

### generate_apa7_citation.py

**Purpose:** Generate APA 7th edition citations

**Usage:** `python scripts/generate_apa7_citation.py <isbn_or_openlibrary_id>`

**Returns:** Formatted APA7 citation with structured data (authors, year, title, publisher)

**Accepts:** ISBN-10, ISBN-13, or OpenLibrary book ID

**Format:** Author, A. A. (Year). *Title of book: Subtitle*. Publisher.

### generate_bibtex.py

**Purpose:** Generate Zotero-compatible BibTeX entries

**Usage:** `python scripts/generate_bibtex.py <isbn_or_openlibrary_id>`

**Returns:** BibTeX entry with citation key and all relevant fields

**Accepts:** ISBN-10, ISBN-13, or OpenLibrary book ID

**Output:** Complete @book{} entry ready for import into Zotero, LaTeX, or other reference managers

## Advanced Usage

For detailed API documentation and response schemas, read:
- `references/api_reference.md` - Complete API endpoint documentation
- `references/response_schemas.md` - JSON response structure examples
- `references/citation_formats.md` - APA7 and BibTeX format guide with examples

These references provide information about:
- All available API endpoints
- Query parameters and options
- Cover image URLs
- Error handling
- Response field definitions
- Citation formatting rules and examples
- BibTeX entry structure
- Zotero import instructions

## Dependencies

All scripts require the `requests` library:

```bash
pip install requests --break-system-packages
```

## Best Practices

1. **Install dependencies first** before running scripts
2. **Test scripts** to verify they work before relying on them
3. **Handle errors gracefully** - API requests may fail or return no results
4. **Use appropriate timeouts** - All scripts use 10-second timeouts
5. **Respect rate limits** - Space out requests when making many lookups
6. **Read references** when you need more than basic functionality

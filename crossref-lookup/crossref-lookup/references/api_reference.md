# Crossref REST API Reference

## Base URL
`https://api.crossref.org`

## Authentication
No authentication required. The API is free and open to all.

## Rate Limiting

### Standard Pool
- **50 requests/second**
- No registration required
- Suitable for light usage

### Polite Pool
- **Higher rate limits** (exact limits not publicly specified)
- Include your email in User-Agent header
- Recommended format: `MyApp/1.0 (mailto:your@email.com)`
- Gets priority during high traffic
- **Always recommended!**

### Plus Pool
- **Unlimited requests**
- Requires Crossref membership
- For heavy institutional usage
- Requires API token

## API Etiquette

Follow these best practices to be a good API citizen:

1. **Use the polite pool** - Include your email in User-Agent
2. **Cache responses** - Don't request the same data repeatedly
3. **Be specific** - Use precise queries instead of broad searches
4. **Respect rate limits** - Don't hammer the API
5. **Handle errors** - Implement proper error handling and retries

## Main Endpoints

### 1. Works (Publications)

#### Single Work by DOI
```
GET /works/{doi}
```

**Example:**
```
GET /works/10.1038/nature12373
```

**Returns:** Complete metadata for a single publication

#### Search Works
```
GET /works?query={query}&rows={n}&filter={filters}
```

**Parameters:**
- `query`: Free text search
- `query.title`: Search in titles
- `query.author`: Search in author names
- `query.bibliographic`: Search across all bibliographic fields
- `rows`: Number of results (default: 20, max: 1000)
- `offset`: Pagination offset
- `sort`: Sort order (score, published, indexed, etc.)
- `order`: asc or desc
- `filter`: Apply filters (see Filters section)

**Example:**
```
GET /works?query=machine+learning&rows=10
GET /works?query.author=einstein&filter=from-pub-date:1905,until-pub-date:1920
```

### 2. Journals

#### Single Journal by ISSN
```
GET /journals/{issn}
```

**Example:**
```
GET /journals/0028-0836
```

**Returns:** Journal metadata including title, publisher, subjects

#### Works from a Journal
```
GET /journals/{issn}/works
```

**Example:**
```
GET /journals/0028-0836/works?rows=10
```

### 3. Members (Publishers)

#### Single Member
```
GET /members/{member_id}
```

#### Works from a Member
```
GET /members/{member_id}/works
```

### 4. Funders

#### Single Funder
```
GET /funders/{funder_id}
```

#### Works Funded by Funder
```
GET /funders/{funder_id}/works
```

### 5. Types

#### List Publication Types
```
GET /types
```

#### Works of a Type
```
GET /types/{type_id}/works
```

## Filters

Filters allow you to narrow search results. Multiple filters are combined with commas.

### Date Filters
- `from-pub-date:{date}` - Published on or after date (YYYY-MM-DD or YYYY-MM or YYYY)
- `until-pub-date:{date}` - Published on or before date
- `from-online-pub-date:{date}` - Online publication date filter
- `until-online-pub-date:{date}`
- `from-print-pub-date:{date}` - Print publication date filter
- `until-print-pub-date:{date}`

**Example:**
```
filter=from-pub-date:2020,until-pub-date:2023
```

### Content Filters
- `has-abstract:true` - Has an abstract
- `has-full-text:true` - Has full text
- `has-references:true` - Has references
- `has-orcid:true` - At least one author has an ORCID
- `has-funder:true` - Has funding information

### Type Filters
- `type:{type}` - Publication type
  - `journal-article`
  - `book`
  - `book-chapter`
  - `proceedings-article`
  - `report`
  - `dataset`
  - `posted-content` (preprints)

**Example:**
```
filter=type:journal-article,has-full-text:true
```

### License Filters
- `has-license:true` - Has license information
- `license.url:{url}` - Specific license URL
- `license.version:{version}` - License version

### Organization Filters
- `member:{member_id}` - From specific publisher
- `funder:{funder_id}` - Funded by specific funder
- `issn:{issn}` - From journal with specific ISSN
- `isbn:{isbn}` - Book with specific ISBN

### Relation Filters
- `relation.type:{type}` - Has relationship of type
- `relation.object-type:{type}` - Related object type

## Response Format

All responses are JSON with this structure:

```json
{
  "status": "ok",
  "message-type": "work",
  "message-version": "1.0.0",
  "message": {
    // Actual content here
  }
}
```

### Common Fields

**Work (Publication) Fields:**
- `DOI`: The DOI
- `title`: Array of title strings
- `author`: Array of author objects
- `published`: Publication date object
- `type`: Publication type
- `container-title`: Journal/book title
- `volume`, `issue`, `page`: Volume/issue/page numbers
- `publisher`: Publisher name
- `ISSN`, `ISBN`: Identifiers
- `URL`: Link to work
- `abstract`: Abstract text (if available)
- `references-count`: Number of references
- `is-referenced-by-count`: Citation count
- `subject`: Subject categories
- `license`: License information

**Author Fields:**
- `given`: Given name
- `family`: Family name
- `ORCID`: ORCID identifier (if available)
- `affiliation`: Array of affiliations

**Date Fields:**
- `date-parts`: Array of [year, month, day]
- `timestamp`: Unix timestamp

## Pagination

Use `offset` and `rows` for pagination:

```
GET /works?query=test&rows=20&offset=0    # First page
GET /works?query=test&rows=20&offset=20   # Second page
GET /works?query=test&rows=20&offset=40   # Third page
```

## Sorting

Use `sort` and `order` parameters:

```
GET /works?query=test&sort=published&order=desc
GET /works?query=test&sort=score&order=desc
```

Available sort fields:
- `score` (relevance)
- `published`
- `indexed`
- `is-referenced-by-count` (citation count)

## Error Handling

### HTTP Status Codes
- `200`: Success
- `404`: Resource not found
- `400`: Bad request
- `500`: Server error
- `503`: Service unavailable

### Best Practices
- Implement exponential backoff for rate limiting
- Cache responses to avoid repeated requests
- Handle 404 errors gracefully
- Set appropriate timeouts (15-30 seconds recommended)

## Content Negotiation

Request different formats:

```
Accept: application/json  (default)
Accept: text/x-bibliography; style=apa
Accept: application/vnd.citationstyles.csl+json
Accept: application/x-bibtex
```

**Example:**
```bash
curl -H "Accept: text/x-bibliography; style=apa" \
  https://api.crossref.org/works/10.1038/nature12373
```

## Examples

### Example 1: Search for Papers
```bash
curl "https://api.crossref.org/works?query=climate+change&rows=5"
```

### Example 2: Get Paper by DOI
```bash
curl "https://api.crossref.org/works/10.1038/nature12373"
```

### Example 3: Filtered Search
```bash
curl "https://api.crossref.org/works?query=machine+learning&filter=from-pub-date:2020,type:journal-article&rows=10"
```

### Example 4: Author Search
```bash
curl "https://api.crossref.org/works?query.author=einstein&rows=10"
```

### Example 5: Get BibTeX
```bash
curl -H "Accept: application/x-bibtex" \
  "https://api.crossref.org/works/10.1038/nature12373"
```

## Additional Resources

- **Official Documentation**: https://www.crossref.org/documentation/retrieve-metadata/rest-api/
- **API Issues**: https://gitlab.com/crossref/issues
- **Metadata Plus**: https://www.crossref.org/services/metadata-retrieval/

# OpenLibrary API Reference

## Base URL
`https://openlibrary.org`

## Authentication
No authentication required. The API is free and open.

## Rate Limiting
Be respectful with requests. No official rate limit, but avoid excessive requests.

## Main Endpoints

### 1. Search API
**Endpoint:** `/search.json`

**Parameters:**
- `q` (required): Search query
- `title`: Search by title
- `author`: Search by author
- `subject`: Search by subject
- `isbn`: Search by ISBN
- `limit`: Number of results (default: 100)
- `offset`: Pagination offset
- `fields`: Comma-separated list of fields to return

**Example:**
```
GET /search.json?q=the+lord+of+the+rings&limit=5
GET /search.json?author=tolkien&limit=10
GET /search.json?subject=science+fiction
```

### 2. Books API
**Endpoint:** `/books/{ISBN|OCLC|LCCN|OLID}.json`

Get information about a specific book edition.

**Example:**
```
GET /books/OL7353617M.json
GET /isbn/0140328726.json
```

### 3. Works API
**Endpoint:** `/works/{OLID}.json`

Get information about a work (a work can have multiple editions).

**Example:**
```
GET /works/OL45804W.json
```

### 4. Authors API
**Endpoint:** `/authors/{OLID}.json`

Get information about an author.

**Example:**
```
GET /authors/OL23919A.json
```

**Search Authors:**
```
GET /search/authors.json?q=tolkien
```

### 5. Subjects API
**Endpoint:** `/subjects/{subject}.json`

Get books on a specific subject.

**Example:**
```
GET /subjects/fantasy.json
```

## Cover Images

Cover images are available at:
```
https://covers.openlibrary.org/b/{key}/{value}-{size}.jpg
```

**Keys:**
- `id`: Cover ID
- `isbn`: ISBN
- `olid`: OpenLibrary ID

**Sizes:**
- `S`: Small (max width/height: 50px)
- `M`: Medium (max width/height: 180px)
- `L`: Large (max width/height: 500px)

**Examples:**
```
https://covers.openlibrary.org/b/id/8739161-L.jpg
https://covers.openlibrary.org/b/isbn/9780140328721-M.jpg
```

## Response Format

All endpoints return JSON. Common fields include:

- `key`: OpenLibrary identifier
- `title`: Book title
- `author_name`: List of author names
- `first_publish_year`: Year of first publication
- `isbn`: List of ISBNs
- `number_of_pages_median`: Typical page count
- `covers`: List of cover IDs

## Error Handling

- `404`: Resource not found
- `500`: Server error
- Timeout: Use appropriate timeout values (10s recommended)

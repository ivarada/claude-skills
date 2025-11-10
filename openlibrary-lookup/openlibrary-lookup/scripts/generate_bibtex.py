#!/usr/bin/env python3
"""
Generate BibTeX citation for Zotero from OpenLibrary book data.
Usage: python generate_bibtex.py <isbn_or_search_query>
"""
import requests
import json
import sys
import re

def clean_string_for_bibtex(text):
    """Clean string for BibTeX format"""
    if not text:
        return ""
    # Remove or escape special characters
    text = text.replace('{', '\\{').replace('}', '\\}')
    text = text.replace('&', '\\&')
    return text

def generate_cite_key(authors, year, title):
    """
    Generate a BibTeX citation key
    Format: FirstAuthorLastName + Year + FirstTitleWord
    Example: Smith2020Introduction
    """
    # Get first author's last name
    author_part = "Unknown"
    if authors and len(authors) > 0:
        author_name = authors[0]
        parts = author_name.split()
        if parts:
            author_part = parts[-1]  # Last word is typically the last name
    
    # Clean author part (remove special chars)
    author_part = re.sub(r'[^a-zA-Z]', '', author_part)
    
    # Get year
    year_part = year if year else "nd"
    
    # Get first significant word from title
    title_part = ""
    if title:
        words = title.split()
        # Skip common articles
        skip_words = {'a', 'an', 'the', 'of', 'in', 'on', 'at', 'to', 'for'}
        for word in words:
            clean_word = re.sub(r'[^a-zA-Z]', '', word)
            if clean_word.lower() not in skip_words and len(clean_word) > 2:
                title_part = clean_word
                break
    
    if not title_part and title:
        title_part = re.sub(r'[^a-zA-Z]', '', title.split()[0])
    
    return f"{author_part}{year_part}{title_part}"

def get_book_data(identifier):
    """
    Get book data from OpenLibrary by ISBN or search query
    Returns standardized book data dict
    """
    # Try as ISBN first
    isbn = identifier.replace('-', '').replace(' ', '')
    if isbn.isdigit() and (len(isbn) == 10 or len(isbn) == 13):
        url = f"https://openlibrary.org/isbn/{isbn}.json"
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                book_data = response.json()
                
                # Get author names
                authors = []
                if 'authors' in book_data:
                    for author_ref in book_data['authors']:
                        author_key = author_ref.get('key')
                        if author_key:
                            author_url = f"https://openlibrary.org{author_key}.json"
                            author_response = requests.get(author_url, timeout=10)
                            if author_response.status_code == 200:
                                author_data = author_response.json()
                                authors.append(author_data.get('name', ''))
                
                return {
                    'title': book_data.get('title', ''),
                    'subtitle': book_data.get('subtitle'),
                    'authors': authors,
                    'publishers': book_data.get('publishers', []),
                    'publish_date': book_data.get('publish_date', ''),
                    'publish_place': book_data.get('publish_places', []),
                    'isbn_10': book_data.get('isbn_10', []),
                    'isbn_13': book_data.get('isbn_13', []),
                    'number_of_pages': book_data.get('number_of_pages'),
                    'edition': book_data.get('edition_name')
                }
        except:
            pass
    
    # Try as search query
    search_url = "https://openlibrary.org/search.json"
    params = {'q': identifier, 'limit': 1}
    
    try:
        response = requests.get(search_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get('docs'):
            doc = data['docs'][0]
            return {
                'title': doc.get('title', ''),
                'subtitle': doc.get('subtitle'),
                'authors': doc.get('author_name', []),
                'publishers': doc.get('publisher', []),
                'publish_date': str(doc.get('first_publish_year', '')),
                'publish_place': doc.get('place', []),
                'isbn_10': doc.get('isbn', [])[:1] if doc.get('isbn') else [],
                'isbn_13': [],
                'number_of_pages': doc.get('number_of_pages_median'),
                'edition': None
            }
    except:
        pass
    
    return None

def generate_bibtex(book_data):
    """
    Generate BibTeX format citation from book data
    
    BibTeX Book Format:
    @book{citekey,
      author = {Author, First and Author, Second},
      title = {Book Title: Subtitle},
      publisher = {Publisher Name},
      year = {2020},
      address = {City},
      isbn = {978-0-123456-78-9},
      edition = {2nd},
      pages = {350}
    }
    """
    if not book_data:
        return {'error': 'No book data provided'}
    
    # Extract year from publish_date
    publish_date = book_data.get('publish_date', '')
    year = None
    if publish_date:
        year_match = re.search(r'\b(19|20)\d{2}\b', publish_date)
        if year_match:
            year = year_match.group(0)
    
    # Generate citation key
    cite_key = generate_cite_key(
        book_data.get('authors', []),
        year,
        book_data.get('title', '')
    )
    
    # Build BibTeX entry
    bibtex_lines = [f"@book{{{cite_key},"]
    
    # Authors (required)
    authors = book_data.get('authors', [])
    if authors:
        # Format: "Last1, First1 and Last2, First2"
        author_str = " and ".join(authors)
        bibtex_lines.append(f"  author = {{{clean_string_for_bibtex(author_str)}}},")
    
    # Title (required) - combine with subtitle
    title = book_data.get('title', 'Untitled')
    subtitle = book_data.get('subtitle')
    if subtitle:
        full_title = f"{title}: {subtitle}"
    else:
        full_title = title
    bibtex_lines.append(f"  title = {{{clean_string_for_bibtex(full_title)}}},")
    
    # Publisher
    publishers = book_data.get('publishers', [])
    if publishers and publishers[0]:
        bibtex_lines.append(f"  publisher = {{{clean_string_for_bibtex(publishers[0])}}},")
    
    # Year
    if year:
        bibtex_lines.append(f"  year = {{{year}}},")
    
    # Address (publish place)
    publish_place = book_data.get('publish_place', [])
    if publish_place and publish_place[0]:
        bibtex_lines.append(f"  address = {{{clean_string_for_bibtex(publish_place[0])}}},")
    
    # ISBN (prefer ISBN-13)
    isbn_13 = book_data.get('isbn_13', [])
    isbn_10 = book_data.get('isbn_10', [])
    if isbn_13:
        bibtex_lines.append(f"  isbn = {{{isbn_13[0]}}},")
    elif isbn_10:
        bibtex_lines.append(f"  isbn = {{{isbn_10[0]}}},")
    
    # Edition
    edition = book_data.get('edition')
    if edition:
        bibtex_lines.append(f"  edition = {{{clean_string_for_bibtex(edition)}}},")
    
    # Pages
    pages = book_data.get('number_of_pages')
    if pages:
        bibtex_lines.append(f"  pages = {{{pages}}},")
    
    # Remove trailing comma from last field
    if bibtex_lines[-1].endswith(','):
        bibtex_lines[-1] = bibtex_lines[-1][:-1]
    
    bibtex_lines.append("}")
    
    bibtex_entry = "\n".join(bibtex_lines)
    
    return {
        'bibtex': bibtex_entry,
        'cite_key': cite_key,
        'format': 'BibTeX',
        'book_title': book_data.get('title'),
        'authors': book_data.get('authors'),
        'year': year,
        'usage': f"Use \\cite{{{cite_key}}} in your LaTeX document"
    }

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python generate_bibtex.py <isbn_or_search_query>")
        print("\nExamples:")
        print("  python generate_bibtex.py 9780140328721")
        print("  python generate_bibtex.py 'Fantastic Mr Fox'")
        sys.exit(1)
    
    identifier = ' '.join(sys.argv[1:])
    
    # Get book data
    book_data = get_book_data(identifier)
    
    if not book_data:
        result = {'error': f'No book found for: {identifier}'}
    else:
        result = generate_bibtex(book_data)
    
    print(json.dumps(result, indent=2))

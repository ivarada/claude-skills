#!/usr/bin/env python3
"""
Generate APA 7th edition citations for books from OpenLibrary.
Usage: python generate_apa7_citation.py <isbn_or_openlibrary_id>
"""
import requests
import json
import sys
import re

def get_book_data(identifier):
    """
    Fetch book data from OpenLibrary.
    Accepts ISBN or OpenLibrary ID.
    """
    # Check if it's an ISBN or OpenLibrary ID
    if identifier.startswith('OL') or identifier.startswith('/books/'):
        if not identifier.startswith('/books/'):
            identifier = f'/books/{identifier}'
        url = f"https://openlibrary.org{identifier}.json"
    else:
        # Assume it's an ISBN
        isbn = identifier.replace('-', '').replace(' ', '')
        url = f"https://openlibrary.org/isbn/{isbn}.json"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

def get_author_name(author_key):
    """Fetch author name from OpenLibrary."""
    try:
        url = f"https://openlibrary.org{author_key}.json"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        author_data = response.json()
        return author_data.get('name', 'Unknown Author')
    except:
        return 'Unknown Author'

def format_author_apa7(author_name):
    """
    Format author name in APA 7 style: Last, F. M.
    """
    # Split name into parts
    parts = author_name.split()
    
    if len(parts) == 0:
        return "Unknown Author"
    elif len(parts) == 1:
        # Only one name (likely last name)
        return parts[0]
    elif len(parts) == 2:
        # First and last name
        last = parts[-1]
        first = parts[0]
        return f"{last}, {first[0]}."
    else:
        # Multiple names (First Middle Last or variations)
        last = parts[-1]
        initials = ' '.join([name[0] + '.' for name in parts[:-1]])
        return f"{last}, {initials}"

def generate_apa7_citation(book_data):
    """
    Generate APA 7th edition citation from book data.
    
    APA 7 Book Format:
    Author, A. A. (Year). Title of book: Subtitle. Publisher.
    """
    if 'error' in book_data:
        return {'error': book_data['error']}
    
    # Get authors
    authors = []
    if 'authors' in book_data:
        for author_ref in book_data['authors']:
            author_key = author_ref.get('key')
            if author_key:
                author_name = get_author_name(author_key)
                authors.append(format_author_apa7(author_name))
    
    if not authors:
        authors = ['Unknown Author']
    
    # Format multiple authors
    if len(authors) == 1:
        author_string = authors[0]
    elif len(authors) == 2:
        author_string = f"{authors[0]}, & {authors[1]}"
    elif len(authors) <= 20:
        author_string = ', '.join(authors[:-1]) + f", & {authors[-1]}"
    else:
        # More than 20 authors: list first 19, then "..." then last author
        author_string = ', '.join(authors[:19]) + f", ... {authors[-1]}"
    
    # Get year
    publish_date = book_data.get('publish_date', 'n.d.')
    year_match = re.search(r'\b(19|20)\d{2}\b', str(publish_date))
    year = year_match.group(0) if year_match else 'n.d.'
    
    # Get title and subtitle
    title = book_data.get('title', 'Unknown title')
    subtitle = book_data.get('subtitle', '')
    
    # Title should be in sentence case (only first word and proper nouns capitalized)
    # For simplicity, we'll use the title as provided
    full_title = f"{title}: {subtitle}" if subtitle else title
    
    # Get publisher
    publishers = book_data.get('publishers', [])
    publisher = publishers[0] if publishers else 'Unknown Publisher'
    
    # Construct citation
    citation = f"{author_string} ({year}). {full_title}. {publisher}."
    
    # Also return structured data
    return {
        'citation': citation,
        'authors': authors,
        'year': year,
        'title': full_title,
        'publisher': publisher,
        'style': 'APA 7th Edition'
    }

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python generate_apa7_citation.py <isbn_or_openlibrary_id>")
        sys.exit(1)
    
    identifier = sys.argv[1]
    book_data = get_book_data(identifier)
    
    if 'error' in book_data:
        print(json.dumps(book_data, indent=2))
    else:
        citation_data = generate_apa7_citation(book_data)
        print(json.dumps(citation_data, indent=2))

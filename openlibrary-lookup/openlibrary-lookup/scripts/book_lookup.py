#!/usr/bin/env python3
"""
Unified Book Lookup - Generate both APA7 and BibTeX citations
Supports the format: bib.isbn == <isbn_number>

Usage: 
  python book_lookup.py bib.isbn == 978-1566199094
  python book_lookup.py 9781566199094
  python book_lookup.py "The Great Gatsby"

This will:
1. Look up the book in OpenLibrary
2. Generate APA 7th edition citation
3. Generate BibTeX entry
4. Save both to files
"""
import requests
import json
import sys
import re
import os

def clean_string_for_bibtex(text):
    """Clean string for BibTeX format"""
    if not text:
        return ""
    text = text.replace('{', '\\{').replace('}', '\\}')
    text = text.replace('&', '\\&')
    return text

def generate_cite_key(authors, year, title):
    """
    Generate a BibTeX citation key
    Format: FirstAuthorLastName + Year + FirstTitleWord
    Example: Marshall1998Encyclopedia
    """
    author_part = "Unknown"
    if authors and len(authors) > 0:
        author_name = authors[0]
        parts = author_name.split()
        if parts:
            author_part = parts[-1]
    
    author_part = re.sub(r'[^a-zA-Z]', '', author_part)
    year_part = year if year else "nd"
    
    title_part = ""
    if title:
        words = title.split()
        skip_words = {'a', 'an', 'the', 'of', 'in', 'on', 'at', 'to', 'for'}
        for word in words:
            clean_word = re.sub(r'[^a-zA-Z]', '', word)
            if clean_word.lower() not in skip_words and len(clean_word) > 2:
                title_part = clean_word
                break
    
    if not title_part and title:
        title_part = re.sub(r'[^a-zA-Z]', '', title.split()[0])
    
    return f"{author_part.lower()}{year_part}{title_part.lower()}"

def format_author_apa7(author_name):
    """Format author name in APA 7 style: Last, F. M."""
    parts = author_name.split()
    
    if len(parts) == 0:
        return "Unknown Author"
    elif len(parts) == 1:
        return parts[0]
    elif len(parts) == 2:
        last = parts[-1]
        first = parts[0]
        return f"{last}, {first[0]}."
    else:
        last = parts[-1]
        initials = ' '.join([name[0] + '.' for name in parts[:-1]])
        return f"{last}, {initials}"

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
        except Exception as e:
            print(f"Error fetching ISBN: {e}", file=sys.stderr)
    
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
    except Exception as e:
        print(f"Error searching: {e}", file=sys.stderr)
    
    return None

def generate_apa7_citation(book_data):
    """Generate APA 7th edition citation"""
    if not book_data:
        return None
    
    # Get authors
    authors = book_data.get('authors', [])
    if not authors:
        authors = ['Unknown Author']
    
    apa_authors = [format_author_apa7(name) for name in authors]
    
    # Format multiple authors
    if len(apa_authors) == 1:
        author_string = apa_authors[0]
    elif len(apa_authors) == 2:
        author_string = f"{apa_authors[0]}, & {apa_authors[1]}"
    elif len(apa_authors) <= 20:
        author_string = ', '.join(apa_authors[:-1]) + f", & {apa_authors[-1]}"
    else:
        author_string = ', '.join(apa_authors[:19]) + f", ... {apa_authors[-1]}"
    
    # Get year
    publish_date = book_data.get('publish_date', 'n.d.')
    year_match = re.search(r'\b(19|20)\d{2}\b', str(publish_date))
    year = year_match.group(0) if year_match else 'n.d.'
    
    # Get title
    title = book_data.get('title', 'Unknown title')
    subtitle = book_data.get('subtitle', '')
    full_title = f"{title}: {subtitle}" if subtitle else title
    
    # Get publisher
    publishers = book_data.get('publishers', [])
    publisher = publishers[0] if publishers else 'Unknown Publisher'
    
    # Construct citation
    citation = f"{author_string} ({year}). {full_title}. {publisher}."
    
    return {
        'citation': citation,
        'authors': apa_authors,
        'year': year,
        'title': full_title,
        'publisher': publisher,
        'style': 'APA 7th Edition'
    }

def generate_bibtex(book_data):
    """Generate BibTeX format citation"""
    if not book_data:
        return None
    
    # Extract year
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
    
    # Authors
    authors = book_data.get('authors', [])
    if authors:
        author_str = " and ".join(authors)
        bibtex_lines.append(f"  author    = {{{clean_string_for_bibtex(author_str)}}},")
    
    # Title
    title = book_data.get('title', 'Untitled')
    subtitle = book_data.get('subtitle')
    if subtitle:
        full_title = f"{title}: {subtitle}"
    else:
        full_title = title
    bibtex_lines.append(f"  title     = {{{clean_string_for_bibtex(full_title)}}},")
    
    # Publisher
    publishers = book_data.get('publishers', [])
    if publishers and publishers[0]:
        bibtex_lines.append(f"  publisher = {{{clean_string_for_bibtex(publishers[0])}}},")
    
    # Year
    if year:
        bibtex_lines.append(f"  year      = {{{year}}},")
    
    # Address
    publish_place = book_data.get('publish_place', [])
    if publish_place and publish_place[0]:
        bibtex_lines.append(f"  address   = {{{clean_string_for_bibtex(publish_place[0])}}},")
    
    # ISBN
    isbn_13 = book_data.get('isbn_13', [])
    isbn_10 = book_data.get('isbn_10', [])
    if isbn_13:
        bibtex_lines.append(f"  isbn      = {{{isbn_13[0]}}},")
    elif isbn_10:
        bibtex_lines.append(f"  isbn      = {{{isbn_10[0]}}},")
    
    # Edition
    edition = book_data.get('edition')
    if edition:
        bibtex_lines.append(f"  edition   = {{{clean_string_for_bibtex(edition)}}},")
    
    # Pages
    pages = book_data.get('number_of_pages')
    if pages:
        bibtex_lines.append(f"  pages     = {{{pages}}},")
    
    # Remove trailing comma
    if bibtex_lines[-1].endswith(','):
        bibtex_lines[-1] = bibtex_lines[-1][:-1]
    
    bibtex_lines.append("}")
    bibtex_entry = "\n".join(bibtex_lines)
    
    return {
        'bibtex': bibtex_entry,
        'cite_key': cite_key
    }

def save_citations(isbn, apa_data, bibtex_data, output_dir="."):
    """Save APA and BibTeX citations to files"""
    clean_isbn = isbn.replace('-', '').replace(' ', '')
    
    # Save APA citation
    apa_filename = os.path.join(output_dir, f"{clean_isbn}_apa7.txt")
    with open(apa_filename, 'w', encoding='utf-8') as f:
        f.write(f"APA 7th Edition Citation:\n")
        f.write(f"{'-' * 50}\n\n")
        f.write(apa_data['citation'])
        f.write(f"\n\n{'-' * 50}\n")
        f.write(f"Authors: {', '.join(apa_data['authors'])}\n")
        f.write(f"Year: {apa_data['year']}\n")
        f.write(f"Title: {apa_data['title']}\n")
        f.write(f"Publisher: {apa_data['publisher']}\n")
    
    # Save BibTeX citation
    bibtex_filename = os.path.join(output_dir, f"{clean_isbn}.bib")
    with open(bibtex_filename, 'w', encoding='utf-8') as f:
        f.write(bibtex_data['bibtex'])
    
    return apa_filename, bibtex_filename

def main():
    if len(sys.argv) < 2:
        print("Usage: python book_lookup.py [bib.isbn ==] <isbn_or_query>")
        print("\nExamples:")
        print("  python book_lookup.py bib.isbn == 978-1566199094")
        print("  python book_lookup.py 9781566199094")
        print("  python book_lookup.py 'The Great Gatsby'")
        sys.exit(1)
    
    # Parse arguments - support "bib.isbn == <isbn>" format
    args = sys.argv[1:]
    
    # Check for bib.isbn == format
    if 'bib.isbn' in args[0].lower() or '==' in ' '.join(args):
        # Extract ISBN after ==
        full_arg = ' '.join(args)
        if '==' in full_arg:
            identifier = full_arg.split('==')[1].strip()
        else:
            identifier = args[-1]
    else:
        identifier = ' '.join(args)
    
    print(f"Looking up: {identifier}")
    print("-" * 50)
    
    # Get book data
    book_data = get_book_data(identifier)
    
    if not book_data:
        result = {'error': f'No book found for: {identifier}'}
        print(json.dumps(result, indent=2))
        sys.exit(1)
    
    # Generate citations
    apa_citation = generate_apa7_citation(book_data)
    bibtex_citation = generate_bibtex(book_data)
    
    # Display results
    print("\n📚 BOOK INFORMATION")
    print("=" * 50)
    print(f"Title: {book_data.get('title', 'N/A')}")
    if book_data.get('subtitle'):
        print(f"Subtitle: {book_data['subtitle']}")
    print(f"Authors: {', '.join(book_data.get('authors', ['N/A']))}")
    print(f"Publisher: {', '.join(book_data.get('publishers', ['N/A']))}")
    print(f"Year: {book_data.get('publish_date', 'N/A')}")
    if book_data.get('isbn_13'):
        print(f"ISBN-13: {book_data['isbn_13'][0]}")
    if book_data.get('isbn_10'):
        print(f"ISBN-10: {book_data['isbn_10'][0]}")
    
    print("\n\n📖 APA 7TH EDITION CITATION")
    print("=" * 50)
    print(apa_citation['citation'])
    
    print("\n\n📚 BIBTEX CITATION")
    print("=" * 50)
    print(bibtex_citation['bibtex'])
    
    # Save to files
    apa_file, bibtex_file = save_citations(
        identifier,
        apa_citation,
        bibtex_citation,
        output_dir="/home/claude"
    )
    
    print("\n\n💾 FILES SAVED")
    print("=" * 50)
    print(f"APA Citation: {apa_file}")
    print(f"BibTeX Entry: {bibtex_file}")
    
    # Return JSON for programmatic use
    result = {
        'book_data': book_data,
        'apa7': apa_citation,
        'bibtex': bibtex_citation,
        'files': {
            'apa': apa_file,
            'bibtex': bibtex_file
        }
    }
    
    print("\n\n📋 JSON OUTPUT")
    print("=" * 50)
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()

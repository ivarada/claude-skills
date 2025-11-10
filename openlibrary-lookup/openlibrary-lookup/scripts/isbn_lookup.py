#!/usr/bin/env python3
"""
Look up a book by ISBN using the OpenLibrary API.
Usage: python isbn_lookup.py <isbn>
"""
import requests
import json
import sys

def lookup_isbn(isbn):
    """
    Look up a book by ISBN.
    
    Args:
        isbn: ISBN-10 or ISBN-13
    
    Returns:
        Book information dictionary
    """
    # Remove hyphens and spaces from ISBN
    isbn = isbn.replace('-', '').replace(' ', '')
    
    url = f"https://openlibrary.org/isbn/{isbn}.json"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        book_data = response.json()
        
        # Get additional work information if available
        work_key = book_data.get('works', [{}])[0].get('key') if book_data.get('works') else None
        
        result = {
            'title': book_data.get('title'),
            'subtitle': book_data.get('subtitle'),
            'authors': [],
            'publish_date': book_data.get('publish_date'),
            'publishers': book_data.get('publishers', []),
            'isbn_10': book_data.get('isbn_10', []),
            'isbn_13': book_data.get('isbn_13', []),
            'number_of_pages': book_data.get('number_of_pages'),
            'cover_ids': book_data.get('covers', []),
            'work_key': work_key,
            'openlibrary_key': book_data.get('key')
        }
        
        # Get author information
        if 'authors' in book_data:
            for author_ref in book_data['authors']:
                author_key = author_ref.get('key')
                if author_key:
                    author_url = f"https://openlibrary.org{author_key}.json"
                    author_response = requests.get(author_url, timeout=10)
                    if author_response.status_code == 200:
                        author_data = author_response.json()
                        result['authors'].append({
                            'name': author_data.get('name'),
                            'key': author_key
                        })
        
        # Add cover URL if available
        if result['cover_ids']:
            result['cover_url'] = f"https://covers.openlibrary.org/b/id/{result['cover_ids'][0]}-L.jpg"
        
        return result
    
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return {'error': f'No book found with ISBN: {isbn}'}
        return {'error': str(e)}
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python isbn_lookup.py <isbn>")
        sys.exit(1)
    
    isbn = sys.argv[1]
    result = lookup_isbn(isbn)
    print(json.dumps(result, indent=2))

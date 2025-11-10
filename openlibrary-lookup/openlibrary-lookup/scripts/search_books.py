#!/usr/bin/env python3
"""
Search for books using the OpenLibrary Search API.
Usage: python search_books.py "query string" [--limit 5]
"""
import requests
import json
import sys
import argparse

def search_books(query, limit=5):
    """
    Search for books on OpenLibrary.
    
    Args:
        query: Search query (title, author, subject, etc.)
        limit: Maximum number of results to return
    
    Returns:
        List of book results with key information
    """
    base_url = "https://openlibrary.org/search.json"
    params = {
        'q': query,
        'limit': limit,
        'fields': 'key,title,author_name,first_publish_year,isbn,publisher,number_of_pages_median,cover_i'
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        books = []
        for doc in data.get('docs', []):
            book = {
                'title': doc.get('title', 'Unknown'),
                'authors': doc.get('author_name', []),
                'first_published': doc.get('first_publish_year'),
                'isbn': doc.get('isbn', [])[0] if doc.get('isbn') else None,
                'publishers': doc.get('publisher', []),
                'pages': doc.get('number_of_pages_median'),
                'cover_id': doc.get('cover_i'),
                'openlibrary_key': doc.get('key'),
                'cover_url': f"https://covers.openlibrary.org/b/id/{doc.get('cover_i')}-M.jpg" if doc.get('cover_i') else None
            }
            books.append(book)
        
        return {
            'num_found': data.get('numFound', 0),
            'books': books
        }
    
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search for books on OpenLibrary')
    parser.add_argument('query', help='Search query')
    parser.add_argument('--limit', type=int, default=5, help='Maximum results to return')
    
    args = parser.parse_args()
    results = search_books(args.query, args.limit)
    print(json.dumps(results, indent=2))

#!/usr/bin/env python3
"""
Get author information from OpenLibrary.
Usage: python get_author_info.py <author_key_or_name>
"""
import requests
import json
import sys

def get_author_by_key(author_key):
    """Get author info by OpenLibrary author key (e.g., OL23919A)"""
    if not author_key.startswith('/authors/'):
        author_key = f'/authors/{author_key}'
    
    url = f"https://openlibrary.org{author_key}.json"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

def search_author(author_name):
    """Search for an author by name"""
    url = "https://openlibrary.org/search/authors.json"
    params = {'q': author_name}
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data.get('numFound', 0) > 0:
            authors = []
            for doc in data.get('docs', [])[:5]:
                authors.append({
                    'name': doc.get('name'),
                    'key': doc.get('key'),
                    'birth_date': doc.get('birth_date'),
                    'death_date': doc.get('death_date'),
                    'work_count': doc.get('work_count'),
                    'top_work': doc.get('top_work')
                })
            return {'authors': authors}
        else:
            return {'error': f'No authors found matching: {author_name}'}
    
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python get_author_info.py <author_key_or_name>")
        sys.exit(1)
    
    query = sys.argv[1]
    
    # Check if it's an author key or name
    if query.startswith('OL') or query.startswith('/authors/'):
        result = get_author_by_key(query)
    else:
        result = search_author(query)
    
    print(json.dumps(result, indent=2))

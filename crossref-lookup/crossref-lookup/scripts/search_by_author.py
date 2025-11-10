#!/usr/bin/env python3
"""
Search for publications by author name using the Crossref API.
Usage: python search_by_author.py "Author Name" [--rows 10]
"""
import requests
import json
import sys
import argparse

def search_by_author(author_name, rows=10, mailto="user@example.com"):
    """
    Search for publications by author.
    
    Args:
        author_name: Author name to search for
        rows: Number of results to return
        mailto: Email for polite pool
    
    Returns:
        List of publications by the author
    """
    url = "https://api.crossref.org/works"
    
    params = {
        'query.author': author_name,
        'rows': rows
    }
    
    headers = {
        'User-Agent': f'CrossrefLookupSkill/1.0 (mailto:{mailto})'
    }
    
    try:
        response = requests.get(url, params=params, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        if data['status'] == 'ok':
            items = data['message']['items']
            total_results = data['message']['total-results']
            
            publications = []
            for item in items:
                pub = {
                    'doi': item.get('DOI'),
                    'title': item.get('title', ['Unknown'])[0] if item.get('title') else 'Unknown',
                    'type': item.get('type'),
                    'authors': [],
                    'published_year': None,
                    'journal': item.get('container-title', ['Unknown'])[0] if item.get('container-title') else None,
                    'publisher': item.get('publisher'),
                    'url': item.get('URL')
                }
                
                # Get all authors
                if 'author' in item:
                    for author in item['author']:
                        name = f"{author.get('given', '')} {author.get('family', '')}".strip()
                        if name:
                            pub['authors'].append(name)
                
                # Get publication year
                if 'published' in item or 'published-print' in item:
                    pub_date = item.get('published') or item.get('published-print')
                    if pub_date and 'date-parts' in pub_date:
                        pub['published_year'] = pub_date['date-parts'][0][0]
                
                publications.append(pub)
            
            return {
                'author_searched': author_name,
                'total_results': total_results,
                'returned_results': len(publications),
                'publications': publications
            }
        else:
            return {'error': 'Search failed'}
    
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search for publications by author')
    parser.add_argument('author', help='Author name')
    parser.add_argument('--rows', type=int, default=10, help='Number of results')
    
    args = parser.parse_args()
    results = search_by_author(args.author, args.rows)
    print(json.dumps(results, indent=2))

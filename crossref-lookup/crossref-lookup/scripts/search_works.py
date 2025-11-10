#!/usr/bin/env python3
"""
Search for academic works using the Crossref API.
Usage: python search_works.py "query string" [--rows 10] [--filter "filter_string"]
"""
import requests
import json
import sys
import argparse

def search_works(query, rows=10, filter_str=None, mailto="user@example.com"):
    """
    Search Crossref for academic works.
    
    Args:
        query: Search query string
        rows: Number of results to return (max 1000)
        filter_str: Crossref filter string (e.g., "from-pub-date:2020,type:journal-article")
        mailto: Email for polite pool
    
    Returns:
        List of matching works
    """
    url = "https://api.crossref.org/works"
    
    params = {
        'query': query,
        'rows': rows
    }
    
    if filter_str:
        params['filter'] = filter_str
    
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
            
            works = []
            for item in items:
                work = {
                    'doi': item.get('DOI'),
                    'title': item.get('title', ['Unknown'])[0] if item.get('title') else 'Unknown',
                    'type': item.get('type'),
                    'authors': [],
                    'published_year': None,
                    'journal': item.get('container-title', ['Unknown'])[0] if item.get('container-title') else None,
                    'publisher': item.get('publisher'),
                    'url': item.get('URL'),
                    'score': item.get('score')
                }
                
                # Get authors
                if 'author' in item:
                    for author in item['author'][:5]:  # Limit to first 5 authors
                        name = f"{author.get('given', '')} {author.get('family', '')}".strip()
                        if name:
                            work['authors'].append(name)
                
                # Get publication year
                if 'published' in item or 'published-print' in item:
                    pub_date = item.get('published') or item.get('published-print')
                    if pub_date and 'date-parts' in pub_date:
                        work['published_year'] = pub_date['date-parts'][0][0]
                
                works.append(work)
            
            return {
                'total_results': total_results,
                'returned_results': len(works),
                'works': works
            }
        else:
            return {'error': 'Search failed'}
    
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Search Crossref for academic works')
    parser.add_argument('query', help='Search query')
    parser.add_argument('--rows', type=int, default=10, help='Number of results')
    parser.add_argument('--filter', dest='filter_str', help='Crossref filter string')
    
    args = parser.parse_args()
    results = search_works(args.query, args.rows, args.filter_str)
    print(json.dumps(results, indent=2))

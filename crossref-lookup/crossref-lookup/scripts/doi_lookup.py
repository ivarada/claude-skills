#!/usr/bin/env python3
"""
Look up publication metadata by DOI using the Crossref API.
Usage: python doi_lookup.py <doi>
"""
import requests
import json
import sys

def lookup_doi(doi, mailto="user@example.com"):
    """
    Look up a publication by DOI.
    
    Args:
        doi: DOI string (with or without https://doi.org/ prefix)
        mailto: Email for Crossref polite pool (better rate limits)
    
    Returns:
        Publication metadata dictionary
    """
    # Clean DOI
    doi = doi.replace('https://doi.org/', '').replace('http://doi.org/', '')
    
    # Crossref API endpoint
    url = f"https://api.crossref.org/works/{doi}"
    
    headers = {
        'User-Agent': f'CrossrefLookupSkill/1.0 (mailto:{mailto})'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        if data['status'] == 'ok':
            message = data['message']
            
            # Extract key information
            result = {
                'doi': message.get('DOI'),
                'title': message.get('title', ['Unknown'])[0] if message.get('title') else 'Unknown',
                'type': message.get('type'),
                'authors': [],
                'published': {},
                'journal': {},
                'abstract': message.get('abstract'),
                'url': message.get('URL'),
                'publisher': message.get('publisher'),
                'issn': message.get('ISSN', []),
                'isbn': message.get('ISBN', []),
                'references_count': message.get('references-count', 0),
                'is_referenced_by_count': message.get('is-referenced-by-count', 0),
                'subject': message.get('subject', []),
                'license': message.get('license', []),
                'full_metadata': message
            }
            
            # Parse authors
            if 'author' in message:
                for author in message['author']:
                    author_info = {
                        'given': author.get('given', ''),
                        'family': author.get('family', ''),
                        'name': f"{author.get('given', '')} {author.get('family', '')}".strip(),
                        'affiliation': author.get('affiliation', [])
                    }
                    result['authors'].append(author_info)
            
            # Parse publication date
            if 'published' in message or 'published-print' in message or 'published-online' in message:
                pub_date = message.get('published') or message.get('published-print') or message.get('published-online')
                if pub_date and 'date-parts' in pub_date:
                    date_parts = pub_date['date-parts'][0]
                    result['published'] = {
                        'year': date_parts[0] if len(date_parts) > 0 else None,
                        'month': date_parts[1] if len(date_parts) > 1 else None,
                        'day': date_parts[2] if len(date_parts) > 2 else None,
                        'raw': pub_date
                    }
            
            # Parse journal information
            if 'container-title' in message:
                result['journal'] = {
                    'name': message.get('container-title', ['Unknown'])[0] if message.get('container-title') else 'Unknown',
                    'volume': message.get('volume'),
                    'issue': message.get('issue'),
                    'page': message.get('page'),
                    'issn': message.get('ISSN', [])
                }
            
            return result
        else:
            return {'error': 'DOI not found or API error'}
    
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return {'error': f'DOI not found: {doi}'}
        return {'error': str(e)}
    except requests.exceptions.RequestException as e:
        return {'error': f'Request failed: {str(e)}'}

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python doi_lookup.py <doi>")
        sys.exit(1)
    
    doi = sys.argv[1]
    result = lookup_doi(doi)
    print(json.dumps(result, indent=2))

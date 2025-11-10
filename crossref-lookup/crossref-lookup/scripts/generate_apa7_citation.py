#!/usr/bin/env python3
"""
Generate APA 7th edition citations from DOIs using the Crossref API.
Usage: python generate_apa7_citation.py <doi>
"""
import requests
import json
import sys

def get_doi_metadata(doi, mailto="user@example.com"):
    """Fetch metadata from Crossref API."""
    doi = doi.replace('https://doi.org/', '').replace('http://doi.org/', '')
    url = f"https://api.crossref.org/works/{doi}"
    
    headers = {
        'User-Agent': f'CrossrefLookupSkill/1.0 (mailto:{mailto})'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()
        return data['message'] if data['status'] == 'ok' else None
    except:
        return None

def format_author_apa7(given, family):
    """Format author name in APA 7 style."""
    if not family:
        return "Unknown"
    if not given:
        return family
    
    # Get initials from given name
    initials = ' '.join([name[0] + '.' for name in given.split()])
    return f"{family}, {initials}"

def generate_apa7_citation(doi):
    """
    Generate APA 7th edition citation from DOI.
    
    Supports:
    - Journal articles
    - Books and book chapters
    - Conference papers
    - Reports and other publication types
    """
    metadata = get_doi_metadata(doi)
    
    if not metadata:
        return {'error': f'Could not retrieve metadata for DOI: {doi}'}
    
    # Get authors
    authors = []
    if 'author' in metadata:
        for author in metadata['author']:
            given = author.get('given', '')
            family = author.get('family', '')
            authors.append(format_author_apa7(given, family))
    
    if not authors:
        authors = ['Unknown Author']
    
    # Format multiple authors (APA 7 style)
    if len(authors) == 1:
        author_string = authors[0]
    elif len(authors) == 2:
        author_string = f"{authors[0]}, & {authors[1]}"
    elif len(authors) <= 20:
        author_string = ', '.join(authors[:-1]) + f", & {authors[-1]}"
    else:
        # More than 20 authors: list first 19, ellipsis, then last
        author_string = ', '.join(authors[:19]) + f", ... {authors[-1]}"
    
    # Get publication year
    year = 'n.d.'
    if 'published' in metadata or 'published-print' in metadata or 'published-online' in metadata:
        pub_date = metadata.get('published') or metadata.get('published-print') or metadata.get('published-online')
        if pub_date and 'date-parts' in pub_date:
            year = str(pub_date['date-parts'][0][0])
    
    # Get title
    title = metadata.get('title', ['Unknown title'])[0] if metadata.get('title') else 'Unknown title'
    
    # Get publication type
    pub_type = metadata.get('type', 'unknown')
    
    # Format citation based on type
    if pub_type in ['journal-article', 'article-journal']:
        # Journal Article Format
        journal = metadata.get('container-title', ['Unknown journal'])[0] if metadata.get('container-title') else 'Unknown journal'
        volume = metadata.get('volume', '')
        issue = metadata.get('issue', '')
        pages = metadata.get('page', '')
        
        # Format volume/issue/pages
        vol_issue = f"{volume}" if volume else ""
        if issue:
            vol_issue += f"({issue})"
        if pages:
            vol_issue += f", {pages}"
        
        citation = f"{author_string} ({year}). {title}. *{journal}*"
        if vol_issue:
            citation += f", *{vol_issue}*"
        citation += f". https://doi.org/{doi}"
        
    elif pub_type in ['book', 'monograph']:
        # Book Format
        publisher = metadata.get('publisher', 'Unknown Publisher')
        citation = f"{author_string} ({year}). *{title}*. {publisher}. https://doi.org/{doi}"
        
    elif pub_type in ['book-chapter', 'book-section']:
        # Book Chapter Format
        container = metadata.get('container-title', ['Unknown book'])[0] if metadata.get('container-title') else 'Unknown book'
        publisher = metadata.get('publisher', 'Unknown Publisher')
        pages = metadata.get('page', '')
        
        citation = f"{author_string} ({year}). {title}. In *{container}*"
        if pages:
            citation += f" (pp. {pages})"
        citation += f". {publisher}. https://doi.org/{doi}"
        
    elif pub_type in ['proceedings-article', 'paper-conference']:
        # Conference Paper Format
        container = metadata.get('container-title', ['Unknown conference'])[0] if metadata.get('container-title') else 'Unknown conference'
        publisher = metadata.get('publisher', '')
        
        citation = f"{author_string} ({year}). {title}. *{container}*"
        if publisher:
            citation += f". {publisher}"
        citation += f". https://doi.org/{doi}"
        
    else:
        # Generic Format for other types
        publisher = metadata.get('publisher', 'Unknown Publisher')
        citation = f"{author_string} ({year}). {title}. {publisher}. https://doi.org/{doi}"
    
    return {
        'citation': citation,
        'authors': authors,
        'year': year,
        'title': title,
        'doi': doi,
        'type': pub_type,
        'style': 'APA 7th Edition'
    }

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python generate_apa7_citation.py <doi>")
        sys.exit(1)
    
    doi = sys.argv[1]
    result = generate_apa7_citation(doi)
    print(json.dumps(result, indent=2))

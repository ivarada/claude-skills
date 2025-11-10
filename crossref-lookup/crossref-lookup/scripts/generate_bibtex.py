#!/usr/bin/env python3
"""
Generate BibTeX entries from DOIs using the Crossref API.
Usage: python generate_bibtex.py <doi>
"""
import requests
import json
import sys
import re

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

def sanitize_for_bibtex(text):
    """Sanitize text for BibTeX format."""
    if not text:
        return ""
    
    replacements = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}'
    }
    
    for old, new in replacements.items():
        text = text.replace(old, new)
    
    return text

def generate_citation_key(authors, year, title):
    """Generate citation key: firstauthor_year_firstword"""
    # Get first author's last name
    if authors:
        first_author = authors[0].get('family', 'unknown').lower()
        first_author = re.sub(r'[^a-z]', '', first_author)
    else:
        first_author = 'unknown'
    
    # Get first significant word from title
    title_words = re.findall(r'\b\w+\b', title.lower())
    skip_words = {'a', 'an', 'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of'}
    first_word = next((word for word in title_words if word not in skip_words), 'work')
    
    # Clean year
    year_str = str(year) if year != 'n.d.' else 'nd'
    
    return f"{first_author}_{year_str}_{first_word}"

def generate_bibtex(doi):
    """
    Generate BibTeX entry from DOI.
    
    Supports:
    - @article (journal articles)
    - @book (books)
    - @inbook (book chapters)
    - @inproceedings (conference papers)
    - @misc (other types)
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
            if family:
                authors.append({'given': given, 'family': family})
    
    if not authors:
        author_string = 'Unknown Author'
    else:
        author_string = ' and '.join([f"{a['family']}, {a['given']}" if a['given'] else a['family'] for a in authors])
    
    # Get year
    year = 'n.d.'
    if 'published' in metadata or 'published-print' in metadata:
        pub_date = metadata.get('published') or metadata.get('published-print')
        if pub_date and 'date-parts' in pub_date:
            year = str(pub_date['date-parts'][0][0])
    
    # Get title
    title = metadata.get('title', ['Unknown title'])[0] if metadata.get('title') else 'Unknown title'
    
    # Get publication type
    pub_type = metadata.get('type', 'misc')
    
    # Generate citation key
    citation_key = generate_citation_key(metadata.get('author', []), year, title)
    
    # Sanitize fields
    author_string = sanitize_for_bibtex(author_string)
    title = sanitize_for_bibtex(title)
    
    # Build BibTeX entry based on type
    if pub_type in ['journal-article', 'article-journal']:
        # Journal Article
        entry_type = 'article'
        journal = metadata.get('container-title', ['Unknown'])[0] if metadata.get('container-title') else 'Unknown'
        journal = sanitize_for_bibtex(journal)
        volume = metadata.get('volume', '')
        issue = metadata.get('issue', '')
        pages = metadata.get('page', '')
        
        bibtex = f"@{entry_type}{{{citation_key},\n"
        bibtex += f"  author = {{{author_string}}},\n"
        bibtex += f"  title = {{{title}}},\n"
        bibtex += f"  journal = {{{journal}}},\n"
        bibtex += f"  year = {{{year}}},\n"
        if volume:
            bibtex += f"  volume = {{{volume}}},\n"
        if issue:
            bibtex += f"  number = {{{issue}}},\n"
        if pages:
            bibtex += f"  pages = {{{pages}}},\n"
        bibtex += f"  doi = {{{doi}}}\n}}"
        
    elif pub_type in ['book', 'monograph']:
        # Book
        entry_type = 'book'
        publisher = metadata.get('publisher', 'Unknown')
        publisher = sanitize_for_bibtex(publisher)
        isbn = metadata.get('ISBN', [])
        
        bibtex = f"@{entry_type}{{{citation_key},\n"
        bibtex += f"  author = {{{author_string}}},\n"
        bibtex += f"  title = {{{title}}},\n"
        bibtex += f"  publisher = {{{publisher}}},\n"
        bibtex += f"  year = {{{year}}},\n"
        if isbn:
            bibtex += f"  isbn = {{{isbn[0]}}},\n"
        bibtex += f"  doi = {{{doi}}}\n}}"
        
    elif pub_type in ['book-chapter', 'book-section']:
        # Book Chapter
        entry_type = 'inbook'
        booktitle = metadata.get('container-title', ['Unknown'])[0] if metadata.get('container-title') else 'Unknown'
        booktitle = sanitize_for_bibtex(booktitle)
        publisher = metadata.get('publisher', 'Unknown')
        publisher = sanitize_for_bibtex(publisher)
        pages = metadata.get('page', '')
        
        bibtex = f"@{entry_type}{{{citation_key},\n"
        bibtex += f"  author = {{{author_string}}},\n"
        bibtex += f"  title = {{{title}}},\n"
        bibtex += f"  booktitle = {{{booktitle}}},\n"
        bibtex += f"  publisher = {{{publisher}}},\n"
        bibtex += f"  year = {{{year}}},\n"
        if pages:
            bibtex += f"  pages = {{{pages}}},\n"
        bibtex += f"  doi = {{{doi}}}\n}}"
        
    elif pub_type in ['proceedings-article', 'paper-conference']:
        # Conference Paper
        entry_type = 'inproceedings'
        booktitle = metadata.get('container-title', ['Unknown'])[0] if metadata.get('container-title') else 'Unknown'
        booktitle = sanitize_for_bibtex(booktitle)
        publisher = metadata.get('publisher', '')
        pages = metadata.get('page', '')
        
        bibtex = f"@{entry_type}{{{citation_key},\n"
        bibtex += f"  author = {{{author_string}}},\n"
        bibtex += f"  title = {{{title}}},\n"
        bibtex += f"  booktitle = {{{booktitle}}},\n"
        bibtex += f"  year = {{{year}}},\n"
        if publisher:
            publisher = sanitize_for_bibtex(publisher)
            bibtex += f"  publisher = {{{publisher}}},\n"
        if pages:
            bibtex += f"  pages = {{{pages}}},\n"
        bibtex += f"  doi = {{{doi}}}\n}}"
        
    else:
        # Generic/Misc
        entry_type = 'misc'
        publisher = metadata.get('publisher', '')
        
        bibtex = f"@{entry_type}{{{citation_key},\n"
        bibtex += f"  author = {{{author_string}}},\n"
        bibtex += f"  title = {{{title}}},\n"
        bibtex += f"  year = {{{year}}},\n"
        if publisher:
            publisher = sanitize_for_bibtex(publisher)
            bibtex += f"  publisher = {{{publisher}}},\n"
        bibtex += f"  doi = {{{doi}}}\n}}"
    
    return {
        'bibtex': bibtex,
        'citation_key': citation_key,
        'entry_type': entry_type,
        'doi': doi
    }

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python generate_bibtex.py <doi>")
        sys.exit(1)
    
    doi = sys.argv[1]
    result = generate_bibtex(doi)
    print(json.dumps(result, indent=2))

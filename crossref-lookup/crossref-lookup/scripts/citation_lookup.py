#!/usr/bin/env python3
"""
Unified DOI Citation Lookup - Generate both APA7 and BibTeX citations
Supports the format: bib.doi == <doi>

Usage: 
  python citation_lookup.py bib.doi == 10.1038/s41586-025-09663-y
  python citation_lookup.py bib.doi == https://doi.org/10.1038/s41586-025-09663-y
  python citation_lookup.py 10.1038/s41586-025-09663-y
  python citation_lookup.py https://doi.org/10.1038/s41586-025-09663-y

This will:
1. Look up the publication in Crossref
2. Generate APA 7th edition citation
3. Generate BibTeX entry
4. Save both to files
"""
import requests
import json
import sys
import re
import os

def get_doi_metadata(doi, mailto="user@example.com"):
    """Fetch metadata from Crossref API."""
    # Clean DOI - remove URL prefix if present
    doi = doi.replace('https://doi.org/', '').replace('http://doi.org/', '')
    doi = doi.strip()
    
    url = f"https://api.crossref.org/works/{doi}"
    
    headers = {
        'User-Agent': f'CrossrefLookupSkill/2.0 (mailto:{mailto})'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()
        return data['message'] if data['status'] == 'ok' else None
    except Exception as e:
        print(f"Error fetching DOI: {e}", file=sys.stderr)
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
    
    return f"{first_author}{year_str}{first_word}"

def format_author_apa7(author):
    """Format a single author in APA 7 style."""
    family = author.get('family', '')
    given = author.get('given', '')
    
    if not family:
        return 'Unknown'
    
    if given:
        # Extract initials
        initials = ' '.join([f"{name[0]}." for name in given.split()])
        return f"{family}, {initials}"
    else:
        return family

def generate_apa7_citation(metadata, doi):
    """Generate APA 7th edition citation."""
    if not metadata:
        return None
    
    # Get authors
    authors = metadata.get('author', [])
    if not authors:
        author_string = 'Unknown Author'
    else:
        apa_authors = [format_author_apa7(a) for a in authors]
        
        if len(apa_authors) == 1:
            author_string = apa_authors[0]
        elif len(apa_authors) == 2:
            author_string = f"{apa_authors[0]}, & {apa_authors[1]}"
        elif len(apa_authors) <= 20:
            author_string = ', '.join(apa_authors[:-1]) + f", & {apa_authors[-1]}"
        else:
            author_string = ', '.join(apa_authors[:19]) + f", ... {apa_authors[-1]}"
    
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
    
    # Build citation based on type
    if pub_type in ['journal-article', 'article-journal']:
        # Journal Article
        journal = metadata.get('container-title', ['Unknown'])[0] if metadata.get('container-title') else 'Unknown'
        volume = metadata.get('volume', '')
        issue = metadata.get('issue', '')
        pages = metadata.get('page', '')
        
        citation = f"{author_string} ({year}). {title}. {journal}"
        if volume:
            citation += f", {volume}"
        if issue:
            citation += f"({issue})"
        if pages:
            citation += f", {pages}"
        citation += f". https://doi.org/{doi}"
        
    elif pub_type in ['book', 'monograph']:
        # Book
        publisher = metadata.get('publisher', 'Unknown Publisher')
        citation = f"{author_string} ({year}). {title}. {publisher}. https://doi.org/{doi}"
        
    elif pub_type in ['book-chapter', 'book-section']:
        # Book Chapter
        booktitle = metadata.get('container-title', ['Unknown'])[0] if metadata.get('container-title') else 'Unknown'
        publisher = metadata.get('publisher', 'Unknown Publisher')
        pages = metadata.get('page', '')
        
        citation = f"{author_string} ({year}). {title}. In {booktitle}"
        if pages:
            citation += f" (pp. {pages})"
        citation += f". {publisher}. https://doi.org/{doi}"
        
    elif pub_type in ['proceedings-article', 'paper-conference']:
        # Conference Paper
        conference = metadata.get('container-title', ['Unknown'])[0] if metadata.get('container-title') else 'Unknown'
        publisher = metadata.get('publisher', '')
        pages = metadata.get('page', '')
        
        citation = f"{author_string} ({year}). {title}. In {conference}"
        if pages:
            citation += f" (pp. {pages})"
        if publisher:
            citation += f". {publisher}"
        citation += f". https://doi.org/{doi}"
        
    else:
        # Generic
        publisher = metadata.get('publisher', '')
        citation = f"{author_string} ({year}). {title}"
        if publisher:
            citation += f". {publisher}"
        citation += f". https://doi.org/{doi}"
    
    return {
        'citation': citation,
        'authors': [format_author_apa7(a) for a in authors] if authors else ['Unknown Author'],
        'year': year,
        'title': title,
        'type': pub_type,
        'style': 'APA 7th Edition'
    }

def generate_bibtex(metadata, doi):
    """Generate BibTeX format citation."""
    if not metadata:
        return None
    
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
        bibtex += f"  author  = {{{author_string}}},\n"
        bibtex += f"  title   = {{{title}}},\n"
        bibtex += f"  journal = {{{journal}}},\n"
        bibtex += f"  year    = {{{year}}},\n"
        if volume:
            bibtex += f"  volume  = {{{volume}}},\n"
        if issue:
            bibtex += f"  number  = {{{issue}}},\n"
        if pages:
            bibtex += f"  pages   = {{{pages}}},\n"
        bibtex += f"  doi     = {{{doi}}}\n}}"
        
    elif pub_type in ['book', 'monograph']:
        # Book
        entry_type = 'book'
        publisher = metadata.get('publisher', 'Unknown')
        publisher = sanitize_for_bibtex(publisher)
        isbn = metadata.get('ISBN', [])
        
        bibtex = f"@{entry_type}{{{citation_key},\n"
        bibtex += f"  author    = {{{author_string}}},\n"
        bibtex += f"  title     = {{{title}}},\n"
        bibtex += f"  publisher = {{{publisher}}},\n"
        bibtex += f"  year      = {{{year}}},\n"
        if isbn:
            bibtex += f"  isbn      = {{{isbn[0]}}},\n"
        bibtex += f"  doi       = {{{doi}}}\n}}"
        
    elif pub_type in ['book-chapter', 'book-section']:
        # Book Chapter
        entry_type = 'inbook'
        booktitle = metadata.get('container-title', ['Unknown'])[0] if metadata.get('container-title') else 'Unknown'
        booktitle = sanitize_for_bibtex(booktitle)
        publisher = metadata.get('publisher', 'Unknown')
        publisher = sanitize_for_bibtex(publisher)
        pages = metadata.get('page', '')
        
        bibtex = f"@{entry_type}{{{citation_key},\n"
        bibtex += f"  author    = {{{author_string}}},\n"
        bibtex += f"  title     = {{{title}}},\n"
        bibtex += f"  booktitle = {{{booktitle}}},\n"
        bibtex += f"  publisher = {{{publisher}}},\n"
        bibtex += f"  year      = {{{year}}},\n"
        if pages:
            bibtex += f"  pages     = {{{pages}}},\n"
        bibtex += f"  doi       = {{{doi}}}\n}}"
        
    elif pub_type in ['proceedings-article', 'paper-conference']:
        # Conference Paper
        entry_type = 'inproceedings'
        booktitle = metadata.get('container-title', ['Unknown'])[0] if metadata.get('container-title') else 'Unknown'
        booktitle = sanitize_for_bibtex(booktitle)
        publisher = metadata.get('publisher', '')
        pages = metadata.get('page', '')
        
        bibtex = f"@{entry_type}{{{citation_key},\n"
        bibtex += f"  author    = {{{author_string}}},\n"
        bibtex += f"  title     = {{{title}}},\n"
        bibtex += f"  booktitle = {{{booktitle}}},\n"
        bibtex += f"  year      = {{{year}}},\n"
        if publisher:
            publisher = sanitize_for_bibtex(publisher)
            bibtex += f"  publisher = {{{publisher}}},\n"
        if pages:
            bibtex += f"  pages     = {{{pages}}},\n"
        bibtex += f"  doi       = {{{doi}}}\n}}"
        
    else:
        # Generic/Misc
        entry_type = 'misc'
        publisher = metadata.get('publisher', '')
        
        bibtex = f"@{entry_type}{{{citation_key},\n"
        bibtex += f"  author = {{{author_string}}},\n"
        bibtex += f"  title  = {{{title}}},\n"
        bibtex += f"  year   = {{{year}}},\n"
        if publisher:
            publisher = sanitize_for_bibtex(publisher)
            bibtex += f"  publisher = {{{publisher}}},\n"
        bibtex += f"  doi    = {{{doi}}}\n}}"
    
    return {
        'bibtex': bibtex,
        'citation_key': citation_key,
        'entry_type': entry_type
    }

def save_citations(doi, apa_data, bibtex_data, output_dir="."):
    """Save APA and BibTeX citations to files"""
    # Create safe filename from DOI
    safe_doi = doi.replace('/', '_').replace('.', '_')
    
    # Save APA citation
    apa_filename = os.path.join(output_dir, f"{safe_doi}_apa7.txt")
    with open(apa_filename, 'w', encoding='utf-8') as f:
        f.write(f"APA 7th Edition Citation:\n")
        f.write(f"{'-' * 70}\n\n")
        f.write(apa_data['citation'])
        f.write(f"\n\n{'-' * 70}\n")
        f.write(f"DOI: {doi}\n")
        f.write(f"Type: {apa_data['type']}\n")
        f.write(f"Authors: {', '.join(apa_data['authors'])}\n")
        f.write(f"Year: {apa_data['year']}\n")
        f.write(f"Title: {apa_data['title']}\n")
    
    # Save BibTeX citation
    bibtex_filename = os.path.join(output_dir, f"{safe_doi}.bib")
    with open(bibtex_filename, 'w', encoding='utf-8') as f:
        f.write(bibtex_data['bibtex'])
    
    return apa_filename, bibtex_filename

def main():
    if len(sys.argv) < 2:
        print("Usage: python citation_lookup.py [bib.doi ==] <doi>")
        print("\nExamples:")
        print("  python citation_lookup.py bib.doi == 10.1038/s41586-025-09663-y")
        print("  python citation_lookup.py bib.doi == https://doi.org/10.1038/s41586-025-09663-y")
        print("  python citation_lookup.py 10.1038/s41586-025-09663-y")
        print("  python citation_lookup.py https://doi.org/10.1038/s41586-025-09663-y")
        sys.exit(1)
    
    # Parse arguments - support "bib.doi == <doi>" format
    args = sys.argv[1:]
    
    # Check for bib.doi == format
    if 'bib.doi' in args[0].lower() or '==' in ' '.join(args):
        # Extract DOI after ==
        full_arg = ' '.join(args)
        if '==' in full_arg:
            doi = full_arg.split('==')[1].strip()
        else:
            doi = args[-1]
    else:
        doi = ' '.join(args)
    
    # Clean DOI
    doi = doi.replace('https://doi.org/', '').replace('http://doi.org/', '').strip()
    
    print(f"Looking up DOI: {doi}")
    print("-" * 70)
    
    # Get metadata
    metadata = get_doi_metadata(doi)
    
    if not metadata:
        result = {'error': f'Could not retrieve metadata for DOI: {doi}'}
        print(json.dumps(result, indent=2))
        sys.exit(1)
    
    # Generate citations
    apa_citation = generate_apa7_citation(metadata, doi)
    bibtex_citation = generate_bibtex(metadata, doi)
    
    # Display results
    print("\n📄 PUBLICATION INFORMATION")
    print("=" * 70)
    print(f"Title: {metadata.get('title', ['N/A'])[0] if metadata.get('title') else 'N/A'}")
    
    if metadata.get('author'):
        authors = [f"{a.get('given', '')} {a.get('family', '')}" for a in metadata['author'][:5]]
        if len(metadata['author']) > 5:
            authors.append(f"... and {len(metadata['author']) - 5} more")
        print(f"Authors: {', '.join(authors)}")
    
    if metadata.get('container-title'):
        print(f"Published in: {metadata['container-title'][0]}")
    
    pub_date = metadata.get('published') or metadata.get('published-print')
    if pub_date and 'date-parts' in pub_date:
        print(f"Year: {pub_date['date-parts'][0][0]}")
    
    print(f"Type: {metadata.get('type', 'N/A')}")
    print(f"DOI: {doi}")
    
    print("\n\n📖 APA 7TH EDITION CITATION")
    print("=" * 70)
    print(apa_citation['citation'])
    
    print("\n\n📚 BIBTEX CITATION")
    print("=" * 70)
    print(bibtex_citation['bibtex'])
    
    # Save to files
    apa_file, bibtex_file = save_citations(
        doi,
        apa_citation,
        bibtex_citation,
        output_dir="/home/claude"
    )
    
    print("\n\n💾 FILES SAVED")
    print("=" * 70)
    print(f"APA Citation: {apa_file}")
    print(f"BibTeX Entry: {bibtex_file}")
    
    # Return JSON for programmatic use
    result = {
        'doi': doi,
        'metadata': {
            'title': metadata.get('title', [''])[0],
            'type': metadata.get('type', ''),
            'year': pub_date['date-parts'][0][0] if pub_date and 'date-parts' in pub_date else 'n.d.'
        },
        'apa7': apa_citation,
        'bibtex': bibtex_citation,
        'files': {
            'apa': apa_file,
            'bibtex': bibtex_file
        }
    }
    
    print("\n\n📋 JSON OUTPUT")
    print("=" * 70)
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()

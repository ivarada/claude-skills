#!/usr/bin/env python3
"""
Look up journal information by ISSN using the Crossref API.
Usage: python journal_lookup.py <issn>
"""
import requests
import json
import sys

def lookup_journal(issn, mailto="user@example.com"):
    """
    Look up journal information by ISSN.
    
    Args:
        issn: ISSN (print or electronic)
        mailto: Email for polite pool
    
    Returns:
        Journal metadata dictionary
    """
    # Clean ISSN (remove hyphens)
    issn = issn.replace('-', '')
    
    # Format ISSN with hyphen (XXXX-XXXX)
    if len(issn) == 8:
        issn = f"{issn[:4]}-{issn[4:]}"
    
    url = f"https://api.crossref.org/journals/{issn}"
    
    headers = {
        'User-Agent': f'CrossrefLookupSkill/1.0 (mailto:{mailto})'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        data = response.json()
        
        if data['status'] == 'ok':
            message = data['message']
            
            result = {
                'title': message.get('title'),
                'publisher': message.get('publisher'),
                'issn': message.get('ISSN', []),
                'subjects': message.get('subjects', []),
                'last_status_check_time': message.get('last-status-check-time'),
                'flags': message.get('flags', {}),
                'coverage': message.get('coverage', {}),
                'breakdowns': message.get('breakdowns', {}),
                'counts': message.get('counts', {})
            }
            
            # Additional details
            if 'counts' in message:
                result['total_dois'] = message['counts'].get('total-dois', 0)
                result['current_dois'] = message['counts'].get('current-dois', 0)
            
            return result
        else:
            return {'error': 'Journal not found'}
    
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return {'error': f'No journal found with ISSN: {issn}'}
        return {'error': str(e)}
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python journal_lookup.py <issn>")
        sys.exit(1)
    
    issn = sys.argv[1]
    result = lookup_journal(issn)
    print(json.dumps(result, indent=2))

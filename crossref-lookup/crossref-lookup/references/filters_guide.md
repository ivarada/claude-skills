# Crossref API Filters and Advanced Search Guide

This guide covers advanced filtering and search techniques for the Crossref API.

## Filter Syntax

Filters use the format: `filter=key:value,key:value`

Multiple filters are combined with commas (AND logic).

## Date Filters

### Publication Date Filters

**From date (on or after):**
```
from-pub-date:YYYY-MM-DD
from-pub-date:YYYY-MM
from-pub-date:YYYY
```

**Until date (on or before):**
```
until-pub-date:YYYY-MM-DD
until-pub-date:YYYY-MM
until-pub-date:YYYY
```

**Examples:**
```bash
# Papers from 2020 onwards
filter=from-pub-date:2020

# Papers between 2018 and 2022
filter=from-pub-date:2018,until-pub-date:2022

# Papers from specific month
filter=from-pub-date:2020-06,until-pub-date:2020-06
```

### Online Publication Date
```
from-online-pub-date:YYYY-MM-DD
until-online-pub-date:YYYY-MM-DD
```

### Print Publication Date
```
from-print-pub-date:YYYY-MM-DD
until-print-pub-date:YYYY-MM-DD
```

### Indexed Date
```
from-index-date:YYYY-MM-DD
until-index-date:YYYY-MM-DD
```

### Created/Updated Dates
```
from-created-date:YYYY-MM-DD
until-created-date:YYYY-MM-DD
from-update-date:YYYY-MM-DD
until-update-date:YYYY-MM-DD
```

## Type Filters

### By Publication Type

```
type:journal-article
type:book
type:book-chapter
type:proceedings-article
type:report
type:dataset
type:posted-content
```

**Example:**
```bash
# Only journal articles
filter=type:journal-article

# Only books and book chapters
filter=type:book
# (separate query for book-chapter)
```

### Common Type Values

| Type | Description |
|------|-------------|
| `journal-article` | Standard journal article |
| `book` | Complete book |
| `book-chapter` | Chapter in a book |
| `proceedings-article` | Conference paper |
| `report` | Technical report |
| `dataset` | Research dataset |
| `posted-content` | Preprints, working papers |
| `dissertation` | PhD thesis |
| `monograph` | Scholarly monograph |

## Content Availability Filters

### Has Content
```
has-abstract:true          # Has an abstract
has-full-text:true         # Has full text
has-references:true        # Has reference list
has-orcid:true            # Author has ORCID
has-authenticated-orcid:true  # Verified ORCID
has-funder:true           # Has funding info
has-license:true          # Has license info
has-clinical-trial-number:true  # Has clinical trial
has-affiliation:true      # Has author affiliations
has-update:true           # Has been updated
has-ror-id:true          # Has ROR identifier
```

**Examples:**
```bash
# Papers with abstracts and references
filter=has-abstract:true,has-references:true

# Papers with ORCID and affiliations
filter=has-orcid:true,has-affiliation:true

# Open access with full text
filter=has-full-text:true,has-license:true
```

## Organization Filters

### By Publisher/Member
```
member:{member_id}
```

**Example:**
```bash
# Papers from Springer Nature (member ID: 297)
filter=member:297
```

### By Journal (ISSN)
```
issn:{issn}
```

**Example:**
```bash
# Papers from Nature (ISSN: 0028-0836)
filter=issn:0028-0836
```

### By Funder
```
funder:{funder_id}
```

**Example:**
```bash
# NSF funded research (funder DOI: 10.13039/100000001)
filter=funder:10.13039/100000001
```

### By ISBN
```
isbn:{isbn}
```

## License Filters

### Has License
```
has-license:true
```

### License URL
```
license.url:{url}
```

**Example:**
```bash
# Creative Commons BY license
filter=license.url:http://creativecommons.org/licenses/by/4.0/
```

### License Version
```
license.version:{version}
```

### License Delay
```
license.delay:{days}
```

## Relation Filters

### Relation Type
```
relation.type:is-preprint-of
relation.type:has-preprint
relation.type:is-version-of
relation.type:has-version
relation.type:is-review-of
```

### Relation Object Type
```
relation.object-type:work
relation.object-type:journal
```

**Example:**
```bash
# Find preprints
filter=relation.type:is-preprint-of
```

## Update Filters

### Update Type
```
update-type:correction
update-type:retraction
update-type:withdrawal
update-type:addendum
```

### Has Update
```
has-update:true
```

**Example:**
```bash
# Find retracted papers
filter=update-type:retraction
```

## Directory Filters

### Directory of Open Access Journals (DOAJ)
```
directory:doaj
```

**Example:**
```bash
# Only DOAJ indexed journals
filter=directory:doaj
```

## Advanced Query Parameters

### Field-Specific Queries

Instead of general `query`, use field-specific parameters:

```
query.title={text}           # Search in titles only
query.author={text}          # Search in author names
query.bibliographic={text}   # Search all bibliographic fields
query.affiliation={text}     # Search affiliations
query.container-title={text} # Search journal/book names
```

**Examples:**
```bash
# Search only in titles
/works?query.title=machine+learning

# Search only by author
/works?query.author=Einstein

# Search in journal names
/works?query.container-title=Nature
```

## Complex Filter Combinations

### Example 1: Recent Open Access ML Papers
```bash
/works?query=machine+learning&filter=from-pub-date:2022,type:journal-article,has-full-text:true,has-license:true&rows=20
```

### Example 2: NSF-Funded Climate Research
```bash
/works?query=climate+change&filter=funder:10.13039/100000001,has-abstract:true,from-pub-date:2020&rows=50
```

### Example 3: Conference Papers with ORCIDs
```bash
/works?query.author=smith&filter=type:proceedings-article,has-orcid:true,from-pub-date:2019&rows=10
```

### Example 4: Recent Books from Specific Publisher
```bash
/works?filter=type:book,member:297,from-pub-date:2021&rows=20
```

### Example 5: Nature Papers with References
```bash
/works?filter=issn:0028-0836,has-references:true,from-pub-date:2020&rows=30
```

## Sorting Results

### Sort Parameters

```
sort=score               # Relevance (default for searches)
sort=published           # Publication date
sort=indexed             # Date indexed by Crossref
sort=is-referenced-by-count  # Citation count
sort=created             # Date record created
sort=updated             # Date record updated
```

### Order

```
order=desc  # Descending (default)
order=asc   # Ascending
```

**Examples:**
```bash
# Most cited papers first
/works?query=neural+networks&sort=is-referenced-by-count&order=desc

# Newest papers first
/works?query=covid&sort=published&order=desc

# Oldest papers first
/works?query=darwin&sort=published&order=asc
```

## Pagination

### Parameters
```
rows={n}      # Number of results (max: 1000)
offset={n}    # Starting position
```

**Example:**
```bash
# Page 1 (results 0-19)
/works?query=test&rows=20&offset=0

# Page 2 (results 20-39)
/works?query=test&rows=20&offset=20

# Page 3 (results 40-59)
/works?query=test&rows=20&offset=40
```

### Deep Pagination Warning

- Maximum offset: ~10,000
- For deep pagination, use cursor (not yet available)
- Consider narrowing your search instead

## Faceting

### Sample Parameter

Get a sample of results for faceting:

```
sample={n}  # Random sample of N results
```

**Example:**
```bash
/works?query=biology&sample=100
```

## Performance Tips

### 1. Use Specific Filters
```bash
# Slow: broad search
/works?query=cancer

# Fast: narrow with filters
/works?query=cancer&filter=type:journal-article,from-pub-date:2020,has-abstract:true
```

### 2. Reduce Result Size
```bash
# Request fewer results
/works?query=test&rows=10

# Better than
/works?query=test&rows=1000
```

### 3. Use Field-Specific Queries
```bash
# More efficient
/works?query.title=machine+learning

# Than
/works?query=machine+learning
```

### 4. Cache Results
- Store results locally
- Don't repeatedly query the same DOI
- Use appropriate cache TTL (time to live)

## Examples by Use Case

### Use Case 1: Literature Review - Recent Papers in Field

```bash
/works?query.title=deep+learning&filter=type:journal-article,from-pub-date:2020,has-abstract:true&sort=is-referenced-by-count&order=desc&rows=50
```

### Use Case 2: Finding Author's Publications

```bash
/works?query.author=jane+smith&filter=has-orcid:true&sort=published&order=desc&rows=100
```

### Use Case 3: Open Access Papers on Topic

```bash
/works?query=quantum+computing&filter=has-license:true,has-full-text:true,from-pub-date:2021&rows=30
```

### Use Case 4: Conference Proceedings Search

```bash
/works?query=CVPR+2022&filter=type:proceedings-article,from-pub-date:2022,until-pub-date:2022&rows=100
```

### Use Case 5: Finding Preprints

```bash
/works?query=coronavirus&filter=type:posted-content,from-online-pub-date:2020&rows=50
```

### Use Case 6: Highly Cited Papers

```bash
/works?query.bibliographic=climate+change&filter=from-pub-date:2015,until-pub-date:2020&sort=is-referenced-by-count&order=desc&rows=100
```

## Troubleshooting

### No Results

**Check:**
1. Filter syntax is correct
2. Date formats are YYYY-MM-DD (or YYYY-MM or YYYY)
3. Type values match Crossref types exactly
4. Combine filters appropriately

### Too Many Results

**Solutions:**
1. Add more specific filters
2. Narrow date range
3. Use field-specific queries
4. Increase sort relevance

### Slow Performance

**Solutions:**
1. Reduce rows parameter
2. Use more specific filters
3. Cache results
4. Use polite pool (include mailto)

## Best Practices

1. **Start broad, then narrow**: Begin with simple queries, add filters as needed
2. **Use appropriate row counts**: Don't request more than you need
3. **Combine filters wisely**: More filters = more precise = faster
4. **Cache aggressively**: Same queries shouldn't hit API repeatedly
5. **Use polite pool**: Always include your email in User-Agent
6. **Check field availability**: Not all works have all fields
7. **Test filters**: Verify filters work before bulk operations

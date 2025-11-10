# Crossref API Response Schemas

## Work (Publication) Response

### Journal Article Example

```json
{
  "DOI": "10.1038/nature12373",
  "type": "journal-article",
  "title": ["The genome of the Western clawed frog Xenopus tropicalis"],
  "author": [
    {
      "given": "Uffe",
      "family": "Hellsten",
      "sequence": "first",
      "affiliation": [
        {
          "name": "US Department of Energy Joint Genome Institute"
        }
      ]
    }
  ],
  "container-title": ["Nature"],
  "volume": "496",
  "issue": "7446",
  "page": "311-316",
  "published": {
    "date-parts": [[2013, 4, 30]]
  },
  "publisher": "Springer Science and Business Media LLC",
  "ISSN": ["0028-0836", "1476-4687"],
  "URL": "http://dx.doi.org/10.1038/nature12373",
  "abstract": "<p>Abstract text here...</p>",
  "references-count": 92,
  "is-referenced-by-count": 247,
  "subject": ["Multidisciplinary"],
  "license": [
    {
      "URL": "http://www.springer.com/tdm",
      "start": {
        "date-parts": [[2013, 4, 30]],
        "timestamp": 1367280000000
      },
      "content-version": "tdm"
    }
  ]
}
```

### Book Example

```json
{
  "DOI": "10.1007/978-3-319-24277-4",
  "type": "book",
  "title": ["Machine Learning: A Probabilistic Perspective"],
  "author": [
    {
      "given": "Kevin P.",
      "family": "Murphy",
      "sequence": "first"
    }
  ],
  "publisher": "Springer",
  "ISBN": ["978-3-319-24276-7", "978-3-319-24277-4"],
  "published": {
    "date-parts": [[2012]]
  },
  "URL": "http://dx.doi.org/10.1007/978-3-319-24277-4"
}
```

### Conference Paper Example

```json
{
  "DOI": "10.1145/3025453.3025922",
  "type": "proceedings-article",
  "title": ["Neural Machine Translation by Jointly Learning to Align and Translate"],
  "author": [
    {
      "given": "Dzmitry",
      "family": "Bahdanau",
      "sequence": "first"
    },
    {
      "given": "Kyunghyun",
      "family": "Cho",
      "sequence": "additional"
    },
    {
      "given": "Yoshua",
      "family": "Bengio",
      "sequence": "additional"
    }
  ],
  "container-title": ["Proceedings of the 2017 CHI Conference"],
  "published": {
    "date-parts": [[2017, 5]]
  },
  "publisher": "ACM",
  "page": "1234-1245",
  "URL": "http://dx.doi.org/10.1145/3025453.3025922"
}
```

## Search Response

### Works Search Example

```json
{
  "status": "ok",
  "message-type": "work-list",
  "message-version": "1.0.0",
  "message": {
    "total-results": 47823,
    "items": [
      {
        "DOI": "10.1234/example.doi",
        "title": ["Example Paper Title"],
        "author": [
          {
            "given": "John",
            "family": "Doe"
          }
        ],
        "type": "journal-article",
        "container-title": ["Journal Name"],
        "volume": "10",
        "issue": "2",
        "published": {
          "date-parts": [[2020, 3, 15]]
        },
        "score": 42.5
      }
    ],
    "items-per-page": 20,
    "query": {
      "start-index": 0,
      "search-terms": "machine learning"
    }
  }
}
```

## Journal Response

### Journal Metadata Example

```json
{
  "status": "ok",
  "message-type": "journal",
  "message": {
    "title": "Nature",
    "publisher": "Springer Nature",
    "ISSN": ["0028-0836", "1476-4687"],
    "subjects": [
      {
        "name": "Multidisciplinary",
        "ASJC": "1000"
      }
    ],
    "last-status-check-time": 1636502400000,
    "flags": {
      "deposits-abstracts-current": true,
      "deposits-orcids-current": true,
      "deposits": true
    },
    "coverage": {
      "affiliations-current": 0.95,
      "references-count": 142357,
      "references-count-backfile": 8234
    },
    "counts": {
      "total-dois": 250000,
      "current-dois": 150000
    }
  }
}
```

## Author Object Structure

```json
{
  "given": "Marie",
  "family": "Curie",
  "sequence": "first",
  "ORCID": "http://orcid.org/0000-0001-2345-6789",
  "authenticated-orcid": true,
  "affiliation": [
    {
      "name": "University of Paris",
      "place": ["Paris, France"]
    }
  ]
}
```

### Author Sequence Values
- `first`: First author
- `additional`: Additional authors
- Authors are in order as they appear in publication

## Date Object Structure

```json
{
  "date-parts": [[2020, 3, 15]],
  "timestamp": 1584230400000
}
```

### Date Fields
- `date-parts`: Array of [year, month, day]
- `timestamp`: Unix timestamp in milliseconds
- Month and day may be missing: `[[2020]]` or `[[2020, 3]]`

## Publication Types

Common type values:

- `journal-article`: Standard journal article
- `book`: Complete book
- `book-chapter`: Chapter in a book
- `book-section`: Section of a book
- `monograph`: Scholarly monograph
- `proceedings-article`: Conference paper
- `paper-conference`: Conference paper (alternate)
- `report`: Technical report
- `dataset`: Research dataset
- `posted-content`: Preprint or working paper
- `dissertation`: PhD thesis
- `edited-book`: Edited volume
- `reference-book`: Reference work
- `journal`: Journal (for journal metadata)
- `component`: Component (figures, tables, etc.)

## License Object

```json
{
  "URL": "https://creativecommons.org/licenses/by/4.0/",
  "start": {
    "date-parts": [[2020, 1, 1]],
    "timestamp": 1577836800000
  },
  "content-version": "vor",
  "delay-in-days": 0
}
```

### Content Version Values
- `vor`: Version of Record
- `am`: Accepted Manuscript
- `tdm`: Text and Data Mining
- `unspecified`

## Funder Object

```json
{
  "name": "National Science Foundation",
  "DOI": "10.13039/100000001",
  "award": ["1234567", "7654321"]
}
```

## Reference Object

```json
{
  "key": "ref1",
  "doi-asserted-by": "crossref",
  "DOI": "10.1234/referenced.work",
  "article-title": "Referenced Article Title",
  "author": "Smith",
  "year": "2019",
  "journal-title": "Journal Name",
  "volume": "15",
  "first-page": "123"
}
```

## Clinical Trial Object

```json
{
  "clinical-trial-number": "NCT01234567",
  "registry": "ClinicalTrials.gov",
  "type": "preResults"
}
```

## Relation Object

```json
{
  "id-type": "doi",
  "id": "10.1234/related.work",
  "asserted-by": "publisher"
}
```

### Relation Types
- `is-preprint-of`: This is a preprint of
- `has-preprint`: Has a preprint
- `is-version-of`: Is a version of
- `has-version`: Has versions
- `is-review-of`: Reviews this work
- `has-review`: Has reviews
- `is-supplement-to`: Supplements this work
- `is-supplemented-by`: Is supplemented by

## Affiliation Object

```json
{
  "name": "Massachusetts Institute of Technology",
  "place": ["Cambridge", "MA", "USA"],
  "department": ["Department of Computer Science"],
  "acronym": ["MIT"]
}
```

## Error Response

```json
{
  "status": "failed",
  "message-type": "work",
  "message-version": "1.0.0",
  "message": {
    "error": "Resource not found"
  }
}
```

## Field Availability

Not all fields are available for all works. Common missing fields:

- `abstract`: ~30% of works have abstracts
- `references`: ~70% of works have reference data
- `ORCID`: ~25% of authors have ORCIDs
- `affiliation`: ~40% of authors have affiliation data
- `license`: ~50% of works have license information
- `funder`: ~35% of works have funding information

Always check if fields exist before using them in your code!

# OpenLibrary API Response Schemas

## Search Response

```json
{
  "numFound": 629,
  "start": 0,
  "numFoundExact": true,
  "docs": [
    {
      "key": "/works/OL45804W",
      "title": "Fantastic Mr Fox",
      "author_name": ["Roald Dahl"],
      "author_key": ["OL34184A"],
      "first_publish_year": 1970,
      "isbn": ["0141365439", "9780141365435"],
      "publisher": ["Puffin"],
      "number_of_pages_median": 96,
      "cover_i": 8739161,
      "edition_count": 50,
      "language": ["eng"],
      "subject": ["Children's fiction", "Foxes"]
    }
  ]
}
```

## Book/Edition Response

```json
{
  "publishers": ["Puffin"],
  "number_of_pages": 96,
  "isbn_10": ["0141365439"],
  "isbn_13": ["9780141365435"],
  "covers": [8739161],
  "key": "/books/OL7353617M",
  "authors": [
    {
      "key": "/authors/OL34184A"
    }
  ],
  "title": "Fantastic Mr Fox",
  "publish_date": "2016",
  "works": [
    {
      "key": "/works/OL45804W"
    }
  ]
}
```

## Author Response

```json
{
  "name": "Roald Dahl",
  "bio": "Roald Dahl was a British novelist...",
  "birth_date": "13 September 1916",
  "death_date": "23 November 1990",
  "key": "/authors/OL34184A",
  "photos": [6287214],
  "links": [
    {
      "title": "Wikipedia",
      "url": "https://en.wikipedia.org/wiki/Roald_Dahl"
    }
  ]
}
```

## Work Response

```json
{
  "title": "Fantastic Mr Fox",
  "key": "/works/OL45804W",
  "authors": [
    {
      "author": {
        "key": "/authors/OL34184A"
      },
      "type": {
        "key": "/type/author_role"
      }
    }
  ],
  "description": "The main character of Fantastic Mr. Fox is an extremely clever...",
  "covers": [8739161],
  "subjects": ["Children's fiction", "Foxes"],
  "first_publish_date": "1970"
}
```

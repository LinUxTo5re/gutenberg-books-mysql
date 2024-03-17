# gutenberg book library

## Description

A Django web application for searching and filtering books from Project Gutenberg's extensive collection of free eBooks.

## Swagger Documentation

Access the Swagger API documentation by navigating to:

- http://127.0.0.1:8000/swagger

Alternatively, you can manually interact with the API by visiting:

- http://127.0.0.1:8000

## Manual Endpoint Access

Alternatively, you can manually hit the API endpoints by sending HTTP requests to the respective URLs.

- http://127.0.0.1:8000/gb-data/data/?bookshelf=6

- http://127.0.0.1:8000/gb-data/data/

- http://127.0.0.1:8000/gb-data/data/    ===> followed by querystring

### Note - 
- *Download_links are not added in json, having issue while extracting. will fix asap.*

- ## Fixed:
       *some of swagger parameters are not working but you can check those manually hitting endpoint with querystring, will fix asap.*


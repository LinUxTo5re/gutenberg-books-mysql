# gutenberg book library

## Description

A Django web application for searching and filtering books from Project Gutenberg's extensive collection of free eBooks.

## Set Up
- ``` git clone https://github.com/LinUxTo5re/gutenberg-books-mysql.git ```

- ``` cd gutenberg-books-mysql ```

- ``` pip install -r requirements.txt ```

before proceeding with next steps, unzip gutendex.sql.zip and follow steps (Mysql Script):
- create new user: gutenberg 

- password for new user: gutenberg

- create database: db_gutenberg

after this continue with  following steps to run Django server:
- ```python3 manage.py makemigrations```

- ```python3 manage.py migrate```

- ```python3 manage.py runserver ``` (run the server)

## Swagger Documentation

Access the Swagger API documentation by navigating to:

- http://127.0.0.1:8000/swagger

Alternatively, you can manually interact with the API by visiting:

- http://127.0.0.1:8000

## Manual Endpoint Access

Alternatively, you can manually hit the API endpoints by sending HTTP requests to the respective URLs.

- http://127.0.0.1:8000/gb-data/data/?bookshelf=6

- http://127.0.0.1:8000/gb-data/data/

- http://127.0.0.1:8000/gb-data/data/?id=23&id=85&bookshelf=4&language=en&language=de 
  
(use as much as possible parameters in querystring in last one API call)

## Connect with me

- [LinkedIn](https://www.linkedin.com/in/chaitanya-ajabe-99a449221/)

# *Enjoy the code*


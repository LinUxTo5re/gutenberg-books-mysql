from rest_framework import serializers
from .models import *

class BooksAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksAuthor
        fields = ['id', 'birth_year','death_year','name']

class BooksBookSerializer(serializers.ModelSerializer):
    # booksauthor = BooksAuthorSerializer()  
    class Meta:
        model = BooksBook
        fields = ['id', 'download_count', 'gutenberg_id', 'media_type', 'title']

class BooksBookAuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksBookAuthors
        fields = ['id', 'book_id', 'author_id']

class BooksBookBookshelvesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksBookBookshelves
        fields = ['id', 'book_id', 'bookshelf_id']

class BooksBookLanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksBookLanguages
        fields = ['id', 'book_id', 'language_id']

class BooksBookSubjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksBookSubjects
        fields = ['id', 'book_id', 'subject_id']

class BooksBookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksBookshelf
        fields = ['id', 'name']

class BooksFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksFormat
        fields = ['id', 'mime_type', 'url', 'book_id']

class BooksLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksLanguage
        fields = ['id', 'code']

class BooksSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksSubject
        fields = ['id', 'name']


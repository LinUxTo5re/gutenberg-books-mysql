from django.db import models


class BooksAuthor(models.Model):
    id = models.IntegerField(primary_key=True)
    birth_year = models.SmallIntegerField(blank=True, null=True)
    death_year = models.SmallIntegerField(blank=True, null=True)
    name = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'books_author'


class BooksBook(models.Model):
    id = models.IntegerField(primary_key=True)
    download_count = models.IntegerField(blank=True, null=True)
    gutenberg_id = models.IntegerField()
    media_type = models.CharField(max_length=16)
    title = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'books_book'


class BooksBookAuthors(models.Model):
    id = models.IntegerField(primary_key=True)
    book_id = models.IntegerField()
    author_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'books_book_authors'


class BooksBookBookshelves(models.Model):
    id = models.IntegerField(primary_key=True)
    book_id = models.IntegerField()
    bookshelf_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'books_book_bookshelves'


class BooksBookLanguages(models.Model):
    id = models.IntegerField(primary_key=True)
    book_id = models.IntegerField()
    language_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'books_book_languages'


class BooksBookSubjects(models.Model):
    id = models.IntegerField(primary_key=True)
    book_id = models.IntegerField()
    subject_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'books_book_subjects'


class BooksBookshelf(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'books_bookshelf'


class BooksFormat(models.Model):
    id = models.IntegerField(primary_key=True)
    mime_type = models.CharField(max_length=32)
    url = models.TextField()
    book_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'books_format'


class BooksLanguage(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'books_language'


class BooksSubject(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()

    class Meta:
        managed = False
        db_table = 'books_subject'

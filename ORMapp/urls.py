from django.urls import path
from .views import *

urlpatterns = [
    path('authors/', BooksAuthorListView.as_view(), name='authors-list'),
    path('books/', BooksBookListView.as_view(), name='books-list'),
    path('book-authors/', BooksBookAuthorsListView.as_view(), name='book-authors-list'),
    path('book-bookshelves/', BooksBookBookshelvesListView.as_view(), name='book-bookshelves-list'),
    path('book-languages/', BooksBookLanguagesListView.as_view(), name='book-languages-list'),
    path('book-subjects/', BooksBookSubjectsListView.as_view(), name='book-subjects-list'),
    path('bookshelves/', BooksBookshelfListView.as_view(), name='bookshelves-list'),
    path('formats/', BooksFormatListView.as_view(), name='formats-list'),
    path('languages/', BooksLanguageListView.as_view(), name='languages-list'),
    path('subjects/', BooksSubjectListView.as_view(), name='subjects-list'),
]
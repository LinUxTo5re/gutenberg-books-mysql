from django.test import TestCase, Client
from django.urls import reverse
from .models import BooksLanguage, BooksBook, BooksSubject, BooksBookshelf, BooksAuthor

class TestGutenbergDataListView(TestCase):
    def test_gutenberg_data_list_view_with_invalid_language(self):
        client = Client()
        url = reverse('gb-list')
        response = client.get(url, {'language': ['en','fr']})
        self.assertEqual(response.status_code, 200)


    def test_gutenberg_data_list_view_with_multiple_valid_ids(self):
        client = Client()
        url = reverse('gb-list')

        response = client.get(url, {'id': [1, 2]})
        self.assertEqual(response.status_code, 200)

    def test_gutenberg_data_list_view_with_invalid_bookshelf(self):
        client = Client()
        url = reverse('gb-list')

        response = client.get(url, {'bookshelf': [23,53,2]})
        self.assertEqual(response.status_code, 200)

from django.test import TestCase, Client
from django.urls import reverse
from .models import BooksLanguage, BooksBook, BooksSubject, BooksBookshelf, BooksAuthor

class TestGutenbergDataListView(TestCase):
    def setUp(self):
        self.book1 = BooksBook.objects.create(gutenberg_id=1, media_type='text', title='Book 1')
        self.book2 = BooksBook.objects.create(gutenberg_id=2, media_type='text', title='Book 2')
        self.book3 = BooksBook.objects.create(gutenberg_id=3, media_type='text', title='Book 3')

    def test_gutenberg_data_list_view_with_valid_parameters(self):
        client = Client()
        url = reverse('gb-list')

        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_gutenberg_data_list_view_with_invalid_language(self):
        client = Client()
        url = reverse('gb-list')

        response = client.get(url, {'language': 'invalid_lang'})
        self.assertEqual(response.status_code, 200)

    def test_gutenberg_data_list_view_with_invalid_page(self):
        client = Client()
        url = reverse('gb-list')

        response = client.get(url, {'page': 'abc'})
        self.assertEqual(response.status_code, 200)

    def test_gutenberg_data_list_view_with_multiple_valid_ids(self):
        client = Client()
        url = reverse('gb-list')

        response = client.get(url, {'id': [1, 2]})
        self.assertEqual(response.status_code, 200)

    def test_gutenberg_data_list_view_with_valid_author(self):
        client = Client()
        url = reverse('gb-list')

        response = client.get(url, {'author': 'Author Name'})
        self.assertEqual(response.status_code, 200)

    def test_gutenberg_data_list_view_with_valid_title(self):
        client = Client()
        url = reverse('gb-list')

        response = client.get(url, {'title': 'Book Title'})
        self.assertEqual(response.status_code, 200)

    def test_gutenberg_data_list_view_with_invalid_bookshelf(self):
        client = Client()
        url = reverse('gb-list')

        response = client.get(url, {'bookshelf': 'invalid_bookshelf'})
        self.assertEqual(response.status_code, 200)

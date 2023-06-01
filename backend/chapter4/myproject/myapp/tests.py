from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Book
from .serializers import BookSerializer


class BookTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book_data = {
            'title': 'Test Book',
            'author': 'John Doe',
            'publication_date': '2023-01-01',
            'price': '9.99',  # Updated to a string value
        }
        self.book = Book.objects.create(**self.book_data)

    def test_get_all_books(self):
        response = self.client.get('/myapp/books/')
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'], serializer.data)  # Check 'results' key

    def test_get_single_book(self):
        response = self.client.get(f'/myapp/books/{self.book.id}/')
        book = Book.objects.get(id=self.book.id)
        serializer = BookSerializer(book)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_book(self):
        response = self.client.post('/myapp/create/', data=self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        updated_data = {
            'title': 'Updated Book',
            'author': 'Jane Smith',
            'publication_date': '2023-02-01',
            'price': '19.99',  # Updated to a string value
        }
        response = self.client.put(f'/myapp/books/{self.book.id}/', data=updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_book = Book.objects.get(id=self.book.id)
        self.assertEqual(updated_book.title, updated_data['title'])
        self.assertEqual(updated_book.author, updated_data['author'])
        self.assertEqual(updated_book.publication_date.strftime('%Y-%m-%d'), updated_data['publication_date'])
        self.assertEqual(str(updated_book.price), updated_data['price'])  # Convert Decimal to string

    def test_delete_book(self):
        response = self.client.delete(f'/myapp/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

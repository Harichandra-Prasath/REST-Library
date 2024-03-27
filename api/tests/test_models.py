from django.test import TestCase
from ..models import Book
from django.db import IntegrityError


class BookTestCase(TestCase):
    
    def setUp(self) -> None:
        book = Book(
            Title="Test",
            Author="Tester",
            ISBN="1234567890123"
        )
        book.save()

    def test_retrieve_book(self):
        _book = Book.objects.get(ISBN="1234567890123")        
        self.assertEqual(_book.Title,"Test")
        self.assertEqual(_book.Author,"Tester")
        
    
    def test_unique(self):
        bad_book = Book(
            Title="Test1",
            Author="Tester",
            ISBN="1234567890123"
        )
        with self.assertRaises(IntegrityError):
            bad_book.save()
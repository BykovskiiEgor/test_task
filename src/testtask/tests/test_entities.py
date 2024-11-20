import unittest
from domain.entities import Book

class TestBook(unittest.TestCase):
    def test_book_creation(self):
        book = Book(id=1, title="1984", author="George Orwell", year=1949, status="в наличии")
        self.assertEqual(book.id, 1)
        self.assertEqual(book.title, "1984")
        self.assertEqual(book.author, "George Orwell")
        self.assertEqual(book.year, 1949)
        self.assertEqual(book.status, "в наличии")

if __name__ == "__main__":
    unittest.main()
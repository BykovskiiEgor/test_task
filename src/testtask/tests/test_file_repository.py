import unittest
import os
from adapters.file_repository import FileBookRepository
from domain.entities import Book

class TestFileBookRepository(unittest.TestCase):
    TEST_FILE = "test_books.json"

    def setUp(self):
        self.repo = FileBookRepository(self.TEST_FILE)
        self.repo.clear() 

    def tearDown(self):
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

    def test_add_book(self):
        book = Book(id=1, title="test", author="test", year=1111, status="в наличии")
        self.repo.save(book)
        books = self.repo.get_all()
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "test")

    def test_delete_book(self):
        book = Book(id=1, title="test", author="test", year=1111, status="в наличии")
        self.repo.save(book)
        self.repo.delete(1)
        self.assertEqual(len(self.repo.get_all()), 0)

    def test_search_books(self):
        book1 = Book(id=1, title="test", author="test", year=1111, status="в наличии")
        book2 = Book(id=2, title="test2", author="test2", year=2222, status="в наличии")
        self.repo.save(book1)
        self.repo.save(book2)

        result = self.repo.search("test", "title")
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].title, "test")

if __name__ == "__main__":
    unittest.main()

import json
from typing import List, Optional
from domain.entities import Book
from domain.interfaces import BookRepository

class FileBookRepository(BookRepository):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def _load_data(self) -> List[Book]:
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                return [Book(**item) for item in data]
        except FileNotFoundError:
            return []

    def _save_data(self, books: List[Book]) -> None:
        with open(self.file_path, 'w') as f:
            json.dump([book.__dict__ for book in books], f, indent=4)

    def get_all(self) -> List[Book]:
        return self._load_data()

    def save(self, book: Book) -> None:
        books = self._load_data()
        books = [b for b in books if b.id != book.id] + [book]
        self._save_data(books)

    def delete(self, book_id: int) -> bool:
        books = self._load_data()
        updated_books = [book for book in books if book.id != book_id]
        if len(updated_books) < len(books):
            self._save_data(updated_books)
            return True
        return False

    def find_by_id(self, book_id: int) -> Optional[Book]:
        books = self._load_data()
        for book in books:
            if book.id == book_id:
                return book
        return None

    def search(self, query: str, field: str) -> List[Book]:
        books = self._load_data()
        return [book for book in books if query.lower() in str(getattr(book, field, "")).lower()]
    
    
    def clear(self):       
        with open(self.file_path, 'w') as file:
            json.dump([], file)

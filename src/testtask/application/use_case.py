from typing import List, Optional
from domain.interfaces import BookRepository
from domain.entities import Book
from .dto import BookDTO

class AddBook:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self, title: str, author: str, year: int) -> BookDTO:
        books = self.repository.get_all()
        new_book = Book(id=len(books) + 1, title=title, author=author, year=year)
        self.repository.save(new_book)
        return BookDTO(**new_book.__dict__)

class DeleteBook:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self, book_id: int) -> bool:
        return self.repository.delete(book_id)

class SearchBook:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self, query: str, field: str) -> List[BookDTO]:
        books = self.repository.search(query, field)
        return [BookDTO(**book.__dict__) for book in books]

class DisplayBooks:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self) -> List[BookDTO]:
        books = self.repository.get_all()
        return [BookDTO(**book.__dict__) for book in books]

class UpdateStatus:
    def __init__(self, repository: BookRepository):
        self.repository = repository

    def execute(self, book_id: int, status: str) -> Optional[BookDTO]:
        book = self.repository.find_by_id(book_id)
        if book:
            book.status = status
            self.repository.save(book)
            return BookDTO(**book.__dict__)
        return None

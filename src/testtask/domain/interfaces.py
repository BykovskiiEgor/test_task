from abc import ABC, abstractmethod
from typing import List, Optional
from .entities import Book

class BookRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Book]:
        pass
    
    @abstractmethod
    def find_by_id(self, book_id: int) -> Optional[Book]:
        pass
    
    @abstractmethod
    def save(self, book: Book) -> None:
        pass
    
    @abstractmethod
    def delete(self, book_id: int) -> bool:
        pass
    
    @abstractmethod
    def search(self, query: str, field: str) -> List[Book]:
        pass

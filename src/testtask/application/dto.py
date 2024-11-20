from dataclasses import dataclass

@dataclass
class BookDTO:
    id: int
    title: str
    author: str
    year: int
    status: str
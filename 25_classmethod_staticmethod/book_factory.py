from __future__ import annotations

class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight) -> None:
        self.name = name
        self.book_type = book_type
        self.weight = weight
    
    def __repr__(self) -> str:
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    @classmethod
    def hardcover(cls, name: str, page_weight: int) -> Book:
        # return Book(name, Book.TYPES[0], page_weight + 100)
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name: str, page_weight: int) -> Book:
        return cls(name, cls.TYPES[1], page_weight)

print(Book.TYPES)
book = Book("System Design", "hardcover", 500)
print(book.name)
print(book)

book2 = Book.hardcover("Game Development with python", 200)
print(book2)

book3 = Book.paperback("Game Development with python", 200)
print(book3)
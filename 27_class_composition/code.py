# Description: 27 - Class Composition
# Composition represents HAS-A relationship
# This is more common than inheritance and allows your class to be simpler
# and reduce complexity of your code
from typing import Tuple

class Bookshelf:
    def __init__(self, *books: "Book"):
        self.books = books
    
    def __str__(self) -> str:
        return f"Bookshelf with {len(self.books)} books."

class Book:
    def __init__(self, name: str):
        self.name = name
    
    def __str__(self) -> str:
        return f"Book {self.name}"

book = Book("System Design")
book2 = Book("Game Development with python")
shelf = Bookshelf(book, book2)

print(shelf)
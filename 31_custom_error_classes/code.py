# Description: Custom error classes
# To implement a custom error class, we need to inherit from the Exception class.

class TooManyPagesReadError(ValueError): # inherits from ValueError
    pass

class Book:
    def __init__(self, name: str, page_count: int) -> None:
        self.name = name
        self.page_count = page_count
        self.pages_read = 0
    
    def __repr__(self):
        return (
            f"<Book {self.name}, read {self.pages_read} pages out of {self.page_count}>"
        )
    
    def read(self, pages: int):
        if self.pages_read + pages > self.page_count:
            raise TooManyPagesReadError(
                f"You tried to read {self.pages_read + pages} pages, but this book only has {self.page_count} pages."
            )
        
        self.pages_read += pages
        print(f"You have now read {self.pages_read} pages of of {self.page_count}.")

python101 = Book("Python Introduction", 200)
python101.read(135)
python101.read(100)

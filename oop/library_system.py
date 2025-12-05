class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"
    
class EBook(Book):
    def __init__(self, file_size):
        super().__init__(title=None, author=None)
        self.file_size = file_size  # in MB

class PrintBook(Book):
    def __init__(self, page_count):
        super().__init__(title = None, author = None)
        self.page_count = page_count  # in grams


class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only Book instances can be added to the library.")
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else: 
            print("Books in the library:")
            for book in self.books:
                print(book)
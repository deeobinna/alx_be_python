class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"
    
class EBook(Book):
    def __init__(self, file_size, title, author):
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}MB"

class PrintBook(Book):
    def __init__(self, page_count, title, author):
        super().__init__(title, author)
        self.page_count = page_count  # in grams

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


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
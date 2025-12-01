class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'"{self.title}" by {self.author}'
    
class EBook(Book):
    def __init__(self, file_size):
        super().__init__(self.title, self.author)
        self.file_size = file_size  # in MB

class PrintBook(Book):
    def __init__(self, page_count):
        super().__init__(self.title, self.author)
        self.page_count = page_count  # in grams


class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)
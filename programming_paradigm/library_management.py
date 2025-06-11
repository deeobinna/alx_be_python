class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
    
    def check_out(self):
        if self._is_checked_out:
            raise ValueError("This book is already checked out.")
        self._is_checked_out = True
        return True

    def return_book(self):
        if not self._is_checked_out:
            raise ValueError("This book was not checked out.")
        self._is_checked_out = False
        return True
    
    def is_available(self):
        return not self._is_checked_out
    
    
    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"
    
class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    return f"You have checked out '{book.title}'."
        return f"'{title}' is not available for checkout."
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    return f"You have returned '{book.title}'."
        return f"'{title}' was not checked out."
    
    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            return "No books are currently available."
        return "\n".join(str(book) for book in available_books)
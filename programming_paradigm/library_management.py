class Book:
    def __init__(self, title, author, _is_checked_out=False):
        self.title = title
        self.author = author
        self._is_checked_out = _is_checked_out  

#Implement a Library class with a private list _books to store instances of Book. Include methods to add_book, check_out_book(title), return_book(title), and list_available_books.

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)
        return f'Book "{book.title}" added to the library.'

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out:
                book._is_checked_out = True
                return f'You have checked out "{title}".'
        return f'Sorry, "{title}" is not available.'

    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out:
                book._is_checked_out = False
                return f'You have returned "{title}".'
        return f'"{title}" was not checked out.'

    def list_available_books(self):
        available_books = [book for book in self._books if not book._is_checked_out]
        if not available_books:
            return "No books are currently available."
        return [f'"{book.title}" by {book.author}' for book in available_books]


    
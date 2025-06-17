from library_system import Library, EBook, PrintBook, Book
def main():
    # Create a library instance
    library = Library()

    # Create some books
    ebook1 = EBook("Python Programming", "John Doe", 500)
    printbook1 = PrintBook("Learning OOP", "Jane Smith", 300)

    # Add books to the library
    library.add_book(ebook1)
    library.add_book(printbook1)

    # List all books in the library
    library.list_books()
if __name__ == "__main__":
    main()  
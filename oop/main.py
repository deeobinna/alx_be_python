from book_class import Book

def main():
    #create an instance of Book
    book1 = Book("1984", "George Orwell", 1949)

#demonstrate __str__ and __repr__
    print(book1)  # Calls __str__
    print(repr(book1))  # Calls __repr__

# Delete the book instance
    del book1

if __name__ == "__main__":
    main()
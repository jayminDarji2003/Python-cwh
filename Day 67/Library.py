class Library:
    # constructor
    def __init__(self, books=[]):
        self.books = books
        self.no_of_books = len(books)

    # Get Books
    def get_books(self):
        for book in self.books:
            print(book)

    # Get no of books
    def get_no_of_books(self):
        print(f"Number of Books in our library is : {self.no_of_books} ")

    # add a book to our Library
    def add_book(self, book_name):
        self.books.append(book_name)

    # add a book to our Library
    def remove_book(self):
        print(self.books)
        idx = int(input("Enter index of books to remove : "))
        self.books.pop(idx)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
class Library:
    def __init__(self, _books):
        self._books = []
    def add_book(self, book):
        self._books.append(book)
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out = False
                break
            book._is_checked_out = True
            print(f"{title} is already checked out.")
    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book._is_checked_out = False
                break
            else:
                print(f"{title} was not checked out.")
    def list_available_books(self):
        """List all books that are not checked out."""
        available_books = [book for book in self._books if not book._is_checked_out]
        if not available_books:
            print("No books are currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")

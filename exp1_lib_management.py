class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False

class Patron:
    def __init__(self, name, patron_id):
        self.name = name
        self.patron_id = patron_id
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)
        book.borrow()

    def return_book(self, book):
        self.borrowed_books.remove(book)
        book.return_book()
        
class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)

    def register_patron(self, patron):
        self.patrons.append(patron)

    def borrow_book(self, patron, book):
        patron.borrow_book(book)

    def return_book(self, patron, book):
        patron.return_book(book)

library = Library()

book1 = Book("Python", "Guido", "101")
book2 = Book("Java", "James", "102")

library.add_book(book1)
library.add_book(book2)

patron1 = Patron("Anushka", "P001")
library.register_patron(patron1)

library.borrow_book(patron1, book1)

print("Borrowed Books:")
for book in patron1.borrowed_books:
    print(book.title)

library.return_book(patron1, book1)

print("\nBook Returned Successfully")

print("\nLibrary Books:")
for book in library.books:
    print(book.title, "-", "Borrowed" if book.is_borrowed else "Available")
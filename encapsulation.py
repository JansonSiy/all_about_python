# Encapsulation
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_borrowed:
            print("Book is already borrowed!")
        else:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"Book - {book.title}|{book.author} has been successfully borrowed!")
    
    def return_book(self, book):
        if book not in self.borrowed_books:
            print(f"Book is not currently borrowed by {self.name}!")
        else:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"Book - {book.title}|{book.author} has been successfully returned!")
        
book1 = Book("Avengers", "Polar Bear")
book2 = Book("Justice League", "Pixie Fairy")
member = Member("Leon Siy")

member.borrow_book(book1) # Book - Avengers|Polar Bear has been successfully borrowed
member.borrow_book(book1) # Book is already borrowed!
member.return_book(book1) # Book - Avengers|Polar Bear has been successfully returned!
member.return_book(book1) # Book is not currently borrowed by Leon Siy!

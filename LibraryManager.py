from Book import Book
from Member import Member


class LibraryManager:
    def __init__(self):
        self.books = []
        self.members = []

        self.borrowed_book = {}

    def add_book(self, book_id, title, author, category, availability):
        for book in self.books:
            if book_id == book.book_id:
                print("Book", book_id, " already exist")
                break
        else:
            self.books.append(Book(book_id, title, author, category, availability))

    def add_member(self, member_id, name, email):
        for member in self.members:
            if member_id == member.member_id:
                print("Member ", member_id, " already exist")
        else:
            self.members.append(Member(member_id, name, email))

    def display_books(self):
        if not self.books:
            print("There are currently no books in the library.")
        else:
            for book in self.books:
                book.display()

    def search_book_by_id(self, book_id):
        for book in self.books:
            if(book.book_id == book_id):
                book.display()
                break
        else:
            print("Book Not Found")

    def search_book_by_category(self, category):
        found = False
        for book in self.books:
            if(book.category == category):
                book.display()
                found = True
        if found:
            print("Book Found")
        else:
            print("No Book Found")

    def borrow_book(self, member_id, book_id):
        found_member = False
        found_book = False
        for book in self.books:
            if (book.book_id == book_id and book.availability == "available"):
                for member in self.members:
                    if member_id == member.member_id:
                        if (member_id not in self.borrowed_book):
                            self.borrowed_book.setdefault(member_id, []).append(book_id)
                        else:
                            self.borrowed_book[member_id].append(book_id)
                        book.availability = "unavailable"
                        found_member = True
                if found_member:
                    print("Member found")
                else:
                    print("Add a member first")
                found_book = True

            elif(book.book_id == book_id and book.availability == "unavailable"):
                for member_key, book_value in self.borrowed_book.items():
                    if book_id in book_value:
                        print("Book", book_id, " was borrowed by Member ", member_key)
                found_book = True
        if found_book:
            print("Book found")
        else:
            print("Book ", book_id, " doesn't exist")

    def return_book(self, member_id, book_id):

        for book_key, book_value in self.borrowed_book.items():
            if (book_id in book_value and member_id == book_key):
                for book in self.books:
                    if (book.book_id == book_id):
                        book.availability = "available"
                        book_value.remove(book_id)
                break
        else:
            for book in self.books:
                if book.availability == "available":
                    print("Book ", book_id, " is available in the library, cannot be returned")
                    break
            else:
                print("Invalid, member ", member_id, " doesn't have book ", book_id)

    def delete_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.availability == "available":
                    self.books.remove(book)
                else:
                    print("Book", book_id," is not available, therefore it can not be deleted.")
                break
        else:
            print("Book not found")

    def display_statistics(self):
        number_of_borrowed_books = 0
        for book_key, book_value in self.borrowed_book.items():
            for book_id in book_value:
                number_of_borrowed_books += 1
        number_of_available_books = 0
        for book in self.books:
            if book.availability == "available":
                number_of_available_books += 1
        number_of_books = number_of_available_books + number_of_borrowed_books
        print("Total number of books: ", number_of_books)
        print("Total number of books borrowed: ", number_of_borrowed_books)
        print("Total number of available books: ", number_of_available_books)



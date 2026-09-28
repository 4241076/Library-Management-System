from LibraryManager import LibraryManager

def add_books():
    book_id = get_integer("Book ID: ")
    title = input("Title: ").lower()
    author = input("Author: ").lower()
    category = input("Category: ").lower()
    availability = input("Availability: ").lower()
    manager.add_book(book_id, title, author, category, availability)

def add_member():
    member_id = get_integer("Member ID: ")
    name = input("Name: ")
    email = input("Email: ")
    manager.add_member(member_id, name, email)

def search_a_book_by_id():
    book_id = get_integer("Enter book id: ")
    manager.search_book_by_id(book_id)

def search_a_book_by_category():
    category = input("Enter category: ").lower()
    manager.search_book_by_category(category)

def borrow_book():
    book_id = get_integer("Enter book id: ")
    member_id = get_integer("Enter member id: ")
    manager.borrow_book(member_id, book_id)

def return_book():
    book_id = get_integer("Enter book id: ")
    member_id = get_integer("Enter member id: ")
    manager.return_book(member_id, book_id)

def delete_book():
    book_id = get_integer("Enter book id: ")
    manager.delete_book(book_id)

def display_statistics():
    manager.display_statistics()

def display_books():
    manager.display_books()

def display_info():
    print("===================================")
    print("     LIBRARY MANAGEMENT SYSTEM     ")
    print("===================================")

    while True:
        print("\n1.Add book\n2.Add member\n3.Search book by ID\n4.Search book by category\n5.Borrow a book\n6.Return book\n7.Delete a book\n8.Display books\n9.Show statistics\n10.Exit")
        print("")

        option = get_integer("Choose option: ")
        match option:
            case 1:
                add_books()
            case 2:
                add_member()
            case 3:
                search_a_book_by_id()
            case 4:
                search_a_book_by_category()
            case 5:
                borrow_book()
            case 6:
                return_book()
            case 7:
                delete_book()
            case 8:
                display_books()
            case 9:
                display_statistics()
            case 10:
                break
            case _ :
                print("Invalid option")

def get_integer(string):
    while True:
        try:
            value = int(input(string))
            return value
        except ValueError:
            print("Invalid input")

manager = LibraryManager()

if __name__=="__main__":
    display_info()
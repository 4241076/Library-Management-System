class Book:
    def __init__(self, book_id, title, author, category, availability):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.availability = availability

    def display(self):
        print("Book ID: ", self.book_id, "\nTitle: ", self.title, "\nAuthor: ", self.author, "\nCategory: ", self.category, "\nAvailability: ", self.availability)

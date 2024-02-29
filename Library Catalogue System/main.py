# main.py RoboGarden Library Catalogue System
# Demian Swindells 2/28/2024
# Build a library catalogue system that manages information about books, including their title, author, and availability status.
# Use classes to represent books and include methods for checking out and returning books.

class Books:
 
  # Constructor
    def __init__(self, title, author, status):
        self.title = title
        self.author = author
        self.status = status

    #  Function to create and add a new book
    def add_book(self, title, author, status):
        book = Books(title, author, status)
        lst.append(book)

    # Function to check out a book
    def checkout_book(self, book):
        book.status = "Not Available"
        print("Book Checked out")

    # Function to return a book
    def return_book(self, book):
        book.status = "Available"
        print("Book Returned")
    # Function to display Library details
    def display_info(self, book):
        print("Title : ", book.title)
        print("Author : ", book.author)
        print("Status : ", book.status)
        print("\n")

# Create list to stor books
lst = []

# create objet of the Books Class
obj = Books("", "", "")

run = True
while run:
    user_input = input("Please make a choice: stop, view, add, checkout, return: ")

    if user_input == "stop":
        run = False
        break
    elif user_input == 'add':
        title = input("Enter Title Name: ")
        author = input("Enter Author Name: ")
        status = input("Enter Book Status: ")
        obj.add_book(title, author, status)
        continue
    elif user_input == 'view':
        print("\n")
        print("\nList of Books\n")
        for i in range(lst.__len__()):
            obj.display_info(lst[i])
        continue
    elif user_input == 'checkout':
        book = input("Please Enter Book Title to checkout: ")
        for i in range(lst.__len__()):
            if book == lst[i].title:
                obj.checkout_book(lst[i])
    elif user_input == 'return':
        book = input("Please Enter Book Title to return: ")
        for i in range(lst.__len__()):
            if book == lst[i].title:
                obj.return_book(lst[i])
    else:
        print("Please choose from the list provided")
        continue
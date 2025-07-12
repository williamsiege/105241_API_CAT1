# Question 1: Library Management System
# File: 105241_q1.py
# This program implements a simple library management system where users can borrow and return books.

# CLASS: Book
class Book:
    # Attributes: title, author, is_borrowed
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    # Methods: borrow, return_book, __str__
    def borrow(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False

    def __str__(self):
        return f"{self.title} by {self.author}"
# CLASS: LibraryMember
class LibraryMember:
    #Attributes: name, member_id, borrowed_books
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []
    # Methods: borrow_book, return_book, list_borrowed_books
    def borrow_book(self, book):
        if book.is_borrowed:
            print(f"Book '{book.title}' is already borrowed.")
        else:
            book.borrow()
            self.borrowed_books.append(book)
            print(f"You have borrowed '{book.title}'.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"You have returned '{book.title}'.")
        else:
            print("You did not borrow this book from our library.")

    def list_borrowed_books(self):
        if not self.borrowed_books:
            print("You have no borrowed books.")
        else:
            for i, book in enumerate(self.borrowed_books, 1):
                print(f"{i}. {book}")

# Main function to run the library management system
def main():
    # Sample books in the library
    books = [
        Book("Python Programming", "John Smith"),
        Book("Data Science Basics", "Jane Doe"),
        Book("Web Development", "Bob Johnson"),
        Book("Machine Learning", "Alice Brown")
    ]
    # Welcome message and member registration
    print("=== Library Management System ===")
    member_name = input("Enter your name: ")
    member_id = input("Enter your member ID: ")
    member = LibraryMember(member_name, member_id)

    print(f"Welcome, {member.name}! Your member ID is {member.member_id}.")
    # Main menu loop
    while True:
        print("\n=== Menu ===")
        print("1. View available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. List my borrowed books")
        print("5. Exit")
        # Get user choice
        choice = input("Enter your choice (1-5): ")
        # Process user choice
        if choice == '1':
            print("\n=== Available Books ===")
            available_books = [book for book in books if not book.is_borrowed]
            if available_books:
                for i, book in enumerate(available_books, 1):
                    print(f"{i}. {book}")
            else:
                print("No books available")

        elif choice == '2':
            print("\n=== Borrow a Book ===")
            available_books = [book for book in books if not book.is_borrowed]
            if available_books:
                for i, book in enumerate(available_books, 1):
                    print(f"{i}. {book}")
                try:
                    book_choice = int(input("Enter book number to borrow: ")) - 1
                    if 0 <= book_choice < len(available_books):
                        member.borrow_book(available_books[book_choice])
                    else:
                        print("Invalid book number")
                except ValueError:
                    print("Please enter a valid number")
            else:
                print("No books available for borrowing")

        elif choice == '3':
            print("\n=== Return a Book ===")
            if member.borrowed_books:
                for i, book in enumerate(member.borrowed_books, 1):
                    print(f"{i}. {book}")
                try:
                    book_choice = int(input("Enter book number to return: ")) - 1
                    if 0 <= book_choice < len(member.borrowed_books):
                        member.return_book(member.borrowed_books[book_choice])
                    else:
                        print("Invalid book number")
                except ValueError:
                    print("Please enter a valid number")
            else:
                print("You have no borrowed books to return")

        elif choice == '4':
            print("\n=== My Borrowed Books ===")
            member.list_borrowed_books()

        elif choice == '5':
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid choice. Please try again.")
# End of main function

if __name__ == "__main__": # Run the main function
    main()
# End of script
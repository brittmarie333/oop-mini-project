

import re
from bookclass import Book
from userclass import User
from authorclass import Author

class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []

    def display_main_menu(self):
        print("\nWelcome to the Library Management System!")
        print("Main Menu:")
        print("1. Book Operations")
        print("2. User Operations")
        print("3. Author Operations")
        print("4. Quit")

    def book_operations_menu(self):
        print("\nBook Operations:")
        print("1. Add a new book")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Search for a book")
        print("5. Display all books")
        print("6. Quit")

    def user_operations_menu(self):
        print("\nUser Operations:")
        print("1. Add a new user")
        print("2. View user details")
        print("3. Display all users")
        print("4. Quit")

    def author_operations_menu(self):
        print("\nAuthor Operations:")
        print("1. Add a new author")
        print("2. View author details")
        print("3. Display all authors")
        print("4. Quit")

    def add_book(self):
        title = input("Enter book title: ")
        if any(b.get(title) for b in self.books):
            print("We already have this book in the library!")
            return
        author = input("Enter author name: ")
        genre = input("Enter genre: ")
        publication_date = input("Enter publication date: ")
        new_book = Book(title, author, genre, publication_date)
        self.books.append(new_book)
        print("Book has been successfully added!")

    def borrow_book(self):
        book_title = input("Enter book title to borrow: ")
        user_name = input("Enter your name: ")
        user_id = input("Enter your library ID: ")

        user = next((u for u in self.users if u.get_library_id() == user_id), None)
        book = next((b for b in self.books if b.get_title() == book_title), None)

        if user and book:
            user.borrow_book(book)
        else:
            print("Invalid user or book.")

    def return_book(self):
        book_title = input("Enter book title to return: ")
        user_name = input("Enter your name: ")
        user_id = input("Enter your library ID: ")

        user = next((u for u in self.users if u.get_library_id() == user_id), None)
        book = next((b for b in self.books if b.get_title() == book_title), None)

        if user and book:
            user.return_book(book)
        else:
            print("Invalid, unable to find user or book.")

    def search_book(self):
        title = input("Please provide title: ")
        book = next((b for b in self.books if b.get_title() == title), None)
        if book:
            print(book.display_details())
        else:
            print("Book not found.")

    def display_books(self):
        for book in self.books:
            print(book.display_details())

    def add_user(self):
        name = input("Enter user name: ")
        library_id = input("Enter library ID: ")
        new_user = User(name, library_id)
        self.users.append(new_user)
        print("User added successfully!")

    def view_user_details(self):
        library_id = input("Enter user library ID: ")
        user = next((u for u in self.users if u.get_library_id() == library_id), None)
        if user:
            print(user.display_user_details())
        else:
            print("User not found.")

    def display_users(self):
        for user in self.users:
            print(user.display_user_details())

    def add_author(self):
        name = input("Enter author name: ")
        fav_color = input("Provide author's favorite color: ")
        new_author = Author(name,fav_color)
        self.authors.append(new_author)
        print("Author added successfully!")

    def view_author_details(self):
        name = input("Enter author name to view details: ")
        author = next((a for a in self.authors if a.get_name() == name), None)
        if author:
            print(author.display_author_details())
        else:
            print("Author not found.")

    def display_authors(self):
        for author in self.authors:
            print(author.display_author_details())

    def start(self):
        while True:
            self.display_main_menu()
            choice = input("Choose an option: ")

            if choice == "1":
                self.book_operations_menu()
                book_choice = input("Choose an option: ")
                if book_choice == "1":
                    self.add_book()
                elif book_choice == "2":
                    self.borrow_book()
                elif book_choice == "3":
                    self.return_book()
                elif book_choice == "4":
                    self.search_book()
                elif book_choice == "5":
                    self.display_books()
                elif book_choice == "6":
                    break

            elif choice == "2":
                self.user_operations_menu()
                user_choice = input("Choose an option: ")
                if user_choice == "1":
                    self.add_user()
                elif user_choice == "2":
                    self.view_user_details()
                elif user_choice == "3":
                    self.display_users()
                elif user_choice == "4":
                    br

            elif choice == "3":
                self.author_operations_menu()
                author_choice = input("Choose an option: ")
                if author_choice == "1":
                    self.add_author()
                elif author_choice == "2":
                    self.view_author_details()
                elif author_choice == "3":
                    self.display_authors()
                elif author_choice == "4":
                    break

            elif choice == "4":
                print("Thank you for visiting the Library.")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    system = LibraryManagementSystem()
    system.start()
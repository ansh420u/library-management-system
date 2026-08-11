import json
class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False


class Library:
    

    def __init__(self):
        self.books = []
        self.load_books()
    def add_book(self):

        title = input("Enter book title: ")
        author = input("Enter author name: ")

        book = Book(title, author)

        self.books.append(book)

        self.save_books()

        print("Book added successfully!")

    def view_books(self):

        if len(self.books) == 0:
            print("No books available.")
            return

        print("\n===== BOOKS =====")

        for index, book in enumerate(self.books, start=1):

            status = "Issued" if book.is_issued else "Available"

            print(f"\nBook {index}")
            print("Title:", book.title)
            print("Author:", book.author)
            print("Status:", status)
    def load_books(self):

        try:
            with open("books.json", "r") as file:
                data = json.load(file)

                for book_data in data:
                    book = Book(
                        book_data["title"],
                        book_data["author"]
                    )

                    book.is_issued = book_data["is_issued"]

                    self.books.append(book)

        except FileNotFoundError:
            self.books = []
    def save_books(self):

        data = []

        for book in self.books:

            book_data = {
                "title": book.title,
                "author": book.author,
                "is_issued": book.is_issued
            }

            data.append(book_data)

        with open("books.json", "w") as file:
            json.dump(data, file, indent=4)

    def search_book(self):

        title = input("Enter book title to search: ")

        found = False

        for book in self.books:

            if book.title.lower() == title.lower():

                status = "Issued" if book.is_issued else "Available"

                print("\nBook found!")
                print("Title:", book.title)
                print("Author:", book.author)
                print("Status:", status)

                found = True

        if not found:
            print("Book not found.")

    def issue_book(self):

        title = input("Enter book title to issue: ")

        for book in self.books:

            if book.title.lower() == title.lower():

                if book.is_issued:
                    print("Book is already issued.")
                    return

                book.is_issued = True
                self.save_books()
                print("Book issued successfully!")
                return

        print("Book not found.")

    def return_book(self):

        title = input("Enter book title to return: ")

        for book in self.books:

            if book.title.lower() == title.lower():

                if not book.is_issued:
                    print("Book is already available.")
                    return

                book.is_issued = False
                self.save_books()
                print("Book returned successfully!")
                return

        print("Book not found.")

    def delete_book(self):

        title = input("Enter book title to delete: ")

        for book in self.books:

            if book.title.lower() == title.lower():

                self.books.remove(book)
                self.save_books()
                print("Book deleted successfully!")
                return

        print("Book not found.")


library = Library()


while True:

    print("\n================================")
    print("      LIBRARY MANAGEMENT")
    print("================================")

    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.view_books()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.issue_book()

    elif choice == "5":
        library.return_book()

    elif choice == "6":
        library.delete_book()

    elif choice == "7":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")
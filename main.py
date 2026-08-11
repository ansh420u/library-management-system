import json
class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False

class Member:

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.issued_books = []


class Library:
    
    def load_members(self):

        try:
            with open("members.json", "r") as file:
                data = json.load(file)

                for member_data in data:

                    member = Member(
                        member_data["member_id"],
                        member_data["name"]
                    )

                    member.issued_books = member_data["issued_books"]

                    self.members.append(member)

        except FileNotFoundError:
            self.members = []

    def save_members(self):

        data = []

        for member in self.members:

            member_data = {
                "member_id": member.member_id,
                "name": member.name,
                "issued_books": member.issued_books
            }

            data.append(member_data)

        with open("members.json", "w") as file:
            json.dump(data, file, indent=4)
    def add_member(self):

        member_id = input("Enter member ID: ")
        name = input("Enter member name: ")

        for member in self.members:

            if member.member_id == member_id:
                print("Member ID already exists.")
                return

        member = Member(member_id, name)

        self.members.append(member)

        self.save_members()

        print("Member added successfully!")
        
    def view_members(self):
        if len(self.members) == 0:
            print("No members found.")
            return

        print("\n===== MEMBERS =====")

        for member in self.members:

            print("\nMember ID:", member.member_id)
            print("Name:", member.name)

            if len(member.issued_books) == 0:
                print("Issued Books: None")
            else:
                print("Issued Books:")
                for book in member.issued_books:
                    print("-",book)
                    
    def search_member(self):

        member_id = input("Enter member ID: ")

        for member in self.members:

            if member.member_id == member_id:

                print("\nMember found!")
                print("Member ID:", member.member_id)
                print("Name:", member.name)

                if len(member.issued_books) == 0:
                    print("Issued Books: None")
                else:
                    print("Issued Books:")

                    for book in member.issued_books:
                        print("-", book)

                return

        print("Member not found.")
    
    def delete_member(self):

        member_id = input("Enter member ID to delete: ")

        for member in self.members:

            if member.member_id == member_id:

                if len(member.issued_books) > 0:
                    print("Cannot delete member.")
                    print("Member has books that have not been returned.")
                    return

                self.members.remove(member)

                self.save_members()

                print("Member deleted successfully!")
                return

        print("Member not found.")        
    def __init__(self):
        self.books = []
        self.members=[]
        self.load_books()
        self.load_members()
        
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
        member_id=input("enter member ID:")
        selected_book=None
        selected_member=None
        for book in self.books:

            if book.title.lower() == title.lower():
                selected_book=book
                break

        if selected_book is None:
            print("Book not found.")
            return

        if selected_book.is_issued:
            print("Book is already issued.")
            return

        for member in self.members:

            if member.member_id == member_id:
                selected_member = member
                break

        if selected_member is None:
            print("Member not found.")
            return

        selected_book.is_issued = True

        selected_member.issued_books.append(selected_book.title)
        self.save_books()
        self.save_members()
        
        print("Book issued successfully")
        
        
    def return_book(self):

        title = input("Enter book title to return: ")

        selected_book = None
        selected_member = None

        for book in self.books:

            if book.title.lower() == title.lower():
                selected_book = book
                break

        if selected_book is None:
            print("Book not found.")
            return

        if not selected_book.is_issued:
            print("Book is already available.")
            return

        for member in self.members:

            if title.lower() in [book.lower() for book in member.issued_books]:
                selected_member = member
                break

        if selected_member is None:
            print("Member record not found.")
            return

        selected_book.is_issued = False

        selected_member.issued_books.remove(
            selected_book.title
        )

        self.save_books()
        self.save_members()

        print("Book returned successfully!")    


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

    print("\n----- BOOK MANAGEMENT -----")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")

    print("\n----- MEMBER MANAGEMENT -----")
    print("7. Add Member")
    print("8. View Members")
    print("9. Search Member")
    print("10. Delete Member")

    print("\n11. Exit")

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
        library.add_member()

    elif choice == "8":
        library.view_members()

    elif choice == "9":
        library.search_member()

    elif choice == "10":
        library.delete_member()

    elif choice == "11":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice. Please try again.")



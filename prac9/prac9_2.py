class Book:
    def __init__(self, title):
        self.title = title
        self.is_issued = False


class Member:
    def __init__(self, name):
        self.name = name


class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, title):
        self.books.append(Book(title))
        print("Book added successfully!")

    def display_books(self):
        print("\nAvailable Books:")
        for book in self.books:
            status = "Issued" if book.is_issued else "Available"
            print(f"{book.title} - {status}")

    def issue_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_issued:
                book.is_issued = True
                print("Book issued successfully!")
                return
        print("Book not available!")

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_issued:
                book.is_issued = False
                print("Book returned successfully!")
                return
        print("Invalid book name!")


# Menu-driven system
lib = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        title = input("Enter book title: ")
        lib.add_book(title)

    elif choice == '2':
        lib.display_books()

    elif choice == '3':
        title = input("Enter book title to issue: ")
        lib.issue_book(title)

    elif choice == '4':
        title = input("Enter book title to return: ")
        lib.return_book(title)

    elif choice == '5':
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
def add_book(library):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    book = {
        'title': title,
        'author': author,
        'status': 'Available'
    }
    library.append(book)
    print(f"Book '{title}' by {author} added successfully.\n")


def display_books(library):
    if not library:
        print("Library is empty.\n")
        return
    print("\nAvailable Books in Library:")
    for i, book in enumerate(library, start=1):
        print(f"{i}. {book['title']} by {book['author']} - Status: {book['status']}")
    print()


def borrow_book(library):
    title = input("Enter the title of the book to borrow: ")
    for book in library:
        if book['title'].lower() == title.lower():
            if book['status'] == 'Available':
                book['status'] = 'Borrowed'
                print(f"You have successfully borrowed '{book['title']}'.\n")
                return
            else:
                print("This book is currently borrowed.\n")
                return
    print("Book not found in the library.\n")


def return_book(library):
    title = input("Enter the title of the book to return: ")
    for book in library:
        if book['title'].lower() == title.lower():
            if book['status'] == 'Borrowed':
                book['status'] = 'Available'
                print(f"You have successfully returned '{book['title']}'.\n")
                return
            else:
                print("This book was not borrowed.\n")
                return
    print("Book not found in the library.\n")


def main():
    library = []  
    while True:
        
        print("1. Add Book")
        print("2. Display Books")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_book(library)
        elif choice == '2':
            display_books(library)
        elif choice == '3':
            borrow_book(library)
        elif choice == '4':
            return_book(library)
        elif choice == '5':
            print("Thank you for using the Library Management System.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")

l1=main()

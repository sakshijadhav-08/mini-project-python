library = {}

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Search Book")
    print("5. View All Books")
    print("6. Exit")

    choice = input("Enter Choice: ")

    # Add Book
    if choice == "1":
        isbn = input("Enter ISBN: ")

        if isbn in library:
            print("Book Already Exists!")
        else:
            title = input("Enter Book Title: ")
            author = input("Enter Author Name: ")

            library[isbn] = [title, author, "Available"]

            print("=== Book Added Successfully ===")
            print("Title:", title,"| Author:", author,"| ISBN:", isbn,"| Status: Available")

    # Issue Book
    elif choice == "2":
        isbn = input("Enter ISBN: ")

        if isbn in library:
            if library[isbn][2] == "Available":
                library[isbn][2] = "Issued"
                print("Book Issued Successfully!")
            else:
                print("Book Already Issued!")
        else:
            print("Book Not Found!")

    # Return Book
    elif choice == "3":
        isbn = input("Enter ISBN: ")

        if isbn in library:
            if library[isbn][2] == "Issued":
                library[isbn][2] = "Available"
                print("Book Returned Successfully!")
            else:
                print("Book is Already Available!")
        else:
            print("Book Not Found!")

    # Search Book
    elif choice == "4":
        isbn = input("Enter ISBN: ")

        if isbn in library:
            book = library[isbn]

            print("Title:", book[0])
            print("Author:", book[1])
            print("Status:", book[2])
        else:
            print("Book Not Found!")

    # View All Books
    elif choice == "5":
        if len(library) == 0:
            print("No Books Available!")
        else:
            for isbn, book in library.items():
                print("\nISBN:", isbn,"| Title:", book[0],"| Author:", book[1],"| Status:", book[2])

    # Exit
    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice!")
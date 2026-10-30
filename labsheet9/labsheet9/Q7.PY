# Menu-driven book management

books = []

while True:
    print("\n--- Book Management ---")
    print("1. Add book")
    print("2. View books")
    print("3. Update book")
    print("4. Delete book")
    print("5. Exit")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        book_id = input("Book ID: ").strip()

        if any(book["id"] == book_id for book in books):
            print("Book ID already exists.")
            continue

        title = input("Book title: ").strip()
        author = input("Author: ").strip()

        books.append({
            "id": book_id,
            "title": title,
            "author": author
        })
        print("Book added successfully.")

    elif choice == "2":
        if not books:
            print("No books available.")
        else:
            for book in books:
                print(book)

    elif choice == "3":
        book_id = input("Book ID to update: ").strip()

        for book in books:
            if book["id"] == book_id:
                book["title"] = input("New title: ").strip()
                book["author"] = input("New author: ").strip()
                print("Book updated successfully.")
                break
        else:
            print("Book not found.")

    elif choice == "4":
        book_id = input("Book ID to delete: ").strip()

        for book in books:
            if book["id"] == book_id:
                books.remove(book)
                print("Book deleted successfully.")
                break
        else:
            print("Book not found.")

    elif choice == "5":
        break

    else:
        print("Invalid choice.")
shelf_with_books = input().split("&")

while True:
    command = input().split(" | ")

    if command[0] == "Done":
        break

    event = command[0]
    value = command[1]

    if event == "Add Book":
        if value not in shelf_with_books:
            shelf_with_books.insert(0, value)

    elif event == "Take Book":
        if value in shelf_with_books:
            shelf_with_books.remove(value)

    elif event == "Swap Books":
        value_2 = command[2]
        if value in shelf_with_books and value_2 in shelf_with_books:
            index_book_1 = shelf_with_books.index(value)
            index_book_2 = shelf_with_books.index(value_2)
            temporary = shelf_with_books[index_book_1]
            shelf_with_books[index_book_1] = shelf_with_books[index_book_2]
            shelf_with_books[index_book_2] = temporary

    elif event == "Insert Book":
        if value not in shelf_with_books:
            shelf_with_books.append(value)

    elif event == "Check Book":
        if int(value) <= len(shelf_with_books) - 1:
            print(f"{shelf_with_books[int(value)]}")
print(", ".join(shelf_with_books))
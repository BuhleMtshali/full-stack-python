## 📚 Mini Book Wishlist App

A simple Python console app that helps you manage your personal book wishlist.
You can add books, view them, remove them, and even mark them as read — all through a fun, interactive menu.


## 🚀 Features

- View Books 📖 – See all the books in your wishlist with details (title, pages, year, read status).

- Add Book 📒 – Add a new book with title, number of pages, publication year, and read status.

- Remove Book 🗑️ – Remove a book from the wishlist by its title.

- Mark as Read 🥸 – Update a book’s read status to True once you’ve finished reading it.

- Exit 🚫 – Quit the app gracefully.


## 🛠️ How It Works

1. When you run the program, a menu is displayed.

2. You choose an option (1–5).

3. The app runs the corresponding function:

    - view_books() → Displays all saved books.

    - add_book() → Prompts for title, page numbers, year, and whether you’ve read it.

    - remove_book() → Lets you delete a book by title.

    - update_read() → Lets you mark a book as read.

    - main_function() → Controls the menu loop and app flow


## 🧰 Input Validation

- Uses a reusable get_input() function with validators to ensure correct user input.

- Prevents empty strings, invalid numbers, or invalid yes/no answers.

- Read status is stored as a boolean (True/False).


## 📋 Example Run

```
===== 🍄 Welcome To My Mini Bookwishlist 📚 =====

1. View Books 📖

2. Add Book 📒

3. Remove Book 🗑️

4. Mark as Read 🥸

5. Exit 🚫

Please choose an option?: 2

Enter the title of the book?: The Hobbit

How many pages is the book?: 310

Enter publication year: 1937

Have you read it yet? (yes/no): no

✅ Book has been added to the list

```

- Then, when you view books:

```
----- YOUR BOOKS -----
Title: The Hobbit
Pages: 310
Year: 1937
Read: False
------------------------------

```

## 💡 Future Improvements

- Save the wishlist to a file so data isn’t lost after exiting.

- Allow editing details (like changing the title or year).

- Add search/filter (e.g., show only unread books).

- Improve menu with error handling for invalid option choices.

## 🏁 Getting Started

- Run the app:

```
python book_wishlist.py

```

- Enjoy managing your book wishlist! 🍄
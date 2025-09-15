# BOOK WISHLIST
book_list = []

# HERE I'M GONNA CREATE FUNCTIONS FOR EACH OPTION
def greeting_message():
    print("\n" + "=" * 45)
    print("===== 🍄 Welcome To My Mini Bookwishlist 📚 =====")
    print("=" * 45 + "\n")

# FUNCTION FOR SHOWING THE MENU
def show_menu():
    print("1. View Books 📖")
    print("2. Add Book 📒")
    print("3. Remove Book 🗑️")
    print("4. Mark as Read 🥸")
    print("5. Exit 🚫")

    choice = int(input("Please choose an option?: "))

# FUNCTION FOR VIEWING BOOKS
def view_books():
    if book_list:
        print("----- YOUR BOOKS -----")
        for books in book_list:
            for key, value in books.items():
                print(f"{key.capitalize()}: {value}")
            print("-" * 30)

    else:
        print("🧺 Your cart is currently empty.")


# ADD BOOKS TO THE LIST
def get_input(prompt, validator, transform=lambda v: v):
    """REUSABLE INPUT FUNCTION WITH VALIDATION"""
    while True:
        value = input(prompt).strip()
        if validator(value):
            return transform(value)
        print("❌ Invalid input, try again.")

# HERE I AM VALIDATING THE USERS INPUT FOR YES/NO
def yes_no_validator(value):
    return value.lower() in ["yes", "y", "no", "n"]

#RETURNS TRUE IF YES/Y
def yes_no_transform(value):
    return value.lower() in ["yes", "y"]

# FUNCTION THAT ACTUALLY THE BOOK TO THE LIST
def add_book():
    while True:
        book_name = get_input("Enter the title of the book?: ", lambda v: len(v) > 0)
        page_numbers = get_input("How many pages is the book?: ", lambda v: v.isdigit() and 0 < int(v) < 10000000, transform=lambda v: int(v)) #HERE THE BOOK PAGES ARE STORED AS A NUMBER INSTEAD OF STRING
        book_pub_year = get_input("Enter publification year: ", lambda v: v.isdigit() and 0 < int(v) <= 2025, transform=lambda v: int(v))
        have_read = get_input("Have you read it yet? (yes/no): ", yes_no_validator, yes_no_transform)

        book = {
            "title": book_name,
            "pages": page_numbers,
            "year": book_pub_year,
            "read": have_read
        }

        book_list.append(book)
        print(f"✅ Book has been added to the list")
        print(book_list)

        add_another = input("Wanna add another book? (yes/no): ")
        if add_another != "yes":
            break
    
# FUNCTION TO REMOVE A BOOK
def remove_book():
    while True:
        book_name = get_input("Enter the title of the book you want to remove: ", lambda v: len(v) > 0)
        found = False

        for book in book_list:
            if book["title"].lower() == book_name.lower():
                book_list.remove(book)
                print(f"✅ {book['title']} has been successfuly removed")
                found = True
                break

        if not found:
            print(f"🚫 {book_name} does not exist")

        remove_another = input("Do you want to remove another book? (yes/no): ")
        if remove_another != "yes":
            break


# FUNCTION TO UPDATE THAT THE PEROSN HAS READ THE BOOK
def update_read():
    while True:
        update_name = get_input("Enter the title of the book you want to update: ", lambda v: len(v) > 0)
        found = False
        for book in book_list:
            if book["title"].lower() == update_name.lower():
                book["read"] = True
                print(f"✅ Updated {book["title"]} to read!")
                found = True
                break

        if not found:
            print(f"{update_name} does not exist!")

        update_another = input("Do you want to update another book? (yes/no): ")
        if update_another != "yes":
            break


# STARTING THE MAIN FUNCTION
def main_function():
    while True:

        print("1. View Books 📖")
        print("2. Add Book 📒")
        print("3. Remove Book 🗑️")
        print("4. Mark as Read 🥸")
        print("5. Exit 🚫")

        choice = int(input("Please choose an option?: "))

        # CONDITIONAL STATEMENTS
        if choice == 1:
            view_books()
        
        elif choice == 2:
            add_book()

        elif choice == 3:
            remove_book()

        elif choice == 4:
            update_read()

        elif choice == 5:
            break

        do_another = input("\nDo want to perfom another action your book list? (yes/no): ")
        if do_another != "yes":
            print("\n--------- THANK YOU FOR TRYING MY MINI BOOK WISHLIST APP ------")
            break

main_function()
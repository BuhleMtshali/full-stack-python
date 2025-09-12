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

# FUNCTION FOR VIEWING BOOKS
def view_books():
    if book_list:
        print("\n📝 Your Books:")
        for i, book in enumerate(book_list, start=1):
            print(f"{i}. {book.title()}")

    else:
        print("🧺 Your cart is currently empty.")


# ADD BOOKS TO THE LIST
def get_input(prompt, validator):
    """REUSABLE INPUT FUNCTION WITH VALIDATION"""
    while True:
        value = input(prompt).strip()
        if validator(value):
            return value
        print("❌ Invalid input, try again.")

def add_book():
    book_name = get_input("Enter the title of the book?: ", lambda v: len(v) > 0)
    page_numbers = get_input("How many pages is the book?: ", lambda v: v.isdigit() and 0 < int(v) < 10000000)
    #book_pub_year = input("Enter publification year: ")
    #have_read = input("Have you read it yet? (yes/no): ")
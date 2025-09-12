# BOOK WISHLIST
book_list = []

# HERE I'M GONNA CREATE FUNCTIONS FOR EACH OPTION
def greeting_message():
    print("\n" + "=" * 45)
    print("===== 🍄 Welcome To My Mini Bookwishlist 📚 =====")
    print("=" * 45 + "\n")


def show_menu():
    print("1. View Books 📖")
    print("2. Add Book 📒")
    print("3. Remove Book 🗑️")
    print("4. Mark as Read 🥸")
    print("5. Exit 🚫")

def view_books():
    if book_list:
        print("\n📝 Your Books:")
        for i, book in enumerate(book_list, start=1):
            print(f"{i}. {book.title()}")

    else:
        print("🧺 Your cart is currently empty.")


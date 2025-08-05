# ==== 🍄 Grocery List Mini Project 🛒 ==== #

# List to hold the grocery items
grocery_list = []

def print_greeting():
    print("\n" + "=" * 45)
    print("===== 🍄 Welcome To My Mini Grocery List 🛒 =====")
    print("=" * 45 + "\n")

def show_menu():
    print("1. View Cart")
    print("2. Add Item")
    print("3. Delete Item")
    print("4. Search Item")
    print("5. Exit")

def view_cart():
    if grocery_list:
        print("\n🛍️ Your Cart Items:")
        for i, item in enumerate(grocery_list, start=1):
            print(f"{i}. {item.title()}")
    else:
        print("🫥 Your cart is currently empty.")

def add_item():
    item = input("Enter the name of the item you want to add: ").strip().lower()
    if item in grocery_list:
        print("🚫 Item already exists in your list.")
    else:
        grocery_list.append(item)
        print(f"✅ {item.title()} has been successfully added to your cart.")

def delete_item():
    item = input("Enter the name of the item you want to remove: ").strip().lower()
    if item in grocery_list:
        grocery_list.remove(item)
        print(f"✅ {item.title()} has been successfully removed from your cart.")
    else:
        print(f"🚫 {item.title()} does not exist in your cart.")

def search_item():
    item = input("Enter the name of the item you want to search for: ").strip().lower()
    if item in grocery_list:
        print(f"✅ {item.title()} *does* exist in your list.")
    else:
        print(f"🚫 {item.title()} does not currently exist in your list. Try adding it!")

# Start the program
print_greeting()

while True:
    show_menu()
    option = input("\nPlease choose an option (1–5): ").strip()

    if option == "1":
        view_cart()
    elif option == "2":
        add_item()
    elif option == "3":
        delete_item()
    elif option == "4":
        search_item()
    elif option == "5":
        print("\n🛒 Thank you for using this mini grocery cart app. See you next time!")
        break
    else:
        print("🚫 Invalid input. Please enter a number from 1 to 5.")

    print("\n" + "-" * 40)
    again = input("Wanna make another operation? (yes/no): ").strip().lower()
    if again != "yes":
        print("\n👋 Thank you for trying my mini grocery list.")
        break

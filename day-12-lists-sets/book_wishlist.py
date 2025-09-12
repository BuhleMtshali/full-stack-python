#MAIN CART
shopping_cart = {"bread", "cheese"}

print("\n--------- 📝 Welcome to My Mini Shopping Cart 🛒 --------")

# START THE WHILE LOOP

while True:
    try:
        print("1. View Cart 🛒")
        print("2. Add Item 🥗")
        print("3. Remove item 🚫")
        print("4. Exit❌ ")
    except ValueError:
        print("Oppps wrong option")
        continue
#list to hold the grocery items
grocery_list = []

#greeting message
greeting = print("===== 🍄Welcome To My Mini Grocery List🛒 ======");
user_name = print("Enter your name: ");

while True:
    print("here is the start of the loop")
    #loop opens at the top here

    print("1. View Cart")
    print("2. Add Item")
    print("3. Delete Item")
    print("4. Search Item")
    print("5. Exit")

    optio = input("\nPlease Choose an option: ")



    #closing the loop
    add_again = input("\nWanna make another operation? (yes/no): ").strip().lower()
    if add_again != "yes":
        print("\nThank you for trying my mini grocery list")
        break
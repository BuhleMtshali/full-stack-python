#list to hold the grocery items
grocery_list = ["eggs", "rice"]

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

    option = input("\nPlease Choose an option: ")

    #tomorrow i will implement if/else
    if option == "1":
        if len(grocery_list) > 0:
            for item in grocery_list:
                print(item)
        else:
            print("Your cart is currently empty")
        


    #closing the loop
    add_again = input("\nWanna make another operation? (yes/no): ").strip().lower()
    if add_again != "yes":
        print("\nThank you for trying my mini grocery list")
        break
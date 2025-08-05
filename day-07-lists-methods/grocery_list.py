#list to hold the grocery items
grocery_list = ["eggs", "rice"]

#greeting message
greeting = print("\n===== 🍄Welcome To My Mini Grocery List🛒 ======");
user_name = print("\nEnter your name: ");

while True:
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

    elif option == "2":
        add_item = input("Enter the name of the item you want to add: ").strip().lower()
        if add_item in grocery_list:
            print("🚫 Item already exists in your list") 
        else:
            grocery_list.append(add_item)
            print(f"✅ {add_item} has been successfuly added to your cart")       


    elif option == "3":
        remove_item = input("Enter the item you want to remove: ").strip().lower()
        if remove_item in grocery_list:
            grocery_list.remove(remove_item)
            print(f"✅ {remove_item} has been successfully removed from your cart")
        else:
            print(f"🚫 {remove_item} does not exist in your cart")
    
    elif option == "4":
        search_item = input("Enter the name of the item you want to search for in the list: ").strip().lower()
        if search_item in grocery_list:
            print(f"✅ {search_item} does exist in your list")
        else:
            print(f"🚫 {search_item} does not currently exist in your list, try adding it")

    elif option == "5":
        print("Thank you using this mini cart app")
        break

    else:
        print("🚫Invalid input try again")
    #closing the loop
    add_again = input("\nWanna make another operation? (yes/no): ").strip().lower()
    if add_again != "yes":
        print("\nThank you for trying my mini grocery list")
        break
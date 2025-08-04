#list to hold the grocery items
grocery_list = []

while True:
    print("here is the start of the loop")



    #closing the loop
    add_again = input("\nWanna make another operation? (yes/no): ").strip().lower()
    if add_again != "yes":
        print("\nThank you for trying my mini grocery list")
        break
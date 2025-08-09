#main list 
phone_book = []


#greet message
greeting = print(" ===== 📵Welcome To Your Mini PhoneBook☎️ =====")

print(greeting)

#creatng a function for viewing the phone phonebook
def view_contact_list():
    """view the contact list"""
    if len(phone_book) > 0:
        for phone in phone_book:
            print(f"Contact: {phone}")
    else:
        print("🚫Phone Book is currently empty")


while True:
    print("1. View Contact")


    add_again = input("\nWanna add another contact? (yes/no): " ).strip().lower()
    if add_again != "yes":
        print("\nThank you for trying Mini Phonebook app!")
        break
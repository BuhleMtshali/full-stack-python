#main list 
phone_book = [("Buhle", "0815905473")]


#greet message
greeting = print(" ===== 📵Welcome To Your Mini PhoneBook☎️ =====")

print(greeting)

#creatng a function for viewing the phone phonebook
def view_contact_list():
    """view the contact list"""
    if len(phone_book) > 0:
        print("====== Contact List☎️ =======")
        for index, (name, phone) in enumerate(phone_book, start=1):
            print(f"""
            List no. {index}
            Name: {name.title()}
            Number: {phone}
                  """)
    else:
        print("🚫Phone Book is currently empty")

#creating an add function
def add_contact():
    #check if the name was actually given
    while True:
        name = input("Enter name: ").strip().lower()
        if not name:
            print("Name cannot be empty, please add your name")
        else:
            break
                
    #while loop to check if the len is actually 10
    while True:
        number = input("Enter number: ").strip()
        if len(number) >= 10:
            person = (name, number)
            break;
        else:
            print("Number is invalid, please try again")

    phone_book.append(person)

#CREATING THE DELETE FUNCTION
def delete_contact():
    while True:
        delete_name = input("Enter the name of the contact you want to delete: ").strip().lower()
        found = False

        for contact in phone_book:
            if contact[0].lower() == delete_name:
                phone_book.remove(contact)
                print(f"✅ {contact[0]} has been successfully removed from the list")
                found = True
                break  # exit loop after deleting
        
        if not found:
            print(f"🚫 {delete_name.title()} does not exist in the list")
        
        again = input("Delete another contact? (yes/no): ").strip().lower()
        if again != "yes":
            break



#THE MAIN LOOOP FOR THE WHOLE PROGRAM

while True:
    print("1. View Contact List")
    print("2. Add Contact")
    print("3. Delete Contact")

    #user choice
    choice = int(input("Choose an option: "))

    #conditional statements
    if choice == 1:
        view_contact_list()

    elif choice == 2:
        add_contact()

    elif choice == 3:
        delete_contact()
    
    #ask the user if they wanna continue again
    add_again = input("\nWanna add another contact? (yes/no): " ).strip().lower()
    if add_again != "yes":
        print("\nThank you for trying Mini Phonebook app!")
        print("===== end ====")
        break
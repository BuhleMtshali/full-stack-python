#main list 
phone_book = [("Buhle", "0815905473")]


#greet message
greeting = print(" ===== 📵Welcome To Your Mini PhoneBook☎️ =====")

print(greeting)

#creatng a function for viewing the phone phonebook
def view_contact_list():
    """view the contact list"""
    if len(phone_book) > 0:
        for index, (name, phone) in enumerate(phone_book, start=1):
            print(f"""
                ====== Contact List☎️ =======
                
                List no. {index}
                Name: {name.title()}
                Number: {phone}
                  """)
    else:
        print("🚫Phone Book is currently empty")


while True:
    print("1. View Contact List")

    #user choice
    choice = int(input("Choose an option: "))

    #conditional statements
    if choice == 1:
        view_contact_list()


    add_again = input("\nWanna add another contact? (yes/no): " ).strip().lower()
    if add_again != "yes":
        print("\nThank you for trying Mini Phonebook app!")
        break
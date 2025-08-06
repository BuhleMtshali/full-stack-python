#main list 
phone_book = []


#greet message
greeting = print(" ===== 📵Welcome To Your Mini PhoneBook☎️ =====")

print(greeting)


while True:
    print("Here i am startig a loop")


    add_again = input("\nWanna add another contact? (yes/no): " ).strip().lower()
    if add_again != "yes":
        print("\nThank you for trying Mini Phonebook app!")
        break
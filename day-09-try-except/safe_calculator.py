print("------ Welcome to my Mini Safe Calculator📝 -------")

#STARTING THE WHILE LOOP
while True:
    try:
        first_number = float(input("Enter your first digit: "))
    except ValueError:
        print("Oops, invalid input, please try again")
        continue
    
    try:
        operator = input("Choose your operator (+, -, *, /): ")
    except ValueError:
        print("Invalid operator, please try again!")

    
    second_number = float(input("Enter your second digit: "))

    calculate_again = input("\nWanna make another calculation? (yes/no): ")
    if calculate_again != "yes":
        print("\nThank you trying my mini calculator!!!")
        break;

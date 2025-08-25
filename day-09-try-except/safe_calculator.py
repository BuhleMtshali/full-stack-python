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

    try:
        second_number = float(input("Enter your second digit: "))
    except ValueError:
        print("Invalid number, please try again")
    
    result = 0

    #IF STATEMENT
    if operator == "+":
        result = first_number + second_number

    elif operator == "-":
        result = first_number - second_number
    
    elif operator == "*":
        result = first_number * second_number

    elif operator == "/":
        if first_number == 0:
            print("Cannot divide by 0")
        else:
            result = first_number / second_number



    print(f"Result: {result}")

    calculate_again = input("\nWanna make another calculation? (yes/no): ")
    if calculate_again != "yes":
        print("\nThank you trying my mini calculator!!!")
        break;

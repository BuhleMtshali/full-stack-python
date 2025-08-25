print("------ Welcome to my Mini Safe Calculator📝 -------")

#STARTING THE WHILE LOOP
while True:
    first_number = float(input("Enter your first digit: "))
    operator = input("Choose your operator (+, -, *, /): ")
    second_number = float(input("Enter your second digit: "))

    calculate_again = input("\nWanna make another calculation? (yes/no): ")
    if calculate_again != "yes":
        print("\nThank you trying my mini calculator!!!")
        break;

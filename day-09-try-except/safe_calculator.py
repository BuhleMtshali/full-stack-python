print("------ Welcome to my Mini Safe Calculator📝 -------")

while True:
    try:
        first_number = float(input("Enter your first digit: "))
    except ValueError:
        print("🚫 Oops, invalid input, please try again")
        continue

    operator = input("Choose your operator (+, -, *, /): ")
    if operator not in ["+", "-", "*", "/"]:
        print("🚫 Invalid operator, please try again!")
        continue

    try:
        second_number = float(input("Enter your second digit: "))
    except ValueError:
        print("🚫 Invalid number, please try again")
        continue

    result = 0

    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        if second_number == 0:
            print("🚫 Cannot divide by 0")
            continue
        else:
            result = first_number / second_number

    print(f"✅ Result: {result}")

    calculate_again = input("\nWanna make another calculation? (yes/no): ").strip().lower()
    if calculate_again != "yes":
        print("\n🙏 Thank you for trying my mini calculator!!!")
        break

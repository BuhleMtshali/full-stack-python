print("====== Welcome to My Mini Multiplication Calculator🧮 =======")

while True:
    try:
        number_to_multiply = int(input("Enter the number for the Multiplication table: "))
    except ValueError:
        print("Oops! That's not a number. Try again. 💀\n")
        continue

    print(f"\nMultiplication table for {number_to_multiply}:")
    for i in range(1, 11):
        result = number_to_multiply * i
        print(f"{number_to_multiply} x {i} = {result}")

    multiply_again = input("\nWanna go another round? (yes/no): ").strip().lower()
    if multiply_again != "yes":
        print("\nOkay, thank you for trying my mini multiplication calculator! See ya! 👋")
        break

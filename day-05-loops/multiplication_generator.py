main_list = [];

print("====== Welcome to My Mini Multiplication Calculator🧮 =======");

while True:

    number_to_multiply = int(input("Enter the number for the Multiplication table: "));

    print(f"Multiplication table for {number_to_multiply}: ")
    for i in range(1, 11):
        result = number_to_multiply * 1
        print(f"{number_to_multiply} x {i} = {result}")

    multiply_again = input("\nWanna go another round? (yes/no): ").lower()
    if multiply_again != "yes":
        print("\nOkay, thank you for trying my mini multiplication calculator!!")
        break;
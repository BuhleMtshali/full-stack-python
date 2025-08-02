def get_BMI():
    """Calculate the BMI for the user"""
    print("===== Welcome to My mini BMI Calculator🧮 =====")

    while True:
    
        user_name = input("Enter your name: ")
        user_weight = float(input("Enter your weight in(kg): "))
        user_height_cm = float(input("Enter your height in(cm): "))
        user_height = user_height_cm / 100
        overall_BMI = user_weight / (user_height ** 2)

        print(f"Okay {user_name}, your weight is {user_weight}kg and your height is {user_height}m, so with that information, we have calculated your overall BMI to be {overall_BMI:.2f}kg/m^2")
        
        calculate_again = input("\nWanna make another calculation? (yes/no): ").strip().lower()
        if calculate_again != "yes":
            print(f"\nThank you {user_name} for trying my mini BMI calculator")
        break

get_BMI()
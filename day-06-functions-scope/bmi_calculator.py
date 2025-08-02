def get_BMI():
    """Calculate the BMI for the user"""
    print("===== Welcome to My mini BMI Calculator🧮 =====")
    user_name = input("Enter your name: ")
    user_weight = float(input("Enter your weight in(kg): "))
    user_height = float(input("Enter your height in(m): "))

    overall_BMI = user_weight * (user_height ** 2)

    print(f"Okay {user_name}, your weight is {user_weight}kg and your height is {user_height}m, so with that information, we have calculated your overall BMI to be {overall_BMI}kg/m^2")


get_BMI()
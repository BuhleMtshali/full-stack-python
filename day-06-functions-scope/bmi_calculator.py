
def get_BMI():
    """Calculate the BMI for the user"""
    print("===== Welcome to My mini BMI Calculator🧮 =====")
    user_name = input("Enter your name: ")

    #main loop
    while True:

        #second loop
        while True:
            try:
                user_weight = float(input("Enter your weight in(kg): "))
                break
            except ValueError:
                print(f"Sorry, that is not a valid number, lets try again: ")
        
        while True:        
            try:
                user_height_cm = float(input("Enter your height in(cm): "))
                break
            except ValueError:
                print(f"Sorry, {user_name}, this is not a valid number, please try again: ")
    

        user_height = user_height_cm / 100
        overall_BMI = user_weight / (user_height ** 2)
       
        category = get_BMI_category(overall_BMI)
    
        print(f"\n{user_name}, your BMI is {overall_BMI:.2f}kg/m² — You are **{category}**!")


        
        calculate_again = input("\nWanna make another calculation? (yes/no): ").strip().lower()
        if calculate_again != "yes":
            print(f"\nThank you {user_name} for trying my mini BMI calculator")
            break
    
 
def get_BMI_category(bmi):
    """Categorizing BMI"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"
    
get_BMI()
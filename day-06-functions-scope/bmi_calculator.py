
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
        return overall_BMI

        def get_BMI_category(overall_BMI):
            """categorizing BMI"""
            if overall_BMI < 18.5:
                return "underweight"
            elif 18.5 <= overall_BMI < 25:
                return "Normal Weight"
            elif 25 <= overall_BMI < 30:
                return "Overweight"
            else:
                return "Obese"



        calculate_again = input("\nWanna make another calculation? (yes/no): ").strip().lower()
        if calculate_again != "yes":
            print(f"\nThank you {user_name} for trying my mini BMI calculator")
            break
    
 
get_BMI()
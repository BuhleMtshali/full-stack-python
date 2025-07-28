#greeting
print("----- Welcome to My Mini Tip Calculator💰 -----")

order_total = int(input('Enter your order total: '))

tip_amount = int(input('Enter the tip percentage you wanna leave(0% - 100%): '))

converted_tip_amount = (tip_amount / 100) * order_total

overall_total = order_total + converted_tip_amount

number_of_people = int(input('How many people are the dividing the order total with: '))

amount_per_person = overall_total / number_of_people

print(f"Each person will pay: {amount_per_person}")


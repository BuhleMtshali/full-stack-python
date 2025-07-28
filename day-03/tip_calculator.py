#greeting
print("----- Welcome to My Mini Tip Calculator💰 -----")

order_total = float(input('Enter your order total: '))

tip_amount = float(input('Enter the tip percentage you wanna leave(0 - 100): '))

converted_tip_amount = (tip_amount / 100) * order_total

overall_total = order_total + converted_tip_amount

number_of_people = int(input('How many people are the dividing the order total with: '))

if number_of_people == 0:
    print("Okay friend the whole bill is on you!!")
    print("======== Order Receipt🧾 =========")
    print(f"Order Total: R{order_total:.2f}")
    print(f"Tip Amount: {tip_amount}%")
    print(f"Overall Total: R{overall_total:.2f}")
else:
    amount_per_person = overall_total / number_of_people
    print("======== Order Receipt🧾 =========")
    print(f"Order Total: R{order_total:.2f}")
    print(f"Tip Amount: {tip_amount}%")
    print(f"Overall Total: R{overall_total:.2f}")
    print(f"Number of People Sharing the Bill: {number_of_people}")
    print(f"Amount Per Person: R{amount_per_person:.2f}")
    print("========= Thank You For Trying My Tip Calculator =======")


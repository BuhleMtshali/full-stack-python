print("======= 📝Welcome to My Mini Grade Checker ======")
student_name = input("Enter your name🙋🏻‍♀️: ")
module_name = input("Enter your Module Name📔: ")
module_grade = float(input('What was your mark for the module✅: '))
module_total = float(input('What was the Module total📇: '))

overall_grade = (module_grade / module_total) * 100

if overall_grade >= 90:
    print(f"Okay {student_name.title()}, you got {module_grade} in your {module_name} which was out of {module_total} and thus your final grade is: {overall_grade}%, Congrats, you got an A+")
elif overall_grade >= 80:
    print(f"Okay {student_name.title()}, you got {module_grade} in your {module_name} which was out of {module_total} and thus your final grade is: {overall_grade}%, ongrats, you got an A-")
elif overall_grade >= 70:
    print(f"Okay {student_name.title()}, you got {module_grade} in your {module_name} which was out of {module_total} and thus your final grade is: {overall_grade}%, ongrats, you got an C")
elif overall_grade >= 60:
    print(f"Okay {student_name.title()}, you got {module_grade} in your {module_name} which was out of {module_total} and thus your final grade is: {overall_grade}%, ongrats, you got an D+")
elif overall_grade >= 50:
    print(f"Okay {student_name.title()}, you got {module_grade} in your {module_name} which was out of {module_total} and thus your final grade is: {overall_grade}%, ongrats, you got an D-")
elif overall_grade < 50:
    print(f"Okay {student_name.title()}, you got {module_grade} in your {module_name} which was out of {module_total} and thus your final grade is: {overall_grade}%, ongrats, you got an F")
else:
    print(f"Okay {student_name.title()}, thats invalid friend")



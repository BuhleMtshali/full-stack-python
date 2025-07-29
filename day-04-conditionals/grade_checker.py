print("======= 📝 Welcome to My Mini Grade Checker ======")

student_name = input("Enter your name 🙋🏻‍♀️: ")
module_name = input("Enter your Module Name 📔: ")
module_grade = float(input('What was your mark for the module ✅: '))
module_total = float(input('What was the Module total 📇: '))

overall_grade = (module_grade / module_total) * 100

# Response templates
grade_message = f"""
Okay {student_name.title()}, you got {module_grade} in your {module_name} 
which was out of {module_total}, and your final grade is: {overall_grade:.2f}%.
"""

# Grade boundaries
if overall_grade >= 90:
    print(grade_message + "🎉 Congrats, you got an A+")
elif overall_grade >= 80:
    print(grade_message + "👏 Congrats, you got an A-")
elif overall_grade >= 70:
    print(grade_message + "👍 Congrats, you got a C")
elif overall_grade >= 60:
    print(grade_message + "🙂 Congrats, you got a D+")
elif overall_grade >= 50:
    print(grade_message + "😅 Congrats, you got a D-")
elif overall_grade < 50:
    print(grade_message + "😢 Sorry, you got an F. But hey, you can bounce back!")

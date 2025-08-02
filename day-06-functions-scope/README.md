## 🧮 Mini BMI Calculator – Day 6 Project

Welcome to Day 6 of Buhle's Full-Stack Python Developer journey!
Today, we cooked up a BMI calculator with error handling, looping logic, function modularity, and ✨clean output formatting✨.

## 💡 Project Description

- This is a simple console-based Body Mass Index (BMI) calculator built with Python.

- It takes a user’s name, weight (kg), and height (cm), then calculates and categorizes their BMI based on WHO standards.

- The user can also loop through multiple calculations until they’re done.

## 🧠 What I Learned

- How to nest loops inside a while True block for repeated validation.

- Used try-except blocks to handle bad user input like a champ.

- Created multiple functions to break up logic: one for BMI calculation, another for category classification.

- Practiced f-strings and multi-line formatting for clean and readable output.

- Used Unicode (like ²) to style math expressions ✨


## 🧪 Features

✅ Asks the user for their name

✅ Takes user weight and height with validation

✅ Calculates BMI using: BMI = weight / height²

✅ Classifies the BMI into: Underweight, Normal weight, Overweight, or Obese

✅ Asks if the user wants to calculate again

✅ Uses formatted, professional-looking print output

## 🖥️ Sample Output

```
===== Welcome to My mini BMI Calculator🧮 =====
Enter your name: Buhle
Enter your weight in(kg): 55
Enter your height in(cm): 165

========= BMI Report🙋🏻‍♀️ for: Buhle ===========

Name: Buhle
Weight(kg): 55.0
Height(cm): 1.65
BMI(kg/m²): 20.20
BMI Category: Normal Weight

======================

Wanna make another calculation? (yes/no): no

Thank you Buhle for trying my mini BMI calculator

```

## 🔧 How It Works

```

# Main Function:
def get_BMI():  
    # Gets user input, validates it, calculates BMI and prints results

# Helper Function:
def get_BMI_category(bmi):  
    # Returns BMI category string based on value

```

## 🛠️ Next Steps

- Add unit tests to check the BMI and category logic

- Turn this into a GUI version using tkinter or a web app with Flask

- Allow for imperial units (lbs/inches) in the future

- Log previous BMI results into a text file or CSV

## 📅 Day 6 Vibes

✅ Focus: Error handling, nested loops, and output formatting

🎯 Goal: Build a beginner-friendly but robust terminal app

🔥 Status: Completed with ✨style and logic✨

Made with love, logic, and a sprinkle of chaos by Buhle 💻💫
## 🧮 Mini Safe Calculator (Day 9)

## 📌 Project Overview

This is a beginner-friendly safe calculator built in Python.
It allows users to perform basic math operations (addition, subtraction, multiplication, division) while ensuring the program doesn’t crash when invalid inputs are entered.

The calculator uses try/except error handling to validate user input and gracefully recover from mistakes like entering text instead of a number.


## 🚀 Features

- Handles invalid inputs without breaking.

- Supports the following operators:

    - ➕ Addition (+)

    - ➖ Subtraction (-)

    - ✖️ Multiplication (*)

    - ➗ Division (/)

- Prevents division by zero errors.

- Allows continuous calculations until the user decides to exit.


## 🛠️ Technologies Used

Python 3

## 📂 Project Structure

```
Day9_MiniCalculator/

│── calculator.py   # Main program file

│── README.md       # Project documentation

```

## 💡 How It Works

1. User inputs the first number.

2. Chooses an operator (+, -, *, /).

3. Inputs the second number.

4. Program calculates and prints the result.

5. User can choose to calculate again or exit.

## 📝 Example Run

```
------ Welcome to my Mini Safe Calculator📝 -------

Enter your first digit: 12
Choose your operator (+, -, *, /): *
Enter your second digit: 5

Result: 60.0

Wanna make another calculation? (yes/no): no

Thank you trying my mini calculator!!!

```

## 🔮 Future Improvements

- Add power (^) and modulus (%) operators.

- Allow users to type entire equations (e.g., 12 + 5).

- Add a simple GUI version with Tkinter or PyQt.
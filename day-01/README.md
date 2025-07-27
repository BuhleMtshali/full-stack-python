# 🐍 Day 1 — Hello Python World! 🌍💻

## 📅 Date: July 1, 2025  
## 🔥 Level: Beginner (Day 1 of 100)

---

## 🎯 Today's Mission

Kickstart my full-stack Python dev journey with the absolute basics:
- What the heck is Python?
- Writing my first line of code!
- Understanding the Python workflow
- 🧠 Input, output, variables, and comments

---

## 📘 Resources Used

| Resource | Section |
|---------|---------|
| **Python Crash Course (3rd Edition)** | Chapter 1: Getting Started |
| **Automate the Boring Stuff with Python** | Chapter 1: Python Basics |
| **YouTube** | [Programming with Mosh - Python in 1 Hour](https://youtu.be/kqtD5dpn9C8) |

---

## 🛠️ What I Learned

- How to install Python ✅  
- Running Python in terminal vs. writing in `.py` files 🧪  
- `print()` is how you make your code speak 📣  
- Variables are like containers for data 🧺  
- Comments help humans read code (`# this is a comment`) 👁️  
- You don’t have to semicolon everything here 😭🙏

---

## 🧪 Mini Project of the Day: "Say Hello, Python!" 🧑🏾‍🚀

**Goal**: Write a Python script that:
1. Greets the user using their name 🤗
2. Asks their age and gives a cute reply 🎂
3. Tells them what year they’ll turn 100 😮‍💨

### Example Output:

Hey there, what's your name? 👉 Buhle
Awesome, Buhle! How old are you? 👉 21
Wow Buhle! You’ll turn 100 in the year 2104 🔥🔥🔥


💭 Reflections
- Honestly, this was kinda fun! 😄

- I kept typing Print instead of print() — classic noob mistake 😩

- Starting small feels good. No pressure, just vibes.

🚀 What's Next?
➡️ Day 2: Variables, Data Types & String Magic!
We gon’ vibe with strings, numbers, and start flexin’ with f-strings and formatting 🧪🧃

💬 “Start where you are. Use what you have. Do what you can.” — Arthur Ashe
Let’s get it, Day 1 ✅


### 🐍 Code Snippet:

```python
# Simple intro program - Day 1 🐍
from datetime import datetime

name = input("Hey there, what's your name? 👉 ")
age = int(input(f"Awesome, {name}! How old are you? 👉 "))
current_year = datetime.now().year
year_turn_100 = current_year + (100 - age)

print(f"Wow {name}! You’ll turn 100 in the year {year_turn_100} 🔥🔥🔥")


# 📆 Day 2: Mini Age Calculator 👶🏾➡️🧓🏾

Welcome to Day 2 of my 🔥 Full-Stack Python Journey!  
Today’s project is a cute but clever little **Mini Age Calculator** built with Python's `datetime` module.

---

## 🚀 What This Does

You enter your name, year and month of birth — and boom 💥 — it tells you exactly how old you are in **years and months**. Like:

> _"Okay Buhle, you are 24 years and 6 months old 🎁"_

Because why settle for *just* your age in years, when you can get the ✨full tea✨?

---

## 🧠 What I Learned

- How to use Python's `datetime` module 🕰️  
- Creating date objects using `datetime(year, month, day)`  
- Subtracting dates to calculate age 📉  
- Handling negative month differences like a boss 😎  
- Adding personality to my Python prompts (yes, it matters!)

---

## 💡 Code Highlights

```python
if months_diff < 0:
    years_diff -= 1
    months_diff += 12

👆 This part right here? It adjusts the age if the user’s birthday hasn’t happened yet this year.
Without it, your calculator would be out here LYING. 💅


##🧪 Sample Run
--------- Welcome to the Mini Age Calculator🍄 --------
Enter your name: Buhle  
Great, What year were you born in Buhle: 2000  
What month were you born in ? (1-12): 1  
Okay Buhle, You are 25 years and 6 months old 🎁

##📂 Folder Structure
📁 day-02-age-calculator/
├── age_calculator.py
└── README.md ← you're reading it 👀

##🛠️ Tools Used
- Python 3 🐍

- datetime module 🗓️

- A sprinkle of ✨vibes✨

##💬 Thoughts
This was fun and a great warmup!
It's simple, but it lays the foundation for date manipulation in real-world apps — from calendars to birthday reminders to age gates on websites.

##📌 Status
✅ Completed and committed
🗂️ Saved under /day-02-age-calculator
🔥 Part of my 100 Days of Code Challenge

##🧚🏾 Quote of the Day
"Every line of code is a seed for future greatness." 🌱
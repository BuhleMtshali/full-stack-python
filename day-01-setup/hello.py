#importing the date
from datetime import datetime

name = input('Enter your name: ');
age = int(input(f"Awesome, {name}! How old are you?: "))

current_year = datetime.now().year
year_turn_100 = current_year + (100 - age)

print(f"Wow {name}! You'll turn 100 in the year {year_turn_100} 🔥")
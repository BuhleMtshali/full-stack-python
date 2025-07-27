from datetime import datetime

print('--------- Welcome to the Mini Age Calculator🍄 --------')
name = input('Enter your name: ')
year = int(input(f'Great, What year were you born in {name.title()}: '))
month = int(input('What month were you born in ? (1-12): '))

#getting today's date
today = datetime.now()

#creating the birthday object
birth_date = datetime(year, month, 1)

#calculating the difference in months
years_diff = today.year - birth_date.year
months_diff = today.month - birth_date.month

#adjusting if the birthday hasn't cum yet
if months_diff < 0:
    years_diff -= 1
    months_diff += 12

print(f"Okay {name.title()}, You are {years_diff} years and {months_diff} months old🎁")

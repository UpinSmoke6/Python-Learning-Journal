import datetime # I wanted to have fun and import the actual year always.

name = input('What is your name? ') # Input user's name
age = int(input('What is your age? ' )) # Input user's age

now = datetime.datetime.today().strftime('%Y') # I googled this AND only took the year, not day or month
current_year = int(now) - age # current year is 2025 - age. Changed now into an integer.

print('Hello', name, '! You were born in ', current_year) # Prints inputs.
numbers = [0, 1, 2, 3, 4]
double_numbers = []

for number in numbers:
    double_numbers.append(number * 2)

print(double_numbers)

double_numbers = [number * 2 for number in numbers]

# This code below is equivalent to the top code
double_numbers1 = [number * 2 for number in range(5)]
print(double_numbers1)

# list to create a new list with string
friend_ages = [22, 31, 35, 37]
age_strings = [f"My friend is {age} years old." for age in friend_ages]
print(age_strings)

#lower case
names = ["Rolf", "Bob", "Jen"]
lower = [name.lower() for name in names]
print(lower)

# User input in list
friend = input("Enter your friends name: ")
friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
friends_lower = [name.lower() for name in friends]

if friend.lower() in friends_lower:
    friend_titlecased = friend.title()
    print(f"{friend.title()} is one of your friends.")


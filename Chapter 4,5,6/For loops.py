friends = ["Rolf", "Jen", "Anne"]

for friend in friends: # Starts with Rolf, then Jen, then Anne
    print(friend)

elements = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]
for index in elements: # Prints "Hello, world" 10 times
    print(f"Hello, world!")

for index in range(10): # 10 times repeat
    print(index) //

students = [
    {"name": "Rolf", "grade": 90},
    {"name": "Bob", "grade": 78},
    {"name": "Jen", "grade": 100},
    {"name": "Anne", "grade": 80},

]

for student in students: # once for each value
    name = student["name"]
    grade = student["grade"]

    print(f"{name} has a grade of {grade}.")
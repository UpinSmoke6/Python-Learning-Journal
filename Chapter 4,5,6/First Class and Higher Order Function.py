"""def greet():             #First-Class Function
    print('Hello')

hello = greet # Greet function equals hello function

hello() # Newly assigned
"""

"""

def before_and_after(func):     ## Higher order function
    print("Before...")
    func()
    print("After...")

def greet():
    print("Hello!")

before_and_after(greet)         

"""

operations = {
    "average": lambda seq: sum(seq) / len(seq),
    "total": lambda seq: sum(seq),
    "top": lambda seq: max(seq)
}

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)}
    ]

for student in students:
    name = student['name']
    grades = student["grades"]

    print(f"Student: {name}")
    operation = input("Enter 'average', 'total', or 'top':")

    result = operations[operation](grades)
    print(result)
age = int(input("Enter your age: "))
can_learn_programming = age > 0 and age <150

print(f"You can learn programming: {can_learn_programming}")

# working?

age = int(input("Enter your age: "))
usually_not_working = age < 18  and age > 65

print(f"At {age}, you are usually not working:"
      f"{usually_not_working}")

name = input("Enter your name: ")
surname = input("Enter your surname: ")

greeting = name or f"Mr. {surname}"
print(greeting)
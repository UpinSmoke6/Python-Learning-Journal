#Input Function!
my_name = "Jose"
your_name = input("Enter your name: ")

print(f"Hello {your_name}. My name is {my_name}")

# Age as input age as integer.
age = input("Enter Your age ")
age_num = int(age)
print(f"You have lived for {age_num * 12} months.")

# age inside brackets run first
age = int(input("Enter your age: "))
print(f"You have lived for {age * 12} months.")

#separate months into it's own defintion
age = int(input("Enter your age "))
months = age * 12
print(f"You have lived for {months} months.")
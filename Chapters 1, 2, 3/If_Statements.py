friend = "Rolf"
user_name = input("Enter your name: ")

if user_name == friend:   #if statement and if friend = user_name then... print.
    print("Hello, friend!")
else:
    print("Hello, stranger!")

print(bool(5)) # is true
print(bool(0)) # is false

name = input("Enter your name here: ")

print(bool(name))

if name:
    print("We don't know your name")
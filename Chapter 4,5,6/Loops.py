user_input = input("Do you wish to run the program? (Yes/No): ")

while user_input == "Yes":
    print(f"We are running") # prints You're Learning indefinitely.
    user_input = input('Do you wish to run the program? (Yes/No): ') # 'Yes' input continues loop
    is_learning = user_input == "Yes"

print(f"We stopped Running")


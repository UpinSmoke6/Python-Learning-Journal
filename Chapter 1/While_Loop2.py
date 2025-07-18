user_input = input("Do you wish to run the program? (Yes/no): ")  # Repeats unlimited amount of times until user input

while user_input == "yes":
    print("We're running!")
    user_input = input("Do you with to run the program? (Yes/no): ")

print("We've stopped running.")
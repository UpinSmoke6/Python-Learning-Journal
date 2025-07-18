is_learning = True

while is_learning:                                  # Loop repeats until anything but 'yes' is inputted
    print("You're Learning!")
    user_input = input("Are you still learning? ")
    is_learning = user_input == "yes"
user_input = input()
tokens = user_input.split()

# Convert to integers
my_list = []
for token in tokens:
    my_list.append(int(token))

# Determine list
my_list.sort()
for i in my_list[:]:
    if i < 0:
        my_list.remove(i)
print(*my_list)



""" 
This is google's Solution... The top one is my solution, both are incorrect by zybooks.

# Take user input
user_input = input("Enter numbers separated by spaces: ")

# Split input into tokens and convert to integers
tokens = user_input.split()
my_list = [int(token) for token in tokens]

# Sort the list
my_list.sort()

# Remove negative numbers
my_list = [i for i in my_list if i >= 0]

# Print the resulting list
print(*my_list)

"""
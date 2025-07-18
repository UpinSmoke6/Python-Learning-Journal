# TODO: Finish reading another word and an integer into variables.
# Output all the values on a single line
favorite_color = input()
pet_name = input()
number = int(input())

print(f'You entered:', favorite_color, pet_name, number)
# TODO: Output two password options
password1 = favorite_color + '_' + pet_name # displays new password
password2 = str(number) + favorite_color + str(number) # displays second new password

print(f"\nFirst password: {password1}")
print(f"Second password: {password2}")
# TODO: Output the length of the two password options
LengthP1 = len(password1)
LengthP2 = len(password2)

print(f'\nNumber of characters in {password1}: {LengthP1}')
print(f'Number of characters in {password2}: {LengthP2}')
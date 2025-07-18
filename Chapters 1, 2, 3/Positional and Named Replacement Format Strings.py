first_name = 'Cardi'
last_name = 'B'

# Empty replacement fields infer their position based on order of values format()
print("{}'s last name is {}".format(first_name, last_name))
# Numbers in replacement fields indicate the position of the value in format()
print("{1}'s first name is {0}".format(first_name, last_name))
# Name replacement fields indicate a named keyword from format()
print("{first} {last}? More like {first} {other}".format(first = first_name, last=last_name, other = 'Z'))

# Printing a string
user_word = input()
user_number = int(input())

'{0},{1}'.format(user_word, user_number)
print('{0},{1}'.format(user_word, user_number))
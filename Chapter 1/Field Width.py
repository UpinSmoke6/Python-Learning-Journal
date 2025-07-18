format_string = '{name:16}{goals:8}'


print(format_string.format(name='Player Name', goals='Goals')) # Inserted into the leftmost part of the 16 Character
                                                               # wide field. 'Goals' is inserted at leftmost part of the
                                                               # second 8-character wide field.

print('-' * 24)                                                # Prints '-' 24 times

# inserting Strings into field.
print(format_string.format(name='Sadio Mane', goals=22))

print(format_string.format(name='Gabriel Jesus', goals=7))
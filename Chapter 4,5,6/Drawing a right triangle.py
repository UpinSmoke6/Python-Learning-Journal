triangle_char = input('Enter a character:\n')
triangle_height = int(input('Enter triangle height:\n'))
print('')

for i in range(1, triangle_height + 1): # Starts at the 2nd value of height and adds plus one to triangle height each
                                        # iteration.
    for j in range(i):                  # The horizontal component prints triangle_character
        print(triangle_char, end=' ')
    print()
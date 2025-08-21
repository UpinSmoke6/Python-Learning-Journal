def print_total_inches(feet, inches):               # Function defined in terms of feet and inches.
    num_inches = feet * 12                          # Converting inches into feet.
    total_inches = num_inches + inches              # Adding and totalling.
    print('Total inches: {}'.format(total_inches))  # Printing
feet = int(input())                                 # Required input
inches = int(input())                               # Required input.
print_total_inches(feet, inches)                    # Total inches
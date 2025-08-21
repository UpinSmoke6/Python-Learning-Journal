num_rows = int(input())
num_cols = int(input())

# Note 1: You will need to declare more variables
# Note 2: Place end=' ' at the end of your print statement to separate seats by spaces
row = 1 # Start here
while row <= num_rows: # outer loop
    col = 0
    while col <= num_cols: # inner loop
        print(f'{row}{chr(ord("A") + col)}', end=' ')
        col += 1
    row += 1
print()
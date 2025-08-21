num_rows = int(input('Enter rows:'))
num_cols = int(input('Enter columns:'))

while num_rows <= 0:                # Value validation
    num_rows = int(input())
while num_cols <= 0:                # Value validation
    num_cols = int(input())
for i in range(num_rows):           #Height
    for j in range (num_cols):      #Width
        print('*', end=' ')
    print()
num1 = int(input()) # input 1
num2 = int(input()) # input 2
num3 = int(input()) # input 3

output = num1 if (num1 < num2 < num3) else num2 if (num2 < num1 < num3) else num3 if (num3 < num1 < num2) else num2
#conditional statements
print(int(output)) # outputs smallest number
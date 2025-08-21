num_resistors = 5
resistors = []
voltage_drop = []

print( '%d resistors are in series.' % num_resistors)
print('This program calculates the'),
print('voltage drop across each resistor.')

input_voltage = float(input('Input voltage applied to circuit: '))
print (input_voltage)

print('Input ohms of {} resistors'.format(num_resistors))
for i in range(num_resistors):
    res = float(input('{})'.format(i + 1)))
    print(res)
    resistors.append(res)

#  Calculate current
current = input_voltage / sum(resistors)

# Calculate voltage drop over each resistor
# ...

# Print the voltage drop per resistor
# ...



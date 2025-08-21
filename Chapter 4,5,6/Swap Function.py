def swap(values_list):                                                      # defines swap
    values_list[-1], values_list[0] = values_list[0], values_list[-1]       # last and first and first and last swap


values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
swap(values_list)

print(values_list)
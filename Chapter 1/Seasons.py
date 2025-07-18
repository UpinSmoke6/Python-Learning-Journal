input_month = input()
input_day = int(input())

month_to_num = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5,
    'June': 6, 'July': 7, 'August': 8, 'September': 9,
    'October': 10, 'November': 11, 'December': 12
}

month = month_to_num[input_month]
if input_month not in month_to_num:
    print('Invalid')
elif (month == 3) and (input_day <= 20): #beginning spring
    print('Winter')
elif (month == 6) and (input_day >= 21): # cutoff for spring
    print('Summer')
elif (month == 6) and (input_day <= 31): # beginning for summer
    print('Summer')
elif (month == 9) and (input_day <= 21): #cutoff for summer
    print('Summer')
elif (month == 9) and (input_day >= 22): #Beginning for Autumn
    print('Autumn')
elif (month == 12) and (input_day <= 20): # cutoff for Autumn
    print('Winter')
elif (month == 12) and (input_day >= 21): # beginning Winter
    print('Winter')
elif (month == 3) and (input_day > 20):
    print('Spring')

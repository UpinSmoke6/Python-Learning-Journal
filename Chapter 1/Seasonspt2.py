input_month = input().capitalize()
input_day = int(input())

month_to_num = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5,
    'June': 6, 'July': 7, 'August': 8, 'September': 9,
    'October': 10, 'November': 11, 'December': 12
}

# Validate month
if input_month not in month_to_num:
    print("Invalid")
if input_day > 31:
    print('Invalid')
else:
    month = month_to_num[input_month]

    # Determine season
    if (month == 3 and input_day >= 21) or (month in [4, 5]) or (month == 6 and input_day <= 20):
        print("Spring")
    elif (month == 6 and input_day >= 21) or (month in [7, 8]) or (month == 9 and input_day <= 21):
        print("Summer")
    elif (month == 9 and input_day >= 22) or (month == 9 and input_day != 31) or (month in [10, 11]) or (month == 12 and input_day <= 20):
        print("Autumn")
    elif (month == 9 and input_day >= 31):
        print('Invalid')
    print("Winter")
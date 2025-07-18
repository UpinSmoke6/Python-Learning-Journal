# calculating averages
grades_list = [80, 75, 90, 100] # use for ultimate freedom
grades_tuple = (80, 75, 90, 100) # use if no adding
grades_set = {80, 75, 90, 100}   # only for comparisons


total = sum(grades_list)
length = len(grades_list)

average = total / length

print(average)

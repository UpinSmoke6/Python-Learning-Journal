exam1_grade = float(input('Enter score on Exam 1 (out of 100):\n'))
exam2_grade = float(input('Enter score on Exam 2 (out of 100):\n'))
exam3_grade = float(input('Enter score on Exam 3 (out of 100):\n'))
# Average the exams by weight:
overall_exams = (((exam1_grade * (1 / 300)) + (exam2_grade * (1 / 300)) + (exam3_grade * (1 / 300))) * 100)

print('Your overall exam grade is: ', overall_exams)

prog1_grade = float(input('Enter Score on Assignment 1 (Out of 50):\n'))
prog2_grade = float(input('Enter Score on Assignment 2 (Out of 50):\n'))
prog3_grade = float(input('Enter Score on Assignment 3 (Out of 50):\n'))
prog4_grade = float(input('Enter Score on Assignment 4 (Out of 50):\n'))
# Average in-class work with weight:
overall_progs = ((((prog1_grade * (1 / 200)) + (prog2_grade * (1 / 200)) + (prog3_grade * (1/ 200)) + (prog4_grade * (1/200)))) * 100)
print('Your overall program grade is:', overall_progs)
# This is the weight each grade has on overall grade:
print('Your overall class grade is: ', (0.6 * overall_exams) + (0.4 * overall_progs))
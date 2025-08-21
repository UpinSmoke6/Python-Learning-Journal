
""" def hello_func(greeting, name = 'you'):
    return '{}, {}'.format(greeting, name) # required argument

## hello_func() # functions allow certain code in certain statements. Easier to code in multiple locations

## print(hello_func('Hi', name = 'Derek'))"""

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['math', 'art']
info = {'name': 'John', 'age': 22}

student_info(*courses, **info)

student_info('Math', 'Art', name = 'John', age = 22)
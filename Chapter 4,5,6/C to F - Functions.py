def c_to_f():                   # Define function
    f = temp_c * (9 / 5) + 32   # conversion
    c = temp_c                  # Yes
    return f  # FIXME: Finish


temp_c = float(input())         # Input for Celsius
temp_f = temp_c * (9 / 5) + 32  # Fahrenheit

c_to_f()                        # Call function
# temp_f = ??


print('Fahrenheit:', temp_f)    # prints

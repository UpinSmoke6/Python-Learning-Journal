for n in range(2, 10):
    for x in range(2, n): # This line will never break if prime. Only to the sqrt(x)
        if n % x == 0: # if remainder = 0
            print(f"{n} equals {x} * {n/x}")
            break
    else:
        print(f"{n} is a prime number.")
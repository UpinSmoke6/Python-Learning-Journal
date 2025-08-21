cars = [ "ok", "ok", "ok", "ok", "ok", "ok"] # Add or remove "faulty" to check program's use.

for status in cars:
    if status == 'faulty':
        print(f"Stopping the production line!")
        break
    print(f"This car is {status}.")
    print("Shipping new car to customer!")
else: # can be added to loops.
    print("All cars built successfully. No Faulty cars!")
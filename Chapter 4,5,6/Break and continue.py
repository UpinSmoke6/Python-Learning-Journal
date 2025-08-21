cars = [ "ok", "ok", "ok", "ok", "faulty", "ok", "ok"]

for status in cars: # checks lists status
    if status == "faulty":
        print("Stopping the production line!")
        break # stops loop
    print(f"This car is {status}")

cars1 = [ "ok", "ok", "ok", "ok", "ok", "ok", "faulty"]

for status1 in cars1: # checks lists status
    if status1 == "faulty": # if status is 'faulty'
        print("Faulty car found, skipping...")
        continue # continues loop
    print(f"This car is {status1}")
    print("Shipping new  car to customer!")
currencies = 0.8, 1.2
usd, eur = currencies

friends = [("Rolf", 25), ("Anne", 37), ("Charlie", 31), ("Bob", 22)]

for name, age in friends:
    #name, age = friends ^^^^^^^^^^^^^^^^^^^^^^^^^

    #name = friends[0] # ^  Equivalent to line 6.^
    #age = friends[1] # ^^^^^^^^^^^^^^^^^^^^^^^^^^

    print(f"{name} is {age} years old.")
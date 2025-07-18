cents = int(input()) # enter amount of cents
if cents == 0:
    print('No change')
else:
    dollars = cents // 100 # divides into dollars
cents %= 100
quarters = (cents ) // 25 # divide into quarters
cents %= 25
dimes = (cents) // 10 # into dimes
cents %= 10
nickles = (cents) // 5 # into nickles
cents %= 5
pennies = (cents) // 1 #into pennies
pennies = cents


if dollars > 0:
    print(f"{dollars} Dollar{'s' if dollars > 1 else ''}")
if quarters > 0:
    print(f"{quarters} Quarter{'s' if quarters > 1 else ''}")
if dimes > 0:
    print(f"{dimes} Dime{'s' if dimes > 1 else ''}")
if nickles > 0:
    print(f"{nickles} Nickel{'s' if nickles > 1 else ''}")
if pennies > 0:
    print(f"{pennies} Penn{'ies' if pennies > 1 else 'y'}")

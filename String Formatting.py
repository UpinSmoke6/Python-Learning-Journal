from json import JSONEncoder

age = 34

#age_as_string = str(age)
# print("You are " + age_as_string) #delete this line
print(f"You are {age}") # 3.6 and above python version.

# Use this template as your go-to.
name = "Jose"
greeting = f"How are you, {name}?"
print(greeting)

# Using one string for two names. Final greeting is used by Bob and Jose

name = "Jose"
final_greeting = "How are you, {}?"
jose_greeting = final_greeting.format(name)
print(jose_greeting)

name = "Bob"
bob_greeting = final_greeting.format(name)
print(bob_greeting)

# if using variables specifically

name = "Jose"
final_greeting = "How are you, {name}?"
jose_greeting = final_greeting.format(name="Jose")
print(jose_greeting)

name = "Bob"
bob_greeting = final_greeting.format(name="bob")
print(bob_greeting)
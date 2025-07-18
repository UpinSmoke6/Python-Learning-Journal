# keys and values

friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

print(friend_ages["Rolf"])

friend_ages["Bob"] = 20 # adds key
friend_ages["Rolf"] = 25 # changes age of rolf to 25

print(friend_ages)

# Use a list or tuple of dictionary
friends = (
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27}
)

# stores information for easy access.

print(friends[0]["name"])
print(friends[1]["name"])
print(friends[2]["name"])

# dict function

friends2 = {"Rolf": 24, "Adam": 30, "Anne": 27}
friend_ages2 = dict(friends2)
print(friend_ages2)
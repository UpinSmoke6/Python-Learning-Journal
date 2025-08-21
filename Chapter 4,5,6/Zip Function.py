# Set and Dictionary Comprehension.py second code re-written. Use this for simpler list creation.
friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]
# replaces the [i] function
long_timers = dict(zip(friends, time_since_seen))
#{
#    friends[i]: time_since_seen[i]
#    for i in range(len(friends)) # range is length of list of friends
#    if time_since_seen[i] > 5 # only when greater than 5
#}

print(long_timers)
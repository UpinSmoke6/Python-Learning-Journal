art_friends = {"Rolf", "Anne", "Jen"} # list A
science_friends = {"Jen", "Charlie"} #list B

art_but_not_science =  art_friends.difference(science_friends) # list A minus list B
science_but_not_art = science_friends.difference(art_friends) # list B minus list A

print(art_but_not_science)
print(science_but_not_art)

not_in_both = art_friends.symmetric_difference(science_friends) # elements appearing only once
art_and_science = art_friends.intersection(science_friends) # elements similar to both lists

print(not_in_both)
print(art_and_science)

all_friends = art_friends.union(science_friends) # unifies both lists

print(all_friends)
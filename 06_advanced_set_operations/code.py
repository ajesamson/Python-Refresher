friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

# set - difference
local_friend = friends.difference(abroad)
print(f"Local friends: {local_friend}")

# set - intersection
science = {"maths", "biology", "physics"}
art = {"geography", "maths", "social studies"}
subject = science.intersection(art)
print(f"Similar subject for science and art are: {subject}")

# set - union
school = science.union(art)
print(f"All school subjects: {school}")

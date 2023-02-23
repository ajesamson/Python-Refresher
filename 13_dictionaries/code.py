# DICTIONARIES
# key - value pair 
friend_ages = { "Rolf": 24, "Adam": 30, "Anne": 27}

#access item
print(friend_ages["Adam"])
for f in friend_ages:
    print(f)
    print(friend_ages[f])
# - iterate key, value pair
for k, v in friend_ages.items():
    print(f"Key: {k}, Value: {v}")

# item exists
print(f"Is grace in friend age list? {'grace' in friend_ages}")
average_age = sum(friend_ages.values()) / len(friend_ages.values())
print(f"Average age is {average_age}")

# change item
friend_ages["Adam"] = 40
print(friend_ages["Adam"])

# add an item
friend_ages["Bob"] = 35
print(friend_ages)

# list of dictionaries
friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27}
]
for friend in friends:
    print(friend)
print(f"Friend at index 1: {friends[1]}")

# check if value exists in keys
print("Bob" in friend)

# LIST COMPREHENSION
# Note that new list are always generated
# after using list comprehension

# Scenario 1 - Without condition 
# QS - double the items in a list
# [ result iteration ]
numbers = [1,3,5]
result1 = []

# using loop
for number in numbers:
    result1.append(number * 2)
print(f"Doubled number using for loop: {result1}")
# using list comprehension
result2 = [n * 2 for n in numbers]
print(f"Doubled number using list comprehension: {result2}")

# Scenario 2 - With condition
# QS - Extract names starting with 's' in a list
friends = ["Sam", "Paul", "Kobe", "Samantha"]
starts_s_loop = []

# using loop
for friend in friends:
    if friend.startswith("S"):
        starts_s_loop.append(friend)
print(f"Scenario 2 using loop: {starts_s_loop}")
# using list comprehension
starts_s = [f for f in friends if f.startswith("S")]
print(f"Scenario 2 using list comprehension: {starts_s}")





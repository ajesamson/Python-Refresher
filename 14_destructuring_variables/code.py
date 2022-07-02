t = 5, 11 # equivalent to t = (5, 11) - tuple initialization
x, y = t


people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 22, "Lecturer")]
for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

# To ignore a value, use an underscore
user = ("Bob", 42, "Mechanic")
name, _, profession = user

# collecting group of items use *
head, *tail = [1, 2, 3, 4, 5]
print(f"head: {head}, tail: {tail}")
# reversing the collection
*head, tail = [5, 6, 7, 8, 9]
print(f"head: {head}, tail: {tail}")

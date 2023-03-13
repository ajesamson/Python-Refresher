# Description - Mutability in python

# a and b are just names that refer to the same object
# All things a mutable in python unless there is no way to change it
# (such as a tuple, string, integer, float and boolean)
a = []
b = a

print(id(a))
print(id(b))

a.append(1)

print(a)
print(b)
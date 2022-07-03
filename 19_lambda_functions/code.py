# LAMBDA FUNCTION
# They are function without names and only used to return 
# Better to define a function that use a lambda function due to readability

def add(x, y):
    return x + y

# in lambda expression
lambda x, y: x + y
# to make the lambda function have a name
sum = lambda x, y: x + y
print(sum(5, 7))
# without name
(lambda x, y: x + y)(5, 7) # not very common usage

def double(x):
    return x * 2

sequence = [1, 3, 5]
# with list comprehension
doubled = [s * 2 for s in sequence]
# for simplification
doubled = [double(s) for s in sequence]
# replacing with lambda function instead of defining a new function
doubled = [(lambda s: s * 2)(s) for s in sequence]
# using a map
doubled = map(double, sequence)
# using a map with lambda
doubled = list(map(lambda s: s * 2, sequence))
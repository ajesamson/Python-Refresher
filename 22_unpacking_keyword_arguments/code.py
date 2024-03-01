# UNPACKING KEYWORD ARGUMENTS

# collects keyword arguments into a dictionary
def named(**kwargs):
    print(kwargs)

# if the variables is not a dictionary, an error is thrown
named(name="Bob", age=25) 

# unpack dictionary into named argument
print("======unpack dictionary======")
def named_unpack(name, age):
    print(name, age)

details = {"name": "Bob", "age": 25}
named_unpack(**details)

print("==================")
def print_nicely(**kwargs):
    named(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}: {value}")

print_nicely(name="Bob", age=25)

print("==================")
# accepting unlimited number of arguments
# so we can pass them to another function
def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 3, 5, name="Bob", age=25)


# Passed arguments must always be a dictionary.
# If not, an exception would be thrown
# def doNotExecute(**kwargs):
#     print(kwargs)

# doNotExecute("Bob", 25)
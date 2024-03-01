# FUNCITON - RETURN VALUES
# By default, NONE is returned from a function
# if no explicit return is made

def add(x, y):
    print(x + y)

result = add(5, 8)
print(result)

def add_1(x, y):
    print(x + y)
    return x + y # note that return terminates the function

# Avoid returning different type of data unless when necessary
def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"
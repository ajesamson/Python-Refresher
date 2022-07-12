# UNPACKING ARGUMENTS
# Collecting multiple arguments into a single variable
# Collection is made into a tuple

def multiply(*args):
    total = 1
    print(args)
    for arg in args:
        total *= arg
    
    return total

print(multiply(1,2,3,4,5))

# Unpacking List 
# - there must be same number of parameters
# as the list count sent
def add(x, y):
    return x + y

nums = [3, 5]
print(add(*nums))

# Unpacking dictionaries
nums_dic = {"x": 15, "y": 25}
print(add(nums_dic["x"], nums_dic["y"]))
# passing the parameter as named argument
print(add(**nums_dic))

# combining variable packing and named argument

def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()"

print(apply(1, 3, 5, 7, operator="*"))

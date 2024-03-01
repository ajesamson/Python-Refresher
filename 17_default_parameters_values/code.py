# Note - 
# 1. no space between equal and value for default parameters
# 2. Default parameters must go at the end in function definition
def add(x, y=8):
    print(x + y)

add(5)
add(x=10) # still valid
add(x=10, y=20) # still valid
# add(y=15) is invalid because x is required

print("Testing change of default value...")
default_y = 3

def new_add(x, y=default_y):
    sum = x + y
    print(sum)

add(2)

# changing the default value would not impact initial function definition
default_y = 4
add(2)

# Arguments
# When arguments types are mixed, positional argument goes
# before a keyword argument

# 1 - positional argument
# parameters are determined by position
# the first parameter would be stored in surname
# while the second would be the firstname
# Note: surname and firstname are parameters
def greet(surname, firstname):
    print(f"Hello, {firstname} {surname}")

# Note: Tailor and Smith are arguments
greet("Tailor", "Smith")

# 2 - keyword (or named) argument
# The arguments must tally with the function's parameter
def divide(dividend, divisor):
    if divisor != 0:
        print(dividend / divisor)
    else:
        print("Division by zero not allowed")

# Note: there should be no space between the arg and equal
# wrong => divisor = 0
divide(divisor=0, dividend=15)
# mixing parameters types but positional argument
# must come first, otherwise, errors are thrown
divide(25, divisor=5) 
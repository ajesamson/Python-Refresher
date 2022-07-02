# FUNCTIONS
# Note 
#  1. Do not re-use function name
#  2. variables are local to a function

# function definition
# Not executed until called
def hello():
    print("Hello!")

# function call
hello()

def user_age_in_seconds():
    user_age = int(input("Enter you age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}")

print("Welcome to the age in seconds program!")
user_age_in_seconds()

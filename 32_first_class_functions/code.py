# Description - First Class Functions
# A first class function is a function that can be 
# passed as an argument to another function, returned 
# from another function, and assigned to a variable.

def divide(dividend: float, divisor: float) -> float:
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor

def calculate(*values: float, operator: str) -> float:
    return operator(*values)

result = calculate(20, 4, operator=divide)
print(result)


from operator import itemgetter

# Example 2
def search(sequence:list, expected:str, finder) -> str:
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Could not find an element with {expected}.")

friends = [
    {"name": "Tiger Woods", "age": 45},
    {"name": "Roger Federar", "age": 34},
    {"name": "Tyson Gayle", "age": 30}
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends, "Tiger Woods", get_friend_name))
print(search(friends, "Tiger Woods", lambda friend: friend["name"])) # using lambda function
print(search(friends, "Tiger Woods", itemgetter("name"))) # itemgetter - function that creates other function

# print(search(friends, "Bod Woods", get_friend_name))
def divide(dividend, divisor) -> float:
    return dividend / divisor

print("mymodule.py: ", __name__)

# Warning: This will not work in python2 without having
# __init__.py file in the folder you are importing from
import libs.mylib
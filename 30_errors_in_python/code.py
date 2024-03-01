def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    
    return dividend / divisor

grades = []
print("Welcome to the average grade program.")
try:
    average = divide(sum(grades), len(grades))
    print(f"The average grade is {average}.")
except ZeroDivisionError as e:
    print(e)
    print("There are no grades yet in your list")
else: # run if there is no exception
    print("-- All student average calculated --")
finally: # run irrespective of whether an exception is raised or not
    print("-- End of student average calculation --")




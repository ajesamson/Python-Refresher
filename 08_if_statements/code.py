# user lower() to ensure your program works irrespective of what the user types
day_of_week = input("What day of the week is it today? ")

if day_of_week == "monday":
    print("Have a great start to your week!")
elif day_of_week == "tuesday":
    print("It's Tuesday.")
else:
    print("Full speed ahead!")

print("This always runs.")
# DICTIONARY COMPREHENSIONS
users = [
    (0, "Bob", "password"),
    (0, "Rolf", "bob123"),
    (0, "Jose", "longp4assword"),
    (0, "username", "1234")
]

# creating a mapping between each user their details
# this saves having to create a method that loop through
# 
username_mapping = {user[1]: user for user in users}

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password == password_input:
    print("Your details are correct")
else:
    print("Your details are incorrect")
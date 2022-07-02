# List - you can add or remove an item
# Printing is orderly by index - l[0]
# Add items with append - l.append("Toad")
l = ["Bob", "Rolf", "Anne"]

# tuple - you cannot add or remove item
# printing is orderly by index t[0]
t = ("Bob", "Rolf", "Anne")
# Note: bracket around tuple is not compulsory
# it is only necessary to avoid confusion especially with a list
# by clearly indicate you want a tuple and not ordinary list
# tl = [("female", "male"), ...] as compared to
# tl = ["female", "male", ... ]
sex = "female", "male", "not specified"
print(sex)

# sets - you can add or remove items
# Printing is not orderly
# No subscript notation - s[2]
# Add items is Add - s.add("Toad")
# Empty set as set() - s = set()
s = {"Bob", "Rolf", "Anne"}

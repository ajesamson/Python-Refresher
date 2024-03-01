# boolean operations - ==, <=, >= <, >, is
print(f"5 == 5: { 5 == 5}") 
print(f"5 <= 5: { 5 <= 5}") 
print(f"5 >= 5: { 5 >= 5}") 
print(f"5 < 5: { 5 < 5}") 
print(f"5 > 5: { 5 > 5}") 

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]
local = friends
print(f"friends == abroad: { friends == abroad }") 
# avoid using the "is"
print(f"friends is local: { friends is local }") 

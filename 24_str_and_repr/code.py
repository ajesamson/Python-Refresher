# _str_ and _repr_
# Magic methods (methods with 2 underscore on both sides) are 
# called automatically by python in some situations such as __init__

from unicodedata import name

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    # generates a string representation of an object
    # def __str__(self) -> str:
    #     return f'Person {self.name}, {self.age} years old.'
    
    # generates an unambiguous string on how to recreate original object
    def __repr__(self) -> str:
        return f'<Person("{self.name}", {self.age})>'

bob = Person("Bob", 35)
# Prints an object reference if __str__ is not defined
print(bob)
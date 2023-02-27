# _str_ and _repr_
from unicodedata import name


class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

bob = Person("Bob", 35)
print(bob)
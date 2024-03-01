from typing import List, Optional

class Student:
    # Using mutable default parameters is bad practice
    # It evaluates as when it is defined, not when it is called
    def __init__(self, name: str, grades: List[int] = []): 
        self.name = name
        self.grades = grades
    
    def take_exam(self, result: int):
        self.grades.append(result)


bob = Student("Bob")
rolf = Student("Rolf")
bob.take_exam(90)
print(bob.grades) # [90]
print(rolf.grades) # [90]

# To solve the issue
class Student1:
    def __init__(self, name: str, grades: Optional[List[int]] = None): 
        self.name = name
        self.grades = grades or []
    
    def take_exam(self, result: int):
        self.grades.append(result)

bob = Student1("Bob")
rolf = Student1("Rolf")
bob.take_exam(90)
print(bob.grades) # [90]
print(rolf.grades) # []
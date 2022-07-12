# OBJECT ORIENTED PROGRAMMING
class Student:
    # note that init can take named parameter -> (self, name, grades)
    def __init__(self) -> None: 
        self.name = "Rolf"
        self.grades = (89, 90, 93, 78, 90)

    def average_grade(self) -> float:
        return sum(self.grades) / len(self.grades)

# creating an instance
student = Student()
print(student.name)
print(student.grades)
print(student.average_grade()) # equivalent to Student.average(student)


# Class method and static method

# Instance Method
# Used when you want an action performed on class data
class ClassTest:
    # all method that uses object as first parameter
    # are called instance method
    def instance_method(self):
        print(f"Called instance_method of {self}")

test = ClassTest()
test.instance_method()

# Class Methods
# Used as factory
class ClassTest2:
    # Receives class as implicit first argument just as instance method
    # receives argument
    @classmethod
    def class_method(cls): #cls in a classmethod is the class itself
        print(f"Called class_method of {cls}")

ClassTest2.class_method() # ClassTest2.class_method(ClassTest2)

# Static Methods
# Used to place a method inside a class
class ClassTest3:
    # do not receive parameter like class and instance method
    @staticmethod
    def static_method(): 
        print(f"Called static_method")

ClassTest3.static_method()
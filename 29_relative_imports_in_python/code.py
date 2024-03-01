# Description - 29 Relative Imports in Python

# import forces subsequent statements to be suspended 
# and jumps into imported files to import before continuing
# operator.py:  libs.operations.operator
# mylib.py: libs.mylib
# mymodule.py: mymodule
# code.py:  __main__
import mymodule

print("code.py: ", __name__)

# Note: The imports above are absolute import where
# you have to define the path file is gotten from
# Relative import imports from current folder
# Avoid using relative import to make things easier 
# without import failures

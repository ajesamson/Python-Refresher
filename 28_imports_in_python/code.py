from mymodule import divide # import specific function from module

# alternative syntax:
# from mymodule import divide as div # import specific function from module and rename it
# from mymodule import * # import all functions from module
# import mymodule # import module and use it as mymodule.divide

print(divide(20, 10))

# Note: If you run this file directly, __name__ 
# (dunder name or magic method name) will be __main__.
# Python is able to identify file source using module sys
# You can include specific paths to python from terminal using:
# export PYTHONPATH=/path/to/your/module
import sys 
# prints all paths where Python looks for modules starting with the current directory
print(sys.path)

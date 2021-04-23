# A module is a file containing some python code
# A package is a folder where can be some modules

# importing module
from a_module import get_factorial, get_sum
# from a_module import *     : import all things from a_module
# import a_module            : import a_module and use module name as a prefix of all the things under a_module

print("Sum :", get_sum(5, 9))


# importing package
from a_package.calcx import get_factorial2 as fact2 # renaming imported things
# from a_package.calcx import *
# from a_package import calcx
# import a_package

print("Factorial of 6 :", fact2(6))

# importing sub package
from a_package.a_sub_package.calc import get_factorial3
# from a_package.a_sub_package.calc import *
# from a_package.a_sub_package import calc
# import a_package.a_sub_package

print("Factorial of 6 :", get_factorial3(6))


# A Folder is determined a package/sub-package, if it contains __init__.py

# Python will look these folder for module/package
import sys
print(sys.path)


# get all the attributes/method/classes names of a module
from a_package import calcx
print("a_package.calcx contains:", dir(calcx))

print(calcx.__name__) # a_package.calcx  : module name with it's package
# but if that module is called directly, __name__ will be '__main__'


# When a module/package is imported, python compile that module/package
# and put them to __pycache__ folder
# When we call a file, if there is a module imported,
# python check for it's compiled version, and then check for update by compairing last modified datetimes
# if it's the same datetime, then python loads that compiled version, by this module loads become faster
# if there is newer version of that module or no compiled version found, python complie that and then use that

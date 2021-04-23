# Here if we want to access a_sub_package or anything outside of the current package

from a_package.a_sub_package import calc # absulote (use it)
from ..a_sub_package import calc         # relative


from .calc2 import get_factorial6  # importing from the same folder/package



def get_factorial2(n):
    if n == 0:
        return 1
    r = 1
    for i in range(1, n+1):
        r *= i
    return r

# All these things are optional to use
# Use list / tuple / set etc. built-in types
# But, when working with large dataset and causing bad performance, use these


# *** Stack ***
# Stack is just like a list
# But it has a system like LIFO : Last In - First Out : Just like a pot
 
#  | **** |
#  | **** |
#  |______|

# In python, we can use built-in list for stack


# *** Queue ***
# Queue is just like a list
# But it has a system like FIFO : First In - First Out : Just like a waiting line in bank
# ---------------------------
# ***************************
# ---------------------------
# It makes inserting and removing item more efficient
from collections import deque

data = deque([]) # define deque
data.append(1)   # adding items
data.append(5)
data.append(10)
data.popleft()  # remove the first item
if not data:    # checking if it's empty
    print('data is empty')


# *** Array ***
# Array : Efficient arrays of numeric values
# More about array and all typecodes : https://docs.python.org/3/library/array.html
from array import array

num = array('i', [1, 5, 8, 6, 9]) # here, 'i' is a typecode for signed int
# so, we can only put one type of data here : adding any other data types would through error
# like list we can do most of the things here : pop(), instert(), remove() etc.

# ::: Tuple :::
# tuple is just like list but read only
# almost all the thing is judt like list. 


# defining a tuple
marks = (454, 657, 587, 345, 893) # just like list, only '[]' to '()'
marks = 454, 657, 587, 345, 893   # python will take it as a tuple
marks = tuple("Helo World")


# unpacking
marks = [45, 63, 96]
first, second, third = marks


# swaping values using tuple
x = 4
y = 6
x, y = y, x # same to : x, y = (y, x) 
# at first 'y, x' is taken as a tuple and then unpack it
# this also works same way when define more than one variable at a line
x, y = 8, 6 # take as a tuple and then unpack it


# ====================================================================================
# ====================================================================================


# ::: Set :::
# set is also like list with some difference
# set is a list of unique items

# defining a set
num = {6, 8, 9, 12, 36}                # just like list, only '[]' to '{}'
marks = set([1, 6, 9, 6, 3, 3, 4, 7])  # set from other iterables (set removes the duplicate)


# Adding item
num.add(6) # unlike list, set do not have append/insert
# Modify / Remove item
num.remove(12)
# Unlike list, set do not have index
# So, we can not access item with their index, like num[2], this will not work
# but we can iterate over the set, loop through a set etc.
for i in num:
    print(i)

has_12 = 12 in num # 12 is not in num, so it will return False


# Some mathematics
first = {3, 2, 4, 6, 7}
second = {1, 2, 4, 5}
union               = first | second  # retuns all items that is in first or second set : {1, 2, 3, 4, 5, 6, 7}
intersection        = first & second  # retuns items that is both in first and second set : {2, 4}
difference          = first - second  # retuns first set after removing items that is in second set : {3, 6, 7}
semetric_difference = first ^ second  # retuns items that is either in first or second set  : {1, 3, 5, 6, 7}

# unlike list, we can not use + or * operator in set
# first = {45, 85, 69} + {85, 32, 45}  :  this will through error

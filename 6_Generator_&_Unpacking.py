# *** Generator ***
# We used list and dict comprehension
# but in tuple, there is no comprehension
# instead of that, we can make a generator
from sys import getsizeof
import itertools

# using list comprehension
values = [x * 2 for x in range(100000)] # this gives us a list
print('Size of list      :', getsizeof(values), 'bytes') # 412236 bytes
# using generator
values = (x * 2 for x in range(100000)) # this gives us a generator
print('Size of Generator :', getsizeof(values), 'bytes') # 64 bytes

# We can see a list of 100000 elements takes 412236 bytes
# Where generator takes only 64 bytes
# size of list get increased with the size, but the generator remain constant
# So, when processing a large data, better use generator

# Using generator
for i in values:
    # do any thing
    pass
# or : list(generator)
# we can not do this for generator : len(values)
# because we don't know that how many items it gonna produce

# Just like this :
r = range(120) # this is also a generator


# Generator function with yield
# all same to the normal function without yield
# return exit the function, yield returns something and save function state for later use in iterator
def pass_generator(min_length, max_length, all_keys):
    for length in range(min_length, max_length+1):
        for i in itertools.product(all_keys, repeat=length):
            s = ''
            for ii in range(0, length):
                s += i[ii]
            yield s

for i in pass_generator(4, 6, '123'):
    print(i)


# *** UNPACKING ***
# We learned unpacking before
list1 = [5, 6, 5, 6]
dict1 = {'Rabbi': 250, 'Fahim': 180, 'Faruk': 220, 'Sami': 290}

one, two = [5, 6]
one, *two = list1
Rabbi, Fahim, Faruk, Sami = dict1

values = [*list1, *"Hello", 12, 45, *range(2, 6), 45] # [5, 6, 5, 6, 'H', 'e', 'l', 'l', 'o', 12, 45, 2, 3, 4, 5, 45]
combined = {**dict1, **{'Zayed': 300, 'Samir': 210}, 'Rokib': 150}

# Unpacking and send
def func1(name, password, *data):
    print('name and password are positional/keyword arguments')
    print('data is the tuple of rest of the positional arguments')

func1("Name", "pass", 4, "fgt", 69)
func1("hiu", *list1) # unpacking list and send as positional args

def func2(name, password, **data):
    print('name and password are positional/keyword arguments')
    print('data is the dict of rest of the keyword arguments')

func2("Name", "pass", key1=4, key2="fgt", key3=69)
func2("hiu", "fdf", **dict1) # unpacking dict and send as keyword args


def func3(name, password, *data1, **data2):
    print('name and password are positional/keyword arguments')
    print('data1 is the tuple of rest of the positional arguments')
    print('data2 is the dict of rest of the keyword arguments')

func3("Name", "pass", 58, 998, 63, key1=4, key2="fgt", key3=69)
func3("hiu", "fdf", *list1, **dict1) # unpacking list and dict and send as positional and keyword args

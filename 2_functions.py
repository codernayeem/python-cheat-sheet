# Functions
print("************* Function ***********")

# Simple function without any arguments/parameters
def say_welocme():
    return print('Welocme')

# Simple function with arguments/parameters
def say_helo(name, age):
    print('Helo', name, age)
    # this function returns None

say_helo('Nayeem', 18)         # passing args as positional args
say_helo(age=19, name='Sami')  # passing args as keyword args (if you mismatch the serial, use keywords)


def check_odd_number(n):
    return True if n % 2 else False

if check_odd_number(43):
    print(43, " is a odd number")


print("********* Default parameter **********")
# Simple function with a default arguments/parameters
def say_somethings(name, message="Welcome"):
    print(message, name)



# Type hint:
print("********* Type hint **********")
def greeting(name: str) -> str:
    # Type hints improve IDEs and linters. They make it much easier to statically reason about your code
    # The Python runtime does not enforce function and variable type annotations. They can be used by third party tools such as type checkers, IDEs, linters, etc
    # here we defined name should be str and a str will be returned
    return 'Hello ' + name
greeting("Nayeem")


# scope
print("************ Scope *************")
parent_name = "Anything" # this is a global variable

def show_parent1():
    print(parent_name) # this will print the global variable

def show_parent2():
    parent_name = "Lovely" # this will not change global variable. it will create a new local variable
    print(parent_name) # print local variable

def show_parent3():
    # we can use global variable in function
    # but cannot modify them directly
    # TO modify:
    # method 1:
    global parent_name
    parent_name = "Something" # this will change the global variable
    print(parent_name)
    # method 2:
    globals()['parent_name'] = "Something_Nothing" # this will change the global variable
    print(globals()['parent_name'])

def show_parent4(parent_name):
    print(parent_name) # this parent_name is a local variable
    # to use the global variable here
    print(globals()['parent_name']) # this will print the global variable, not the local one

    # A variable can not be both : parameter and global
    # So you can not do that here:
    # global parent_name
    # print(parent_name)

show_parent1()
show_parent2()
show_parent3()
show_parent4("Long Lasting")


l1 = [56, 87, 89, 45, 57]
d1 = {'Karim': 50, 'Rafiq': 90, 'Sabbir': 60}

# Lambda function
print("************ Lambda function *************")
# lambda function is just a one line simple anonymous function.
# It's defination ==> lambda parameter_list: expression
# lambda function is used when we need a function once and as a argument to another function
print(min(d1.items(), key=lambda item: item[1])) # returns the smallest element


# Python built-in functions/methods
print("************ Some Built-in functions *************")

print(len(l1)) # returns the length of that iterable
print(sum(l1)) # return the sum of an iterable
print(max(l1)) # returns the biggext element
print(min(l1)) # returns the smallest element
print(max(d1, key=lambda k: d1[k])) # returns the biggext element
print(min(d1.items(), key=lambda item: item[1])) # returns the smallest element

print(all([0, 1, 5])) # returns True if all the elements is True, otherwise False
print(any([0, 1, 5])) # returns True if any of the elements is True, otherwise False

print(repr('hi')) # call __repr__() for that object. Represent object
print(id(l1))     # returns a unique integer number which represents identity
print(type(56))   # returns the class type of that object

print(dir(567)) # Returns a list of the specified object's properties and methods

print(ord('A')) # 65 : Return the Unicode code point for a one-character string
print(chr(65))  # 'A' : Return a Unicode string of one character with ordina
print(abs(-62))  # 62 : Return a absolute value of a number

eval('print("hi")')         # Evaluates and executes an expression
print(eval('(58*9)+3**2'))  # Evaluates and executes an expression


print("************ All Built-in functions *************")

# abs()      Returns the absolute value of a number
# all()      Returns True if all items in an iterable object are true
# any()      Returns True if any item in an iterable object is true
# ascii()    Returns a readable version of an object. Replaces none-ascii characters with escape character
# bin()      Returns the binary version of a number
# bool()     Returns the boolean value of the specified object
# bytearray()   Returns an array of bytes
# bytes()       Returns a bytes object
# callable()    Returns True if the specified object is callable, otherwise False
# chr()         Returns a character from the specified Unicode code.
# classmethod()    Converts a method into a class method
# compile()     Returns the specified source as an object, ready to be executed
# complex()     Returns a complex number
# delattr()     Deletes the specified attribute (property or method) from the specified object
# dict()        Returns a dictionary (Array)
# dir()         Returns a list of the specified object's properties and methods
# divmod()      Returns the quotient and the remainder when argument1 is divided by argument2
# enumerate()   Takes a collection (e.g. a tuple) and returns it as an enumerate object
# eval()        Evaluates and executes an expression
# exec()        Executes the specified code (or object)
# filter()      Use a filter function to exclude items in an iterable object
# float()       Returns a floating point number
# format()      Formats a specified value
# frozenset()   Returns a frozenset object
# getattr()     Returns the value of the specified attribute (property or method)
# globals()     Returns the current global symbol table as a dictionary
# hasattr()     Returns True if the specified object has the specified attribute (property/method)
# hash()        Returns the hash value of a specified object
# help()        Executes the built-in help system
# hex()         Converts a number into a hexadecimal value
# id()          Returns the id of an object
# input()       Allowing user input
# int()         Returns an integer number
# isinstance()  Returns True if a specified object is an instance of a specified object
# issubclass()  Returns True if a specified class is a subclass of a specified object
# iter()        Returns an iterator object
# len()         Returns the length of an object
# list()        Returns a list
# locals()      Returns an updated dictionary of the current local symbol table
# map()         Returns the specified iterator with the specified function applied to each item
# max()         Returns the largest item in an iterable
# memoryview()  Returns a memory view object
# min()         Returns the smallest item in an iterable
# next()        Returns the next item in an iterable
# object()      Returns a new object
# oct()         Converts a number into an octal
# open()        Opens a file and returns a file object
# ord()         Convert an integer representing the Unicode of the specified character
# pow()         Returns the value of x to the power of y
# print()       Prints to the standard output device
# property()    Gets, sets, deletes a property
# range()       Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
# repr()        Returns a readable version of an object
# reversed()    Returns a reversed iterator
# round()       Rounds a numbers
# set()         Returns a new set object
# setattr()     Sets an attribute (property/method) of an object
# slice()       Returns a slice object
# sorted()      Returns a sorted list
# @staticmethod()    Converts a method into a static method
# str()         Returns a string object
# sum()         Sums the items of an iterator
# super()       Returns an object that represents the parent class
# tuple()       Returns a tuple
# type()        Returns the type of an object
# vars()        Returns the __dict__ property of an object
# zip()         Returns an iterator, from two or more iterators



# Decorators
print('*********** Decorators ************')

from functools import wraps

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


@star
def printer1(msg):
    print(msg)

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer2(msg):
    print(msg)

printer1("Hello")
printer2("Hello")


# Function caching
print('*********** Function caching ************')

import time
from functools import lru_cache

@lru_cache(maxsize=32)
def some_work(n):
    time.sleep(3)
    return n * 2

print('Running work')
some_work(5)
print('Calling again ..')
some_work(9) # tihs time, this run immedietly
print('finished')



# Coroutines
print('*********** Coroutines ************')

import time

def searcher():
    time.sleep(3)
    book = "Tihs is ok"

    while True:
        text = (yield) # this means its a Coroutine function
        if text in book:
            print(f'"{text}" found')
        else:
            print(f'"{text}" not found')

search = searcher()
next(search) # this runs until that while loop
search.send('ok')
print('Going for next')
search.send('okk')
print('Going for next')
search.send('is')
print('Finished')

search.close()



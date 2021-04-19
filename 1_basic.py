# Here we will cover:
# print
# numbers, operators, logical operators, boolean, string
# if-else, for loop, while loop, nested loop
# functions
# input


print('Hello World')
print('Hello World 4', 'Hello World 5', sep=" __ ")
print('Hello World 2', 'Hello World 3 ', 89, 12.856, True, end="   ")
print() # Just print a line break

# Numbers (int, float)
n1, n2, n3 = 45, 68.36, 6 + 4j # int, float, complex number

# Mathmetical Operation
# +  : add
# -  : subtract
# *  : multiply
# /  : divide
# // : divide (retuns only int)
# %  : remainder
# There is a shortcut for using these simply : like:
n1 += 90 # n1 = n1 + 90
n1 /= 5  # n1 = n1 / 5
n1 //= 7 # n1 = n1 // 7
n1 %= 3  # n1 = n1 % 3


# Boolean (bool)
has_permission, done = True, False
ready = not has_permission # not True : False


# String (str, char)
name, father_name = 'Kabir Khan', "Arif Hasan"
qs1, qs2 = "Are you 'Sabbir'?", 'Are you "Kabir"?'
qs1, qs2 = "Are you \"Menna\"?", 'Are you \'Tina\'?' 
qs1, qs2 = '''Are you 'Tina' or "Mena"?''', """Are you 'Rana' or "Opu"?"""

# String formatting
s1 = 'My name is ' + name + f"Sorry, {father_name}!" 
s2 = "{} got + {number} ".format(name, number=n2)

# String functions
print(s1[2:6], s1[:6], s1[2:], s1[2:-2], s1[:-3], s1[-6:], sep=" ___ ")
start_k, end_h = s1.startswith('k'), s1.endswith('h')
s1.find("got")
# s1.index("got")
s1.split(",")
s1.splitlines()
s1.replace('gh', 'ry')
s1.lower()
s1.upper()
s1.title()
s1.strip()  # Remove whitespace from both side
s1.rstrip() # Remove whitespace from right side
s1.lstrip() # Remove whitespace from left side
' >> '.join(['57', '354', '4547', "56456", '576765']) # return string : "57 >> 354 >> 4547 >> 56456 >> 576765"

a = "*" * 5 # a = "*****"
length = len("gfhgtyh") # length of a string

# There is a another thing : None > that means nothing
my_name = None # my_name is not set yet


# conditions
# logical operators : and, or, not
# we have ==, !=, >, <, =>, =< to check conditions
# unlike other language, we can chain them like : 5 < n2 <= 100
if n1 >= 4 and n2 < 4 and s1:
    print('Wow')
elif 5 < n2 <= 100 or 5 < len(s1) <= 25:
    print('Opps')
else:
    print('How')
number1 = 56 if n2 == 0 and not s1 else n2 # if-else comprehension (true_value if conditon else false_value)
# In logics
# ""              : False
# 'anything', " " : True
# 0               : False
# 45, -64.89      : Ture
# empty list, set, dict is also False
a = "hi " and 56    # True
a = True and 0      # False
a = None or 0         # False
a = 475 > 45 or ""  # True


# for loop
for i in 'hfyhty':
    print(i)

for i in 'hfyhty':
    if i == 'y':
        print('y Found')
        break
else:
    # this else works when for loop itearate over all the elements (no break)
    print('y not Found')

for _ in range(5): # when you are not gonna use that variable : name it '_'
    print("*", end="")
print()

# break    : it used to get out of the loop immediately
# continue : it used to get to the next loop immediately

# while loop
i = 2
while i == 5:
    i += 1
    print('*')

# infinite loop
while True:
    if not 4 > 5:
        break

# nested loop
for a in 'abcde':
    if a == 'c':
        continue # if a == 'c' : then the rest part of this loop is ignored and directly go to next loop that is 'd'
    for b in 'ghk':
        print('(', a, ', ', b, ')')


# Type conversation
a = int(34.56)
a = float("34.56")
a = str(4686 + 95)
a, b = bool("hi"), bool("") # True, False


# get input from console
ans1 = input() # get data from console
my_name = input("What is your name : ") # get data from console with qs
age = int(input("Type a age : "))    # get an int


# Functions
def check_odd_number(n):
    # this function return something (bool)
    # if n = 3, then n % 2 = 1, and 1 means True
    # if n = 4, then n % 2 = 0, and 0 means False
    return True if n % 2 else False

def say_hi(name, age, message="Welcome", ignore=False): # with some default value of paramaters
    # this function return nothing / None
    if ignore:
        print("You ignored")
    else:
        print(f'{message} {name}! You are {age}')
    # using if else comprehension
    # print("You ignored" if ignore else f'{message} {name}! You are {age}')

if check_odd_number(43):
    print(43, " is a odd number")

say_hi(my_name, age)                                # here, default value for other 2 params will used
say_hi(my_name, age, "Helo")                        # overriding default values
say_hi(my_name, age, "Helo", True)                  # overriding default values
say_hi(my_name, age, ignore=False, message="Helo")  # if you mismatch the serial, use param's name too
say_hi(my_name, ignore=True, age=age)               # if you mismatch the serial, use param's name too



# scope
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


# some keywords and their work:
pass                    # this do nothing, used in any empty scope
l = len('fdgdfg')       # return the length of any iterable
s = sum(4, 78, 45.89)   # return the sum
unicode_of_a = ord('A') # 65 : Return the Unicode code point for a one-character string
char_of_65 = chr(65)    # 'A' : Return a Unicode string of one character with ordina
type_of_something = type("455") # returns the type of the data : string
del type_of_something   # delete the variable, 'type_of_something' is no longer a valid variable

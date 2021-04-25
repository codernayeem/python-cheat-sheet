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
qs5 = r'Hi, "\" this is backslash.'  # raw string

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
# 'is' is also works like '==', but == : check same value, 'is' : check same object reference
# using 'is' means, need to be same object instance
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
a = None or 0       # False
a = 475 > 45 or ""  # True

a = 56 == 56.0        # True  | '==' only checks value
a = 56 is 56.0        # False | 'is' checks value + objects



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



# some keywords and their work:
pass      # this do nothing, used in any empty scope
del age   # delete the variable, 'parent_name' is no longer a valid variable

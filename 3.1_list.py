# Here we will cover: list

# Defining list
list_of_marks = [56, 89, 45.5, 456, None, 0.0, 46]
list_of_any = ['A', [0, 1], [4, 67, "any"], 54, [], None] # list element can be anything, even an another list
list_of_zero1 = [0] * 5     # returns [0, 0, 0, 0, 0]
list_of_zero2 = [9, 7] * 5  # returns [9, 7, 9, 7, 9, 7, 9, 7, 9, 7]
my_list = list_of_zero1 + list_of_zero2 # returns[0, 0, 0, 0, 0, 9, 7, 9, 7, 9, 7, 9, 7, 9, 7]
list_of_num = list(range(5))        # retuns [0, 1, 2, 3, 4]  : (stop)  : default start = 0
list_of_num = list(range(1, 5))     # retuns [1, 2, 3, 4]     : (start, stop)
list_of_num = list(range(1, 8, 2))  # retuns [1, 3, 5, 7]     : (start, stop, step)
list_of_num = list("Helo World")  # retuns ['H', 'e', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
list_of_num = list({4, 8, 6})  # list from set
list_of_num = list((1, 5,  9, 7, 5))  # list from tuple
# by his way, we can make list from any other iterable

# Accessing Items
print(list_of_num[3]) # 'o'  : the item at index 3
print(list_of_num[-2]) # 'l' : the second item from the end
print(list_of_num[3:6]) # ['o', ' ', 'W'] : return a new list according to the start and stop
print(list_of_num[3:-2]) # ['o', ' ', 'W', 'o', 'r'] : return a new list according to the start and stop
print(list_of_num[:-2]) # ['H', 'e', 'l', 'o', ' ', 'W', 'o', 'r']
print(list_of_num[3:]) # ['o', ' ', 'W', 'o', 'r', 'l', 'd']
print(list_of_num[3::2]) # ['o', 'W', 'r', 'd']  :  extra 2 represent step
print(list_of_num[::-1]) # ['d', 'l', 'r', 'o', 'W', ' ', 'o', 'l', 'e', 'H']  :  minus makes reverse and 1 is step

# Same way for modifying
list_of_num[3] = 'gyu'
list_of_num[-2] = 45
list_of_num[3:6] = ['oo', '_', None]


# list unpacking & packing
my_list = [45, 67, 90]
my_list2 = [45, 67, 90, 65, 93, 15, 68]
# Bad way :
first = my_list[0]
second = my_list[1]
third = my_list[2]
# Better way
first, second, third = my_list # remember : the number of element and variable should be same
first, second, *other_num = my_list2 # after putting first and second, python put all other elements in other_num
first, second, *other_num, the_last = my_list2 # just like the previous, but set the last item to the_last


# looping through list
lst = ['Nayeem', 'Robin', 'Rabbi', 'Fahim', 'Arif', 'Rokib']

for name in lst: # looping through just the item
    print(name)

for index, name in enumerate(lst): # looping through the index and name
    print(index, name)


# Add & Remove items
lst.append("Kawser") # add the item at the end
lst.insert(2, "Faruk") # add the item at index 2
lst.pop() # remove the last element from the list and retuns that element
lst.pop(2) # remove the element of index 2 from the list and retuns that element
lst.remove("Fahim") # remove the "Fahim" element the list
del lst[:2] # deleting a range of items


# Finding item
lst = ['Nayeem', 'Robin', 'Rabbi', 'Fahim', 'Arif', 'Rokib']
index = lst.index("Rabbi") # returns the index of "Rabbi" element 
# index = lst.index("Kabir")
# but "Kabir" is not in the list. That case :
if "Kabir" in lst:
    index = lst.index("Kabir")
count = lst.count("Nayeem") # returns how much "Nayeem" element is in in the list


# sorting lsit
lst1 = ['Nayeem', 'Robin', 'Rabbi', 'Fahim', 'Arif', 'Rokib']
lst2 = [95, 36, 96, 15, 3, 78, 9, 99, 16, 36]

# These function sort the list
lst1.sort() # ['Arif', 'Fahim', 'Nayeem', 'Rabbi', 'Robin', 'Rokib']
lst2.sort(reverse=True) # [99, 96, 95, 78, 36, 36, 16, 15, 9, 3]

# These function returns the sorted list
new_list1 = sorted(lst1, reverse=True) # ['Rokib', 'Robin', 'Rabbi', 'Nayeem', 'Fahim', 'Arif']
new_list2 = sorted(lst2) # [3, 9, 15, 16, 36, 36, 78, 95, 96, 99]

# both sort and sorted functions have same things like: key, reverse

# These were simple list. When thing gets complex for sorting:
lst = [
    ["Apple", 280],
    ["Nango", 120],
    ["Orange", 300],
    ["Berry", 180],
]

def get_name(item):
    return item[0]
def get_price(item):
    return item[1]

lst.sort(key=get_name)  # sort the list accordingly to the fruit name
lst.sort(key=get_price) # sort the list accordingly to the fruit price
# without using extra function (using lamda function):
lst.sort(key=lambda item: item[0])  # sort the list accordingly to the fruit name
lst.sort(key=lambda item: item[1])  # sort the list accordingly to the fruit price


# reverse
lst1.reverse()               # reverse elements in lst1
new_lst1 = reversed(lst1)    # returns a new list reversing elements of lst1

# map, filter
prices = list(map(lambda item: item[1], lst)) # get the list of prices
less_than_200 = list(filter(lambda item: item[1] < 200, lst)) # get the list of product with less than 200 price

# list comprehension
prices = [item[1] for item in lst]  # same as map function
less_than_200 = [item for item in lst if item[1] < 200] # same as filter function
less_than_200_only_name_lowercase = [item[0].lower() for item in lst if item[1] < 200] # we can do both map and filter here
print(less_than_200_only_name_lowercase)

# zip
list1 = [1, 5, 6]
list2 = [6, 8, 3]
print(list(zip(list1, list2))) # [(1, 6), (5, 8), (6, 3)]
# zip function makes tuples. That tuple contains same posioned value of given lists or any iterables


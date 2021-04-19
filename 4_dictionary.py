# Dictionary
# a collection of data with key


# define dictionary
# key   : can be string / number / bool etc
# value : can be any thing
data = {
    'name': "Nayeem",
    'age': 18,
    12.45: "Some",
    "list1": ['helo', 'world', 'Hi'],
    "data_go": {
        'key': 'value',
        'key2': 'value2',
    },
}
data = dict(name="Nayeem", roll=347, age=18)


# Access and modify data
data['name'] = "Robin"
print(data['name'])          # if 'name' key not found, it throw error
# solution 1
if 'name2' in data:
    print(data['name2'])
# solution 1
print(data.get('name'))      # if 'name' key not found, it return None
print(data.get('name', ''))  # if 'name' key not found, it return ''

data.pop('name')             # delete that item from dict and returns the value
del data['roll']             # delete an item (key: value)


# Looping through dict
data = {'name': 'Rabbi', 'age': 20, 'salary': 12000, 'subject': 'Math'}
for key in data:
    print(key, data[key])

for item in data.items():
    print(item[0], item[1])

for key, value in data.items():
    print(key, value)


# Some methods:
data.keys()   # returns all keys
data.values() # returns all values
data.clear()  # delete all items


# Dictionary Comprehension
marks = {'Rabbi': 250, 'Fahim': 180, 'Faruk': 220, 'Sami': 290}
marks_in_100 = {}
for key, value in marks.items():
    marks_in_100[key.lower()] = value // 3
print(marks_in_100)
# For achieving the same result :
marks_in_100 = {key.lower() : value // 3 for key, value in marks.items()}
print(marks_in_100)
marks_in_100 = {key.lower() : value // 3 for key, value in marks.items() if key != 'Faruk'} # with condition
print(marks_in_100)

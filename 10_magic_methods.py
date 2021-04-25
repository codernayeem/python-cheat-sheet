# Details : https://rszalski.github.io/magicmethods/

# __init__(), __str__() etc. are magic functions
# magic methods starts and ends with __.
# There is many more magic methods :

class Point:
    def __init__(self, x=0, y=0, z=0):
        # Construct the object
        self.x = x
        self.y = y
        self.z = z

    # Represet the object, There are more like : __format__(), __nonzero_(_, __sizeof__()
    def __str__(self):
        # printing object / making string, call this function
        return f"Point({self.x}, {self.y}, {self.z})"
    
    def __repr__(self):
        # called when using repr()
        # called when printing object / making string, when __str__() not 
        # as a alternative of __str__()
        return f"Point({self.x}, {self.y}, {self.z})"

    
    # Comparison magic methods
    def __eq__(self, other):
        # Defines behavior for the equality operator, ==
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other):
        # Defines behavior for the inequality  operator, !=
        return not self.__eq__(other)

    def __lt__(self, other):
        # Defines behavior for the less-than operator, <
        return self.x < other.x and self.y < other.y and self.z < other.z

    def __gt__(self, other):
        # Defines behavior for the greater-than operator, >
        return self.x > other.x and self.y > other.y and self.z > other.z

    def __le__(self, other):
        # Defines behavior for the less-than-or-equal-to operator, <=
        return self.x <= other.x and self.y <= other.y and self.z <= other.z
    
    def __ge__(self, other):
        # Defines behavior for the greater-than-or-equal-to operator, >=
        return self.x >= other.x and self.y >= other.y and self.z >= other.z


    # Normal arithmetic operators
    def __add__(self, other):
        # Defines behavior for the addition, +
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        # Defines behavior for the subtraction, -
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        # Defines behavior for the multiplication, *
        return Point(self.x * other.x, self.y * other.y, self.z * other.z)

    def __floordiv__(self, other):
        # Defines behavior for the integer division using the // operator
        return Point(self.x // other.x, self.y // other.y, self.z // other.z)

    def __div__(self, other):
        # Defines behavior for the division using the / operator
        return Point(self.x / other.x, self.y / other.y, self.z + other.z)

    def __mod__(self, other):
        # Defines behavior for the modulo using the % operator
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __pow__(self, other):
        # Defines behavior for the exponents using the ** operator
        return Point(self.x ** other.x, self.y ** other.y, self.z ** other.z)

    def __lshift__(self, other):
        # Defines behavior for the left bitwise shift using the << operator
        return Point(0, 0, 0) # anything

    def __rshift__(self, other):
        # Defines behavior for the right bitwise shift using the >> operator
        return Point(0, 0, 0) # anything

    def __and__(self, other):
        # Defines behavior for the bitwise and using the & operator
        return Point(0, 0, 0) # anything

    def __or__(self, other):
        # Defines behavior for the bitwise or using the | operator
        return Point(0, 0, 0) # anything

    def __xor__(self, other):
        # Defines behavior for the bitwise xor using the ^ operator
        return Point(0, 0, 0) # anything
    # there is more like that and aslo for reflected arithmetic operators too, that case functions name start with 'r' like: __radd__()
    # i = self + other  ||| Reflected : i = other + self

point1 = Point(4, 5, 9)
point2 = Point(6, 2, 3)
point3 = point1 + point2
print(point3)


# Magic methods for a Container
class TagCloud:
    __tags = {} # private variable
    # to make a variable / method private, just set a prefix with __.

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __len__(self):
        # Returns the length of the container when using len()
        return len(self.__tags)

    def __getitem__(self, tag):
        # Defines behavior for when an item is accessed, using the notation self[key]
        # We can also raise exception or do anything if the key is wrong, in this case : return 0
        return self.__tags.get(tag.lower(), 0)
    
    def __setitem__(self, tag, count):
        # Defines behavior for when an item is assigned to, using the notation self[key] = value
        self.__tags[tag.lower()] = count
    
    def __delitem__(self, tag):
        # Defines behavior for when an item is deleted (e.g. del self[key])
        del self.__tags[tag.lower()]
    
    def __iter__(self):
        # Should return an iterator for the container, that can be used in for loop or anywhere
        return iter(self.__tags) # iter() is a buit-in function to make iterable
    
    def __reversed__(self):
        # Called to implement behavior for the reversed() built in function
        pass
    
    def __contains__(self, tag):
        # Defines behavior for membership tests using in and not in
        return tag in self.__tags.keys()
    
    def __missing__(self, tag):
        # __missing__ is used in subclasses of dict. It defines behavior for whenever a key is accessed that does not exist in a dictionary
        pass


all_tags = TagCloud()
all_tags.add("python")
all_tags.add("Python")
all_tags.add("PyThon")
all_tags.add("Java")
print(all_tags["PYTHoN"]) # 3
all_tags["JAVA"] = 5
print(len(all_tags)) # 2 : python, java
del all_tags['java']
print(all_tags["JAVA"]) # 0



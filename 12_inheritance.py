# *** Inheritance ***

class Animal:
    def __init__(self):
        print("Animal class init")
    
    def eat(self):
        print('Eating')
    
class Bird(Animal):
    def __init__(self): # override base calss __init__() method
        print("Bird class init")

    def fly(self):
        print("Fly")

class Fish(Animal):
    def __init__(self):  # override base calss __init__() method
        super().__init__()  # calling base calss __init__() method
        print("Fish class init")

    def swim(self):
        print("Swim")

sparow = Bird()
sparow.eat()


# The Animal class is the blueprint for creating Bird and Fish subclasses
# The Animal class is inherited from a another class called object
# From that object, all magic method comes
# We could write it too : class Animal(object):

# checking instance and subclass
isinstance(sparow, Bird)   # True
isinstance(sparow, Animal) # True
isinstance(sparow, object) # True
isinstance(sparow, Fish)   # False

issubclass(Bird, Animal)   # True
issubclass(Fish, Animal)   # True
issubclass(Bird, object)   # True
issubclass(Bird, Fish)     # False


# *** Multilevel Inheritance ***
class Ilish(Fish):
    pass
# here, the inheritance tree: object -> Animal -> Fish -> Ilish
# this is called Multilevel-Inheritance
# more than 2-3 Multilevel-inheritance can fall you to trouble, carefull


# *** Multiple Inheritance ***
class Flyer:
    def fly(self):
        pass

class Swimmer:
    def swim(self):
        pass

class FlyingFish(Swimmer, Flyer):
    pass

# In that case, FlyingFish will have all things of Swimmer and Flyer
# If Swimmer and Flyer has any common attributes/methods:
# then it will look for the first Base class, if that attributes/methods not found, then the other one 
# so, the order of Base class will matter if they have any common things


# Another Example
class InvalidOperationError(Exception): # creating custom error using inheritance
    pass

class Stream:
    def __init__(self):
        self.opened = False
    
    def open(self):
        if self.opened:
            raise InvalidOperationError("Already Opened")
        self.opened = True
    
    def close(self):
        if not self.opened:
            raise InvalidOperationError("Already Closed")
        self.opened = False

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a file")


# *** Abstract Base Class ***
# We can say in the last example:
# stream = Stream()
# stream.open()
# here, which one will open? so, we should not create a instance of Stream (Base class)
# also, both subclass has read() func. That is common and must, right?
# So, There comes Abstract Base Class (ABC)

from abc import ABC, abstractmethod

class Stream2(ABC):
    def __init__(self):
        self.opened = False

    @abstractmethod # by using it, we tell to the subclass to override this read method must
    def read(self):
        pass
    
    def open(self):
        if self.opened:
            raise InvalidOperationError("Already Opened")
        self.opened = True
    
    def close(self):
        if not self.opened:
            raise InvalidOperationError("Already Closed")
        self.opened = False

# Now, you can not create a instance of Stream2
# And, all the subclass of Stream2 needs to implement read method, like:

class FileStream2(Stream2):
    def read(self):
        print("Reading data from a file")

class MemoryStream(Stream2):
    def read(self):
        print("Reading data from a memory")

stream = MemoryStream()
stream.read()

# if the subclass has no read method, then that subclass will also be considerd as a abstract class, like:
class SsdStream(Stream2):
    pass
# this is also a abstract class and you can not create a instance of SsdStream class



# *** Extending Built-in types ***

class Text(str): # inherit all things from str
    def duplicate(self):
        return self + self
    
text = Text("Python")
print(text.lower())      # methods from str
print(text.duplicate())  # methods from Text

class SumNum(list):            # inherit all things from list
    def append(self, x, y):    # override the append func of of base class (list)
        print("Append called")
        super().append(x + y)  # call the append func of base class (list)
    
a_list = SumNum()
a_list.append(5, 9)
a_list.append(4, 16)
a_list.append(78, 16)
print(a_list)



# *** Data Classes ***
# Data Class = Those class, which has only data and no methods

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
point1 = Point(3, 6)
point2 = Point(3, 6)
print(point1 == point2) # True

# Instead of this code avobe, we can use data classes
from collections import namedtuple

Point2 = namedtuple("Point2", ['x', 'y'])
p1 = Point2(x=6, y=9)
p2 = Point2(x=6, y=9)
print(p1 == p2) # True
print(p1.x)     # 6

# here, this instance is immutable / not editable
# that means, we can not do : p1.x = 46
# that case, you need to create a new instance of Point2 with x=46

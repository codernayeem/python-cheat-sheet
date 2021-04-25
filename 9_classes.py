# Class: bluprint for creating new objects
# Object: instance of a class

# Class: Person
# Object: Nayeem, Robin, Faruk

class Point:
    x, y = 0, 0

    def draw(self):
        print(self.x, self.y)

    def distance(self):
        return self.x - self.y
    
    def print_distance(self):
        print("Distance:", self.distance())

point = Point()  # object
point.x = 5
point.y = 5
point.draw()
point.print_distance()
    
print(type(point)) # <class '__main__.Point'>

# checking instance
print(isinstance(point, Point)) # True
print(isinstance(point, int))   # False



class PointClass:
    # class variable
    color = "Red"
    apply_time = 5

    # constructor
    def __init__(self, x=0, y=0):
        # instance variable
        self.x = x
        self.y = y

    def draw(self):
        print(self.x, self.y)
    
    
    # this method change a instance variable
    def change_color1(self, color):
        self.color = color # this create a new instance variable

    # this method change a class variable
    @classmethod
    def change_color2(cls, color):
        cls.color = color  # this change class instance variable


point = PointClass(4, 5)
print(point.color) # printing class variable

# point.color = "Blue"
# print(point.color) # printing instance variable

# PointClass.color = "Black" # changing class variable
point.change_color2('Yelow') # changing class variable
print(point.color)  # printing class variable





class Employee:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = int(age)

    # returns instance by reading given string (Alternative constructor)
    @classmethod
    def from_dash(cls, data):
        return cls(*data.split('-'))
    
# using default constructor
roni = Employee('Roni', 50)

# using class method
sami = Employee.from_dash('Sami-35')

# use classmethod, when no need of instance variable, needed class variable




class Coder:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def print_hi():
        print('Welcome')

    @staticmethod
    def calculate(a, b):
        return a * b

# use staticmethod, when don't need any class/instance variables
# when you don't need self/cls ...

# calling from instance
roni = Coder('Roni')
roni.print_hi()

# calling from class
print(Coder.calculate(5, 9))



# public variable/functons    : name
# protected variable/functons : _name
# private variable/functons   : __name

# public    : use anywhere
# protected : use in base and sub class
# private   : use only in base class


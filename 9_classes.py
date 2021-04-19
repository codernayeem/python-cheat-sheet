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
    color = "Red"
    # constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def draw(self):
        print(self.x, self.y)


point = PointClass(4, 5)
point.draw()
PointClass.color = "Black" # this change will apply to all objects
print(point.color)
point.color = "Blue" # this change will apply to this object only
print(point.color)
point.z = 4       # we can also create new variables on that object
print(point.z)


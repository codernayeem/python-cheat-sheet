# Setting property
# property is like attributes, but you can control how to get, set, del that
class Product:
    def __init__(self, price):
        self.set_price(price)
    
    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = price

    price = property(get_price, set_price)


product = Product(50)
product.price = -50 # this will raise exception



# Using decorator
class Product2:
    def __init__(self, price):
        self.price = price
    
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = price

product2 = Product2(50)
product2.price = -50 # this will raise exception

# in case, if the setter is not declared, then it will be read only
# then you can not do that : product2.price = 50


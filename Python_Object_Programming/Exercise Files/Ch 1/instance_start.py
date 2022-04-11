# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret 
    # TODO: create instance methods
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount

# TODO: create some book instances
b1 = Book("War and Peace", "SK", 5000, 20.25)
b2 = Book("The Catcher in the Rye", "Steph King", 100, 10.50)

# TODO: print the price of book1
print(b1.getprice())

# TODO: try setting the discount
print(b2.getprice())
b2.setdiscount(.25)
print(b2.getprice())

# TODO: properties with double underscores are hidden by the interpreter

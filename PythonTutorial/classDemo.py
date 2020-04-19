class car:
    # class variable
    wheels = 4

    # this is constructor of this class
    def __init__(self, color):
        print("car class constructor")
        self.color = color

    # this is a function/method
    def test(self):
        print("test method")

    # any variable is declared inside function or constructor is called instance variables .i.e price is instance variable
    def setprice(self, price):
        self.price = price

    def getprice(self):
        return self.price


# how to create the object of class

c1 = car("Black")
c1.setprice(1000)
print(c1.getprice())

c2 = car("Red")
c2.setprice(2000)
print(c2.getprice())

c1.test()
print(c1.wheels)

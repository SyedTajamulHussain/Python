# object printing concept
class test:

# this is a constructor
    def __init__(self,x,y):
        self.x=x
        self.y=y

# rept and str are two methods
    def __repr__(self):
       return "a:%s and b:%s" % (self.x,self.y)
    # str method, if there is no str method it will take repr method and if str is present it will bypass repr method.
    def __str__(self):
       return "Value of a is %s and b is %s" %(self.x,self.y)

t= test(10,20)
print(t)


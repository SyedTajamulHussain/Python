#Passing arguments in key value pair in function
def login(username,Password):
    print(username,Password)

   #Calling the login function
login("Tajamul123","passwd")
login(username="tango" ,Password="charle")

# *agr (Single star agr)

def getmarks(*arg):
    for x in arg:
        print(x)

getmarks(10,20,30,40,50)
#**agrs (two stat argument)
def getstudentMarks(**agrs):
    for x, y in agrs.items():
        print("%s == %s" %(x,y))

getstudentMarks (tajamul = 10, zahid =20)

#Lambda function , also called annonymous function
#this is a function without any name

cube= lambda x: x*x*x
print(cube(4))

# other example of lambda
totalMarks=lambda marks: marks +10
print(totalMarks(90))


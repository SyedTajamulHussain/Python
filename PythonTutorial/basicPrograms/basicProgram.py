import sys

print(sys.version)

if 5 > 2:
    print("five is greate then 2")

# python variable -  A variable is created the moment you first assign a value to it.

x = 5
y = "Address"
print(x)
print(y)
# Variables do not need to be declared with any particular type, and can even change type after they have been set.
x = 4  # x is of type int
x = "Sally"  # x is now of type str
print(x)

# casting
# If you want to specify the data type of variable, this can be done with casting.

x = str(3)  # x will be '3'
y = int(2)  # y will be 3
z = float(3)  # z will be 3.0
print(x, y, z)

# Get the Type
# You can get the data type of variable with the type() function.
x = 5
y = "Tajamul"
Z = 5.0
print(type(x))
print(type(y))
print(type(z))

# String variables can be declared either by using single or double quotes:
x = "John"
# is the same as
x = 'John'

# Case-Sensitive
# Variable names are case-sensitive.
a = 4
A = "Sally"
# A will not overwrite a .this is creating two variables.
print(a)
print(A)

# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:
name, age, phoneNo = "Syed", 42, 9971113356
print(name)
print(age)
print(phoneNo)
# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
# Global Variables
#  that are created outside of a function (as in all of the examples above) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.

x = "syed Tajamul"


def my_name():
    print("My name is " + x)


my_name()

# Data Type
string = str("Hello sir welocome to python world")
print(string)

integer = int(20)
print(integer)

Float = float(3.5)
print(Float)

Complex = complex(1J)
print(Complex)

List = list(("Orange", "Apple", "Banana", "Kiwi"))
List.reverse()
print(List)
List.sort()
print(List)
List.insert(0, "Zebra")
print(List)

Tuple = tuple(("apple", "banana", "cherry"))
print(Tuple)

Range = range(6)
print(Range)

Dict = dict(Name="John", age=36)
print(Dict)

SET = {"apple", "banana", "cherry"}
print(SET)

Frozenset = frozenset(("apple", "banana", "cherry"))
print(Frozenset)


#Casting
xa = int(1)   # x will be 1
ya = int(2.8) # y will be 2
za = int("3") # z will be 3
print(xa)
print(ya)
print(za)

#Strings are Arrays

MyAddress = "syedManzil shalimar srinager kashmir 190025"
print(MyAddress[0])
#Looping Through a String
for x in MyAddress:
    print(x)

#String Length
print(len(MyAddress))

#Check String
print("shalimar" in MyAddress)

#Use it in an if statement:

if "shalimar" in MyAddress:
    print("hurry text match")
else:
    print("Alas, text does not match")

#Check if NOT in string

print("shalimar" not in MyAddress)
#Slicing Strings
print(MyAddress[1:4])
print(MyAddress[:4])
print(MyAddress[4:])
#Modify Strings
print(MyAddress.upper())
print(MyAddress.lower())
#Remove Whitespace
print(MyAddress.strip())
#Split String
split ="syed-tajamul"
print(split)
print(split.split("-"))
#Format - Strings
age = 36
txt = "My name is John, I am {}"
print(txt.format(age))

#2nd expample

Class = 1
grade = 'A'
RollNo = 20.1
Name = "Haadiya"
Detail = "My Name is {} , I study in class {} Grade {} .My rollno is {}"
print(Detail.format(Name,Class,grade,RollNo))
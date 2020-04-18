def test():
    print("this is my first program")


test()


def sum(a):
    print(a + 10)


sum(10)


def getcountryname(name="USA"):
    print(name)


getcountryname()
getcountryname("india")


# Passing list in function
def getNames(list):
    for x in list:
        print(x)


names = ["JAVA", "Phython", "dot net", "c sharp"]
getNames(names)


# function with return

def sum(a, b):
    c = a + b
    return c


total = sum(10, 20)
print(total)


def getCapitalname(countryName):
    if countryName == "India":
        return "New Delhi"
    elif countryName == "USA":
        return "Washington DC"


print(getCapitalname("India"))

def launchBrowder(BrowserName):
    if BrowserName == "Chrome":
        print("Chrome Launched")
    elif BrowserName == "FireFox":
        print("FireFox is launched")
    else:
        print("Browser not defined")

launchBrowder("FireFox")

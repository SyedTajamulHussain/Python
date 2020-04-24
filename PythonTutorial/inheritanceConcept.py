class Person():

    def __init__(self, name):
        self.name = name

    def getname(self):
        return self.name

    def isemployee(self):
        return False

 # inheriting the person class
class employee(Person):

    def isemployee(self):
        return True

    emp = Person("Tajamul")
    print(emp.name)
    print(emp.getname(), emp.isemployee())


emp1 = employee("Zahid")
print(emp1.name)
print(emp1.getname(), emp1.isemployee())

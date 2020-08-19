# __str__ : Executes Automatically when you print reference variable
#If we do not pass any value to __str__, by default it will return object memory.
#We cannot return int or float values using __str__

class Emp:
    def __init__(self, eid, ename, sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal

    def __str__(self):
        return ("Employee id:{}  Employee name:{}  Salary:{}".format(self.eid, self.ename, self.sal))

e = Emp(101, "Shreyas", 30000.50)
print(e)    #__str__ is invoked without calling when we want to print the reference variable values

#__del__
#Automatically invoked when we want to destroy the object reference variable.

class MyClass:
    def __del__(self):
        print("Destroyed")

z = MyClass()
z1 = MyClass()

del z
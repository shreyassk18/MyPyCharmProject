#Super() method can be used to:
#   1. Invoke parent class methods
#   2. Invoke parent class variables
#   3. Invoke parent class constructor

#Invoke parent class methods
class A:
    def m1(self):
        print("This is m1 method from parent class")

class B(A):
    def m2(self):
        print("This is m2 method from child class")
        super().m1()    #calling parent class method in child class using super()

b = B()
b.m2()

#Invoke parent class variables
#we can use super() method for calling variables, when we have same name variable for both class,
#If variable names are different for both class, we can call them using self keyword

class C:
    a,b=10,20

class D(C):
    a,b=100,200
    def add(self):
        print(self.a+self.b)
        print(super().a+super().b)  #Calling parent class variables in child class

d = D()
d.add()

#Invoke parent class constructor
#When we do not have constructor defined for child class, by default object will invoke parent class constructor,
#But when we have constructor present in child class also, we need to use super() method to invoke parent method

class E:
    def __init__(self):
        print("This is the constructor from parent class")

class F(E):
    def __init__(self):
        print("This is the constructor from child class")
        super().__init__()  #calls parent class constructor
        #E.__init__(self)    #Another way to invoke parent class constructor

f = F()
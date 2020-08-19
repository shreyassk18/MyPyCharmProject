#classes can inherit functionality of other classes
#If an object is created using a class that inherits from a super class, then object will have methods of both class and super class
#The same holds true for variables.



#5. Hybrid - Combination of multiple and hierarchical

class A:
    def m1(self):
        print("This is a method from parents class")

class B(A):
    def m2(self):
        print("This is a method from child class")

a = A()
a.m1()
#a.m2() #This will throw attribute error

b = B()
b.m1()
b.m2()
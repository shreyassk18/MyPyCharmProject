#If we have n number of methods in an abstract class, then we must implement all n number of methods in subclass,
#If we do not implement all n methods in sub class, then that sub class will also be treated as abstract class,
#Means we cannot create object for that sub class also.
#We can either implement all n methods in one subclass and create object for that sub class,
#Or we can create multiple subclasses by inheriting all sub classes and implement those n abstract method and create an object for last sub-class.

from abc import ABC,abstractclassmethod

class A(ABC):

    @abstractclassmethod
    def m1(self):
        pass

    @abstractclassmethod
    def m2(self):
        pass

class B(A):
    def m1(self):
        print("This is m1 method")

#b = B()
#b.m1()  #this will throw an error (TypeError: Can't instantiate abstract class B with abstract methods m2)

class C(B):
    def m2(self):
        print("This is m2 method")

c = C()
c.m1()
c.m2()
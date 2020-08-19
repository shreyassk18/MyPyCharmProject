#Abstract classes are classes which contains one or more abstract methods
#An abstract method is a method that is declared, but contains no implementation.
#Abstract classes must have sub-classes to implement abstract methods.
#We cannot create objects for abstract class, we can create a object for sub-class of abstract class
#These classes are useful when you know the requirement part and does not have clue with implementation.
#Abstract concept can be used to secure methods.


#ABC is a pre-defined abstract class in python
#We have to use ABC class to define a abstract class in python

from abc import ABC,abstractclassmethod

class A(ABC):       #Class A is an abstract class

    @abstractclassmethod
    def display(self):  #Abstract method
        None

class B(A):
    def display(self):
        print("This is a abstarct class example")

b = B()
b.display()

#Below statement will throw an error as we cannot create object for abstract method
#TypeError: Can't instantiate abstract class A with abstract methods display

#a = A()
#a.display()

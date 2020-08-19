#In OOPs concept, we can restrict the access to methods and variables, which is called encapsulation
#Encapsulation can be achieved using private methods and private variables

#public methods can be accessible from anywhere.
#private methods can be accessible only in their own class starts with two underscores.
#Same goes with variables.

#private variable
class MyClass:
    __a=10  #private variables starts with two preceeding underscores
    def display(self):
        print(self.__a)

mc = MyClass()
mc.display()


#If you try to access the variable "a" outside of the class,
#print(MyClass.__a)  #AttributeError: type object 'MyClass' has no attribute '__a' , We cannot access this variable as it is private


#private method

class MyClass1:
    def __display1(self):
        print("This is display1 method")

    def display2(self):
        print("This is display2 method")    #As we cannot call private method outside the class, we need to create one more method to call that method.
        self.__display1()   #We need to specify self keyword to call methods and variables of a class   (This is called inner function in python)

mc1=MyClass1()
#mc1.__display1()    #AttributeError: 'MyClass1' object has no attribute '__display1'    we cannot call private method directly outside the class
mc1.display2()
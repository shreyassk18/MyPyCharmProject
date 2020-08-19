#class is a logical entity which contains logic
#class contains variables and methods
#logic should be included within a method

#An object is a physical entity created for a class
#We can create any number of objects for a class

#Function is something which is created without or outside of a class
#Method is something which is created within a class

class MyClass:
    def myFunc(self):
        pass
    def display(self,name):
        print("Name is :", name)

mc = MyClass()  #MyClass is an object and mc is a refence variable for the object(object reference)
mc.myFunc()
mc.display("Shreyas")

